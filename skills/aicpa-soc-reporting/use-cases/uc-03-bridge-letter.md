---
uc_id: UC-03
title: "Bridge Letter for Gap Period Between SOC 2 Reports"
industries: [saas-technology, financial-services]
frameworks: [SOC-2-TSC-2017]
inputs:
  prior_report: "SOC 2 Type II covering 2025-01-01 to 2025-12-31, issued 2026-02-15."
  gap_period: "2026-01-01 to 2026-06-30 (6 months)."
  next_report_expected: "2026-08-15."
  material_changes: "No material changes to system description or control design."
  exceptions_in_prior: "No exceptions in prior SOC 2 Type II report."
procedure:
  - "chunks/05-assertion-bridge.md -- Generate bridge letter covering 4 attestations: system description changes, control design changes, operating effectiveness exceptions, CUEC/CSOC appropriateness."
  - "chunks/02-engagement-type-decision.md -- Confirm prior report was SOC 2 Type II."
expected_outputs:
  bridge_letter: "Management-issued bridge letter with all 4 attestations, disclaimer of no auditor assurance, covering gap period."
oracle:
  type: schema_match
  assertion: "Bridge letter contains: addressee, reference to prior SOC 2 report, 4 attestations, disclaimer statement, management signature block."
data_refs:
  - "data/seeds/uc-03-input.json (planned)"
tests:
  - "tests/test_oracle.py::test_uc_03_oracle (planned)"
status: stub
---

# UC-03 -- Bridge Letter for Gap Period

## Scenario

CloudStack SaaS Inc. received their SOC 2 Type II report covering Jan 1-Dec 31, 2025, issued Feb 15, 2026. A customer requests assurance through June 2026, but the next report will not be ready until August 2026. No material changes to system description or control design occurred. No exceptions in the prior SOC 2 Type II report.

## Walk-through

1. Determine gap period: Jan 1, 2026 to Jun 30, 2026 (6 months). Bridge letter needed.

2. Generate bridge letter per chunk 05 template covering:
   - Attestation 1: No material changes to system description.
   - Attestation 2: No material changes to control design.
   - Attestation 3: No exceptions in operating effectiveness.
   - Attestation 4: CUECs and CSOCs remain appropriate.

3. Include disclaimer: "This letter is a management representation only and does not provide auditor assurance. It is not a substitute for a SOC 2 Type II report."

4. Signed by management representative, issued on company letterhead.

## Output Sample
```
CloudStack SaaS Inc.
June 15, 2026

RE: Bridge Letter -- CloudStack Platform SOC 2 Type II Report
Period Covered: January 1, 2026 to June 30, 2026

Dear Customer:

This letter supplements the SOC 2 Type II report issued by CPA Firm dated February 15, 2026, covering January 1, 2025 to December 31, 2025.

During the period from January 1, 2026 to June 30, 2026:

1. There have been no material changes to the system description.
2. There have been no material changes to the design of controls.
3. There have been no exceptions in the operating effectiveness of controls.
4. The CUECs and CSOCs disclosed in the SOC 2 Type II report remain appropriate.

This letter is a management representation only and does not provide auditor assurance. It is not a substitute for a SOC 2 Type II report and should not be relied upon as such.

Sincerely,
Jane Smith
CISO
CloudStack SaaS Inc.
```
