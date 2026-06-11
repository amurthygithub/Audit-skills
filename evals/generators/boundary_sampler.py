#!/usr/bin/env python3
"""Boundary/combinatorial sampler (SOX-601 generator 1 of 4).

Hammers the thresholds where judgment flips. V1 domain: MUS sampling
(audit-workpapers UC-01) — every supported RIA (each is an RF-table boundary)
crossed with TM steps around round-number cliffs, at a fixed BV grid.

The oracle-anchored self-labeling flywheel: every generated input is labeled by
running the deterministic stub — zero human labeling. Generation is fully
deterministic (fixed grids, no randomness) and idempotent: rerunning rewrites
the same files. Generated cases land in evals/<skill>/cases/gen-*.yaml and are
picked up by the runner and CI exactly like hand-written cases.

Usage: python3 evals/generators/boundary_sampler.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

EVALS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVALS / "harness"))
from executors import StubExecutor  # noqa: E402

SKILL = "audit-workpapers"
USE_CASE = "UC-01"

RIA_GRID = [0.01, 0.05, 0.10, 0.15, 0.20]   # the full supported RF table
BV_GRID = [1_000_000, 5_000_000, 12_500_000]
TM_GRID = [100_000, 200_000, 500_000]


def main() -> None:
    executor = StubExecutor()
    out_dir = EVALS / SKILL / "cases"
    written = 0
    for ria in RIA_GRID:
        for bv in BV_GRID:
            for tm in TM_GRID:
                payload = {
                    "population_book_value": bv,
                    "tolerable_misstatement": tm,
                    "risk_of_incorrect_acceptance": ria,
                    "expected_overstatements": 0,
                }
                label = executor.run(SKILL, USE_CASE, payload)
                mus = label["mus_evaluation"]
                case = {
                    "id": f"gen-boundary-ria{int(ria * 100):02d}-bv{bv // 1_000_000}m-tm{tm // 1_000}k",
                    "skill": SKILL,
                    "use_case": USE_CASE,
                    "description": (f"Generated boundary case (boundary_sampler.py, oracle-labeled): "
                                    f"RIA {ria:.0%}, BV ${bv:,}, TM ${tm:,}."),
                    "generated_by": "evals/generators/boundary_sampler.py",
                    "input": payload,
                    "expected": {
                        "mus_evaluation.sample_size": mus["sample_size"],
                        # display-rounded by the stub; true interval may differ by <1
                        "mus_evaluation.sampling_interval": {
                            "value": mus["sampling_interval"], "tolerance": 1},
                        "mus_evaluation.reliability_factor": mus["reliability_factor"],
                        "classification": label["classification"],
                    },
                    "stub_only_paths": ["classification"],
                    "validators": ["oracle_match"],
                    "coverage_tags": [f"boundary.ria-{ria}", "mus.sample-size",
                                      "mus.sampling-interval"],
                }
                path = out_dir / f"{case['id']}.yaml"
                path.write_text(yaml.safe_dump(case, sort_keys=False, width=100))
                written += 1
    print(f"wrote {written} boundary cases to {out_dir}")


if __name__ == "__main__":
    main()
