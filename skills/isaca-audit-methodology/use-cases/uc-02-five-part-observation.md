---
uc_id: UC-02
title: "ITGC finding in 5-part observation format"
industries: [financial-services, saas-technology]
frameworks: [ISACA-CISA-CRM, ITAF, COBIT-2019]
inputs:
  finding_context: "Access recertification gap discovered during quarterly ITGC testing of a core banking application"
  scope: "Access Controls category (ITGC Category 1) for 5 critical financial applications"
  evidence: "3 of 5 applications lack quarterly recertification; 12% of terminated employees retain active access"
procedure:
  - "chunks/04-itgc-itac.md §ITGC Category 1: Access Controls"
  - "chunks/06-observation-and-lifecycle.md §5-Part format"
  - "chunks/05-risk-and-planning.md §Finding severity"
expected_outputs:
  finding: "YAML with finding id, title, severity, condition, criteria, cause, effect, recommendations, sample_summary; result envelope carries a classification field equal to the severity"
oracle:
  type: schema_match
  assertion: "Output contains all 5 parts (condition, criteria, cause, effect, recommendation), severity classification, and a sample_summary (total/non_compliant/compliance_rate_pct)"
data_refs:
  - "data/seeds/uc-02-input.json"
tests:
  - "tests/test_isaca_audit_methodology_oracle.py::test_uc_02_five_part_observation"
status: stub
---

# UC-02 - ITGC Finding in 5-Part Observation Format

## Scenario

During quarterly ITGC testing at a commercial bank, the audit team discovers that access recertification is not performed for 3 of 5 critical financial applications. A sample of terminated employees shows 12% retained active access for an average of 45 days post-termination.

## Walk-Through

1. Apply ITGC Category 1 testing from `chunks/04-itgc-itac.md`: verify access provisioning, termination, recertification, privileged access, authentication, SoD.
2. Document finding using the 5-part observation format from `chunks/06-observation-and-lifecycle.md`.
3. Classify severity using the ISACA scale from `chunks/05-risk-and-planning.md` (Critical/High/Medium/Low).

## Expected Output

Severity "High" reflects the 60% deviation rate in critical applications -- a judgment call
per `chunks/05 §Finding Severity`, not a mechanical count (and never an automatic ICFR
deficiency classification). Criteria cite the auditee's obligations (policy + COBIT practice);
ITAF standards govern the auditor and are not finding criteria.

```yaml
classification: "High"
observation:
  id: "ACC-2026-001"
  title: "Inadequate Access Recertification for Critical Applications"
  severity: "High"
  status: "Open"
  condition: "No periodic access recertification for 3 of 5 critical applications"
  criteria: "Company Policy ISP-003 Section 4.2 (quarterly access recertification for critical applications); COBIT 2019 DSS05.04 (Manage user identity and logical access)"   # policy ref comes from the seed's finding_context.policy_reference
  cause:
    description: "Lack of automated recertification tooling; insufficient staff"
    root_cause_category: "Technology"
  effect:
    actual: "12% of terminated employees retained active access avg 45 days"
    potential: "Unauthorized data access; regulatory exposure under GLBA (Interagency Guidelines, 12 CFR 30 App. B) and FFIEC examination criticism"
    cobit_criteria_affected: ["Confidentiality", "Integrity", "Compliance"]  # information-attribute tags (house convention; see chunk 02)
  sample_summary:
    total_applications: 5
    non_compliant: 3
    compliance_rate_pct: 40.0
  recommendations:
    - type: "Primary"
      action: "Implement automated IGA tool"
      owner: "CISO"
      target: "Q3 2026"
    - type: "Compensating"
      action: "Manual recertification monthly until tool deployed"
      priority: "Immediate"
    - type: "Long-term"
      action: "Increase security staffing by 1 FTE for access governance"
      target: "Q1 2027"
```
