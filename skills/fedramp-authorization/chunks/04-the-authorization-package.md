---
chunk_id: 04-the-authorization-package
parent_skill: fedramp-authorization
topic: "The FedRAMP authorization package — the SSP (CSP-authored 'security blueprint' + per-control implementation narrative + FIPS 199 categorization + attachments), the SAP (3PAO-authored plan), the SAR (3PAO-authored results), and the POA&M (CSP-authored corrective-action plan); who authors each artifact and the sequence in which they are produced"
load_when: "user asks what is in the authorization package, what to submit, the SSP / SAP / SAR / POA&M, who writes each document, or the order in which the package artifacts are produced"
---

# Chunk 04 — The authorization package

The FedRAMP authorization package is built from **4 core artifacts**: the **SSP**, the **SAP**, the **SAR**, and the **POA&M**. The two facts consumers get wrong are **who authors each** and **the sequence** in which they are produced. This chunk pins both.

## 1. The four core artifacts

| Artifact | Full name | Author | What it is |
|----------|-----------|--------|------------|
| **SSP** | System Security Plan | **CSP** | The "security blueprint" for the Cloud Service Offering — components, architecture, data flows, and the per-control implementation narrative [FEDRAMP-PLAYBOOK §ssp] |
| **SAP** | Security Assessment Plan | **3PAO** | The 3PAO's methodical approach to assessing the controls (scope, methods, sampling) |
| **SAR** | Security Assessment Report | **3PAO** | The 3PAO's evaluation of the controls — vulnerabilities, risk, and recommendation |
| **POA&M** | Plan of Action & Milestones | **CSP** | The CSP's corrective-action plan for SAR-identified deficiencies; tracked monthly in ConMon |

These **4** artifacts are the core of the package [FEDRAMP-PLAYBOOK §ssp].

## 2. The SSP — the CSP's security blueprint

The **System Security Plan (SSP)** is the **CSP-authored** "security blueprint" for the Cloud Service Offering (CSO) [FEDRAMP-PLAYBOOK §ssp]. It describes the system's components, architecture, and data flows, and carries the **per-control implementation narrative** — how each control in the selected FedRAMP baseline (`chunks/02-impact-levels-and-baselines.md`) is implemented. It also records the **FIPS 199 categorization** (the high-water-mark rationale for the system's impact level) that drove baseline selection.

The SSP carries attachments, including:
- the **FIPS 199 categorization** worksheet/rationale,
- the **contingency plan** and **incident response (IR) plan**,
- the **system inventory**, and
- **vulnerability scan results**.

## 3. The SAP and SAR — the 3PAO's plan and results

The **Security Assessment Plan (SAP)** is **3PAO-authored**: it is the 3PAO's methodical plan for assessing the controls. The **Security Assessment Report (SAR)** is also **3PAO-authored**: it documents the 3PAO's evaluation of the controls, the vulnerabilities found, the risk, and the assessor's recommendation. The 3PAO is the independent assessor (A2LA-accredited to ISO/IEC 17020) — the assessment mechanics, sampling, and control inheritance are in `chunks/05-assessment-and-inheritance.md`.

## 4. The POA&M — the CSP's corrective-action plan

The **Plan of Action & Milestones (POA&M)** is **CSP-authored**: it is the corrective-action plan for the deficiencies the SAR identifies. Each SAR finding becomes a POA&M item with a severity and a remediation deadline; the POA&M is then tracked **monthly** through Continuous Monitoring (`chunks/06-continuous-monitoring.md`). The POA&M lifecycle, severities, and deviation requests are detailed in `chunks/07-poam-and-risk.md`.

## 5. The sequence — who produces what, in order

The artifacts are produced in a fixed order, because each feeds the next:

```
SSP (CSP)  ->  SAP (3PAO)  ->  assessment (3PAO)  ->  SAR (3PAO)  ->  POA&M (CSP)  ->  ATO (agency AO)
```

1. **SSP (CSP)** — the CSP documents the system and its per-control implementation.
2. **SAP (3PAO)** — the 3PAO plans the assessment against the SSP.
3. **Assessment (3PAO)** — the 3PAO executes the SAP (tests/samples the controls).
4. **SAR (3PAO)** — the 3PAO reports the results, vulnerabilities, risk, and recommendation.
5. **POA&M (CSP)** — the CSP plans corrective actions for the SAR-identified deficiencies.
6. **ATO** — the sponsoring agency's **AO** reviews the package and grants the Authorization to Operate (`chunks/03-authorization-paths.md`).

## 6. Procedure — assemble the authorization package

1. **Categorize and select the baseline.** FIPS 199 high-water mark → Low 156 / Moderate 323 / High 410 / LI-SaaS 156 (`chunks/02-impact-levels-and-baselines.md`).
2. **Author the SSP (CSP).** Document architecture, data flows, the per-control implementation narrative, the FIPS 199 categorization, and the attachments (contingency/IR plans, inventory, scan results).
3. **3PAO authors the SAP.** The 3PAO plans the assessment against the SSP.
4. **3PAO assesses and authors the SAR.** Execute the SAP; report results, vulnerabilities, risk, and the recommendation (`chunks/05-assessment-and-inheritance.md`).
5. **Author the POA&M (CSP).** Convert each SAR deficiency into a POA&M item with severity and a remediation deadline.
6. **Submit for the ATO.** The agency AO reviews the assembled package and grants the ATO; then enter monthly ConMon.

## 7. Output template — package checklist (author + sequence)

```
System / CSO: <name>     Overall FIPS 199 impact: <Low | Moderate | High>   Baseline: <156 | 323 | 410 | LI-SaaS 156>
[ ] 1. SSP    (author: CSP)   security blueprint + per-control narrative + FIPS 199 categorization
        attachments: [ ] contingency plan  [ ] IR plan  [ ] system inventory  [ ] scan results
[ ] 2. SAP    (author: 3PAO)  assessment plan (scope, methods, sampling)
[ ] 3. SAR    (author: 3PAO)  assessment results, vulnerabilities, risk, recommendation
[ ] 4. POA&M  (author: CSP)   corrective-action plan for SAR deficiencies (severity + deadline)
Sequence: SSP -> SAP -> assessment -> SAR -> POA&M -> ATO (agency AO)
```

## 8. Anti-hallucination

- **The package has 4 core artifacts: SSP, SAP, SAR, POA&M** [FEDRAMP-PLAYBOOK §ssp]. Do not drop or rename one.
- **Authorship is fixed: the CSP authors the SSP and the POA&M; the 3PAO authors the SAP and the SAR.** Do not attribute the SSP or POA&M to the 3PAO, or the SAP/SAR to the CSP.
- **The SSP is the CSP's "security blueprint"** for the CSO — the per-control implementation narrative plus the FIPS 199 categorization and attachments (contingency/IR plans, inventory, scan results) [FEDRAMP-PLAYBOOK §ssp].
- **The sequence is SSP → SAP → assessment → SAR → POA&M → ATO.** The POA&M is built from SAR-identified deficiencies and is then tracked monthly in ConMon (`chunks/06`, `chunks/07`).
