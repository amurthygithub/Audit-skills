"""Shared-infrastructure tests for every on-Spine skill (SOX-634).

1. Telemetry drift guard: every skill's telemetry/instrument.py and
   telemetry/schema.json must be byte-identical to skills/TEMPLATE's
   canonical copy. The copies are vendored (each skill folder stays
   self-contained for distribution), and this test is what makes
   vendoring safe: drift caused the nist-csf-2 module-shadowing hazard
   (lessons-learned §3.7), so drift is now a test failure.

2. Lint gate: the Tier 0a linter passes for every skill. Skills are
   auto-discovered, so a new skill cannot be forgotten (the CI lint
   list went stale at 5 skills exactly this way).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "skills" / "TEMPLATE"
SKILLS = sorted(
    p.parent for p in (REPO / "skills").glob("*/SKILL.md") if p.parent.name != "TEMPLATE"
)
SKILL_IDS = [s.name for s in SKILLS]

VENDORED_FILES = ("telemetry/instrument.py", "telemetry/schema.json")
REQUIRED_TELEMETRY_EXPORTS = (
    # lessons-learned §3.7 / AGENTS.md §6.5: full API surface in every copy,
    # so sys.path shadowing between identical modules is harmless.
    "instrumented", "SkillInvocation", "skill_invocation", "emit", "timed",
)


def test_skills_discovered():
    assert len(SKILLS) >= 6, f"expected at least 6 on-Spine skills, found {SKILL_IDS}"


@pytest.mark.parametrize("skill", SKILLS, ids=SKILL_IDS)
@pytest.mark.parametrize("rel", VENDORED_FILES)
def test_vendored_telemetry_matches_template(skill: Path, rel: str):
    canonical = (TEMPLATE / rel).read_bytes()
    vendored = (skill / rel).read_bytes()
    assert vendored == canonical, (
        f"{skill.name}/{rel} has drifted from skills/TEMPLATE/{rel}. "
        f"Edit the TEMPLATE copy and re-sync: "
        f"cp skills/TEMPLATE/{rel} skills/{skill.name}/{rel}"
    )


def test_canonical_telemetry_exports():
    text = (TEMPLATE / "telemetry" / "instrument.py").read_text(encoding="utf-8")
    for name in REQUIRED_TELEMETRY_EXPORTS:
        assert f"def {name}" in text or f"class {name}" in text, (
            f"TEMPLATE telemetry/instrument.py missing export: {name}"
        )


@pytest.mark.parametrize("skill", SKILLS, ids=SKILL_IDS)
def test_lint_passes(skill: Path):
    result = subprocess.run(
        [sys.executable, str(REPO / "tools" / "lint_skill.py"), str(skill)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, (
        f"Linter failed for {skill.name}:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
