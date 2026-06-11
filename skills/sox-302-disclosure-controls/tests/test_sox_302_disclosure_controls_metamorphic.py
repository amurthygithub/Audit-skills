"""Metamorphic tests for sox-302-disclosure-controls."""

from __future__ import annotations

import json
from pathlib import Path

from sox_302_disclosure_controls_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name):
    return json.loads((SEEDS / name).read_text())


def test_uc01_subcert_order_invariance():
    p1 = _load("uc-01-input.json")
    p2 = dict(p1)
    p2["sub_certifications"] = list(reversed(p1["sub_certifications"]))
    o1, o2 = run_skill("UC-01", p1), run_skill("UC-01", p2)
    assert o1["subcert_exceptions"] == o2["subcert_exceptions"]
    assert o1["dcp_conclusion"] == o2["dcp_conclusion"]


def test_uc01_remediated_mw_flips_dcp_conclusion():
    """Remediating the MW flips DC&P to effective — proving the conclusion is fact-driven."""
    p = _load("uc-01-input.json")
    p = dict(p)
    p["material_weakness"] = {**p["material_weakness"], "remediated": True}
    out = run_skill("UC-01", p)
    assert out["dcp_conclusion"] == "effective"
    assert out["classification"] == "DCP_EFFECTIVE"


def test_uc03_entity_order_invariance():
    p1 = _load("uc-03-input.json")
    p2 = dict(p1)
    p2["entities"] = list(reversed(p1["entities"]))
    o1, o2 = run_skill("UC-03", p1), run_skill("UC-03", p2)
    assert o1["entities_covered"] == o2["entities_covered"]
    assert sorted(o1["coverage_gaps"]) == sorted(o2["coverage_gaps"])
    assert o1["quarterly_eval_entities"] == o2["quarterly_eval_entities"]
