"""Lint test for aicpa-soc-reporting.

Runs the Tier 0a linter against this skill and asserts it passes.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LINTER = ROOT / "tools" / "lint_skill.py"
SKILL = Path(__file__).resolve().parent.parent


def test_lint_passes():
    result = subprocess.run(
        [sys.executable, str(LINTER), str(SKILL)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, (
        f"Linter failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
