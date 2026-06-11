---
uc_id: UC-02
title: "Full-ROC retail merchant scopes a 14-system inventory to 10 in-scope / 4 out-of-scope and routes one customized-approach request with a TRA to accepted (Ironvale Retail)"
industries: [retail-ecommerce, financial-services]
frameworks: [PCI-DSS-4.0.1]
inputs:
  org: "Ironvale Retail — fictional L1 merchant (L1 is brand-defined), ~8,000,000 annual transactions, validating via full ROC (data/seeds/uc-02-input.json)"
  system_inventory: "14 systems each tagged cde / connected / out — 5 CDE, 5 connected, 4 out-of-scope"
  customized_approach_requests: "one request: requirement 8.3.6 (password length/complexity) with targeted_risk_analysis_present=true"
  as_of_date: "2026-06-11"
procedure:
  - "chunks/02-scoping-and-segmentation.md — Classify every system: in-scope = CDE + connected/security-impacting; out = segmented and validated out of scope. Scoping is the highest-leverage decision in the assessment."
  - "chunks/02-scoping-and-segmentation.md — Show the segmentation effect: re-tagging a connected system to out-of-scope lowers the in-scope count deterministically (scope reduction is the payoff of segmentation)."
  - "chunks/06-validation-roc-aoc.md — Confirm the full-ROC path for a large merchant and the assessor's scope-confirmation step (sampling over the in-scope population)."
  - "chunks/07-approaches-and-compensating-controls.md — Route the 8.3.6 request through the defined-vs-customized decision: a customized approach (Appendix D) requires a documented Targeted Risk Analysis (TRA); with a TRA present it is accepted."
  - "SKILL.md §1-§11 — apply the scope-determination logic and the defined-vs-customized routing per flagged requirement."
expected_outputs:
  classification: "ROC_IN_SCOPE_10"
  total_systems: 14
  cde_systems: 5
  in_scope_systems: 10
  out_of_scope_systems: 4
  customized_approach_accepted: ["8.3.6"]
  customized_approach_rejected_no_tra: []
oracle:
  - "in_scope_systems recomputed independently from the seed tags (count of cde + connected) == 10 == stub == expected seed; cde_systems == 5"
  - "footing invariant: in_scope_systems + out_of_scope_systems == total_systems (10 + 4 == 14)"
  - "classification == ROC_IN_SCOPE_10, derived from the in-scope count"
  - "8.3.6 is accepted because targeted_risk_analysis_present is true; a request without a TRA lands in customized_approach_rejected_no_tra"
  - "segmentation monotonicity: re-tagging one connected system to out-of-scope drops the in-scope count by exactly 1 (can only lower it)"
data_refs:
  - data/seeds/uc-02-input.json
  - data/seeds/uc-02-expected.json
tests:
  - tests/test_pci_dss_assessment_oracle.py::test_uc_02_oracle
  - tests/test_pci_dss_assessment_metamorphic.py::test_uc02_inventory_order_invariance
  - tests/test_pci_dss_assessment_metamorphic.py::test_uc02_segmentation_monotonicity
  - tests/test_pci_dss_assessment_adversarial.py::test_uc02_empty_inventory_zero_scope
  - tests/test_pci_dss_assessment_adversarial.py::test_uc02_customized_without_tra_rejected
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-02 — Full ROC: scoping, segmentation, and a customized-approach request (Ironvale Retail)

## §1 Context and persona

**Ironvale Retail** is a fictional **L1 merchant** — and "L1" is a **brand-defined** level, not a PCI SSC designation; this UC labels it as such everywhere it appears. With roughly 8,000,000 card transactions a year and a card-present plus e-commerce footprint, Ironvale validates via a **full Report on Compliance (ROC)**. The persona is the retail security manager (with QSA support) doing the two things that govern a ROC's cost and credibility: **getting the scope right**, and **routing any requirement that will be met by a customized approach** through the correct mechanism.

The seeds in `data/seeds/` are the tested fixture and this UC's source of truth; every number below is recomputed from them by `tests/test_pci_dss_assessment_oracle.py::test_uc_02_oracle`. No PAN appears in this example.

## §2 Scope determination — 14 systems → 10 in-scope / 4 out-of-scope

Scoping is the **highest-leverage decision** in any PCI DSS assessment: everything in scope must satisfy the applicable requirements, and everything legitimately out of scope is work avoided. **House scope convention (labeled):** in-scope = **CDE** systems + **connected/security-impacting** systems; **out** = systems that are **segmented and validated** out of scope.

Ironvale's 14-system inventory carries these tags:

| Scope tag | Systems | Count |
|---|---|---|
| CDE | POS-terminals, payment-switch, card-vault, store-controller, e-comm-web | 5 |
| Connected / security-impacting | auth-AD, siem, jump-host, patch-server, backup | 5 |
| Out of scope (segmented & validated) | corp-email, hr-system, guest-wifi, dev-sandbox | 4 |

**In-scope = CDE (5) + connected (5) = 10. Out of scope = 4. Footing: 10 + 4 = 14.**

The classification is **ROC_IN_SCOPE_10**, derived from the in-scope count. The 5 connected systems are in scope precisely because they can affect the security of the CDE (the authentication directory, the SIEM, the administrative jump host, the patch source, the backup target) even though they are not themselves part of the CDE.

## §3 Segmentation as scope reduction

Segmentation is the lever that moves a system from in-scope to out-of-scope, and the effect is **deterministic and monotonic**: re-tagging one `connected` system to `out` lowers the in-scope count by exactly 1 (and never raises it). For example, if the `backup` target were fully isolated from the CDE and connected systems and validated out of scope, Ironvale's in-scope count would drop from 10 to 9. This is the entire economic argument for segmentation — every system you can defensibly segment out is requirements work you do not have to perform or evidence. The metamorphic test asserts this monotonicity directly.

## §4 The customized-approach request — 8.3.6 with a TRA → accepted

Ironvale has one requirement it intends to meet by a **customized approach** rather than the defined approach: **requirement 8.3.6** (password length/complexity), where a passphrase policy plus adaptive lockout is argued to meet or exceed the stated objective.

**A customized approach (Appendix D) requires a documented Targeted Risk Analysis (TRA).** The seed's request carries `targeted_risk_analysis_present = true`, so it is **accepted**:

- `customized_approach_accepted = ["8.3.6"]`
- `customized_approach_rejected_no_tra = []`

Had the TRA been absent, 8.3.6 would have landed in `customized_approach_rejected_no_tra` instead — the adversarial test `test_uc02_customized_without_tra_rejected` exercises exactly that path. The customized approach is **distinct from a compensating control** (the Appendix B/C mechanism in UC-03): the customized approach meets the requirement's *objective* by a different method with a TRA and is not constraint-driven; a compensating control addresses an existing requirement an entity *cannot* meet due to a legitimate constraint.

## §5 Oracle — every number is derivable

`tests/test_pci_dss_assessment_oracle.py::test_uc_02_oracle` recomputes each figure independently from the seed tags and asserts the stub agrees and equals the expected seed:

- `cde_systems` recomputed as the count of `cde` tags == 5.
- `in_scope_systems` recomputed as the count of `cde` + `connected` tags == 10; `out_of_scope_systems` == 14 − 10 == 4.
- Footing invariant: `in_scope_systems + out_of_scope_systems == total_systems` (10 + 4 == 14).
- `classification` == `ROC_IN_SCOPE_10`, derived from the in-scope count.
- `customized_approach_accepted` == `["8.3.6"]` because the TRA is present; the rejected-no-TRA list is empty.

Metamorphic: reversing the inventory order changes nothing (`test_uc02_inventory_order_invariance`); re-tagging one connected system out of scope drops the in-scope count by exactly 1 and never raises it (`test_uc02_segmentation_monotonicity`). Adversarial: an empty inventory yields zero in-scope systems and `ROC_IN_SCOPE_0` (`test_uc02_empty_inventory_zero_scope`); a customized-approach request with no TRA is rejected (`test_uc02_customized_without_tra_rejected`).

## §6 Anti-hallucination

- **Ironvale Retail is fictional**; the seeds are the tested fixture and this UC's source of truth.
- **"L1" is a brand-defined merchant level** — payment brands and acquirers set validation levels and thresholds, not PCI DSS; this UC never asserts a level threshold as an SSC fact.
- **The scope convention is a labeled house heuristic** — the in-scope/connected/out-of-scope categories apply the standard's scoping principles; the precise scoping rules come from the standard [PCI-SSC-Document-Library §scoping].
- **Customized approach ≠ compensating control.** A customized approach (Appendix D) is objective-met-differently with a TRA and is not constraint-driven; a compensating control (Appendix B/C) is constraint-driven against an existing requirement (UC-03). Blurring them is the single most common v4 error.
- **No PAN is shown** — PAN is modeled as a CDE-scoping fact, never reproduced.
- **Future-dated v4.0.1 requirements are in force**; nothing here is presented as optional [PCI-SSC-Blog-v401 §v4.0.1].
