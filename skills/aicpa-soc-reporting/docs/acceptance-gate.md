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

## G4.5 consumer smoke tests (fresh-agent, per prompts/consumer-smoke-test.md)

N=1 existence proofs on one model — NOT reliability evidence. Clean sessions.

| test | model | result | notes | date | verifier |
|------|-------|--------|-------|------|----------|
| smoke-test uc-01 | claude-fable-5 | PASS-WITH-NOTES | All 4 report sections, ≥4 CUECs with criteria links, AWS CSOCs, valid opinion logic. Agent flagged the skill's 33-vs-35 count contradiction unprompted and reported 38 per the UC oracle. Reproduced then-current defects (CC6.5 physical mapping, "no responsibility to evaluate CUECs") — fixed same day. | 2026-06-10 | claude (dispatcher-graded) |
| smoke-test uc-02 | claude-fable-5 | PASS-WITH-NOTES | 3 subservice orgs, carve-out rationale, CUECs/CSOCs linked. Agent independently caught and corrected the UC's out-of-scope PI mappings (skill fixture defect, fixed same day). | 2026-06-10 | claude |
| smoke-test uc-03 | claude-fable-5 | PASS-WITH-NOTES | Complete letter: addressee, prior-report ref, 4 attestations, disclaimer, signature block, correct issuer (management). Inherited the template's future-dating flaw (attesting through period end from an earlier date) — fixed same day. | 2026-06-10 | claude |
| smoke-test uc-04 | claude-fable-5 | PASS-WITH-NOTES | Full preparation playbook; agent surfaced the 33-vs-35 contradiction with an explicit caveat (good anti-hallucination behavior). | 2026-06-10 | claude |

## §5.11 verification of the 2026-06-10 fix pass (BEFORE merge, per process v2)

| fact | tier | source | status |
|------|------|--------|--------|
| TSC 2017 inventory: 33 CC (CC8=CC8.1 only) + 3 A + 2 C + 5 PI + 18 P = 61; full ID list extracted | Tier 2 | 2017 TSC PDF (2022 PoF edition), text-extracted | PASS |
| CC1.1–CC1.5 map sequentially to COSO P1–P5 (CC1.2 = board oversight, verbatim) | Tier 2 | same PDF | PASS |
| Verbatim texts: CC6.4 physical access, CC6.5 disposal, CC7.1/7.2 monitoring, CC8.1, A1.1 capacity, A1.2, A1.3 | Tier 2 | same PDF | PASS |
| AT-C codification: 105 (SSAE 18 am.), 205 (SSAE 21, renamed), 206 (new, SSAE 21), 210 (SSAE 22), 215 (SSAE 19), 320 (SSAE 18); SSAE 18 NOT superseded; SSAE 21 eff. June 15 2022 | Tier 2 | AICPA "Sources of Sections" PDF + SSAEs-currently-effective page | PASS |
| AICPA prescribes NO minimum SOC 2 examination period (FAQ §.05 verbatim; <2-month evidence caution) | Tier 2 | AICPA SOC 2 FAQ PDF (archived official copy) | PASS |
| 45 CFR 164.312(a)(2)(i)/(ii)/(iii) = unique user ID / emergency access / automatic logoff; 164.308(a)(5)(ii)(B) malware; 164.308(a)(6) incident procedures | Tier 2 | LII CFR text (verbatim) | PASS |
| HITRUST CSF v11's 19 assessment domains (full list; shipped labels wrong for 3/7/10/17) | Tier 2 | HITRUST sample validated-assessment reports + assessor publications | PASS |
| SP 800-53 Rev 5 has 20 families incl. PT; no AR/DI (Rev 4 Appendix J) | Tier 2 | nvlpubs SP 800-53r5 Table 1 | PASS |

Persona vetting: 4 CRITICAL / 12 HIGH — all resolved. See docs/persona-review.md.
