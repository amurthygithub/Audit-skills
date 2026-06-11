"""Adversarial tests for coso-internal-controls."""
from __future__ import annotations
from coso_internal_controls_stub import run_skill

def test_unknown_use_case():
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN"
    assert "error" in out

def test_uc01_missing_processes():
    out = run_skill("UC-01", {"entity_description": "Bank"})
    assert out["rcm"]["processes"] == 0

def test_uc02_no_candidates_still_unmitigated():
    """A deficiency with no compensating candidates cannot be mitigated; a pervasive
    ITGC with material magnitude is a material weakness (SOX-641 contract)."""
    out = run_skill("UC-02", {
        "deficiency": {"type": "itgc_logical_access", "affected_systems": ["ERP"],
                       "assertion_at_risk": "occurrence"},
        "authority_of_retained_access": {"can_create_vendors": True},
        "materiality": 100000, "compensating_controls_candidates": [],
        "preliminary_classification": "Significant Deficiency"})
    assert out["qualifying_compensating_controls"] == []
    assert out["classification"] == "Material Weakness"

def test_uc02_all_fields_missing():
    out = run_skill("UC-02", {})
    assert out["classification"] == "INSUFFICIENT_INPUT"

def test_uc03_empty_entity():
    out = run_skill("UC-03", {})
    assert out["entity_description"] == ""
    assert len(out["principle_assessments"]) == 17

def test_uc01_unknown_processes():
    out = run_skill("UC-01", {"entity_description": "Bank", "processes": ["Unknown X", "Foo"]})
    assert out["rcm"]["processes"] == 2

def test_uc02_only_preliminary():
    out = run_skill("UC-02", {"preliminary_classification": "Material Weakness"})
    assert out["classification"] == "INSUFFICIENT_INPUT"
