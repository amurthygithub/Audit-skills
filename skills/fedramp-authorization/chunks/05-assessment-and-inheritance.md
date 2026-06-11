---
chunk_id: 05-assessment-and-inheritance
parent_skill: fedramp-authorization
topic: "The 3PAO — independence and A2LA accreditation to ISO/IEC 17020 (Type A or C; Type B prohibited); the assessment flow (SAP -> control testing & sampling -> SAR with findings, risk, and recommendation); control inheritance / leveraging (IaaS/PaaS -> SaaS; inherited controls not re-tested by the leveraging CSP)"
load_when: "user asks about the 3PAO, A2LA, ISO/IEC 17020, who writes the SAP/SAR, control testing and sampling, the SAR recommendation, or control inheritance / leveraging from an IaaS/PaaS provider"
---

# Chunk 05 — The 3PAO assessment and control inheritance

The independent assessment is the heart of a FedRAMP authorization. This chunk fixes **who the assessor is** (the 3PAO, and how it is accredited), **what it produces** (the SAP and the SAR), and **what it does not re-test** (inherited / leveraged controls). One rule frames all of it: the **3PAO recommends; the authorizing official (AO) grants the ATO.** A 3PAO never issues an authorization.

## 1. The 3PAO — an independent, accredited assessor

A **3PAO (Third Party Assessment Organization)** is the **independent assessor** that evaluates a CSP's controls. Independence is the point: the 3PAO is not the CSP and not the agency, so its assessment can be trusted across agencies.

- A 3PAO is **accredited by A2LA** (the **American Association for Laboratory Accreditation**) against **ISO/IEC 17020** as either a **Type A** or a **Type C** inspection body [A2LA-3PAO §17020].
- A **Type B inspection body is prohibited** for FedRAMP work. Type B serves only its parent organization, which would defeat the independence requirement, so it cannot act as a 3PAO.
- The 3PAO **writes the SAP and the SAR**; it does **not** grant the ATO. The ATO is the **authorizing official's** risk-based decision (see `chunks/03-authorization-paths.md`).

## 2. The assessment flow — SAP -> testing & sampling -> SAR

The 3PAO's work runs in three phases that map onto the package artifacts (the package itself is `chunks/04-the-authorization-package.md`):

1. **Plan — the SAP (Security Assessment Plan).** The 3PAO writes a methodical plan for assessing the controls in the CSP's SSP: scope, the system boundary, the controls to be tested, the test methods (examine / interview / test), and the **sampling** approach for repeated components (e.g., a representative set of servers rather than every host).
2. **Test — control testing & sampling.** The 3PAO executes the SAP: it examines evidence, interviews staff, and tests control implementations, recording each control as satisfied or as having a deficiency. Vulnerability scanning of the system feeds this step.
3. **Report — the SAR (Security Assessment Report).** The 3PAO documents the results: the **findings** (failed / deficient controls), the associated **risk**, and a **recommendation** to the authorizing official. Each SAR finding seeds a **POA&M** item that the CSP then tracks (`chunks/07-poam-and-risk.md`).

The 3PAO's recommendation typically turns on residual risk: if an **unmitigated high-severity finding** remains, that is a risk signal the AO must weigh before granting the ATO.

## 3. Control inheritance / leveraging

A CSP rarely runs its own data centers. A SaaS offering is usually **built on an authorized IaaS or PaaS** (e.g., a SaaS on an authorized cloud platform). When that underlying provider is already FedRAMP-authorized, the leveraging CSP **inherits** the provider's controls.

- **Inherited (leveraged) controls are NOT re-tested by the leveraging CSP's 3PAO.** They were already assessed in the **provider's** package and are tracked in the **provider's** POA&M.
- The leveraging CSP is responsible only for the controls it **owns** — the controls implemented in its own layer of the stack. Those are what its 3PAO tests and what populate its SSP and POA&M.
- Inheritance flows **down the stack**: IaaS/PaaS -> SaaS. The leveraging CSP documents which controls are inherited (and from whom) versus which it implements itself.

This is why a SAR finding roll-up must separate **CSP-owned** failures from **inherited** ones: an inherited failure is the provider's to remediate, not the leveraging CSP's.

## 4. Procedure — plan, test, report

1. **Plan (SAP).** From the SSP, scope the system boundary, list the controls in the baseline, mark which are **inherited** (provider's) versus **CSP-owned**, choose test methods, and define the sampling set. Inherited controls are noted but not scheduled for re-testing.
2. **Test.** Examine, interview, and test each **CSP-owned** control; run vulnerability scans; record each as satisfied or deficient with a severity for each deficiency.
3. **Report (SAR).** Roll up the **findings** = CSP-owned failed controls (inherited excluded), count them by severity, note inheritance, and state the **recommendation** — flagging any residual high finding as an AO risk note. The findings become the initial POA&M.

## 5. Output template — SAR finding roll-up

This roll-up aligns with UC-03 (the Big-4 3PAO assessment of a Moderate CSP): findings = CSP-owned failed controls, inherited controls excluded, and a residual-high finding is an AO risk signal.

```
System: <CSP / CSO name>            Baseline: <Low 156 | Moderate 323 | High 410>
Findings (CSP-owned failed controls; inherited EXCLUDED): <count>
  By severity:  High <n>   Moderate <n>   Low <n>
Inherited controls (provider's package/POA&M; not re-tested here): <count>
POA&M items opened (= number of findings): <count>
Residual high findings: <n>   -> AO risk note: <none | review required before ATO>
3PAO recommendation: <authorize-with-POA&M | not recommended>
   (3PAO RECOMMENDS; the authorizing official GRANTS the ATO)
```

## 6. Cross-reference — health-tech CSP overlap

A health-tech CSP serving government health systems often must satisfy **FedRAMP and HIPAA at the same time**, and several control families double-count across the two regimes. For the HIPAA Security Rule side of that overlap, see `hipaa-security-rule` (and `industries/healthcare.md`). FedRAMP authorization and HIPAA compliance are distinct obligations; this skill covers the FedRAMP side.

## 7. Anti-hallucination

- **A 3PAO is accredited by A2LA to ISO/IEC 17020** as a **Type A or Type C** inspection body; **Type B is prohibited** (it would not be independent) [A2LA-3PAO §17020].
- **The 3PAO writes the SAP and SAR and RECOMMENDS; it does NOT grant the ATO.** The ATO is the **authorizing official's** risk-based decision — never attribute the authorization to the 3PAO.
- **Inherited / leveraged controls are the provider's responsibility** — they are **not re-tested** by the leveraging CSP's 3PAO and live in the **provider's** package and POA&M, not the leveraging CSP's [A2LA-3PAO §17020].
- **SAR findings = CSP-owned failed controls** (inherited-and-failed controls are excluded); each finding seeds a POA&M item, and a residual high finding is a risk signal for the AO.
