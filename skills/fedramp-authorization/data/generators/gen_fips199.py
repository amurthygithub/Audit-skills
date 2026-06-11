#!/usr/bin/env python3
"""Deterministic generator for FIPS 199 categorization cases (eval sampler input).

Emits CIA-objective triples (confidentiality / integrity / availability, each
Low/Moderate/High) plus the saas_delivery flag. The oracle computes the overall
impact as the HIGH-WATER MARK (max of C/I/A), then the selected FedRAMP Rev 5
baseline and control count (Low 156 / Moderate 323 / High 410) and the LI-SaaS
eligibility (Low + SaaS). Content is fixed; --seed is a marker (the oracle
recomputes either way).

Usage: python3 gen_fips199.py --seed 42 --out ../seeds/fips199-cases.json
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def build() -> list:
    # Each row: per-objective CIA + saas_delivery. The oracle derives the overall
    # level (high-water mark), the baseline count, and LI-SaaS eligibility.
    rows = [
        ("Low", "Low", "Low", True),          # -> Low; SaaS -> LI-SaaS eligible (156)
        ("Low", "Low", "Low", False),         # -> Low; not SaaS -> full Low baseline (156)
        ("Moderate", "Low", "Low", True),     # -> Moderate (one objective lifts it); NOT LI-SaaS (323)
        ("Moderate", "Moderate", "Low", False),  # -> Moderate (323)
        ("Low", "High", "Low", False),        # -> High (one High objective makes the system High; 410)
        ("High", "Moderate", "Moderate", True),  # -> High (410); SaaS does not make it LI-SaaS
    ]
    cases = []
    for c, i, a, saas in rows:
        cases.append({
            "fips199": {"confidentiality": c, "integrity": i, "availability": a},
            "saas_delivery": saas,
        })
    return cases


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="../seeds/fips199-cases.json")
    args = ap.parse_args()
    Path(args.out).write_text(json.dumps(build(), indent=1) + "\n")
    print(f"wrote {args.out} ({len(build())} FIPS 199 categorization cases)")


if __name__ == "__main__":
    main()
