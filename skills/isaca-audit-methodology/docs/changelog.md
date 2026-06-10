# Changelog - isaca-audit-methodology

All notable changes to this skill are documented here.

## [Unreleased]

### Fixed (G4.5 consumer-ready vetting, 2026-06-10 — SOX-636/SOX-630)
- **COBIT 2019 catalog rebuilt from verified publication text**: BAI12 (invented) removed; MEA04 Managed Assurance restored; BAI/MEA names corrected to official titles (BAI06 Managed IT Changes back in the catalog); counts 5/14/11/6/4 everywhere; "7 information criteria" relabeled COBIT 4.1 legacy (goals cascade documented).
- **Fake ITAF S1-S18/G1-G18 numbering retired skill-wide**; real series (General 1001-1008, Performance 1201-1207, Reporting 1401-1402, verified against ITAF 4th Ed text) now in chunk 03 and the lifecycle tables; ITAF 5th Edition (2026) cited as current; "ITAF binds the auditor, not the auditee" criteria rule added; oracle now asserts the fake numbering is absent.
- **CISA domain weights reconciled** to the live exam content outline (18/18/12/26/26, effective Aug 2024); the stale 21/17/12/23/27 removed from the limits doc.
- **Severity decoupled from MW/SD**: stub/oracle/docs aligned ("High" for the UC-02 scenario); count-based rule replaced with a labeled deviation-rate demo heuristic; ICFR deficiency classification fenced as a magnitude+likelihood judgment.
- **Output contracts unified**: chunk 03/06 templates, UCs, and README now match the tested envelope (`classification` + `maturity_assessment`/`observation`); UC-01 renamed `uc-01-saas-maturity-assessment.md`; UC-03 routed in §11; healthcare routed; phantom "other" industry dropped; broken test pointers fixed.
- **Questionnaire chunk corrected**: CCM/CAIQ v4 17-domain codes (verified), VSAQ named questionnaires, SIG 21 domains; CSA-CCM-v4 added to the citation registry.
- **HIPAA crosswalk corrected** (no change-mgmt standard in the Security Rule; break-glass = 164.312(a)(2)(ii) Required + DSS05.04; 164.312(b) quoted accurately + DSS05.07); production-safety rule for destructive ITAC tests; patient-safety impact note.
- **Effect/citation fixes**: GDPR Art 32 → Art 83(4) tier (EUR 10M/2%); bank UC effect now GLBA Interagency Guidelines/FFIEC; GLBA split by charter (16 CFR 314.1(b) vs 12 CFR 30 App. B); AT-C 320 for SOC 1; COSO Control Environment; C-C-C-E-R lineage to GAGAS 2024/IIA; fabricated focus-area titles replaced with verified ISACA publications; CMMC role updated (ISACA = CAICO, 2025); risk-scoring model + design-factor weights labeled house conventions; heat-map cells corrected; attribute-sampling formula replaced with AICPA tables pointer.
- **README regenerated from disk** (8 chunks, 4 industries, 3 UCs, real test files; canned-stub and Path-1 context warnings; data-handling caveat); acceptance-gate checkboxes re-verified against disk; persona-review.md added (G4.5 evidence).

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
