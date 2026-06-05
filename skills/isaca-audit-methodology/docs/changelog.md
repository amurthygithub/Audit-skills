# Changelog - isaca-audit-methodology

All notable changes to this skill are documented here.

## [Unreleased]

## [0.2.0] - 2026-06-03

### Changed (BREAKING)
- **Adopted the router + chunks pattern** (per TEMPLATE S11).
  - `SKILL.md` reduced from 1,662 lines to 198 lines (router only).
  - Deep-dive content moved to 7 chunk files under `chunks/` (each <= 200 lines).
  - `SKILL.md` S11 contains a routing table mapping user intent to chunks.
- **Frontmatter now declares `context_budget`** with 4 token fields.
- **Added industries/**, **use-cases/**, data/, tests/, telemetry/, docs/.
- **Linter enforces**: `SKILL.md` <= 300 lines, `chunks/*.md` <= 200 lines each, `NN-slug.md` naming, `context_budget` required.

### Notes
- Per-call token cost reduced from ~20,000 (monolithic) to ~3,200-6,500 (router + 1-2 chunks).
- The chunks are loaded on demand by the LLM agent per `SKILL.md S11 Routing`.
- Original `SKILL.md.bak` (1,662 lines) preserved for reference.

## [0.1.0] - 2026-05-25

### Added
- Initial monolithic SKILL.md (1,662 lines) covering CISA 5 domains, COBIT 2019, ITAF, ITGC/ITAC, risk planning, 5-part observations, maturity model, cross-references, terminology.
- Pre-Spine layout (no chunks/, no industries/, no use-cases/, no telemetry/).
