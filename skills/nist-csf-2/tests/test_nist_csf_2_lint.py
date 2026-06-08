import subprocess, sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
TOOLS_DIR = Path(__file__).parent.parent.parent.parent / "tools"
LINT_SCRIPT = TOOLS_DIR / "lint_skill.py"


def test_lint_passes():
    result = subprocess.run(
        [sys.executable, str(LINT_SCRIPT), str(SKILL_DIR)],
        capture_output=True, text=True,
    )
    ok = result.returncode == 0
    out = result.stdout + result.stderr
    assert ok, "Lint FAIL: " + out
