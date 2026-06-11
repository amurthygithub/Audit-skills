# Changelog — HIPAA Security Rule skill

All notable changes to this skill are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] — 2026-06-10 — Initial release (SOX-572, born-vetted build)

First skill built end-to-end under process v3: the Day 0 fact sheet
(`docs/hipaa-security-rule-fact-sheet.md`, mechanical eCFR transcription) and the design doc
(`docs/builds/hipaa-security-rule/hipaa-security-rule-design.md`) preceded every content file;
seed + derivability-oracle contracts were written before the UC docs; G4.5 persona vetting and
§5.11 live-source verification run inside the build PR (born-vetted, not retrofitted).

### Added

- `SKILL.md` router (§1-§11 contract, §10 citation manifest, §11 routing table) + `README.md`
- 8 chunks (`chunks/01-08`): scope & general rules, risk analysis & management,
  administrative safeguards, physical safeguards, technical safeguards, organizational &
  documentation, addressable decisions & evidence, enforcement/audit/NPRM (all NPRM content
  isolated in chunk 08 and flagged PROPOSED)
- 4 industry views (`industries/`): healthcare, saas-technology, financial-services,
  public-sector
- 3 use cases (`use-cases/`): UC-01 BA risk analysis & addressable dispositions (CareSync
  Relay, 40 staff), UC-02 hospital CE OCR-readiness (Bellbrook Regional Health, 6k staff),
  UC-03 solo-consultant BAA + right-sized safeguard checklist (Meridian HIT Consulting, 1
  person)
- `data/seeds/` (UC inputs, sub-seeds, expected outputs; zero PHI; `as_of_date` everywhere a
  date computation exists) + `data/generators/` (addressable register, control inventory) +
  `data/crosswalks/` intentionally empty (CPRT deferral, SOX-638)
- Test suite + `hipaa_security_rule_stub.py`: derivability oracles (SOX-637 pattern, includes
  the standing fact-sheet inventory-diff gate), grounding, trace, metamorphic, adversarial,
  telemetry, chunk smoke tests
- 4 telemetry files: `schema.json`, `instrument.py`, `redaction.md`, `baseline.md`
- 4 docs files: `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`,
  `acceptance-gate.md` (seeded from the fact sheet's verified rows with verbatim anchors)
- Registry citations: CFR-45-164-Subpart-C, HIPAA-Security-NPRM-2025, NIST-SP-800-66-Rev2,
  HHS-SRA-Tool, PL-116-321, CFR-45-102

### Known deferrals

- Crosswalk rows (Security Rule → CSF → 800-53): SOX-638, pending CPRT extraction
- Breach Notification Rule (Subpart D) mechanics: future skill; touchpoints only here
- NPRM status must be re-verified at every G4 pass (volatile claim)
