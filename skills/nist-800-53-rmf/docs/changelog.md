# Changelog — nist-800-53-rmf

All notable changes to this skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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
- SKILL.md (~1,500 lines) covering FIPS 199, RMF 7-step, 800-53 Rev 5/5.1.1, 800-53A, ATO logic, output templates, cross-references, anti-hallucination disclaimers, citation manifest.
- 4 industry views: `public-sector.md`, `financial-services.md`, `saas-technology.md`, `healthcare.md`.
- 3 use cases: UC-01 FedRAMP Moderate, UC-02 Agency ATO, UC-03 SOC 2 → 800-53 crosswalk.
- Synthetic data generators: `gen_fips199.py`, `gen_sar_findings.py`, `gen_crosswalk_gap.py`.
- Seeds: `uc-01-input.json`, `uc-01-crm.json`, `uc-01-expected.json`, `uc-02-input.json`, `uc-02-findings.json`, `uc-02-expected.json`, `uc-03-input.json`, `uc-03-gap-list.json`, `uc-03-remediation.json`, `uc-03-expected.json`.
- Crosswalk: `data/crosswalks/soc2-to-800-53-mod.json` (33 mappings covering 27 unique 800-53 controls).
- 7 test files: `test_oracle.py`, `test_trace.py`, `test_grounding.py`, `test_metamorphic.py`, `test_adversarial.py`, `test_telemetry.py`, `test_lint.py`.
- Telemetry: `schema.json`, `instrument.py`, `redaction.md`, `baseline.md`.
- Docs: `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md`.
