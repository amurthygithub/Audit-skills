---
name: audit-workpapers
description: "Create, organize, evaluate, and review audit workpapers per PCAOB AS 1215, AS 2315, AS 1105, and AS 3105, AICPA AU-C 230, ISA 230, COSO ICIF-2013, and ISACA ITAF. Use when asked to draft workpapers, design sampling plans (MUS/attribute/variables), document audit evidence, write findings in 5-part format, compute sample sizes or upper limits on misstatement, structure tickmark systems, perform audit risk model calculations, determine audit opinions, or build cross-reference tables, document material weaknesses, or prepare ICFR draft reports and management letters."
category: audit
risk: high
source: "PCAOB AS 1215, AS 1105, AS 3105, AS 2110, AS 2315, AS 2201; AICPA AU-C 230; ISA 230; COSO ICIF-2013; ISACA ITAF; arXiv:2604.06116; arXiv:2403.14069"
date_added: 2026-05-25
version: 0.2.0
status: draft
industries: [financial-services, public-sector, saas-technology, healthcare, other]
frameworks: [PCAOB-AS-1215, PCAOB-AS-1105, PCAOB-AS-3105, PCAOB-AS-2315, PCAOB-AS-2110, PCAOB-AS-2201, AICPA-AU-C-230, IAASB-ISA-230, COSO-ICIF-2013, ISACA-ITAF]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
token_baseline_target:
  input_p90: 14000
  output_p90: 4500
context_budget:
  always_loaded_tokens: 3000
  per_call_typical_tokens: 6000
  per_call_max_tokens: 15000
  per_call_p90_tokens: 8000
tags: [audit, workpapers, pcaob, aicpa, sampling, mus, attribute-sampling, audit-evidence, audit-risk, internal-control, coso, isaca, findings, quality-control, documentation, isa, board-deck, questionnaire-reuse, caic, sig-lite, vsaq]
---
You are an expert audit agent performing PCAOB / AICPA / ISA / ISACA-compliant audit workpaper work. Use official standards terminology exclusively.

# Audit Workpapers Skill (Router)

This SKILL.md is a *router*. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent. See section 11 Routing for the table.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Creating, organizing, indexing, or reviewing any audit workpaper
- Designing sampling plans (attribute, MUS/PPS, variables, non-statistical, dual-purpose)
- Documenting audit evidence, re-performance, or re-computation
- Writing audit findings in the 5-part C-C-C-E-R format
- Computing sample sizes, upper limits on misstatement, or projected misstatements
- Building tickmark legends, cross-reference tables, or lead schedules
- Performing audit risk model calculations (AR = IR x CR x AP x TD)
- Determining audit opinions (unqualified, qualified, adverse, disclaimer)
- Preparing engagement completion documents (per AS 1215.13)
- Ensuring compliance with PCAOB, AICPA, ISA, or ISACA documentation standards
- Evaluating electronic workpaper controls, retention, or sign-off protocols
- Integrating data analytics or ML-enhanced sampling into audit documentation
- Reusing audit workpaper evidence for customer security questionnaires (CAIQ, SIG Lite, VSAQ).
- Using the board-ready audit committee deck template (see aicpa-soc-reporting/assets/board_deck_template.md).

### Do NOT Use This Skill When:
- The task is purely tax preparation (different standards apply)
- The task is a forensic investigation outside an audit engagement
- The task involves advisory/consulting services with no audit documentation requirements
- The task is a SOC 1/SOC 2 examination (use SOC-specific skills instead)
- The user is asking about financial statement preparation (not an audit task)

## 2. Framework Overview

The audit workpapers skill encodes PCAOB, AICPA, IAASB (ISA), and ISACA documentation standards into a single executable playbook.

| Layer | Document | Role |
|-------|----------|------|
| Documentation | [PCAOB-AS-1215] / [AICPA-AU-C-230] / [IAASB-ISA-230] | Workpaper content, retention, review, completion |
| Evidence | [PCAOB-AS-1105] / AU-C 500 / ISA 500 | Evidence types, hierarchy, reliability, assertions |
| Sampling | [PCAOB-AS-2315] / AU-C 530 / ISA 530 | Statistical/nonstatistical, MUS, attribute, variables |
| Risk | AS 1101 / [PCAOB-AS-2110] / AS 2301 | Audit risk model (AR = IR x CR x AP x TD) |
| Opinion | [PCAOB-AS-3105] / AS 3101 | Unqualified, qualified, adverse, disclaimer |
| Internal Control | [PCAOB-AS-2201] / [COSO-ICIF-2013] | Material weakness, significant deficiency |
| IT Audit | [ISACA-ITAF] | IT-specific workpaper standards, CAATs |
| Quality | QC 1000 / AS 1220 / AS 1201 | Firm QC, EQR, supervisory review |

Regulatory updates (2024-2026): QC 1000 eff. Dec 2025; [PCAOB-AS-1215] amendments eff. Dec 2026; [PCAOB-AS-2315] amendment eff. Dec 2026; COSO 2026 GenAI guidance.

## 3. Core Concepts

### 3.1 Workpaper Indexing (A-N)
Every workpaper receives a unique alphanumeric index: A=Permanent File, B=Planning & Risk, C=Internal Control, D=Revenue, E=Expenditures, F=Assets, G=Liabilities, H=Equity, I=Sampling, J=Analytical Procedures, K=Completion, L=Communications, M=Quality Review, N=Specialty Areas. See `chunks/01-standards-and-structure.md`.

### 3.2 Three Mandatory Elements (AS 1215.04)
Purpose, source, conclusion. See `chunks/01-standards-and-structure.md` for 5W1H framework and experienced auditor standard.

### 3.3 Tickmark System
8 standard tickmarks. See `chunks/01-standards-and-structure.md`.

### 3.4 Evidence Hierarchy
External > internal. Written > oral. See `chunks/02-evidence-and-reperformance.md`.

### 3.5 Sampling Methods
Attribute, MUS/PPS, variables, non-statistical, dual-purpose. See `chunks/03-sampling.md`.

### 3.6 Audit Risk Model
AR = IR x CR x AP x TD. See `chunks/04-risk-and-opinion.md`.

### 3.7 Five-Part Finding Format
C-C-C-E-R (Condition, Criteria, Cause, Effect, Recommendation). See `chunks/05-finding-and-workflow.md`.

### 3.8 Substantive Analytical Procedures
Expectation modeling, tolerable difference, variance analysis. See `chunks/09-substantive-analytical-procedures.md`.

## 4. Decision Logic (summary)

Full logic in chunks. Quick-ref:
- Workpaper completeness -> chunks/01-standards-and-structure.md
- Sample method -> 100% > specific items > statistical vs non-stat > attribute/MUS/variables -> chunks/03-sampling.md
- MUS evaluation -> ULM = BP + Incremental Allowances -> chunks/03-sampling.md
- Risk model -> compute TD from IR, CR, AP -> chunks/04-risk-and-opinion.md
- Opinion -> scope limited? GAAP departure? material/pervasive? -> chunks/04-risk-and-opinion.md
- IPE gating -> classify source x purpose -> chunks/02-evidence-and-reperformance.md
- Analytical procedures -> build expectation, set tolerable difference, investigate variance -> chunks/09-substantive-analytical-procedures.md

## 5. Procedure Templates (summary)

- 7-step workflow -> chunks/05-finding-and-workflow.md
- Sampling plan -> chunks/03-sampling.md
- Re-performance / re-computation -> chunks/02-evidence-and-reperformance.md
- Quality checklist -> chunks/07-qc-compliance-cross-refs.md
- Substantive analytical procedure -> chunks/09-substantive-analytical-procedures.md

## 6. Output Templates (summary)

- Standard workpaper template -> chunks/06-outputs-electronic-review.md
- Sampling workpaper template -> chunks/06-outputs-electronic-review.md
- Finding documentation template -> chunks/06-outputs-electronic-review.md
- Engagement completion document -> chunks/06-outputs-electronic-review.md
- IPE validation log -> chunks/06-outputs-electronic-review.md
- Substantive analytical procedures workpaper template -> chunks/09-substantive-analytical-procedures.md

## 7. Cross-References (summary)

Internal: nist-800-53-rmf, isaca-audit-methodology, coso-internal-controls, aicpa-soc-reporting.
External crosswalks in chunks/07-qc-compliance-cross-refs.md.

## 8. Worked Examples (high-level)

Full worked examples in use-cases/.

| UC | Title | Industry | Key output |
|----|-------|----------|------------|
| UC-01 | MUS sampling workpaper for accounts receivable | financial-services | MUS plan, ULM, conclusion |
| UC-02 | 5-part finding for AP cutoff control gap | financial-services, public-sector | C-C-C-E-R finding, severity |
| UC-03 | Audit risk model TD calculation | financial-services | TD computed from IR, CR, AP |

## 9. Anti-Hallucination Disclaimers

- PCAOB standards reorganization — paragraph numbers may have shifted post-2024. Verify against current PCAOB publications.
- AS 1215 amendments (.09/.11) — effective Dec 15, 2026 per PCAOB Release No. 2024-005.
- Sample size tables — illustrative. Use statistical formulas or audit software for engagement-level precision.
- MUS worked examples — rounding differences up to $1 are immaterial.
- ML/sequential sampling — based on arXiv preprints; emerging methodologies. Validate against current professional standards.
- Opinion determination — requires professional judgment.

This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| PCAOB-AS-1215 | Audit Documentation | PCAOB | AS 1215 | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS1215 |
| PCAOB-AS-1105 | Audit Evidence | PCAOB | AS 1105 | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105 |
| PCAOB-AS-2315 | Audit Sampling | PCAOB | AS 2315 | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2315 |
| PCAOB-AS-3105 | Departures from Unqualified Opinions | PCAOB | AS 3105 | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS3105 |
| PCAOB-AS-2110 | Identifying and Assessing Risks | PCAOB | AS 2110 | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2110 |
| PCAOB-AS-2201 | Audit of ICFR | PCAOB | AS 2201 | 2026-05-25 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201 |
| AICPA-AU-C-230 | Audit Documentation | AICPA | AU-C 230 | 2026-05-25 | https://www.aicpa-cima.com |
| IAASB-ISA-230 | Audit Documentation | IAASB | ISA 230 | 2026-05-25 | https://www.iaasb.org |
| COSO-ICIF-2013 | Internal Control Integrated Framework | COSO | 2013 | 2026-05-25 | https://www.coso.org |
| ISACA-ITAF | IT Audit Framework | ISACA | ITAF 4th Ed. | 2026-05-25 | https://www.isaca.org |

In-body citations use the form [LABEL section] and resolve to this manifest.

## 11. Routing

| User intent | Load chunk(s) | Industry hint | Use case |
|-------------|---------------|---------------|----------|
| "Workpaper structure" / "indexing" / "tickmarks" / "AS 1215" / "sign-off" | chunks/01-standards-and-structure.md | match industry | - |
| "Evidence hierarchy" / "AS 1105" / "re-performance" / "IPE validation" / "recomputation" | chunks/02-evidence-and-reperformance.md | match industry | - |
| "Sampling plan" / "MUS" / "attribute sampling" / "variables" / "ULM" | chunks/03-sampling.md | match industry | UC-01 |
| "Audit risk model" / "AR = IR x CR" / "TD calculation" / "opinion" / "material weakness" | chunks/04-risk-and-opinion.md | match industry | UC-03 |
| "Audit finding" / "C-C-C-E-R" / "workflow" / "7-step" / "draft a report" | chunks/05-finding-and-workflow.md | match industry | UC-02 |
| "Workpaper templates" / "electronic workpapers" / "retention" / "review" | chunks/06-outputs-electronic-review.md | match industry | - |
| "Quality checklist" / "compliance" / "cross-reference" / "glossary" | chunks/07-qc-compliance-cross-refs.md | match industry | - |
| "Full audit engagement" | chunks/01,02,03,04,05,06,07 | financial-services | UC-01, UC-02 |
| "CAIQ" / "SIG Lite" / "VSAQ" / "customer questionnaire" / "workpaper evidence reuse" | chunks/08-questionnaire-reuse.md | match industry | - |
| "High-level question" | this SKILL.md only | - | - |

Industries (load matching file from industries/): financial-services, public-sector, saas-technology, healthcare, other.
Use cases (load matching file from use-cases/): UC-01 (MUS sampling AR), UC-02 (5-part finding), UC-03 (TD calculation).

## 12. Operational Quick-Reference

1. Structure the workpaper -> chunks/01-standards-and-structure.md
2. Document evidence -> chunks/02-evidence-and-reperformance.md
3. Design sampling -> chunks/03-sampling.md
4. Assess risk / opinion -> chunks/04-risk-and-opinion.md
5. Write findings -> chunks/05-finding-and-workflow.md
6. Use templates -> chunks/06-outputs-electronic-review.md
7. Validate quality -> chunks/07-qc-compliance-cross-refs.md
