# Changelog -- aicpa-soc-reporting

All notable changes to this skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.0] -- 2026-06-03

### Changed (BREAKING)
- Adopted the router + chunks pattern (per TEMPLATE Section 11).
  - `SKILL.md` reduced from 1,580 lines to ~280 lines (router only). Original preserved as `SKILL.md.bak`.
  - Deep-dive content moved to 7 chunk files under `chunks/` (each <= 200 lines).
  - `SKILL.md` Section 11 contains a routing table mapping user intent -> chunks to load.
- Frontmatter now declares `context_budget` with `always_loaded_tokens: 2800`, `per_call_typical_tokens: 5500`, `per_call_max_tokens: 14000`, `per_call_p90_tokens: 7500`.
- Added: `industries/` (4 industry files), `use-cases/` (2 UC stubs), `docs/` (4 files), `telemetry/` (from TEMPLATE), `tests/` (conftest.py + test_lint.py), `data/README.md`.
- Old section numbering (1-29 in .bak) mapped to new chunk organization:
  - Sections 2-4 -> chunk 01 (SOC overview)
  - Sections 5-6 -> chunk 02 (engagement type decision)
  - Section 7 + 20 -> chunk 03 (TSP criteria + cross-framework maps)
  - Sections 8-10 + 18-19 + 21 -> chunk 04 (report structures)
  - Sections 11-12 -> chunk 05 (assertions + bridge letter)
  - Sections 13-14 -> chunk 06 (CUEC/CSOC)
  - Sections 15-17 + 20 -> chunk 07 (opinion, lifecycle, sampling, crosswalks)
- Sections 23 (quality gates), 24 (terminology), 25 (behavioral requirements), 26 (examples), 27 (updates), 28 (ethics), 29 (QC) folded into router and chunks.

### Notes
- Per-call token cost reduced from ~35,000 (monolithic) to 2,800-5,500 (router + 1-2 chunks).
- Chunks are loaded on demand by the LLM agent per `SKILL.md` Section 11 Routing.
- `SKILL.md.bak` preserved for reference.
- Use-case files and test files are stubs. Full UC execution ships in SOX-611 Phase 2.

## [0.1.0] -- 2026-05-25

### Added
- Initial monolithic SKILL.md (1,580 lines) covering SOC 1/2/3/for-Cybersecurity/for-Supply-Chain, TSC criteria, engagement lifecycle, opinion determination, sampling, CUECs/CSOCs, bridge letters, cross-framework mappings.
