"""Trace tests for hipaa-security-rule.

End-to-end: load the seed input, run the skill, and verify the output dict
has the expected top-level structure (every UC returns a dict with the keys
named in its frontmatter expected_outputs).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from hipaa_security_rule_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def _uc01_payload() -> dict:
    payload = _load("uc-01-input.json")
    payload["risks"] = _load("uc-01-risks.json")
    payload["addressable_register"] = _load("uc-01-addressable-register.json")
    return payload


def _uc02_payload() -> dict:
    payload = _load("uc-02-input.json")
    payload["control_inventory"] = _load("uc-02-control-inventory.json")
    payload["documentation_register"] = _load("uc-02-documentation-register.json")
    return payload


def _uc03_payload() -> dict:
    payload = _load("uc-03-input.json")
    payload["baa_terms"] = _load("uc-03-baa-terms.json")
    return payload


_PAYLOADS = {"UC-01": _uc01_payload, "UC-02": _uc02_payload, "UC-03": _uc03_payload}


def test_uc_01_output_shape():
    """UC-01 output dict has the expected top-level keys from the frontmatter expected_outputs."""
    out = run_skill("UC-01", _uc01_payload())
    assert "risk_register" in out
    assert "risk_summary" in out
    rs = out["risk_summary"]
    assert "total" in rs
    assert "by_band" in rs
    assert "addressable_dispositions" in out
    assert "disposition_summary" in out
    assert "encryption_at_rest_disposition" in out


def test_uc_02_output_shape():
    """UC-02 output dict has the expected top-level keys."""
    out = run_skill("UC-02", _uc02_payload())
    assert "readiness_matrix" in out
    assert "readiness_summary" in out
    assert "gap_register" in out
    assert "gap_priorities" in out
    assert "stale_docs" in out
    # Every matrix row carries the four readiness fields
    for row in out["readiness_matrix"]:
        for key in ("standard_id", "name", "family", "status"):
            assert key in row, f"Matrix row missing {key}: {row}"


def test_uc_03_output_shape():
    """UC-03 output dict has the expected top-level keys."""
    out = run_skill("UC-03", _uc03_payload())
    assert "baa_check" in out
    baa = out["baa_check"]
    for key in ("required_provisions", "present_provisions", "missing_provisions"):
        assert key in baa, f"baa_check missing {key}"
    assert "safeguard_checklist" in out
    assert "checklist_summary" in out


@pytest.mark.parametrize("uc_id,expected_top_key", [
    ("UC-01", "risk_summary"),
    ("UC-02", "readiness_matrix"),
    ("UC-03", "baa_check"),
])
def test_trace_each_uc(uc_id, expected_top_key):
    """Each UC's seed input flows through to a recognizable output shape."""
    out = run_skill(uc_id, _PAYLOADS[uc_id]())
    assert expected_top_key in out, f"{uc_id} missing top-level key {expected_top_key}"
    assert "classification" in out
