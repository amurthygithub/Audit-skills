"""Skill entrypoint stub for nist-csf-2.

In a real implementation, this function takes the use case inputs, builds the
prompt, calls the LLM, parses the output, and returns a structured result.

For the Spine / Tier 0a, this stub provides a deterministic reference
implementation that the oracle tests can call. The production implementation
(in a future SOX-611 Phase 2 migration) will replace this with the real skill
executor. Until then, the stub returns the expected output for known seeds.

The tests that compare to expected output are the contract; the stub
exists to keep the test suite runnable today.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parent.parent / "data"
SEEDS = DATA / "seeds"


def _load(name: str) -> dict:
    return json.loads((SEEDS / name).read_text())


# CSF 2.0 status enum per NIST CSWP 29 §3.2
VALID_STATUSES = ("Not Implemented", "Partially Implemented", "Largely Implemented", "Fully Implemented")
# Tier enum per NIST CSF 2.0 §3.1: T1=Partial, T2=Risk Informed, T3=Repeatable, T4=Adaptive
TIER_ORDER = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}


def _rollup_tier(scores: list[dict]) -> str:
    """Function-level Tier rollup from Subcategory status scores.

    Heuristic: take the median status ordinal (Not=0, Partially=1, Largely=2, Fully=3)
    and map to Tier: 0→T1, 1→T2, 2→T3, 3→T4. For mixed scores, the median is the
    conservative-but-fair rollup. Real engagements would use a more nuanced rollup
    (e.g., penalty for any "Not Implemented" Subcategory); the heuristic is a
    starting point and should be refined in Wave 3.
    """
    status_ord = {"Not Implemented": 0, "Partially Implemented": 1, "Largely Implemented": 2, "Fully Implemented": 3}
    if not scores:
        return "T1"
    ordinals = sorted(status_ord.get(s.get("status", "Not Implemented"), 0) for s in scores)
    mid = ordinals[len(ordinals) // 2]
    if mid <= 0:
        return "T1"
    if mid == 1:
        return "T2"
    if mid == 2:
        return "T3"
    return "T4"


def _uc01_first_profile(inputs: dict) -> dict:
    """UC-01: Series-A SaaS builds first Organizational Profile.

    Inputs: {"org": {...}, "current_practices": {...}, "target_tier": 3}

    The 6 representative Subcategory scores are illustrative; real engagements
    would carry 106 Subcategory scores in the seed input.
    """
    subcategory_scores = inputs.get("subcategory_scores", [])
    current_tier_by_function: dict[str, str] = {}
    # Group scores by Function letter prefix
    by_function: dict[str, list[dict]] = {}
    for s in subcategory_scores:
        sc_id = s.get("subcategory_id", "")
        # CSF 2.0 Subcategory IDs are like GV.OC-01, ID.AM-01, etc. Function = first 2 chars
        fn = sc_id.split(".")[0] if "." in sc_id else "GV"
        by_function.setdefault(fn, []).append(s)
    for fn, scores in by_function.items():
        current_tier_by_function[fn] = _rollup_tier(scores)
    return {
        "current_profile": {
            "org": inputs.get("org", {}).get("name", "DataRelay Inc."),
            "org_size": inputs.get("org", {}).get("size", "50 FTE"),
            "current_tier_by_function": current_tier_by_function,
            "subcategory_scores": subcategory_scores,
        },
        "classification": "FIRST_ORGANIZATIONAL_PROFILE",
    }


def _uc02_board_report(inputs: dict) -> dict:
    """UC-02: $20B regional bank produces board cyber maturity report.

    Inputs: {"org": {...}, "function_scores": {...6 Tiers...}, "investment_capacity": "$2M"}
    """
    function_scores = inputs.get("function_scores", {})
    # The 6 Functions: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER
    for fn in ("GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND", "RECOVER"):
        function_scores.setdefault(fn, "T2")
    # Sanity-check tier values
    for fn, tier in function_scores.items():
        if tier not in TIER_ORDER:
            function_scores[fn] = "T2"
    return {
        "six_function_radar": function_scores,
        "classification": "BOARD_MATURITY_REPORT",
    }


def _uc03_crosswalk(inputs: dict) -> dict:
    """UC-03: Mid-market DoD supplier maps CSF 2.0 to 800-171 Rev 3 for CMMC L2.

    Inputs: {"org": {...}, "lagging_subcategories": [14 IDs], "cmmc_target": "L2"}
    """
    lagging = inputs.get("lagging_subcategories", [])
    return {
        "gap_subcategories": [{"subcategory_id": sid} for sid in lagging],
        "gap_count": len(lagging),
        "cmmc_target": inputs.get("cmmc_target", "L2"),
        "classification": "CSF_TO_800-171_L2_READINESS",
    }


def run_skill(uc_id: str, payload: dict) -> dict:
    """Top-level skill entrypoint. Dispatch by UC ID."""
    if uc_id == "UC-01":
        return _uc01_first_profile(payload)
    if uc_id == "UC-02":
        return _uc02_board_report(payload)
    if uc_id == "UC-03":
        return _uc03_crosswalk(payload)
    raise ValueError(f"Unknown uc_id: {uc_id!r}. Expected one of: UC-01, UC-02, UC-03.")


__all__ = ["run_skill", "VALID_STATUSES", "TIER_ORDER"]
