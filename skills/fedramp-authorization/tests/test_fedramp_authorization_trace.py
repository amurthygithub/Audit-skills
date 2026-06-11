"""Trace tests for fedramp-authorization.

End-to-end: load each seed, run the skill, and verify the output dict has the
expected top-level structure (the keys named in each UC's frontmatter
expected_outputs). Seeds are self-contained (loaded as-is).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from fedramp_authorization_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


_PAYLOADS = {
    "UC-01": lambda: _load("uc-01-input.json"),
    "UC-02": lambda: _load("uc-02-input.json"),
    "UC-03": lambda: _load("uc-03-input.json"),
}


def test_uc_01_output_shape():
    out = run_skill("UC-01", _PAYLOADS["UC-01"]())
    for k in ("overall_impact", "baseline", "baseline_controls", "poam_open", "poam", "classification"):
        assert k in out


def test_uc_02_output_shape():
    out = run_skill("UC-02", _PAYLOADS["UC-02"]())
    for k in ("overall_impact", "li_saas_eligible", "baseline", "baseline_controls", "classification"):
        assert k in out


def test_uc_03_output_shape():
    out = run_skill("UC-03", _PAYLOADS["UC-03"]())
    for k in ("controls_total", "inherited_count", "findings", "poam_item_count",
              "findings_by_severity", "has_high_severity_finding", "classification"):
        assert k in out
    assert isinstance(out["findings"], list)


@pytest.mark.parametrize("uc_id,expected_top_key", [
    ("UC-01", "baseline_controls"),
    ("UC-02", "li_saas_eligible"),
    ("UC-03", "poam_item_count"),
])
def test_trace_each_uc(uc_id, expected_top_key):
    out = run_skill(uc_id, _PAYLOADS[uc_id]())
    assert expected_top_key in out, f"{uc_id} missing top-level key {expected_top_key}"
    assert "classification" in out
