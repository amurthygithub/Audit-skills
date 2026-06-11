---
chunk_id: 01-fedramp-and-governance
parent_skill: fedramp-authorization
topic: "What FedRAMP is; the FedRAMP Authorization Act of 2022 (44 U.S.C. 3607-3616); the statutory FedRAMP Board (NOT the retired JAB); OMB M-24-15; FedRAMP as the program layer on NIST SP 800-53"
load_when: "user asks what FedRAMP is, who authorizes a cloud service, the FedRAMP Authorization Act, the FedRAMP Board vs the JAB, OMB M-24-15, or how FedRAMP relates to 800-53 and SOC 2"
---

# Chunk 01 — FedRAMP and current governance

FedRAMP (the Federal Risk and Authorization Management Program) is the U.S. government's standardized program for **assessing and authorizing cloud services** for federal use, so that one rigorous authorization can be reused across agencies instead of each agency reassessing the same cloud product. This chunk fixes **what FedRAMP is** and the **current** governance — which changed materially in 2022–2024. Do not describe the pre-2022 "JAB" structure as current.

## 1. The program in one paragraph

A cloud service provider (CSP) categorizes its offering (FIPS 199), implements a FedRAMP **baseline** of NIST SP 800-53 Rev 5 controls, documents them in a **System Security Plan (SSP)**, has an independent **3PAO** assess them (SAP → SAR), tracks gaps in a **POA&M**, and — once an agency grants an **Authorization to Operate (ATO)** — maintains the authorization through monthly **Continuous Monitoring (ConMon)**. Each of those is a later chunk; this one is the program and its authority.

## 2. The statutory authority — the FedRAMP Authorization Act of 2022

FedRAMP was an OMB policy program from 2011 until Congress put it in statute. The **FedRAMP Authorization Act of 2022** (enacted 2022-12-23 as part of Public Law 117-263, the NDAA for FY2023) codified FedRAMP at **44 U.S.C. 3607–3616** and established it as the standardized, reusable approach to cloud-security authorization.

- It created a statutory **FedRAMP Board** to provide input and approve guidance [FEDRAMP-ACT-2022 §3610]. **The FedRAMP Board replaced the Joint Authorization Board (JAB).**
- It enshrined the principle of **reuse** — agencies should leverage existing authorizations rather than duplicate assessments.
- The chapter carries a 5-year sunset clause (sections 3607–3616 are struck five years after enactment) — a currency flag, not a present limitation.

## 3. OMB M-24-15 — the modernization memo (2024-07-25)

**OMB Memorandum M-24-15, "Modernizing the Federal Risk and Authorization Management Program (FedRAMP)"** (2024-07-25), implements the Act and is the operative policy today [OMB-M-24-15 §authority]. It:

1. **Rescinded and replaced** the original 2011-12-08 FedRAMP memo in its entirety.
2. Reframed FedRAMP as a **security/risk-management** program and directed scaling the marketplace.
3. Established the **presumption of adequacy**: an agency must presume the security assessment documented in a FedRAMP authorization package is **adequate** for a product at a given FIPS 199 impact level [OMB-M-24-15 §presumption] — this is what makes reuse real and reduces agency-by-agency reassessment.
4. Pushed **automation / machine-readable** authorization and ConMon artifacts (OSCAL until NIST designates a successor).
5. **Retired the JAB P-ATO model.** Existing JAB "provisional ATOs" (P-ATOs) at the time of the memo were **re-designated** by the FedRAMP PMO. There is no JAB issuing P-ATOs today.

> **Currency rule:** the current authorizers are **agencies** (with the FedRAMP Board + GSA/PMO governing the program). The JAB and its P-ATO are **historical**. If a user frames a question around "the JAB," correct it to the current FedRAMP Board / agency-authorization model. See `chunks/03-authorization-paths.md`.

## 4. FedRAMP is the *program* layer on NIST SP 800-53 — the boundary

FedRAMP does **not** define its own control catalog. Its Low/Moderate/High baselines are **NIST SP 800-53 Rev 5** controls, tailored from the 800-53B baselines with FedRAMP-specific additions and parameter values [NIST-800-53R5 §baselines]. So:

- **This skill** owns the FedRAMP *program and process*: categorization → baseline selection → the authorization package → the 3PAO assessment → ConMon → the modernized direction (20x).
- **`nist-800-53-rmf`** owns the **control catalog itself** (the families, the controls, the general Risk Management Framework). Do not re-teach the catalog here; cite the boundary (`chunks/02-impact-levels-and-baselines.md`).

## 5. FedRAMP vs SOC 2 — a frequent confusion

FedRAMP is the **federal** authorization regime (statutory, agency-granted ATO, monthly ConMon, 800-53 controls). **SOC 2** (see `aicpa-soc-reporting`) is a **commercial** AICPA attestation against the Trust Services Criteria — useful evidence and a related discipline, but **not** a FedRAMP authorization and not interchangeable with one. A SOC 2 report does not authorize a cloud service for federal use.

## 6. Adjacent regimes (named, not covered)

- **DoD Impact Levels (IL2/IL4/IL5/IL6) / DISA Cloud Computing SRG** — the Department of Defense's cloud-authorization regime, built on but distinct from FedRAMP.
- **StateRAMP** — a state/local analog that borrows FedRAMP's model.
- **CMMC** — the defense-contractor cybersecurity certification.

These are separate programs; this skill does not cover their mechanics.

## 7. Anti-hallucination

- **The current authorizer is the statutory FedRAMP Board (44 U.S.C. 3610) + agencies — NOT the JAB.** The JAB and its P-ATO were retired by OMB M-24-15; legacy P-ATOs were re-designated by the PMO [OMB-M-24-15 §authority]. Never present the JAB as a current authorizing body.
- **FedRAMP was codified in statute by the 2022 Act** (44 U.S.C. 3607-3616); it is no longer only an OMB policy program [FEDRAMP-ACT-2022 §3610].
- **OMB M-24-15 is dated 2024-07-25** and rescinded the 2011 memo; the **presumption of adequacy** is its central reuse principle [OMB-M-24-15 §presumption].
- **FedRAMP baselines are tailored NIST SP 800-53 Rev 5 controls — not a separate catalog** [NIST-800-53R5 §baselines]. For the catalog/RMF, use `nist-800-53-rmf`.
- **FedRAMP ≠ SOC 2.** SOC 2 is a commercial AICPA attestation, not a federal authorization.
