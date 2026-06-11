---
chunk_id: 07-approaches-and-compensating-controls
parent_skill: pci-dss-assessment
topic: "Defined vs customized approach (Appendix D/E; TRA); requirements with no customized option; compensating controls (Appendix B/C) and the six worksheet elements; how customized and compensating differ and when to use each"
load_when: "user asks about the customized approach, defined approach, Targeted Risk Analysis, compensating controls, the compensating-controls worksheet, or whether a control can be met differently or not at all"
---

# Chunk 07 — Approaches and Compensating Controls

v4 offers two ways to **meet** a requirement (defined, customized) and one fallback for a requirement an entity **cannot meet** (compensating control). These three are distinct, and conflating the customized approach with compensating controls is the single most common v4 error this skill guards against.

## 1. Defined approach

Meet the requirement **as written** and validate against its stated **testing procedures**. This is the default and the only path most assessments use. No extra analysis is required beyond the testing procedures themselves.

## 2. Customized approach (Appendix D / E)

The customized approach lets an entity meet a requirement's **stated objective** by a **different method** than the defined requirement specifies — for entities with mature risk management that want to implement controls suited to their environment.

- It is **by design**, not a fallback: the entity chooses to meet the objective differently.
- It **requires a Targeted Risk Analysis (TRA)** (anchored by Req 12.3) documenting how the alternative control meets or exceeds the objective.
- The assessor derives and applies **customized testing procedures** for the entity's control.
- **Some requirements have no customized-approach option** — those must be met by the defined approach (or, if genuinely unattainable, a compensating control).
- Appendix E provides sample templates (controls matrix; the TRA).

**Validation gate:** a customized approach without a documented TRA is **not** acceptable — the TRA is mandatory, not optional. (In the UC-02 shape, requirement 8.3.6 is accepted as a customized approach **because** a TRA is present; a request lacking a TRA is rejected.)

## 3. Compensating controls (Appendix B / C)

A compensating control is a **fallback** for an **existing defined requirement** that an entity **cannot meet as stated** due to a **legitimate business or technical constraint**, where the entity instead implements controls that **sufficiently mitigate the risk**.

The **compensating-controls worksheet (Appendix C)** has **six "Information Required" rows**:

1. **Constraints** — the legitimate business/technical constraint preventing the defined requirement.
2. **Definition of Compensating Controls** — the compensating controls themselves and how they meet the requirement's intent/rigor.
3. **Objective** — the objective of the original requirement.
4. **Identified Risk** — the additional risk posed by not meeting the defined requirement.
5. **Validation of Compensating Controls** — how the compensating controls were validated and tested.
6. **Maintenance** — how the compensating controls are maintained over time.

A worksheet is **complete iff all six rows are present**. Compensating controls must go **above and beyond** the defined requirement and address the additional risk the constraint introduces.

## 4. Customized vs compensating — the contrast

| | **Customized approach** (App D/E) | **Compensating control** (App B/C) |
|---|---|---|
| Why used | Meet the objective a **better/different** way, by design | Entity **cannot meet** an existing defined requirement |
| Trigger | Choice + mature risk management | A **legitimate constraint** |
| Required analysis | **Targeted Risk Analysis (TRA)** | **Six-row worksheet** |
| Relationship to the requirement | Replaces the defined method for that requirement | Sits alongside an unmet **defined** requirement |
| Constraint-driven? | **No** | **Yes** |

**Classification rule (engagement-decision logic):** if a control exists because a **legitimate constraint** blocks the **existing defined requirement** → it is a **compensating control**. If the entity instead chooses to **meet the objective by a different method** (no blocking constraint) → it is a **customized approach**. The two are not interchangeable, and an entity does not file both for the same control.

## 5. Procedure — choosing and documenting an approach

1. Identify the requirement and whether the entity will/can meet it as written → **defined**.
2. If the entity wants to meet the objective differently and the requirement **permits** customization → **customized**: produce a **TRA** and (with the assessor) customized testing procedures.
3. If the entity **cannot** meet the defined requirement due to a **legitimate constraint** → **compensating control**: complete the **six-row worksheet** and show the controls exceed the defined requirement.
4. Record the choice per requirement in the ROC (`chunks/06`).

## 6. Output templates

**Customized-approach record:** `requirement`, `objective`, `alternative_method`, `tra_reference`, `customized_testing_procedures`.

**Compensating-control worksheet:** `requirement`, `constraints`, `compensating_controls_defined`, `objective`, `identified_risk`, `validation`, `maintenance` (six rows), `complete` (true iff all six present), `control_type` (`compensating_control` when constraint-driven).

**Worked illustration (UC-03 shape):** a 30-location franchise on SAQ D has a legacy POS that cannot enforce a defined Req-8 authentication control — a legitimate technical constraint. The proposed control (legacy-POS network isolation + MFA at the jump host + enhanced logging/alerting) is documented with all six worksheet rows → **worksheet complete**, classified **compensating control** (constraint-driven), **not** a customized approach. See `use-cases/uc-03-compensating-control.md`.

## 7. Cross-references
TRA anchor: Req 12.3 (`chunks/05`). Both records flow into the ROC findings (`chunks/06`). For the requirements these approaches modify, see `chunks/04` and `chunks/05`.
