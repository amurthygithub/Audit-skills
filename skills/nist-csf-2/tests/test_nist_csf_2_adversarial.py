"""Adversarial tests for nist-csf-2.

Feeds invalid/malformed inputs to the stub and asserts that the
skill degrades gracefully (returns an error in the output dict,
does not raise an unhandled exception).
"""

from __future__ import annotations

import pytest

from nist_csf_2_stub import run_skill, VALID_UC_IDS


def test_unknown_uc_id_returns_error():
    """An unknown UC id should return an error dict, not raise."""
    out = run_skill("UC-99", {"org_name": "Test"})
    assert "error" in out
    assert "UC-99" in out["error"] or "unknown" in out["error"].lower()


def test_empty_payload_still_returns_structured_output():
    """An empty payload should not crash; stub should return its baseline shape."""
    for uc_id in VALID_UC_IDS:
        out = run_skill(uc_id, {})
        # Every UC must return a dict with at least 'classification' and 'uc_id'
        assert isinstance(out, dict)
        assert "classification" in out
        assert out["uc_id"] == uc_id


def test_invalid_status_value_in_subcategory_score():
    """A Subcategory score with an invalid status value should be flagged."""
    payload = {
        "org": {"name": "Test", "fte": 50},
        "current_profile": {
            "subcategory_scores": {
                "GV.OC-01": {"status": "Mostly Implemented", "tier_indicator": 2},
            }
        },
    }
    out = run_skill("UC-01", payload)
    # Stub should either drop the invalid entry or surface a warning;
    # it should NOT crash.
    assert isinstance(out, dict)


def test_oversized_fte_handled():
    """A 100k-FTE org should still process (no off-by-one or list bounds issues)."""
    payload = {
        "org": {"name": "Mega Corp", "fte": 100_000, "sector": "saas-technology"},
        "current_profile": {"subcategory_scores": {}, "function_tiers": {}},
        "target_profile": {"function_tiers": {}},
    }
    out = run_skill("UC-01", payload)
    assert isinstance(out, dict)
    assert "classification" in out


def test_negative_remaining_budget_raises_no_exception():
    """A negative remaining budget should be processed (not raise)."""
    payload = {
        "org": {"name": "Test", "fte": 100, "sector": "financial-services"},
        "function_scores": {},
        "investment_capacity_usd": -1_000_000,
    }
    out = run_skill("UC-02", payload)
    assert isinstance(out, dict)
