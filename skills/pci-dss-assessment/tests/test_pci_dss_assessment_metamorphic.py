"""Metamorphic tests for pci-dss-assessment."""

from __future__ import annotations

import json
from pathlib import Path

from pci_dss_assessment_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def test_uc02_inventory_order_invariance():
    """Reordering the system inventory must not change the scope counts."""
    p1 = _load("uc-02-input.json")
    p2 = dict(p1)
    p2["system_inventory"] = list(reversed(p1["system_inventory"]))
    o1, o2 = run_skill("UC-02", p1), run_skill("UC-02", p2)
    assert o1["in_scope_systems"] == o2["in_scope_systems"]
    assert o1["cde_systems"] == o2["cde_systems"]
    assert o1["classification"] == o2["classification"]


def test_uc02_segmentation_monotonicity():
    """Re-tagging an in-scope system to out-of-scope can only lower the in-scope count."""
    base = run_skill("UC-02", _load("uc-02-input.json"))
    p = _load("uc-02-input.json")
    # move one 'connected' system out of scope (segmentation)
    for s in p["system_inventory"]:
        if s["scope_tag"] == "connected":
            s["scope_tag"] = "out"
            break
    after = run_skill("UC-02", p)
    assert after["in_scope_systems"] <= base["in_scope_systems"]
    assert after["in_scope_systems"] == base["in_scope_systems"] - 1


def test_uc03_element_order_invariance():
    """Worksheet-element evaluation must not depend on dict key order."""
    p1 = _load("uc-03-input.json")
    p2 = dict(p1)
    pcc = dict(p1["proposed_compensating_control"])
    p2["proposed_compensating_control"] = {k: pcc[k] for k in reversed(list(pcc))}
    o1, o2 = run_skill("UC-03", p1), run_skill("UC-03", p2)
    assert o1["worksheet_complete"] == o2["worksheet_complete"]
    assert o1["worksheet_elements_present"] == o2["worksheet_elements_present"]


def test_uc01_volume_does_not_flip_saq_path():
    """SAQ path is architecture-driven; transaction volume alone must not change it
    (brand thresholds are out of model — a documented non-goal)."""
    p = _load("uc-01-input.json")
    base = run_skill("UC-01", p)
    p2 = dict(p)
    p2["entity"] = {**p["entity"], "annual_transactions": 50}
    assert run_skill("UC-01", p2)["saq_eligibility"] == base["saq_eligibility"]
