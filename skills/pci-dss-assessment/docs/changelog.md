# Changelog — PCI DSS assessment skill

All notable changes to this skill are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] — 2026-06-11 — Initial release (SOX-568, born-vetted build, M5 cycle 1)

First skill built end-to-end in M5 cycle 1 under process v3: the Day 0 fact sheet
(`docs/pci-dss-assessment-fact-sheet.md`, mechanical extraction from the licensed PCI DSS
v4.0.1 PDF) and the design doc preceded every content file; seed + derivability-oracle
contracts were written before the UC docs; G4.5 persona vetting and §5.11 live-source
verification run inside the build PR (born-vetted, not retrofitted).

### Added

- `SKILL.md` router (§1-§11 contract, §10 citation manifest, §11 routing table) + `README.md`
- 8 chunks (`chunks/01-08`): scope & applicability, scoping & segmentation, SAQ selection,
  Requirements 1-6, Requirements 7-12, validation (ROC/AOC), approaches & compensating controls,
  currency & program context (all volatile content — version currency, future-dated-now-in-force
  status, SAQ catalog versions, OLIR crosswalk status, card-brand program context — isolated in
  chunk 08)
- 4 industry views (`industries/`): saas-technology, retail-ecommerce, financial-services,
  healthcare
- 3 use cases (`use-cases/`): UC-01 SAQ selection (CartNimbus, e-commerce merchant → SAQ A-EP),
  UC-02 ROC scope & segmentation (Ironvale Retail, L1 brand-defined → 10 of 14 systems in
  scope), UC-03 compensating control (Meridian QSA-Support, legacy-POS authentication
  constraint → complete Appendix B/C worksheet)
- `data/seeds/` (self-contained UC inputs + expected outputs; zero PAN/CHD/SAD; `as_of_date`
  everywhere a date computation exists) + `data/generators/` + `data/crosswalks/` intentionally
  empty (OLIR PCI → CSF v2.0 deferral)
- Test suite + `pci_dss_assessment_stub.py`: derivability oracles (SOX-637 pattern, includes the
  standing fact-sheet inventory-diff gate), grounding, trace, metamorphic, adversarial,
  telemetry, chunk smoke tests
- 4 telemetry files: `schema.json`, `instrument.py`, `redaction.md`, `baseline.md`
- 4 docs files: `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`,
  `acceptance-gate.md` (seeded from the fact sheet's verified rows)
- Registry citations: PCI-SSC-Document-Library, PCI-SSC-Blog-v401, NIST-CSF-Informative-References,
  NIST-OLIR

### Known deferrals

- Crosswalk rows (PCI DSS v4.0.1 → CSF v2.0): pending OLIR extraction; chunks point to the OLIR
  program without asserting any row
- Card-brand compliance programs, fines, and level thresholds: pointer-only (brand-defined, no
  amounts or thresholds asserted)
- Version currency and the SAQ catalog versions must be re-verified at every G4 pass (volatile
  claims, isolated in chunk 08)
