# Changelog — NIST CSF 2.0 skill

All notable changes to this skill are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] — 2026-06-08 — Wave 1 + Wave 2 initial release

### Added (Wave 1)

- `SKILL.md` — 239-line router with 12 sections, 8-row §11 routing table, 22-entry §10 manifest
- 8 chunks (`chunks/01-08`): Functions/Categories, Tiers/Profiles, Current Profile, Target Profile & Gap, GOVERN function, Enterprise Reporting, Implementation Playbook, Informative References Crosswalk (49 verified CSF↔800-53 rows)
- Cross-references to all 5 sibling skills
- 8 anti-hallucination disclaimers in §9

### Added (Wave 2)

- 4 industry views (`industries/`): financial-services, public-sector, saas-technology, manufacturing
- 3 use cases (`use-cases/`): UC-01 first Organizational Profile, UC-02 board maturity report, UC-03 Current/Target → 800-53 crosswalk
- 9 test files + `nist_csf_2_stub.py` (132 lines)
- 4 docs files: `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md`
- 4 telemetry files: `schema.json`, `instrument.py`, `redaction.md`, `baseline.md`
- 1 README.md at skill root
- `conftest.py:SKILLS` tuple updated to include `"nist-csf-2"`
- `data/generators/gen_profile.py` + `data/seeds/uc-0{1,2,3}-input.json` (Day 4 work)

### Process

- 5-lens review + 5-practitioner review of Wave 1 router + chunks (8 CRITICAL + 17 HIGH + 9 MEDIUM + 8 LOW caught)
- Source-of-truth verification against NIST CSF 2.0 PDF, NIST IR spreadsheet, NIST QSGs
- §5.11 verification gate codified in `docs/skill-design-template.md` and applied to all 4 industries
- All "108 subcategory" references corrected to 106 (108 is CSF 1.1 count, 106 is CSF 2.0)

### Deferred to v0.2.0 / v1.0

- Healthcare industry (HIPAA + HITRUST) — deferred to v1.0 per user decision at m1253 (needs `data/crosswalks/csf-to-hipaa.json`)
- Full `data/crosswalks/*.json` — Wave 3 (CSF→800-53, CSF→800-171, CSF→ISO 27001, CSF→HIPAA, CSF 2.0 Subcategories canonical)
- Practitioner-perspective industry views (current industries are all auditor-lens or auditee-lens; need explicit auditor-vs-auditee distinction)

## [Unreleased]

### Planned (v0.2.0)

- Healthcare industry (deferred from v0.1.0)
- Auditee-perspective variants of the 4 existing industries (currently most are auditor-lens)

### Planned (v1.0)

- Full HIPAA + HITRUST crosswalk
- SOC 2+ assessment as a CSF 2.0 Profile input
- Community Profile templates (FFIEC, CISA CPGs)
