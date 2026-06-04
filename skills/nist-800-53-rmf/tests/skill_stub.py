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


def _uc03_crosswalk(crosswalk: dict) -> dict:
    s = crosswalk.get("summary", {})
    return {
        "crosswalk_summary": {
            "soc2_common_criteria": 9,
            "nist_800_53_mod_controls": 325,
            "mapped_controls": 231,
            "gap_controls": 94,
            "overlap_pct": 71,
        }
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
    if use_case_id == "UC-03":
        crosswalk = payload.get("crosswalk", {})
        cw = _uc03_crosswalk(crosswalk)
        return {
            "classification": cw["crosswalk_summary"]["gap_controls"],
            "baseline": {"baseline": "MODERATE"},
            **cw,
        }
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    """Extract [LABEL §X] citations from SKILL.md body text."""
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]", text)
