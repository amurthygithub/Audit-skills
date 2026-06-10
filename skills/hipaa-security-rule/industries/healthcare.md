---
industry: healthcare
parent_skill: hipaa-security-rule
title: "Healthcare providers — hospital covered-entity operations: workforce churn, medical devices and legacy systems, OCR readiness"
version: 0.1.0
status: active
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2, HHS-SRA-Tool, PL-116-321]
primary_personas: [Hospital CISO, HIPAA Security Officer, Compliance Director, Internal Audit, Clinical Engineering Lead]
regulatory_anchors: [HIPAA-Security-Rule, OCR-enforcement]
last_verified: "2026-06-10"
---

# Healthcare providers — hospital covered-entity operations

Hospitals and provider systems are the Security Rule's archetypal covered entities, and the place where its 2003-era text meets the hardest modern facts: thousands of workforce accounts turning over constantly, medical devices and legacy clinical systems that cannot run an EDR agent, and an OCR enforcement docket in which an inadequate risk analysis is the recurring finding. This view applies the skill to the hospital CE — the UC-02 engagement (`use-cases/uc-02-ocr-readiness.md`, Bellbrook Regional Health, 6,000 staff, 4 facilities) is the worked example.

## The hospital framing

### Why is workforce churn a Security Rule problem and not just an HR problem?

§164.308(a)(3) Workforce security carries three addressable specs — authorization and/or supervision (a)(3)(ii)(A), workforce clearance procedure (a)(3)(ii)(B), and termination procedures (a)(3)(ii)(C). All three are Addressable as written, but at hospital scale the §164.306(d)(3) assessment almost always lands on *implement*: a 6,000-person workforce with clinical rotations, students, locums, and contractors makes ad-hoc access handling indefensible "when analyzed with reference to the likely contribution to protecting electronic protected health information." The compliance artifact is twofold: the disposition record (see `chunks/07-addressable-decisions-and-evidence.md`) and the operational evidence — same-day termination of EHR access, periodic re-validation of role-based access against §164.308(a)(4) Information access management, and §164.308(a)(1)(ii)(C) sanctions actually applied when policy is violated.

### What do medical devices and legacy systems do to the §164.312 technical safeguards?

§164.312 makes no exception for devices that "can't." The hardest case is **§164.312(b) Audit controls** — a *standard* with no separately titled implementation specifications, so there is no addressable disposition path: a legacy lab system or infusion-pump gateway that contains or uses ePHI must have hardware, software, and/or procedural mechanisms that record and examine activity. Where the device itself cannot log, the procedural mechanism and the surrounding architecture (network segmentation, gateway-level capture) carry the load — and the gap stays on the remediation register until closed, exactly as UC-02 models with its legacy-lab-system finding. The same pattern hits §164.312(a)(2)(iii) automatic logoff (addressable — a nursing-station workstation may justify an alternative measure such as proximity-card locking, documented per §164.306(d)(3)) and encryption specs on devices with fixed firmware. Flexibility of approach (§164.306(b)(2)) lets a hospital pick the *how*; it never waives the standard.

### What does "OCR-ready" actually mean for a hospital?

Three artifacts, current and producible on request:

1. **A risk analysis that covers everything** (§164.308(a)(1)(ii)(A)): every system that creates, receives, maintains, or transmits ePHI — EHR, lab, PACS, patient portal, biomedical devices, and the research data warehouse everyone forgot. Scope misses are the classic finding.
2. **A disposition record for every addressable spec** (§164.306(d)(3)) and evidence that Required specs are implemented.
3. **Documentation that satisfies §164.316**: written (which may be electronic), retained 6 years from creation or last effective date (§164.316(b)(2)(i) — a retention floor, not a review cadence), available to the people who implement it (§164.316(b)(2)(ii)), and reviewed periodically (§164.316(b)(2)(iii) — the rule sets no cadence; pick one, label it as your own, and meet it).

§164.308(a)(8) Evaluation is the standing self-check: a periodic technical and nontechnical evaluation, repeated "in response to environmental or operational changes" — an EHR migration, a merger, a new telehealth platform all trigger it. Documenting recognized security practices in place for the prior 12 months can mitigate certain penalty/audit determinations under PL 116-321 — mitigation, not immunity [PL-116-321].

## What's unique to hospital CEs

- **Scale flips addressable math.** Specs a 10-person clinic might document around (log-in monitoring, security reminders) are nearly always *implement* at 6,000 staff — the §164.306(b)(2)(iv) probability-and-criticality factor dominates.
- **Hybrid clinical/IT ownership.** Clinical engineering owns devices, IT owns the network, compliance owns the rule. The risk analysis is the forcing function that puts all three in one inventory.
- **Contingency is patient safety.** §164.308(a)(7) (data backup, disaster recovery, emergency mode operation — all three Required) is about keeping ePHI available during downtime procedures, not just restoring files.
- **The BAA estate is large.** A hospital may hold hundreds of BAAs (§164.308(b)(1), §164.314(a)) — transcription, imaging, billing, cloud. UC-02 models the partial-status finding of an incomplete BAA inventory.

## Anti-hallucination

- **Addressable never means optional** — the only correct gloss is the §164.306(d)(3) decision logic [CFR-45-164-Subpart-C §164.306(d)(3)].
- **§164.312(b) Audit controls and §164.308(a)(8) Evaluation are standards with no separately titled specs**; the Appendix A matrix prints a standard-level (R) for them. Never restate them as addressable.
- **The 6-year figure (§164.316(b)(2)(i)) is documentation retention** — it is not a review cadence, not a record-of-care retention rule (medical-record retention is state law), and not a risk-analysis refresh interval.
- **The 2025 NPRM (90 FR 898) is a Proposed Rule only as of 2026-06-10** [HIPAA-Security-NPRM-2025] — see `chunks/08-enforcement-audit-and-nprm.md`; nothing in it is current law.
- **Penalty amounts are stated once, as-of-dated, in chunk 08** — this file deliberately repeats none.
- This skill covers Subpart C (ePHI security) only — Privacy Rule and Breach Notification mechanics are out of scope (touchpoints noted in `chunks/06-organizational-and-documentation.md`).

## Cross-references

- `use-cases/uc-02-ocr-readiness.md` — the worked hospital engagement (22-standard matrix, gap priorities, stale-doc flags, NPRM pre-read).
- `chunks/02-risk-analysis-and-management.md` — risk analysis as the anchor control; SP 800-66r2 cyclical approach; the HHS SRA Tool [HHS-SRA-Tool] (sized for small/medium practices; hospitals typically outgrow it).
- `chunks/05-technical-safeguards.md` — the §164.312 standards, including the audit-controls vs information-system-activity-review distinction.
- `chunks/07-addressable-decisions-and-evidence.md` — disposition records and the per-family evidence catalog.
- `nist-csf-2` (sibling skill) — for the executive maturity narrative on top of Security Rule compliance; its healthcare HIPAA references point INTO this skill.
