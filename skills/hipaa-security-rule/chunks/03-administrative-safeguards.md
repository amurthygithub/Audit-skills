---
chunk_id: 03-administrative-safeguards
parent_skill: hipaa-security-rule
topic: "§164.308 administrative safeguards beyond the security management process: standards (a)(2)-(a)(8) and (b), specs with exact (R)/(A) designations, evidence"
load_when: "user asks about workforce security, access management, training, incident procedures, contingency planning, evaluation, or the BA-contracts standard"
---

# Chunk 03 — Administrative Safeguards (§164.308)

§164.308 [CFR-45-164-Subpart-C] contains **9 standards with 21 titled implementation specifications (10 Required / 11 Addressable)** — the largest safeguard family. The first standard (Security management process, all 4 specs Required) has its own chunk: `chunks/02-risk-analysis-and-management.md`. This chunk covers the remaining 8 standards. Addressable specs below follow the §164.306(d)(3) disposition workflow in `chunks/07-addressable-decisions-and-evidence.md`.

## 1. Assigned security responsibility — §164.308(a)(2) (no separate specs)

"Identify the security official who is responsible for the development and implementation of the policies and procedures required by this subpart." One named, accountable individual — not a committee. Scales to any size (a solo BA documents that the practitioner is the security official). **Evidence:** designation document or org chart with name and date; job description covering Subpart C responsibility.

## 2. Workforce security — §164.308(a)(3)

Ensure workforce members have appropriate access to ePHI and prevent those without authorization from obtaining it.

| Spec | Title | Designation |
|------|-------|-------------|
| (a)(3)(ii)(A) | Authorization and/or supervision | (Addressable) |
| (a)(3)(ii)(B) | Workforce clearance procedure | (Addressable) |
| (a)(3)(ii)(C) | Termination procedures | (Addressable) |

Note: all three are Addressable in the text; the eCFR matrix rendering drops the (A) on Workforce clearance procedure, but §164.308(a)(3)(ii)(B) is explicitly "(Addressable)" (see `chunks/01 §6.3`). **Evidence:** access-authorization procedures; background/role-review records at hire; offboarding checklists with dated access-revocation tickets. Termination timeliness is a high-churn-environment focus (hospitals: see `industries/healthcare.md`).

## 3. Information access management — §164.308(a)(4)

Authorize access to ePHI consistent with Subpart E (Privacy Rule) requirements.

| Spec | Title | Designation |
|------|-------|-------------|
| (a)(4)(ii)(A) | Isolating health care clearinghouse functions | (Required) |
| (a)(4)(ii)(B) | Access authorization | (Addressable) |
| (a)(4)(ii)(C) | Access establishment and modification | (Addressable) |

The clearinghouse-isolation spec is **(Required) but conditional** — it applies only if a clearinghouse is part of a larger organization. **Evidence:** role-based access policies; access-grant approvals; periodic access reviews with documented modifications.

## 4. Security awareness and training — §164.308(a)(5)

A security awareness and training program "for all members of its workforce (including management)."

| Spec | Title | Designation |
|------|-------|-------------|
| (a)(5)(ii)(A) | Security reminders | (Addressable) |
| (a)(5)(ii)(B) | Protection from malicious software | (Addressable) |
| (a)(5)(ii)(C) | Log-in monitoring | (Addressable) |
| (a)(5)(ii)(D) | Password management | (Addressable) |

All four specs are Addressable, but the **standard itself is mandatory** — a program must exist; the specs shape its content. **Evidence:** training content and completion records (including management); reminder artifacts (newsletters, phishing-simulation results); anti-malware procedures; log-in-discrepancy reporting procedures; password policy.

## 5. Security incident procedures — §164.308(a)(6)

Policies and procedures to address security incidents (defined in §164.304 — **attempted** or successful unauthorized access/use/disclosure/modification/destruction or interference).

| Spec | Title | Designation |
|------|-------|-------------|
| (a)(6)(ii) | Response and reporting | (Required) |

Identify and respond to suspected or known incidents; mitigate harmful effects to the extent practicable; **document incidents and their outcomes**. BAs additionally owe incident reports to the CE under the BAA (§164.314(a)(2)(i)(C) — see `chunks/06`). **Evidence:** incident response plan; incident log with outcomes (or attestation of none); post-incident reviews.

## 6. Contingency plan — §164.308(a)(7)

Respond to emergencies (fire, vandalism, system failure, natural disaster) that damage systems containing ePHI.

| Spec | Title | Designation |
|------|-------|-------------|
| (a)(7)(ii)(A) | Data backup plan | (Required) |
| (a)(7)(ii)(B) | Disaster recovery plan | (Required) |
| (a)(7)(ii)(C) | Emergency mode operation plan | (Required) |
| (a)(7)(ii)(D) | Testing and revision procedures | (Addressable) |
| (a)(7)(ii)(E) | Applications and data criticality analysis | (Addressable) |

The backup plan requires "retrievable **exact copies**" of ePHI. **Evidence:** backup configuration and restore-test results; DR plan with RTO/RPO; emergency-mode procedures preserving security during operations; test reports (for the Addressable testing spec or its disposition); criticality rankings feeding the other components.

## 7. Evaluation — §164.308(a)(8) (no separate specs)

"Perform a periodic technical and nontechnical evaluation" — initially against this rule, thereafter in response to environmental or operational changes — establishing the extent to which policies and procedures meet Subpart C. This is the **compliance evaluation** standard: it may be internal or external, but it must be periodic and documented. Distinct from the risk analysis (risks to ePHI) — the evaluation measures the *program* against the *rule*. **Evidence:** dated evaluation reports tied to rule requirements; remediation tracking.

## 8. Business associate contracts and other arrangements — §164.308(b)(1)

A CE may permit a BA to create, receive, maintain, or transmit ePHI on its behalf **only with satisfactory assurances per §164.314(a)**, documented in a written contract or other arrangement. The same obligation cascades: a BA must obtain the same assurances from its **subcontractors** (§164.308(b)(2)); the CE is *not* required to contract directly with subcontractors.

| Spec | Title | Designation |
|------|-------|-------------|
| (b)(3) | Written contract or other arrangement | (Required) |

This standard does not carry the "Standard:" prefix in the body text but is the 9th administrative standard per Appendix A (see `chunks/01 §6.3`). Required BAA contents live in §164.314 — see `chunks/06-organizational-and-documentation.md`. **Evidence:** BAA inventory mapped to vendor list; executed agreements; subcontractor flow-down attestations.

## 9. Anti-hallucination notes for this chunk

- Designation discipline: Required specs in this chunk are exactly — clearinghouse isolation (a)(4)(ii)(A), response and reporting (a)(6)(ii), data backup (a)(7)(ii)(A), disaster recovery (a)(7)(ii)(B), emergency mode (a)(7)(ii)(C), written contract (b)(3). Everything else titled here is Addressable. (Plus the four Required specs under (a)(1) in `chunks/02`, totaling 10 R / 11 A for the family.)
- Addressable specs still require a documented disposition — never present them as skippable (§164.306(d)(3); `chunks/07`).
- Standards with no separate specs ((a)(2), (a)(8)) are mandatory in full; the Appendix A "(R)" printed for them is a standard-level entry under the 42-entry counting convention (label conventions per `chunks/01 §6.2`).
- Training applies to the entire workforce **including management** — the parenthetical is in the rule text.
