"""Metamorphic tests for coso-internal-controls."""
from __future__ import annotations
from skill_stub import run_skill

def test_uc02_deficiency_removed():
    out = run_skill("UC-02", {"deficiency_description": "", "affected_accounts": [], "affected_assertions": [], "compensating_controls_candidates": [], "preliminary_classification": "D"})
    assert out["classification"] == "Significant Deficiency"
    assert len(out["compensating_control_analysis"]) == 0

def test_uc02_compensating_controls_match():
    out = run_skill("UC-02", {"deficiency_description": "ERP gap", "affected_accounts": ["OpEx","Payroll"], "affected_assertions": ["Existence"], "compensating_controls_candidates": ["Bank reconciliation (monthly, precise)","Payroll reconciliation (monthly, precise)","Budget variance analysis (monthly, low precision)"], "preliminary_classification": "SD"})
    analysis = out["compensating_control_analysis"]
    assert len(analysis) == 3
    assert len([a for a in analysis if a["precision"]=="sufficient"]) == 2
    assert len([a for a in analysis if a["precision"]=="insufficient"]) == 1

def test_uc01_more_processes_more_controls():
    o1 = run_skill("UC-01", {"entity_description": "Bank", "processes": ["Loan Origination"]})
    o3 = run_skill("UC-01", {"entity_description": "Bank", "processes": ["Loan Origination","Deposit Operations","Investment Securities"]})
    assert o1["rcm"]["processes"] == 1
    assert o3["rcm"]["processes"] == 3
    assert len(o1["deficiencies"]) == len(o3["deficiencies"])

def test_uc03_all_principles_present():
    out = run_skill("UC-03", {"entity_description": "TestCo", "assessment_date": "2026-01-01"})
    for pa in out["principle_assessments"]:
        assert pa["deficiencies"] <= pa["pofs_assessed"]
        assert pa["pofs_yes"] + pa["pofs_partial"] + pa["pofs_no"] == pa["pofs_assessed"]

def test_uc03_integrated_operation():
    out = run_skill("UC-03", {"entity_description": "TestCo", "assessment_date": "2026-01-01"})
    assert "assessment" in out["integrated_operation"]
    assert "evidence" in out["integrated_operation"]
