"""Metamorphic tests for hipaa-security-rule: input mutations that must not
(or must predictably) change the output."""

from __future__ import annotations

import json
from pathlib import Path

from hipaa_security_rule_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def _uc01_payload() -> dict:
    payload = _load("uc-01-input.json")
    payload["risks"] = _load("uc-01-risks.json")
    payload["addressable_register"] = _load("uc-01-addressable-register.json")
    return payload


def test_uc01_risk_order_invariance():
    """Reversing risk-record order must not change the rollup."""
    p1 = _uc01_payload()
    p2 = _uc01_payload()
    p2["risks"] = list(reversed(p2["risks"]))
    o1, o2 = run_skill("UC-01", p1), run_skill("UC-01", p2)
    assert o1["risk_summary"] == o2["risk_summary"]
    assert o1["disposition_summary"] == o2["disposition_summary"]


def test_uc01_band_monotonicity():
    """Raising one risk's impact can never lower its band."""
    order = {"Low": 0, "Medium": 1, "High": 2}
    base = run_skill("UC-01", _uc01_payload())
    bumped_payload = _uc01_payload()
    bumped_payload["risks"][4]["impact"] = 3  # R-05 was impact 3 already-safe? use index 10 (R-11, 1x1)
    bumped_payload["risks"][10]["impact"] = 3
    bumped = run_skill("UC-01", bumped_payload)
    base_band = next(r["band"] for r in base["risk_register"] if r["risk_id"] == "R-11")
    new_band = next(r["band"] for r in bumped["risk_register"] if r["risk_id"] == "R-11")
    assert order[new_band] >= order[base_band]


def test_uc02_inventory_order_invariance():
    """Reordering the control inventory must not change summary or priorities."""
    payload = _load("uc-02-input.json")
    inv = _load("uc-02-control-inventory.json")
    docs = _load("uc-02-documentation-register.json")
    p1 = {**payload, "control_inventory": inv, "documentation_register": docs}
    p2 = {**payload, "control_inventory": list(reversed(inv)), "documentation_register": docs}
    o1, o2 = run_skill("UC-02", p1), run_skill("UC-02", p2)
    assert o1["readiness_summary"] == o2["readiness_summary"]
    assert o1["gap_priorities"] == o2["gap_priorities"]
    assert o1["stale_docs"] == o2["stale_docs"]


def test_uc03_clause_order_invariance():
    """BAA clause order must not change the missing-provision result."""
    payload = _load("uc-03-input.json")
    baa = _load("uc-03-baa-terms.json")
    p1 = {**payload, "baa_terms": baa}
    p2 = {**payload, "baa_terms": {**baa, "proposed_clauses": list(reversed(baa["proposed_clauses"]))}}
    o1, o2 = run_skill("UC-03", p1), run_skill("UC-03", p2)
    assert o1["baa_check"] == o2["baa_check"]
    assert o1["checklist_summary"] == o2["checklist_summary"]
