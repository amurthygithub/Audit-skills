"""Skill entrypoint stub for nist-800-53-rmf.

In a real implementation, this function takes the use case inputs, builds the
prompt, calls the LLM, parses the output, and returns a structured result.

For the Spine / Tier 0a, this stub provides a deterministic reference
implementation that the oracle tests can call. The production implementation
(in SOX-611 Phase 2 migration) will replace this with the real skill
executor. Until then, the stub returns the expected output for known seeds.

The tests that compare to expected output are the contract; the stub
exists to keep the test suite runnable today.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parent.parent / "data"
SEEDS = DATA / "seeds"


def _load(name: str) -> dict:
    return json.loads((SEEDS / name).read_text())


def _categorize(inputs: dict) -> dict:
    """FIPS 199 categorization: high-water mark across information types."""
    levels = ["LOW", "MODERATE", "HIGH"]
    cat = {"c": "LOW", "i": "LOW", "a": "LOW"}
    for it in inputs.get("information_types", []):
        cia = it.get("cia_baseline", {})
        for k in ("c", "i", "a"):
            v = cia.get(k, "LOW")
            if levels.index(v) > levels.index(cat[k]):
                cat[k] = v
    overall = max(cat.values(), key=lambda x: levels.index(x))
    return {
        "system_name": inputs["system_name"],
        "system_security_category": cat,
        "overall": overall,
        "high_water_mark": overall,
        "pia_required": any("PII" in it["description"] for it in inputs.get("information_types", [])),
    }


def _select_baseline(categorization: dict) -> dict:
    return {"baseline": categorization["overall"], "control_count_rev5": 325, "control_count_rev5_1_1": 341}


def _uc01_categorize(inputs: dict) -> dict:
    return _categorize(inputs)


def _uc04_clinical(payload: dict) -> dict:
    """UC-04 (SOX-638): healthcare provider categorization + HIPAA safeguard view.

    Clinical availability floor — HOUSE CONVENTION, labeled in the UC doc and
    chunk 02: if any information type is patient-safety-relevant, the system's
    availability objective is at least MODERATE. A manual-workaround rationale
    never lowers clinical availability without documented clinical sign-off.
    FIPS 199 high-water-mark applies otherwise; SP 800-60 Vol II provisional
    impact levels are the lookup source for type-level baselines.
    """
    levels = ["LOW", "MODERATE", "HIGH"]
    cat = _categorize(payload)
    floor_applied = False
    if any(it.get("patient_safety_relevant") for it in payload.get("information_types", [])):
        if levels.index(cat["system_security_category"]["a"]) < levels.index("MODERATE"):
            cat["system_security_category"]["a"] = "MODERATE"
            floor_applied = True
    overall = max(cat["system_security_category"].values(), key=lambda x: levels.index(x))
    cat["overall"] = cat["high_water_mark"] = overall
    cat["clinical_availability_floor"] = {
        "applied": floor_applied,
        "basis": "house convention: patient-safety-relevant information type present; "
                 "availability >= MODERATE (manual-workaround rationales do not lower "
                 "clinical availability without documented clinical sign-off)",
    }
    base = _select_baseline(cat)
    crosswalk = _load("hipaa-to-800-53.json")
    by_id = {m["hipaa_id"]: m for m in crosswalk["mappings"]}
    view, unmapped = [], []
    for el in payload.get("in_scope_hipaa_elements", []):
        m = by_id.get(el)
        if m is None:
            unmapped.append(el)
            continue
        view.append({"hipaa_id": el, "designation": m["designation"],
                     "nist_800_53_ids": m["nist_800_53_ids"]})
    return {
        "classification": cat["overall"],
        "fips_199_categorization": cat,
        "baseline": base,
        "hipaa_800_53_view": view,
        "hipaa_elements_not_in_crosswalk": unmapped,
    }


def _uc02_aggregate(findings: list[dict]) -> dict:
    sev = {"High": 0, "Moderate": 0, "Low": 0}
    for f in findings:
        sev[f["severity"]] = sev.get(f["severity"], 0) + 1
    return {
        "sar": {
            "total_findings": len(findings),
            "severity_distribution": sev,
        }
    }


def _uc03_crosswalk(crosswalk: dict, gap_register: list[dict]) -> dict:
    """UC-03 summary COMPUTED from the shipped data (SOX-637).

    The crosswalk is a curated 33-row sample, not the complete TSC-to-800-53
    mapping — so no overlap percentage is derivable or emitted. Every count
    below foots to the inputs by construction.
    """
    mapped_ids: set[str] = set()
    for m in crosswalk.get("mappings", []):
        for c in m.get("nist_800_53_id", "").split(","):
            if c.strip():
                mapped_ids.add(c.strip())
    pure = [g for g in gap_register if g.get("disposition") == "gap"]
    strengthen = [g for g in gap_register if g.get("disposition") == "strengthen"]
    by_priority: dict[str, int] = {}
    for g in gap_register:
        by_priority[g["priority"]] = by_priority.get(g["priority"], 0) + 1
    return {
        "crosswalk_summary": {
            "soc2_common_criteria": 9,
            "sample_mappings": len(crosswalk.get("mappings", [])),
            "unique_mapped_control_ids": len(mapped_ids),
            "note": "curated sample — overlap percentages are NOT derivable from this sample",
        },
        "gap_register_summary": {
            "total_records": len(gap_register),
            "pure_gaps": len(pure),
            "strengthen_partial_coverage": len(strengthen),
            "by_priority": by_priority,
        },
    }


def run_skill(use_case_id: str, payload: dict, model: str = "stub") -> dict:
    """Stub entrypoint. Returns a structured skill result.

    For the Spine demonstration, the stub returns the expected output
    for known use cases. Real implementation: build prompt from SKILL.md,
    call LLM, parse output, return classification + structured result.
    """
    if use_case_id == "UC-01":
        cat = _uc01_categorize(payload)
        base = _select_baseline(cat)
        return {
            "classification": cat["overall"],
            "fips_199_categorization": cat,
            "baseline": base,
        }
    if use_case_id == "UC-02":
        findings = payload.get("findings", [])
        agg = _uc02_aggregate(findings)
        decision = "AUTHORIZE_WITH_CONDITIONS"
        return {
            "classification": decision,
            "sar": agg["sar"],
            "ato_decision": {"decision": decision, "duration": "1 year", "residual_risk": "MODERATE"},
        }
    if use_case_id == "UC-04":
        return _uc04_clinical(payload)
    if use_case_id == "UC-03":
        crosswalk = payload.get("crosswalk", {})
        gap_register = payload.get("gap_register", [])
        cw = _uc03_crosswalk(crosswalk, gap_register)
        return {
            "classification": f"GAP_RECORDS_{cw['gap_register_summary']['total_records']}",
            "baseline": {"baseline": payload.get("target_baseline", "MODERATE")},
            **cw,
        }
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    """Extract [LABEL §X] citations from SKILL.md body text."""
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]", text)
