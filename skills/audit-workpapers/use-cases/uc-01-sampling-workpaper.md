---
uc_id: UC-01
title: "MUS sampling workpaper for accounts receivable"
industries: [financial-services]
frameworks: [PCAOB-AS-2315, PCAOB-AS-1215, PCAOB-AS-1105]
inputs:
  population: "Accounts receivable ledger as of 12/31/2025"
  population_book_value: "$12,500,000"
  tolerable_misstatement: "$500,000"
  risk_of_incorrect_acceptance: "5%"
  expected_overstatements: 0
procedure:
  - "chunks/03-sampling.md -- Determine sample size via MUS formula n = (BV x RF) / TM"
  - "chunks/03-sampling.md -- Select items using systematic PPS with random start"
  - "chunks/03-sampling.md -- Evaluate using ULM = BP + sum(IA)"
  - "chunks/06-outputs-electronic-review.md -- Document in sampling workpaper template"
expected_outputs:
  sampling_interval: "$166,667 (TM $500,000 / RF 3.00)"
  sample_size: "75 items (($12,500,000 x 3.00) / $500,000)"
  basic_precision: "$500,001"
  upper_limit_conclusion: "Compare ULM to TM; determine if materially misstated"
oracle:
  type: exact_match
  assertion: "Sample size = 75, Sampling interval = $166,667 (rounded), BP = $500,001"
data_refs:
  - "data/seeds/uc-01-input.json"
tests:
  - "tests/test_oracle.py::test_uc_01"
status: draft
---

# UC-01 -- MUS Sampling Workpaper for Accounts Receivable

## Scenario
XYZ Corp. FY 2025 audit. AR population = $12,500,000. Auditor applies MUS at 5% RIA, 0 expected overstatements (RF=3.00), TM=$500,000.

## Walk-through
1. Calculate SI = TM/RF = $500,000/3.00 = $166,667
2. Sample size n = (BV x RF)/TM = ($12,500,000 x 3.00)/$500,000 = 75
3. Select 75 items via systematic PPS; all items > $166,667 auto-selected
4. Test each item; record misstatements
5. Calculate ULM = BP + sum(IA). Compare to TM.
6. Document conclusion in sampling workpaper per chunks/06 template

## Expected Output
Sampling workpaper (I-series) with full sections A-F per the template in chunks/06-outputs-electronic-review.md.

## Variations
- If misstatements found, compute tainting percentages and incremental allowances
- If ULM > TM, consider expanded sample or management adjustments
- Dual-purpose: add attribute testing of AR-related controls
