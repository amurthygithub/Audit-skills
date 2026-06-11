#!/usr/bin/env python3
"""Deterministic generator for 3PAO control-test sets (eval sampler input).

Emits control-test sets — each control tagged tested/passed/inherited plus a
severity for the failures — for the UC-03-style SAR finding roll-up. The oracle
computes findings = the controls the CSP OWNS that FAILED (tested AND not passed
AND not inherited); the POA&M item count = len(findings); inherited-and-failed
controls are excluded (the provider's POA&M, not the leveraging CSP's). Content
is fixed; --seed is a marker (the oracle recomputes either way).

Usage: python3 gen_control_results.py --seed 42 --out ../seeds/control-results-cases.json
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

# (id, tested, passed, inherited, severity) — severity only meaningful on failures.
_SETS = [
    # A clean set: nothing failed -> 0 findings, 0 POA&M items.
    [
        ("AC-2", True, True, False, None),
        ("AU-2", True, True, False, None),
        ("SC-7", False, None, True, "High"),   # inherited -> excluded regardless
    ],
    # Mixed: 2 CSP-owned failures (1 high, 1 low) + 1 inherited failure (excluded).
    [
        ("AC-2", True, False, False, "High"),
        ("CP-9", True, False, False, "Low"),
        ("AU-6", True, True, False, None),
        ("PE-3", False, None, True, "Moderate"),  # inherited -> not the CSP's POA&M
    ],
    # All severities present on CSP-owned failures; one inherited failure excluded.
    [
        ("AC-2", True, False, False, "High"),
        ("SI-2", True, False, False, "High"),
        ("AU-6", True, False, False, "Moderate"),
        ("CM-6", True, False, False, "Low"),
        ("AU-2", True, True, False, None),
        ("CA-7", True, True, False, None),
        ("SC-7", False, None, True, "High"),
        ("PE-3", False, None, True, "Moderate"),
    ],
]


def build() -> list:
    cases = []
    for ctrls in _SETS:
        cases.append({"controls": [
            {"id": cid, "tested": tested, "passed": passed,
             "inherited": inherited, "severity": severity}
            for cid, tested, passed, inherited, severity in ctrls
        ]})
    return cases


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="../seeds/control-results-cases.json")
    args = ap.parse_args()
    Path(args.out).write_text(json.dumps(build(), indent=1) + "\n")
    print(f"wrote {args.out} ({len(build())} control-test sets)")


if __name__ == "__main__":
    main()
