"""Skill entrypoint stub for hipaa-security-rule.

Deterministic reference implementation for the Spine / Tier 0a test suite.
The production LLM-backed executor replaces this in a later phase; until then
the seed + oracle pair is the contract and this stub computes — it never
echoes fixture numbers (derivability oracles, SOX-637 pattern).

House conventions implemented here (labeled as such in the chunks and UC docs;
they are NOT from 45 CFR 164 or any NIST publication):
  - UC-01 risk score = likelihood (1-3) x impact (1-3); bands Low <=2, Medium 3-4, High >=6.
  - UC-02 gap priority: standard status 'missing' -> High, 'partial' -> Medium,
    stale policy document -> Low. Review staleness threshold is the engagement's
    review_cycle_years input (the regulation says "periodically", 164.316(b)(2)(iii),
    with no stated cadence).

Regulatory logic implemented here (this IS from the rule):
  - Addressable disposition per 164.306(d)(3): assess; implement if reasonable and
    appropriate; otherwise document why not and implement an equivalent alternative
    measure if reasonable and appropriate.
  - UC-03 BAA required provisions per 164.314(a)(2)(i)(A)-(C) plus 164.308(b)(3).
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parent.parent / "data"
SEEDS = DATA / "seeds"

RISK_BANDS = [(6, "High"), (3, "Medium"), (0, "Low")]  # house convention, labeled

BAA_REQUIRED_PROVISIONS = [
    # 164.314(a)(2)(i)(A): comply with the applicable requirements of Subpart C
    "comply_with_subpart",
    # 164.314(a)(2)(i)(B): subcontractor flow-down per 164.308(b)(2)
    "subcontractor_flowdown",
    # 164.314(a)(2)(i)(C): report security incidents incl. 164.410 breaches
    "incident_reporting",
    # 164.308(b)(3): written contract or other arrangement
    "written_contract",
]

# UC-03 checklist mapping: system -> [(cfr_cite, action, scaled_down, scaling_rationale)].
# Cites must exist in the fact-sheet identifier list (asserted by the oracle).
# scaled_down means right-sized via the 164.306(b)(2) flexibility factors —
# never skipped: Required specs stay required at every org size.
_BASE_CHECKLIST = [
    ("164.308(a)(1)(ii)(A)", "Conduct and document a risk analysis covering every system touching ePHI", False, None),
    ("164.308(a)(2)", "Designate a security official", True,
     "size factor 164.306(b)(2)(i): the solo practitioner serves as the security official; designation is documented, not delegated"),
    ("164.308(a)(5)", "Complete and document annual security awareness training", True,
     "size factor 164.306(b)(2)(i): a formal multi-role training program is scaled to documented annual self-administered training"),
    ("164.316(b)(2)(i)", "Retain all Subpart C documentation for 6 years", False, None),
]
_SYSTEM_CHECKLIST = {
    "laptop": [
        ("164.310(c)", "Physically secure the workstation; auto-lock screen; full-disk encryption", False, None),
        ("164.312(a)(2)(iv)", "Encrypt local storage (addressable — document the implement decision)", False, None),
    ],
    "saas_ehr_access": [
        ("164.308(a)(4)", "Limit EHR access to the minimum accounts and roles the engagement requires", False, None),
        ("164.312(d)", "Authenticate every EHR session under the consultant's own identity — "
         "enable MFA where the EHR offers it (good practice; an MFA mandate is NPRM-PROPOSED, "
         "not current Subpart C)", False, None),
    ],
    "email": [
        ("164.312(e)(1)", "Use encrypted transmission for any message carrying ePHI", False, None),
    ],
    "cloud_storage": [
        ("164.308(a)(7)(ii)(A)", "Maintain retrievable exact copies of any ePHI the practice stores", True,
         "size factor 164.306(b)(2)(i): provider-managed versioned storage satisfies the backup requirement for a solo practice"),
    ],
}


def _load(name: str) -> Any:
    return json.loads((SEEDS / name).read_text())


def _risk_band(score: int) -> str:
    for floor, name in RISK_BANDS:
        if score >= floor:
            return name
    return "Low"


def _disposition(spec: dict) -> str:
    """164.306(d)(3) decision logic."""
    if spec.get("reasonable_and_appropriate"):
        return "implement"
    if spec.get("alternative"):
        return "alternative_measure"
    return "not_reasonable_documented"


def _uc01(payload: dict) -> dict:
    risks = payload["risks"]
    register = payload["addressable_register"]
    by_band: dict[str, int] = {}
    register_rows = []
    for r in risks:
        score = r["likelihood"] * r["impact"]
        b = _risk_band(score)
        by_band[b] = by_band.get(b, 0) + 1
        register_rows.append({**r, "score": score, "band": b})
    dispositions = []
    summary: dict[str, int] = {}
    for spec in register:
        d = _disposition(spec)
        summary[d] = summary.get(d, 0) + 1
        dispositions.append({
            "spec_id": spec["spec_id"], "name": spec["name"], "family": spec["family"],
            "decision_required": spec["decision_required"], "disposition": d,
            "alternative": spec.get("alternative"),
            "justification": spec.get("justification"),
            # 164.306(d)(3)(ii)(B)(2): on the not-reasonable path the equivalent-
            # alternative question must be answered even when the answer is "none".
            "alternative_considered": spec.get("alternative_considered"),
        })
    enc = next((d for d in dispositions if d["spec_id"] == "164.312(a)(2)(iv)"),
               {"disposition": "not_assessed"})
    return {
        "classification": f"RISKS_{len(risks)}_HIGH_{by_band.get('High', 0)}",
        "risk_register": register_rows,
        "risk_summary": {"total": len(risks), "by_band": by_band},
        "addressable_dispositions": dispositions,
        "disposition_summary": summary,
        "decision_required_count": sum(1 for s in register if s["decision_required"]),
        "encryption_at_rest_disposition": enc["disposition"],
        "scale_note": payload.get("scale_note",
            "house convention: score = likelihood x impact; bands Low <=2, Medium 3-4, High >=6"),
    }


def _parse_date(s: str) -> date:
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)


def _uc02(payload: dict) -> dict:
    inventory = payload["control_inventory"]
    docs = payload["documentation_register"]
    as_of = _parse_date(payload["as_of_date"])
    cycle_days = payload.get("review_cycle_years", 3) * 365.25
    status_counts: dict[str, int] = {}
    matrix = []
    for row in inventory:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
        matrix.append({k: row[k] for k in ("standard_id", "name", "family", "status")})
    stale = sorted(d["doc_id"] for d in docs
                   if (as_of - _parse_date(d["last_reviewed"])).days > cycle_days)
    gaps = []
    for row in inventory:
        if row["status"] == "missing":
            gaps.append({"standard_id": row["standard_id"], "priority": "High",
                         "basis": "standard not implemented (all Subpart C standards are mandatory)"})
        elif row["status"] == "partial":
            gaps.append({"standard_id": row["standard_id"], "priority": "Medium",
                         "basis": "standard partially implemented"})
    for doc_id in stale:
        gaps.append({"standard_id": doc_id, "priority": "Low",
                     "basis": "policy document past the engagement review cycle (house parameter; "
                              "the rule requires periodic review without a stated cadence)"})
    pri: dict[str, int] = {}
    for g in gaps:
        pri[g["priority"]] = pri.get(g["priority"], 0) + 1
    return {
        "classification": f"READINESS_GAPS_{len(gaps)}",
        "readiness_matrix": matrix,
        "readiness_summary": {"total": len(inventory), **status_counts},
        "gap_register": gaps,
        "gap_priorities": pri,
        "stale_docs": stale,
        # NPRM pre-read is narrative-only and always flagged PROPOSED; it never
        # contributes records to the current-law gap register.
        "nprm_items_in_current_law_gaps": 0,
    }


def _uc03(payload: dict) -> dict:
    clauses = payload["baa_terms"]["proposed_clauses"]
    present = {c["provision"] for c in clauses}
    missing = sorted(p for p in BAA_REQUIRED_PROVISIONS if p not in present)
    checklist = list(_BASE_CHECKLIST)
    for system in payload["org"]["systems"]:
        checklist.extend(_SYSTEM_CHECKLIST.get(system, []))
    items = [{"cfr_cite": c, "action": a, "scaled_down": s,
              **({"scaling_rationale": r} if s else {})}
             for c, a, s, r in checklist]
    return {
        "classification": f"BAA_MISSING_{len(missing)}",
        "baa_check": {
            "required_provisions": BAA_REQUIRED_PROVISIONS,
            "present_provisions": sorted(present & set(BAA_REQUIRED_PROVISIONS)),
            "missing_provisions": missing,
        },
        "safeguard_checklist": items,
        "checklist_summary": {
            "items": len(items),
            "scaled_down": sum(1 for i in items if i["scaled_down"]),
        },
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
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]", text)
