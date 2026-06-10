---
industry: financial-services
parent_skill: hipaa-security-rule
title: "Financial services — group health plan sponsors (§164.314(b) plan-document amendments) and insurers as covered entities"
version: 0.1.0
status: active
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2]
primary_personas: [Benefits/HR compliance counsel, Plan sponsor CISO, Health insurer compliance officer, ERISA plan administrator, Internal Audit]
regulatory_anchors: [HIPAA-Security-Rule, group-health-plan-requirements]
last_verified: "2026-06-10"
---

# Financial services — plan sponsors and insurers

Financial-services organizations meet the Security Rule from two directions that have nothing to do with treating patients: **health insurers are covered entities** (a health plan is one of the three CE types), and **any employer sponsoring a self-funded or experience-rated group health plan** — a bank, an asset manager, an insurance group's own HR function — picks up obligations through §164.314(b), the least-known of the 22 Subpart C standards. This view covers both.

## The financial-services framing

### Why does a bank's HR department have Security Rule obligations?

Because the **group health plan** it sponsors is itself a covered entity, and ePHI routinely flows from the plan (or its TPA/insurer) to the **plan sponsor** — for plan administration, claims oversight, or stop-loss decisions. §164.314(b)(1) requires that, except in the limited disclosure cases it enumerates (enrollment/disenrollment data and summary health information under §164.504(f)(1)(ii)–(iii), or disclosures authorized under §164.508), "a group health plan must ensure that its plan documents provide that the plan sponsor will reasonably and appropriately safeguard electronic protected health information created, received, maintained, or transmitted to or by the plan sponsor on behalf of the group health plan."

### What exactly must the plan documents say?

§164.314(b)(2) — implementation specifications, **Required**: the plan documents must be **amended** to incorporate provisions requiring the plan sponsor to:

| Spec | Plan-document provision |
|------|-------------------------|
| (b)(2)(i) | Implement administrative, physical, and technical safeguards that reasonably and appropriately protect the confidentiality, integrity, and availability of the ePHI it handles on behalf of the plan |
| (b)(2)(ii) | Ensure the adequate separation required by §164.504(f)(2)(iii) — the firewall between plan-administration staff and the rest of the employer — is supported by reasonable and appropriate security measures |
| (b)(2)(iii) | Ensure any agent to whom it provides the information agrees to implement reasonable and appropriate security measures |
| (b)(2)(iv) | Report to the group health plan any security incident of which it becomes aware |

In practice this means: the benefits-administration system access list *is* the technical expression of the §164.504(f)(2)(iii) separation; HR analysts who see claims-level ePHI sit inside the firewall, payroll and management outside it; and the plan sponsor's incident-response process needs a lane that reports **to the plan**.

### Are insurers just ordinary covered entities?

Yes — a health insurer, HMO, or insurance group writing health lines is a health plan CE and owes the full Subpart C program: all 22 standards, the §164.308(a)(1)(ii)(A) risk analysis over claims platforms and member portals, §164.306(d)(3) dispositions for the 22 addressable specs, and BAAs (§164.308(b)(1), §164.314(a)) with TPAs, pharmacy benefit managers, and analytics vendors. The hospital playbook in `industries/healthcare.md` and the UC-02 readiness engagement transfer directly; only the system inventory changes (claims adjudication, broker portals, actuarial data stores instead of EHR and PACS). Note the scope boundary: it is the *health* lines that make a CE — property/casualty or life books do not, and an insurer's banking affiliates are typically outside the plan entirely unless they sponsor their own group health plan.

## What's unique to financial services

- **The obligation hides in the plan documents.** Unlike a hospital, a plan sponsor can be out of compliance simply because nobody ever amended the plan document — a paper gap with a Required designation.
- **Summary health information is the safe lane.** Sponsors that receive only enrollment data and summary health information (for premium bids or plan changes) under §164.504(f)(1)(ii)–(iii) stay outside the §164.314(b)(2) amendment machinery — minimizing what flows to the sponsor is the cheapest control.
- **Existing financial-sector security programs help but do not answer.** GLBA/FFIEC-grade controls likely satisfy many safeguards *in substance*, but the Security Rule artifacts — ePHI-scoped risk analysis, addressable-disposition records, plan-document provisions — must exist in their own right. Overlap, not equivalence, again.
- **The firewall is auditable.** Examiners and OCR alike can test §164.504(f)(2)(iii) adequate separation as implemented: who actually has access to claims-level data, and does the access list match the plan document's named functions?

## Anti-hallucination

- **§164.314(b)'s implementation specifications are Required, not addressable** — the plan-document amendment cannot be dispositioned away.
- **§164.504(f) (permitted disclosures to sponsors, adequate separation) is Privacy Rule (Subpart E) text** — Subpart C's §164.314(b)(2)(ii) requires *security measures supporting* that separation; this skill cites the touchpoint and does not restate Subpart E mechanics.
- **This file gives no ERISA, state-insurance, or GLBA advice** — those regimes interact with plan administration but are out of this skill's scope.
- **The 2025 NPRM (90 FR 898) is a Proposed Rule only as of 2026-06-10** [HIPAA-Security-NPRM-2025]; nothing here changes until a final rule is codified.
- **Penalty amounts live once, as-of-dated, in `chunks/08-enforcement-audit-and-nprm.md`** — none are restated here.

## Cross-references

- `chunks/06-organizational-and-documentation.md` — §164.314 in full: BAA required provisions and the group-health-plan standard side by side.
- `chunks/01-scope-and-general-rules.md` — who is a CE/BA; the §164.306(b)(2) flexibility factors a lean benefits team will lean on.
- `use-cases/uc-02-ocr-readiness.md` — the 22-standard readiness method; swap the hospital system inventory for claims platforms and member portals.
- `industries/healthcare.md` — the provider-side CE playbook insurers can largely reuse.
- `nist-csf-2` (sibling skill, financial-services view) — the examiner-facing maturity narrative; its HIPAA touchpoints reference INTO this skill.
