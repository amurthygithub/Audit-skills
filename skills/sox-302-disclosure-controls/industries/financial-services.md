---
industry: financial-services
parent_skill: sox-302-disclosure-controls
title: "Financial services — banks and insurers as accelerated filers: mature DC&P, the material-weakness §302/§404 interplay, regulatory-disclosure overlap, and the large sub-certification cascade"
version: 0.1.0
status: active
frameworks: [SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15, Reg-S-K-Item-307, Reg-S-K-Item-308]
primary_personas: [Controller, SEC-reporting manager, SOX program lead, Audit-committee liaison]
regulatory_anchors: [SOX-302, SOX-404, SEC-Release-33-8124, Form-8-K-Item-1.05]
last_verified: "2026-06-11"
---

# Financial services — the accelerated-filer lens

A bank, asset manager, or insurance group filing as an **accelerated or large accelerated filer** runs a mature SOX program: a standing disclosure committee, a large sub-certification cascade across business and control functions, and an annual §404(b) auditor attestation on top of the quarterly §302 certification. This view applies the skill to the seasoned financial-services issuer. The UC-01 engagement (`use-cases/uc-01-mw-interplay.md`, Crestline Financial Corp — accelerated filer, Q3 10-Q, unremediated ITGC material weakness) is the worked example.

## The accelerated-filer framing

### A new ICFR material weakness landed mid-year. What happens to the §302 certification now?

The material weakness flows into **both** SOX obligations, and the §302 effect is **immediate**:

- **§302 — this quarter.** If the material weakness is **unremediated** and affects a **disclosure-relevant area**, the officers cannot conclude DC&P is effective. The Item 307 DC&P conclusion turns **not effective** [Reg-S-K-Item-307 §229.307], and the ICFR material weakness is disclosed under Item 308 [Reg-S-K-Item-308 §229.308]. The cert ¶5 disclosure to the auditors and audit committee fires for any significant deficiency or material weakness [SOX-302-Statute-15USC7241 §7241(a)(5)].
- **§404 — at year-end.** The same MW flows into management's annual ICFR assessment (Item 308(a)) and — for an accelerated filer — the **auditor's §404(b) attestation**.

This is the **302/404 interplay**: one control failure, two distinct obligations, on two different cadences. §302 is the **quarterly officer certification**; §404 is the **annual management assessment + auditor attestation**. They are not the same thing. UC-01 §6 walks the interplay; `coso-internal-controls` owns the §404 mechanics.

### Isn't a material weakness in ICFR automatically a DC&P failure?

Only when it lands in a **disclosure-relevant area**. ICFR is a subset of DC&P for financial-statement matters, so an ICFR material weakness over a financially significant area (revenue, loan-loss allowance, investment valuation) is **also** a DC&P deficiency — the officers cannot conclude DC&P effective there [CFR-17-240.13a-15 §240.13a-15(e)/(f)]. The derivation is fact-driven: in UC-01 the ITGC logical-access weakness over the revenue system forces DC&P "not effective," and remediating it would flip the conclusion. The conclusion is never a default.

### How does the large sub-certification cascade work here?

A financial-services issuer typically runs a deep cascade — business lines, treasury, credit, actuarial, IT, legal, and external reporting each sub-certify up to the PEO/PFO. The cascade is a **house framework, not a rule** (the SEC recommended a disclosure committee in Release 33-8124; it did not mandate sub-certifications). The roll-up counts exceptions and decides whether the top-level cert is clean: in UC-01, 14 process owners roll up to **1 exception / 13 clean** (the IT/ITGC owner carrying the material weakness), and because DC&P is not effective and an exception exists, the **top-level cert is not clean**.

### How does regulatory disclosure overlap with §302 DC&P?

Banks and insurers carry parallel regulatory-reporting regimes (call reports, statutory filings, prudential disclosures). These overlap with — but do not replace — the §302 DC&P universe: DC&P covers all information required to be disclosed in **Exchange Act** reports, financial and non-financial [CFR-17-240.13a-15 §240.13a-15(e)]. A regulatory matter (an enforcement action, a capital event) is a §302 DC&P item when it must be disclosed in the issuer's 10-Q/10-K or an 8-K — including a material cybersecurity incident on 8-K Item 1.05.

## What's unique to financial-services issuers

- **Mature program, high stakes on the conclusion.** The DC&P effectiveness conclusion is closely watched; the MW-to-conclusion logic must be derived from facts and documented, not asserted.
- **Deep cascade.** More process owners and legal entities than a typical issuer; the roll-up footing (covered + gaps = total, clean + exceptions = total) is the control.
- **§404(b) always in play.** As an accelerated/large accelerated filer there is no §404(b) exemption — every MW that survives to year-end is auditor-attested.
- **ITGC is the recurring weak point.** Logical access, change management, and segregation of duties over financial systems are the most common material-weakness sources — and they are disclosure-relevant when they sit over revenue or other key accounts.

## Anti-hallucination

- **DC&P ≠ ICFR** — an ICFR material weakness is a DC&P matter only when it affects a disclosure-relevant area [CFR-17-240.13a-15 §240.13a-15(e)/(f)].
- **§302 ≠ §404** — the §302 quarterly officer certification and the §404 annual assessment/attestation are distinct; UC-01 shows the interplay, not an equivalence.
- **The sub-certification cascade is a house framework, not a rule** — Release 33-8124 recommended a disclosure committee; it did not mandate sub-certifications.
- **The DC&P conclusion is derived, never hard-coded** — change the MW facts (remediation status, disclosure relevance) and the conclusion changes.
- **This is not legal advice** — filer status and remediation timing turn on the issuer's specific facts; confirm with counsel and the auditor.

## Cross-references

- `use-cases/uc-01-mw-interplay.md` — the worked MW-interplay engagement: DC&P "not effective," ¶5 disclosure, 14-owner cascade (1 exception / 13 clean).
- `chunks/07-material-weakness-and-change.md` — the MW-to-DC&P-conclusion logic and the cyber-8-K touchpoint.
- `chunks/05-section-302-vs-404.md` — the §302-vs-§404 boundary (references `coso-internal-controls` for §404 mechanics).
- `chunks/06-disclosure-committee-subcert.md` — the disclosure-committee charter and sub-certification cascade (house framework).
- `coso-internal-controls` (sibling skill) — authoritative for the §404 ICFR assessment and auditor attestation mechanics.
