#!/usr/bin/env python3
"""
Ambient AI Screen Monitor - Analysis Engine & Report Generator
Processes the week's screenshots with a vision LLM and writes a Markdown report.
"""

import os
import sys
import base64
import logging
import argparse
from datetime import datetime, timedelta
from pathlib import Path

import anthropic
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

# --- Configuration ---
SCREENSHOTS_DIR = Path(os.getenv("SCREENSHOTS_DIR", Path.home() / ".ambient_monitor" / "screenshots"))
REPORTS_DIR     = Path(os.getenv("REPORTS_DIR",     Path.home() / ".ambient_monitor" / "reports"))
MODEL           = os.getenv("CLAUDE_MODEL", "claude-opus-4-8")   # vision-capable
MAX_IMAGES_PER_BATCH = int(os.getenv("MAX_IMAGES_PER_BATCH", 20))  # stay within context limits
DELETE_AFTER_ANALYSIS = os.getenv("DELETE_AFTER_ANALYSIS", "true").lower() == "true"
MAX_IMAGE_DIMENSION  = 1024  # pixels — shrink before sending to save tokens

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [analyze] %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(Path.home() / ".ambient_monitor" / "analyze.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def encode_image(path: Path) -> tuple[str, str]:
    """Return (base64_data, media_type) for a screenshot, resized if needed."""
    with Image.open(path) as img:
        img = img.convert("RGB")
        w, h = img.size
        if max(w, h) > MAX_IMAGE_DIMENSION:
            scale = MAX_IMAGE_DIMENSION / max(w, h)
            img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=75)
        return base64.standard_b64encode(buf.getvalue()).decode(), "image/jpeg"


def collect_screenshots(since: datetime | None = None) -> list[Path]:
    """Return sorted screenshot paths, optionally filtered to the past week."""
    if not SCREENSHOTS_DIR.exists():
        return []
    paths = sorted(SCREENSHOTS_DIR.glob("*.png"))
    if since:
        paths = [p for p in paths if datetime.fromtimestamp(p.stat().st_mtime) >= since]
    return paths


def chunk(lst: list, size: int):
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


# ---------------------------------------------------------------------------
# Vision Analysis
# ---------------------------------------------------------------------------

BATCH_SYSTEM_PROMPT = """You are a productivity analyst reviewing a series of screenshots from a professional's computer.
The user is Brad Cartier, Fractional CMO of Small Living Company (SLC), which focuses on attainable/small-unit housing,
veterans housing, and grant-funded community development projects (e.g., Hammond Hill).

For each batch of screenshots, extract STRUCTURED observations:
1. **Applications & Tools Used** — list each app/website visible, rough frequency.
2. **Tasks & Activities** — what is the user actively doing (writing, reviewing, calling, spreadsheet work, etc.)?
3. **Recurring Patterns** — any task that appears in multiple frames suggesting repetition.
4. **SLC-Specific Work** — any visible work related to Small Living Company, Hammond Hill, veterans housing, grant applications, or marketing campaigns.
5. **Manual / Low-Leverage Work** — tasks that look manual, tedious, or ripe for automation.

Be concise and factual. Output valid JSON with keys:
  apps, tasks, patterns, slc_work, manual_work
"""

SYNTHESIS_SYSTEM_PROMPT = """You are a senior productivity and AI-adoption consultant.
You have received structured observations from a full week of screen activity for Brad Cartier,
Fractional CMO of Small Living Company (SLC).

Write a detailed Weekly Productivity Audit Report in Markdown with these sections:

# Weekly Productivity Audit — {week_label}

## 1. Executive Summary
2-3 sentences on the overall shape of the week.

## 2. Activity Breakdown
A table or bulleted breakdown of time spent by category (estimated from frequency of observations).

## 3. Delegation Opportunities
Specific tasks Brad could turn into SOPs and hand off to a VA, team member, or AI agent.
For each, include: Task | Effort saved | Suggested owner/tool

## 4. Workflow Bottlenecks
Areas where manual effort is slowing things down. Be specific — reference what was observed.

## 5. AI Tool Recommendations
For each high-frequency or high-effort task, recommend a specific AI tool, prompt template, or automation.
Format: **Task** → Recommended tool/approach + one-sentence rationale.

## 6. SLC-Specific Acceleration
Tailored suggestions for Hammond Hill, veterans housing, grant applications, or marketing work observed.

## 7. Quick Wins (This Week)
3-5 immediate actions Brad can take in the next 48 hours to reclaim time.

Be specific, actionable, and ruthlessly practical. Avoid generic advice.
"""


def analyze_batch(client: anthropic.Anthropic, paths: list[Path], batch_num: int) -> str:
    log.info("Analyzing batch %d (%d images)…", batch_num, len(paths))

    content = [{"type": "text", "text": f"Batch {batch_num} — {len(paths)} screenshots taken throughout the work week. Analyze each carefully."}]
    for p in paths:
        b64, mime = encode_image(p)
        content.append({
            "type": "image",
            "source": {"type": "base64", "media_type": mime, "data": b64},
        })

    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system=BATCH_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": content}],
    )
    return response.content[0].text


def synthesize_report(client: anthropic.Anthropic, batch_observations: list[str], week_label: str) -> str:
    log.info("Synthesizing final report from %d batch observations…", len(batch_observations))

    combined = "\n\n---\n\n".join(
        f"**Batch {i+1} Observations:**\n{obs}" for i, obs in enumerate(batch_observations)
    )

    system = SYNTHESIS_SYSTEM_PROMPT.replace("{week_label}", week_label)
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": f"Here are all the batch observations from this week:\n\n{combined}"}],
    )
    return response.content[0].text


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def run_analysis(days_back: int = 7, dry_run: bool = False):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        log.error("ANTHROPIC_API_KEY not set in environment / .env file.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    since = datetime.now() - timedelta(days=days_back)
    screenshots = collect_screenshots(since=since)

    if not screenshots:
        log.warning("No screenshots found in %s for the past %d days.", SCREENSHOTS_DIR, days_back)
        sys.exit(0)

    log.info("Found %d screenshots to process.", len(screenshots))

    if dry_run:
        log.info("Dry run — skipping API calls.")
        return

    # Batch analysis
    observations: list[str] = []
    for i, batch in enumerate(chunk(screenshots, MAX_IMAGES_PER_BATCH), start=1):
        obs = analyze_batch(client, batch, i)
        observations.append(obs)
        log.info("Batch %d complete.", i)

    # Synthesis
    week_start = since.strftime("%b %d")
    week_end   = datetime.now().strftime("%b %d, %Y")
    week_label = f"{week_start} – {week_end}"
    report_md  = synthesize_report(client, observations, week_label)

    # Save report
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = REPORTS_DIR / f"productivity_report_{ts}.md"
    report_path.write_text(report_md, encoding="utf-8")
    log.info("Report saved → %s", report_path)
    print(f"\n{'='*60}\nReport saved to:\n  {report_path}\n{'='*60}\n")

    # Cleanup raw screenshots
    if DELETE_AFTER_ANALYSIS:
        for p in screenshots:
            p.unlink(missing_ok=True)
        log.info("Deleted %d raw screenshots.", len(screenshots))

    return report_path


def main():
    parser = argparse.ArgumentParser(description="Ambient AI Screen Monitor — analysis & report generator")
    parser.add_argument("--days", type=int, default=7, help="How many past days to analyze (default: 7)")
    parser.add_argument("--dry-run", action="store_true", help="Collect screenshots list without calling API")
    parser.add_argument("--no-delete", action="store_true", help="Keep raw screenshots after analysis")
    args = parser.parse_args()

    if args.no_delete:
        os.environ["DELETE_AFTER_ANALYSIS"] = "false"

    run_analysis(days_back=args.days, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
