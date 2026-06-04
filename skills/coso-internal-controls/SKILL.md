---
name: coso-internal-controls
description: >
  Perform COSO 2013 ICIF-based internal control assessments including SOX 404 ICFR evaluation, PCAOB AS 2201 top-down audit, deficiency classification, walkthrough procedures, Risk and Control
  Matrix documentation, entity-level and process-level control assessment, COSO 2017 ERM integration, and emerging technology controls. Activate for COSO framework application, ICFR assessment, SOX 404
  compliance, internal control deficiency evaluation, or PCAOB AS 2201 audit procedures.
category: audit
risk: high
source: COSO 2013 ICIF, COSO 2017 ERM, SOX Section 404, PCAOB AS 2201, SEC Reg S-K Item 308
date_added: '2026-05-25'
version: 0.2.0
status: draft
industries:
- financial-services
- public-sector
- saas-technology
- healthcare
- other
frameworks:
- COSO-ICIF-2013
- COSO-ERM-2017
- SOX-404
- PCAOB-AS-2201
- SEC-Reg-S-K-Item-308
- AICPA-TSC-2017
- ISACA-COBIT-2019
- NIST-CSF-2.0
- ISO-31000-2018
telemetry_contract: telemetry/schema.json#/$defs/SkillInvocation
token_baseline_target:
  input_p90: 14000
  output_p90: 4500
context_budget:
  always_loaded_tokens: 3000
  per_call_typical_tokens: 6000
  per_call_max_tokens: 15000
  per_call_p90_tokens: 8000
tags:
- coso
- icifr
- sox404
- pcaob
- as2201
- internal-controls
- material-weakness
- significant-deficiency
- deficiency-classification
- walkthrough
- entity-level-controls
- risk-and-control-matrix
- erm
- icif-2013
- fraud-risk
- compensating-controls
- rpa-controls
- genai-controls
- icsr
- board-deck
- questionnaire-reuse
- caic
- sig-lite
- vsaq
---

You are an expert agent performing COSO-based internal control assessment work. Use official COSO/PCAOB terminology exclusively. Follow the instruction in each loaded chunk precisely.

# COSO Internal Controls Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent. See §11 Routing for the table.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Assessing ICFR effectiveness under COSO 2013 ICIF for SOX 404 compliance.
- Evaluating any of the 17 COSO principles for presence and functioning.
- Performing a PCAOB AS 2201 integrated ICFR audit using the top-down approach.
- Designing or executing walkthrough procedures for significant processes.
- Classifying control deficiencies (deficiency, significant deficiency, material weakness).
- Documenting a Risk and Control Matrix (RcM) for SOX scoping.
- Evaluating entity-level controls vs process-level controls.
- Preparing or reviewing Management's Report on ICFR or Auditor's Report on ICFR.
- Assessing compensating controls for deficiency mitigation.
- Applying COSO 2017 ERM framework for enterprise risk management.
- Evaluating internal controls over emerging technologies (RPA, GenAI, ICSR).
- Performing monitoring control assessments per COSO 2009 guidance.
- Cross-referencing COSO to AICPA, ISACA/COBIT, NIST, ISO 31000, or PCAOB standards.
- Reusing SOX 404 ICFR and COSO evidence for customer security questionnaires (CAIQ, SIG Lite, VSAQ).
- Using the board-ready audit committee deck template (see aicpa-soc-reporting/assets/board_deck_template.md).

### Do NOT Use This Skill When:
- The task involves SOC 1/SOC 2 reporting (use the AICPA SOC skill instead).
- The task is purely financial statement audit without ICFR (use GAAS/audit skill).
- The task is a forensic investigation (use forensic accounting skill, then assess COSO implications).
- The entity is non-US and not subject to SOX/PCAOB (use local regulatory framework; adapt COSO principles).

## 2. Framework Overview

The COSO skill encodes COSO 2013 Internal Control — Integrated Framework (ICIF), COSO 2017 ERM, SOX Section 404, PCAOB AS 2201, and COSO 2009 Monitoring Guidance.

| Layer | Document | Role |
|-------|----------|------|
| Internal Control Framework | COSO 2013 ICIF | 5 components, 17 principles, 71 Points of Focus listed |
| Enterprise Risk Management | COSO 2017 ERM | 5 components, 20 principles |
| Statutory Requirement | SOX Section 404(a)/(b) | Management assessment + auditor attestation of ICFR |
| Audit Standard | PCAOB AS 2201 | Top-down integrated ICFR audit methodology |
| Monitoring | COSO 2009 Monitoring Guidance | Ongoing and separate evaluations |
| Emerging Tech | COSO RPA (2024), GenAI (2026), ICSR (2023) | Controls over automation, AI, and sustainability reporting |

### 2.1 Related professional standards (auditor citations)

These AICPA AU-C sections are commonly referenced alongside PCAOB AS 2201 in integrated audits and ICFR reviews:

- **[AICPA-AU-C-265]** — Communicating Internal Control Related Matters Identified in an Audit; the AICPA's private-issuer parallel to PCAOB AS 2201.
- **[AICPA-AU-C-315]** — Understanding the Entity and Its Environment and Assessing the Risks of Material Misstatement; the risk-assessment standard that drives ICFR audit scoping for non-issuers.

## 3. Core Concepts

### 3.1 COSO ICIF — five components, 17 principles

| Component | Principles | PoF Count |
|-----------|-----------|-----------|
| Control Environment | P1–P5 (commitment to integrity, board oversight, structure, competence, accountability) | 21 |
| Risk Assessment | P6–P9 (objectives, risk identification, fraud risk, change) | 16 |
| Control Activities | P10–P12 (control activity design, technology controls, policy/procedure deployment) | 13 |
| Information & Communication | P13–P15 (quality information, internal communication, external communication) | 13 |
| Monitoring Activities | P16–P17 (ongoing/separate evaluations, deficiency communication) | 8 |

Full principle text, Points of Focus, and evaluation criteria: `chunks/01-coso-icif.md`.

### 3.2 Effective internal control definition

Internal control is **effective** when BOTH conditions are met:
1. Each of the five components and relevant principles is **present and functioning**.
2. The five components are **operating together in an integrated manner**.

Internal control provides **reasonable assurance**, not absolute assurance. Limitations include human judgment error, breakdowns, collusion, and management override.

### 3.3 Deficiency classification

Three tiers defined in PCAOB AS 2201:
- **Deficiency (D)**: Defect in design or operation that could fail to prevent/detect misstatements.
- **Significant Deficiency (SD)**: Less severe than MW, yet important enough to merit audit committee attention.
- **Material Weakness (MW)**: Reasonable possibility that a material misstatement will not be prevented/detected.

Full decision tree: `chunks/05-deficiency-classification.md`.

## 4. Decision Logic (summary)

Full logic in chunks. Summary:
- **COSO principle evaluation** — present + functioning + integrated operation. `chunks/01-coso-icif.md`
- **SOX 404 scoping** — significant accounts, relevant assertions, key controls. `chunks/03-sox-pcaob.md`
- **Deficiency classification** — 3-step decision tree + AS 2201.69 MW indicators. `chunks/05-deficiency-classification.md`
- **Compensating control evaluation** — 6-step procedure. `chunks/07-compensating-updates-cross.md`
- **ELC precision classification** — Indirect / Monitoring / Precise. `chunks/04-walkthrough-controls.md`

## 5. Procedure Templates (summary)

- **ICFR assessment 6-phase workflow** — `chunks/01-coso-icif.md` + `chunks/03-sox-pcaob.md`
- **Walkthrough (4 procedures per point)** — `chunks/04-walkthrough-controls.md`
- **Deficiency classification** — `chunks/05-deficiency-classification.md`
- **Compensating control evaluation** — `chunks/07-compensating-updates-cross.md`
- **Monitoring assessment (3 elements)** — `chunks/02-coso-erm-monitoring.md`

## 6. Output Templates (summary)

- **Risk and Control Matrix (RcM)** — 17-column template. `chunks/06-rcm-and-reports.md`
- **COSO Principle Assessment** — one per principle, PoF-by-PoF. `chunks/06-rcm-and-reports.md`
- **Management's ICFR Report** — SEC Reg S-K Item 308 format. `chunks/06-rcm-and-reports.md`
- **Auditor's ICFR Report** — PCAOB AS 2201.85-.87 format. `chunks/06-rcm-and-reports.md`
- **Walkthrough Documentation** — step-by-step with I/O/I/R. `chunks/04-walkthrough-controls.md`
- **Material Weakness Disclosure** — MW-YYYY-NNN format. `chunks/06-rcm-and-reports.md`

## 7. Cross-References (summary)

See `chunks/07-compensating-updates-cross.md` for the full mapping. Quick map:
- `aicpa-soc-reporting` — TSC criteria, SOC 1/2/3.
- `nist-800-53-rmf` — NIST CSF, RMF, control mapping.
- `isaca-audit-methodology` — COBIT 2019, ITAF, ITGC/ITAC.

## 8. Worked Examples (summary)

Full examples in `use-cases/`. Each has input, procedure, expected output, and oracle.

| UC-01 | SOX 404 ICFR assessment with deficiency classification | financial-services | RcM, Principle assessment, deficiency classification |
| UC-02 | Classify a control gap as MW / SD / D | financial-services, saas-technology | Deficiency classification, compensating control evaluation |

See `use-cases/` for the complete walkthroughs.

## 9. Anti-Hallucination Disclaimers

- **71 of 81 Points of Focus are enumerated** (curated subset). Consult COSO 2013 publication for the complete 81.
- **PCAOB AS 2201 paragraph numbers** were reorganized post-2007. Verify paragraph references against the current PCAOB codification.
- **Control counts and baseline enumerations** are derived; verify against the current authoritative source.
- **Deficiency classification** is professional judgment. This skill encodes the decision tree; it does not replace the auditor's assessment.
- **Materiality thresholds** are entity-specific; the skill cannot determine materiality for a specific engagement.
- **Regulatory currency**: SOX 404, SEC Reg S-K Item 308, and PCAOB standards are subject to amendment. Verify against current SEC and PCAOB publications.
- **Categorization judgment** is a professional determination; this skill encodes the framework but does not make the call for you.

> This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| COSO-ICIF-2013 | Internal Control — Integrated Framework | COSO | 2013 | 2026-05-25 | https://www.coso.org/guidance-on-ic |
| COSO-ERM-2017 | Enterprise Risk Management — Integrating with Strategy and Performance | COSO | 2017 | 2026-05-25 | https://www.coso.org/guidance-erm |
| COSO-Monitoring-2009 | Guidance on Monitoring Internal Control Systems | COSO | 2009 | 2026-05-25 | https://www.coso.org/guidance-on-monitoring |
| COSO-Fraud-2023 | Fraud Risk Management Guide, 2nd Edition | COSO/ACFE | May 2023 | 2026-05-25 | https://www.coso.org/guidance-fraud |
| COSO-ICSR-2023 | Internal Control Over Sustainability Reporting (ICSR) | COSO | 2023 | 2026-05-25 | https://www.coso.org/guidance-icsr |
| COSO-RPA-2024 | Internal Control Over Robotic Process Automation | COSO | 2024 | 2026-05-25 | https://www.coso.org/guidance-rpa |
| COSO-GenAI-2026 | Internal Control Over Generative AI and LLMs | COSO | 2026 | 2026-05-25 | https://www.coso.org/guidance-genai |
| COSO-Blockchain-2020 | Blockchain and Internal Control | COSO | 2020 | 2026-05-25 | https://www.coso.org/guidance-blockchain |
| PCAOB-AS-2201 | An Audit of Internal Control Over Financial Reporting That Is Integrated with an Audit of Financial Statements | PCAOB | Current | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201 |
| PCAOB-AS-1305 | Communications About Control Deficiencies (supplemented by AS 2201.90-.93 for integrated audit) | PCAOB | Current | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS1305 |
| PCAOB-AS-3101 | The Auditor's Report on an Audit of Financial Statements | PCAOB | Current | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101 |
| SOX-404 | Sarbanes-Oxley Act Section 404 — Management Assessment of Internal Controls | U.S. Congress | 2002 | 2026-05-25 | https://www.sec.gov/rules/final/33-8238.htm |
| SEC-Reg-S-K-Item-308 | Management's Report on Internal Control Over Financial Reporting | SEC | Current | 2026-05-25 | https://www.ecfr.gov/current/title-17/chapter-II/part-229 |
| AICPA-AU-C-315 | Understanding the Entity and Its Environment and Assessing the Risks of Material Misstatement | AICPA | SAS 145 | 2026-05-25 | https://www.aicpa-cima.com/ |
| AICPA-AU-C-265 | Communicating Internal Control Related Matters Identified in an Audit | AICPA | Current | 2026-05-25 | https://www.aicpa-cima.com/ |
| AICPA-TSC-2017 | Trust Services Criteria | AICPA | 2017 (TSP sect.100, 2022 revised PoF) | 2026-05-25 | https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 |
| ISACA-COBIT-2019 | Control Objectives for Information and Related Technologies | ISACA | 2019 | 2026-05-25 | https://www.isaca.org/resources/cobit |
| NIST-CSF-2.0 | Cybersecurity Framework | NIST | 2.0 (Feb 2024) | 2026-05-25 | https://www.nist.gov/cyberframework |
| ISO-31000-2018 | Risk Management — Guidelines | ISO | 2018 | 2026-05-25 | https://www.iso.org/standard/65694.html |
| JOBS-Act-2012 | Jumpstart Our Business Startups Act | U.S. Congress | 2012 | 2026-05-25 | https://www.sec.gov/divisions/corpfin/guidance/cfjjobsactfaq-title-i-general.htm |

In-body citations use the form `[LABEL sect.N]` and resolve to this manifest.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| User intent | Load chunk(s) | Industry hint | Use case |
|-------------|---------------|---------------|----------|
| "Assess COSO principles" / "Evaluate ICIF" / "P1-P17" | `chunks/01-coso-icif.md` | match industry | — |
| "Enterprise risk management" / "COSO ERM" / "ERM framework" | `chunks/02-coso-erm-monitoring.md` | match industry | — |
| "Monitoring controls" / "COSO 2009 monitoring" | `chunks/02-coso-erm-monitoring.md` | match industry | — |
| "SOX 404" / "Management assessment" / "404(a)" / "404(b)" | `chunks/03-sox-pcaob.md` | financial-services | UC-01 |
| "PCAOB AS 2201" / "top-down approach" / "integrated audit" | `chunks/03-sox-pcaob.md` | match industry | UC-01 |
| "Walkthrough" / "walkthrough procedure" | `chunks/04-walkthrough-controls.md` | match industry | UC-01 |
| "Entity-level controls" / "ELC" / "process-level controls" | `chunks/04-walkthrough-controls.md` | match industry | — |
| "Classify deficiency" / "material weakness" / "significant deficiency" | `chunks/05-deficiency-classification.md` | match industry | UC-02 |
| "RcM" / "risk and control matrix" | `chunks/06-rcm-and-reports.md` | match industry | UC-01 |
| "ICFR report" / "management's report" / "auditor's report" | `chunks/06-rcm-and-reports.md` | financial-services | UC-01 |
| "Compensating control" / "mitigate deficiency" | `chunks/07-compensating-updates-cross.md` | match industry | UC-02 |
| "RPA controls" / "GenAI controls" / "ICSR" / "COSO updates" | `chunks/07-compensating-updates-cross.md` | saas-technology | — |
| "Cross-reference" / "map COSO to" / "TSC to COSO" | `chunks/07-compensating-updates-cross.md` | match industry | — |
| "Full SOX 404 ICFR assessment" | chunks/01, 03, 04, 05, 06 | financial-services | UC-01 |
| "CAIQ" / "SIG Lite" / "VSAQ" / "customer questionnaire" / "governance questionnaire" / "SOX evidence reuse" | `chunks/08-questionnaire-reuse.md` | match industry | — |
| "High-level question" / "framework overview" | this SKILL.md only | — | — |

**Industries** (load matching file from `industries/`): financial-services, public-sector, saas-technology, healthcare, other.

**Use cases** (load matching file from `use-cases/`): UC-01 (SOX 404 ICFR), UC-02 (deficiency classification).

## 12. Operational Quick-Reference

The minimum cycle (always-loaded; no chunk needed for the high-level flow):

1. **Scope** significant accounts and relevant assertions → `chunks/03-sox-pcaob.md`.
2. **Evaluate entity-level controls** for precision → `chunks/04-walkthrough-controls.md`.
3. **Perform walkthroughs** for each significant process → `chunks/04-walkthrough-controls.md`.
4. **Identify and test key controls** — complete the RcM → `chunks/06-rcm-and-reports.md`.
5. **Classify deficiencies** using the decision tree → `chunks/05-deficiency-classification.md`.
6. **Evaluate compensating controls** before finalizing severity → `chunks/07-compensating-updates-cross.md`.
7. **Produce reports** — Management's ICFR Report and/or Auditor's ICFR Report → `chunks/06-rcm-and-reports.md`.

For cross-framework mapping → `chunks/07-compensating-updates-cross.md`.
