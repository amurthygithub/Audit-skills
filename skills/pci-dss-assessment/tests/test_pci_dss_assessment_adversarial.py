"""Adversarial tests for pci-dss-assessment: edge cases and refusal paths."""

from __future__ import annotations

import json
from pathlib import Path

from pci_dss_assessment_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def test_uc01_missing_architecture_fact_refuses():
    """A missing payment-page fact must REFUSE, never guess the SAQ path."""
    payload = _load("uc-01-input.json")
    payload = dict(payload)
    pp = dict(payload["payment_page"])
    del pp["merchant_servers_touch_pan"]
    payload["payment_page"] = pp
    try:
        run_skill("UC-01", payload)
        assert False, "expected a refusal"
    except ValueError as e:
        assert "missing payment-page fact" in str(e)


def test_uc01_service_provider_routes_to_roc():
    payload = _load("uc-01-input.json")
    payload = dict(payload)
    payload["entity"] = {**payload["entity"], "is_service_provider": True}
    out = run_skill("UC-01", payload)
    assert out["saq_eligibility"] == "ROC"


def test_uc01_merchant_servers_touch_pan_forces_roc():
    payload = _load("uc-01-input.json")
    payload = dict(payload)
    payload["payment_page"] = {**payload["payment_page"], "merchant_servers_touch_pan": True}
    out = run_skill("UC-01", payload)
    assert out["saq_eligibility"] == "ROC"
    assert out["client_side_script_requirements_apply"] == ["6.4.3", "11.6.1"]


def test_uc02_empty_inventory_zero_scope():
    payload = _load("uc-02-input.json")
    payload = dict(payload)
    payload["system_inventory"] = []
    out = run_skill("UC-02", payload)
    assert out["total_systems"] == 0 and out["in_scope_systems"] == 0
    assert out["classification"] == "ROC_IN_SCOPE_0"


def test_uc02_customized_without_tra_rejected():
    """A customized-approach request without a TRA is rejected (Appendix D requires it)."""
    payload = _load("uc-02-input.json")
    payload = dict(payload)
    payload["customized_approach_requests"] = [
        {"requirement": "8.3.6", "topic": "x", "targeted_risk_analysis_present": False,
         "rationale": "no TRA"}]
    out = run_skill("UC-02", payload)
    assert out["customized_approach_accepted"] == []
    assert out["customized_approach_rejected_no_tra"] == ["8.3.6"]


def test_uc03_incomplete_worksheet_flagged():
    """A compensating control missing a worksheet element is incomplete."""
    payload = _load("uc-03-input.json")
    payload = dict(payload)
    pcc = {**payload["proposed_compensating_control"], "maintenance_documented": False}
    payload["proposed_compensating_control"] = pcc
    out = run_skill("UC-03", payload)
    assert out["worksheet_complete"] is False
    assert "maintenance_documented" in out["missing_elements"]
    assert out["classification"] == "COMP_CONTROL_INCOMPLETE"


def test_uc03_no_constraint_is_customized_not_compensating():
    """Without a legitimate constraint it is a customized approach, not a compensating control."""
    payload = _load("uc-03-input.json")
    payload = dict(payload)
    payload["constraint"] = {**payload["constraint"],
                             "legitimate_business_or_technical_constraint": False}
    out = run_skill("UC-03", payload)
    assert out["control_type"] == "customized_approach"


def test_unknown_use_case_refuses():
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN" and "error" in out
