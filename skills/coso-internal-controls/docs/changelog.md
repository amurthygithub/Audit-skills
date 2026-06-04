# Changelog — coso-internal-controls

All notable changes are documented here.

## [Unreleased]

## [0.2.0] — 2026-06-03

### Changed (BREAKING)
- **Adopted the router + chunks pattern** (per TEMPLATE sect.11).
  - SKILL.md reduced from 1,879 lines to 214 lines (router only).
  - Deep-dive content moved to 7 chunk files under chunks/.
  - SKILL.md sect.11 contains a routing table mapping user intent to chunks.
- **Frontmatter now declares context_budget** with tokens: always_loaded 3000, typical 6000, max 15000, p90 8000.
- **Use-case procedure frontmatter** now references chunks/NN-*.md.
- **Linter updated** to enforce SKILL.md <= 300 lines, chunks <= 200 lines, NN-slug.md naming.

### Notes
- Per-call context cost reduced from ~40,000 (monolithic) to 3,000-6,000 (router + 1-2 chunks).
- 71 of 81 Points of Focus preserved (curated subset from the original body).
- PCAOB AS 2201 reorganization disclosure preserved.
- 3 industry files: financial-services, public-sector, saas-technology.
- 2 use cases: UC-01 (SOX 404 ICFR), UC-02 (deficiency classification).

## [0.1.0] — 2026-05-25

### Added
- Initial monolithic SKILL.md (1,879 lines) covering COSO ICIF 2013, ERM 2017, SOX 404, PCAOB AS 2201, walkthroughs, deficiency classification, RcM, report templates, compensating controls, emerging tech, cross-references, and examples.
