"""Adversarial tests for coso-internal-controls."""
from __future__ import annotations
from skill_stub import run_skill

def test_unknown_use_case():
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN"
    assert "error" in out

def test_uc01_missing_processes():
    out = run_skill("UC-01", {"entity_description": "Bank"})
    assert out["rcm"]["processes"] == 0

def test_uc02_missing_compensating_controls():
    out = run_skill("UC-02", {"deficiency_description": "Gap", "preliminary_classification": "D"})
    assert out["classification"] == "Significant Deficiency"
    assert out["compensating_control_analysis"] == []

def test_uc02_all_fields_missing():
    out = run_skill("UC-02", {})
    assert "classification" in out
    assert "decision_tree" in out

def test_uc03_empty_entity():
    out = run_skill("UC-03", {})
    assert out["entity_description"] == ""
    assert len(out["principle_assessments"]) == 17

def test_uc01_unknown_processes():
    out = run_skill("UC-01", {"entity_description": "Bank", "processes": ["Unknown X", "Foo"]})
    assert out["rcm"]["processes"] == 2

def test_uc02_only_preliminary():
    out = run_skill("UC-02", {"preliminary_classification": "Material Weakness"})
    assert out["classification"] == "Significant Deficiency"
