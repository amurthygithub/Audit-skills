---
uc_id: UC-01
title: "SaaS COBIT 2019 maturity assessment"
industries: [saas-technology, public-sector]
frameworks: [COBIT-2019, ITAF]
inputs:
  organization: "SaaS company with 500 employees, SOC 2 Type II in place, multi-tenant architecture"
  scope: "Security management process (APO13), change management (BAI07), operations (DSS01)"
  current_capability: "Baseline evidence: documented security policy, SIEM deployed, 24/7 SOC, partial RBAC"
procedure:
  - "chunks/02-cobit-2019.md SAssessment procedure (10 steps)"
  - "chunks/03-itaf-and-maturity.md SMaturity assessment process"
  - "chunks/07-outputs-and-cross-refs.md SMaturity output"
expected_outputs:
  maturity_assessment: "YAML with current/target maturity per process, gap analysis, improvement roadmap"
oracle:
  type: schema_match
  assertion: "Output contains current_maturity, target_maturity, gap, and improvement_roadmap fields per COBIT 2019 format"
data_refs:
  - "data/seeds/uc-01-input.json"
tests:
  - "tests/test_oracle.py::test_uc_01"
status: stub
---

# UC-01 - SaaS COBIT 2019 Maturity Assessment

## Scenario

A 500-employee B2B SaaS company with SOC 2 Type II in place wants to assess its COBIT 2019 maturity for security management (APO13), change management (BAI07), and IT operations (DSS01). The company operates a multi-tenant application on AWS.

## Walk-Through

1. Select objectives in scope: APO13 (Managed Security), BAI07 (Managed Change Acceptance), DSS01 (Managed Operations).
2. Apply COBIT 2019 assessment procedure (10 steps from `chunks/02-cobit-2019.md`).
3. Determine current capability using CMMI-based model (0-5) from `chunks/03-itaf-and-maturity.md`.
4. Identify gaps between current and target levels.
5. Develop improvement roadmap with quick wins, short-term, medium-term, long-term phases.

## Expected Output

```yaml
assessment:
  date: "YYYY-MM-DD"
  processes:
    - id: APO13
      name: "Managed Security"
      current_maturity: 2.5
      target_maturity: 4
      gap: 1.5
    - id: BAI07
      name: "Managed Change Acceptance"
      current_maturity: 3
      target_maturity: 4
      gap: 1.0
    - id: DSS01
      name: "Managed Operations"
      current_maturity: 3
      target_maturity: 4
      gap: 1.0
  improvement_roadmap:
    - phase: "Quick Win (1-3 months)"
      gain: 0.5
      initiatives:
        - "Refresh security policy for cloud/multi-tenant architecture"
    - phase: "Short-Term (3-6 months)"
      gain: 1.0
      initiatives:
        - "Integrate remaining systems into SIEM monitoring"
        - "Implement role-based security training"
```