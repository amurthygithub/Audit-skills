"""Oracle tests for sox-302-disclosure-controls (derivability, SOX-637)."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from sox_302_disclosure_controls_stub import run_skill

ROOT = Path(__file__).resolve().parent.parent
SEEDS = ROOT / "data" / "seeds"
FACT_SHEET = ROOT.parent.parent / "docs" / "sox-302-disclosure-controls-fact-sheet.md"


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def _fact_sheet():
    m = re.search(r"```yaml\n(.*?)\n```", FACT_SHEET.read_text(), re.DOTALL)
    return yaml.safe_load(m.group(1))


def test_uc_01_oracle():
    """A new unremediated MW in a disclosure-relevant area -> DC&P not effective; cascade foots."""
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)
    mw = payload["material_weakness"]
    expect_dcp = ("not effective" if (mw["affects_disclosure_relevant_area"] and not mw["remediated"])
                  else "effective")
    assert out["dcp_conclusion"] == expect_dcp == "not effective"
    assert out["classification"] == "DCP_NOT_EFFECTIVE"
    assert out["par5_disclosure_required"] is True  # an MW always triggers the 7241(a)(5) disclosure
    subs = payload["sub_certifications"]
    exc = sum(1 for s in subs if s["status"] == "exception")
    assert out["subcert_total"] == len(subs) == 14
    assert out["subcert_exceptions"] == exc
    assert out["subcert_clean"] == len(subs) - exc
    assert out["top_level_cert_clean"] is False
    expected = _load("uc-01-expected.json")
    assert expected["dcp_conclusion"] == out["dcp_conclusion"]
    assert expected["subcert_exceptions"] == out["subcert_exceptions"]


def test_uc_02_oracle():
    """Newly-public: §302 applies from the first periodic report; §404(b) exempt; DC&P scope full."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    inv = payload["disclosure_inventory"]
    assert out["section_302_certification_required"] is True  # no newly-public exemption from 302
    assert out["section_404b_auditor_attestation_required"] is False  # newly-public / EGC exempt
    assert out["classification"] == "FIRST_302_404B_EXEMPT"
    assert out["dcp_scope_count"] == len(inv)  # financial + non-financial
    assert out["icfr_scope_count"] == sum(1 for d in inv if d["category"] == "financial")
    assert out["dcp_scope_count"] > out["icfr_scope_count"]  # DC&P strictly broader than ICFR here
    assert out["cyber_8k_in_dcp_scope"] is True
    expected = _load("uc-02-expected.json")
    assert expected["section_404b_auditor_attestation_required"] == out["section_404b_auditor_attestation_required"]


def test_uc_03_oracle():
    """15-entity cascade: coverage + gaps recomputed; FPI annual-vs-quarterly split derived."""
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    ents = payload["entities"]
    gaps = [e["entity"] for e in ents if not e["covered"]]
    assert out["entities_total"] == len(ents) == 15
    assert out["entities_covered"] == sum(1 for e in ents if e["covered"])
    assert out["coverage_gaps"] == gaps
    assert out["entities_covered"] + len(out["coverage_gaps"]) == out["entities_total"]  # footing
    assert out["quarterly_eval_entities"] == sum(1 for e in ents if e["type"] == "domestic")
    assert out["annual_eval_entities"] == sum(1 for e in ents if e["type"] == "fpi")
    assert out["quarterly_eval_entities"] + out["annual_eval_entities"] == out["entities_total"]
    expected = _load("uc-03-expected.json")
    assert expected["coverage_gaps"] == out["coverage_gaps"]


def test_fact_sheet_inventory_diff():
    """Counts the skill states must match the fact sheet §0 — standing inventory-diff gate."""
    c = _fact_sheet()["counts"]
    assert c["certification_elements_302a"] == 6
    assert c["cert_paragraphs_in_exhibit"] == 6
    assert c["signing_officers"] == 2
    assert c["implementing_rules_core"] == 4
    assert c["reg_sk_items"] == 3
    ids = {r["code"] for r in _fact_sheet()["identifiers"]}
    for must in ("17 CFR 240.13a-15(e)", "17 CFR 240.13a-15(f)", "15 U.S.C. 7241", "Reg S-K Item 307"):
        assert must in ids
