---
uc_id: UC-03
title: "Audit risk model TD calculation for revenue substantive testing"
industries: [financial-services, saas-technology]
frameworks: [PCAOB-AS-2315, PCAOB-AS-2110, PCAOB-AS-1101]
inputs:
  allowable_audit_risk: "5%"
  inherent_risk: "80% (complex revenue recognition)"
  control_risk: "60% (moderate)"
  analytical_procedures_risk: "50%"
procedure:
  - "chunks/04-risk-and-opinion.md -- Compute TD = AR / (IR x CR x AP)"
  - "chunks/04-risk-and-opinion.md -- Map TD to RIA for MUS sample size selection"
expected_outputs:
  td_result: "20.8% (TD = 0.05 / (0.80 x 0.60 x 0.50))"
  sample_size_implication: "TD ~21% -> Moderate RIA (10%), RF 2.31"
oracle:
  type: exact_match
  assertion: "TD = 20.8%; sample size implication moderate-large"
data_refs:
  - "data/seeds/uc-03-input.json"
tests:
  - "tests/test_oracle.py::test_uc_03"
status: stub
---

# UC-03 -- Audit Risk Model TD Calculation for Revenue Testing

## Scenario
XYZ Corp. FY 2025 audit. Complex revenue recognition (multiple-element ASC 606). AR=5%, IR=80%, CR=60%, AP=50%.

## Walk-through
1. Compute TD = AR / (IR x CR x AP) = 0.05 / 0.24 = 20.8%.
2. Map to sample size: 20.8% -> moderate RIA (10%), moderate-large sample.

## Expected Output
TD with inputs shown. RIA mapping to sample size implication.

## Variations
- Lower CR -> lower TD -> smaller sample.
- Higher IR -> higher TD -> larger sample.
