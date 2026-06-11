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
- 71 of the Points of Focus preserved (curated subset from the original body).
- PCAOB AS 2201 reorganization disclosure preserved.
- 3 industry files: financial-services, public-sector, saas-technology.
- 2 use cases: UC-01 (SOX 404 ICFR), UC-02 (deficiency classification).

## [0.1.0] — 2026-05-25

### Added
- Initial monolithic SKILL.md (1,879 lines) covering COSO ICIF 2013, ERM 2017, SOX 404, PCAOB AS 2201, walkthroughs, deficiency classification, RcM, report templates, compensating controls, emerging tech, cross-references, and examples.

## 2026-06-11 — SOX-641 (correctness slice): UC-02 occurrence-assertion rework + citation hygiene

- **UC-02 reworked from a security-unsound SD to a derivable Material Weakness** (3PAO CRITICAL; Partner put MW on the table). The compensating-control test is now two-part: a control mitigates only if it (1) addresses the ASSERTION AT RISK (improper access → occurrence/validity, not the completeness/accuracy that reconciliations cover) AND (2) is independent of the deficiency (not drawing IPE from the affected system). The three reconciliations fail both. Added: ITGC-pervasiveness step, authority-driven magnitude (not a per-transaction cap), and the lookback procedure that gates the conclusion. Full-stack: seed + stub (computes the classification) + derivability oracle + metamorphic test (a qualifying occurrence-control + affirmative lookback moves it off MW) + UC doc + chunk 07.
- **Citation hygiene:** COSO-RPA-2024 and COSO-GenAI-2026 verified REAL (not fabricated) and re-cited with correct titles ("Achieving Effective Internal Control Over Robotic Process Automation", Dec 2024; "Achieving Effective Internal Control Over Generative AI (GenAI)", Feb 2026, coso.org/generative-ai).
- **UC-01 scoping note:** the period-end financial reporting process and ITGCs are always in scope for an accelerated filer (a risk-based scope reduces transaction coverage, never these).
- Split to own tickets: Green Book layer (SOX-668), 404(a) path (SOX-669), non-issuer branch (SOX-670). PoF-count audit gated on the COSO 2013 copy.
