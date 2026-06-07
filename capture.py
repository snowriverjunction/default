#!/usr/bin/env python3
"""
Ambient AI Screen Monitor - Capture Daemon
Silently captures screenshots every 5 minutes during working hours.
"""

import os
import sys
import time
import signal
import logging
import argparse
from datetime import datetime, time as dtime
from pathlib import Path

import pyautogui
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
SCREENSHOTS_DIR = Path(os.getenv("SCREENSHOTS_DIR", Path.home() / ".ambient_monitor" / "screenshots"))
WORK_START = dtime(int(os.getenv("WORK_START_HOUR", 8)), 0)   # 8:00 AM
WORK_END   = dtime(int(os.getenv("WORK_END_HOUR", 18)), 0)    # 6:00 PM
WORK_DAYS  = {0, 1, 2, 3, 4}                                  # Monday–Friday
INTERVAL   = int(os.getenv("CAPTURE_INTERVAL_SECONDS", 300))  # 5 minutes
PAUSE_FILE = Path.home() / ".ambient_monitor" / ".paused"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [capture] %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(Path.home() / ".ambient_monitor" / "capture.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)


def is_working_hours() -> bool:
    now = datetime.now()
    return now.weekday() in WORK_DAYS and WORK_START <= now.time() <= WORK_END


def is_paused() -> bool:
    return PAUSE_FILE.exists()


def take_screenshot() -> Path | None:
    if is_paused():
        log.info("Capture paused — skipping.")
        return None

    if not is_working_hours():
        log.debug("Outside working hours — skipping.")
        return None

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = SCREENSHOTS_DIR / f"screen_{timestamp}.png"

    try:
        screenshot = pyautogui.screenshot()
        # Downscale to reduce storage while preserving readability for the vision model
        w, h = screenshot.size
        screenshot = screenshot.resize((w // 2, h // 2), Image.LANCZOS)
        screenshot.save(path, optimize=True)
        log.info("Captured %s", path.name)
        return path
    except Exception as exc:
        log.error("Screenshot failed: %s", exc)
        return None


def pause():
    PAUSE_FILE.parent.mkdir(parents=True, exist_ok=True)
    PAUSE_FILE.touch()
    print("Capture PAUSED. Run with --resume to continue.")


def resume():
    if PAUSE_FILE.exists():
        PAUSE_FILE.unlink()
    print("Capture RESUMED.")


def status():
    state = "PAUSED" if is_paused() else ("ACTIVE (working hours)" if is_working_hours() else "ACTIVE (outside working hours)")
    count = len(list(SCREENSHOTS_DIR.glob("*.png"))) if SCREENSHOTS_DIR.exists() else 0
    print(f"Status : {state}")
    print(f"Screenshots stored : {count}")
    print(f"Storage directory  : {SCREENSHOTS_DIR}")


def run_daemon():
    log.info("Capture daemon started. PID=%d  interval=%ds", os.getpid(), INTERVAL)
    log.info("Working hours: %s–%s Mon–Fri", WORK_START, WORK_END)

    def _shutdown(signum, frame):
        log.info("Signal %d received — shutting down.", signum)
        sys.exit(0)

    signal.signal(signal.SIGTERM, _shutdown)
    signal.signal(signal.SIGINT, _shutdown)

    while True:
        take_screenshot()
        time.sleep(INTERVAL)


def main():
    parser = argparse.ArgumentParser(description="Ambient AI Screen Monitor — capture daemon")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--pause",  action="store_true", help="Pause screenshot capture")
    group.add_argument("--resume", action="store_true", help="Resume screenshot capture")
    group.add_argument("--status", action="store_true", help="Show current status")
    group.add_argument("--run",    action="store_true", help="Start the capture daemon (default)")
    args = parser.parse_args()

    if args.pause:
        pause()
    elif args.resume:
        resume()
    elif args.status:
        status()
    else:
        run_daemon()


if __name__ == "__main__":
    main()
