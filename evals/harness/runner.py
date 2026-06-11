#!/usr/bin/env python3
"""The ONE shared harness runner (SOX-600 V1) — all skills plug in here.

Loads case fixtures (evals/<skill>/cases/*.yaml), resolves the executor, runs
each case N times, applies its validator set, writes a per-skill report and
coverage.json. The fixture schema, validators, and reports are executor-
agnostic: swapping --executor stub -> llm (V3) changes nothing else.

Case schema (validated here):
  id: str (unique per skill)
  skill: str (must match the directory)
  use_case: str (e.g. UC-01)
  description: str
  input: dict                      # clean params; OR
  input_from_seeds:                # build payload from skill seed files
    base: <path relative to skills/<skill>/>
    merge: {key: <path>, ...}      # each loaded and attached at key
  expected: {dotted.path: value}   # for oracle_match
  invariant: {...}                 # for the invariant validator
  validators: [oracle_match|invariant, ...]
  coverage_tags: [str, ...]        # declared, not derived (decision-path
                                   # derivation is a later Epic 6 slice)
  runs: int (default 1; set >1 for non-deterministic executors)

Usage:
  python3 evals/harness/runner.py --skill audit-workpapers
  python3 evals/harness/runner.py --all --executor stub --runs 1
Exit code: 0 if every case's pass rate >= --pass-rate (default 1.0).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from executors import EXECUTORS  # noqa: E402
from validators import VALIDATORS  # noqa: E402

EVALS = Path(__file__).resolve().parents[1]
REPO_ROOT = EVALS.parent

REQUIRED_KEYS = {"id", "skill", "use_case", "description", "validators", "coverage_tags"}


class Runner:
    def __init__(self, executor) -> None:
        self.executor = executor

    def build_payload(self, case: dict) -> dict:
        if "input" in case:
            return dict(case["input"])
        spec = case["input_from_seeds"]
        skill_root = REPO_ROOT / "skills" / case["skill"]
        payload = json.loads((skill_root / spec["base"]).read_text())
        for key, rel in (spec.get("merge") or {}).items():
            payload[key] = json.loads((skill_root / rel).read_text())
        return payload

    def execute(self, case: dict) -> dict:
        kwargs = {}
        if getattr(self.executor, "name", "") == "llm":
            if "expected" in case:
                kwargs["required_paths"] = sorted(case["expected"])
            elif "invariant" in case:
                kwargs["required_paths"] = [case["invariant"].get("metric", "classification")]
        return self.executor.run(case["skill"], case["use_case"],
                                 self.build_payload(case), **kwargs)

    def run_case(self, case: dict, runs: int) -> dict:
        passes, failures = 0, []
        n = case.get("runs", runs)
        for i in range(n):
            run_failures = []
            for v in case["validators"]:
                try:
                    run_failures.extend(VALIDATORS[v](case, self))
                except Exception as e:  # an unexpected executor/parse error is a failed run
                    run_failures.append(f"{v}: {type(e).__name__}: {e}")
            if run_failures:
                failures.append({"run": i + 1, "failures": run_failures})
            else:
                passes += 1
        return {"id": case["id"], "use_case": case["use_case"], "runs": n,
                "passes": passes, "pass_rate": passes / n if n else 0.0,
                "coverage_tags": case["coverage_tags"], "failures": failures}


def load_cases(skill: str) -> list[dict]:
    cases, seen = [], set()
    for path in sorted((EVALS / skill / "cases").glob("*.yaml")):
        case = yaml.safe_load(path.read_text())
        missing = REQUIRED_KEYS - case.keys()
        if missing:
            raise ValueError(f"{path}: missing keys {sorted(missing)}")
        if case["skill"] != skill:
            raise ValueError(f"{path}: skill {case['skill']!r} != directory {skill!r}")
        if ("input" in case) == ("input_from_seeds" in case):
            raise ValueError(f"{path}: exactly one of input / input_from_seeds required")
        if case["id"] in seen:
            raise ValueError(f"{path}: duplicate case id {case['id']!r}")
        seen.add(case["id"])
        for v in case["validators"]:
            if v not in VALIDATORS:
                raise ValueError(f"{path}: unknown validator {v!r}")
        cases.append(case)
    return cases


def eval_skills() -> list[str]:
    return sorted(p.parent.name for p in EVALS.glob("*/cases") if p.is_dir())


def run_skill_evals(skill: str, executor_name: str, runs: int,
                    model: str | None = None, only: list[str] | None = None) -> dict:
    executor = (EXECUTORS[executor_name](model=model) if model and executor_name == "llm"
                else EXECUTORS[executor_name]())
    runner = Runner(executor)
    cases = load_cases(skill)
    if only:
        cases = [c for c in cases if c["id"] in only]
    results = [runner.run_case(c, runs) for c in cases]
    tags: dict[str, int] = {}
    for r in results:
        for t in r["coverage_tags"]:
            tags[t] = tags.get(t, 0) + 1
    report = {
        "skill": skill,
        "executor": executor_name,
        "model": model,
        "cases": len(results),
        "overall_pass_rate": (sum(r["passes"] for r in results)
                              / max(1, sum(r["runs"] for r in results))),
        "results": results,
    }
    write_coverage = executor_name == "stub" and not only
    coverage = {
        "skill": skill,
        "cases": len(results),
        "coverage_tags": dict(sorted(tags.items())),
        "note": "tags are DECLARED per case, not derived from the skill's decision "
                "tree — decision-path derivation is a later Epic 6 slice (SOX-603)",
    }
    if write_coverage:
        (EVALS / skill / "coverage.json").write_text(json.dumps(coverage, indent=1) + "\n")
    reports = EVALS / "reports"
    reports.mkdir(exist_ok=True)
    suffix = f".{model}" if model else ""
    (reports / f"{skill}.{executor_name}{suffix}.latest.json").write_text(
        json.dumps(report, indent=1) + "\n")
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--executor", default="stub", choices=sorted(EXECUTORS))
    ap.add_argument("--runs", type=int, default=1,
                    help="default runs per case (case-level `runs` overrides)")
    ap.add_argument("--pass-rate", type=float, default=1.0,
                    help="minimum per-case pass rate to exit 0")
    ap.add_argument("--model", help="model id for --executor llm")
    ap.add_argument("--only", nargs="*", help="run only these case ids")
    args = ap.parse_args()
    skills = eval_skills() if args.all else [args.skill]
    if not skills or skills == [None]:
        ap.error("--skill <name> or --all required")
    ok = True
    for skill in skills:
        report = run_skill_evals(skill, args.executor, args.runs,
                                 model=args.model, only=args.only)
        for r in report["results"]:
            flag = "PASS" if r["pass_rate"] >= args.pass_rate else "FAIL"
            if flag == "FAIL":
                ok = False
            print(f"[{flag}] {skill}/{r['id']} pass_rate={r['pass_rate']:.2f} "
                  f"({r['passes']}/{r['runs']})")
            for f in r["failures"][:3]:
                print(f"        run {f['run']}: {'; '.join(f['failures'][:2])}")
        print(f"== {skill}: {report['cases']} cases, overall pass rate "
              f"{report['overall_pass_rate']:.2%} (executor={report['executor']})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
