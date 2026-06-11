"""Validators — tiered output checks (SOX-600 V1; spec §4).

V1 ships the two cheap deterministic tiers:

- oracle_match — dotted-path subset match of `expected` against the output.
- invariant — metamorphic checks needing no labeled answer: monotonicity over a
  swept parameter, and idempotence (same input -> same classification).

Citation-grounding, reasoning-trace, LLM-judge, and adversarial-skeptic tiers
are later Epic 6 slices (SOX-602+); the per-case `validators` list is already
the dispatch surface for them.
"""

from __future__ import annotations

from typing import Any, Callable


def get_path(obj: Any, dotted: str) -> Any:
    cur = obj
    for part in dotted.split("."):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def oracle_match(case: dict, runner) -> list[str]:
    """Every dotted path in `expected` must match the executor's output value.

    Expected values may be plain values (exact match) or {"value": X,
    "tolerance": T} for numerics where the oracle's value embeds a display-
    rounding convention (e.g. the MUS sampling interval). Paths listed in
    `stub_only_paths` are stub-internal conventions (classification label
    formats) and are skipped for non-stub executors — the LLM lane is graded
    on substance, not on house label spelling.
    """
    failures = []
    executor_name = getattr(runner.executor, "name", "stub")
    try:
        out = runner.execute(case)
    except ValueError as e:
        if executor_name != "stub" and case.get("accept_refusal"):
            return []
        raise

    stub_only = set(case.get("stub_only_paths", []))
    for path, want in case["expected"].items():
        if executor_name != "stub" and path in stub_only:
            continue
        tolerance = 0
        if isinstance(want, dict) and "value" in want:
            tolerance = want.get("tolerance", 0)
            want = want["value"]
        try:
            got = get_path(out, path)
        except (KeyError, IndexError, TypeError):
            failures.append(f"oracle_match: path {path!r} missing from output")
            continue
        if tolerance and isinstance(got, (int, float)) and isinstance(want, (int, float)):
            if abs(got - want) <= tolerance:
                continue
        if isinstance(got, list) and isinstance(want, list):
            try:
                if sorted(got) == sorted(want):
                    continue
            except TypeError:
                pass
        if got != want:
            failures.append(f"oracle_match: {path} = {got!r}, expected {want!r}")
    return failures


_DIRECTIONS: dict[str, Callable[[list], bool]] = {
    "non_increasing": lambda v: all(a >= b for a, b in zip(v, v[1:])),
    "non_decreasing": lambda v: all(a <= b for a, b in zip(v, v[1:])),
}


def invariant(case: dict, runner) -> list[str]:
    """Metamorphic invariants: monotonic sweep or idempotence."""
    spec = case["invariant"]
    kind = spec["type"]
    if kind == "monotonic":
        values = []
        for v in spec["values"]:
            payload = dict(case["input"])
            payload[spec["param"]] = v
            out = runner.execute({**case, "input": payload})
            values.append(get_path(out, spec["metric"]))
        ok = _DIRECTIONS[spec["direction"]](values)
        if not ok:
            return [f"invariant: {spec['metric']} over {spec['param']}={spec['values']} "
                    f"gave {values}, expected {spec['direction']}"]
        return []
    if kind == "idempotent":
        o1 = runner.execute(case)
        o2 = runner.execute(case)
        metric = spec.get("metric", "classification")
        a, b = get_path(o1, metric), get_path(o2, metric)
        return [] if a == b else [f"invariant: idempotence violated on {metric}: {a!r} != {b!r}"]
    raise ValueError(f"unknown invariant type: {kind!r}")


def refusal(case: dict, runner) -> list[str]:
    """The case's input is defective (missing/invalid load-bearing parameter);
    the only passing answer is an explicit refusal — abstention beats a wrong
    number (spec §5). With the stub executor a refusal is a raised ValueError;
    the LLM executor (V3) maps this to ask-vs-fabricate behavior."""
    try:
        out = runner.execute(case)
    except ValueError:
        return []
    return [f"refusal: expected a refusal but got output "
            f"classification={out.get('classification')!r}"]


VALIDATORS = {"oracle_match": oracle_match, "invariant": invariant, "refusal": refusal}
