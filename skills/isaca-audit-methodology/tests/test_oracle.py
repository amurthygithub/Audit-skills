"""Oracle tests for isaca-audit-methodology.

Tests the expected output contracts for each use case against the
skill stub reference implementation.
"""

from __future__ import annotations

import json
from pathlib import Path

from skill_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_saas_maturity_output():
    """UC-01: maturity assessment contains required fields per COBIT 2019."""
    payload = _load("uc-01-input.json")
    result = run_skill("UC-01", payload)
    assessment = result["maturity_assessment"]

    assert "processes" in assessment, "Output should contain processes"
    assert "improvement_roadmap" in assessment, "Output should contain improvement_roadmap"
    assert "date" in assessment

    processes = assessment["processes"]
    assert len(processes) == 3, f"Expected 3 processes, got {len(processes)}"

    apo13 = next(p for p in processes if p["id"] == "APO13")
    assert apo13["current_maturity"] == 2.5
    assert apo13["target_maturity"] == 4.0
    assert apo13["gap"] == 1.5
    assert apo13["name"] == "Managed Security"

    roadmap = assessment["improvement_roadmap"]
    assert len(roadmap) >= 4, f"Expected >= 4 roadmap phases, got {len(roadmap)}"
    assert all("phase" in p and "gain" in p and "initiatives" in p for p in roadmap)

    assert "GAP_" in result["classification"]


def test_uc_02_five_part_observation():
    """UC-02: 5-part observation format with all required fields."""
    payload = _load("uc-02-input.json")
    result = run_skill("UC-02", payload)
    observation = result["observation"]

    assert observation["id"] == "ACC-2026-001"
    assert observation["severity"] == "Critical"
    assert observation["status"] == "Open"
    assert observation["title"] == "Inadequate Access Recertification for Critical Applications"

    for part in ("condition", "criteria", "cause", "effect", "recommendations"):
        assert part in observation, f"Missing 5-part field: {part}"

    assert "ISACA Standard S17" in observation["criteria"]
    assert "COBIT APO13.02" in observation["criteria"]

    cause = observation["cause"]
    assert "description" in cause
    assert "root_cause_category" in cause
    assert cause["root_cause_category"] == "Technology"

    effect = observation["effect"]
    assert "actual" in effect
    assert "potential" in effect
    assert "cobit_criteria_affected" in effect
    assert "Confidentiality" in effect["cobit_criteria_affected"]

    recs = observation["recommendations"]
    assert len(recs) >= 3, f"Expected >= 3 recommendations, got {len(recs)}"
    assert any(r["type"] == "Primary" for r in recs)
    assert any(r["type"] == "Compensating" for r in recs)
    assert any(r["type"] == "Long-term" for r in recs)

    assert "sample_summary" in observation
    assert observation["sample_summary"]["total_applications"] == 5
    assert observation["sample_summary"]["non_compliant"] == 3
    assert observation["sample_summary"]["compliance_rate_pct"] == 40.0


def test_uc_02_severity_from_seed_data():
    """UC-02: severity classification based on non-compliance count."""
    payload = _load("uc-02-input.json")
    result = run_skill("UC-02", payload)
    assert result["observation"]["severity"] == "Critical"
    assert result["classification"] == "Critical"

    sample_results = payload["sample_results"]
    non_comp = [r for r in sample_results if r["compliant"] is False]
    assert len(non_comp) == 3


def test_uc_02_actual_effect_from_seed():
    """UC-02: actual effect text flows through from seed data."""
    payload = _load("uc-02-input.json")
    result = run_skill("UC-02", payload)
    assert "12%" in result["observation"]["effect"]["actual"]
    assert "terminated employees" in result["observation"]["effect"]["actual"]


def test_uc_03_design_factors_output():
    """UC-03: design factors assessment with prioritized objectives."""
    payload = _load("uc-03-input.json")
    result = run_skill("UC-03", payload)
    assessment = result["design_factor_assessment"]

    assert assessment["enterprise_strategy"] == "Compliance-focused"
    assert "risk_profile" in assessment
    assert assessment["risk_profile"]["regulatory_risk"] == "High"
    assert assessment["risk_profile"]["vendor_risk"] == "High"

    assert "prioritized_objectives" in assessment
    objectives = assessment["prioritized_objectives"]
    assert len(objectives) == 5, f"Expected 5 prioritized objectives, got {len(objectives)}"

    top = objectives[0]
    assert top["objective"] == "MEA03"
    assert top["priority"] == 1
    assert top["name"] == "Managed Compliance"

    obj_ids = [o["objective"] for o in objectives]
    expected_order = ["MEA03", "APO12", "APO13", "DSS04", "APO10"]
    assert obj_ids == expected_order, f"Expected {expected_order}, got {obj_ids}"

    assert "design_factors_applied" in assessment
    assert len(assessment["design_factors_applied"]) == 5


def test_uc_03_strategy_reflected_in_rationale():
    """UC-03: enterprise strategy reflected in MEA03 rationale."""
    payload = _load("uc-03-input.json")
    result = run_skill("UC-03", payload)
    top = result["design_factor_assessment"]["prioritized_objectives"][0]
    assert "compliance" in top["rationale"].lower()
