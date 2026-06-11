# Changelog -- audit-workpapers

All notable changes to this skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.0] -- 2026-06-03

### Changed (BREAKING)
- Adopted the router + chunks pattern (per TEMPLATE section 11).
  - SKILL.md reduced from 2,060 lines (v1.0) to 184 lines (router only).
  - Deep-dive content moved to 7 chunk files under chunks/ (each  - Deep-dive content moved to 7 chunk files under chunks/ (ele mapping user intent to chunks to load.
- Frontmatter now declares context_budget with always_loaded_tokens: 3000, per_call_typical_tokens: 6000, per_call_max_tokens: 15000, per_call_p90_tokens: 8000.
- Version reset from 1.0 to 0.2.0 (Spine-compliant semver).
- Added new frontmatter fields: industries, frameworks, telemetry_contract, token_baseline_target, context_budget.
- Added industries/, use-cases/, data/, tests/, telemetry/, docs/ directories.

### Added
- 7 chunk files covering: standards & structure, evidence & re-performance, sampling, risk & opinion, findings & workflow, outputs & electronic review, quality & compliance & cross-refs.
- 3 industry views: financial-services, public-sector, saas-technology.
- 2 use cases: UC-01 (MUS sampling AR), UC-02 (5-part finding AP cutoff).
- Telemetry: schema.json, instrument.py, redaction.md, baseline.md (copied from TEMPLATE).
- Docs: architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md.
- Tests: conftest.py, test_lint.py.

### Notes
- Original 2,060-line SKILL.md preserved as SKILL.md.bak.
- Per-call token cost reduced from ~40,000 (monolithic) to 3,000-6,000 (router + 1-2 chunks).
- The chunks are loaded on demand by the LLM agent per SKILL.md section 11 Routing.
- LLM-backed executor is a stub in this version; production executor ships in SOX-611 Phase 2.

## [1.0] -- 2026-05-25

### Added
- Initial monolithic SKILL.md (2,060 lines) covering PCAOB AS 1215, AS 2315, AS 1105, AS 3105, AICPA AU-C 230, ISA 230, COSO ICIF-2013, ISACA ITAF.
- Complete sampling methodology (MUS/PPS, attribute, variables, non-statistical, dual-purpose, sequential, ML-enhanced).
- Audit risk model (AR = IR x CR x AP x TD) with worked examples.
- 5-part finding format (C-C-C-E-R) with severity classification.
- 7-step workpaper creation workflow.
- Output templates: standard WP, sampling WP, finding, ECD, tickmark legend, cross-ref- Output templates: standard WP, sampling WP, finding, ECD, tickmark legend, cross-equirements and review standards.
- Compliance validation rules and cross-reference tables.
- Key terminology glossary (64 terms).
- 14 agent behavioral requirements.
- 5 complete worked examples (MUS, attribute, variables, finding, mock workpaper).

## 2026-06-10 — SOX-600/601: silent-default contract fix (found by the eval harness probe)

- `_mus_evaluate` no longer silently defaults a missing `population_book_value` or
  `tolerable_misstatement` (pre-fix: missing BV defaulted to $12.5M and sized n=187 against
  the wrong population) and refuses on TM <= 0 / BV < 0 (pre-fix: negative TM emitted
  SI=-66,667). Abstention is the passing answer — ask, never assume a materiality.
- `test_uc_01_missing_tm` previously ASSERTED the silent default; replaced by two refusal
  tests. Found by the SOX-600 perturbation probe before the generator even ran.
- This skill is an eval-harness pilot: 54 cases under `evals/audit-workpapers/cases/`
  (4 hand-written incl. the SIEVE MUS PoC, 45 boundary-sampled, 5 perturbations),
  oracle-labeled and CI-enforced.

## 2026-06-10 — eval-driven skill fix: RF table interpolation barred

- chunks/03-sampling.md: explicit "off-table parameters: do not interpolate" instruction
  after the RF table. Found by the LLM eval lane (sweep 1): at RIA 7% the model answered by
  interpolating instead of refusing — ambiguous instructions are a skill bug
  (validation-harness-design.md section 7). Post-fix: 2/2 refusals.
