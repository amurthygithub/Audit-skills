---
name: isaca-audit-methodology
description: "Perform ISACA-based IT audit work including CISA methodology, COBIT 2019 governance/management objectives, ITAF standards, ITGC/ITAC testing, risk-based audit planning, 5-part audit observations, COBIT maturity assessment, and cross-framework mapping. Activate when performing IT audits, IS audits, control assessments, COBIT evaluations, IT risk assessments, audit observation writing, ITGC/ITAC testing, audit planning, or audit report generation."
category: audit
risk: high
source: "ISACA CISA CRM 28th Ed 2024, COBIT 2019, ITAF, ISACA Code of Professional Ethics"
date_added: 2026-05-25
version: 0.2.0
status: draft
industries: [financial-services, saas-technology, public-sector, healthcare, other]
frameworks: [ISACA-CISA-CRM, COBIT-2019, ITAF, COSO-2013, NIST-CSF-2.0, ISO-27001-2022, AICPA-TSC-2017]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
token_baseline_target:
  input_p90: 16000
  output_p90: 5000
context_budget:
  always_loaded_tokens: 3200
  per_call_typical_tokens: 6500
  per_call_max_tokens: 16000
  per_call_p90_tokens: 8500
tags: [isaca, cisa, cobit-2019, itaf, itgc, itac, it-audit, risk-assessment, audit-observation, maturity-model, internal-controls, governance, compliance, coso, aicpa, nist, iso-27001, board-deck, questionnaire-reuse, caic, sig-lite, vsaq]
---

You are an expert agent performing ISACA-based IT audit work. Follow every instruction below precisely. Use official ISACA/COBIT terminology exclusively.

# ISACA IT Audit Methodology Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent. See S11 Routing for the table.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Planning or executing an IT audit engagement (IS audit, integrated audit, compliance audit).
- Performing ITGC or ITAC testing and assessment.
- Developing a risk-based audit plan or audit universe.
- Writing audit observations using the 5-part format (Condition, Criteria, Cause, Effect, Recommendation).
- Assessing COBIT 2019 governance or management objectives.
- Performing COBIT maturity assessments (legacy 0-5 or CMMI-based 0-5).
- Mapping controls across frameworks (COBIT, COSO, NIST, ISO 27001, AICPA).
- Evaluating IT governance, risk management, or security controls.
- Reusing ISACA/COBIT/ITGC evidence for customer security questionnaires (CAIQ, SIG Lite, VSAQ).
- Using the board-ready audit committee deck template (see aicpa-soc-reporting/assets/board_deck_template.md).

### Do NOT Use This Skill When:
- Performing financial statement audits (use AICPA/GAAP methodology).
- Providing legal opinions or regulatory compliance certifications.
- Performing penetration testing or vulnerability assessment (use security testing methodology).
- Providing audit opinions without sufficient, reliable, relevant evidence.
- Overriding organizational audit charters or policies.
- Replacing professional judgment of certified IS auditors.

## 2. Framework Overview

ISACA (est. 1969) provides global standards for IT governance, audit, risk, and cybersecurity. This skill encodes CISA domains (5 domains, 21/17/12/23/27% weights), COBIT 2019 (40 objectives: 5 EDM + 14 APO + 12 BAI + 6 DSS + 3 MEA), ITAF standards (S1-S18 pedagogical reconstruction), ITGC/ITAC testing, risk-based audit planning, 5-part observation format, and cross-framework mapping.

| Layer | Document | Role |
|-------|----------|------|
| Professional certification | CISA CRM 28th Ed | 5-domain methodology; 2024 edition |
| IT governance | COBIT 2019 | 40 governance/management objectives, design factors, maturity model |
| Audit standards | [ITAF] (ISACA) | Mandatory standards (Tier 1), guidelines (Tier 2), procedures (Tier 3) |
| ITGC | ISACA methodology | Access, Change, Operations, SDLC (4 categories) |
| ITAC | ISACA methodology | Input, Processing, Output, Data Integrity (4 categories) |
| Risk & Planning | ISACA methodology | 5-step planning, risk scoring (L x I x CRF), audit universe |
| Observations | ISACA methodology | 5-part format: Condition, Criteria, Cause, Effect, Recommendation |
| Ethics | [ISACA-ETHICS] | 7 principles |

### 2.1 Related frameworks (governance and adjacent standards)

- **[ITIL]** — IT service management framework; complements COBIT 2019's BAI/DSS domains; used for change, incident, and problem management.
- **[ISO-38500]** — Corporate governance of IT; the top-level standard COBIT 2019 maps into; sets the "evaluate, direct, monitor" pattern at board level.
- **[NIST-SP-800-61]** — NIST Computer Security Incident Handling Guide; pairs with ISACA's ITGC operations category for incident response audit testing.

## 3. Core Concepts

### 3.1 CISA 5 Domains

D1 (21%): Auditing Process. D2 (17%): Governance. D3 (12%): Acquisition/Development. D4 (23%): Operations/Resilience. D5 (27%): Protection of Information Assets. Full detail in `chunks/01-framework-and-cisa.md`.

### 3.2 COBIT 2019

40 objectives in 5 domains: EDM (governance, 5 objectives), APO (align/plan, 14), BAI (build/acquire, 12), DSS (deliver/service, 6), MEA (monitor/evaluate, 3). Plus 7 information criteria and 5 design factors. Full detail in `chunks/02-cobit-2019.md`.

### 3.3 ITAF

Tier 1: Mandatory standards (S1-S18, pedagogical numbering). Tier 2: Guidelines (G1-G18). Tier 3: Procedures/Techniques. **Important:** S1-S18/G1-G18 are reconstructed for reference; not official ITAF numbering. Full detail in `chunks/03-itaf-and-maturity.md`.

### 3.4 ITGC / ITAC

ITGC: Access Controls, Change Management, IT Operations, SDLC (4 categories). ITAC: Input, Processing, Output, Data Integrity (4 categories). ITGC effectiveness determines ITAC reliance. Full detail in `chunks/04-itgc-itac.md`.

### 3.5 Risk-Based Audit Planning

5-step methodology: Establish Audit Universe, Perform Risk Assessment, Prioritize Engagements, Develop Annual Plan, Execute and Monitor. Risk Score = (Likelihood x Impact) x Control Risk Factor. Full detail in `chunks/05-risk-and-planning.md`.

### 3.6 5-Part Observation Format

Condition (what is), Criteria (what should be), Cause (why), Effect (so what), Recommendation (what should be done). Always cite specific ISACA standards, COBIT objectives, or policies. Full detail in `chunks/06-observation-and-lifecycle.md`.

## 4. Decision Logic (summary)

- **Risk score** -> `chunks/05-risk-and-planning.md §Decision`. Use (L x I) x CRF. Priority: Critical >= 15, High 10-14, Medium 5-9, Low 1-4.
- **ITGC -> ITAC reliance** -> `chunks/04-itgc-itac.md §ITGC-to-ITAC`. If ITGC effective -> controls-based; if not -> substantive; if partial -> hybrid.
- **Audit approach** -> `chunks/06-observation-and-lifecycle.md §Approach`. Controls-based, substantive, or hybrid depending on ITGC effectiveness.
- **COBIT maturity** -> `chunks/03-itaf-and-maturity.md §Maturity`. Rate at highest level where ALL attributes are satisfied.
- **Finding severity** -> `chunks/05-risk-and-planning.md §Severity`. Critical = Material Weakness, High = Significant Deficiency, Medium = Deficiency, Low = Observation.

## 5. Procedure Templates (summary)

- **COBIT 2019 Assessment** -> `chunks/02-cobit-2019.md §Assessment procedure` (10 steps).
- **ITGC Assessment** -> `chunks/04-itgc-itac.md §ITGC procedure` (10 steps).
- **ITAC Assessment** -> `chunks/04-itgc-itac.md §ITAC procedure` (9 steps).
- **Risk-Based Audit Planning** -> `chunks/05-risk-and-planning.md §Procedure` (5 steps).
- **Audit Engagement Lifecycle** -> `chunks/06-observation-and-lifecycle.md §Lifecycle` (Planning, Fieldwork, Reporting, Follow-Up).
- **5-Part Observation** -> `chunks/06-observation-and-lifecycle.md §5-Part format`.

## 6. Output Templates (summary)

- **Audit Report** -> `chunks/07-outputs-and-cross-refs.md §Audit report`.
- **Audit Observation (5-part)** -> `chunks/07-outputs-and-cross-refs.md §Observation template`.
- **Risk Assessment Output** -> `chunks/07-outputs-and-cross-refs.md §Risk assessment`.
- **COBIT Maturity Assessment** -> `chunks/07-outputs-and-cross-refs.md §Maturity output`.

## 7. Cross-References (summary)

Full maps in `chunks/07-outputs-and-cross-refs.md`. Quick links:

- `nist-800-53-rmf` — NIST 800-53 / RMF; COBIT APO13 maps to security controls.
- `coso-internal-controls` — COSO ICIF; COBIT extends COSO into IT domain.
- `aicpa-soc-reporting` — SOC 1/2/3; ITGC supports TSC criteria.
- `audit-workpapers` — AS 1215, AS 1105, sampling.

External: ISO 27001, NIST CSF 2.0, ITIL, ISO 38500, SOX, PCI DSS, HIPAA.

## 8. Worked Examples (summary)

Full worked examples in `use-cases/`. Each has complete input, procedure, expected output, and oracle.

| UC | Title | Industry | Key output |
|----|-------|----------|------------|
| UC-01 | SaaS COBIT 2019 maturity assessment | saas-technology | Maturity assessment, improvement roadmap |
| UC-02 | ITGC finding in 5-part observation format | financial-services, saas-technology | 5-part observation, severity classification |

## 9. Anti-Hallucination Disclaimers

- **ITAF numbering (S1-S18, G1-G18)** is a pedagogical reconstruction. It does NOT correspond to official ISACA ITAF numbering. Do not cite these as official identifiers.
- **Topic guidance areas (G19-G35 references)** are supplementary and NOT formal ITAF guidelines. Reference actual ISACA publication names.
- **CISA domain weights** (21/17/12/23/27%) are from the CISA CRM 28th Ed (2024). Verify against current publication.
- **COBIT 2019 objectives** (40 total) are as published; verify against the ISACA COBIT 2019 Framework.
- **Ethics principle count** — ISACA Code of Professional Ethics may list 7 or 8 principles depending on edition. Verify.
- **AI Audit Certificate** availability and name may change. Verify at ISACA.org.

> This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| CISA-CRM-28E | CISA Review Manual 28th Edition | ISACA | 28th Ed (2024) | 2026-05-25 | https://www.isaca.org/credentialing/cisa |
| COBIT-2019 | COBIT 2019 Framework: Introduction and Methodology | ISACA | 2019 | 2026-05-25 | https://www.isaca.org/resources/cobit |
| ITAF | IT Audit Framework, 4th Edition | ISACA | 4th Ed | 2026-05-25 | https://www.isaca.org/resources/itaf |
| ISACA-ETHICS | ISACA Code of Professional Ethics | ISACA | current edition | 2026-05-25 | https://www.isaca.org/credentialing/code-of-professional-ethics |
| COSO-2013 | Internal Control — Integrated Framework | COSO | 2013 | 2026-05-25 | https://www.coso.org |
| AICPA-TSC-2017 | Trust Services Criteria | AICPA | 2017 (TSP 100, 2022 revised POF) | 2026-05-25 | https://www.aicpa-cima.com/topic/audit-assurance/soc-2 |
| NIST-CSF-2.0 | Cybersecurity Framework | NIST | 2.0 (Feb 2024) | 2026-05-25 | https://www.nist.gov/cyberframework |
| ISO-27001-2022 | Information security management systems — Requirements | ISO/IEC | 2022 | 2026-05-25 | https://www.iso.org/standard/27001 |
| ISO-38500 | Governance of IT for the organization | ISO/IEC | 2024 | 2026-05-25 | https://www.iso.org/standard/38500 |
| ITIL | ITIL 4 Foundation | Axelos | 2019 | 2026-05-25 | https://www.axelos.com |
| NIST-SP-800-61 | Computer Security Incident Handling Guide | NIST | Rev 2 (2012) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/61/r2/final |

In-body citations use the form `[LABEL]` and resolve to this manifest.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| User intent | Load chunk(s) | Industry hint | Use case |
|-------------|---------------|---------------|----------|
| "ISACA overview" / "CISA domains" / "CISA certification" | `chunks/01-framework-and-cisa.md` | match industry | — |
| "COBIT 2019" / "COBIT objectives" / "governance objectives" / "focus area" | `chunks/02-cobit-2019.md` | match industry | UC-01 |
| "ITAF" / "audit standards" / "maturity assessment" / "COBIT maturity" | `chunks/03-itaf-and-maturity.md` | match industry | UC-01 |
| "ITGC" / "ITAC" / "general controls" / "application controls" / "sampling" | `chunks/04-itgc-itac.md` | match industry | UC-02 |
| "Risk assessment" / "audit plan" / "risk score" / "audit universe" | `chunks/05-risk-and-planning.md` | match industry | UC-02 |
| "Audit observation" / "5-part" / "audit lifecycle" | `chunks/06-observation-and-lifecycle.md` | match industry | UC-02 |
| "Audit report template" / "draft audit report" / "cross-reference" / "mapping to COSO/AICPA/NIST" | `chunks/07-outputs-and-cross-refs.md` | match industry | — |
| "Full COBIT maturity assessment for SaaS" | chunks/02, 03 | saas-technology | UC-01 |
| "ITGC testing engagement" | chunks/04, 05, 06 | financial-services | UC-02 |
| "CAIQ" / "SIG Lite" / "VSAQ" / "customer questionnaire" / "ITGC evidence reuse" / "COBIT governance evidence" | `chunks/08-questionnaire-reuse.md` | match industry | — |
| "High-level question" / "framework overview" | this SKILL.md only | — | — |

**Industries** (load matching file from `industries/`): financial-services, saas-technology, public-sector, other.

**Use cases** (load matching file from `use-cases/`): UC-01 (COBIT maturity for SaaS), UC-02 (5-part ITGC observation).

## 12. Operational Quick-Reference

The minimum cycle (always-loaded; no chunk needed for the high-level flow):

1. Review CISA domains and scope -> `chunks/01-framework-and-cisa.md`.
2. Apply COBIT 2019 governance objectives -> `chunks/02-cobit-2019.md`.
3. Apply ITAF standards and assess maturity -> `chunks/03-itaf-and-maturity.md`.
4. Test ITGC/ITAC -> `chunks/04-itgc-itac.md`.
5. Perform risk-based planning -> `chunks/05-risk-and-planning.md`.
6. Write observations and follow lifecycle -> `chunks/06-observation-and-lifecycle.md`.
7. Produce outputs and cross-reference -> `chunks/07-outputs-and-cross-refs.md`.

**Questionnaire reuse**: -> `chunks/08-questionnaire-reuse.md`. Map ITGC/COBIT evidence to CAIQ, SIG Lite, VSAQ.
**Board deck**: Use `aicpa-soc-reporting/assets/board_deck_template.md` for quarterly audit committee presentations.

For all engagements, maintain professional skepticism, apply the 5-part observation format, and verify evidence is sufficient, reliable, relevant, and useful.
