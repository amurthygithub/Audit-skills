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


# This skill's status convention (NOT a NIST scale — CSWP 29 defines no implementation-status
# scale; SP 1301's Profile example is explicitly notional/free-format)
VALID_STATUSES = ("Not Implemented", "Partially Implemented", "Largely Implemented", "Fully Implemented")
# Tier names per NIST CSF 2.0: T1=Partial, T2=Risk Informed, T3=Repeatable, T4=Adaptive.
# NIST applies Tiers to Organizational Profiles and they are not maturity levels; the
# per-Function values this stub emits are a labeled demo heuristic, not NIST methodology.
TIER_ORDER = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}

# All 6 GOVERN Categories per NIST CSF 2.0
GOVERN_CATEGORIES = ("GV.OC", "GV.RM", "GV.SC", "GV.PO", "GV.OV", "GV.RR")

# The four 800-171 Rev 2 families Apex targets first in UC-03 (CMMC L2 assesses
# 800-171 Rev 2 per 32 CFR 170.14(c)(3); Rev 2 has 14 families total)
CMMC_L2_DOMAINS = (
    "Access Control",
    "Identification & Authentication",
    "Configuration Management",
    "Incident Response",
)

ALL_FUNCTIONS = ("GV", "ID", "PR", "DE", "RS", "RC")


def _rollup_tier(scores: list[dict]) -> str:
    """Indicative Tier from Subcategory statuses — demo heuristic ONLY.

    Implementation status and Tier are separate concepts (a deployed tool is not
    "Repeatable" governance). Mapping: Not=1, Partially/Largely=2, Fully=3; take the
    median. A status-derived indicator can never exceed T3 (Tier 4's adaptive
    practices cannot be inferred from implementation status). No scored rows -> T1.
    """
    status_ord = {"Not Implemented": 1, "Partially Implemented": 2, "Largely Implemented": 2, "Fully Implemented": 3}
    if not scores:
        return "T1"
    ordinals = sorted(status_ord.get(s.get("status", "Not Implemented"), 1) for s in scores)
    mid = ordinals[len(ordinals) // 2]
    return f"T{mid}"


def _priority_gaps(scores: list[dict], n: int = 5) -> list[dict]:
    """Pick the n lowest-scoring Subcategories (largest delta from 'Fully Implemented')."""
    status_ord = {"Not Implemented": 0, "Partially Implemented": 1, "Largely Implemented": 2, "Fully Implemented": 3}
    ranked = sorted(
        scores,
        key=lambda s: (status_ord.get(s.get("status", "Not Implemented"), 0), s.get("subcategory_id", "")),
    )
    return [{"subcategory_id": s["subcategory_id"], "current_status": s["status"]} for s in ranked[:n]]


def _uc01_first_profile(inputs: dict) -> dict:
    """UC-01: Series-A SaaS builds first Organizational Profile."""
    subcategory_scores = inputs.get("subcategory_scores", [])
    by_function: dict[str, list[dict]] = {}
    for s in subcategory_scores:
        sc_id = s.get("subcategory_id", "")
        fn = sc_id.split(".")[0] if "." in sc_id else "GV"
        by_function.setdefault(fn, []).append(s)
    # Emit all 6 Functions; unscored Functions default to T1 (no evidence = Partial)
    current_tier_by_function = {fn: _rollup_tier(by_function.get(fn, [])) for fn in ALL_FUNCTIONS}
    return {
        "current_profile": {
            "org": inputs.get("org", {}).get("name", "DataRelay Inc."),
            "org_size": inputs.get("org", {}).get("size", "50 FTE"),
            "current_tier_by_function": current_tier_by_function,
            "subcategory_scores": subcategory_scores,
        },
        "gap_analysis": {
            "prioritization": _priority_gaps(subcategory_scores, n=5),
        },
        "classification": "FIRST_ORGANIZATIONAL_PROFILE",
    }


def _uc02_board_report(inputs: dict) -> dict:
    """UC-02: $20B regional bank produces board cyber maturity report."""
    raw_scores = inputs.get("function_scores", {})
    # Normalize to lowercase keys; backfill defaults. (Per-Function Tier values are the
    # org's own scoring convention — see chunks/02; NIST applies Tiers to Org Profiles.)
    radar: dict[str, str] = {}
    for fn in ("governance", "identify", "protect", "detect", "respond", "recover"):
        radar[fn] = raw_scores.get(fn, "T2")
    for fn, tier in radar.items():
        if tier not in TIER_ORDER:
            radar[fn] = "T2"
    return {
        "six_function_radar": radar,
        "govern_narrative": {
            "six_categories_covered": list(GOVERN_CATEGORIES),
        },
        "capital_plan_12mo": inputs.get("capital_plan_12mo", [
            {"investment_line": "Identity & Access Management modernization", "cost_estimate": "$400K", "owner": "CISO", "regulatory_rationale": "Supervisory expectation: FFIEC IT Examination Handbook (Information Security); 12 CFR 30 App. B"},
            {"investment_line": "Third-party risk management program", "cost_estimate": "$300K", "owner": "TPRM Lead", "regulatory_rationale": "Interagency TPRM Guidance (2023); NY DFS §500.11"},
            {"investment_line": "Security operations center uplift", "cost_estimate": "$500K", "owner": "SOC Director", "regulatory_rationale": "Supervisory expectation: FFIEC IT Examination Handbook (continuous monitoring)"},
            {"investment_line": "Disaster recovery & resilience testing", "cost_estimate": "$250K", "owner": "BCP Lead", "regulatory_rationale": "FFIEC Business Continuity Management booklet"},
            {"investment_line": "Cybersecurity training & awareness", "cost_estimate": "$150K", "owner": "People Security Lead", "regulatory_rationale": "NY DFS §500.14"},
            {"investment_line": "GRC tooling consolidation", "cost_estimate": "$400K", "owner": "GRC Director", "regulatory_rationale": "12 CFR 30 App. B (information security program governance)"},
        ]),
        "classification": "BOARD_MATURITY_REPORT",
    }


def _uc03_crosswalk(inputs: dict) -> dict:
    """UC-03: DoD supplier maps CSF 2.0 to 800-171 Rev 2 (the CMMC L2 set) for readiness.

    The crosswalk and readiness data come from the SEED (curated rows) — this stub
    performs no mapping logic. The fallbacks below are placeholders for malformed
    input, not a crosswalk.
    """
    lagging = inputs.get("lagging_subcategories", [])
    crosswalk = inputs.get("crosswalk", [
        {"subcategory_id": sid, "primary_800_171_control": "<unmapped — consult the NIST IR spreadsheet>", "practice_domain": "<unmapped>"}
        for sid in lagging
    ])
    cmmc_l2_readiness = inputs.get("cmmc_l2_readiness", [
        {"practice_domain": d, "controls_assessed": 0, "controls_satisfied": 0, "gap_count": 0}
        for d in CMMC_L2_DOMAINS
    ])
    return {
        "gap_subcategories": [{"subcategory_id": sid} for sid in lagging],
        "gap_count": len(lagging),
        "crosswalk": crosswalk,
        "cmmc_l2_readiness": cmmc_l2_readiness,
        "cmmc_target": inputs.get("cmmc_target", "L2"),
        "classification": "CSF_TO_800-171_L2_READINESS",
    }


def run_skill(uc_id: str, payload: dict) -> dict:
    """Top-level skill entrypoint. Dispatch by UC ID."""
    if uc_id == "UC-01":
        out = _uc01_first_profile(payload)
    elif uc_id == "UC-02":
        out = _uc02_board_report(payload)
    elif uc_id == "UC-03":
        out = _uc03_crosswalk(payload)
    else:
        return {
            "uc_id": uc_id,
            "error": f"Unknown uc_id: {uc_id!r}. Expected one of: {', '.join(VALID_UC_IDS)}.",
            "classification": "ERROR_UNKNOWN_UC",
        }
    out["uc_id"] = uc_id
    return out


VALID_UC_IDS = ("UC-01", "UC-02", "UC-03")


__all__ = ["run_skill", "VALID_STATUSES", "VALID_UC_IDS", "TIER_ORDER", "GOVERN_CATEGORIES", "CMMC_L2_DOMAINS"]
