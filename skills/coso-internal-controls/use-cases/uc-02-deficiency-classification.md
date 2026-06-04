---
uc_id: UC-02
title: "Classify a control gap as MW, SD, or D with compensating control evaluation"
industries: [financial-services, saas-technology]
frameworks: [COSO-ICIF-2013, PCAOB-AS-2201]
inputs:
  deficiency_description: "IT access provisioning for ERP system not properly controlled. Terminated employees retain access avg 45 days. No quarterly access review. Affects expenditure and payroll."
  affected_accounts: ["Operating Expenses", "Payroll Expense", "Accounts Payable"]
  affected_assertions: ["Existence", "Completeness"]
  compensating_controls_candidates: ["Bank reconciliation (monthly, precise)", "Payroll reconciliation (monthly, precise)", "Budget variance analysis (monthly, low precision)"]
  preliminary_classification: "Significant Deficiency"
procedure:
  - "chunks/05-deficiency-classification.md: Step 1 - Confirm deficiency exists"
  - "chunks/05-deficiency-classification.md: Step 2 - Assess reasonable possibility of misstatement"
  - "chunks/05-deficiency-classification.md: Step 3 - Assess magnitude of potential misstatement"
  - "chunks/07-compensating-updates-cross.md: Evaluate compensating controls"
  - "chunks/05-deficiency-classification.md: Check MW indicators (AS 2201.69)"
expected_outputs:
  classification: "Significant Deficiency"
  basis: "Reasonable possibility of misstatement exists, but compensating controls (bank rec, payroll rec) are precise enough to prevent material misstatement."
  compensating_control_analysis:
    - {control: "Bank reconciliation", effective: true, precision: "sufficient"}
    - {control: "Payroll reconciliation", effective: true, precision: "sufficient"}
    - {control: "Budget variance analysis", effective: true, precision: "insufficient"}
  remediation: {action: "Implement quarterly access review and automated de-provisioning", owner: "IT Security Manager"}
oracle:
  type: schema_match
  assertion: "Classification follows 3-step decision tree, compensating controls evaluated per 6-step procedure, MW indicators checked"
data_refs: []
tests: ["tests/test_lint.py"]
status: stub
---

# UC-02: Deficiency Classification

## Scenario

Mid-cap fintech/bank identifies IT access deficiency: terminated employees retain ERP access 45 days, no quarterly review. No actual misstatement detected. Compensating controls exist.

## Walk-through

Step 1: Deficiency exists (design defect in provisioning and monitoring).
Step 2: Reasonable possibility of misstatement (terminated users could process unauthorized transactions).
Step 3: Magnitude assessment: max single tx $5K, 120 terminations/year, potential $50K-$200K. But bank rec and payroll rec detect material misstatements. Classification: Significant Deficiency.
Step 4: Compensating controls: bank rec (precise, effective), payroll rec (precise, effective), budget variance (not precise enough).
Step 5: No AS 2201.69 MW indicators present.
Final: Significant Deficiency. Communicate to audit committee in writing. Remediate with quarterly access review.
