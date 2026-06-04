---
title: Board-Ready Audit Committee Deck Template
version: 1.0.0
date_added: 2026-06-03
status: draft
industries: [financial-services, saas-technology, healthcare, public-sector, other]
frameworks: [SOC-2-TSC-2017, COSO-ICIF-2013, NIST-SP-800-53-Rev5, ISACA-COBIT-2019, ISO-27001-2022]
use_case: Present quarterly compliance posture to audit committee / board of directors.
---

# Board-Ready Audit Committee Deck Template

A 15-20 slide quarterly executive presentation for audit committees and boards. SOC 2 reports provide the reporting cadence. Replace bracketed placeholders `[VALUE]` with live data.

## Slide-by-Slide Outline

### Slide 1: Cover
- Title: "Audit Committee Compliance Update -- Q[N] FY[YYYY]"
- Date, presenter name/title, confidentiality marking

### Slide 2: Executive Summary (3 bullets)
- Overall posture: [GREEN/YELLOW/RED] -- see §Control Coverage Heat Map
- Key wins this quarter: [bullet 1], [bullet 2], [bullet 3]
- Open risks needing committee attention: [bullet 1], [bullet 2]

### Slide 3: Control Coverage Heat Map
- Table: Y-axis = framework domains (SOC 2 TSC categories). X-axis = coverage status (Fully Covered / Partial / Gap / N/A).
- Color-coding: Green = Fully Covered, Yellow = Partial, Red = Gap, Grey = N/A.
- Total control count vs. mapped count. Coverage % by domain.

### Slide 4: SOC 2 / Attestation Program Status
- Current SOC report type, opinion, period, issuing firm, expiration.
- SOC 2 TSC categories in scope. Key CUECs disclosed. Subservice carve-outs/inclusive.
- Bridge letter status (if applicable). Next examination window.

### Slide 5: Audit Findings Summary
- Table: Finding ID, Severity (Critical/High/Moderate/Low), Control Domain, Status, Days Open.
- Total findings: open vs. closed vs. risk-accepted. Aging buckets (<30d, 30-60d, 60-90d, >90d).
- Trend line: findings per quarter (last 4 quarters).

### Slide 6: Exceptions & Deviations Log
- Table: Exception ID, Control Reference, Description, Compensating Control, Expiration, Approval.
- Total active exceptions. Expired exceptions needing renewal.

### Slide 7: Corrective Action Plan (CAP) Status
- Table: CAP ID, Finding Linked, Owner, Target Date, % Complete, Milestone Status.
- CAPs completed vs. outstanding. Overdue CAPs highlighted red.

### Slide 8: CAP Aging & Velocity
- Bar chart: CAPs opened vs. closed per quarter (trailing 4 quarters).
- Average days to close. Stale CAPs (>90 days open) count and detail.

### Slide 9: Risk Register -- Top Risks
- Table: Top 10 risks by residual score. Inherent (LxI), Controls, Residual, Owner, Treatment.
- Risk heat map (5x5: Likelihood x Impact) with residual risk positions.

### Slide 10: Forward-Looking Risks (Horizon Scan)
- Upcoming regulatory changes (SEC cybersecurity rules, EU DORA, state privacy laws).
- M&A risk. New product launch risk. Geo-expansion risk.
- AI/ML governance evolving expectations. Third-party concentration risk.

### Slide 11: Third-Party / Vendor Risk
- Top N critical vendors by risk tier. Inherited control summary.
- Vendors without current SOC 2/ISO 27001. Vendors on watch list. Fourth-party risk.

### Slide 12: Customer Audit Fatigue & Questionnaire Reuse
- Inbound questionnaires this quarter: total count, distinct questionnaires, CAIQ count.
- Evidence reuse rate (% of fields answered from pre-mapped repository).
- Average turnaround time. Top 3 most-requested control domains.
- Cross-reference: see questionnaire-reuse chunk in each skill.

### Slide 13: Training & Awareness
- Compliance training completion rate (target >= 95%). Phishing simulation click rate.
- Policy attestation completion. Role-based training coverage by department.

### Slide 14: Incident & Breach Summary
- Incidents this quarter: total count, severity breakdown, MTTC/MTTR.
- Reportable incidents (regulator/customer notification). Root-cause trends.

### Slide 15: Budget Ask / Resource Request
- Current compliance spend: people, tools, external audit fees, consulting.
- Requested incremental: [amount] for [purpose].
- ROI / risk-reduction rationale. Consequences of not funding.

### Slide 16: Key Decisions Requested
- Decision 1: [Description, Options, Recommendation]
- Decision 2: [Description, Options, Recommendation]

### Slide 17: Metrics Dashboard (One-Pager)
- KPIs at a glance: control coverage %, findings open, CAPs overdue, questionnaire turnaround, training %, incident count, audit opinion status.
- Each KPI with green/yellow/red threshold bands and QoQ trend arrow.

### Slide 18: Appendix -- Framework Mappings
- SOC 2 TSC <-> COSO 2013 ICIF <-> NIST 800-53 Rev 5 <-> ISO 27001:2022 <-> COBIT 2019.
- Mapping table: columns = frameworks, rows = control domains, cells = mapped control IDs.

### Slide 19: Appendix -- Detailed Finding Log
- Full finding log exportable from GRC tool. Filterable by severity, owner, status.

### Slide 20: Appendix -- Acronym Glossary
- SOC, TSC, CUEC, CSOC, CAP, POA&M, ATO, RMF, ITGC, ITAC, ELC, MW, SD, D, etc.

## Cross-Reference to Skills

- `aicpa-soc-reporting` -- SOC 2 opinion, TSC categories, CUEC/CSOC (Slides 4, 18)
- `nist-800-53-rmf` -- POA&M, ATO, control families, FedRAMP (Slides 5-8, 18)
- `coso-internal-controls` -- Deficiency classification, MW/SD/D, RcM (Slides 5, 6, 18)
- `isaca-audit-methodology` -- ITGC/ITAC findings, risk scoring (Slides 5, 9, 18)
- `audit-workpapers` -- Finding documentation format (Slides 5, 7)

## Usage Notes

- Update quarterly. Present within 45 days of quarter-end.
- Redact customer names for board distribution.
- Archive each quarter for regulatory history (retention: 7 years per SEC 17a-4).
- Cross-reference each finding to a CAP ID with bidirectional traceability.
