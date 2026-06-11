---
title: "Industry views for SOX §302 Disclosure Controls & Procedures (15 U.S.C. 7241; 17 CFR 240.13a-14/15; Reg S-K Items 307/308)"
parent_skill: sox-302-disclosure-controls
type: industries-index
last_verified: "2026-06-11"
---

# Industry views — SOX §302 Disclosure Controls & Procedures

SOX §302 is one certification mandate with one structure — two signing officers, six certification elements, a quarterly DC&P evaluation — but it lands very differently on a newly-public SaaS company, a seasoned bank, a health-tech issuer, and a multi-entity manufacturer. Each industry view shows the sector-specific angle: which part of the obligation set dominates, which DC&P-vs-ICFR scoping question recurs, and which adjacent regime (§404, HIPAA breach, SOC 2, regulatory disclosure) gets confused with the §302 certification.

## Available industry views (alphabetical)

| Industry | File | When to use | Sector angle | Anchor sources |
|---|---|---|---|---|
| Financial services | financial-services.md | Bank, insurer, or asset manager as an accelerated / large accelerated filer with a mature SOX program. | The material-weakness §302/§404 interplay; a disclosure-relevant ICFR MW turns the DC&P conclusion not effective; the large sub-certification cascade; regulatory-disclosure overlap. | 15 U.S.C. 7241(a)(5), §240.13a-15(e)/(f), Item 307, Item 308 |
| Healthcare | healthcare.md | Public health-tech, digital-health, or life-sciences issuer. Non-financial-heavy disclosure: clinical, HIPAA/privacy, regulatory, cyber. | HIPAA/clinical matters as non-financial DC&P scope; the privacy + cyber 8-K Item 1.05 touchpoints; DC&P scope much broader than ICFR scope. | §240.13a-15(e), Item 307, Form 8-K Item 1.05 |
| Manufacturing | manufacturing.md | Multi-entity / multi-segment group with a parent filer over domestic and foreign subsidiaries. | The 15-entity sub-certification cascade; coverage-gap control; the foreign-private-issuer annual-vs-quarterly DC&P-evaluation split. | §240.13a-14, §240.13a-15(b), 15 U.S.C. 7241(a) |
| SaaS technology | saas-technology.md | Newly-public or pre-IPO technology issuer (recent IPO / EGC). | §302 applies from the first periodic report; §404(b) exempt but §302 is not; the disclosure committee; the non-financial (cyber 8-K) DC&P scope. | 15 U.S.C. 7241(a), §240.13a-14, §240.13a-15(e), Item 307 |

## How the views map to the use cases

- `financial-services.md` → UC-01 (Crestline Financial Corp, accelerated-filer MW interplay and 14-owner cascade).
- `saas-technology.md` → UC-02 (Nimbus Cloud Inc, newly-public first 302, disclosure committee, cyber scope, 404(b) exempt).
- `manufacturing.md` → UC-03 (Meridian Group, 15-entity cascade and the FPI annual-vs-quarterly nuance).
- `healthcare.md` → no dedicated seeded UC in v1; it reuses the UC-02 scope method with a health-tech disclosure inventory (HIPAA/clinical and privacy/cyber items as non-financial DC&P scope).

## Industries not in scope (use a different skill or view)

| Need | Where to go instead |
|---|---|
| The §404 ICFR assessment / auditor attestation mechanics | `coso-internal-controls` — this skill references the §302-vs-§404 boundary and does not re-teach §404 |
| HIPAA Breach Notification mechanics behind a healthcare cyber 8-K | `hipaa-security-rule` — this skill covers only the §302 DC&P / SEC 8-K side |
| SOC 2 report content for a SaaS issuer's disclosure-process evidence | `aicpa-soc-reporting` — pair with `saas-technology.md` for the evidence-reuse pattern |
| Executive cyber-maturity narrative behind the cyber-8-K DC&P touchpoint | `nist-csf-2` — pointer only; this skill stops at the §302 DC&P timeliness question |

## How to use an industry view

1. Open the view matching your sector and read the framing questions first — they answer the most common scoping mistakes ("are we exempt from §302 too?", "is an ICFR MW automatically a DC&P failure?", "quarterly or annual evaluation for foreign subs?").
2. Use the anchor-sources column to jump into the right chunks (chunks/01–07) and SKILL.md §1–§11.
3. Treat each view's anti-hallucination section as the known-traps list for that sector; the disclosure committee and sub-certification cascade are labeled house framework / recommended practice wherever they appear.
4. For a seeded, test-verified worked example, follow the view's use-case cross-reference — the seeds in `data/seeds/` are the contract and the oracles recompute every number.
