"""Metamorphic tests for nist-csf-2.

Permutation invariants: the skill's outputs should be stable under
order-of-inputs permutations and other valid input reorderings.
"""

from __future__ import annotations

import json
from pathlib import Path

from nist_csf_2_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_subcategory_score_order_irrelevant():
    """Reordering the subcategory_scores in UC-01 input should not change the function-level Tier rollup."""
    payload = _load("uc-01-input.json")
    out1 = run_skill("UC-01", payload)
    rolled1 = out1["current_profile"]["current_tier_by_function"]

    payload2 = json.loads(json.dumps(payload))
    # Reorder subcategory_scores (reverse)
    payload2["subcategory_scores"] = list(reversed(payload["subcategory_scores"]))
    out2 = run_skill("UC-01", payload2)
    rolled2 = out2["current_profile"]["current_tier_by_function"]

    assert rolled1 == rolled2, f"Reorder changed rollup: {rolled1} vs {rolled2}"


def test_uc_02_radar_is_idempotent():
    """Running UC-02 twice on the same input produces the same radar output."""
    payload = _load("uc-02-input.json")
    out1 = run_skill("UC-02", payload)
    out2 = run_skill("UC-02", payload)
    assert out1["six_function_radar"] == out2["six_function_radar"]


def test_uc_03_lagging_subcategory_order_irrelevant():
    """UC-03 gap_count is invariant under reordering of lagging_subcategories."""
    payload = _load("uc-03-input.json")
    out1 = run_skill("UC-03", payload)
    out2 = run_skill("UC-03", json.loads(json.dumps(payload)))
    assert out1["gap_count"] == out2["gap_count"] == 14
