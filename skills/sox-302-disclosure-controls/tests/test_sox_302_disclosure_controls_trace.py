"""Trace tests for sox-302-disclosure-controls.

End-to-end: load the seed input, run the skill, and verify the output dict
has the expected top-level structure (every UC returns a dict with the keys
named in its frontmatter expected_outputs). The §302 seeds are self-contained
(no sub-seed merging) — each `uc-0N-input.json` is loaded as-is.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from sox_302_disclosure_controls_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def _uc01_payload() -> dict:
    return _load("uc-01-input.json")


def _uc02_payload() -> dict:
    return _load("uc-02-input.json")


def _uc03_payload() -> dict:
    return _load("uc-03-input.json")


_PAYLOADS = {"UC-01": _uc01_payload, "UC-02": _uc02_payload, "UC-03": _uc03_payload}


def test_uc_01_output_shape():
    """UC-01 output dict has the expected top-level keys (DC&P conclusion + cascade roll-up)."""
    out = run_skill("UC-01", _uc01_payload())
    assert "dcp_conclusion" in out
    assert "par5_disclosure_required" in out
    assert "subcert_total" in out
    assert "subcert_exceptions" in out
    assert "subcert_clean" in out
    assert "top_level_cert_clean" in out
    assert "classification" in out


def test_uc_02_output_shape():
    """UC-02 output dict has the expected top-level keys (first-302 obligations + scope split)."""
    out = run_skill("UC-02", _uc02_payload())
    assert "section_302_certification_required" in out
    assert "section_404a_management_assessment_required" in out
    assert "section_404b_auditor_attestation_required" in out
    assert "dcp_scope_count" in out
    assert "icfr_scope_count" in out
    assert "cyber_8k_in_dcp_scope" in out
    assert "classification" in out


def test_uc_03_output_shape():
    """UC-03 output dict has the expected top-level keys (cascade coverage + eval-frequency split)."""
    out = run_skill("UC-03", _uc03_payload())
    assert "entities_total" in out
    assert "entities_covered" in out
    assert "coverage_gaps" in out
    assert "fully_covered" in out
    assert "quarterly_eval_entities" in out
    assert "annual_eval_entities" in out
    assert "classification" in out
    assert isinstance(out["coverage_gaps"], list)


@pytest.mark.parametrize("uc_id,expected_top_key", [
    ("UC-01", "dcp_conclusion"),
    ("UC-02", "section_404b_auditor_attestation_required"),
    ("UC-03", "entities_covered"),
])
def test_trace_each_uc(uc_id, expected_top_key):
    """Each UC's seed input flows through to a recognizable output shape."""
    out = run_skill(uc_id, _PAYLOADS[uc_id]())
    assert expected_top_key in out, f"{uc_id} missing top-level key {expected_top_key}"
    assert "classification" in out
