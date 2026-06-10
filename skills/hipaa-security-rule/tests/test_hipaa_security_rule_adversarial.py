"""Adversarial tests for hipaa-security-rule: edge cases and refusal paths."""

from __future__ import annotations

import json
from pathlib import Path

from hipaa_security_rule_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def test_uc01_empty_register():
    """An empty addressable register yields zero dispositions — never invented specs."""
    payload = _load("uc-01-input.json")
    payload["risks"] = _load("uc-01-risks.json")
    payload["addressable_register"] = []
    out = run_skill("UC-01", payload)
    assert out["addressable_dispositions"] == []
    assert out["disposition_summary"] == {}
    assert out["decision_required_count"] == 0


def test_uc01_no_alternative_and_no_justification_still_documented_path():
    """A spec assessed not-reasonable with no alternative falls to the documented
    path; the oracle (not this stub) enforces that justification text exists —
    here we assert the disposition logic never silently produces 'implement'."""
    payload = _load("uc-01-input.json")
    payload["risks"] = []
    payload["addressable_register"] = [{
        "spec_id": "164.310(a)(2)(ii)", "name": "Facility security plan",
        "family": "physical", "decision_required": True,
        "reasonable_and_appropriate": False, "alternative": None, "justification": "remote org",
    }]
    out = run_skill("UC-01", payload)
    assert out["addressable_dispositions"][0]["disposition"] == "not_reasonable_documented"


def test_uc02_all_implemented_zero_gaps():
    """A fully implemented inventory with current docs produces an empty gap register."""
    payload = _load("uc-02-input.json")
    inv = [{**r, "status": "implemented"} for r in _load("uc-02-control-inventory.json")]
    docs = [{**d, "last_reviewed": "2026-01-15"} for d in _load("uc-02-documentation-register.json")]
    out = run_skill("UC-02", {**payload, "control_inventory": inv, "documentation_register": docs})
    assert out["gap_register"] == []
    assert out["gap_priorities"] == {}
    assert out["readiness_summary"] == {"total": 22, "implemented": 22}


def test_uc02_nprm_never_in_gap_basis():
    """Even if a seed row smuggles NPRM language into its name, the gap basis text
    stays current-law (the stub never emits NPRM-based gap records)."""
    payload = _load("uc-02-input.json")
    inv = _load("uc-02-control-inventory.json")
    inv[0] = {**inv[0], "name": inv[0]["name"] + " (NPRM proposes annual audit)"}
    docs = _load("uc-02-documentation-register.json")
    out = run_skill("UC-02", {**payload, "control_inventory": inv, "documentation_register": docs})
    assert out["nprm_items_in_current_law_gaps"] == 0
    assert not any("NPRM" in g["basis"].upper() for g in out["gap_register"])


def test_uc03_complete_baa_no_missing():
    """A BAA covering all four required provisions reports nothing missing."""
    payload = _load("uc-03-input.json")
    baa = _load("uc-03-baa-terms.json")
    clauses = baa["proposed_clauses"] + [
        {"clause_id": "C-5", "provision": "subcontractor_flowdown",
         "text": "Consultant shall ensure subcontractors agree to the same restrictions."},
        {"clause_id": "C-6", "provision": "incident_reporting",
         "text": "Consultant shall report security incidents including 164.410 breaches."},
    ]
    out = run_skill("UC-03", {**payload, "baa_terms": {**baa, "proposed_clauses": clauses}})
    assert out["baa_check"]["missing_provisions"] == []


def test_uc03_unknown_system_contributes_nothing():
    """An unrecognized system never fabricates checklist items."""
    payload = _load("uc-03-input.json")
    payload["org"] = {**payload["org"], "systems": ["quantum_fax_machine"]}
    out = run_skill("UC-03", {**payload, "baa_terms": _load("uc-03-baa-terms.json")})
    base_items = 4  # the always-present base checklist
    assert out["checklist_summary"]["items"] == base_items


def test_unknown_use_case_refuses():
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN"
    assert "error" in out
