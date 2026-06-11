# Changelog — SOX §302 Disclosure Controls skill

All notable changes to this skill are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] — 2026-06-11 — Initial release (SOX-570, born-vetted build, M5 cycle 2)

First §302 skill built end-to-end under process v3: the Day 0 fact sheet
(`docs/sox-302-disclosure-controls-fact-sheet.md`, mechanical transcription from public US
federal text — 15 U.S.C. 7241 + eCFR Title 17) preceded every content file; seed +
derivability-oracle contracts were written before the UC docs; G4.5 persona vetting and §5.11
live-source verification run inside the build PR (born-vetted, not retrofitted).

### Added

- `SKILL.md` router (§1-§11 contract, §10 citation manifest, §11 routing table) + `README.md`
- 7 chunks (`chunks/01-07`): §302 overview, DC&P vs. ICFR, the six certifications,
  evaluation & disclosure, the §302-vs-§404 boundary, disclosure committee & sub-certification
  cascade (labeled recommended practice / house framework), material weakness & change
- 4 industry views (`industries/`): saas-technology, financial-services, healthcare,
  manufacturing
- 3 use cases (`use-cases/`): UC-01 material-weakness ↔ DC&P-conclusion interplay (Crestline
  Financial Corp, accelerated filer), UC-02 newly-public first §302 obligations + §404(b)
  exemption (Nimbus Cloud Inc, EGC), UC-03 multi-entity sub-certification cascade coverage
  (Meridian Group, 15 entities)
- `data/seeds/` (UC-01/02/03 self-contained inputs + expected outputs; zero MNPI; `as_of_date`
  everywhere a date computation exists) + `data/registry/citations.json` (the §10 manifest
  labels); no crosswalk rows in v1
- Test suite + `sox_302_disclosure_controls_stub.py`: derivability oracles (SOX-637 pattern,
  includes the standing fact-sheet inventory-diff gate), grounding, trace, metamorphic,
  adversarial, telemetry, chunk smoke tests
- 4 telemetry files: `schema.json`, `instrument.py`, `redaction.md`, `baseline.md`
- 4 docs files: `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`,
  `acceptance-gate.md` (seeded from the fact sheet's verified rows)
- Registry citations: SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15,
  Reg-S-K-Item-307, Reg-S-K-Item-308

### Known deferrals

- Crosswalk rows (§302 DC&P ↔ §404 ICFR / cyber-8-K touchpoint): one-way prose references only
  in v1; row-level encoding deferred
- §404 ICFR assessment + auditor-attestation (AS 2201) mechanics: `coso-internal-controls`;
  boundary referenced only here
- §906 criminal certification (18 U.S.C. 1350): mentioned as the companion cert; not detailed
- Currency: the rule text (current through 2007 amendments) and the 2023 cyber additions must be
  re-verified at every G4 pass
