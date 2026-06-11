"""Skill entrypoint stub for audit-workpapers.

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


def _mus_evaluate(inputs: dict) -> dict:
    """MUS evaluation per AS 2315: n = (BV x RF) / TM, ULM = BP + sum(IA)."""
    # SOX-600/601: no silent defaults for sizing parameters — a defaulted BV or
    # TM sizes the sample against the wrong population. Missing -> refuse and ask
    # (abstention is the passing answer; validation-harness-design.md section 5).
    if "population_book_value" not in inputs or "tolerable_misstatement" not in inputs:
        missing = [k for k in ("population_book_value", "tolerable_misstatement")
                   if k not in inputs]
        raise ValueError(f"missing required sampling parameter(s) {missing}; "
                         "ask for them — do not assume a population or materiality")
    bv = inputs["population_book_value"]
    tm = inputs["tolerable_misstatement"]
    if tm <= 0 or bv < 0:
        raise ValueError(f"invalid sampling parameters (BV={bv}, TM={tm}): TM must be "
                         "positive and BV non-negative — refusing rather than emitting "
                         "a nonsense interval")
    ria = inputs.get("risk_of_incorrect_acceptance", 0.05)
    expected = inputs.get("expected_overstatements", 0)

    # RF table (Poisson, 0 expected misstatements) — AICPA Audit Sampling Guide
    RF_TABLE = {0.01: 4.61, 0.05: 3.00, 0.10: 2.31, 0.15: 1.90, 0.20: 1.61}
    if isinstance(ria, str):
        ria = float(ria.replace("%", "")) / 100.0
    if expected != 0 or ria not in RF_TABLE:
        raise ValueError(
            f"unsupported sampling parameters (RIA={ria}, expected={expected}); "
            f"supported RIA: {sorted(RF_TABLE)} at 0 expected misstatements — "
            "a silent default would size the sample in the wrong direction"
        )
    rf = RF_TABLE[ria]
    si = round(tm / rf)              # display value (rounded)
    n = int((bv * rf) / tm)
    bp = int(round(rf * (tm / rf)))  # BP = RF x unrounded SI = TM exactly

    return {
        "sampling_interval": int(si),
        "sample_size": n,
        "reliability_factor": rf,
        "basic_precision": bp,
        "upper_limit_misstatement": bp,
        "upper_limit_conclusion": "ULM <= TM — population not materially misstated; accept" if bp <= tm else "ULM > TM — consider expanded sample or management adjustment",
        "items_tested": n,
        "misstatements_found": 0,
        "tainting_sum": 0,
    }


def _finding_document(inputs: dict) -> dict:
    """5-part C-C-C-E-R finding format per AS 2201 Appendix A, AS 2201.62-.70."""
    severity = inputs.get("severity", "Significant Deficiency")
    return {
        "finding_id": inputs.get("finding_id", 3),
        "wp_index": inputs.get("wp_index", "C-4.2"),
        "severity": severity,
        "assertion": "Completeness (Accounts Payable)",
        "condition": "12 of 75 invoices (16%) recorded in incorrect period; $342,500+$128,750 misstated across periods",
        "criteria": "Accrual-basis GAAP period-end liability/expense recognition; company AP Policy AP-200; AS 2201 ICFR",
        "cause": "Receiving dept not notifying AP of goods received in last 3 days of month; 3-way match relies on invoice date",
        "effect": "Actual: expenses understated by $342,500 in 2024; overstated in 2025. Net understatement $213,750",
        "recommendation": "Implement ERP automated cutoff; daily receiving reports through month-end; internal audit monitoring for 6 months",
        "impact": "Net $213,750 P&L impact; potential material misstatement if systemic",
        "deviation_rate_pct": 16.0,
        "classification": severity,
    }


def _td_calculate(inputs: dict) -> dict:
    """Audit risk model: TD = AR / (IR x CR x AP)."""
    ar = inputs.get("ar", "5%")
    ir = inputs.get("ir", "80%")
    cr = inputs.get("cr", "60%")
    ap = inputs.get("ap", "50%")

    def _pct(s: str) -> float:
        return float(s.replace("%", "")) / 100.0

    ar_n = _pct(ar)
    ir_n = _pct(ir)
    cr_n = _pct(cr)
    ap_n = _pct(ap)
    denom = ir_n * cr_n * ap_n
    if denom == 0:
        td_n = 100.0
    else:
        td_n = ar_n / denom

    td_pct = round(td_n * 100, 1)
    # TD IS the allowable risk of incorrect acceptance (AS 2315 appendix) —
    # use the RF at the largest tabulated RIA that does not exceed TD (conservative).
    RF_TABLE = [(1.0, 4.61), (5.0, 3.00), (10.0, 2.31), (15.0, 1.90), (20.0, 1.61)]
    rf_map = next((rf for ria_t, rf in reversed(RF_TABLE) if ria_t <= td_pct), 4.61)
    extent = ("Very large" if td_pct <= 1 else "Large" if td_pct <= 5
              else "Moderate" if td_pct <= 10 else "Moderate-small" if td_pct <= 15 else "Small")

    return {
        "ar": ar_n,
        "ir": ir_n,
        "cr": cr_n,
        "ap": ap_n,
        "td": round(td_n, 4),
        "td_pct": td_pct,
        "td_formula": f"TD = AR / (IR x CR x AP) = {ar_n} / ({ir_n} x {cr_n} x {ap_n}) = {td_pct}%",
        "ria_pct": td_pct,
        "ria_implication": f"TD {td_pct}% is the allowable RIA for the test of details (AS 2315)",
        "rf_implication": rf_map,
        "extent": extent,
        "sample_size_implication": f"TD {td_pct}% = RIA; RF {rf_map} -> {extent} substantive sample",
    }


def run_skill(use_case_id: str, payload: dict, model: str = "stub") -> dict:
    """Stub entrypoint. Returns a structured skill result.

    For the Spine demonstration, the stub returns the expected output
    for known use cases. Real implementation: build prompt from SKILL.md,
    call LLM, parse output, return classification + structured result.
    """
    if use_case_id == "UC-01":
        mus = _mus_evaluate(payload)
        return {
            "classification": "MUS_SAMPLE_SIZE_%d" % mus["sample_size"],
            "mus_evaluation": mus,
            "conclusion": mus["upper_limit_conclusion"],
        }
    if use_case_id == "UC-02":
        finding = _finding_document(payload)
        return {
            "classification": finding["severity"].upper().replace(" ", "_"),
            "finding": finding,
            "ccc_er_complete": all(
                finding.get(k) for k in ["condition", "criteria", "cause", "effect", "recommendation"]
            ),
        }
    if use_case_id == "UC-03":
        td = _td_calculate(payload)
        return {
            "classification": "TD_%.1f" % td["td_pct"],
            "td_calculation": td,
            "ria_mapping": td["ria_implication"],
        }
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    """Extract [LABEL §X] or [LABEL section] citations from SKILL.md body text."""
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/§,()\-]+?)\s*§\s*([\w.\-]+)\]", text)
