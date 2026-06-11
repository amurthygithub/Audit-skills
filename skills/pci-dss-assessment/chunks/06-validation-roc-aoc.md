---
chunk_id: 06-validation-roc-aoc
parent_skill: pci-dss-assessment
topic: "The assessment process; ROC vs AOC vs SAQ; QSA/ISA/QSA-support roles; assessor sampling; AOC parts; service-provider responsibility matrix"
load_when: "user asks about ROC, AOC, SAQ deliverables, QSA or ISA roles, assessor sampling, the responsibility matrix, or how PCI validation results are documented"
---

# Chunk 06 — Validation: ROC and AOC

Validation is **how** an entity demonstrates PCI DSS compliance for a defined scope and period. The three deliverable families are the **SAQ** (self-assessment, `chunks/03`), the **ROC** (assessor report), and the **AOC** (attestation), all available from the PCI SSC document library [PCI-SSC-Document-Library].

## 1. The three deliverable families

| Deliverable | Who produces it | What it is |
|-------------|-----------------|------------|
| **SAQ** | the entity (merchant/SP), eligibility-gated | Self-attestation against a channel-specific subset of PCI DSS |
| **ROC** | a **QSA** (or **ISA** internally, where permitted) | Full Report on Compliance: per-requirement findings, testing performed, sampling rationale, scope description |
| **AOC** | signed by the entity (and assessor, for an assessed report) | Attestation of Compliance: the summary cover document that accompanies a SAQ or ROC |

Every assessment, whether SAQ- or ROC-based, produces an **AOC**. The AOC is what the entity typically shares with an acquirer or a requesting customer; the ROC contains the detailed evidence.

## 2. The assessment roles

- **QSA (Qualified Security Assessor)** — an individual, employed by a PCI SSC-qualified QSA company, authorized to perform PCI DSS assessments and sign ROCs/AOCs.
- **ISA (Internal Security Assessor)** — a trained employee of the assessed entity, permitted (within program rules) to perform internal assessments.
- **QSA-support / consultant** — assists an entity in preparing for assessment (scoping, remediation, evidence, worksheets) **without** signing the ROC as the assessing QSA. This skill supports that preparation role; it does **not** simulate or assert a QSA engagement determination.

## 3. ROC anatomy (paraphrased)

A ROC documents, per the assessor template:
- **Scope** — the CDE, in-scope components, segmentation, and connected-to systems (`chunks/02`).
- **Per-requirement findings** — for each applicable section: the **approach used** (defined or customized — `chunks/07`), the testing performed, and the finding (In Place / Not Applicable / Not Tested / Not in Place), with any **compensating controls** documented via the worksheet.
- **Sampling rationale** — where representative samples were tested instead of full populations (`chunks/02 §6`); sampling never narrows scope.
- **Evidence references** — interviews, observations, documentation, and configuration reviews supporting each finding.

## 4. AOC parts (paraphrased)

The AOC summarizes assessment results: entity and assessor identification, scope and validation method, the requirement-level summary, the compliance determination for the period, and signatures. Service-provider AOCs additionally summarize which requirements the provider covers on behalf of customers.

## 5. Service-provider responsibility matrix

Where a service provider performs PCI DSS controls on a customer's behalf (Req 12.8 / 12.9 territory — `chunks/05`), the parties document a **responsibility matrix**: for each applicable requirement, who is responsible — the **service provider**, the **customer**, or **shared**. This matrix is the artifact that lets a customer scope its own assessment around the outsourced functions. A customer cannot inherit compliance it has not confirmed; an SP's AOC plus a responsibility matrix is the evidence of coverage.

## 6. Procedure — ROC / AOC assembly (assessor-support view)

1. **Confirm scope** (`chunks/02`) and the validation path (SAQ vs ROC, `chunks/03`).
2. For each applicable section, record the **approach** (defined/customized) and gather testing evidence.
3. Document **sampling** rationale where populations are large and centrally managed.
4. Record any **compensating controls** with the four-element worksheet and any **customized approaches** with their TRA (`chunks/07`).
5. Capture the **service-provider responsibility matrix** for outsourced functions.
6. Produce the **AOC** summary consistent with the ROC/SAQ findings; reconcile every "In Place" to evidence.

## 7. Output template — validation summary

| Field | Meaning |
|-------|---------|
| `deliverable` | SAQ type / ROC |
| `scope_summary` | CDE + connected; segmentation note |
| `approach_by_requirement` | defined / customized per section |
| `findings_rollup` | counts of In Place / N/A / Not in Place |
| `compensating_controls` | worksheet references (`chunks/07`) |
| `responsibility_matrix_ref` | for outsourced functions |
| `aoc_signed` | attestation status |

## 8. Cross-references
Brand/acquirer rules (which deliverable, what cadence, which level) are **brand-defined** (`chunks/08`) — the standard prescribes the deliverable formats, not the level thresholds. For the approach distinctions referenced throughout, see `chunks/07-approaches-and-compensating-controls.md`.
