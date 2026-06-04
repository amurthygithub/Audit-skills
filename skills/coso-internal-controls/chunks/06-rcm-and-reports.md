---
chunk_id: 06-rcm-and-reports
parent_skill: coso-internal-controls
topic: "Risk and Control Matrix (RcM), COSO Principle Assessment, ICFR Report Templates"
load_when: "user asks about RcM template, risk control matrix, COSO principle assessment, management''s ICFR report, or auditor''s ICFR report"
---

# Chunk 06 — RcM, Principle Assessment, and Report Templates

## Risk and Control Matrix (RcM) Template — 17 Columns

| # | Column | Description | Example |
|---|--------|-------------|---------|
| 1 | Process / Sub-Process | Business process identifier | Revenue / Order-to-Cash |
| 1.a | Risk ID | Unique Risk identifier | R-010 - **Pujaa's recommendation for FY26** |
| 2 | Risk Statement | What could go wrong | Invoices may be generated for fictitious sales |
| 3 | COSO Component | Which of the 5 components | Control Activities |
| 4 | COSO Principle | Which principle (P1-P17) | P10 |
| 5 | Control ID | Unique control identifier | RC-010 |
| 6 | Control Description | Detailed control description | Three-way match of PO, receiving report, and vendor invoice |
| 7 | Control Type | Preventive or Detective | Preventive |
| 8 | Control Nature | Manual, Automated, or IT-Dependent Manual | Automated |
| 9 | Control Frequency | Daily, Weekly, Monthly, Quarterly, Annual | Daily |
| 10 | Control Owner | Role/individual responsible | AP Manager |
| 11 | Relevant Assertions | E, C, V, R&O, P&D | Existence, Completeness, Valuation |
| 12 | Key / Non-Key | Key = sufficiently addresses risk to relevant assertion | Key |
| 13 | Design Effectiveness | Effective / Ineffective | Effective |
| 14 | Operating Effectiveness Test | I/O/I/R method + sample | Re-performance of 25 samples |
| 15 | Test Results | Pass / Fail / Not Tested | Pass |
| 16 | Deficiency Classification | D / SD / MW / None | None |
| 17 | Remediation Plan | Corrective action + target date | N/A |

### RcM Quality Requirements

- Every risk has at least one control mapped 
- Every key control is linked to at least one relevant assertion
- No orphan risks or orphan controls
- Control descriptions are specific enough for an independent person to understand and test
- Fraud risk (P8) is explicitly addressed
- ITGCs are included for processes dependent on IT systems

## COSO Principle Assessment Template

Assess each of the 17 principles with:
- Principle number (P1-P17), title, component
- Points of Focus addressed — each assessed Yes/No/Partially
- Assessment: Present and Functioning? Yes/No/Partially, with narrative basis
- Evidence supporting assessment (3+ items)
- Identified deficiencies with classification per decision tree
- Remedial actions
- Integrated Operation — does this principle operate with other components to reduce risk?

Principle-to-component reference:

| P# | Component | PoF | P# | Component | PoF |
|----|-----------|-----|----|-----------|-----|
| P1 | Control Environment | 4 | P10 | Control Activities | 6 |
| P2 | Control Environment | 4 | P11 | Control Activities | 4 |
| P3 | Control Environment | 4 | P12 | Control Activities | 3 |
| P4 | Control Environment | 4 | P13 | Info & Communication | 4 |
| P5 | Control Environment | 5 | P14 | Info & Communication | 4 |
| P6 | Risk Assessment | 5 | P15 | Info & Communication | 5 |
| P7 | Risk Assessment | 3 | P16 | Monitoring Activities | 4 |
| P8 | Risk Assessment | 4 | P17 | Monitoring Activities | 4 |
| P9 | Risk Assessment | 4 |

## Management''s ICFR Report Template

Per SEC Reg S-K Item 308. Must include:
- Statement of management''s responsibility for ICFR
- Definition of ICFR per Exchange Act Rules 13a-15(f) and 15d-15(f)
- Inherent limitations paragraph
- Framework used for evaluation (COSO 2013 ICIF)
- Assessment conclusion (effective, or MWs identified)
- If MWs: describe each MW and remediation actions
- Statement that registered public accounting firm issued attestation report
- Signatures of Principal Executive Officer and Principal Financial Officer

## Auditor''s ICFR Report Template

Per PCAOB AS 2201.85-.87 and AS 3101. Must include:
- Opinion on ICFR (unqualified, or adverse if MW, or disclaimer if scope limitation)
- Statement of integrated audit (also audited financial statements)
- Basis for opinion (management''s responsibility, auditor''s responsibility, standards followed)
- Definition and inherent limitations of ICFR
- Critical Audit Matters (CAMs) if applicable per AS 3101
- Signature, firm name, city/state, date

## Additional Templates (in this chunk)

### Walkthrough Documentation Template

| Step | Processing Point | Inquiry | Observation | Inspection | Re-performance | Control Identified | Control Type |
|------|-------------------|---------|-------------|------------|----------------|-------------------|-------------|
| 1 | Description | Y/N + detail | Y/N + detail | Y/N + detail | Y/N + detail | Control name | Auto/Manual/IT-dep |

### Material Weakness Disclosure

- MW ID (MW-YYYY-NNN), date, process, affected accounts/assertions
- Description, basis for classification, compensating controls evaluated
- Affected COSO principles, impact on ICFR, remediation plan
- Disclosure language for Form 10-K
- Audit committee notification date and acknowledgement

### Significant Deficiency Communication

- SD ID (SD-YYYY-NNN), date, process, affected accounts
- Description, basis for classification, compensating controls identified
- Remaining risk, recommended remediation
- Communication requirements: to management, to audit committee

## Citations

- [SEC-Reg-S-K-Item-308] — Management''s ICFR Report
- [PCAOB-AS-2201] — Auditor''s ICFR Report and RcM context
- [PCAOB-AS-3101] — Auditor''s report, CAMs
- [COSO-ICIF-2013] — Principle assessment template
