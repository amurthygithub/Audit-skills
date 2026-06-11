"""CI gate: README + category pointer stay in sync with reality.

Added 2026-06-11 after the M5-cycle-1 sweep found the root README's banner, CI
line, quickstart, and one per-skill test count all stale (per-PR updates had
been partial). The pointer-drift test catches presence; this catches the
COUNTS — the higher-frequency drift class. Wraps tools/check_readme_sync.py so
the same check runs standalone and in CI.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def test_readme_and_pointer_in_sync():
    result = subprocess.run(
        [sys.executable, "tools/check_readme_sync.py"],
        cwd=str(REPO), capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
