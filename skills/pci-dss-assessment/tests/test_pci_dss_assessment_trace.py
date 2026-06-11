"""Trace tests for pci-dss-assessment.

End-to-end: load the seed input, run the skill, and verify the output dict
has the expected top-level structure (every UC returns a dict with the keys
named in its frontmatter expected_outputs).

Unlike hipaa-security-rule, the PCI seeds are self-contained — each UC payload
is its ``uc-NN-input.json`` as-is, with no sub-seed merging.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from pci_dss_assessment_stub import run_skill

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
    """UC-01 (SAQ selection) output dict has the expected top-level keys."""
    out = run_skill("UC-01", _uc01_payload())
    assert "saq_eligibility" in out
    assert "deciding_factor" in out
    assert "client_side_script_requirements_apply" in out
    assert isinstance(out["client_side_script_requirements_apply"], list)
    assert "brand_caveat" in out
    assert "classification" in out


def test_uc_02_output_shape():
    """UC-02 (ROC scope / segmentation) output dict has the expected top-level keys."""
    out = run_skill("UC-02", _uc02_payload())
    for key in ("total_systems", "cde_systems", "in_scope_systems", "out_of_scope_systems"):
        assert key in out, f"UC-02 output missing {key}"
    # footing: in-scope + out-of-scope == total
    assert out["in_scope_systems"] + out["out_of_scope_systems"] == out["total_systems"]
    assert "customized_approach_accepted" in out
    assert "customized_approach_rejected_no_tra" in out
    assert "classification" in out


def test_uc_03_output_shape():
    """UC-03 (compensating control) output dict has the expected top-level keys."""
    out = run_skill("UC-03", _uc03_payload())
    assert "control_type" in out
    assert "worksheet_complete" in out
    assert "worksheet_elements_present" in out
    assert "missing_elements" in out
    assert isinstance(out["missing_elements"], list)
    assert "classification" in out


@pytest.mark.parametrize("uc_id,expected_top_key", [
    ("UC-01", "saq_eligibility"),
    ("UC-02", "in_scope_systems"),
    ("UC-03", "control_type"),
])
def test_trace_each_uc(uc_id, expected_top_key):
    """Each UC's seed input flows through to a recognizable output shape."""
    out = run_skill(uc_id, _PAYLOADS[uc_id]())
    assert expected_top_key in out, f"{uc_id} missing top-level key {expected_top_key}"
    assert "classification" in out
