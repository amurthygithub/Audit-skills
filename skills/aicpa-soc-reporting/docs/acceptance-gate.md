# Acceptance Gate -- aicpa-soc-reporting (v0.2.0)

This file tracks the Acceptance Gate for the v0.2.0 release. Each box is filled in only when the criterion is actually satisfied.

## Required

- [x] Frontmatter -- all required fields present (`name`, `description`, `category`, `risk`, `source`, `date_added`, `version`, `status`, `industries`, `frameworks`, `telemetry_contract`, `context_budget`, `tags`).
- [x] Sections -- first 10 sections present, in order.
- [x] Section 11 Routing -- present, with routing table mapping user intent -> chunks.
- [x] Folders -- `chunks/`, `industries/`, `use-cases/`, `data/`, `tests/`, `telemetry/`, `docs/` all exist.
- [x] SKILL.md size -- ~280 lines (<= 300 limit).
- [x] Chunks -- 7 files; each <= 200 lines; names match `NN-slug.md`.
- [x] context_budget -- declared in frontmatter with 4 token fields.
- [x] Industries -- 4 industry files; `_index.md` registered.
- [x] Use cases -- 2 use-case files (UC-01, UC-02); `_index.md` registered; each with `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`.
- [x] Data -- `data/README.md` present.
- [x] Tests -- `conftest.py` + `test_lint.py`.
- [x] Telemetry -- `schema.json`, `instrument.py`, `redaction.md`, `baseline.md` from TEMPLATE.
- [x] Docs -- `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md` all present.
- [ ] Baseline -- `telemetry/baseline.md` populated after first instrumented run per UC.
- [x] Citations -- every in-body citation uses `[LABEL]` form.

## Reviewer sign-off (3 cycles)

- [ ] Cycle 1 -- structure/completeness reviewer (linter passes -- pending CI)
- [ ] Cycle 2 -- factual verification reviewer (test_grounding + test_trace pass)
- [ ] Cycle 3 -- production readiness reviewer (test_oracle + test_telemetry + baseline populated)
- [ ] Decision: `published` / `rejected` (with notes)

## Notes

- Token baseline: target `input_p90: 12000`, `output_p90: 4000`. Per-call context budget: `always_loaded_tokens: 2800`, `per_call_typical_tokens: 5500`, `per_call_max_tokens: 14000`. To be measured and updated in `telemetry/baseline.md` after first instrumented run.
- v0.2.0 adopted the router + chunks pattern. Per-call context cost is ~6x lower than v0.1.0's monolithic 1,580-line layout.
- `SKILL.md.bak` preserved from v0.1.0.
- Use-case and test files are stubs. Full UC execution ships in SOX-611 Phase 2.
