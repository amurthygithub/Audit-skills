# Evals — the shared validation harness (Epic 6, SOX-600/601)

ONE runner all skills plug into (never a harness per skill — that collapses at
689 standards). Spec: `validation-harness-design.md` (audit-skills-mcp repo,
claude-outputs/07-validation/); tickets SOX-599 (epic), SOX-600 (V1 runner),
SOX-601 (V2 generators).

**Stack decision (SOX-600 open question, resolved 2026-06-10): Python.** The
repo's entire toolchain is Python (pytest, linter, generators, stubs), the eval
ecosystem is mature here, and reports are language-neutral JSONL — ARGUS (TS)
consumes artifacts, not the runner.

## Layout

```
evals/
  harness/         # runner.py (CLI + case schema), executors.py, validators.py
  generators/      # SOX-601: boundary sampler, adversarial perturbation
  <skill>/cases/   # *.yaml fixtures
  <skill>/coverage.json   # declared coverage-tag census (derived paths: SOX-603)
  reports/         # per-skill run reports (gitignored; latest only)
```

## Run

```bash
python3 evals/harness/runner.py --all --executor stub          # plumbing + oracle labels
python3 evals/harness/runner.py --skill audit-workpapers       # one skill
# V3 (SOX-602): --executor llm --runs 20 — pinned interface, not implemented
```

CI: `tests/test_eval_harness.py` runs every case against the stub executor —
the stub is the oracle, so 100% is the only passing grade there; failures mean
fixture/harness bugs or seed↔stub contract drift.

## The two-layer correctness model (why this tests a prompt)

The deterministic stub/MCP tool carries the math — unit-tested, 100%
deterministic. The skill (markdown) teaches an agent to apply it. The eval asks:
does a skill-loaded agent reproduce the oracle's answer over N runs, across
models? Pass rate, not vibes. With the stub executor the harness validates its
own plumbing and auto-labels generated inputs (the oracle-anchored self-labeling
flywheel); with the LLM executor (V3) the same cases measure skill fidelity.

## Reading a report

`reports/<skill>.<executor>.latest.json`: per-case `pass_rate` (passes/runs)
plus `overall_pass_rate`. The acceptance-gate reliability rows (M4 step 3) are
sourced from LLM-executor reports only — stub runs prove plumbing, not skill
reliability, and are never quoted as such.
