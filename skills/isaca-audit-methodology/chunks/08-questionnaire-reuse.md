---
chunk_id: 08-questionnaire-reuse
parent_skill: isaca-audit-methodology
topic: "Questionnaire Evidence Reuse (CAIQ / SIG Lite / VSAQ / Customer Security Questionnaires)"
load_when: "user asks to map ISACA COBIT 2019 / ITGC / ITAC evidence to CAIQ, SIG Lite, VSAQ, or customer security questionnaires"
---

# ISACA / COBIT Evidence Reuse for Customer Security Questionnaires

ISACA methodology and COBIT 2019 governance assessments produce evidence that directly answers the governance, risk management, change management, and operations sections of customer security questionnaires. ITGC and ITAC test results are especially valuable -- they provide independently tested evidence that static questionnaire responses lack. This chunk explains how to repurpose ISACA audit work for questionnaire reuse.

## Mapping Table: COBIT 2019 / ITGC -> CAIQ / SIG Lite / VSAQ

| ISACA / COBIT Domain | CAIQ v4 Section(s) | SIG Lite Domain(s) | VSAQ Module | Key Fields Answered |
|----------------------|--------------------|--------------------|--------------------|----------------------|
| EDM (Governance) | GRM | Governance | Section 1 | IT governance, board oversight, value delivery |
| APO (Align/Plan/Organize) | GRM, RSK, HRS | Governance, Risk Mgmt | Section 1 | IT strategy, risk management, HR security |
| BAI (Build/Acquire/Implement) | SDE, CHM | SDLC, Change Mgmt | Section 5, 8 | Secure development, change management, testing |
| DSS (Deliver/Service/Support) | IAM, TVM, BCR, IRM | Ops Mgmt, Access Ctrl, BCP/DR | Section 2, 4, 6, 9 | Access mgmt, vuln mgmt, BCP/DR, incident response |
| MEA (Monitor/Evaluate/Assess) | AAC | Compliance, Monitoring | Section 1 | Internal audit, monitoring, compliance |
| ITGC - Access Controls | IAM, DCS | Access Control | Section 2, 7 | Access provisioning, recertification, privileged access |
| ITGC - Change Management | CHM | Change Management | Section 5 | Change approval, CAB, emergency changes |
| ITGC - IT Operations | TVM, BCR | Operations, BCP/DR | Section 4, 6 | Monitoring, backup, job scheduling |
| ITGC - SDLC | SDE | SDLC | Section 8 | Secure coding, code review, testing |
| ITAC - Input/Processing/Output | SDE, DCS | Data Quality | Section 8 | Input validation, processing integrity |
| ITAC - Data Integrity | DCS | Data Integrity | Section 3, 8 | Reconciliation, balancing, error handling |
| Risk Scoring (L x I x CRF) | RSK | Risk Management | Section 1, 3 | Risk quantification, prioritization |
| 5-Part Observation | AAC | Compliance | Section 1 | Finding documentation, remediation tracking |
| COBIT Maturity Assessment | GRM | Governance | Section 1 | Capability levels, improvement roadmap |

## Evidence Reuse Strategy

### Step 1: Extract ITGC Test Results
- ITGC testing produces quantitative evidence: sample sizes, deviation rates, and conclusions.
- This is higher-quality evidence than self-attested questionnaire responses.
- Map ITGC categories (Access, Change, Ops, SDLC) to CAIQ sections directly.

### Step 2: Package COBIT Maturity as Governance Evidence
- COBIT maturity assessments (0-5 scale per process) provide structured governance evidence.
- A process at maturity 3 (Defined) or higher demonstrates mature governance to questionnaire reviewers.
- Include the maturity assessment summary as an appendix to questionnaire responses.

### Step 3: Use 5-Part Observations for Transparency
- When disclosing findings in questionnaires, use the ISACA 5-part format (C-C-C-E-R).
- This format is instantly recognizable to auditors and builds credibility.
- Include the recommendation and remediation timeline alongside the finding.

## Questionnaire-Specific Tips

- **CAIQ**: ITGC test results answer the CHM, IAM, and TVM sections. COBIT maturity assessments answer GRM and RSK.
- **SIG Lite**: The SIG's 18 domains align with COBIT 2019 processes. A COBIT process inventory maps naturally to SIG domains.
- **VSAQ**: ITGC access control testing answers Section 2. ITGC change management answers Section 5.
- **Custom questionnaires**: Reference the COBIT 2019 design factors to explain why certain controls are implemented at specific maturity levels.

## Cross-Reference to Other Skills

- `aicpa-soc-reporting` -- SOC 2 TSC CC6-CC9 map to ITGC categories (see aicpa-soc-reporting chunk 08).
- `coso-internal-controls` -- COBIT extends COSO P10-P12 into IT-specific control activities.
- `nist-800-53-rmf` -- COBIT APO13 maps to NIST PM/CA families.
- `audit-workpapers` -- ITGC testing workpapers follow audit workpaper standards.

## When to Load This Chunk

Load when the user asks about reusing ISACA/COBIT/ITGC evidence for customer questionnaires, mapping IT audit results to CAIQ/SIG/VSAQ, or using COBIT maturity for vendor due diligence.
