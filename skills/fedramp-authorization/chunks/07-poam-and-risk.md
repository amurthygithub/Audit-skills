---
chunk_id: 07-poam-and-risk
parent_skill: fedramp-authorization
topic: "The POA&M (Plan of Action & Milestones) lifecycle — SAR deficiency -> POA&M item -> severity -> remediation SLA (30/90/180); the three deviation-request types (False Positive / Risk Adjustment / Operational Requirement); vendor-dependency / operational-requirement handling; how the POA&M drives ConMon and re-authorization; the AO's risk-acceptance role (the ATO is the AO's call, not automatic)"
load_when: "user asks about the POA&M, a SAR deficiency or finding, remediation deadlines/SLAs, deviation requests (false positive / risk adjustment / operational requirement), vendor-dependency findings, risk acceptance, or how findings affect re-authorization and the ATO decision"
---

# Chunk 07 — POA&M and risk acceptance

The **POA&M** (Plan of Action & Milestones) is the **CSP-authored** corrective-action plan: it tracks every deficiency the 3PAO documented in the SAR, the planned remediation, and the deadline. The POA&M is the spine of post-authorization risk management — it drives monthly ConMon (`chunks/06-continuous-monitoring.md`) and feeds re-authorization. This chunk fixes the item lifecycle, the severity-driven SLAs, the three deviation-request types, and the one decision that is never automatic: the **authorizing official's** risk acceptance.

## 1. From SAR deficiency to POA&M item

The 3PAO's **SAR** (Security Assessment Report — see `chunks/04-the-authorization-package.md`) records each control deficiency and vulnerability with a severity. Each open SAR deficiency becomes a **POA&M item** the CSP owns and works.

- The POA&M is **CSP-authored** (the 3PAO finds; the CSP plans and remediates).
- Each item carries the finding, its **severity**, the remediation milestones, and a due-date.
- **Inherited/leveraged** controls are **not** the leveraging CSP's POA&M items — they belong to the provider's package and POA&M (`chunks/05-assessment-and-inheritance.md`).

## 2. Severity sets the remediation SLA

The severity of a finding sets the remediation deadline (the same SLAs ConMon enforces):

| Severity | Remediation SLA |
|----------|-----------------|
| **High / Critical** | **30 days** |
| **Moderate** | **90 days** |
| **Low** | **180 days** |

[FEDRAMP-CONMON §monthly]

The due-date for a POA&M item is computed from the date the finding was identified plus the SLA window for its severity (identified-date + 30 / 90 / 180 days). These deadlines are the same ones tracked in monthly ConMon.

The SAR **Risk Exposure Table** uses a **Critical / High / Moderate / Low** severity scale; **Critical and High share the 30-day window**. A Critical finding is the most urgent class and the AO weighs it most heavily at the risk-acceptance decision (§6).

## 3. The three deviation-request types

When a scan finding is **not** a straightforward defect the CSP must remediate on the standard clock, the CSP files a **deviation request** so the finding is handled accurately rather than left as an unmitigated open item. There are **three** types:

1. **False Positive (FP)** — the scanner reported a vulnerability that is **not actually present** (e.g., a misidentified version, a control already in place). With evidence, the finding is removed from the active POA&M rather than remediated.
2. **Risk Adjustment (RA)** — the finding is real, but its **risk rating should be adjusted** (typically downward) because of compensating controls or context the raw scan severity did not account for. The adjusted severity changes how the item is weighed.
3. **Operational Requirement (OR)** — the finding is real and cannot be remediated **without breaking required functionality** (an operational constraint forces the configuration). The item is documented and managed as an accepted operational condition rather than closed.

Each deviation request is evidence-backed and subject to review; a deviation does not unilaterally erase a finding — it reclassifies how the finding is tracked and weighed.

## 4. Vendor-dependency and operational-requirement handling

Some findings cannot be closed by the CSP alone:

- **Vendor-dependency findings** — the fix depends on an upstream vendor or an inherited provider. The item stays on the POA&M, tracked against the vendor's remediation, rather than being treated as a CSP defect that missed its SLA.
- **Operational requirements** — handled via the **OR** deviation type above: the deficiency is documented as a managed operational condition when remediation would break required functionality.

In both cases the item remains visible and tracked; it is not silently dropped.

## 5. How the POA&M drives ConMon and re-authorization

- **ConMon:** the updated POA&M is part of every **monthly** ConMon submission (with the system inventory and vulnerability-scan results) [FEDRAMP-CONMON §monthly]. New scan findings open new items; remediated items close; deviation requests are filed and tracked here.
- **Re-authorization:** the standing POA&M — especially **residual high-severity** items — is what the authorizing official weighs at periodic reassessment. A clean, current, SLA-compliant POA&M supports continued authorization; a backlog of overdue high findings weighs against it.

## 6. The AO owns the risk-acceptance / ATO decision

The **Authorizing Official (AO)** makes the **risk-acceptance** decision. The 3PAO **recommends** (authorize-with-POA&M or not — see `chunks/05-assessment-and-inheritance.md`); the AO **decides**.

- **Residual high-severity** findings weigh **against** authorization, but the ATO is the **AO's risk-based call** — it is **not** a derived or automatic decision computed from the findings.
- A system can be authorized **with** an open POA&M (the AO accepts the residual risk with a remediation plan); a system with few findings can still be denied if the AO judges the residual risk unacceptable.
- This skill encodes the program; it does not grant or guarantee an ATO.

## 7. Procedure — POA&M item lifecycle

1. **Open the item** from the SAR deficiency (or from a new ConMon scan finding): record the finding, the affected control, and the severity.
2. **Set the due-date** = identified-date + SLA for the severity (High/Critical 30, Moderate 90, Low 180 days).
3. **Decide handling:** straightforward defect -> remediate by the due-date; not a straightforward defect -> file a **deviation request** (FP / RA / OR) with evidence; vendor-dependent -> track against the vendor.
4. **Work the milestones** and update status in each **monthly** ConMon submission.
5. **Close** on verified remediation, **or** carry the item with its deviation classification.
6. **Surface residual high-severity items** for the **AO's** risk-acceptance decision at authorization and re-authorization.

## 8. Output template — a POA&M item

```
POA&M item: <id>
  Finding:        <SAR deficiency / control + vulnerability>
  Control:        <800-53 control id, e.g., SI-2>
  Severity:       <High/Critical | Moderate | Low>
  Identified:     <date>
  SLA:            <30 | 90 | 180> days
  Due-date:       <identified + SLA>
  Status:         <open | in-progress | remediated | deviation-requested>
  Deviation type: <none | False Positive (FP) | Risk Adjustment (RA) | Operational Requirement (OR)>
  Notes:          <vendor-dependency / milestones / AO risk note>
```

## 9. Anti-hallucination

- **Remediation SLAs are 30 / 90 / 180 days** — High/Critical **30**, Moderate **90**, Low **180** [FEDRAMP-CONMON §monthly]. Do not state other windows.
- **The POA&M is CSP-authored**; it tracks SAR deficiencies. **Inherited/leveraged** controls are the provider's POA&M, not the leveraging CSP's.
- **The three deviation-request types are False Positive (FP), Risk Adjustment (RA), and Operational Requirement (OR)** — used when a scan finding is not a straightforward defect. A deviation reclassifies a finding; it does not erase it without review.
- **The AO owns the risk-acceptance / ATO decision.** Residual high-severity findings weigh **against** authorization, but the ATO is the **authorizing official's risk-based call — NOT an automatic or derived decision**. A 3PAO recommends; it does not grant the ATO.
- This skill encodes the FedRAMP program and is **not authorization or legal advice**; verify against the cited sources.
