# Acceptance Gate (TEMPLATE)

A skill can flip `status: published` only when **every** box is checked and the linter (`tools/lint_skill.py`) returns exit 0.

## Required

- [ ] **Frontmatter** — all required fields present and well-typed.
- [ ] **Sections** — first 10 sections present, in order.
- [ ] **Folders** — every folder in §1 of `SKILL.md` exists and non-empty.
- [ ] **Industries** — ≥3 industry files; `_index.md` registered.
- [ ] **Use cases** — ≥3 use-case files; `_index.md` registered; each with `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`.
- [ ] **Data** — `data/README.md` present; ≥1 generator; ≥1 seed per use case.
- [ ] **Tests** — `tests/test_oracle.py` covers every use case; `tests/test_lint.py` self-checks; all tests pass locally.
- [ ] **Telemetry** — `telemetry/schema.json` validates against the published $id; `telemetry/instrument.py` importable; `telemetry/redaction.md` non-stub.
- [ ] **Docs** — `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, this `acceptance-gate.md` all non-stub.
- [ ] **No TODO/FIXME outside changelog** — the linter enforces.
- [ ] **Baseline** — `telemetry/baseline.md` populated after one instrumented run per use case.
- [ ] **Citations** — every in-body `[XYZ §N]` reference resolves to `## 10. References & Citation Manifest` in `SKILL.md`.

## Reviewer sign-off (3 cycles)

- [ ] Cycle 1 — structure/completeness reviewer
- [ ] Cycle 2 — factual verification reviewer
- [ ] Cycle 3 — production readiness reviewer
- [ ] Decision: `published` / `rejected` (with notes)
