# Changelog — nist-800-53-rmf

All notable changes to this skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Fixed (SOX-637 — UC-03 data coherence, 2026-06-10, M2)
- UC-03 headline restated to what the shipped data supports: curated-sample crosswalk (33 mappings, 39 unique control IDs after splitting comma entries) + representative 93-record gap register; the underivable "231 mapped / 71% overlap / 94 gaps" claims retired.
- Stub now COMPUTES the UC-03 summary from the crosswalk + gap register; the oracle recomputes independently from the seeds (non-circular) and asserts footing invariants (totals foot; priorities sum; no overlap % emitted).
- One disposition per control: 12 partially-mapped controls (AT-2, RA-3, SI-4, ...) now carry `strengthen`; 81 carry `gap`; gap-register evidence_refs no longer point at nonexistent docs/remediation files.
- AC-2(4)→AC-2 (statement j, account review) corrected across the UC-02 seed, doc, and generator (AC-2(4) is Automated Audit Actions).
- SP 800-53B added to the citation registry and §10 manifest; financial-services.md inheritance claim qualified by deployment model; expected/remediation seeds regenerated so every count foots.


## [0.2.0] — 2026-06-03

### Changed (BREAKING)
- **Adopted the router + chunks pattern** (per TEMPLATE §11).
  - `SKILL.md` reduced from 506 lines to 218 lines (router only).
  - Deep-dive content moved to 7 chunk files under `chunks/` (each ≤ 87 lines, RMF-step aligned).
  - `SKILL.md` §11 contains a routing table mapping user intent → chunks to load.
- **Frontmatter now declares `context_budget`** with `always_loaded_tokens: 3000`, `per_call_typical_tokens: 6000`, `per_call_max_tokens: 15000`, `per_call_p90_tokens: 8000`.
- **Use-case `procedure:` frontmatter** now references `chunks/NN-*.md` instead of `§X.Y` sections.
- **Linter updated** to enforce: `SKILL.md` ≤ 300 lines OR `chunks/` subdir + routing table; `chunks/*.md` ≤ 200 lines each; `chunks/` files must match `NN-slug.md`; `context_budget` field is required.
- **Trace test updated** to validate only the structured `procedure:` frontmatter (the canonical citation), and to accept `chunks/NN-*.md` references.

### Notes
- Per-call token cost reduced from ~20,000 (monolithic) to 3,000-6,000 (router + 1-2 chunks).
- The chunks are loaded on demand by the LLM agent per `SKILL.md §11 Routing`.
- Migration of the 4 pre-Spine skills (1,580-2,060 lines) to this pattern is tracked in **SOX-611 Phase 2**.

## [0.1.0] — 2026-06-03

### Added
- Initial scaffold under the Tier 0 Spine (TEMPLATE).
- SKILL.md (~1,500 lines) covering FIPS 199, RMF 7-step, 800-53 Rev 5, 800-53A, ATO logic, output templates, cross-references, anti-hallucination disclaimers, citation manifest.
- 4 industry views: `public-sector.md`, `financial-services.md`, `saas-technology.md`, `healthcare.md`.
- 3 use cases: UC-01 FedRAMP Moderate, UC-02 Agency ATO, UC-03 SOC 2 → 800-53 crosswalk.
- Synthetic data generators: `gen_fips199.py`, `gen_sar_findings.py`, `gen_crosswalk_gap.py`.
- Seeds: `uc-01-input.json`, `uc-01-crm.json`, `uc-01-expected.json`, `uc-02-input.json`, `uc-02-findings.json`, `uc-02-expected.json`, `uc-03-input.json`, `uc-03-gap-list.json`, `uc-03-remediation.json`, `uc-03-expected.json`.
- Crosswalk: `data/crosswalks/soc2-to-800-53-mod.json` (33 mappings covering 27 unique 800-53 controls).
- 7 test files: `test_oracle.py`, `test_trace.py`, `test_grounding.py`, `test_metamorphic.py`, `test_adversarial.py`, `test_telemetry.py`, `test_lint.py`.
- Telemetry: `schema.json`, `instrument.py`, `redaction.md`, `baseline.md`.
- Docs: `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md`.

## 2026-06-10 — SOX-638 (part 1): HIPAA crosswalk rebuilt from NIST CPRT

- `data/seeds/hipaa-to-800-53.json` regenerated from the CPRT OLIR set SP-800-66-Rev-2-to-SP-800-53-Rev-5.1.1 (extraction archived at `docs/builds/sox-638/cprt-extraction.json`): 12 rows -> 68 Security Rule elements / 279 mapping rows / 108 unique 800-53 Rev 5.1.1 controls.
- Invented `exact`/`partial` strength ratings removed — the OLIR source carries none (informative references).
- Prior wrong rows corrected by regeneration, e.g. 164.308(a)(5)(ii)(C) log-in monitoring: was AT-2 "exact"; CPRT says AT-3 + AU-6 (the persona-suggested AC-7/AU-2/AU-6 was also wrong — source wins).
- §164.310 physical safeguards now fully covered (12 elements / 60 rows); emergency-access (break-glass) row present (164.312(a)(2)(ii) -> AC-2, AC-3, CP-2).
- Generator: `data/generators/gen_hipaa_crosswalk.py` (deterministic; summary computed from rows).
- Healthcare provider UC + FIPS-199 PHI guidance remain open under SOX-638 (part 2).
