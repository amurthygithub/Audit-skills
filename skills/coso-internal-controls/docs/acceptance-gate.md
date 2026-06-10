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

## G4.5 consumer smoke tests (fresh-agent, per prompts/consumer-smoke-test.md)

N=1 existence proofs on one model — NOT reliability evidence. Clean sessions.

| test | model | result | notes | date | verifier |
|------|-------|--------|-------|------|----------|
| smoke-test uc-01 | claude-fable-5 | PASS | 17-column RcM verbatim, 3-step tree, Item 308 report elements, six-phase procedure — clean routing across 9 files. Reproduced the then-current unconditional attestation statement (skill defect, fixed same day). | 2026-06-09 | claude (dispatcher-graded) |
| smoke-test uc-02 | claude-fable-5 | PASS | 3-step tree + 6-step compensating evaluation + MW indicator check, matching the UC oracle exactly. Faithfully reproduced two skill defects fixed/ticketed same day: the rescinded "more than insignificant" threshold and the reconciliation-precision conclusion (SOX-641). | 2026-06-09 | claude |
| smoke-test uc-03 | claude-fable-5 | PASS | All 17 principles grouped correctly with component counts, PoF approach, both-conditions effectiveness logic, curated-subset caveat carried through. | 2026-06-09 | claude |

## §5.11 verification of the 2026-06-09 fix pass (BEFORE merge, per process v2)

| fact | tier | source | status |
|------|------|--------|--------|
| SEC 33-8810: management "should not qualify its assessment"; with an MW, may not conclude effective | Tier 2 | sec.gov 33-8810 PDF (verbatim) | PASS |
| AS 2201.69 lists INDICATORS of material weaknesses (not per-se determinations) | Tier 2 | pcaobus.org AS 2201 (verbatim .69) | PASS |
| AS 2201 "reasonable possibility" note ties to FAS 5 reasonably-possible/probable | Tier 2 | pcaobus.org AS 2201 .A7 + note | PASS |
| AS 2201 Appendix B topics: integration .B1-.B9, multi-location .B10-.B16, service orgs .B17-.B27, benchmarking .B28-.B33 — no ITGC taxonomy | Tier 2 | pcaobus.org AS 2201 App B | PASS |
| Item 308(a)(4) attestation statement conditional on accelerated/large-accelerated status | Tier 2 | LII 17 CFR 229.308 (verbatim) | PASS |
| Non-accelerated 404(b) exemption = Dodd-Frank §989G / SOX 404(c) (SEC 33-9142); EGC = JOBS Act; SRC alone never exempted (34-88365) | Tier 2 | sec.gov 33-9142 + 34-88365 (verbatim) | PASS |
| OMB A-123 (M-16-17) requires GAO Green Book as the framework | Tier 2 | whitehouse.gov M-16-17 PDF (verbatim) | PASS |
| 800-53A = Satisfied/Other-Than-Satisfied; FIPS 199 = 3 levels; L/M/H(+Critical) = FedRAMP POA&M layer | Tier 2 | nvlpubs + fedramp.gov template | PASS |

Persona vetting: 5 CRITICAL / 14 HIGH — all resolved. See docs/persona-review.md.
