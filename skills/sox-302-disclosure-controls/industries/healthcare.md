---
industry: healthcare
parent_skill: sox-302-disclosure-controls
title: "Healthcare — health-tech and life-sciences issuers: HIPAA/clinical matters as non-financial DC&P scope, the privacy/cyber 8-K touchpoints, and the DC&P-vs-ICFR line for regulatory disclosure"
version: 0.1.0
status: active
frameworks: [SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15, Reg-S-K-Item-307, Reg-S-K-Item-308]
primary_personas: [SEC-reporting manager, General Counsel / Chief Compliance Officer, Disclosure-committee chair, CISO/Privacy Officer]
regulatory_anchors: [SOX-302, Form-8-K-Item-1.05, HIPAA-Breach-Notification, SEC-Release-33-8124]
last_verified: "2026-06-11"
---

# Healthcare — the health-tech issuer lens

A publicly traded health-tech, digital-health, or life-sciences company carries a disclosure universe that is unusually **non-financial-heavy**: clinical results, regulatory approvals, HIPAA/privacy events, and material cybersecurity incidents are all disclosure-relevant, and most of them sit in DC&P scope rather than ICFR scope. This view applies the skill to the health-tech issuer. There is no dedicated seeded UC for healthcare in v1; it reuses the UC-02 scope method (`use-cases/uc-02-newly-public-first-302.md`) with a health-tech disclosure inventory.

## The health-tech framing

### Are HIPAA and clinical matters part of our §302 certification?

When they are **required to be disclosed in an Exchange Act report, yes — as DC&P, not ICFR.** DC&P covers all information required to be disclosed in the issuer's reports, financial **and** non-financial [CFR-17-240.13a-15 §240.13a-15(e)]. A material HIPAA breach, an adverse clinical-trial result, an FDA action, or a privacy enforcement matter is a §302 DC&P item when it must be disclosed in the 10-Q/10-K (risk factors, legal proceedings, MD&A) or on an 8-K. ICFR, by contrast, is limited to the reliability of financial reporting [CFR-17-240.13a-15 §240.13a-15(f)] — so these clinical and privacy matters are **outside** ICFR scope but **inside** DC&P scope. They flow into the Item 307 DC&P conclusion [Reg-S-K-Item-307 §229.307], not the Item 308 ICFR report.

### Where do the privacy and cyber 8-K touchpoints fit?

A **material cybersecurity incident** is disclosed on **Form 8-K Item 1.05 within 4 business days of the materiality determination** — a non-financial **timely-disclosure** DC&P obligation. For a health-tech issuer a single event can trigger two parallel regimes: the **SEC 8-K Item 1.05** disclosure (a §302 DC&P matter) and the **HIPAA Breach Notification** obligations (a different rule entirely — see `hipaa-security-rule`). The §302 DC&P question is whether the issuer's controls surfaced and reported the incident to management in time to make the Exchange Act disclosure decision. A missed 8-K Item 1.05 is a DC&P failure that need not be an ICFR failure.

### The DC&P controls must reach into clinical and compliance functions

The accumulation-and-communication requirement [CFR-17-240.13a-15 §240.13a-15(e)] means the disclosure committee (recommended practice, Release 33-8124 — **not a rule**) has to pull disclosure-relevant information from functions a typical issuer's committee never touches: clinical/medical affairs, regulatory affairs, the privacy office, and information security. A health-tech disclosure inventory therefore weights heavily toward non-financial items, and the DC&P scope is materially broader than the ICFR scope — the same asymmetry UC-02 demonstrates with 7 DC&P items against 3 ICFR items.

## What's unique to health-tech issuers

- **Non-financial scope dominates.** Clinical, regulatory, HIPAA/privacy, and cyber items make DC&P scope much larger than ICFR scope; scope each item to the right universe.
- **One event, two regimes.** A breach can be both an SEC 8-K Item 1.05 matter (§302 DC&P) and a HIPAA Breach Notification matter (different rule); do not collapse them.
- **The disclosure committee needs unusual reach.** Clinical/medical affairs and the privacy office are disclosure sources, not just finance and legal — the committee charter (house framework) must name them.
- **Newly-public is common here.** Many health-tech issuers are recent IPOs / EGCs; the newly-public obligation split (UC-02) applies — §302 from day one, §404(b) exempt, §404(a) at the first annual report.

## Anti-hallucination

- **DC&P ≠ ICFR** — clinical, HIPAA/privacy, and cyber matters are non-financial DC&P scope, not ICFR scope [CFR-17-240.13a-15 §240.13a-15(e)/(f)].
- **§302 ≠ §404** — the §302 quarterly officer certification covers the DC&P conclusion; §404 is the annual ICFR assessment/attestation.
- **The SEC 8-K Item 1.05 cyber disclosure and HIPAA Breach Notification are different regimes** — this skill covers only the §302 DC&P side; breach mechanics live in `hipaa-security-rule`.
- **The disclosure committee is recommended practice, not a rule** — Release 33-8124 recommended it.
- **This is not legal advice** — materiality of clinical, regulatory, and privacy events turns on specific facts; confirm with counsel.

## Cross-references

- `use-cases/uc-02-newly-public-first-302.md` — the worked scope method (7 DC&P items / 3 ICFR items; cyber 8-K in DC&P scope), reused with a health-tech inventory.
- `chunks/02-dcp-vs-icfr.md` — the DC&P-vs-ICFR boundary and the non-financial disclosure universe.
- `chunks/07-material-weakness-and-change.md` — the cyber-8-K Item 1.05 DC&P touchpoint (4 business days).
- `chunks/06-disclosure-committee-subcert.md` — the disclosure-committee charter (house framework) and its reach into clinical/privacy functions.
- `hipaa-security-rule` (sibling skill) — authoritative for the HIPAA Breach Notification regime; this skill covers only the §302 DC&P / SEC 8-K side.
