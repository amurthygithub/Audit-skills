---
uc_id: UC-02
title: "Write a 5-part finding (C-C-C-E-R) and a management response — company-side or auditor-side"
industries: [financial-services, public-sector, saas-technology]
frameworks: [PCAOB-AS-2201, PCAOB-AS-1215, GAGAS-2024]
inputs:
  finding_id: 3
  wp_index: "C-4.2"
  severity: "Significant Deficiency"
  cccer: "the five parts (condition / criteria / cause / effect / recommendation) the preparer fills — see data/seeds/uc-02-input.json"
  management_response: "owner, remediation_steps, target_date, operating_effectiveness_evidence, retest_window"
procedure:
  - "chunks/05-finding-and-workflow.md — write each C-C-C-E-R part from the facts (the skill checks all five are present)"
  - "chunks/06-outputs-electronic-review.md — place the finding in the workpaper template at the WP index"
  - "chunks/05-finding-and-workflow.md — draft the management response / remediation plan; the skill checks the 5 required fields are present"
expected_outputs:
  finding: "the 5 C-C-C-E-R parts (taken from the seed), severity, assertion, WP index"
  ccc_er_complete: true
  management_response_complete: true
  management_response_missing: []
  classification: "SIGNIFICANT_DEFICIENCY"
oracle:
  type: derivability
  assertion: |
    tests/test_audit_workpapers_oracle.py::test_uc_02_oracle recomputes from the seed:
    every C-C-C-E-R part equals the seed value (the preparer's words, not a hardcoded
    finding); ccc_er_complete is the AND of the five parts being non-empty; the
    management-response completeness is the AND of the five required fields. The
    incomplete-draft test proves a missing part / field is reported, not papered over.
data_refs: ["data/seeds/uc-02-input.json"]
tests:
  - "tests/test_audit_workpapers_oracle.py::test_uc_02_oracle"
  - "tests/test_audit_workpapers_oracle.py::test_uc_02_incomplete_finding_and_response_flagged"
status: active
---

# UC-02 — Write a 5-part finding and a management response

This UC works from **either side**: an auditor documenting a finding, or a **company-side
preparer** (controller, internal audit, process owner) writing the finding and the management
response. The skill does not hand you a pre-classified finding — you supply the facts, and it
checks that both the finding and the response are **complete** before they go in the file.

## A — A fully-written example finding (AP cutoff, Significant Deficiency)

> **Finding 3 — Accounts Payable cutoff (WP C-4.2). Severity: Significant Deficiency.
> Assertion: Completeness (Accounts Payable).**
>
> **Condition.** In testing 75 invoices around the FY2025 year-end cutoff, 12 (16%) were
> recorded in the incorrect period — $342,500 of expense that belonged in 2024 was recorded
> in 2025, and $128,750 the reverse.
>
> **Criteria.** Accrual-basis GAAP requires period-end liabilities and expenses to be recorded
> in the period the goods/services are received; company AP Policy AP-200 and the entity's
> AS 2201 ICFR require a month-end cutoff control. *(Note: the criteria are accrual/cutoff
> GAAP and AP-200 — not revenue-recognition (ASC 606); cite the standard that actually governs
> the assertion at issue.)*
>
> **Cause.** The receiving department does not notify AP of goods received in the last three
> days of the month, and the 3-way match keys on invoice date rather than receipt date, so
> late-month receipts post to the next period.
>
> **Effect.** 2024 expenses understated by $342,500 and 2025 overstated; net understatement of
> $213,750. Potential for material misstatement if the pattern is systemic across periods.
>
> **Recommendation.** Implement an ERP automated cutoff; produce daily receiving reports
> through month-end; internal-audit monitoring for six months to confirm operating
> effectiveness.

## B — Blank fill-in template

```
Finding #___    WP index: ____    Severity: [Deficiency | Significant Deficiency | Material Weakness]
Assertion(s): ____________________________________________

Condition (what is — factual, quantified): ____________________________________________
Criteria (what should be — cite the standard/policy that governs THIS assertion): ______
Cause (why the difference exists — the control gap, not the symptom): _________________
Effect (so what — actual $ and potential if systemic): _______________________________
Recommendation (what to do — specific, ownerable actions): ___________________________
```

The skill reports `ccc_er_complete: false` and lists `finding_missing_parts` until all five
are filled — so a preparer knows exactly what is still missing.

## C — Management response / remediation template

The response is the company's, not the auditor's. Five fields are required for it to be
complete (the skill checks each):

```
Owner: ______________________________  (accountable person/role)
Remediation steps: __________________  (the specific control changes)
Target date: ________________________  (YYYY-MM-DD)
Operating-effectiveness evidence: ____  (what will demonstrate the fix worked)
Retest window: ______________________  (when the auditor/IA will re-test)
```

Worked: *Owner = VP Controller; steps = configure the ERP receiving-to-AP interface, enable
the daily receiving report, add a month-end cutoff control; target = 2025-09-30; evidence =
two months of cutoff-control operation plus a sample retest; retest window = Q4 2025.* The
skill reports `management_response_complete: true` and `management_response_missing: []`.

## D — Company-side walkthrough

1. **Gather the facts** (test results, amounts, the control that failed) and write the five
   C-C-C-E-R parts in template B — plain, quantified, no conclusions in the Condition.
2. **Check completeness** — the skill flags any empty part; do not file a finding missing the
   Cause or a quantified Effect.
3. **Classify severity** with `chunks/05` (Deficiency / SD / MW) — the C-C-C-E-R facts feed it.
4. **Write the management response** in template C; the skill flags any missing field. A
   response without a retest window or an owner is not yet actionable.
5. **Place it** at the WP index in the `chunks/06` workpaper template, cross-referenced to the
   test workpaper.

## Variations

- **Deviation rate > tolerable** → revisit severity or expand testing (`chunks/05`).
- **Government engagement** → add the compliance element and questioned costs (Yellow Book /
  2 CFR 200.516); the GAGAS report wrapper is a separate ticket (SOX-672).
