---
industry: public-sector
parent_skill: hipaa-security-rule
title: "Public sector — state Medicaid and health agencies, hybrid entities, and public-records pressure vs the 6-year documentation retention floor"
version: 0.1.0
status: active
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2]
primary_personas: [State Medicaid agency ISO, State health department compliance officer, State gov IT audit director, County health system administrator]
regulatory_anchors: [HIPAA-Security-Rule, state-Medicaid-agency-obligations]
last_verified: "2026-06-10"
---

# Public sector — state Medicaid and health agencies

A state Medicaid agency is a **health plan** — a covered entity in its own right — and state and local health departments, public hospitals, and county behavioral-health programs sit somewhere on the CE/BA map too. Government entities bring three twists the private-sector playbook does not: the **hybrid entity** designation that draws the compliance boundary inside a sprawling agency, **public-records and state-archives regimes** that collide with security documentation, and procurement chains in which contractors and other agencies act as business associates. This view covers the government lens; the assessment method itself is UC-02's (`use-cases/uc-02-ocr-readiness.md`).

## The public-sector framing

### Which parts of a state agency does the Security Rule actually reach?

The Security Rule reaches ePHI held by the covered entity (or its BAs). A large state agency that performs both covered functions (the Medicaid plan, a public health clinic) and non-covered functions (licensing, vital records, environmental programs) may designate itself a **hybrid entity**, confining HIPAA obligations to designated health care components. The hybrid-entity mechanics live in 45 CFR 164.103/164.105 (Subpart A) — **outside this skill's Subpart C scope**; what matters here is the consequence: the §164.308(a)(1)(ii)(A) risk analysis must cover every system inside the designated components' ePHI boundary — the MMIS (Medicaid Management Information System), eligibility and enrollment systems, data warehouses, and the interfaces that cross the component boundary into the rest of the agency. Those internal boundaries need the same protection discipline as external ones, and the designation document is the first artifact an assessor asks for.

### How do public-records laws interact with §164.316(b)(2)(i)?

Carefully, and the distinction must never blur:

- **§164.316(b)(2)(i) Time limit (Required)** is a **RETENTION floor**: retain Subpart C documentation "for 6 years from the date of its creation or the date when it last was in effect, whichever is later." It is **retention — never a review cadence**. The review obligation is separate: §164.316(b)(2)(iii) Updates says review "periodically," with no stated interval (engagements pick a labeled house parameter, as UC-02 does with 3 years).
- **State records-retention schedules and archives laws** may demand longer retention, and public-records (FOIA-equivalent) requests may seek security policies, risk analyses, or incident documentation. Retention conflicts resolve upward (keep the longer period); disclosure questions belong to the state's public-records counsel — security documentation often falls under state exemptions for records whose release would jeopardize security, but that is state-law analysis this skill does not perform.
- The practical control: the documentation register (UC-02's `uc-02-documentation-register.json` pattern) carries both dates — last-reviewed (against the house review cycle) and creation/superseded (against the 6-year floor and the state schedule).

### Who are a Medicaid agency's business associates?

The fiscal agent operating the MMIS, managed-care enrollment brokers, data-analytics contractors, the state IT shared-services bureau when it hosts ePHI for the agency, and sometimes sister agencies. Each needs the §164.308(b)(3) written contract or other arrangement; for government entities, §164.314(a)(2)(ii) allows **"other arrangements"** meeting §164.504(e)(3) — a memorandum of understanding between agencies, or reliance on other law — in place of a standard BAA. The completeness check is UC-03's method (`use-cases/uc-03-baa-and-checklist.md`): the §164.314(a)(2)(i)(A)–(C) provisions, however the instrument is styled.

### What about state breach-notification overlays?

Pointer only: most states layer their own breach-notification statutes over the federal regime, often with different clocks and thresholds. Breach mechanics — federal (Subpart D) and state alike — are **out of this skill's scope**; the Subpart C touchpoint is §164.314(a)(2)(i)(C), which makes incident reporting (including §164.410 breaches) a required BAA provision.

## What's unique to public sector

- **Budget cycles meet §164.306(b)(2)(iii).** "The costs of security measures" is a legitimate flexibility factor, but it scales the *how*, never waives a standard — a legislature's appropriation calendar does not disposition a Required spec.
- **Legacy at state scale.** Decades-old MMIS modules raise the same §164.312(b) audit-controls problem as a hospital's legacy lab system (UC-02's High-priority gap pattern) — a standard, not an addressable spec, so the gap stays on the register until architecture compensates and remediation lands.
- **Workforce includes other agencies.** Data-sharing across components and agencies makes §164.308(a)(3)/(a)(4) access governance and the hybrid-entity boundary the same problem viewed twice.
- **Audits come from everywhere.** OCR, CMS program audits, state auditors, and legislative oversight may all probe the same program — one readiness matrix (UC-02's 22-standard method) serves all four masters better than four ad-hoc responses.

## Anti-hallucination

- **The 6-year figure is documentation retention (§164.316(b)(2)(i)) — never a review cadence**; the review obligation (§164.316(b)(2)(iii)) has no stated interval. This file exists partly to keep that distinction crisp under public-records pressure.
- **Hybrid-entity designation is Subpart A material (45 CFR 164.103/164.105)** — this skill flags the touchpoint and does not restate its mechanics.
- **No state-law advice**: public-records exemptions, state breach statutes, and records-retention schedules are pointers only.
- **Government CEs get no penalty discount in Subpart C** — enforcement posture details live once, as-of-dated, in `chunks/08-enforcement-audit-and-nprm.md`.
- **The 2025 NPRM (90 FR 898) is a Proposed Rule only as of 2026-06-10** [HIPAA-Security-NPRM-2025]; procurement language citing its proposals as current requirements is mislabeling.

## Cross-references

- `use-cases/uc-02-ocr-readiness.md` — the 22-standard readiness method; swap the hospital inventory for MMIS, eligibility, and warehouse systems.
- `use-cases/uc-03-baa-and-checklist.md` — the BAA/other-arrangement completeness check for fiscal agents and interagency MOUs.
- `chunks/06-organizational-and-documentation.md` — §164.314 (including the other-arrangements path) and §164.316 documentation discipline.
- `chunks/01-scope-and-general-rules.md` — CE/BA applicability and the flexibility factors.
- `nist-800-53-rmf` (sibling skill) — state agencies running NIST-aligned control baselines; the HIPAA crosswalk is deferred (SOX-638) — no mapping rows are asserted in either skill yet.
