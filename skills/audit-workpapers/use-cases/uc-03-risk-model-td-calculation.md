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
  - "chunks/04-risk-and-opinion.md -- TD is the RIA (AS 2315); size the MUS sample with the RF at the largest tabulated RIA <= TD"
expected_outputs:
  td_result: "20.8% (TD = 0.05 / (0.80 x 0.60 x 0.50))"
  sample_size_implication: "TD ~21% IS the allowable RIA (AS 2315); RF 1.61 -> moderate-small sample"
oracle:
  type: exact_match
  assertion: "TD = 20.8%; TD is the RIA per AS 2315; RF 1.61; moderate-small extent"
data_refs:
  - "data/seeds/uc-03-input.json"
tests:
  - "tests/test_audit_workpapers_oracle.py::test_uc_03_oracle"
status: stub
---

# UC-03 -- Audit Risk Model TD Calculation for Revenue Testing

## Scenario
XYZ Corp. FY 2025 audit. Complex revenue recognition (multiple-element ASC 606). AR=5%, IR=80%, CR=60%, AP=50%.

## Walk-through
1. Compute TD = AR / (IR x CR x AP) = 0.05 / 0.24 = 20.8%.
2. Size the sample: TD 20.8% is the allowable RIA itself (AS 2315) -> RF 1.61 (20% row) -> moderate-small substantive sample.

## Expected Output
TD with inputs shown. TD used directly as the RIA (no second mapping — that double-counts conservatism).

## Variations
- Lower CR -> lower TD -> smaller sample.
- Higher IR -> higher TD -> larger sample.
