---
chunk_id: 07-qc-compliance-cross-refs
parent_skill: audit-workpapers
topic: "Quality Checklist, Compliance Validation Rules, Cross-Reference Tables, Glossary, Data Analytics Trends"
load_when: "user asks about quality checklist, compliance rules, cross-reference tables, glossary, or data analytics"
---

# Chunk 07 — Quality, Compliance, Cross-Refs

## Quality Checklist

### Pre-Engagement
Engagement acceptance evaluated per QC 1000. Independence confirmed. Engagement letter signed. Prior-year WPs reviewed.

### During Engagement
All WPs have purpose/source/conclusion (AS 1215.04). All WPs satisfy experienced auditor standard (AS 1215.06A). All 5W1H elements present. Preparer/reviewer sign-offs. Evidence sufficiency evaluated. Sampling adequacy verified. Tickmarks defined. Cross-referencing bidirectional. Risk-to-response linkage documented. All assertions addressed. Contradictory information documented (AS 1215.08).

### Completion
All findings in 5-part format. Uncorrected misstatements evaluated. Engagement completion document prepared (AS 1215.13). All 8 significant finding categories addressed (AS 1215.12). Management representation letter obtained. Subsequent events evaluated. Opinion determination documented. CAMs identified if applicable.

### Post-Engagement
Documentation completion within 14 days (AS 1215.14-.15). 7-year retention plan. No documentation deleted after completion (AS 1215.17). All review notes resolved. Post-completion additions documented: date, person, reason (AS 1215.16).

## Compliance Validation Rules

1. All WPs: purpose, source, conclusion, preparer, reviewer, dates.
2. All sampling WPs: objective, population, method, sample size rationale, selection, results, evaluation, conclusion.
3. All findings: 5-part C-C-C-E-R format.
4. Evidence assessed for relevance AND reliability (AS 1105.05-.08).
5. No documentation deleted after completion date (AS 1215.17).
6. Post-completion additions identify: date, person, reason (AS 1215.16).
7. Oral evidence alone insufficient for experienced auditor standard (AS 1215.06).
8. Inquiry alone never sufficient (AS 1105.17).
9. Uncorrected misstatements evaluated against tolerable misstatement.
10. Documentation completion within 14 days of report release (AS 1215.15).
11. All significant findings documented per AS 1215.12 (8 categories).
12. Engagement partner review complete before report release (AS 1215.15).
13. Cross-referencing bidirectional.


## Deficiency Severity: Cross-Framework Reconciliation (Master Table)

Each framework uses a different severity tier system. The table below reconciles them for cross-framework assessments.

| COSO/PCAOB (3-Tier) | ISACA (4-Tier) | NIST 800-53 / RMF (4-Tier) | ISACA Risk Priority | Definition |
|----------------------|----------------|----------------------------|---------------------|------------|
| Control Deficiency (Other) | Low | Low | Low (score 1-4) | Does not rise to SD or MW; minor gap or enhancement opportunity |
| Significant Deficiency | Medium | Moderate | Medium (5-9) | Important enough to merit attention by those charged with governance |
| Material Weakness | High | High | High (10-14) | Reasonable possibility of material misstatement not prevented/detected |
| -- (no equivalent) | Critical | Critical | Critical (>=15) | Systemic failure, existential risk beyond material financial impact |

**Mapping notes:**
- COSO/PCAOB uses a 3-tier scale defined in AS 2201. ISACA and NIST both add a fourth tier above COSO's highest.
- In COSO assessments, ISACA/ISACA "Catastrophic" and NIST "Critical" still map to Material Weakness but warrant escalated remediation priority.
- For PCAOB-governed audits, use PCAOB/COSO classifications directly.
- NIST severity uses assessment objective determinations: Satisfied (no finding), Other_than_Satisfied (finding), with NIST SP 800-53A Rev 5 mapping Low/Moderate/High/Critical to the tiers above.
- See: `coso-internal-controls/chunks/07-compensating-updates-cross.md` (COSO cross-ref), `isaca-audit-methodology/chunks/05-risk-and-planning.md` (ISACA severity), `nist-800-53-rmf/chunks/05-assess.md` (NIST assessment).


## Cross-Skill Citation Label Note

Each skill in the audit family maintains its own citation manifest (Section 10 of each SKILL.md). Citation labels are skill-local: labels resolve to the manifest in the skill where they appear.

| Skill | Label Example | Resolves To |
|-------|--------------|-------------|
| aicpa-soc-reporting | AICPA-TSC-2017 | AICPA TSP Section 100 |
| audit-workpapers | PCAOB-AS-1215 | PCAOB Audit Documentation |
| coso-internal-controls | AICPA-TSC-2017 | AICPA TSP Section 100 |
| isaca-audit-methodology | AICPA-TSC-2017 | AICPA TSP Section 100 |
| nist-800-53-rmf | SOC-2-TSC-2017 | AICPA Trust Services Criteria |

**Important:** While the underlying authoritative sources are the same, the citation label format used within each skill may differ (e.g., AICPA skill uses `AICPA-TSC-2017`, NIST skill uses `SOC-2-TSC-2017`). When cross-referencing between skills, resolve the citation label within the referencing skill's own manifest. Do not assume label compatibility across skills.

When a cross-skill chunk references standards from another skill (e.g., "See `aicpa-soc-reporting/chunks/06-cuec-csoc-inheritance.md` for CUEC details"), the referenced skill's own citation labels and manifest apply. No global label registry exists; each skill is self-contained.

## Cross-Reference Tables

### AICPA-PCAOB Crosswalk

| AICPA (AU-C) | PCAOB (AS) | Topic |
|--------------|-----------|-------|
| AU-C 230 | AS 1215 | Audit Documentation |
| AU-C 500 | AS 1105 | Audit Evidence |
| AU-C 530 | AS 2315 | Audit Sampling |
| AU-C 450 | AS 2810 | Evaluating Audit Results |
| AU-C 700 | AS 3101 | Opinion Reporting |
| AU-C 705 | AS 3105 | Modified Opinions |

### ISACA-AICPA/PCAOB Crosswalk

| ISACA (ITAF) | AICPA/PCAOB | Key Differences |
|--------------|------------|-----------------|
| ITAF Planning | AU-C 315 / AS 2110 | ITAF adds IT-specific risk factors |
| ITAF Execution | AU-C 330 / AS 2301 | ITAF includes CAAT/IT test procedures |
| ITAF Reporting | AU-C 700 / AS 3101 | ITAF includes IT-specific findings format |

### COSO-Workpaper Integration

| COSO Component | Principles | Workpaper Documentation |
|----------------|-----------|------------------------|
| Control Environment | 1-5 | Tone at top, org structure, competence (C-1 series) |
| Risk Assessment | 6-9 | Entity/activity risks, fraud risk (C-2 series) |
| Control Activities | 10-12 | Policies, IT controls, SOD (C-3 series) |
| Information & Communication | 13-15 | Financial reporting info (C-4 series) |
| Monitoring | 16-17 | Ongoing/periodic, deficiency communication (C-5 series) |

### ISA-PCAOB Crosswalk

| ISA | PCAOB AS | Notes |
|-----|---------|-------|
| ISA 230 | AS 1215 | ISA more principle-based |
| ISA 500 | AS 1105 | Similar evidence hierarchy |
| ISA 530 | AS 2315 | ISA adds PPS guidance |
| ISA 700 | AS 3101 | Key Audit Matters vs CAMs |
| ISA 705 | AS 3105 | Aligned on opinion types |

## Data Analytics in Audit (2024-2026 Trends)

Full-population testing: test 100% as complement to sampling; sampling risk zero for tested population; nonsampling risk remains (AS 2315.11).

ML-based risk scoring: targeted sampling via risk scores; results cannot be projected unless combined with random selection.

Continuous auditing: automated procedures at regular intervals.
Automated anomaly detection: autoencoder-based approaches; NLP for contract/transaction analysis.
RPA for evidence gathering: routine evidence collection automation.
COSO 2026 GenAI guidance: controls over AI-generated outputs.



## Use Case: CUEC Evaluation for Government Procurement (RFP/RFQ)

When evaluating a service organization's SOC 2 report in the context of government procurement (RFP, RFQ, or contract award), apply the following additional review steps beyond standard CUEC evaluation:

### 1. Evidence of Review Date
Document the date the SOC 2 report was reviewed. Government procurement files often require auditable evidence of when the evaluation occurred. Record: reviewer name/title, review date, report period covered, report issuance date.

### 2. Vendor Report Mapping to RFP Security Requirements
Map each relevant TSC criterion (in-scope categories: Security, Availability, Processing Integrity, Confidentiality, Privacy) to specific RFP/RFQ security requirements. Document gaps where the SOC 2 scope does not cover an RFP requirement. Example: If RFP requires FIPS 140-2 validated encryption and SOC 2 only asserts AES-256, flag the delta.

### 3. Residual Risk Acknowledgment
For each CUEC the procuring agency (user entity) is expected to implement, document whether the agency currently has the CUEC in place. If not, document the residual risk and the compensating controls the agency will implement. Obtain sign-off from the agency's Authorizing Official or CIO.

### 4. Annual Re-Evaluation
Government procurement contracts typically span multiple years. Schedule annual re-evaluation of the vendor SOC 2 report (if Type II covers the period) or re-request bridge letters for gap periods. Document the re-evaluation cycle in the contract file.

### 5. Subservice Organization Review
If the vendor uses carve-out subservice organizations (IaaS, CDN, payment processor), review those subservice organizations' SOC reports separately and map their TSC coverage to the RFP requirements.

This use case extends the CUEC evaluation in `aicpa-soc-reporting/chunks/06-cuec-csoc-inheritance.md` with procurement-specific documentation requirements.

## Key Terminology

| Term | Definition | Source |
|------|-----------|--------|
| Audit Documentation | Written record of basis for auditor's conclusions | AS 1215.02 |
| Experienced Auditor | Auditor with reasonable understanding of audit activities | AS 1215.06A |
| Documentation Completion Date | Within 14 days after report release | AS 1215.15 |
| Engagement Completion Document | Document identifying all significant findings | AS 1215.13 |
| Sampling Risk | Risk auditor's conclusion differs from population conclusion | AS 2315.10 |
| Nonsampling Risk | All audit risk not due to sampling | AS 2315.11 |
| Material Weakness | Reasonable possibility material misstatement not prevented/detected | AS 2201 |
| Significant Deficiency | Less severe than MW but important enough to merit attention by those charged with governance | AS 2201 Appendix A, AS 2201.62-.70 |
| Critical Audit Matter | Especially challenging, subjective, or complex judgment | AS 3101 |
| EQR | Quality review by qualified reviewer not on engagement team | AS 1220 |
| ULM | Upper Limit on Misstatement = BP + sum of incremental allowances | AICPA Audit Guide |
| Tainting Percentage | Misstatement relative to book value; used in MUS evaluation | AICPA Audit Guide |
