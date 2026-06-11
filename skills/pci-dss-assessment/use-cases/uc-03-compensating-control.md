---
uc_id: UC-03
title: "Solo QSA-support consultant validates a compensating control for a legacy POS that cannot meet a Req-8 auth control: all four Appendix-C worksheet elements present, worksheet complete (Meridian QSA-Support)"
industries: [retail-ecommerce, financial-services]
frameworks: [PCI-DSS-4.0.1]
inputs:
  org: "Meridian QSA-Support (solo) — fictional solo consultant supporting a 30-location franchise validating via SAQ D (data/seeds/uc-03-input.json)"
  constraint: "a legacy POS cannot enforce the defined Req-8 authentication control; legitimate_business_or_technical_constraint=true"
  proposed_compensating_control: "the four Appendix-C worksheet elements (constraints_documented, objective_of_original_requirement_stated, identified_risk_documented, controls_in_place_described) all true; controls = network isolation of legacy POS + MFA at the jump host + enhanced logging/alerting"
  as_of_date: "2026-06-11"
procedure:
  - "chunks/07-approaches-and-compensating-controls.md — Classify the situation: an existing defined requirement the entity cannot meet due to a legitimate constraint -> compensating control (Appendix B/C), NOT a customized approach (Appendix D)."
  - "chunks/07-approaches-and-compensating-controls.md — Check the Appendix-C worksheet for all four elements: constraints, objective of the original requirement, identified risk, and controls in place; the worksheet is complete iff all four are present."
  - "chunks/06-validation-roc-aoc.md — Position the QSA-support role: a solo consultant supports the assessment without over-claiming a QSA sign-off they do not hold."
  - "chunks/05-requirements-7-12.md — Anchor the underlying control: Req 8 identifies users and authenticates access to system components; the legacy POS is the system that cannot enforce the defined control."
  - "SKILL.md §1-§11 — apply the compensating-control-vs-customized-approach classification and the worksheet-completeness check."
expected_outputs:
  classification: "COMP_CONTROL_COMPLETE"
  control_type: "compensating_control"
  worksheet_elements_present: 4
  worksheet_complete: true
  missing_elements: []
oracle:
  - "control_type derived from the constraint flag: legitimate constraint against an existing requirement -> compensating_control (not customized_approach); without the constraint it would be customized_approach"
  - "worksheet_elements_present recomputed as the count of present Appendix-C elements == 4; missing_elements == []"
  - "worksheet_complete == true iff no element is missing; Appendix C has exactly four elements"
  - "classification == COMP_CONTROL_COMPLETE, derived from completeness"
  - "removing any one element flips worksheet_complete to false and the classification to COMP_CONTROL_INCOMPLETE"
data_refs:
  - data/seeds/uc-03-input.json
  - data/seeds/uc-03-expected.json
tests:
  - tests/test_pci_dss_assessment_oracle.py::test_uc_03_oracle
  - tests/test_pci_dss_assessment_metamorphic.py::test_uc03_element_order_invariance
  - tests/test_pci_dss_assessment_adversarial.py::test_uc03_incomplete_worksheet_flagged
  - tests/test_pci_dss_assessment_adversarial.py::test_uc03_no_constraint_is_customized_not_compensating
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-03 — Compensating control for a legacy POS: the Appendix-C worksheet (Meridian QSA-Support)

## §1 Context and persona

**Meridian QSA-Support** is a fictional **solo consultant** providing QSA-support to a **30-location franchise** that validates via **SAQ D**. The persona is the consultant who must do two things precisely: (1) decide whether a legacy-system gap is properly handled as a **compensating control** or a **customized approach** — they are different mechanisms — and (2) check that the proposed compensating control is documented to the **Appendix C** standard. The consultant supports the engagement; they do not over-claim a QSA sign-off they do not hold.

The seeds in `data/seeds/` are the tested fixture and this UC's source of truth; every result below is recomputed from them by `tests/test_pci_dss_assessment_oracle.py::test_uc_03_oracle`. No PAN appears in this example.

## §2 The constraint — and why it is a compensating control, not a customized approach

The franchise runs a **legacy POS that cannot enforce the defined Requirement 8 authentication control** (Req 8 — identify users and authenticate access to system components). The seed marks `legitimate_business_or_technical_constraint = true`.

This is the fork that v4 confuses most often:

| Mechanism | When it applies | Driver | Appendix |
|---|---|---|---|
| **Compensating control** | An **existing defined requirement** the entity **cannot meet** due to a **legitimate constraint** | Constraint-driven; must meet the **intent and rigor** of the original requirement | Appendix B (concept) + Appendix C (worksheet) |
| **Customized approach** | The entity chooses to meet the requirement's **objective by a different method** | Design choice; requires a **Targeted Risk Analysis (TRA)**; **not** constraint-driven | Appendix D (concept) + Appendix E (templates) |

Because Meridian's situation is a **legitimate constraint against an existing defined requirement**, the correct mechanism is a **compensating control** — `control_type = compensating_control`. The classification is constraint-driven: remove the legitimate constraint and the same facts would instead be a **customized approach** (the adversarial test `test_uc03_no_constraint_is_customized_not_compensating` exercises that flip). This is the same distinction UC-02 makes from the customized-approach side.

## §3 The Appendix-C worksheet — all four elements present

A compensating control is only valid if it is documented on the **Compensating Controls Worksheet (Appendix C)** with all four elements present. The proposed control carries every one:

| # | Appendix-C element | Seed field | Present |
|---|---|---|---|
| 1 | Constraints (why the defined requirement cannot be met) | `constraints_documented` | yes |
| 2 | Objective of the original requirement | `objective_of_original_requirement_stated` | yes |
| 3 | Identified risk (introduced by the constraint) | `identified_risk_documented` | yes |
| 4 | Controls in place (how the compensating control meets intent and rigor) | `controls_in_place_described` | yes |

The compensating controls themselves: **network isolation of the legacy POS + MFA at the jump host + enhanced logging/alerting** — together intended to meet the intent and rigor of the defined Req-8 control the legacy POS cannot enforce.

**All four elements present → worksheet complete.** `worksheet_elements_present = 4`, `missing_elements = []`, `worksheet_complete = true`, `classification = COMP_CONTROL_COMPLETE`.

## §4 Oracle — completeness and control-type are derivable

`tests/test_pci_dss_assessment_oracle.py::test_uc_03_oracle` recomputes both results independently from the seed and asserts the stub agrees and equals the expected seed:

- `control_type` derived from the constraint flag: a legitimate constraint against an existing requirement → `compensating_control` (not `customized_approach`).
- `worksheet_elements_present` recomputed as the count of present Appendix-C elements == 4; `missing_elements` == `[]`.
- `worksheet_complete` == true iff no element is missing; Appendix C has **exactly four** elements.
- `classification` == `COMP_CONTROL_COMPLETE`, derived from completeness.

Metamorphic: evaluating the four elements does not depend on dict key order (`test_uc03_element_order_invariance`). Adversarial: setting any one element to false (e.g. `identified_risk_documented`) flips `worksheet_complete` to false and the classification to `COMP_CONTROL_INCOMPLETE` (`test_uc03_incomplete_worksheet_flagged`); removing the legitimate constraint reclassifies the mechanism as a customized approach (`test_uc03_no_constraint_is_customized_not_compensating`).

## §5 Anti-hallucination

- **Meridian QSA-Support is fictional**; the seeds are the tested fixture and this UC's source of truth.
- **Compensating control ≠ customized approach.** A compensating control (Appendix B/C) is constraint-driven against an existing requirement and meets its intent and rigor via the four-element worksheet; a customized approach (Appendix D/E) is an objective-met-differently design choice requiring a TRA and is not constraint-driven [PCI-SSC-Document-Library §AppendixC].
- **The worksheet is complete only with all four elements** — constraints, objective, risk, controls in place; a missing element is an incomplete worksheet, never a silent pass.
- **QSA-support is a support role** — a solo consultant supports the assessment without claiming a QSA's validation authority; the validation path here is **SAQ D** for the franchise.
- **No PAN is shown** — the legacy-POS constraint is modeled as an authentication-enforcement fact, never with card data.
- **Future-dated v4.0.1 requirements are in force**; nothing here is presented as optional [PCI-SSC-Blog-v401 §v4.0.1].
