---
uc_id: UC-03
title: "COBIT 2019 design factors assessment for financial services"
industries: [financial-services]
frameworks: [COBIT-2019, ITAF]
inputs:
  organization: "Regional commercial bank, $12B assets, 2,500 employees"
  scope: "Assess governance system using COBIT 2019 design factors"
  context: "Strategy: compliance-focused; Risk: moderate; IT issues: legacy core banking, vendor concentration"
procedure:
  - "chunks/02-cobit-2019.md SDesign Factors"
  - "chunks/02-cobit-2019.md SAssessment procedure (10 steps)"
expected_outputs:
  design_factor_assessment: "YAML with enterprise strategy mapping, risk profile classification, prioritized COBIT objectives"
oracle:
  type: schema_match
  assertion: "Output contains enterprise_strategy, risk_profile, and prioritized_objectives fields"
data_refs:
  - "data/seeds/uc-03-input.json"
tests:
  - "tests/test_oracle.py::test_uc_03"
status: stub
---

# UC-03 - COBIT 2019 Design Factors Assessment

## Scenario

A regional commercial bank with $12B in assets seeks to assess its IT governance system using COBIT 2019 design factors. The bank operates a legacy core banking platform and has significant vendor concentration risk.

## Walk-Through

1. Apply COBIT 2019 design factors (5 factors) from `chunks/02-cobit-2019.md`.
2. Map enterprise strategy to prioritized COBIT objectives.
3. Classify risk profile based on threat landscape and IT-related issues.
4. Produce prioritized governance objectives aligned with the bank's context.

## Expected Output

```yaml
assessment:
  enterprise_strategy: "Compliance-focused"
  risk_profile:
    regulatory_risk: "High"
    technology_risk: "Moderate"
    vendor_risk: "High"
  prioritized_objectives:
    - MEA03  # Managed compliance
    - APO12  # Managed risk
    - APO13  # Managed security
    - DSS04  # Managed continuity
    - APO10  # Managed vendors
```
