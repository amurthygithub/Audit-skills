---
name: aicpa-soc-reporting
description: "Perform AICPA System and Organization Controls (SOC) reporting work including SOC 1, SOC 2, SOC 3, SOC for Cybersecurity, and SOC for Supply Chain engagements. Activates when the user asks about SOC report types, trust services criteria (TSC), TSP Section 100, management assertions, service auditor opinions, CUECs, CSOCs, bridge letters, readiness assessments, Type I vs Type II reports, AT-C 105/205/210/215/320 standards, or SSAE 18."
category: audit
risk: high
source: "AICPA Professional Standards (AT-C 105/205/210/215/320, TSP Section 100, SSAE No. 18, 2022 Revised Implementation Guidance), COSO 2013 Internal Control - Integrated Framework"
date_added: 2026-05-25
version: 0.2.0
status: draft
industries: [saas-technology, financial-services, healthcare, public-sector, other]
frameworks: [SOC-1, SOC-2-TSC-2017, SOC-3, SOC-for-Cybersecurity, SOC-for-Supply-Chain, COSO-2013, ISO-27001-2022, NIST-SP-800-53-Rev5, GDPR, ISAE-3000-3402, COBIT-2019]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
token_baseline_target:
  input_p90: 12000
  output_p90: 4000
context_budget:
  always_loaded_tokens: 2800
  per_call_typical_tokens: 5500
  per_call_max_tokens: 14000
  per_call_p90_tokens: 7500
tags: [aicpa, soc1, soc2, soc3, soc-for-cybersecurity, soc-for-supply-chain, attestation, trust-services-criteria, tsp-section-100, ssae-18, at-c-205, at-c-320, coso, icfr, management-assertion, cuec, csoc, bridge-letter, service-auditor, type-i, type-ii, tsc, sampling, board-deck, questionnaire-reuse, caic, sig-lite, vsaq]
---

You are an expert agent performing AICPA SOC reporting work. Follow every instruction below precisely. Use AICPA terminology exclusively.

# AICPA SOC Reporting Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent. See Section 11 Routing for the table.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- User asks about SOC 1, SOC 2, SOC 3, SOC for Cybersecurity, or SOC for Supply Chain engagements.
- User needs to scope, draft, review, or validate a SOC report or any component therein.
- User inquires about trust services criteria (TSC), TSP Section 100, or specific criteria codes (CC*, A*, PI*, C*, P*).
- User requests management assertion letters, bridge letters, CUECs, or CSOCs.
- User asks about AT-C 105/205/210/215/320, SSAE 18, or AICPA attestation standards.
- User needs to determine which SOC type applies to a given scenario.
- User requires cross-framework mapping (COSO, ISO 27001, NIST 800-53, GDPR) for SOC criteria.
- User asks about service auditor opinion types, exception evaluation, or sampling guidance for Type II.
- User needs engagement lifecycle planning (scoping, evidence gathering, report issuance, monitoring).
- User asks about customer security questionnaires (CAIQ, SIG Lite, VSAQ), questionnaire reuse, or customer audit fatigue.
- User needs an audit committee / board-ready deck template (see assets/board_deck_template.md).

### Do NOT Use This Skill When:
- User asks about financial statement audits (GAAS/PCAOB territory, not SOC attestation).
- User needs ISO 27001 certification guidance alone (without SOC overlap).
- User is performing a SOX ICFR audit (PCAOB AS 2201, not AICPA SOC 1).
- User asks about ISAE 3000/3402 exclusively (international standard -- unless comparing to AICPA SOC).
- User needs penetration testing or vulnerability assessment alone (not an attestation engagement).
- User asks about internal audit methodology unrelated to service organization controls.

## 2. Framework Overview

The AICPA SOC suite provides independent examination of a service organization's controls relevant to user entities' needs.

| Report | Standard Basis | Subject Matter | Audience | Distribution |
|--------|---------------|----------------|----------|--------------|
| SOC 1 | AT-C 320 (SSAE 18) | Controls relevant to user entities' ICFR | User entities, user auditors | Restricted |
| SOC 2 | AT-C 205 + TSP Section 100 | Controls relevant to Security, Availability, Processing Integrity, Confidentiality, Privacy | Knowledgeable users | Restricted |
| SOC 3 | AT-C 205 + TSP Section 100 | Same TSC categories as SOC 2 but summarized | General public | Unrestricted |
| SOC for Cybersecurity | AT-C 205 + Cybersecurity Description Criteria | Entity's cybersecurity risk management program | General use | Unrestricted |
| SOC for Supply Chain | AT-C 205 + TSP Section 100 (adapted) | Controls in production/manufacturing/distribution systems | User entities, supply chain participants | Restricted |

**Governing standards:** [AT-C-210], [AT-C-215], AT-C 105, AT-C 205, AT-C 320. SSAE 18 remains governing; SSAE 21 supersedes SSAE 18, and SSAE Nos. 19-21 have been issued as conforming amendments. Always cite the governing standard when drafting report language.

### 2.1 Related professional standards (cross-jurisdictional context)

- **[ISAE-3000-3402]** — IAASB's international equivalents to the AICPA's AT-C standards; used for non-US jurisdictions where the ISAs apply (EU, UK, Canada, Australia, etc.). A SOC 2 issued under ISAE 3000/3402 is functionally equivalent for most purposes.
- **[GDPR]** — EU General Data Protection Regulation; relevant when the SOC 2 report includes the Privacy TSC category and the service organization processes EU personal data. The Privacy TSC maps to many GDPR articles, but GDPR-specific obligations (DPO appointment, DPIA, breach notification within 72h) are not in TSC and require separate compliance.

## 3. Core Concepts

### 3.1 SOC Report Types
- **SOC 1** -- ICFR controls. Control objectives are management-defined (not standardized). See `chunks/04-report-structures.md`.
- **SOC 2** -- TSC-based. Security (CC) always required; A, PI, C, P optional. 51 primary criteria; ~64 with sub-criteria.
- **SOC 3** -- Same TSC as SOC 2, but abridged. No CUECs/CSOCs. General-use. No detailed tests of controls.
- **SOC for Cybersecurity** -- Entity-level cybersecurity program. Uses TSC (Security + Availability + Confidentiality). General-use.
- **SOC for Supply Chain** -- Production/manufacturing/distribution systems. Adapted TSP Section 100.
- **Type I** -- Design suitability as of a point in time. No Section IV (tests of controls).
- **Type II** -- Design suitability AND operating effectiveness over a period (>=6 months). Includes Section IV with detailed test procedures, samples, and results.

### 3.2 Key Terminology
- **CUEC** -- Complementary User Entity Controls. Controls user entities must implement for service org controls to achieve objectives.
- **CSOC** -- Complementary Subservice Organization Controls. Assumed effective under carve-out method.
- **TSC** -- Trust Services Criteria (CC1.1-CC9.2 + optional A, PI, C, P criteria). Use "Trust Services Criteria" not "Trust Services Principles" for current engagements.
- **Carve-out method** -- Subservice controls disclosed but not tested. CSOCs assumed effective.
- **Inclusive method** -- Subservice controls included in scope and tested directly.
- **Opinion types** -- Unqualified, Qualified, Adverse, Disclaimer. See `chunks/07-opinion-lifecycle-sampling.md`.
- **Bridge letter** -- Management-issued letter covering gap between SOC report periods. No auditor assurance.
- **Management assertion** -- Written statement by management about fairness of description and control effectiveness. Not a "representation letter."
- **Service auditor** -- The CPA performing the SOC examination. Not "auditor."

### 3.3 TSC Categories Summary

| Category | Code Range | Count | Required? |
|----------|-----------|-------|-----------|
| Common Criteria | CC1.1-CC9.2 | 33 | Always |
| Availability | A1.1-A1.3 | 3 | Optional |
| Processing Integrity | PI1.1-PI1.5 | 5 | Optional |
| Confidentiality | C1.1-C1.2 | 2 | Optional |
| Privacy | P1.1-P8.1 | 8 | Optional |

The AICPA commonly references approximately 64 criteria when including refined sub-criteria and 2022 revised implementation guidance expansions with additional points of focus. The exact sub-criteria count varies by publication (61-67 depending on how CC6-CC9 sub-criteria are counted). Verify against the current TSP Section 100 publication.

### 3.4 COSO Integration
The 2017 TSC was explicitly modeled on COSO 2013. CC1-CC5 correspond to COSO's 17 principles. The CC1 mapping is non-sequential: CC1.1->P1, CC1.2->P5, CC1.3->P3, CC1.4->P4, CC1.5->P2. CC6-CC9 supplement COSO Principle 12 with IT-specific controls.

## 4. Decision Logic (summary)

Full logic in chunks. Summary:

- **Engagement type** -- `chunks/02-engagement-type-decision.md`. Walk through ICFR -> TSC -> Cybersecurity -> Supply Chain.
- **Type I vs Type II** -- `chunks/02-engagement-type-decision.md`. First-time -> Type I readiness; established -> Type II (6-12 months).
- **Inclusive vs carve-out** -- `chunks/06-cuec-csoc-inheritance.md`. Subservice org has its own SOC report -> carve-out; otherwise consider inclusive.
- **Opinion determination** -- `chunks/07-opinion-lifecycle-sampling.md`. Evidence sufficiency -> exceptions in description/design/operating -> unqualified/qualified/adverse/disclaimer.
- **Sampling** -- `chunks/07-opinion-lifecycle-sampling.md`. Daily: 25-40, Weekly: 10-20, Monthly: 2-5. Deviation rate vs. tolerable rate.

## 5. Procedure Templates (summary)

- **Engagement classification** -- `chunks/02-engagement-type-decision.md` -- 4-step decision tree.
- **TSP criteria scoping** -- `chunks/03-tsp-criteria.md` -- all 33 CC + selected A/PI/C/P criteria with COSO mapping and agent directives.
- **CUEC/CSOC identification** -- `chunks/06-cuec-csoc-inheritance.md` -- 5-step identification process for each.
- **Opinion determination** -- `chunks/07-opinion-lifecycle-sampling.md` -- 5-step decision tree with compound exception handling.
- **Engagement lifecycle** -- `chunks/07-opinion-lifecycle-sampling.md` -- 4-phase lifecycle: Scoping, Evidence, Report Issuance, Monitoring.
- **Cross-framework mapping** -- `chunks/03-tsp-criteria.md` -- TSC to COSO, ISO 27001, NIST 800-53, GDPR.

## 6. Output Templates (summary)

- **SOC 1 Type I/II report structure** -- `chunks/04-report-structures.md`.
- **SOC 2 Type I/II report structure** -- `chunks/04-report-structures.md`.
- **SOC 3 report structure** -- `chunks/04-report-structures.md`.
- **SOC for Cybersecurity / Supply Chain** -- `chunks/04-report-structures.md`.
- **Management assertion (Type I 2-paragraph / Type II 3-paragraph)** -- `chunks/05-assertion-bridge.md`.
- **Bridge letter (4-attestation format)** -- `chunks/05-assertion-bridge.md`.
- **Board-ready audit committee deck** -- `assets/board_deck_template.md`.

## 7. Cross-References (summary)

Full crosswalk in `chunks/03-tsp-criteria.md`. Quick map:

| Skill | Relationship |
|-------|-------------|
| `nist-800-53-rmf` | NIST 800-53 Rev 5 control families map to TSC categories (AC->CC6, AU/SI->CC7, CM->CC8, RA->CC9, PT->Privacy P1-P8). |
| `isaca-audit-methodology` | COBIT 2019 management objectives map to TSC; ISACA sampling methodology aligns with SOC Type II. |
| `coso-internal-controls` | COSO 2013 17 principles directly underpin CC1-CC5. See coso-internal-controls chunks/07-compensating-updates-cross.md for the reverse mapping. |
| `audit-workpapers` | AS 1215 documentation standards apply; AS 1105 evidence hierarchy applies to SOC evidence. |
| `aicpa-soc-reporting` (chunk 08) | SOC 2 evidence reuse for CAIQ, SIG Lite, VSAQ, and customer questionnaires. See `chunks/08-questionnaire-reuse.md`. |

External: ISO 27001:2022 Annex A, GDPR Articles 6-79, NIST CSF 2.0, HIPAA Security Rule, CMMC 2.0.

## 8. Worked Examples (summary)

Full worked examples live in `use-cases/`. Each has complete input, procedure, expected output, and oracle.

| UC | Title | Industry | Key output |
|----|-------|----------|------------|
| UC-01 | Full SOC 2 Type II examination walkthrough | saas-technology, healthcare | SOC 2 Type II report, opinion type, CUEC/CSOC list, sampling plan |
| UC-02 | CUEC/CSOC identification for a multi-tenant SaaS | saas-technology | CUEC disclosure, CSOC list, carve-out rationale |
| UC-03 | Bridge letter for gap period between SOC 2 reports | saas-technology, financial-services | Bridge letter, management assertion |
| UC-04 | Auditee preparation for SOC 2 Type II examination | saas-technology, healthcare, financial-services | Gap analysis, remediation plan, evidence checklist, CUEC draft |

## 9. Anti-Hallucination Disclaimers

- **TSC criteria count** -- AICPA commonly references ~64 criteria when including refined sub-criteria. Exact count varies by publication (61-67 depending on how CC6-CC9 sub-criteria are counted). Verify against current TSP Section 100.
- **SOC for Cybersecurity and SOC for Supply Chain** are emerging products with guidance still evolving. Consult AICPA directly for current status.
- **SOC 1 control objectives** are management-defined, not standardized. Do not invent specific control objectives.
- **Opinion determination** is professional judgment. The decision tree encodes the framework; the practitioner makes the call.
- **SAS 70 and SSAE 16** are superseded -- never reference in current engagements. Current standard is SSAE 18.
- **SSAE 21** supersedes SSAE 18. SSAE Nos. 19-21 are conforming amendments to specific AT-C sections. Verify current text.
- **Sampling sizes** are minimums. Adjust upward for higher-risk controls or when deviations are found.
- This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| AT-C-105 | Concepts Common to All Attestation Engagements | AICPA | AT-C 105 | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| AT-C-205 | Examination Engagements | AICPA | AT-C 205 | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| AT-C-210 | Review Engagements | AICPA | AT-C 210 | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| AT-C-215 | Agreed-Upon Procedures Engagements | AICPA | AT-C 215 | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| AT-C-320 | Service Organizations - Reporting on ICFR | AICPA | AT-C 320 (SSAE 18) | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| TSP-Section-100 | Trust Services Criteria | AICPA ASEC | 2017 TSC, 2022 Revised Points of Focus | 2026-05-25 | https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 |
| COSO-2013 | Internal Control - Integrated Framework | COSO | 2013 (17 principles) | 2026-05-25 | https://www.coso.org/ |
| SOC-for-Cybersecurity | SOC for Cybersecurity Examination | AICPA | 2017 / updated | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| SOC-for-Supply-Chain | SOC for Supply Chain Examination | AICPA | 2020 | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| SSAE-18 | Statement on Standards for Attestation Engagements No. 18 | AICPA | May 2017 | 2026-05-25 | https://www.aicpa-cima.com/resources/ |
| ISO-27001-2022 | Information security management systems | ISO/IEC | 2022 | 2026-05-25 | https://www.iso.org/standard/27001 |
| NIST-SP-800-53-Rev5 | Security and Privacy Controls | NIST | Rev 5 | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| GDPR | General Data Protection Regulation | EU | Regulation 2016/679 | 2026-05-25 | https://gdpr-info.eu/ |
| ISAE-3000-3402 | International Standards on Assurance Engagements | IAASB | ISAE 3000/3402 | 2026-05-25 | https://www.iaasb.org/ |
| AICPA-Code-of-Conduct | Code of Professional Conduct | AICPA | Current | 2026-05-25 | https://www.aicpa-cima.com/resources/ |

In-body citations use the form `[LABEL N]` and resolve to this manifest.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| User intent | Load chunk(s) | Industry hint | Use case |
|-------------|---------------|---------------|----------|
| "What SOC type applies?" / "SOC 1 vs SOC 2" / "engagement type" | `chunks/01-soc-overview.md`, `chunks/02-engagement-type-decision.md` | match industry | -- |
| "TSC criteria" / "CC1.1" / "common criteria" / "Privacy criteria" | `chunks/03-tsp-criteria.md` | match industry | -- |
| "Draft a SOC 1/2/3 report" / "report structure" | `chunks/04-report-structures.md` | match industry | UC-01 |
| "Management assertion" / "bridge letter" | `chunks/05-assertion-bridge.md` | match industry | -- |
| "CUECs" / "CSOCs" / "carve-out" / "inclusive method" | `chunks/06-cuec-csoc-inheritance.md` | match industry | UC-02 |
| "Opinion type" / "qualified opinion" / "exception" / "sampling" / "engagement lifecycle" | `chunks/07-opinion-lifecycle-sampling.md` | match industry | UC-01 |
| "SOC for Cybersecurity" / "cybersecurity attestation" / "CISO asks for cybersecurity report" | `chunks/01-soc-overview.md`, `chunks/04-report-structures.md` | match industry | -- |
| "SOC for Supply Chain" / "supply chain attestation" | `chunks/01-soc-overview.md`, `chunks/04-report-structures.md` | match industry | -- |
| "Type I" / "Type II" / "Type I vs Type II" | `chunks/02-engagement-type-decision.md` | match industry | -- |
| "Full SOC 2 Type II engagement" | chunks/01, 02, 03, 04, 05, 06, 07 | saas-technology | UC-01 |
| "Preparing for SOC 2 audit" / "auditee readiness" / "audit fatigue" | chunks/06-cuec-csoc-inheritance.md | match industry | UC-04 |
| "CAIQ" / "SIG Lite" / "VSAQ" / "security questionnaire" / "customer audit fatigue" / "evidence library" | `chunks/08-questionnaire-reuse.md` | match industry | -- |
| "High-level question" / "framework overview" | this SKILL.md only | -- | -- |

**Industries** (load matching file from `industries/`): saas-technology, financial-services, healthcare, public-sector, other.

**Use cases** (load matching file from `use-cases/`): UC-01 (SOC 2 Type II), UC-02 (CUEC/CSOC), UC-03 (Bridge letter), UC-04 (Auditee preparation).

## 12. Operational Quick-Reference

The minimum cycle (always-loaded; no chunk needed for the high-level flow):

1. **Classify the engagement** -> `chunks/01-soc-overview.md` + `chunks/02-engagement-type-decision.md`. Output: SOC type + Type I/II.
2. **Scope TSC criteria** -> `chunks/03-tsp-criteria.md`. Output: criteria list (33 CC + optional).
3. **Identify subservice orgs** -> `chunks/06-cuec-csoc-inheritance.md`. Output: CUEC/CSOC list + inclusive vs. carve-out.
4. **Plan examination** -> `chunks/07-opinion-lifecycle-sampling.md`. Output: sample strategy, examination period.
5. **Draft report** -> `chunks/04-report-structures.md`. Output: complete report sections.
6. **Issue opinion** -> `chunks/07-opinion-lifecycle-sampling.md`. Output: opinion type + exception analysis.
7. **Post-issuance** -> `chunks/05-assertion-bridge.md`. Output: bridge letter if needed.
8. **Questionnaire reuse** -> `chunks/08-questionnaire-reuse.md`. Output: mapped evidence for CAIQ/SIG/VSAQ.

**Board deck**: Use `assets/board_deck_template.md` for quarterly audit committee presentations.
