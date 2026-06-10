---
chunk_id: 08-questionnaire-reuse
parent_skill: isaca-audit-methodology
topic: "Questionnaire Evidence Reuse (CAIQ / SIG Lite / VSAQ / Customer Security Questionnaires)"
load_when: "user asks to map ISACA COBIT 2019 / ITGC / ITAC evidence to CAIQ, SIG Lite, VSAQ, or customer security questionnaires"
---

# ISACA / COBIT Evidence Reuse for Customer Security Questionnaires

ISACA methodology and COBIT 2019 governance assessments produce evidence that directly answers the governance, risk management, change management, and operations sections of customer security questionnaires. ITGC and ITAC test results are especially valuable -- they provide independently tested evidence that static questionnaire responses lack. This chunk explains how to repurpose ISACA audit work for questionnaire reuse.

Domain codes below are verified against the questionnaire publishers (2026-06-10): CSA CCM/CAIQ v4 has **17 domains** (GRC, A&A, AIS, BCR, CCC, CEK, DCS, DSP, HRS, IAM, IPY, IVS, LOG, SEF, STA, TVM, UEM); the Shared Assessments SIG measures **21 risk domains**; Google VSAQ uses **named questionnaires** (Web Application Security; Security & Privacy Program; Infrastructure Security; Physical & Datacenter Security), not numbered sections. Versions change -- verify against the questionnaire your customer actually sent.

## Mapping Table: COBIT 2019 / ITGC -> CAIQ v4 / SIG / VSAQ

| ISACA / COBIT Domain | CCM/CAIQ v4 Domain(s) | SIG Domain theme(s) | VSAQ Questionnaire | Key Fields Answered |
|----------------------|----------------------|---------------------|--------------------|----------------------|
| EDM (Governance) | GRC | Enterprise Risk Mgmt / Governance | Security & Privacy Program | IT governance, board oversight, value delivery |
| APO (Align/Plan/Organize) | GRC, HRS, STA | Governance, Risk Mgmt, HR | Security & Privacy Program | IT strategy, risk management, HR security, vendor mgmt |
| BAI (Build/Acquire/Implement) | CCC, AIS | SDLC, Change Mgmt | Web Application Security | Secure development, change management, testing |
| DSS (Deliver/Service/Support) | IAM, TVM, BCR, SEF | Access Control, Ops, Resilience, Incident Mgmt | Infrastructure Security | Access mgmt, vuln mgmt, BCP/DR, incident response |
| MEA (Monitor/Evaluate/Assess) | A&A, LOG | Compliance, Monitoring | Security & Privacy Program | Internal audit, monitoring, compliance |
| ITGC - Access Controls | IAM | Access Control | Infrastructure Security | Access provisioning, recertification, privileged access |
| ITGC - Change Management | CCC | Change Mgmt | Web Application Security | Change approval, CAB, emergency changes |
| ITGC - IT Operations | IVS, BCR, LOG, DCS | Operations, Resilience | Infrastructure Security / Physical & Datacenter Security | Monitoring, backup, job scheduling, facility controls |
| ITGC - SDLC | AIS | SDLC | Web Application Security | Secure coding, code review, testing |
| ITAC - Input/Processing/Output | AIS, DSP | Data Protection | Web Application Security | Input validation, processing integrity |
| ITAC - Data Integrity | DSP, CEK | Data Protection, Crypto | Infrastructure Security | Reconciliation, encryption, error handling |
| Risk Scoring (L x I x CRF) | GRC | Risk Mgmt | Security & Privacy Program | Risk quantification, prioritization |
| 5-Part Observation | A&A | Compliance | Security & Privacy Program | Finding documentation, remediation tracking |
| COBIT Maturity Assessment | GRC | Governance | Security & Privacy Program | Capability levels, improvement roadmap |

These are directional starting points, not authoritative crosswalks -- always answer against the specific question text.

## Evidence Reuse Strategy

### Step 1: Extract ITGC Test Results
- ITGC testing produces quantitative evidence: sample sizes, deviation rates, and conclusions.
- This is higher-quality evidence than self-attested questionnaire responses.
- Map ITGC categories (Access, Change, Ops, SDLC) to the CCM v4 domains above.

### Step 2: Package COBIT Maturity as Governance Evidence
- COBIT capability assessments (0-5 scale per process) provide structured governance evidence.
- A process at capability 3 (Established) or higher demonstrates mature governance to questionnaire reviewers.
- Include the assessment summary as an appendix to questionnaire responses.

### Step 3: Use 5-Part Observations for Transparency
- When disclosing findings in questionnaires, use the ISACA 5-part format (C-C-C-E-R).
- This format is instantly recognizable to auditors and builds credibility.
- Include the recommendation and remediation timeline alongside the finding.

## Questionnaire-Specific Tips

- **CAIQ v4**: ITGC test results answer the CCC, IAM, and TVM domains. COBIT capability assessments answer GRC and A&A.
- **SIG**: the SIG's 21 risk domains (current published count) are broader than COBIT's 5 domains; map per-question, not per-domain.
- **VSAQ**: ITGC access-control testing supports the Infrastructure Security questionnaire; change management supports Web Application Security. (VSAQ's GitHub repo was archived in 2022 -- confirm the customer still uses it.)
- **Custom questionnaires**: Reference the COBIT 2019 design factors to explain why certain controls are implemented at specific capability levels.

## Cross-Reference to Other Skills

- `aicpa-soc-reporting` -- SOC 2 TSC CC6-CC9 map to ITGC categories (see aicpa-soc-reporting chunk 08).
- `coso-internal-controls` -- COBIT extends COSO P10-P12 into IT-specific control activities.
- `nist-800-53-rmf` -- COBIT APO13 maps to NIST PM/CA families.
- `audit-workpapers` -- ITGC testing workpapers follow audit workpaper standards.

## When to Load This Chunk

Load when the user asks about reusing ISACA/COBIT/ITGC evidence for customer questionnaires, mapping IT audit results to CAIQ/SIG/VSAQ, or using COBIT capability levels for vendor due diligence.

## Citations

CCM/CAIQ v4 domain codes from `[CSA-CCM-v4]`. SIG domain count from Shared Assessments (sharedassessments.org/sig, retrieved 2026-06-10). VSAQ questionnaire names from the google/vsaq repository. See SKILL.md S10.
