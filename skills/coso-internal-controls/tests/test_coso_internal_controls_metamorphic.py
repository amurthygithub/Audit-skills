"""Metamorphic tests for coso-internal-controls."""
from __future__ import annotations
from coso_internal_controls_stub import run_skill

def test_uc02_deficiency_removed():
    out = run_skill("UC-02", {"deficiency": {}, "preliminary_classification": "D"})
    assert out["classification"] == "INSUFFICIENT_INPUT"
    assert len(out["compensating_control_analysis"]) == 0

def test_uc02_reconciliations_fail_occurrence_test():
    """Reconciliations address completeness/accuracy and draw IPE from the affected
    system, so none qualify against the occurrence assertion (SOX-641 contract)."""
    out = run_skill("UC-02", {
        "deficiency": {"type": "itgc_logical_access", "affected_systems": ["ERP"],
                       "assertion_at_risk": "occurrence"},
        "authority_of_retained_access": {"can_create_vendors": True}, "materiality": 100000,
        "compensating_controls_candidates": [
            {"control": "Bank reconciliation", "assertions_addressed": ["completeness","accuracy"], "relies_on_ipe_from": "ERP"},
            {"control": "Payroll reconciliation", "assertions_addressed": ["completeness","accuracy"], "relies_on_ipe_from": "ERP"},
            {"control": "Budget variance analysis", "assertions_addressed": ["completeness"], "relies_on_ipe_from": "ERP"}],
        "lookback": {"performed": False}})
    analysis = out["compensating_control_analysis"]
    assert len(analysis) == 3
    assert all(not a["qualifies"] for a in analysis)
    assert out["qualifying_compensating_controls"] == []

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
