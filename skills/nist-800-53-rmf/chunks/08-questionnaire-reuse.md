---
chunk_id: 08-questionnaire-reuse
parent_skill: nist-800-53-rmf
topic: "Questionnaire Evidence Reuse (CAIQ / SIG Lite / VSAQ / Customer Security Questionnaires)"
load_when: "user asks to map 800-53 evidence to CAIQ, SIG Lite, VSAQ, or customer security questionnaires, or asks to reduce customer audit fatigue"
---

# NIST 800-53 / RMF Evidence Reuse for Customer Security Questionnaires

FedRAMP authorization packages and NIST 800-53 assessment evidence are the gold-standard evidence source for customer questionnaires. Since FedRAMP inherits directly into CAIQ (the CSA CAIQ explicitly maps to NIST 800-53 controls), a FedRAMP-authorized system can answer virtually 100% of CAIQ, SIG, and VSAQ fields. This chunk explains how to reuse NIST 800-53 evidence systematically.

## Mapping Table: NIST 800-53 Control Families -> CAIQ / SIG Lite / VSAQ

| NIST 800-53 Family | CAIQ v4 Section(s) | SIG Lite Domain(s) | VSAQ Module | Key Fields Answered |
|--------------------|-------------------|--------------------|--------------------|----------------------|
| AC (Access Control) | IAM, DCS | Access Control, Physical | Section 2, 7 | MFA, SSO, access reviews, provisioning |
| AT (Awareness & Training) | Human Resources (HRS) | HR Security, Training | Section 1 | Security training, role-based training |
| AU (Audit & Accountability) | Audit & Compliance (AAC) | Monitoring, Compliance | Section 1, 4 | Audit logging, log review, retention |
| CA (Assessment & Authorization) | AAC, Governance (GRM) | Compliance, Governance | Section 1 | Authorization boundary, continuous monitoring |
| CM (Configuration Management) | CHM, TVM | Change Mgmt, Config Mgmt | Section 4, 5 | CMDB, baseline config, change approval |
| CP (Contingency Planning) | BCR, IRM | BCP/DR, Incident Response | Section 6, 9 | BCP/DR plan, testing, alternate site |
| IA (Identification & Authentication) | IAM, DCS | Access Control | Section 2 | MFA, identity proofing, PKI |
| IR (Incident Response) | IRM | Incident Management | Section 9 | IR plan, exercises, reporting, lessons learned |
| MA (Maintenance) | TVM, CHM | Operations Mgmt | Section 4 | Maintenance scheduling, remote maintenance |
| MP (Media Protection) | DCS | Data Security | Section 3 | Media sanitization, labeling, disposal |
| PE (Physical & Environmental) | Physical Security | Physical Security | Section 7 | Physical access, monitoring, visitor control |
| PL (Planning) | GRM | Governance | Section 1 | SSP, security architecture |
| PM (Program Management) | GRM | Governance | Section 1 | Risk management strategy, security program |
| PS (Personnel Security) | HRS | HR Security | Section 1 | Background checks, termination, screening |
| PT (Privacy) | DPR, DCS | Privacy | Section 3 | PII inventory, privacy notice, consent, data rights |
| RA (Risk Assessment) | RSK | Risk Management | Section 1, 3 | Risk assessment, vulnerability assessment |
| SA (System & Services Acquisition) | SCM, SDE | Third-Party Mgmt, SDLC | Section 8 | Vendor assessment, supply chain, SDLC security |
| SC (System & Communications Protection) | DCS, EKM, IAM | Network Security, Encryption | Section 2, 3, 4 | Encryption, network segmentation, boundary protection |
| SI (System & Information Integrity) | TVM, IRM | Vuln Mgmt, Malware Protection | Section 6 | Malware protection, flaw remediation, SIEM |
| SR (Supply Chain Risk Management) | SCM | Third-Party Mgmt | Section 8 | Supply chain risk, counterfeit detection |

## FedRAMP -> CAIQ Inheritance Map

FedRAMP-authorized systems (Moderate/High) directly satisfy CAIQ because:
1. The CSA CAIQ v4 explicitly maps its control IDs to NIST 800-53 Rev 5 controls.
2. FedRAMP requires a 3PAO assessment against 800-53 (more rigorous than self-attestation).
3. FedRAMP continuous monitoring (ConMon) provides ongoing evidence that static questionnaires cannot.

## Evidence Reuse Strategy

### Step 1: Build an 800-53 -> Questionnaire Mapping
- Extract the SSP, SAR, and POA&M from the RMF authorization package.
- Map each 800-53 control implementation statement to CAIQ CIDs, SIG Lite questions, VSAQ fields.
- For FedRAMP-authorized systems, the FedRAMP Readiness Assessment Report (RAR) plus SSP often answers 90%+ of questionnaire fields.

### Step 2: Create a "FedRAMP Lite" Response Package
- Produce a concise 3-page summary: system boundary, control inheritance, 3PAO assessment summary, ConMon status.
- This single document answers ~70% of a SIG Lite and replaces dozens of one-off responses.
- Include the FedRAMP P-ATO letter as the authoritative attestation.

### Step 3: Maintain Evidence Currency
- Update mappings when ConMon artifacts roll (monthly vuln scans, annual assessment).
- When a new customer questionnaire arrives, check ConMon age: evidence > 90 days old should be refreshed.
- POA&M items resolved should be reflected in updated questionnaire responses.

## Questionnaire-Specific Tips

- **CAIQ**: FedRAMP Moderate/High authorized systems should answer with the P-ATO letter + SSP executive summary. No need to re-answer per-vendor.
- **SIG Lite**: The SIG's 18 domains map well to 800-53 control families. Use the family-to-domain mapping above.
- **VSAQ**: A FedRAMP authorization covers ~95% of VSAQ. The remaining 5% are commercial-control questions (e.g., SaaS-specific uptime SLAs).
- **Custom questionnaires**: Reference the SSP control implementation narratives. These are pre-written, reviewed, and approved.

## Cross-Reference to Other Skills

- `aicpa-soc-reporting` -- SOC 2 Type II provides complementary evidence for non-federal customers (see its chunk 08).
- `isaca-audit-methodology` -- COBIT APO13 maps to NIST PM and CA families.
- `coso-internal-controls` -- COSO Principle 7 (risk assessment) maps to NIST RA family.
- `audit-workpapers` -- SSP and SAR sections follow workpaper documentation standards (AS 1215).

## When to Load This Chunk

Load when the user asks about CAIQ, SIG, VSAQ, security questionnaires, FedRAMP reuse, 3PAO evidence for customers, or mapping NIST 800-53 to vendor assessments.
