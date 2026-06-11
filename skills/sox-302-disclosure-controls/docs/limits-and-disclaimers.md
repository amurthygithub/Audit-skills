# Limits and disclaimers — SOX §302 Disclosure Controls skill

## DC&P ≠ ICFR — read this first

**Disclosure controls and procedures (DC&P) are NOT internal control over financial reporting
(ICFR).** DC&P (17 CFR 240.13a-15(e)) is the *broader* set: it covers ALL information an issuer
is required to disclose in its Exchange Act reports — financial AND non-financial (risk factors,
legal proceedings, MD&A, the cyber 8-K Item 1.05). ICFR (17 CFR 240.13a-15(f)) is the
*financial-reporting subset*: a process to provide reasonable assurance about the reliability of
financial reporting and GAAP-conforming statement preparation. ICFR sits inside DC&P for
financial-statement matters; DC&P adds the whole non-financial disclosure universe. An ICFR
material weakness is therefore also a DC&P matter, but a DC&P failure (e.g., a missed cyber 8-K)
need not be an ICFR failure. Never collapse the two.

## §302 ≠ §404

- **§302** = the officer **certification** (PEO + PFO) filed as a Rule 13a-14(a) / Item
  601(b)(31) exhibit, **quarterly and annual**, covering the officers' DC&P and ICFR
  conclusions (Item 307 / Item 308).
- **§404** = management's **annual ICFR assessment** (Item 308(a)) and, for **accelerated and
  large accelerated filers only**, the **auditor's ICFR attestation** (§404(b)).
- §302 is quarterly and officer-signed; §404(a)/(b) is annual and assessment/attestation-based.
  Do not describe a §302 certification as a §404 assessment, or vice versa.

## Newly-public / EGC are exempt from §404(b) — NEVER from §302

A newly-public filer and an emerging growth company (EGC) are exempt from the **§404(b) auditor
ICFR attestation**. They are **never** exempt from **§302**: the officer certification applies
from the **first periodic report**. §404(a) management ICFR assessment is required too (first in
the first annual report). The skill's UC-02 derives exactly this split — re-check filer status
before relying on any exemption.

## Disclosure committee and sub-certification cascade are recommended practice, not rule

The SEC **recommended** (it did not mandate) a disclosure committee in the 2002 adopting release
(Release 33-8124). The disclosure committee charter and the multi-entity / sub-certification
cascade modeled in this skill are **recommended practice / house framework** — engagement
design, NOT a rule requirement. Every place they appear they are labeled as such. Do not present
the cascade, a sub-certification roster, or a disclosure-committee charter to a client or
regulator as a §302/13a-14/13a-15 requirement.

## What this skill is NOT

- **Not legal advice.** DC&P effectiveness determinations, certification-liability questions, and
  enforcement responses require qualified counsel. The authoritative text is the statute (15
  U.S.C. 7241), the SEC rules (17 CFR 240.13a-14/-15), and Reg S-K (Items 307, 308, 601(b)(31));
  this skill's summaries are interpretive aids.
- **Not a §404 reference.** ICFR assessment and auditor-attestation mechanics (AS 2201) are
  `coso-internal-controls`; this skill references the §302↔§404 boundary, it does not re-teach
  §404.
- **Not a §906 reference.** The §906 criminal certification (18 U.S.C. 1350) is a **separate
  companion** cert; it is mentioned as the companion only and is **not detailed here**.
- **Not a crosswalk source.** v1 encodes **no crosswalk rows**. The cross-references to
  `coso-internal-controls` and the cyber-8-K touchpoint are one-way prose only.

## No MNPI in examples or telemetry

The seeds contain zero material non-public information (MNPI) — fictional issuer/entity-level
facts only — and **MNPI must never enter examples or telemetry events** (see
`telemetry/redaction.md`). There is no wall-clock dependence in the stub or tests; all date math
runs off the seed `as_of_date`.

## House conventions are engagement parameters, not regulatory requirements

The fixtures and use-case docs use labeled house conventions that come from this skill's
engagement design, NOT from the statute, the SEC rules, or Reg S-K:

- **Sub-certification cascade / disclosure committee**: a roll-up model (clean vs. exception
  sub-certifications foot to the top-level certification). Recommended practice per Release
  33-8124, not a rule mandate.
- **A top-level certification is "clean"** only when DC&P is effective and there are no open
  sub-certification exceptions: an engagement convention for the cascade, not a rule term.

Wherever these appear they are labeled "house convention" / "recommended practice." Do not
present them to a client or regulator as §302 requirements.

## Currency

The rule text is **current through the 2007 amendments** (implementing rules adopted 2002-2003,
amended through 72 FR 35321, June 27, 2007) **plus the 2023 cyber additions** (Release 33-11216:
8-K Item 1.05 material-cybersecurity-incident reporting — 4 business days from the materiality
determination — and Reg S-K Item 106, a DC&P scope expansion for non-financial timely
disclosure). The eCFR Title-17 2026-06-09 issue is current as transcribed.
**Re-verify the rule text and any cyber-disclosure deadline before client use** — a later
amendment may have landed.

## When to escalate to a human

- Any determination with legal or enforcement consequences (certification liability, a §302/§906
  exposure question, an SEC inquiry)
- A disputed DC&P or ICFR effectiveness conclusion (the documented officer conclusion is the
  client's, not the skill's)
- Any reliance on filer-status exemptions (newly-public / EGC / accelerated) — confirm status
  first
- Any cyber 8-K Item 1.05 materiality / timing call

## Anti-hallucination posture

This skill is born-vetted: every identifier, count, and verbatim definition was transcribed from
the official public federal text (15 U.S.C. 7241 from uscode.house.gov; 17 CFR 240.13a-14/-15
and Reg S-K Items 307/308/601(b)(31) from the eCFR) into
`docs/sox-302-disclosure-controls-fact-sheet.md` (repo root), and a standing CI test diffs the
skill's stated structure against that fact sheet. Currency claims (the 2007 amendment cutoff, the
2023 cyber additions) were settled by dated source checks — see `docs/acceptance-gate.md` (this
skill). If you find a factual error, file an issue or open a PR — the skill is maintained
rigorously.
