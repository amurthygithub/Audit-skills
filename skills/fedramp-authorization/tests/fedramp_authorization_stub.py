"""Skill entrypoint stub for fedramp-authorization.

Deterministic reference executor (Spine / Tier 0a). The seed + oracle pair is the
contract; this stub COMPUTES its outputs from the seed facts (derivability oracles,
SOX-637 pattern) — it does not echo a hardcoded result. The production LLM-backed
executor replaces it later.

Program logic implemented here (from the public sources, fact sheet §0):
  - UC-01 (B34): FIPS 199 categorization is the HIGH-WATER MARK across C/I/A
    (Low<Moderate<High); the selected FedRAMP Rev 5 baseline follows from the
    overall impact (Low 156 / Moderate 323 / High 410); each SAR finding's POA&M
    remediation deadline = identified_date + the FedRAMP ConMon SLA for its
    severity (high/critical 30 days, moderate 90, low 180).
  - UC-02 (B35): LI-SaaS (Tailored) eligibility = overall impact Low AND SaaS
    delivery. The Tailored baseline is 156 controls split 66 3PAO-tested + 90
    CSP-attested. Moderate+SaaS is NOT LI-SaaS — it takes the full Moderate baseline.
  - UC-03 (B36): a 3PAO SAR finding roll-up. A finding is a control the CSP OWNS
    (not inherited/leveraged) that FAILED testing; inherited-and-failed controls
    are the provider's POA&M, not the leveraging CSP's. POA&M item count = findings;
    residual high-severity findings are a risk signal for the authorizing official
    (the ATO decision itself is the AO's, not derivable here).

Counts (156/323/410, 66/90) are framework constants taken from the PMO-authored
OSCAL Rev 5 baseline profiles (fact sheet §0); the derivation is the seed-driven
SELECTION/computation, not the constants.
"""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parent.parent / "data"
SEEDS = DATA / "seeds"

# FIPS 199 ordering for the high-water-mark categorization.
_LEVEL_ORDER = {"Low": 1, "Moderate": 2, "High": 3}
_ORDER_LEVEL = {v: k for k, v in _LEVEL_ORDER.items()}

# FedRAMP Rev 5 baseline control totals (base + enhancements) — counted from the
# PMO-authored OSCAL profiles (fact sheet §0). LI-SaaS shares Low's 156.
BASELINE_CONTROLS = {"Low": 156, "Moderate": 323, "High": 410}
LI_SAAS_CONTROLS = 156
LI_SAAS_3PAO_TESTED = 66
LI_SAAS_ATTESTED = 90

# FedRAMP ConMon remediation SLAs (days) by finding severity.
REMEDIATION_SLA_DAYS = {"Critical": 30, "High": 30, "Moderate": 90, "Low": 180}


def _load(name: str) -> Any:
    return json.loads((SEEDS / name).read_text())


def _high_water_mark(fips199: dict) -> str | None:
    """Overall FIPS 199 impact = the max across confidentiality/integrity/availability."""
    levels = [fips199.get(k) for k in ("confidentiality", "integrity", "availability")]
    if any(lvl not in _LEVEL_ORDER for lvl in levels):
        return None
    return _ORDER_LEVEL[max(_LEVEL_ORDER[lvl] for lvl in levels)]


def _uc01(payload: dict) -> dict:
    fips = payload.get("fips199")
    if not fips:
        return {"classification": "INSUFFICIENT_INPUT",
                "basis": "No FIPS 199 categorization supplied — cannot select a baseline."}
    impact = _high_water_mark(fips)
    if impact is None:
        return {"classification": "INSUFFICIENT_INPUT",
                "basis": "FIPS 199 objectives must each be Low/Moderate/High."}
    poam = []
    for f in payload.get("sar_findings", []):
        sev = f.get("severity", "Low")
        sla = REMEDIATION_SLA_DAYS.get(sev, 180)
        due = ""
        if f.get("identified_date"):
            d = date.fromisoformat(f["identified_date"])
            due = (d + timedelta(days=sla)).isoformat()
        poam.append({"id": f.get("id"), "severity": sev, "remediation_due": due})
    return {
        "classification": f"FEDRAMP_{impact.upper()}",
        "overall_impact": impact,
        "baseline": impact,
        "baseline_controls": BASELINE_CONTROLS[impact],
        "poam_open": len(poam),
        "poam": poam,
    }


def _uc02(payload: dict) -> dict:
    fips = payload.get("fips199")
    if not fips or "saas_delivery" not in payload:
        return {"classification": "INSUFFICIENT_INPUT",
                "basis": "Need FIPS 199 categorization and the saas_delivery flag for LI-SaaS eligibility."}
    impact = _high_water_mark(fips)
    if impact is None:
        return {"classification": "INSUFFICIENT_INPUT",
                "basis": "FIPS 199 objectives must each be Low/Moderate/High."}
    eligible = impact == "Low" and bool(payload.get("saas_delivery"))
    if eligible:
        return {
            "classification": "LI_SAAS_ELIGIBLE",
            "overall_impact": impact,
            "li_saas_eligible": True,
            "baseline": "LI-SaaS",
            "baseline_controls": LI_SAAS_CONTROLS,
            "controls_3pao_tested": LI_SAAS_3PAO_TESTED,
            "controls_attested": LI_SAAS_ATTESTED,
        }
    # Not LI-SaaS: a Moderate/High SaaS (or a non-SaaS Low) takes the full baseline.
    return {
        "classification": "LI_SAAS_INELIGIBLE",
        "overall_impact": impact,
        "li_saas_eligible": False,
        "baseline": impact,
        "baseline_controls": BASELINE_CONTROLS[impact],
        "basis": ("Moderate/High impact is not LI-SaaS-eligible — LI-SaaS Tailored is Low-impact only"
                  if impact != "Low" else "Low impact but not SaaS-delivered — full Low baseline"),
    }


def _uc03(payload: dict) -> dict:
    controls = payload.get("controls", [])
    inherited = [c for c in controls if c.get("inherited")]
    # A finding = a control the CSP OWNS (not inherited) that FAILED testing.
    findings = [c for c in controls
                if c.get("tested") and not c.get("passed") and not c.get("inherited")]
    by_sev: dict[str, int] = {}
    for c in findings:
        sev = c.get("severity") or "Unspecified"
        by_sev[sev] = by_sev.get(sev, 0) + 1
    has_high = any((c.get("severity") in ("High", "Critical")) for c in findings)
    note = ("residual high-severity finding(s) present — authorizing official risk acceptance "
            "required before an ATO decision" if has_high
            else "no residual high-severity findings in the CSP-owned control set")
    return {
        "classification": f"SAR_FINDINGS_{len(findings)}",
        "controls_total": len(controls),
        "controls_tested_own": sum(1 for c in controls if c.get("tested") and not c.get("inherited")),
        "inherited_count": len(inherited),
        "findings": [c.get("id") for c in findings],
        "poam_item_count": len(findings),
        "findings_by_severity": by_sev,
        "has_high_severity_finding": has_high,
        "recommendation_note": note,
    }


def run_skill(use_case_id: str, payload: dict, model: str = "stub") -> dict:
    if use_case_id == "UC-01":
        return _uc01(payload)
    if use_case_id == "UC-02":
        return _uc02(payload)
    if use_case_id == "UC-03":
        return _uc03(payload)
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    """Extract [LABEL §X] citations from SKILL.md body text."""
    return re.findall(r"\[([A-Za-z0-9][A-Za-z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]", text)
