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
  - "chunks/04-itgc-itac.md SITGC Category 1: Access Controls"
  - "chunks/06-observation-and-lifecycle.md S5-Part format"
  - "chunks/05-risk-and-planning.md SFinding severity"
expected_outputs:
  finding: "YAML with finding_id, title, severity, condition, criteria, cause, effect, recommendations"
oracle:
  type: schema_match
  assertion: "Output contains all 5 parts (condition, criteria, cause, effect, recommendation) and severity classification"
data_refs:
  - "data/seeds/uc-02-input.json"
tests:
  - "tests/test_oracle.py::test_uc_02"
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

```yaml
finding:
  id: "ACC-2026-001"
  title: "Inadequate Access Recertification for Critical Applications"
  severity: "High"
  status: "Open"
  condition: "No periodic access recertification for 3 of 5 critical applications"
  criteria: "ISACA Standard S17; Company Policy ISP-003 Section 4.2; COBIT APO13.02"
  cause:
    description: "Lack of automated recertification tooling; insufficient staff"
    root_cause_category: "Technology"
  effect:
    actual: "12% of terminated employees retained active access avg 45 days"
    potential: "Unauthorized data access; GDPR Article 32 penalties up to EUR 20M"
    cobit_criteria_affected: ["Confidentiality", "Integrity", "Compliance"]
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
      target: "Q2 2026"
```