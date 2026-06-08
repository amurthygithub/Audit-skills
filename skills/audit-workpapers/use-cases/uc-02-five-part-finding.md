---
uc_id: UC-02
title: "5-part finding (C-C-C-E-R) for AP cutoff control gap"
industries: [financial-services, public-sector]
frameworks: [PCAOB-AS-2201, PCAOB-AS-2201, PCAOB-AS-1215]
inputs:
  finding_id: 3
  wp_index: "C-4.2"
  severity: "Significant Deficiency"
  assertion: "Completeness (Accounts Payable)"
  condition: "12 of 75 invoices (16%) recorded in incorrect period; $342,500+$128,750 misstated across periods"
  criteria: "ASC 606/ASC 330 matching principle; company AP Policy AP-200; AS 2201 ICFR"
  cause: "Receiving dept not notifying AP of goods received in last 3 days of month; 3-way match relies on invoice date"
  effect: "Actual: expenses understated by $342,500 in 2024; overstated in 2025. Net understatement $213,750"
  recommendation: "Implement ERP automated cutoff; daily receiving reports through month-end; internal audit monitoring for 6 months"
procedure:
  - "chunks/05-finding-and-workflow.md -- Document condition using C-C-C-E-R format"
  - "chunks/05-finding-and-workflow.md -- Apply severity classification: significant deficiency"
  - "chunks/06-outputs-electronic-review.md -- Document in finding template"
expected_outputs:
  finding_document: "5-part C-C-C-E-R with severity, assertion, WP index"
  severity: "Significant Deficiency per AS 2201 Appendix A, AS 2201.62-.70"
  impact: "Net $213,750 P&L impact; potential material misstatement if systemic"
oracle:
  type: schema_match
  assertion: "Output must contain all 5 C-C-C-E-R parts, severity classification, and assertion tag"
data_refs:
  - "data/seeds/uc-02-input.json"
tests:
  - "tests/test_oracle.py::test_uc_02"
status: stub
---

# UC-02 -- 5-Part Finding for AP Cutoff Control Gap

## Scenario
XYZ Corp. FY 2025 audit. AP cutoff testing reveals 16% deviation rate. Finding classified as significant deficiency. Root cause: communication gap between receiving and AP at month-end. No automated cutoff controls.

## Walk-through
1. Document CONDITION: factual, specific, quantitative (12/75, amounts)
2. State CRITERIA: ASC 606/330, AP Policy AP-200, AS 2201 ICFR standards
3. Analyze CAUSE: receiving-to-AP notification gap, invoice-date-based matching
4. Quantify EFFECT: actual (actual dollars by period) and potential (systemic)
5. Formulate RECOMMENDATION: three specific actions with owners and timelines per chunks/05 template

## Expected Output
Finding document in chunks/06 template format with all 5 parts, severity=Significant Deficiency, WP index C-4.2.

## Variations
- If deviation rate > tolerable: increase severity or expand testing
- Government context: add compliance element and questioned costs per Yellow Book
