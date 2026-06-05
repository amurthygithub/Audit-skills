# Acceptance Gate - isaca-audit-methodology (v0.2.0)

## Required

- [x] **Frontmatter** - all required fields present (name, description, category, risk, source, date_added, version, status, industries, frameworks, telemetry_contract, context_budget, tags).
- [x] **Sections** - first 10 sections present, in order (When to Use, Framework Overview, Core Concepts, Decision Logic, Procedure Templates, Output Templates, Cross-References, Worked Examples, Anti-Hallucination, References & Citation Manifest).
- [x] **S11 Routing** - present, with routing table mapping user intent to chunks.
- [x] **Folders** - industries/, use-cases/, data/, tests/, telemetry/, docs/, chunks/ all exist.
- [x] **SKILL.md size** - 198 lines (<= 300 limit).
- [x] **Chunks** - 7 files; each <= 200 lines; names match `NN-slug.md`.
- [x] **context_budget** - declared in frontmatter with 4 token fields.
- [x] **Industries** - 3 industry files; `_index.md` registered.
- [x] **Use cases** - 2 stub use cases; `_index.md` registered; each with procedure, expected_outputs, oracle, data_refs, tests, status.
- [x] **Data** - data/README.md present.
- [x] **Tests** - conftest.py, test_lint.py present.
- [x] **Telemetry** - schema.json validates; instrument.py present; redaction.md non-stub.
- [x] **Docs** - architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md all non-stub.
- [x] **No unfinished-work markers outside changelog** - linter enforces.
- [ ] **Baseline** - telemetry/baseline.md populated after first instrumented run per UC.
- [~] **Citations** - manifest present; grounding tests pending.

## Reviewer sign-off (3 cycles)

- [ ] **Cycle 1 - structure/completeness** (linter passes - pending)
- [ ] **Cycle 2 - factual verification** (test_grounding + test_trace pending)
- [ ] **Cycle 3 - production readiness** (test_oracle + test_telemetry + baseline pending)
- [ ] **Decision: `published` / `rejected` (with notes)**

## Notes

- v0.2.0 adopted the router + chunks pattern retrofitting the original 1,662-line monolithic skill.
- Use cases are stubs; full UC-01 (COBIT maturity assessment) and UC-02 (5-part observation) need fleshed out.
- Token baseline target: input_p90 16000, output_p90 5000.
