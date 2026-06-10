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
  - "chunks/02-cobit-2019.md §Design Factors"
  - "chunks/02-cobit-2019.md §Assessment procedure (10 steps)"
expected_outputs:
  design_factor_assessment: "YAML with enterprise strategy mapping, risk profile classification, prioritized COBIT objectives (each with objective/name/priority/rationale), and design_factors_applied (the 5 factors this worked example weights)"
oracle:
  type: schema_match
  assertion: "Output contains enterprise_strategy, risk_profile, prioritized_objectives (5, ordered MEA03/APO12/APO13/DSS04/APO10), and design_factors_applied (5 factors)"
data_refs:
  - "data/seeds/uc-03-input.json"
tests:
  - "tests/test_isaca_audit_methodology_oracle.py::test_uc_03_design_factors_output"
status: stub
---

# UC-03 - COBIT 2019 Design Factors Assessment

## Scenario

A regional commercial bank with $12B in assets seeks to assess its IT governance system using COBIT 2019 design factors. The bank operates a legacy core banking platform and has significant vendor concentration risk.

## Walk-Through

1. Apply COBIT 2019 design factors from `chunks/02-cobit-2019.md`. COBIT 2019 defines 11 design factors; this worked example weights the 5 most discriminating for a compliance-focused bank (Enterprise Strategy, Risk Profile, IT-Related Issues, Threat Landscape, Compliance Requirements) and reports them in `design_factors_applied`.
2. Map enterprise strategy to prioritized COBIT objectives.
3. Classify risk profile based on threat landscape and IT-related issues.
4. Produce prioritized governance objectives aligned with the bank's context, each with a rationale.

> The factor-to-objective weighting below is this skill's worked-example heuristic. The
> official COBIT 2019 Design Guide describes the tailoring method; it does not prescribe
> these numeric weights.

## Expected Output

```yaml
classification: "DESIGN_FACTORS_5"
design_factor_assessment:
  enterprise_strategy: "Compliance-focused"
  risk_profile:
    regulatory_risk: "High"
    technology_risk: "Moderate"
    vendor_risk: "High"
    threat_landscape: "Normal"
    compliance_requirements: "High"
  design_factors_applied:
    - "Enterprise Strategy"
    - "Risk Profile"
    - "IT-Related Issues"
    - "Threat Landscape"
    - "Compliance Requirements"
  prioritized_objectives:
    - objective: MEA03
      name: "Managed Compliance With External Requirements"
      priority: 1
      rationale: "High regulatory risk; compliance-focused strategy"
    - objective: APO12
      name: "Managed Risk"
      priority: 2
      rationale: "Moderate technology risk; legacy core banking"
    - objective: APO13
      name: "Managed Security"
      priority: 3
      rationale: "High regulatory risk demands security governance"
    - objective: DSS04
      name: "Managed Continuity"
      priority: 4
      rationale: "Moderate threat landscape; vendor concentration risk"
    - objective: APO10
      name: "Managed Vendors"
      priority: 5
      rationale: "High vendor concentration risk"
```
