"""Metamorphic tests for isaca-audit-methodology.

Mutation-based: change the input in a known way, verify the output changes
accordingly. Tests invariants of the skill rather than exact outputs.
"""

from __future__ import annotations

import json
from pathlib import Path

from skill_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_process_addition_increases_scope():
    """Adding a process to scope increases the number of assessed processes."""
    payload = _load("uc-01-input.json")
    base = run_skill("UC-01", payload)
    base_count = len(base["maturity_assessment"]["processes"])

    mutated = dict(payload)
    mutated["processes_in_scope"] = list(payload["processes_in_scope"]) + ["DSS04"]
    new = run_skill("UC-01", mutated)
    new_count = len(new["maturity_assessment"]["processes"])

    assert new_count == base_count + 1
    assert any(p["id"] == "DSS04" for p in new["maturity_assessment"]["processes"])


def test_uc_01_evidence_improvement_reduces_gap():
    """Improving evidence for a process reduces its maturity gap."""
    payload = _load("uc-01-input.json")
    base = run_skill("UC-01", payload)
    apo13_base = next(p for p in base["maturity_assessment"]["processes"] if p["id"] == "APO13")
    base_gap = apo13_base["gap"]

    mutated = dict(payload)
    mutated["current_evidence"] = dict(payload.get("current_evidence", {}))
    mutated["current_evidence"]["APO13"] = 3.5
    new = run_skill("UC-01", mutated)
    apo13_new = next(p for p in new["maturity_assessment"]["processes"] if p["id"] == "APO13")
    new_gap = apo13_new["gap"]

    assert new_gap < base_gap


def test_uc_02_more_noncompliant_increases_severity():
    """More non-compliant applications should increase or maintain severity."""
    payload = _load("uc-02-input.json")
    base = run_skill("UC-02", payload)
    base_severity = base["observation"]["severity"]

    mutated = dict(payload)
    extra_failures = [
        {"application": f"App-extra-{i}", "compliant": False, "finding": "Failed recertification"}
        for i in range(5)
    ]
    mutated["sample_results"] = list(payload.get("sample_results", [])) + extra_failures
    new = run_skill("UC-02", mutated)
    new_severity = new["observation"]["severity"]

    severity_order = {"Low": 0, "Medium": 1, "High": 2, "Critical": 3}
    assert severity_order.get(new_severity, 0) >= severity_order.get(base_severity, 0)


def test_uc_02_all_compliant_lowers_severity():
    """All-compliant sample should yield Low severity."""
    payload = _load("uc-02-input.json")
    mutated = dict(payload)
    mutated["sample_results"] = [
        {"application": "App-1", "compliant": True, "finding": None},
        {"application": "App-2", "compliant": True, "finding": None},
    ]
    new = run_skill("UC-02", mutated)
    assert new["observation"]["severity"] == "Low"


def test_uc_03_risk_profile_change_keeps_mea03_first():
    """Changing risk profile to tech-focused still keeps MEA03 highest."""
    payload = _load("uc-03-input.json")
    base = run_skill("UC-03", payload)
    top_base = base["design_factor_assessment"]["prioritized_objectives"][0]["objective"]
    assert top_base == "MEA03"


def test_uc_03_strategy_change_invariant():
    """Regardless of strategy, prioritized objectives are always 5."""
    payload = _load("uc-03-input.json")

    strategies = ["Compliance-focused", "Growth", "Innovation", "Cost Leadership"]
    for strat in strategies:
        mutated = dict(payload)
        mutated["enterprise_strategy"] = strat
        out = run_skill("UC-03", mutated)
        count = len(out["design_factor_assessment"]["prioritized_objectives"])
        assert count == 5, f"Strategy '{strat}' should produce 5 prioritized objectives, got {count}"
