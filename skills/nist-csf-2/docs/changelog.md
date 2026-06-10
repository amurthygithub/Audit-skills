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

### Fixed (G4.5 consumer-ready vetting, 2026-06-10 — SOX-636)
- **Invented CSF identifiers removed**: GV.PO-03/-04 and PR.AT-03 do not exist; RS.AN-01 removed from 2.0 contexts (2.0 = RS.AN-03/-06/-07/-08); subcategory glosses corrected to verified verbatim texts across SKILL.md, chunks 05/06, industries, and UCs.
- **Tiers framing corrected skill-wide**: Tiers characterize risk-governance rigor, are applied to Organizational Profiles, and are NOT maturity levels; per-Function/fractional Tiers and the status scale labeled as house conventions (no official NIST status scale exists — SP 1301's example is notional); the invented "800-53 Tiers = FIPS 199 impact" reconciliation replaced with the real three-construct disambiguation (CSF Tiers / 800-39 Tiers / FIPS 199 levels).
- **All three UC docs rebuilt to their seeds** (each previously described a different company than its tested fixture): UC-01 DataRelay (8-row sample, MFA-since-day-1 truth, stub-aligned tiers), UC-02 Pinecrest ($24B; fabricated 2-quarter trend replaced by the baseline-note rule; "21-day FFIEC MTTD target" and inapplicable Heightened-Standards mandates removed), UC-03 Apex Manufacturing rebuilt on **800-171 Rev 2** — CMMC L2 assesses Rev 2 (110/14) per 32 CFR 170.14(c)(3), not Rev 3 (97/17); file renamed `uc-03-csf-to-800-171-cmmc-l2.md`; seed family labels corrected (3.13.x=SC, 3.3.x=AU, 3.11.x=RA, 3.8.x=MP) and key mappings fixed (PR.DS-01→3.13.16, PR.AA-03→3.5.3, DE.CM-01→3.14.6); IR readiness counts capped at the family's real 3 controls.
- **Stub heuristic made honest**: tier rollup documented (Not=1, Partially/Largely=2, Fully=3; median; never exceeds T3), all 6 Functions emitted (RECOVER no longer dropped), UC-03 fallback no longer fabricates an Access-Control mapping for every gap.
- **Stale/fabricated regulatory anchors fixed**: FFIEC CAT marked SUNSET (eff. Aug 31, 2025; no v2 ever existed; Domain 4 = External Dependency Management; CAT cites replaced with FFIEC IT Handbook/interagency guidance); CISA CPG content updated to the real CPG 2.0 (Dec 11, 2025; ~34 goals, IDs 1.A-6.A — the "8-element" claim and CPG 1-8 table were fabricated); FedRAMP "12-month ATO" statute claim removed (no statutory duration; JAB→FedRAMP Board); HIPAA regulator notification corrected to §164.408; SEC 1.05 wording verified; QSG SP numbers corrected (SP 1300 = Small Business; no per-Function series; no "Profile success story" SP); CJIS v6.0; TX §2054.515 vs §2054.0593; 44 USC §3554; EO 13800 federal CSF mandate stated.
- **Phantom `data/crosswalks/` references removed** (the directory never existed; chunk 08 §7's no-derivative-JSON stance is now consistent skill-wide); MA restored to the 20-family 800-53 list; pseudo-precise "PDF lines 738-906" cites replaced; chunk 06 %-gap table cells corrected to its own formula (33%/50%).
- **README/architecture/acceptance-gate regenerated from disk** (7 test files + stub; frontmatter unified with SKILL.md: status draft, risk informational, real context budget); the acceptance gate's unresolved "hmm = 27, need recount" row, false "24 categories" caveat, and backwards ID.AM-06 claim replaced with the verified table; persona-review.md added.


### Planned (v0.2.0)

- Healthcare industry (deferred from v0.1.0)
- Auditee-perspective variants of the 4 existing industries (currently most are auditor-lens)

### Planned (v1.0)

- Full HIPAA + HITRUST crosswalk
- SOC 2+ assessment as a CSF 2.0 Profile input
- Community Profile templates (FFIEC, CISA CPGs)
