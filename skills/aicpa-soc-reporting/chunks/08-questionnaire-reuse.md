---
chunk_id: 08-questionnaire-reuse
parent_skill: aicpa-soc-reporting
topic: "Questionnaire Evidence Reuse (CAIQ / SIG Lite / VSAQ / Customer Security Questionnaires)"
load_when: "user asks to map SOC 2 / SOC 1 / SOC for Cybersecurity evidence to CAIQ, SIG Lite, VSAQ, or customer security questionnaires"
---

# SOC Evidence Reuse for Customer Security Questionnaires

SOC 2 Type II reports are the single highest-leverage evidence artifact for customer questionnaires. A well-structured SOC 2 report answers 60-80% of CAIQ, SIG Lite, and VSAQ fields before any additional work begins. This chunk explains how to reuse SOC evidence systematically.

## Mapping Table: SOC 2 TSC -> CAIQ / SIG Lite / VSAQ

| SOC 2 TSC | CAIQ v4 Section(s) | SIG Lite Domain(s) | VSAQ Module | Key Fields Answered |
|-----------|-------------------|--------------------|--------------------|----------------------|
| CC1.1-CC1.5 (Control Environment) | Governance & Risk Mgmt (GRM) | Org Security, Governance | Section 1: Security Org | Board oversight, ethics policy, org structure |
| CC2.1-CC2.3 (Communication) | GRM, Human Resources (HRS) | Governance, HR Security | Section 1 | Internal communication, whistleblower |
| CC3.1-CC3.4 (Risk Assessment) | Risk Management (RSK) | Risk Management | Section 1, 3 | Risk methodology, risk register, fraud risk |
| CC4.1-CC4.2 (Monitoring) | Audit & Compliance (AAC) | Compliance, Monitoring | Section 1 | Internal audit, monitoring frequency |
| CC5.1-CC5.3 (Control Activities) | GRM, Change Mgmt (CHM) | Control Environment | Section 1, 5 | Control design, policy deployment |
| CC6.1-CC6.8 (Logical & Physical Access) | IAM, Data Security (DCS) | Access Control, Physical Security | Section 2, 7 | MFA, SSO, provisioning, access review |
| CC7.1-CC7.5 (System Operations) | CHM, Threat & Vuln Mgmt (TVM) | Ops Mgmt, Vuln Mgmt | Section 4, 6 | Change mgmt, vuln scanning, patch mgmt |
| CC8.1-CC8.2 (Change Management) | CHM, Secure Development (SDE) | Change Mgmt, SDLC | Section 5, 8 | SDLC controls, change approval, testing |
| CC9.1-CC9.2 (Risk Mitigation) | BCP (BCR), Incident Response (IRM) | BCP/DR, Incident Response | Section 6, 9 | BCP/DR testing, IR plan |
| A1.1-A1.3 (Availability) | BCR, Supply Chain (SCM) | BCP/DR, Service Delivery | Section 6 | SLA monitoring, capacity, redundancy |
| C1.1-C1.2 (Confidentiality) | DCS, Encryption (EKM) | Data Security, Encryption | Section 2, 3 | Encryption at rest/transit, classification |
| PI1.1-PI1.5 (Processing Integrity) | SDE, CHM | Data Quality | Section 8 | Input validation, error handling |
| P1.1-P8.1 (Privacy) | Data Privacy (DPR), DCS | Privacy, 3rd-Party Mgmt | Section 3 | Privacy notice, consent, data rights |

## Evidence Reuse Strategy

### Step 1: Pre-map SOC Report
- Extract SOC 2 Section IV test procedures and results.
- Map each to CAIQ Control IDs (CIDs), SIG Lite questions, VSAQ fields.
- Store in a centralized evidence library (GRC platform or spreadsheet).
- Target: 80%+ of CAIQ v4 CIDs pre-answered from SOC 2 alone.

### Step 2: Triage Inbound Questionnaires
- Categorize: CAIQ / SIG Lite / SIG Core / VSAQ / custom.
- Score completeness: % of fields matching pre-mapped SOC evidence.
- Flag gaps for manual completion (typically 10-20% of fields).

### Step 3: Maintain a Reuse Registry
- Track SOC 2 test procedure -> questionnaire field mappings.
- Update when SOC report is refreshed (annual Type II cycle).
- Version-lock mapping to report period.
- Backfill when new controls enter scope.

## Questionnaire-Specific Tips

- **CAIQ**: Reference SOC 2 Type II Section IV test descriptions. Assessors often accept "Covered by SOC 2 Type II" when the procedure is directly relevant.
- **SIG Lite/SIG Core**: Maps naturally to TSC categories per the table above.
- **VSAQ**: SOC 2 Type II answers ~70% of VSAQ fields (focus on Sections 1, 2, 6).
- **Custom questionnaires**: Build a "response library" of SOC-2-derived narratives for the top 50 control questions.
- **Bridge letters**: Combine chunk 05 bridge letter with the most recent SOC report for gap-period questionnaires.

## Cross-Reference to Other Skills

- `nist-800-53-rmf` -- FedRAMP authorization package answers CAIQ/SIG with greater depth (see its chunk 08).
- `coso-internal-controls` -- SOX 404 ICFR evidence maps to governance questionnaires.
- `isaca-audit-methodology` -- ITGC results answer Change Mgmt and Access Control sections.
- `audit-workpapers` -- Sampling workpapers provide statistical backing for questionnaire responses.

## When to Load This Chunk

Load when the user asks about CAIQ, SIG, VSAQ, security questionnaires, customer audit fatigue, questionnaire reuse, evidence library, or mapping SOC to vendor assessments.
