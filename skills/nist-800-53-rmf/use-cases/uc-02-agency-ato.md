---
uc_id: UC-02
title: "Federal agency RMF Step 6: SAR 22 findings → POA&M, AO risk-accepts 14, ATO with conditions"
industries: [public-sector]
frameworks: [NIST-SP-800-53-Rev5, NIST-SP-800-37-Rev2, NIST-SP-800-53A-Rev5, FIPS-199]
inputs:
  system_name: "Agency Records System (ARS)"
  system_description: |
    Agency-operated records management system. Processes PII for ~80,000 individuals
    and case files for agency adjudicatory proceedings. On-prem in an agency data center.
    Categorized MODERATE (C: M, I: M, A: L). Selected 800-53 Rev 5 Moderate baseline
    (~325 controls). Independently assessed by an internal assessment team; 22 findings
    identified.
  categorization: {c: MODERATE, i: MODERATE, a: LOW, overall: MODERATE}
  baseline: MODERATE
  assessment_scope: "Full 800-53 Moderate baseline; all in-scope controls assessed."
  findings:
    - finding_id: SAR-001
      control_id: RA-3
      severity: High
      determination: Other Than Satisfied
      description: "Risk assessment is documented but does not include threat catalog updates from the last 12 months."
      cause: Operational lapse
      effect: "Risk to system confidentiality, integrity, or availability from RA-3 deviation."
      recommendation: "Update risk assessment per 800-30 Rev 1; include current threat catalog."
      compensating_control: null
    - finding_id: SAR-002
      control_id: AC-2   # base control, statement j — review accounts for compliance (AC-2(4) is Automated Audit Actions, a different requirement)
      severity: High
      determination: Other Than Satisfied
      description: "Quarterly account review was not performed for the last 4 quarters; logs show no review activity."
      cause: Operational lapse (process not followed)
      effect: "Risk to system confidentiality, integrity, or availability from the AC-2 (account review, element j) deviation."
      recommendation: "Re-perform account review; implement a calendar-tracked quarterly task with sign-off in the GRC tool."
      compensating_control: null
    - finding_id: SAR-003
      control_id: IA-5(1)
      severity: Low
      determination: Other Than Satisfied
      description: "Password policy does not enforce minimum length of 12 characters."
      cause: Design weakness
      effect: "Risk to system confidentiality, integrity, or availability from IA-5(1) deviation."
      recommendation: "Update password policy; deploy to identity provider."
      compensating_control: "Manual review process exists but is not fully effective."
    # … 19 additional findings (1 High, 11 Moderate, 7 Low). Full list in data/seeds/uc-02-findings.json
  total_findings: 22
  risk_acceptances: 14
  conditions: 8
  ato_decision: "AUTHORIZE_WITH_CONDITIONS"
procedure:
  - "chunks/05-assess.md §Procedure — Execute assessment per 800-53A. Generate SAR."
  - "chunks/06-authorize.md §Procedure — AO reviews SSP, SAR, POA&M, risk-acceptance memos."
  - "chunks/06-authorize.md §ATO decision logic — 22 findings; 14 risk-accepted (8 Low, 6 Moderate with documented rationale); 8 conditions (3 High + 5 Moderate, remediation required within 30/60/90 days)."
  - "chunks/06-authorize.md §Procedure — Issue ATO letter with conditions. Specify duration (1 year for agency ATO)."
  - "chunks/07-monitor.md §Procedure — Begin continuous monitoring (Step 7)."
expected_outputs:
  sar:
    total_findings: 22
    severity_distribution: {High: 3, Moderate: 11, Low: 8}
    risk_accepted: 14
    conditions: 8
  poam:
    poam_count: 22
    risk_distribution: {High: 3, Moderate: 11, Low: 8}
    milestones: {30_days: 2, 60_days: 3, 90_days: 3, ongoing: 14}
  ato_decision:
    decision: AUTHORIZE_WITH_CONDITIONS
    duration: 1 year
    conditions:
      - "Remediate SAR-001 (AC-2 account review, element j) within 30 days; submit evidence to AO."
      - "Remediate SAR-003 (CM-6) within 60 days; deploy SCAP scanning."
      - "Remediate SAR-002 (AU-6(1)) within 60 days; document thresholds in IRP."
      - "All 8 Moderate-and-above findings remediated or risk-accepted within 90 days."
    risk_accepted_findings:
      - finding_id: SAR-004  # Low
        rationale: "Compensating control present; remediation scheduled for next major release."
      # … 13 more
    residual_risk: MODERATE
  next_continuous_monitoring:
    annual_assessment_date: "YYYY-MM-DD + 1 year"
    monthly_vuln_scans: true
    significant_change_review: true
oracle:
  type: schema_match
  assertion: |
    The skill's output must satisfy:
      - ato_decision.decision == "AUTHORIZE_WITH_CONDITIONS"
      - ato_decision.conditions length == 8
      - ato_decision.risk_accepted_findings length == 14
      - poam.poam_count == 22
      - poam.risk_distribution sums to 22
      - next_continuous_monitoring.annual_assessment_date is set
      - residual_risk in ["MODERATE", "HIGH"]
data_refs:
  - "data/seeds/uc-02-input.json"
  - "data/seeds/uc-02-findings.json"
  - "data/seeds/uc-02-expected.json"
tests:
  - "tests/test_nist_800_53_rmf_oracle.py::test_uc_02_oracle"
  - "tests/test_nist_800_53_rmf_trace.py::test_use_cases_cite_skill_sections"
  - "tests/test_metamorphic.py::test_uc_02_risk_severity_change"
token_baseline:
  input_p50: null
  output_p50: null
status: active
---

# UC-02 — Federal agency RMF Step 6: SAR + POA&M + ATO with conditions

## Scenario

A federal civilian agency has assessed its records management system (ARS) and the assessment team has identified 22 findings — 3 High, 11 Moderate, 8 Low. The system is MODERATE-baseline, 800-53 Rev 5, on-prem in an agency data center. The AO must decide: ATO, ATO with conditions, or Deny.

The agency's risk tolerance allows:

- 14 findings to be **risk-accepted** with documented rationale (8 Low + 6 Moderate with strong compensating controls or time-bound remediation).
- 8 findings (all Moderate and above) to be **conditions** of the ATO, with remediation required within 30, 60, or 90 days.

Decision: **ATO with Conditions**, duration **1 year**.

## Walk-through

### Step 1 — Assessment aggregation (Skill §5.4, §6.3)

For each in-scope control, the assessor's 800-53A determination is recorded. Aggregation produces the SAR with one finding per control / enhancement. Severity classification (per §4.4) is based on the 800-53A determination, the operational vs. design nature of the finding, and the presence of compensating controls.

In this scenario:

| Severity | Count | Examples |
|----------|-------|----------|
| High | 4 | SAR-001 (AC-2 element j — account review not performed), SAR-003 (CM-6 config drift) |
| Moderate | 8 | SAR-002 (AU-6(1) escalation thresholds), others |
| Low | 10 | Mostly documentation gaps and minor operational lapses |

The SAR output (§6.3) for each finding includes:

```yaml
finding_id: SAR-001
control_id: AC-2   # base control, statement j — review accounts for compliance (AC-2(4) is Automated Audit Actions, a different requirement)
control_title: "Account Management | Automated Audit Actions"
severity: High
determination: Other Than Satisfied
description: "Quarterly account review was not performed..."
condition: "No quarterly account-review event recorded since 2024-Q4"
criteria: "AC-2(4) assessment objective 800-53A: review of accounts is performed at a defined frequency"
cause: "Operational lapse — the process is documented but the calendar-tracked task was not executed"
effect: "Stale accounts may persist beyond separation; risk of unauthorized access"
recommendation: "Re-perform the review; implement a calendar-tracked task with sign-off in the GRC tool"
compensating_control: null
remediation_plan: "Open POA&M-001; complete within 30 days"
risk_acceptance_required: false
```

### Step 2 — POA&M population (Skill §6.4)

Each finding becomes a POA&M item:

```yaml
poam_id: POA&M-001
finding_id: SAR-001
control_id: AC-2   # base control, statement j — review accounts for compliance (AC-2(4) is Automated Audit Actions, a different requirement)
weakness_description: "Quarterly account review not performed for two quarters"
weakness_detected_date: "2026-05-15"
risk_level: High
scheduled_completion_date: "2026-06-14"  # 30 days
status: Open
vendor_dependent: false
remediation_plan: "Re-perform review; implement calendar-tracked task"
milestones: ["2026-05-20: kickoff", "2026-06-10: validation", "2026-06-14: close"]
```

POA&M aggregate:

- 22 items
- 3 High, 11 Moderate, 8 Low
- 2 due in 30 days (High), 3 due in 60 days (Moderate), 3 due in 90 days (Moderate), 14 ongoing / time-bound risk-accepted

### Step 3 — AO review and risk acceptance (Skill §4.5, §5.5)

The AO reviews the SAR, POA&M, and the system owner's risk-acceptance memos. For each risk-accepted finding, the AO signs a memo that:

- Identifies the finding (by ID and control).
- States the residual risk.
- States the rationale (compensating control, business case, time-bound remediation).
- States the remediation date and the trigger for re-review.

For 14 findings (8 Low + 6 Moderate with compensating controls or time-bound remediation), the AO risk-accepts. For 8 findings (the 3 High + 5 Moderate without compensating control or above risk tolerance), the AO issues conditions.

### Step 4 — ATO letter (Skill §6.5)

```
[Agency Letterhead]
[Date]

MEMORANDUM FOR System Owner, ARS
FROM: [Authorizing Official]
SUBJECT: Authorization Decision — Agency Records System (ARS)

1. AUTHORIZATION DECISION: Authorize with Conditions.
2. DURATION: 1 year from this date.
3. CONDITIONS:
   a. Remediate SAR-001 (AC-2(4)) within 30 days; submit evidence to AO.
   b. Remediate SAR-003 (CM-6) within 60 days; deploy SCAP scanning on production database.
   c. Remediate SAR-002 (AU-6(1)) within 60 days; document escalation thresholds in IRP.
   d. All 8 Moderate-and-above findings remediated or risk-accepted within 90 days.
4. RESIDUAL RISK: Moderate. Accepted with conditions.
5. NEXT CONTINUOUS MONITORING REVIEW: [date + 1 year].
6. SIGNATURE: [AO name, title, date]
```

### Step 5 — Continuous monitoring (Skill §5.6)

The ISCM strategy in the SSP §13 documents:

- **Annual assessment** — all controls re-assessed within 1 year.
- **Monthly vulnerability scans** — internal and external.
- **POA&M management** — open items reviewed monthly, status updated.
- **Significant change review** — any change to the system triggers a Step 4 implementation update and a partial assessment.
- **Incident-driven reassessment** — major incidents (catastrophic, severe) trigger re-authorization.

## Expected Output (oracle target)

```yaml
sar:
  total_findings: 22
  severity_distribution: {High: 3, Moderate: 11, Low: 8}
  risk_accepted: 14
  conditions: 8
poam:
  poam_count: 22
  risk_distribution: {High: 3, Moderate: 11, Low: 8}
ato_decision:
  decision: AUTHORIZE_WITH_CONDITIONS
  duration: 1 year
  conditions_count: 8
  risk_accepted_count: 14
  residual_risk: MODERATE
next_continuous_monitoring:
  annual_assessment_date: "2027-MM-DD"
  monthly_vuln_scans: true
  significant_change_review: true
```

## Variations / edge cases (test_metamorphic.py)

- **V1 — Severity change:** if a High finding is re-classified as Moderate (e.g., the compensating control is re-validated), the conditions count drops to 7. The skill must reflect the new state.
- **V2 — Risk acceptance rescinded:** if the AO rescinds a risk-acceptance, the conditions count rises. The skill must handle the reciprocal change.
- **V3 — Additional finding discovered:** if a Step 7 continuous-monitoring scan finds a new High finding, the system is no longer in compliance; the AO must re-authorize. The skill must produce a re-authorization package.
- **V4 — Significant change:** if the system migrates to a new data center, a partial assessment is required. The skill must produce the partial SAR + addendum.
- **V5 — Compensating control challenged:** if the AO or OIG challenges a compensating control on a Moderate finding, the residual risk re-rates to High. The skill must reflect.

## Acceptance

- [x] UC registered.
- [x] Oracle defined.
- [x] Data seeds at `data/seeds/uc-02-input.json`, `data/seeds/uc-02-findings.json`, `data/seeds/uc-02-expected.json`.
- [x] Tests at `tests/test_oracle.py::test_uc_02`, `tests/test_trace.py::test_uc_02_trace`, `tests/test_metamorphic.py::test_uc_02_risk_severity_change`.
- [ ] Token baseline populated.
