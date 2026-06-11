#!/usr/bin/env python3
"""Deterministic generator for multi-entity sub-cert cascade cases (eval sampler input).

Emits entity lists with domestic/FPI types and coverage flags; the oracle computes
coverage gaps and the quarterly/annual evaluation split. Content fixed; --seed is a marker.

Usage: python3 gen_subcert_cascade.py --seed 42 --out ../seeds/cascade-cases.json
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tests"))


def build() -> list:
    cases = []
    for n, fpi, gaps in [(5, 0, 0), (10, 2, 1), (15, 3, 1), (20, 5, 2)]:
        ents = [{"entity": f"E{i:02d}", "type": ("fpi" if i <= fpi else "domestic"),
                 "sub_certifier": f"Controller-E{i:02d}", "covered": i > gaps}
                for i in range(1, n + 1)]
        cases.append({"entities": ents})
    return cases


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="../seeds/cascade-cases.json")
    args = ap.parse_args()
    Path(args.out).write_text(json.dumps(build(), indent=1) + "\n")
    print(f"wrote {args.out} ({len(build())} cascade cases)")


if __name__ == "__main__":
    main()
