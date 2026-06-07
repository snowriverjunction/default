# Ambient AI Screen Monitor & Productivity Auditor

A lightweight, local-only background tool that captures your screen activity during working hours, analyzes it with Claude's vision model, and delivers a weekly productivity audit report.

---

## How It Works

| Script | Role |
|---|---|
| `capture.py` | Runs silently in the background, taking a screenshot every 5 minutes during working hours (Mon–Fri, 8 AM–6 PM) |
| `analyze.py` | Runs at week's end, batches the screenshots through Claude's vision API, and writes a structured Markdown report |

All data stays **local** — screenshots are stored in `~/.ambient_monitor/screenshots/` and are deleted automatically after the report is generated.

---

## Prerequisites

- Python 3.11+
- An [Anthropic API key](https://console.anthropic.com/)
- macOS or Linux (for `pyautogui` screenshot capture)
  - On Linux, install `scrot` or `gnome-screenshot`: `sudo apt install scrot`
  - On macOS, grant Terminal/your IDE **Screen Recording** permission in System Settings → Privacy & Security

---

## Installation

```bash
# 1. Clone or copy the project folder
cd /path/to/ambient-monitor

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your environment variables
cp .env.example .env
# Open .env and add your ANTHROPIC_API_KEY
```

---

## Configuration (`.env`)

| Variable | Default | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | *(required)* | Your Anthropic API key |
| `SCREENSHOTS_DIR` | `~/.ambient_monitor/screenshots` | Where raw screenshots are stored |
| `REPORTS_DIR` | `~/.ambient_monitor/reports` | Where weekly reports are saved |
| `WORK_START_HOUR` | `8` | Start of working hours (24h) |
| `WORK_END_HOUR` | `18` | End of working hours (24h) |
| `CAPTURE_INTERVAL_SECONDS` | `300` | Time between screenshots (5 min) |
| `MAX_IMAGES_PER_BATCH` | `20` | Max images per API call |
| `DELETE_AFTER_ANALYSIS` | `true` | Auto-delete screenshots after report |
| `CLAUDE_MODEL` | `claude-opus-4-8` | Vision model to use |

---

## Usage

### Start the capture daemon

```bash
# Activate venv first
source .venv/bin/activate

# Start capturing (runs until you kill it)
python capture.py --run
```

### Pause / resume (for sensitive work)

```bash
python capture.py --pause    # Creates a .paused lock file — no screenshots taken
python capture.py --resume   # Removes the lock file — capturing resumes
python capture.py --status   # Show current state and screenshot count
```

### Generate the weekly report

```bash
# Analyze the past 7 days and write the report
python analyze.py

# Analyze a different window
python analyze.py --days 5

# Keep raw screenshots (skip auto-delete)
python analyze.py --no-delete

# Dry run — just list files, no API calls
python analyze.py --dry-run
```

The report is saved to `~/.ambient_monitor/reports/productivity_report_YYYYMMDD_HHMMSS.md`.

---

## Running Automatically

### macOS — launchd (recommended)

Create `~/Library/LaunchAgents/com.slc.ambient-monitor.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>              <string>com.slc.ambient-monitor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/.venv/bin/python</string>
        <string>/path/to/capture.py</string>
        <string>--run</string>
    </array>
    <key>RunAtLoad</key>          <true/>
    <key>KeepAlive</key>          <true/>
    <key>StandardOutPath</key>    <string>/tmp/ambient-monitor.log</string>
    <key>StandardErrorPath</key>  <string>/tmp/ambient-monitor-err.log</string>
</dict>
</plist>
```

Load it:
```bash
launchctl load ~/Library/LaunchAgents/com.slc.ambient-monitor.plist
```

### Weekly analysis — cron

Add to crontab (`crontab -e`):

```cron
# Run analysis every Friday at 5:00 PM
0 17 * * 5 /path/to/.venv/bin/python /path/to/analyze.py >> ~/.ambient_monitor/analyze.log 2>&1
```

### Linux — systemd user service

Create `~/.config/systemd/user/ambient-monitor.service`:

```ini
[Unit]
Description=Ambient AI Screen Monitor

[Service]
ExecStart=/path/to/.venv/bin/python /path/to/capture.py --run
Restart=always

[Install]
WantedBy=default.target
```

```bash
systemctl --user enable --now ambient-monitor
```

---

## Privacy & Security

- **100% local** — screenshots never leave your machine until you explicitly run `analyze.py`
- Screenshots are saved to a hidden directory (`~/.ambient_monitor/`) and auto-deleted after analysis
- Use `--pause` / `--resume` any time you're handling confidential information
- The `.env` file (with your API key) is excluded from version control via `.gitignore`

---

## Sample Report Structure

```
# Weekly Productivity Audit — Jun 02 – Jun 06, 2025

## 1. Executive Summary
## 2. Activity Breakdown
## 3. Delegation Opportunities
## 4. Workflow Bottlenecks
## 5. AI Tool Recommendations
## 6. SLC-Specific Acceleration
## 7. Quick Wins (This Week)
```

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `pyautogui` fails on macOS | Grant Screen Recording permission to Terminal in System Settings |
| `ANTHROPIC_API_KEY not set` | Ensure `.env` is in the same directory as the scripts and contains the key |
| Report is empty / no screenshots found | Check that `capture.py` is actually running: `python capture.py --status` |
| Too many API calls / rate limit errors | Lower `MAX_IMAGES_PER_BATCH` in `.env` (e.g., `10`) |
