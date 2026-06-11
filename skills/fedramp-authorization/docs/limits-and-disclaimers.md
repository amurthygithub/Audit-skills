# Limits and disclaimers — FedRAMP Cloud Authorization skill

## FedRAMP baselines ARE the 800-53 catalog, tailored — read this first

**FedRAMP does NOT invent a control catalog.** Its Low / Moderate / High baselines are the NIST SP
800-53B Low / Moderate / High control baselines (**149 / 287 / 370** controls) tailored **up** with
FedRAMP-specific additional controls and parameter values — yielding **156 / 323 / 410**. The
control IDs are the SAME 800-53 Rev 5 catalog (AC-2, SI-2, AU-6, …); LI-SaaS shares Low's exact set
(**156** = 135 base + 21 enhancements). This skill covers the FedRAMP **program / process** layer
(categorization → baseline → package → assessment → ConMon); the control catalog, the control
families, and the general RMF are `nist-800-53-rmf`. Never describe the FedRAMP baselines as a
separate catalog, and never re-teach the 800-53 control catalog from inside this skill — cite the
boundary and stop.

## The FedRAMP Board ≠ the JAB — governance currency

The **FedRAMP Authorization Act of 2022** (44 U.S.C. 3610) established the statutory **FedRAMP
Board**, which replaced the Joint Authorization Board (JAB). **OMB M-24-15 (2024-07-25)** retired the
JAB P-ATO model — legacy "JAB P-ATO" authorizations were **re-designated** by the FedRAMP PMO. Do
**not** describe the JAB as a current authorizing body: it is retired. **Agency Authorization** is the
operative Rev 5 path; M-24-15 adds multi-agency authorization and the **presumption of adequacy**
(an agency must presume a FedRAMP package adequate at a given FIPS 199 impact level, reducing
duplicative agency-by-agency reassessment). Confirm the current governance model before any
authorization-path answer — the source ticket's pre-2022 "JAB → PMO" framing is outdated.

## FedRAMP 20x is an emerging direction, not the settled Rev 5 process

**FedRAMP 20x** is the automation-first, outcome-based modernization track (authority: the 2022 Act +
M-24-15). Its concepts — **Key Security Indicators (KSIs)** and **machine-readable packages** — are
**direction**, not the Rev 5 process a CSP certifies against today. Label 20x as emerging everywhere
it appears; never state 20x mechanics as current requirements. Re-verify the active 20x RFCs before
relying on any 20x detail — the track is moving.

## LI-SaaS is Low-impact SaaS ONLY

The **LI-SaaS (Tailored)** baseline applies **only** to a **Low-impact** offering delivered as
**SaaS**. Eligibility = `overall FIPS 199 impact == Low AND SaaS-delivered`. A **Moderate** (or
**High**) impact system — **even if SaaS-delivered** — takes the full Moderate (**323**) or High
(**410**) baseline, **not** LI-SaaS. Treating "Moderate + SaaS" as LI-SaaS is a common, load-bearing
misconception the skill exists to refuse; the eligible Tailored baseline is **156** controls = **66**
3PAO-tested + **90** CSP-attested (the 66/90 split is documented in the Tailored LI-SaaS baseline
doc, **not** a flat OSCAL count).

## The ATO is the AO's decision — not derived here

The **Authorization to Operate (ATO)** is the **authorizing official's** risk-based decision. A 3PAO
**recommends** (it does not grant the ATO); this skill computes the categorization, the baseline, the
POA&M deadlines, and the finding roll-up, and it flags residual high-severity findings as a risk
signal — but it does **not** issue, derive, or guarantee an ATO. The ATO decision belongs to the AO
and is explicitly out of the stub's derivation surface.

## Inherited / leveraged controls are the provider's responsibility

Controls **inherited** or **leveraged** from an underlying provider (e.g., an IaaS/PaaS provider's
controls) are **not re-tested by, and not in the POA&M of, the leveraging CSP** — they belong to the
provider's authorization package and POA&M. The SAR finding roll-up counts only the controls the CSP
**owns** that failed testing; marking a failed control `inherited` removes it from the leveraging
CSP's POA&M (asserted as a metamorphic invariant).

## Counts are Rev 5 as of 2026-06

The baseline counts are **Rev 5** (post-May-2023 800-53 Rev 5 transition), counted directly from the
PMO-authored OSCAL Rev 5 baseline profiles: **Low 156** (135 + 21), **Moderate 323** (181 + 142),
**High 410** (191 + 219), **LI-SaaS 156** (= Low's set; 66 tested + 90 attested); 800-53B baselines
**149 / 287 / 370**. **325 is the Rev 4 Moderate count, not Rev 5** — do not restate the totals with
other numbers. Two source traps are recorded and avoided: the retired
`github.com/GSA/fedramp-automation` repo (404 — use the OSCAL-Foundation mirror), and the fedramp.gov
`.xlsx` baseline workbook URL that resolves 200 but serves an **empty S3 redirect stub** (not cited
as the count source). **Re-verify currency before client use** — a later 800-53 maintenance release or
a 20x change may have landed (NIST SP 800-53 is still Rev 5 — no Rev 6 — as of 2026-06).

## What this skill is NOT

- **Not authorization or legal advice.** The ATO is the AO's risk-based decision; certification,
  authorization, and enforcement questions require qualified counsel and the sponsoring agency. The
  authoritative text is the statute (44 U.S.C. 3607-3616), OMB M-24-15, the fedramp.gov Rev 5
  playbook, and NIST SP 800-53 Rev 5; this skill's summaries are interpretive aids.
- **Not the 800-53 catalog / RMF.** The control catalog, the control families, and the general RMF
  are `nist-800-53-rmf`; this skill references the boundary, it does not re-teach the catalog. No
  per-control baseline enumeration (300+ rows) in v0.1.0 — counts + tailoring relationship only.
- **Not a DoD / StateRAMP / CMMC reference.** DoD Impact Levels (IL2/4/5/6) / DISA SRG, StateRAMP,
  and CMMC are distinct regimes — named as adjacent, not covered here.
- **Not a substitute for the CSP's own package.** The SSP/SAP/SAR/POA&M are the CSP's and 3PAO's
  obligation; this skill structures the program and explains the package, it does not author a real
  SSP/SAR document.
- **Not a crosswalk source.** v1 encodes **no crosswalk rows** — the baselines are 800-53 controls
  (identity, not a mapping); the cross-reference to `nist-800-53-rmf` is one-way prose only.

## No real package data in examples or telemetry

The seeds contain zero real FedRAMP package data — fictional CSPs/systems (Acme Cloud Suite, Beacon
Forms, Example 3PAO) and structural facts only — and no real system names, IP addresses, or
vulnerability data may enter examples or telemetry events (see `telemetry/redaction.md`). All date
math (POA&M deadlines) runs off the seed `identified_date` / `as_of_date` fields; there is no
wall-clock dependence in the stub or tests.

## When to escalate to a human

- Any determination with authorization or legal consequences (the ATO decision, an authorization
  dispute, an OMB / agency inquiry) — the AO and qualified counsel own these
- A disputed FIPS 199 categorization or a contested baseline selection
- Any reliance on the presumption of adequacy or a leveraged authorization — confirm the underlying
  package's scope and currency first
- Any LI-SaaS eligibility edge case (especially a SaaS offering at Moderate impact)
- Any reliance on a FedRAMP 20x construct — confirm the active RFC status first

## Anti-hallucination posture

This skill is born-vetted: every identifier, count, and verbatim definition was transcribed from the
official public US-government text — the FedRAMP Authorization Act (44 U.S.C. 3607-3616,
law.cornell.edu), OMB M-24-15, fedramp.gov Rev 5 playbook pages, A2LA, and NIST SP 800-53 Rev 5 /
800-53B — into `docs/fedramp-authorization-fact-sheet.md` (repo root), and the baseline counts were
counted directly from the PMO-authored OSCAL Rev 5 baseline profiles. The two highest fidelity risks
are (1) presenting the JAB as a current authorizer (it is retired — explicit grep gate +
adversarial test) and (2) a wrong baseline count (inventory-diff gate against the fact sheet's
156/323/410/156 and 149/287/370). If you find a factual error, file an issue or open a PR — the
skill is maintained rigorously.
