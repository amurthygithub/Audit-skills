"""Adversarial tests for sox-302-disclosure-controls — edge cases and the fidelity traps."""

from __future__ import annotations

import json
from pathlib import Path

from sox_302_disclosure_controls_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name):
    return json.loads((SEEDS / name).read_text())


def test_uc01_missing_mw_facts_refuses():
    out = run_skill("UC-01", {"sub_certifications": []})
    assert out["classification"] == "INSUFFICIENT_INPUT"


def test_uc01_unremediated_mw_forces_not_effective():
    """The fidelity trap: an unremediated MW in a disclosure-relevant area cannot yield an
    'effective' DC&P conclusion."""
    p = dict(_load("uc-01-input.json"))
    p["material_weakness"] = {"area": "revenue", "affects_disclosure_relevant_area": True,
                              "remediated": False}
    out = run_skill("UC-01", p)
    assert out["dcp_conclusion"] == "not effective"


def test_uc02_404b_never_required_for_newly_public():
    """404(b) auditor attestation is exempt for a newly-public filer; 302 still applies."""
    p = dict(_load("uc-02-input.json"))
    p["filer"] = {"newly_public": True, "egc": False, "accelerated": True, "first_periodic_report": True}
    out = run_skill("UC-02", p)
    assert out["section_404b_auditor_attestation_required"] is False
    assert out["section_302_certification_required"] is True  # never exempt from 302


def test_uc02_seasoned_accelerated_filer_owes_404b():
    """A seasoned (not newly-public, not EGC) accelerated filer DOES owe 404(b)."""
    p = dict(_load("uc-02-input.json"))
    p["filer"] = {"newly_public": False, "egc": False, "accelerated": True, "first_periodic_report": False}
    out = run_skill("UC-02", p)
    assert out["section_404b_auditor_attestation_required"] is True
    assert out["classification"] == "FIRST_302_404B_REQUIRED"


def test_uc02_missing_filer_status_refuses():
    out = run_skill("UC-02", {"disclosure_inventory": []})
    assert out["classification"] == "INSUFFICIENT_INPUT"


def test_uc03_empty_entities_zero_coverage():
    p = dict(_load("uc-03-input.json"))
    p["entities"] = []
    out = run_skill("UC-03", p)
    assert out["entities_total"] == 0 and out["coverage_gaps"] == []
    assert out["classification"] == "CASCADE_GAPS_0"


def test_unknown_use_case_refuses():
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN" and "error" in out
