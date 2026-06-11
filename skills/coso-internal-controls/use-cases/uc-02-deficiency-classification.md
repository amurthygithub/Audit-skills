---
uc_id: UC-02
title: "Classify an improper-access ITGC deficiency — the occurrence-assertion compensating-control test"
industries: [financial-services, saas-technology]
frameworks: [COSO-ICIF-2013, PCAOB-AS-2201]
inputs:
  deficiency: "Terminated employees retain ERP access avg 45 days; no quarterly access review; no automated de-provisioning (ITGC, logical access)."
  assertion_at_risk: "occurrence (improper access → unauthorized but recorded transactions)"
  affected_systems: ["ERP"]
  compensating_controls_candidates: ["Bank reconciliation (monthly)", "Payroll reconciliation (monthly)", "Budget variance analysis (monthly)"]
  authority_of_retained_access: "can create vendors, approve payments with no enforced ceiling, change payroll"
  lookback: "not performed"
  preliminary_classification: "Significant Deficiency (the conclusion this UC overturns)"
procedure:
  - "chunks/05-deficiency-classification.md: Steps 1-3 — deficiency exists; reasonable possibility; magnitude from the AUTHORITY of the retained access (not a per-transaction cap)"
  - "chunks/07-compensating-updates-cross.md: the two-part compensating-control test — (1) does it address the ASSERTION AT RISK? (2) is it independent of the deficiency (IPE not drawn from the affected system)?"
  - "chunks/07-compensating-updates-cross.md: ITGC-pervasiveness step — every app control and IPE relying on the ERP, including the reconciliations themselves"
  - "chunks/05-deficiency-classification.md: the lookback procedure gates the conclusion; absent it, the rebuttable presumption for an unmitigated pervasive ITGC is a material weakness"
expected_outputs:
  classification: "Material Weakness"
  assertion_at_risk: "occurrence"
  qualifying_compensating_controls: []
  itgc_pervasive: true
  magnitude: {driver: "authority_of_retained_access", material: true, unbounded: true}
  compensating_control_analysis: "each reconciliation fails BOTH tests: addresses completeness/accuracy not occurrence, and draws IPE from the affected ERP"
  lookback: {performed: false, rules_out_occurrence: false}
oracle:
  type: derivability
  assertion: |
    tests/test_coso_internal_controls_oracle.py::test_uc_02_oracle recomputes the
    classification from the seed: a compensating control qualifies only if it addresses
    the assertion at risk (occurrence) AND is independent of the affected system; none of
    the three reconciliations qualify (wrong assertion + ERP-IPE-impaired) → zero qualifying
    controls; pervasive ITGC + authority-driven unbounded magnitude + no lookback →
    Material Weakness. The metamorphic test proves an affirmative lookback plus a qualifying
    occurrence-control moves the conclusion off MW (the result is fact-driven, not hardcoded).
data_refs: ["data/seeds/uc-02-input.json"]
tests:
  - "tests/test_coso_internal_controls_oracle.py::test_uc_02_oracle"
  - "tests/test_coso_internal_controls_oracle.py::test_uc_02_lookback_and_qualifying_control_can_lower_severity"
status: active
---

# UC-02: Improper-access deficiency — the occurrence-assertion compensating-control test

## Scenario

A mid-cap filer finds that terminated employees retain ERP access for ~45 days with no
quarterly review and no automated de-provisioning. No misstatement has been *detected*. Bank
and payroll reconciliations operate monthly. The preliminary view was **Significant
Deficiency** — the reconciliations were assumed "precise enough." This UC shows why that
conclusion is unsound and what the correct analysis yields.

## The error this UC corrects

Improper logical access threatens the **occurrence** (authorization/validity) assertion: a
terminated or malicious user with retained access can process an **unauthorized but recorded**
transaction — a fictitious-vendor payment, an unauthorized payroll change. A reconciliation
addresses **completeness and accuracy** — it catches *unrecorded* or *mismatched* items. A
fraudulent transaction that is recorded in both the sub-ledger and the bank statement
**reconciles cleanly**; the rec never flags it. So the reconciliations do not address the
assertion at risk, and rating their precision "sufficient" answers the wrong question.

## Walk-through (the corrected analysis)

**Step 1 — Deficiency exists.** Design defect in provisioning and monitoring (ITGC, logical
access).

**Step 2 — Reasonable possibility.** Improper access with no detective review → yes.

**Step 3 — Magnitude from authority, not transaction size.** The exposure is whatever the
retained access can *authorize*: vendor creation (fictitious-vendor scheme → unbounded), payment
approval with no enforced ceiling, payroll changes. Magnitude is **material and effectively
unbounded** — not a "$5K × 120 terminations" cap.

**Step 4 — The two-part compensating-control test.** A candidate mitigates only if it:
1. **addresses the assertion at risk** (occurrence), and
2. **is independent of the deficiency** — it must not draw its information (IPE) from the same
   system whose access is uncontrolled.

| Candidate | Addresses occurrence? | Independent of ERP? | Qualifies? |
|---|---|---|---|
| Bank reconciliation | No (completeness/accuracy) | No — IPE from the ERP | **No** |
| Payroll reconciliation | No (completeness/accuracy) | No — IPE from the ERP | **No** |
| Budget variance analysis | No (completeness, low precision) | No — IPE from the ERP | **No** |

**Zero qualifying compensating controls.** Each reconciliation fails *both* tests.

**Step 5 — ITGC pervasiveness.** Logical-access ITGCs are pervasive: they affect the
reliability of every application control and every piece of IPE on the system — including the
reconciliations themselves, which consume ERP-produced data. The deficiency undermines its own
proposed compensating controls.

**Step 6 — Lookback gates the conclusion.** Before concluding, perform the lookback: review all
transactions initiated or approved by the terminated users during their retained-access window,
focused on occurrence/authorization and independent of the ERP's automated controls. It was not
performed here.

**Conclusion: Material Weakness.** Unmitigated pervasive ITGC, material (authority-driven)
magnitude, reasonable possibility, no lookback ruling out improper activity — the rebuttable
presumption is a material weakness (the Partner independently put MW on the table; the 3PAO
flagged the original SD conclusion as security-unsound).

## What WOULD mitigate (recommended procedures)

- An **occurrence-focused lookback** of terminated-user transactions — the evidence that gates
  the conclusion. If it affirmatively finds no improper activity *and* a qualifying
  occurrence-relevant control exists, severity can come down (proven by the metamorphic test).
- **Independent re-authorization / SoD review** of vendor and payroll changes in the window,
  sourced independently of the ERP.

## Remediation

Automated de-provisioning on termination + quarterly access certification (owner: IT Security
Manager).
