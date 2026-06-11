---
industry: saas-technology
parent_skill: sox-302-disclosure-controls
title: "SaaS / technology — newly-public and pre-IPO issuers: the first §302 certification applies immediately, §404(b) is exempt but §302 is not, the disclosure committee, and the non-financial (cyber 8-K) DC&P scope"
version: 0.1.0
status: active
frameworks: [SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15, Reg-S-K-Item-307, Reg-S-K-Item-308]
primary_personas: [SEC-reporting manager, Disclosure-committee chair, CFO/Controller, General Counsel]
regulatory_anchors: [SOX-302, JOBS-Act-EGC, SEC-Release-33-8124, Form-8-K-Item-1.05]
last_verified: "2026-06-11"
---

# SaaS / technology — the newly-public issuer lens

A technology company that has just completed an IPO — or is in the S-1 process building toward one — faces the §302 certification obligation **from its first periodic report**, on day one as a reporting company. This view applies the skill to the newly-public / pre-IPO tech issuer. The UC-02 engagement (`use-cases/uc-02-newly-public-first-302.md`, Nimbus Cloud Inc — newly-public EGC, first periodic report) is the worked example.

## The newly-public framing

### "We're an EGC and exempt from SOX §404(b) — are we exempt from §302 too?"

**No.** The §404(b) auditor-attestation exemption (for an emerging growth company under the JOBS Act, and during the newly-public transition) does **not** carry §302 with it. SOX §302 requires the PEO and PFO to certify each annual and quarterly report [SOX-302-Statute-15USC7241 §7241(a)], filed as an exhibit under Rule 13a-14 [CFR-17-240.13a-14 §240.13a-14(a)] — from the **first periodic report**. There is no newly-public or EGC exemption from §302. The exemptions you do get are narrower than they sound:

- **§404(b) auditor ICFR attestation — exempt** as an EGC / newly-public filer (the EGC exemption can run up to five years).
- **§404(a) management ICFR assessment — owed**, first appearing in your **first annual report** (Item 308(a)).
- **§302 certification — owed from the first periodic report**, with the Item 307 DC&P conclusion [Reg-S-K-Item-307 §229.307].

Conflating the §404(b) exemption with §302 is the single most common newly-public mistake; UC-02 §3 walks the split and the adversarial test enforces that §302 is never waived.

### What does the first-year disclosure committee do?

The SEC **recommended** a disclosure committee in its 2002 adopting release (Release 33-8124) but did **not mandate** one — so the disclosure committee is **recommended practice, not a rule**. For a newly-public issuer it is the practical engine of DC&P: it operates the §240.13a-15(e) accumulation-and-communication process — pulling disclosure-relevant information from finance, legal, IR, product, and engineering to management in time to make disclosure decisions [CFR-17-240.13a-15 §240.13a-15(e)]. A first-year charter typically names a chair (often the CFO or GC), sets a quarterly calendar tied to the 10-Q/10-K cycle, and defines the sub-certification inputs. Standing it up does not change the §302 obligation — that already applies in full — but it makes the certification defensible.

### Why is the cyber-incident 8-K a §302 (DC&P) issue and not a §404 (ICFR) issue?

Because DC&P is **broader than ICFR**. A material cybersecurity incident is disclosed on **Form 8-K Item 1.05 within 4 business days of the materiality determination** — a **non-financial, timely-disclosure** obligation. It sits in DC&P (controls that ensure information "is recorded, processed, summarized and reported, within the time periods specified" [CFR-17-240.13a-15 §240.13a-15(e)]) and **not** in ICFR (which is limited to the reliability of financial reporting [CFR-17-240.13a-15 §240.13a-15(f)]). A missed cyber-8-K is a DC&P failure that need not be an ICFR failure. UC-02 §5 puts the cyber-incident item in DC&P scope and out of ICFR scope.

## What's unique to newly-public tech issuers

- **The obligation set is asymmetric.** §302 from day one; §404(a) at the first annual report; §404(b) deferred or exempt. State each precisely — "we're not a full SOX filer yet" is wrong about §302.
- **Non-financial scope dominates early.** A high-growth tech issuer's biggest DC&P risks are often non-financial: risk factors, cyber incidents, product/legal proceedings, MD&A forward-looking statements — all in DC&P scope, none in ICFR scope.
- **The disclosure committee is the first thing to build, and it is optional-but-expected.** Label it recommended practice; treat it as table stakes for a defensible first certification.
- **SOC 2 is disclosure-process evidence, not a §302 substitute.** A SaaS issuer's SOC 2 Type II exercises overlapping operational controls; reuse the evidence, but the §302 certification and the DC&P evaluation are separate artifacts (`aicpa-soc-reporting` is authoritative for SOC 2 content).

## Anti-hallucination

- **§404(b) exemption never exempts §302** — §302 applies from the first periodic report regardless of EGC / newly-public status [SOX-302-Statute-15USC7241 §7241(a); CFR-17-240.13a-14 §240.13a-14(a)].
- **The disclosure committee is recommended practice, not a rule** — Release 33-8124 recommended it; no rule mandates it.
- **DC&P ≠ ICFR** — the cyber-8-K and other non-financial items are DC&P scope, not ICFR scope [CFR-17-240.13a-15 §240.13a-15(e)/(f)].
- **§302 ≠ §404** — §302 is the quarterly officer certification; §404(a)/(b) are the annual management assessment and auditor attestation.
- **This is not legal advice** — EGC status and transition periods turn on the issuer's specific facts (IPO date, revenue thresholds); confirm with counsel.

## Cross-references

- `use-cases/uc-02-newly-public-first-302.md` — the worked first-302 engagement: obligation split and the 7-item DC&P / 3-item ICFR scope.
- `chunks/05-section-302-vs-404.md` — the §302-vs-§404 boundary and the newly-public / EGC exemptions.
- `chunks/06-disclosure-committee-subcert.md` — the disclosure-committee charter and sub-certification cascade (house framework).
- `chunks/07-material-weakness-and-change.md` — the cyber-8-K Item 1.05 DC&P touchpoint (4 business days).
- `aicpa-soc-reporting` (sibling skill) — authoritative for SOC 2 report content; pair it for the disclosure-process evidence-reuse pattern.
