# Acceptance Gate — nist-800-53-rmf (v0.2.0)

This file tracks the Acceptance Gate for the v0.2.0 release. Each box is filled in only when the criterion is **actually** satisfied (linter passes, tests run, etc.).

## Required

- [x] **Frontmatter** — all required fields present (`name`, `description`, `category`, `risk`, `source`, `date_added`, `version`, `status`, `industries`, `frameworks`, `telemetry_contract`, `context_budget`, `tags`).
- [x] **Sections** — first 10 sections present, in order (`When to Use`, `Framework Overview`, `Core Concepts`, `Decision Logic`, `Procedure Templates`, `Output Templates`, `Cross-References`, `Worked Examples`, `Anti-Hallucination`, `References & Citation Manifest`).
- [x] **§11 Routing** — present, with the routing table mapping user intent → chunks.
- [x] **Folders** — `industries/`, `use-cases/`, `data/`, `tests/`, `telemetry/`, `docs/`, `chunks/` all exist and non-empty.
- [x] **SKILL.md size** — 218 lines (≤ 300 limit).
- [x] **Chunks** — 7 files (categorize, baseline, implement, assess, authorize, monitor, crosswalk); each ≤ 87 lines (≤ 200 limit); names match `NN-slug.md`.
- [x] **context_budget** — declared in frontmatter with 4 token fields.
- [x] **Industries** — 4 industry files (`public-sector.md`, `financial-services.md`, `saas-technology.md`, `healthcare.md`); `_index.md` registered.
- [x] **Use cases** — 3 use-case files (UC-01, UC-02, UC-03); `_index.md` registered; each with `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`.
- [x] **Data** — `data/README.md` present; 3 generators; 10 seed fixtures.
- [x] **Tests** — 7 test files (`test_oracle.py`, `test_trace.py`, `test_grounding.py`, `test_metamorphic.py`, `test_adversarial.py`, `test_telemetry.py`, `test_lint.py`).
- [x] **Telemetry** — `telemetry/schema.json` validates; `telemetry/instrument.py` importable; `telemetry/redaction.md` non-stub.
- [x] **Docs** — `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md` all non-stub.
- [x] **No unfinished-work markers outside the changelog** — linter enforces.
- [ ] **Baseline** — `telemetry/baseline.md` populated after first instrumented run per UC.
- [x] **Citations** — every in-body `[LABEL §N]` reference resolves to `## 10. References & Citation Manifest` (test_grounding.py).

## Reviewer sign-off (3 cycles)

- [ ] **Cycle 1 — structure/completeness reviewer** (linter passes — pending CI)
- [ ] **Cycle 2 — factual verification reviewer** (test_grounding + test_trace pass)
- [ ] **Cycle 3 — production readiness reviewer** (test_oracle + test_telemetry + baseline populated)
- [ ] **Decision: `published` / `rejected` (with notes)**

## Notes

- Token baseline: target `input_p90: 14000`, `output_p90: 4500` (per `SKILL.md` frontmatter). Per-call context budget: `always_loaded_tokens: 3000`, `per_call_typical_tokens: 6000`, `per_call_max_tokens: 15000`. To be measured and updated in `telemetry/baseline.md` after first instrumented run.
- v0.2.0 adopted the router + chunks pattern (per TEMPLATE §11). Per-call context cost is 3-5× lower than v0.1.0's monolithic layout.
- The 4 pre-Spine skills have not been migrated; this skill is the first on the Spine. Migration backlog is in SOX-611.
- The skill body is draft-quality and requires 3 review cycles before `status: published`.

## G4.5 consumer smoke tests (fresh-agent, per prompts/consumer-smoke-test.md)

N=1 existence proofs on one model — NOT reliability evidence (that requires the Epic 6
harness: ≥95% pass over N≥20 runs, ≥2 models). Clean sessions: agent received only the
skill folder + UC input, no repo context.

| test | model | result | notes | date | verifier |
|------|-------|--------|-------|------|----------|
| smoke-test uc-01 | claude-fable-5 | PASS-WITH-NOTES | All oracle assertions met (overall MODERATE, baseline MODERATE, AC-2/SC-7/AU-2 statuses, tailoring set). Routing clean (8 files, correct order). Agent faithfully reproduced the skill's then-erroneous SC-8(1) scoping — a skill defect, since fixed (persona-review.md CRITICAL #1). | 2026-06-09 | claude (dispatcher-graded vs UC oracle) |
| smoke-test uc-02 (run 1) | claude-fable-5 | FAIL | Skill's own fixtures contradicted each other: UC file {H:4,M:8,L:10} + input examples vs seed/stub {H:3,M:11,L:8}. Agent detected the contradiction, chose the seed, violated the UC-file oracle. Defect in skill fixtures, fixed same day. | 2026-06-09 | claude |
| smoke-test uc-02 (re-run after fix) | claude-fable-5 | PASS | All oracle values match: 22 findings, {H:3,M:11,L:8}, 14 risk-accepted (8L+6M), 8 conditions (3H+5M), AUTHORIZE_WITH_CONDITIONS, residual MODERATE. Routing clean. | 2026-06-09 | claude |
| smoke-test uc-03 | claude-fable-5 | PASS-WITH-NOTES | All oracle assertions met (MODERATE, 71% in [68,75], 94 in [80,110], CC=9, AT-2/RA-3/SI-4 in gap list, priorities+dates). BUT values reachable only via the expected-output seed — underlying crosswalk yields ~8%; agent disclosed the discrepancy unprompted. Confirms SOX-637 (derivability defect). | 2026-06-09 | claude |

Persona vetting (same date): 8 CRITICAL / 12 HIGH — all resolved (fixed/ticketed/accepted);
see docs/persona-review.md.

## §5.11 re-verification of the 2026-06-09 fix pass (live sources, webfetch)

All externally-factual claims edited in PR #32, verified against live authoritative sources
(re-verify mode, prompts/s511-verification.md). Verdict: 7/7 VERIFIED, 0 refuted.

| fact | source | retrieval date | verifier | status |
|------|--------|----------------|----------|--------|
| SC-8(1) = "Cryptographic Protection" under SC-8 Transmission Confidentiality and Integrity; AC-18 = "Wireless Access" (in 800-53B baselines: Low AC-18; Mod AC-18(1)(3)) | csrc.nist.gov CPRT JSON (sp_800_53_5_1_1/element/SC-08) + 800-53B baseline data | 2026-06-09 | s511-agent (live fetch) | PASS |
| FedRAMP POA&M remediation: Critical/High 30 days, Moderate 90, Low 180 | fedramp.gov/docs/rev5/playbook/csp/authorization/poam/ | 2026-06-09 | s511-agent (live fetch) | PASS |
| OMB M-24-15 = "Modernizing the Federal Risk and Authorization Management Program (FedRAMP)", July 25 2024; M-22-15 is an R&D-priorities memo, not FedRAMP | whitehouse.gov M-24-15 PDF (text-extracted) + M-22-15 PDF | 2026-06-09 | s511-agent (live fetch) | PASS |
| 2017 TSC aligned to COSO 2013's 17 principles (TSC ¶.05 verbatim); no 800-53 derivation | AICPA 2017 TSC PDF | 2026-06-09 | s511-agent (live fetch) | PASS |
| CMMC 2.0 L2 = 110 NIST SP 800-171 requirements; L3 adds 24 from SP 800-172 | 32 CFR 170 final rule, govinfo.gov FR-2024-22905 | 2026-06-09 | s511-agent (live fetch) | PASS |
| OMB A-130 (2016) defines ongoing authorization; 3-year cycle is the historical Appendix III norm; no 1-year mandate exists | whitehouse.gov A-130 PDF + legacy App III | 2026-06-09 | s511-agent (live fetch) | PASS |
| Baselines are defined in SP 800-53B (separate publication), not the 800-53 catalog | csrc.nist.gov/pubs/sp/800/53/b/upd1/final | 2026-06-09 | s511-agent (live fetch) | PASS |
