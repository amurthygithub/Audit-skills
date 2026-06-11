# Limits and disclaimers — HIPAA Security Rule skill

## NPRM banner — read this first

**The 2025 Security Rule NPRM (90 FR 898, RIN 0945-AA22) is PROPOSED ONLY as of 2026-06-10.**
This was verified at the Federal Register docket level: the RIN query returns exactly one
document, of type "Proposed Rule" (doc 2024-30983, published 2025-01-06) — no final rule
exists under the RIN. Nothing in this skill treats NPRM items (mandatory encryption, MFA,
removal of the required/addressable distinction, scanning/pen-test cadences, asset inventory,
annual audits) as current law; they appear only in chunk 08, always flagged PROPOSED, and
never enter a current-law gap register (asserted by the oracle and adversarial tests).
**A final rule may drop at any time — re-verify NPRM status before any client use.**

## What this skill IS

- A reference for the structure of 45 CFR Part 164, Subpart C: 22 standards across
  Administrative (§164.308), Physical (§164.310), Technical (§164.312), Organizational
  (§164.314), and Policies/Documentation (§164.316), with the exact (Required)/(Addressable)
  designation per implementation specification
- A method for the §164.306(d)(3) addressable-specification decision workflow, the
  §164.308(a)(1)(ii)(A) risk analysis, OCR-readiness assessment, and BAA completeness checks
- A right-sizing guide via the §164.306(b)(2) flexibility-of-approach factors (org sizes
  1 → 6,000 demonstrated in the use cases)

## What this skill is NOT

- **Not legal advice.** Security Rule compliance determinations, preemption questions, and
  enforcement responses require qualified counsel. The authoritative text is the regulation;
  this skill's summaries are interpretive aids.
- **Not a "small entities are exempt" claim.** No such exemption exists. The flexibility
  factors scale HOW a standard is met, never WHETHER.
- **Not a Privacy Rule or Breach Notification Rule reference.** Subparts D and E are
  touchpoint-only here (e.g., §164.314(a)(2)(i)(C) → §164.410 incident reporting in BAAs).
- **Not a crosswalk source.** v1 encodes **no crosswalk rows** (CSF, 800-53, or otherwise).
  The authoritative mapping moved from SP 800-66r2 to the online NIST CPRT, targets CSF v1.1
  only, and is deferred to SOX-638. The skill points to CPRT/OLIR; it asserts no row.
- **Not an OCR audit protocol reproduction.** The protocol is referenced in prose only.

## Addressable ≠ optional

Per §164.306(d)(3), an Addressable implementation specification requires the covered entity
or business associate to: assess whether it is a reasonable and appropriate safeguard in its
environment; implement it if reasonable and appropriate; or document why it would not be
reasonable and appropriate and implement an equivalent alternative measure if reasonable and
appropriate. Every "Addressable" mention in this skill carries that decision logic — never
"optional," never "skippable."

## Penalty amounts adjust annually

Civil monetary penalty amounts are pinned in **one content location only**:
`chunks/08-enforcement-audit-and-nprm.md` §1 (the 2025 inflation-adjusted values, as of
2026-06-10; adjusted annually per 45 CFR 102.3 [CFR-45-102]); `docs/acceptance-gate.md`
additionally records them as verification evidence. This file deliberately restates
none of them. **These amounts adjust annually** — check the current 45 CFR 102.3 table before
quoting them. OCR's 2019 Notification of Enforcement Discretion (lower annual caps for tiers
1-3) is enforcement posture, not codified law, and is labeled as such wherever mentioned.

## House conventions are engagement parameters, not regulatory requirements

The fixtures and use-case docs use labeled house conventions that come from this skill's
engagement design, NOT from 45 CFR 164 or any NIST publication:

- **Risk bands**: score = likelihood (1-3) × impact (1-3); Low ≤2 / Medium 3-4 / High ≥6.
- **Gap priority**: standard missing → High; partial → Medium; stale policy document → Low.
- **3-year documentation review cycle**: the rule requires periodic review
  (§164.316(b)(2)(iii)) with **no stated cadence**; 3 years is the engagement parameter.

Wherever these appear they are labeled "house convention" / "engagement parameter." Do not
present them to a client or regulator as Security Rule requirements.

## Telemetry and ePHI

Seeds contain zero PHI (fictional org-level facts only), and **ePHI must never enter
telemetry events** — see `telemetry/redaction.md`. There is no wall-clock dependence in the
stub or tests; all date math runs off the seed `as_of_date`.

## When to escalate to a human

- Any determination with legal or enforcement consequences (penalty exposure, breach
  analysis, preemption)
- A disputed addressable-spec disposition (the documented decision is the client's, not the
  skill's)
- An OCR investigation, audit, or data request
- Any reliance on NPRM content — re-verify the docket first

## Anti-hallucination posture

This skill is born-vetted (process v3): every identifier and count was transcribed
mechanically from the official eCFR XML (2026-06-09 snapshot, retrieved 2026-06-10) into
`docs/hipaa-security-rule-fact-sheet.md` (repo root), and a standing CI test diffs the seed
inventory against that fact sheet. Currency claims (NPRM status, SP 800-66r2, PL 116-321,
penalty amounts) were settled by live fetches with verbatim anchors — see
`docs/acceptance-gate.md` (this skill). If you find a factual error, file an issue or open a
PR — the skill is maintained rigorously.
