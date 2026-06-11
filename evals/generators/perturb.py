#!/usr/bin/env python3
"""Adversarial perturbation generator (SOX-601 generator 3 of 4).

Takes the clean PoC input and emits defective variants where the only passing
answer is an explicit refusal (drop a load-bearing fact; invalid magnitude;
off-table parameter) — the ask-vs-fabricate axis. Plus the degenerate-but-legal
zero-population case, which must produce n=0, not a refusal (the boundary
between "defective input" and "unusual input" is itself part of the contract).

This generator FOUND the contract it now enforces: the 2026-06-10 probe showed
the stub silently defaulting a missing BV/TM and emitting a negative sampling
interval for negative TM — fixed in the same change that added the `refusal`
validator. Deterministic and idempotent like boundary_sampler.py.

Usage: python3 evals/generators/perturb.py
"""

from __future__ import annotations

from pathlib import Path

import yaml

EVALS = Path(__file__).resolve().parents[1]
SKILL = "audit-workpapers"
USE_CASE = "UC-01"

BASE = {
    "population_book_value": 5_000_000,
    "tolerable_misstatement": 200_000,
    "risk_of_incorrect_acceptance": 0.05,
    "expected_overstatements": 0,
}

PERTURBATIONS = [
    ("gen-perturb-missing-bv", "Drop the population book value — load-bearing fact gone; must ask, not assume.",
     {k: v for k, v in BASE.items() if k != "population_book_value"}, "refusal", None),
    ("gen-perturb-missing-tm", "Drop tolerable misstatement — must ask, not default to a materiality.",
     {k: v for k, v in BASE.items() if k != "tolerable_misstatement"}, "refusal", None),
    ("gen-perturb-negative-tm", "Negative TM — pre-fix the stub emitted SI=-66,667; must refuse.",
     {**BASE, "tolerable_misstatement": -200_000}, "refusal", None),
    ("gen-perturb-off-table-ria", "RIA 7% is not in the RF table at 0 expected misstatements; must refuse, not interpolate.",
     {**BASE, "risk_of_incorrect_acceptance": 0.07}, "refusal", None),
    ("gen-perturb-zero-bv", "Zero population is degenerate but legal: n=0, NOT a refusal — the defective/unusual boundary.",
     {**BASE, "population_book_value": 0}, "oracle_match",
     {"mus_evaluation.sample_size": 0}),
]


def main() -> None:
    out_dir = EVALS / SKILL / "cases"
    for case_id, desc, payload, validator, expected in PERTURBATIONS:
        case = {
            "id": case_id,
            "skill": SKILL,
            "use_case": USE_CASE,
            "description": f"Generated perturbation (perturb.py): {desc}",
            "generated_by": "evals/generators/perturb.py",
            "input": payload,
            "validators": [validator],
            "coverage_tags": ["perturbation.ask-vs-fabricate" if validator == "refusal"
                              else "boundary.zero-population"],
        }
        if expected:
            case["expected"] = expected
        (out_dir / f"{case_id}.yaml").write_text(
            yaml.safe_dump(case, sort_keys=False, width=100))
    print(f"wrote {len(PERTURBATIONS)} perturbation cases to {out_dir}")


if __name__ == "__main__":
    main()
