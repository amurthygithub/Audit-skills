---
chunk_id: 08-questionnaire-reuse
parent_skill: coso-internal-controls
topic: "Questionnaire Evidence Reuse (CAIQ / SIG Lite / VSAQ / Customer Security Questionnaires)"
load_when: "user asks to map COSO 2013 ICIF / SOX 404 evidence to CAIQ, SIG Lite, VSAQ, or customer security questionnaires"
---

# COSO Evidence Reuse for Customer Security Questionnaires

COSO-based internal control evidence, particularly SOX 404 ICFR documentation, provides robust answers for governance, risk assessment, and control activity questionnaire domains. While COSO is not a cybersecurity framework per se, the entity-level and process-level control evidence directly maps to the governance sections of CAIQ, SIG Lite, and VSAQ. This is especially relevant for public-company SaaS providers subject to both SOX 404 and vendor due diligence.

## Mapping Table: COSO ICIF -> CAIQ / SIG Lite / VSAQ

| COSO Component / Principle | CAIQ v4 Section(s) | SIG Lite Domain(s) | VSAQ Module | Key Fields Answered |
|---------------------------|--------------------|--------------------|--------------------|----------------------|
| Control Environment (P1-P5) | Governance & Risk Mgmt (GRM) | Governance, Org Security | Section 1 | Board oversight, ethics, org structure, accountability |
| Risk Assessment (P6-P9) | Risk Management (RSK), Fraud | Risk Management | Section 1, 3 | Risk methodology, fraud risk, change risk assessment |
| Control Activities (P10-P12) | GRM, CHM | Control Environment, Change Mgmt | Section 1, 5 | Control design, technology controls, policies |
| Information & Communication (P13-P15) | GRM, HRS | Governance, Communication | Section 1 | Quality information, internal/external communication |
| Monitoring Activities (P16-P17) | AAC | Monitoring, Compliance | Section 1 | Ongoing evaluations, deficiency communication |
| Deficiency Classification (MW/SD/D) | N/A (customer-specific) | N/A | Section 1 | Audit committee communication, CAP status |
| Walkthrough Documentation | GRM | Control Environment | Section 1 | Process documentation, I/O/I/R evidence |
| Risk & Control Matrix (RcM) | RSK | Risk Management | Section 1, 3 | Control mapping, assertion coverage |

## Evidence Reuse Strategy

### Step 1: Extract ICFR Governance Evidence
- The COSO Control Environment principles (P1-P5) produce evidence that directly answers governance questionnaires.
- Board minutes, committee charters, ethics policies, and accountability frameworks are questionnaire-ready.
- Entity-level control (ELC) assessments provide precision classification that many questionnaires ask about.

### Step 2: Map SOX 404 Scoping to Questionnaire Domains
- Significant account scoping maps to "key systems" and "critical data" questions.
- Walkthrough documentation maps to process description questions.
- Deficiency classification (MW/SD/D) maps to "known control gaps" questions -- disclose carefully and consistently.

### Step 3: Use the RcM as a Response Library
- The Risk and Control Matrix (17 columns) is a comprehensive control inventory.
- Each RcM row is a pre-written answer to "what controls do you have for X?"
- Filter the RcM by assertion, process, or control objective to answer specific questionnaire domains.

## Questionnaire-Specific Tips

- **CAIQ governance sections (GRM, RSK)**: COSO evidence is the strongest possible answer. Reference the ICFR opinion and COSO framework adoption.
- **SIG Lite governance domain**: Map COSO principles P1-P9 to SIG governance questions. Include the external auditor's ICFR opinion as supporting evidence.
- **VSAQ Section 1 (Security Organization)**: The COSO Control Environment directly maps to security organization questions. Reference the board's oversight role and committee structure.
- **Custom governance questionnaires**: Use the COSO Principle Assessment (per-principle, PoF-by-PoF) as structured evidence.

## Cross-Reference to Other Skills

- `aicpa-soc-reporting` -- SOC 2 TSC CC1-CC5 explicitly map to COSO P1-P17 (see aicpa-soc-reporting chunk 08).
- `isaca-audit-methodology` -- COBIT governance objectives (EDM) map to COSO Control Environment.
- `nist-800-53-rmf` -- NIST PM family maps to COSO P1-P5.
- `audit-workpapers` -- RcM and walkthrough documentation follow workpaper standards.

## When to Load This Chunk

Load when the user asks about reusing SOX 404/COSO evidence for customer questionnaires, mapping governance controls to CAIQ/SIG/VSAQ, or using ICFR documentation for vendor due diligence.
