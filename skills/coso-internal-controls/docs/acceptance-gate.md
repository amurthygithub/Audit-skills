# Acceptance Gate — coso-internal-controls (v0.2.0)

## Required

- [x] Frontmatter — all required fields present.
- [x] Sections — sections 1-12 present per TEMPLATE sect.3.
- [x] sect.11 Routing — present with routing table.
- [x] Folders — industries/, use-cases/, data/, tests/, telemetry/, docs/, chunks/ all exist.
- [x] SKILL.md size — 214 lines (<= 300 limit).
- [x] Chunks — 7 files; each named NN-slug.md.
- [x] context_budget — declared in frontmatter with 4 token fields.
- [x] Industries — 3 files (financial-services, public-sector, saas-technology); _index.md registered.
- [x] Use cases — 2 files (UC-01, UC-02); _index.md registered; each with procedure, expected_outputs, oracle, data_refs, tests, status.
- [x] Data — data/README.md present.
- [x] Tests — conftest.py, test_lint.py present.
- [x] Telemetry — schema.json, instrument.py, redaction.md, baseline.md all present.
- [x] Docs — architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md all non-stub.
- [x] No unfinished-work markers outside the changelog.
- [ ] Baseline — telemetry/baseline.md populated after first instrumented run.
- [ ] Reviewer sign-off — 3-cycle review not yet executed.

## Reviewer sign-off (3 cycles)

- [ ] Cycle 1: structure/completeness reviewer
- [ ] Cycle 2: factual verification reviewer
- [ ] Cycle 3: production readiness reviewer
- [ ] Decision: published / rejected (with notes)

## Notes

- Token baseline: target input_p90 14000, output_p90 4500. Per-call context budget: always_loaded 3000, typical 6000, max 15000. To be measured after first instrumented run.
- v0.2.0 adopted the router + chunks pattern per TEMPLATE sect.11.
- Migration from monolithic 1,879-line SKILL.md to this pattern.
- Status: draft. Requires 3 review cycles before published.
