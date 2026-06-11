"""Skill entrypoint stub for sox-302-disclosure-controls.

Deterministic reference executor (Spine / Tier 0a). The seed + oracle pair is the
contract; this stub COMPUTES its outputs from the seed facts (derivability oracles,
SOX-637 pattern). The production LLM-backed executor replaces it later.

Regulatory logic implemented here (from the public sources, fact sheet §0):
  - UC-01: a §302 DC&P effectiveness conclusion. An UNREMEDIATED material weakness in
    a disclosure-relevant area means DC&P is "not effective" for that area (13a-15(e) /
    Item 307). Any SD/MW triggers the cert ¶5 disclosure to the auditors and audit
    committee (15 U.S.C. 7241(a)(5)). Sub-cert cascade roll-up (a house framework).
  - UC-02: obligations for a newly-public filer. §302 certification applies from the
    first periodic report (no newly-public/EGC exemption). §404(b) auditor attestation
    is exempt for a newly-public filer / EGC. DC&P scope = ALL disclosure items
    (financial AND non-financial); ICFR scope = the financial subset.
  - UC-03: the multi-entity sub-cert cascade — coverage and the FPI annual-vs-quarterly
    DC&P-evaluation split (13a-15(b): domestic each quarter; FPI each fiscal year).
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parent.parent / "data"
SEEDS = DATA / "seeds"


def _load(name: str) -> Any:
    return json.loads((SEEDS / name).read_text())


def _uc01(payload: dict) -> dict:
    mw = payload.get("material_weakness")
    subs = payload.get("sub_certifications", [])
    if mw is None:
        return {"classification": "INSUFFICIENT_INPUT",
                "basis": "No material-weakness facts supplied — cannot conclude on DC&P effectiveness."}
    # 13a-15(e)/Item 307: an unremediated MW in a disclosure-relevant area -> DC&P not effective.
    dcp = ("not effective" if (mw.get("affects_disclosure_relevant_area") and not mw.get("remediated"))
           else "effective")
    exceptions = [s for s in subs if s.get("status") == "exception"]
    return {
        "classification": f"DCP_{'NOT_EFFECTIVE' if dcp == 'not effective' else 'EFFECTIVE'}",
        "dcp_conclusion": dcp,
        # 15 U.S.C. 7241(a)(5): officers disclose all SD/MW (and any management fraud) to
        # the auditors and the audit committee — triggered by the existence of an MW.
        "par5_disclosure_required": True,
        "subcert_total": len(subs),
        "subcert_exceptions": len(exceptions),
        "subcert_clean": len(subs) - len(exceptions),
        "top_level_cert_clean": dcp == "effective" and len(exceptions) == 0,
    }


def _uc02(payload: dict) -> dict:
    f = payload.get("filer")
    inv = payload.get("disclosure_inventory", [])
    if not f or "newly_public" not in f:
        return {"classification": "INSUFFICIENT_INPUT",
                "basis": "Filer status (newly_public / egc / accelerated) not supplied."}
    s404b_exempt = bool(f.get("newly_public")) or bool(f.get("egc"))
    dcp_scope = [d["item"] for d in inv]
    icfr_scope = [d["item"] for d in inv if d.get("category") == "financial"]
    return {
        "classification": "FIRST_302_404B_EXEMPT" if s404b_exempt else "FIRST_302_404B_REQUIRED",
        # §302 applies from the first periodic report — there is no newly-public/EGC exemption.
        "section_302_certification_required": True,
        # §404(a) management ICFR assessment is required, but first in the first ANNUAL report.
        "section_404a_management_assessment_required": True,
        # §404(b) auditor attestation is exempt for a newly-public filer / EGC.
        "section_404b_auditor_attestation_required": not s404b_exempt,
        "dcp_scope_count": len(dcp_scope),
        "icfr_scope_count": len(icfr_scope),
        "cyber_8k_in_dcp_scope": any("8-K Item 1.05" in d.get("item", "") for d in inv),
    }


def _uc03(payload: dict) -> dict:
    ents = payload.get("entities", [])
    covered = [e for e in ents if e.get("covered")]
    gaps = [e["entity"] for e in ents if not e.get("covered")]
    quarterly = [e for e in ents if e.get("type") == "domestic"]
    annual = [e for e in ents if e.get("type") == "fpi"]
    return {
        "classification": f"CASCADE_GAPS_{len(gaps)}",
        "entities_total": len(ents),
        "entities_covered": len(covered),
        "coverage_gaps": gaps,
        "fully_covered": len(gaps) == 0,
        "quarterly_eval_entities": len(quarterly),
        "annual_eval_entities": len(annual),
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
