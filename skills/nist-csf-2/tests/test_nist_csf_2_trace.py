"""Trace tests for nist-csf-2.

End-to-end: load the seed input, run the skill, and verify the output dict
has the expected top-level structure (every UC returns a dict with the keys
named in its frontmatter expected_outputs).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nist_csf_2_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_output_shape():
    """UC-01 output dict has the expected top-level keys from the frontmatter expected_outputs."""
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)
    # The stub returns current_profile; the full deployment would also return
    # target_profile, gap_analysis, roadmap_90_day
    assert "current_profile" in out
    cp = out["current_profile"]
    assert "org" in cp
    assert "org_size" in cp
    assert "current_tier_by_function" in cp
    assert "subcategory_scores" in cp


def test_uc_02_output_shape():
    """UC-02 output dict has the expected top-level keys."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    assert "six_function_radar" in out
    radar = out["six_function_radar"]
    # All 6 Functions must be present
    for fn in ("governance", "identify", "protect", "detect", "respond", "recover"):
        assert fn in radar, f"Missing Function in radar: {fn}"


def test_uc_03_output_shape():
    """UC-03 output dict has the expected top-level keys."""
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    assert "gap_subcategories" in out
    assert "gap_count" in out
    assert "cmmc_target" in out
    assert "crosswalk" in out


@pytest.mark.parametrize("uc_id,seed_name,expected_top_key", [
    ("UC-01", "uc-01-input.json", "current_profile"),
    ("UC-02", "uc-02-input.json", "six_function_radar"),
    ("UC-03", "uc-03-input.json", "gap_subcategories"),
])
def test_trace_each_uc(uc_id, seed_name, expected_top_key):
    """Each UC's seed input flows through to a recognizable output shape."""
    payload = _load(seed_name)
    out = run_skill(uc_id, payload)
    assert expected_top_key in out, f"{uc_id} missing top-level key {expected_top_key}"
    assert "classification" in out
