---
chunk_id: 03-authorization-paths
parent_skill: fedramp-authorization
topic: "The current FedRAMP authorization path — Agency Authorization (the operative Rev 5 path); the Authorizing Official (AO) and the ATO decision; multi-agency authorization; single-authorization + presumption of adequacy (OMB M-24-15); the JAB P-ATO retired (legacy P-ATOs re-designated by the PMO); the readiness sequence (FedRAMP Ready / RAR → full 3PAO assessment → ATO); leveraging an existing authorization"
load_when: "user asks how a cloud service gets authorized, the authorization path, Agency Authorization vs JAB, who grants the ATO, the presumption of adequacy, multi-agency authorization, FedRAMP Ready / readiness assessment (RAR), or how to reuse an existing authorization"
---

# Chunk 03 — Authorization paths (the current model)

This chunk fixes **how a cloud service gets authorized today** — under the FedRAMP Authorization Act of 2022 and OMB M-24-15. The pre-2022 "JAB P-ATO" model is **retired**; do not present it as a current path. The operative Rev 5 path is **Agency Authorization**, and the **Authorizing Official (AO)** grants the **Authorization to Operate (ATO)**.

## 1. Agency Authorization — the operative Rev 5 path

**Agency Authorization** is the operative Rev 5 authorization path: an agency sponsors a cloud service provider (CSP) and grants the authorization [OMB-M-24-15 §presumption]. The CSP categorizes its offering (FIPS 199 high-water mark), implements the selected FedRAMP baseline of NIST SP 800-53 Rev 5 controls, documents them in the **System Security Plan (SSP)**, has an independent **3PAO** assess them (SAP → SAR), and tracks gaps in a **POA&M** — then the sponsoring agency reviews the package and the **AO** issues the **ATO**. The package and the 3PAO assessment are detailed in `chunks/04-the-authorization-package.md` and `chunks/05-assessment-and-inheritance.md`.

## 2. The Authorizing Official and the ATO decision

The **Authorizing Official (AO)** grants the **Authorization to Operate (ATO)**. The ATO is the AO's **risk-based decision** to accept the residual risk of operating the system — it is not automatic and not a 3PAO determination. A 3PAO **assesses** the controls and **recommends**; it does **not** grant the ATO. Once granted, the CSP maintains the authorization through monthly **Continuous Monitoring** (`chunks/06-continuous-monitoring.md`).

## 3. M-24-15 — multi-agency authorization, single authorization, and presumption of adequacy

**OMB M-24-15 (2024-07-25)** modernized the program and reframed it around a **single FedRAMP authorization** that other agencies reuse [OMB-M-24-15 §authority]:

1. **Multi-agency authorization** is permitted — more than one agency may participate in / sponsor an authorization.
2. **Presumption of adequacy**: an agency **must presume** that the security assessment documented in a FedRAMP authorization package is **adequate** for a product at a given FIPS 199 impact level [OMB-M-24-15 §presumption]. This is what makes reuse real and reduces duplicative agency-by-agency reassessment.

## 4. The JAB P-ATO is retired

OMB M-24-15 **retired the JAB P-ATO model**. Existing JAB "provisional ATOs" (P-ATOs) at the time of the memo were **re-designated by the FedRAMP PMO** [OMB-M-24-15 §authority]. There is **no JAB issuing P-ATOs today**. The statutory **FedRAMP Board** (44 U.S.C. 3610) replaced the Joint Authorization Board (see `chunks/01-fedramp-and-governance.md`). If a user frames a question around "the JAB" or a "JAB P-ATO," correct it to the current Agency Authorization model with the AO granting the ATO.

## 5. The readiness sequence (optional precursor → full assessment → ATO)

Before the full assessment, a CSP **may** pursue an optional readiness step:

1. **FedRAMP Ready / Readiness Assessment Report (RAR)** — a 3PAO performs a readiness assessment and produces a **RAR**, an optional precursor that signals the offering is likely ready for a full authorization. This step is **optional**, not required.
2. **Full 3PAO assessment** — the 3PAO executes the **SAP** and produces the **SAR** (`chunks/05-assessment-and-inheritance.md`).
3. **ATO** — the sponsoring agency's **AO** reviews the package and grants the **Authorization to Operate**.

```
(optional) FedRAMP Ready / RAR (3PAO)  ->  full 3PAO assessment (SAP -> SAR)  ->  agency ATO (AO)
```

## 6. Leveraging an existing authorization (reuse)

A core principle of FedRAMP — enshrined by the 2022 Act and reinforced by M-24-15 — is **reuse**: an agency should **leverage** an existing FedRAMP authorization rather than duplicate the assessment. Under the **presumption of adequacy**, a leveraging agency presumes the existing authorization package is adequate at the relevant FIPS 199 impact level [OMB-M-24-15 §presumption]. Leveraged/inherited controls belong to the provider's package and are **not** re-assessed by the leveraging party (control inheritance is detailed in `chunks/05-assessment-and-inheritance.md`).

## 7. Procedure — selecting the authorization path

1. **Confirm the impact level.** Categorize the system (FIPS 199 high-water mark) and select the baseline — `chunks/02-impact-levels-and-baselines.md`.
2. **Check for an existing authorization to leverage.** If the offering (or an underlying provider) is already FedRAMP-authorized at the needed impact level, **leverage** it under the presumption of adequacy rather than reassess.
3. **Identify the sponsoring agency.** Agency Authorization requires an agency sponsor; multi-agency authorization is permitted under M-24-15.
4. **Decide on a readiness step (optional).** Engage a 3PAO for a **FedRAMP Ready / RAR** precursor, or proceed directly to the full assessment.
5. **Run the full assessment.** 3PAO executes the SAP and produces the SAR (`chunks/05`).
6. **Obtain the ATO.** The agency **AO** reviews the package and grants the ATO; then enter monthly ConMon (`chunks/06`).

## 8. Output template — authorization-path decision summary

```
System: <name>            Overall FIPS 199 impact: <Low | Moderate | High>
Path: Agency Authorization (operative Rev 5 path)
Sponsoring agency: <agency>          Multi-agency: <yes/no>
Leverage existing authorization: <yes -> which package | no>
Presumption of adequacy applies: <yes/no>  (presume package adequate at the impact level)
Readiness step (optional): <FedRAMP Ready / RAR by 3PAO | skipped>
Sequence: (RAR) -> full 3PAO assessment (SAP -> SAR) -> ATO
Authorizing Official (AO): <agency AO grants the ATO — risk-based decision>
Note: JAB P-ATO is retired; legacy P-ATOs were re-designated by the PMO.
```

## 9. Anti-hallucination

- **The JAB P-ATO model is retired.** OMB M-24-15 retired it; legacy JAB P-ATOs were **re-designated by the FedRAMP PMO** [OMB-M-24-15 §authority]. Never present the JAB as a current authorizing body or "JAB P-ATO" as a current path. **Agency Authorization** is the operative Rev 5 path.
- **The Authorizing Official (AO) grants the ATO** — it is the AO's **risk-based decision**. A 3PAO assesses and recommends; it does **not** grant the ATO.
- **The presumption of adequacy** (OMB M-24-15) means an agency must presume a FedRAMP authorization package adequate for a product at a given FIPS 199 impact level [OMB-M-24-15 §presumption]; M-24-15 also adds **multi-agency authorization**.
- **FedRAMP Ready / the RAR is an optional precursor** performed by a 3PAO — not a required step. The sequence is (optional RAR) → full 3PAO assessment → agency ATO.
