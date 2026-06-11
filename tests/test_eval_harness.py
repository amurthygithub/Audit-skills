"""CI gate for the eval harness (SOX-600 V1).

Runs every case in evals/*/cases/ with the stub executor. The stub IS the
oracle, so every case must pass at 100% — a failure means either a broken
case fixture, a harness bug, or a contract drift between a skill's seeds and
its stub (which is exactly what this gate exists to catch).
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

HARNESS = Path(__file__).resolve().parent.parent / "evals" / "harness"
sys.path.insert(0, str(HARNESS))

from runner import Runner, eval_skills, load_cases  # noqa: E402
from executors import StubExecutor  # noqa: E402


def _all_cases():
    for skill in eval_skills():
        for case in load_cases(skill):
            yield pytest.param(case, id=f"{skill}/{case['id']}")


@pytest.mark.parametrize("case", _all_cases())
def test_case_passes_against_stub_oracle(case):
    runner = Runner(StubExecutor())
    result = runner.run_case(case, runs=1)
    assert result["pass_rate"] == 1.0, result["failures"]


def test_eval_skills_discovered():
    skills = eval_skills()
    assert "audit-workpapers" in skills and "hipaa-security-rule" in skills
