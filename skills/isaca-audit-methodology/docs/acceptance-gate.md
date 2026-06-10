# Acceptance Gate - isaca-audit-methodology (v0.2.0)

Checkboxes below were re-verified against disk 2026-06-10 (the previous version of this file
contained checked items that were false -- see docs/persona-review.md).

## Required

- [x] **Frontmatter** - all required fields present (name, description, category, risk, source, date_added, version, status, industries, frameworks, telemetry_contract, context_budget, tags).
- [x] **Sections** - first 10 sections present, in order (When to Use, Framework Overview, Core Concepts, Decision Logic, Procedure Templates, Output Templates, Cross-References, Worked Examples, Anti-Hallucination, References & Citation Manifest).
- [x] **S11 Routing** - present; routes all 8 chunks, 4 industries, 3 UCs.
- [x] **Folders** - industries/, use-cases/, data/, tests/, telemetry/, docs/, chunks/ all exist.
- [x] **SKILL.md size** - <= 300-line limit (verify with `wc -l`).
- [x] **Chunks** - 8 files; names match `NN-slug.md`.
- [x] **context_budget** - declared in frontmatter with 4 token fields.
- [x] **Industries** - 4 industry files; `_index.md` registered.
- [x] **Use cases** - 3 stub use cases; `_index.md` registered; each with procedure, expected_outputs, oracle, data_refs, tests, status.
- [x] **Data** - data/README.md, generators/, 3 seeds present.
- [x] **Tests** - 6 test files + stub executor (oracle, grounding, trace, metamorphic, adversarial, telemetry).
- [x] **Telemetry** - schema.json validates; instrument.py present; redaction.md non-stub.
- [x] **Docs** - architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md, persona-review.md all non-stub.
- [x] **No unfinished-work markers outside changelog** - linter enforces.
- [ ] **Baseline** - telemetry/baseline.md populated after first instrumented run per UC.
- [x] **Citations** - manifest synced with data/registry/citations.json (test-enforced); grounding tests pass.

## Reviewer sign-off

- [x] **Cycle 1 - structure/completeness** (linter + pytest green, 2026-06-10)
- [x] **Cycle 2 - factual verification** (G4.5 vetting: 5 personas + Tier-1/Tier-2 verification with verbatim quotes; all CRITICAL/HIGH resolved -- see persona-review.md, 2026-06-10)
- [ ] **Cycle 3 - production readiness** (Epic 6 harness: N>=20 runs, >=2 models -- pending)
- [ ] **Decision: `published` / `rejected` (with notes)**

## G4.5 consumer-ready gate (SOX-636)

| check | result | date | verifier |
|---|---|---|---|
| Persona vetting (5 personas) | 6 CRITICAL / 12 HIGH verified findings; all FIXED/TICKETED/ACCEPTED | 2026-06-10 | claude (LLM-vetted -- a filter, not a certification) |
| §5.11 source verification | COBIT catalog, ITAF series, CISA weights, CCM v4, GDPR 83(4), HIPAA specs verified against live sources with verbatim quotes | 2026-06-10 | claude + 2 Tier-2 verification agents |
| smoke-test uc-01 | pre-fix FAIL (schema mismatch chunk-03 vs oracle) -> post-fix re-run: **PASS-WITH-NOTES** (11/11 assertions; notes fixed: envelope key documented, SKILL.md §6 pointer corrected) | 2026-06-10 | clean-session agents |
| smoke-test uc-02 | pre-fix FAIL (severity High-vs-Critical contradiction; S17 criteria) -> post-fix re-run: **PASS-WITH-NOTES** (notes fixed: `observation` envelope documented; policy reference moved into seed so criteria are input-derived) | 2026-06-10 | clean-session agents |
| smoke-test uc-03 | PASS-WITH-NOTES (MEA03 name + design_factors_applied derivable only from stub -- both fixed) | 2026-06-10 | clean-session agent |

N=1 clean-session runs are an existence proof, not a reliability claim -- that requires the Epic 6 harness (N>=20, >=2 models).

## Notes

- v0.2.0 adopted the router + chunks pattern retrofitting the original 1,662-line monolithic skill.
- 2026-06-10 G4.5 retrofit: COBIT 2019 catalog rebuilt from verified publication text (BAI12 removed, MEA04 added, official names); fake S1-S18/G1-G18 numbering replaced with real ITAF 1000/1200/1400 series; CISA weights reconciled to the live exam content outline; severity decoupled from MW/SD; CCM v4 codes corrected.
- Token baseline target: input_p90 16000, output_p90 5000.
