# Acceptance Gate -- audit-workpapers (v0.2.0)

This file tracks the Acceptance Gate for the v0.2.0 release. Each box is filled in only when the criterion is actually satisfied.

## Required

- [x] Frontmatter -- all required fields present (name, description, category, risk, source, date_added, version, status, industries, frameworks, telemetry_contract, context_budget, tags).
- [x] Sections -- all 12 sections present and in order.
- [x] Section 11 Routing -- present, with the routing table mapping user intent to chunks.
- [x] Folders -- chunks/, industries/, use-cases/, data/, tests/, telemetry/, docs/ all exist.
- [x] SKILL.md size -- 184 lines (<=300 limit).
- [x] Chunks -- 7 files; each <=200 lines; names match NN-slug.md.
- [x] context_budget -- declared in frontmatter with 4 token fields.
- [x] Industries -- 3 industry files (>=3 minimum).
- [x] Use cases -- 2 use-case files; UC-01 draft, UC-02 stub.
- [ ] Use cases -- need 3 use-case files with status != stub to fully satisfy linter.
- [x] Data -- data/README.md present.
- [x] Tests -- conftest.py and test_lint.py present.
- [x] Telemetry -- telemetry/schema.json validates; telemetry/instrument.py importable.
- [x] Docs -- architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md all non-stub.
- [x] No unfinished-work markers outside the changelog.
- [ ] Baseline -- telemetry/baseline.md populated after first instrumented run per UC.

## Reviewer sign-off (3 cycles)

- [ ] Cycle 1 -- structure/completeness reviewer
- [ ] Cycle 2 -- factual verification reviewer
- [ ] Cycle 3 -- production readiness reviewer
- [ ] Decision: published / rejected (with notes)

## Notes

- v0.2.0 adopted router + chunks pattern. Per-call context cost is 5-7x lower than v1.0 monolithic.
- Original SKILL.md preserved as SKILL.md.bak.
- The skill body is draft-quality.
- To satisfy linter: add a 3rd use case (UC-03) with status != template, or add a 3rd industry file with _index.md register.

## G4.5 consumer smoke tests (fresh-agent, per prompts/consumer-smoke-test.md)

N=1 existence proofs on one model — NOT reliability evidence. Clean sessions: agent
received only the skill folder + UC input.

| test | model | result | notes | date | verifier |
|------|-------|--------|-------|------|----------|
| smoke-test uc-01 | claude-fable-5 | PASS | n=75, SI=$166,667, RF=3.00 derived from the skill's tables; full workpaper structure per chunk 06. Agent reproduced BP=$500,001 and the then-current ULM framework — both skill defects fixed same day (BP=TM; full BP+PM+IA evaluation). | 2026-06-09 | claude (dispatcher-graded) |
| smoke-test uc-02 | claude-fable-5 | PASS | All 5 C-C-C-E-R parts + severity + assertion tag per oracle. Agent reproduced the input's ASC-606 criteria miscite (skill fixture defect, fixed same day). | 2026-06-09 | claude |
| smoke-test uc-03 | claude-fable-5 | PASS-WITH-NOTES | TD=20.8% arithmetic exact, "moderate-large" implication matched the oracle — but via the skill's TD→RIA double-mapping, which Tier-2 verification (AS 2315) showed to be wrong; chunk/stub/oracle corrected to TD=RIA same day. | 2026-06-09 | claude |

## §5.11 verification of the 2026-06-09 fix pass (BEFORE merge, per process v2)

| fact | tier | source | status |
|------|------|--------|--------|
| MUS RF factors (Poisson) — 20% col 3.00/4.28/5.52, 15% k=3 6.02 | Tier 1 — recomputed (solver) | computation in PR log | PASS |
| Attribute sizes 149/59/93/42/29 tie to AICPA Table A-1 | Tier 1 — exact binomial recomputation | computation in PR log | PASS |
| ULM = BP + PM + IA, taintings descending, top-stratum actual | Tier 2 | AICPA Audit Sampling Guide methodology (learnauditsampling.com quote) | PASS |
| AS 2315: TD IS the allowable risk of incorrect acceptance | Tier 2 | pcaobus.org AS 2315 appendix (verbatim) | PASS |
| GAGAS 2024: four elements of a finding, "to the extent necessary"; views of responsible officials required (¶6.58) | Tier 2 | GAO-24-106786 PDF (verbatim ¶6.17/¶8.57/¶6.53/¶6.58) | PASS |
| AS 1215.15 14-day completion = PCAOB Release 2024-004, staged effective dates (>100-issuer firms FY≥2024-12-15; others FY≥2025-12-15); AS 1215.14 = 7-year retention; AU-C 230 = 5-year | Tier 2 | pcaobus.org AS 1215 + Release 2024-004 PDF p.96 | PASS |
| 45 CFR 164.312(a)(2)(iv) encryption is ADDRESSABLE | Tier 2 | LII CFR text (verbatim) | PASS |
| 800-53A findings are Satisfied/Other-Than-Satisfied; L/M/H(+Critical) severity is the FedRAMP POA&M layer | Tier 2 | nvlpubs 800-53Ar5 + FedRAMP POA&M template | PASS |

Persona vetting: 6 CRITICAL / 12 HIGH — all resolved; 1 persona claim refuted in
verification and dropped. See docs/persona-review.md.

## Measured reliability (LLM eval lane — SOX-599/600, M4 step 3)

"Fully tested" is a measured pass rate, not a smoke test. Cases under `evals/audit-workpapers/cases/`
(hand-written + perturbations), run via `evals/harness/runner.py --executor llm`, N=20 per case,
2026-06-10. The deterministic stub lane (54 cases incl. 45 boundary-grid) runs in CI at 100% by
construction.

| Model | Cases x N | Pass rate | Dominant residual |
|---|---|---|---|
| claude-sonnet-4-6 | 7 x 20 | **100%** (140/140) | none |
| claude-haiku-4-5 | 7 x 20 | **96.4%** (135/140) | off-table-RIA refusal adherence 17/20 (instruction holds 85% on the floor model); 2 output-shape slips |

Eval-driven skill fix already shipped from these sweeps: chunks/03 "off-table parameters: do not
interpolate" (pre-fix the floor model interpolated 2/2; post-fix refuses 17/20 at N=20).
