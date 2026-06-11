---
chunk_id: 08-fedramp-20x-and-modernization
parent_skill: fedramp-authorization
topic: "FedRAMP 20x (EMERGING DIRECTION, not the settled Rev 5 process) — automation-first, outcome-based; Key Security Indicators (KSIs); machine-readable packages (RFC 0024); OSCAL artifacts and the OSCAL-Foundation mirror (the GSA OSCAL repo is retired); how 20x realizes the presumption of adequacy; what is SETTLED (Rev 5) vs what is DIRECTION (20x)"
load_when: "user asks about FedRAMP 20x, KSIs / Key Security Indicators, machine-readable or automated authorization packages, RFC 0024, OSCAL artifacts, where the OSCAL baselines live, or how FedRAMP is modernizing"
---

# Chunk 08 — FedRAMP 20x and modernization (EMERGING DIRECTION)

**FedRAMP 20x is an emerging direction, not the settled Rev 5 process a CSP certifies against today.** Treat everything in this chunk as **direction**: it orients you to where the program is heading (automation-first, outcome-based, machine-readable), but it is **not** a set of current binding requirements. When a question is about what to do today, the answer is the **settled Rev 5** process (chunks 01–07); 20x is the trajectory layered on top of it.

## 1. What FedRAMP 20x is

FedRAMP 20x is the **automation-first, outcome-based** modernization track for the program, pursued under the authority of the 2022 Act and OMB M-24-15 (`chunks/01-fedramp-and-governance.md`). Its goal is to shift authorization and continuous monitoring from document review toward **machine-readable evidence** and **measurable outcomes**.

- **Automation-first:** authorization and ConMon artifacts are produced and checked by machine rather than assembled and read as prose documents.
- **Outcome-based:** assessment focuses on whether security **outcomes** are demonstrably met, not only on whether a control narrative was written.

## 2. The 20x concepts (orienting, not binding)

- **Key Security Indicators (KSIs):** outcome-oriented security signals — the things a system must demonstrably achieve — used to express and check security posture in an automatable way.
- **Machine-readable packages (RFC 0024):** the authorization package as structured, machine-readable data rather than narrative documents. RFC 0024 is part of the 20x RFC track that defines this direction.
- **OSCAL artifacts:** the Open Security Controls Assessment Language is the machine-readable format for baselines, SSP, assessment, and POA&M data. M-24-15 pushed machine-readable artifacts (OSCAL until NIST designates a successor); 20x builds on that.

These concepts are how 20x is described **today**; the specific mechanics are still moving and are tracked through the 20x RFC process.

## 3. Where the OSCAL artifacts live (the retired-repo trap)

The **PMO-authored OSCAL Rev 5 baseline profiles** are the machine-readable, count-authoritative source for the four baselines (Low 156 / Moderate 323 / High 410 / LI-SaaS 156).

- They now live at the **OSCAL-Foundation/fedramp-resources** mirror (`/baselines/rev5/json/FedRAMP_rev5_*-baseline_profile.json`) [FEDRAMP-REV5-BASELINES §counts].
- **The old GSA OSCAL repo `github.com/GSA/fedramp-automation` is RETIRED (404).** Do **not** cite it; use the OSCAL-Foundation mirror.

## 4. How 20x realizes the presumption of adequacy

The **presumption of adequacy** (M-24-15: an agency must presume a FedRAMP authorization package adequate for a product at a given FIPS 199 impact level — see `chunks/03-authorization-paths.md`) depends on packages being trustworthy and reusable. 20x advances that goal: **machine-readable, KSI-driven, continuously-validated** packages make reuse faster and more verifiable than re-reading prose, so an agency can lean on an existing authorization with less manual reassessment. 20x is the **mechanism** the program is building to make the presumption of adequacy operationally real — but the presumption itself is already settled M-24-15 policy.

## 5. Settled (Rev 5) vs direction (20x)

| Topic | SETTLED — Rev 5 (today) | DIRECTION — 20x (emerging) |
|-------|--------------------------|-----------------------------|
| Authorization path | Agency Authorization; presumption of adequacy (M-24-15) | Automation-first, KSI/outcome-based flow |
| The package | SSP / SAP / SAR / POA&M (largely document-based) | Machine-readable packages (RFC 0024) |
| Evidence of posture | Control narratives + 3PAO assessment | Key Security Indicators (KSIs) |
| Format | OSCAL pushed by M-24-15 (machine-readable artifacts) | OSCAL-native, automated validation |
| Status | Binding — what a CSP certifies against now | Direction — do not certify against it as a current rule |

Use the **left column** to answer "what do I do today." Use the **right column** only to explain **where the program is going** — and say so explicitly.

## 6. How to track 20x

1. **Default to Rev 5** for any operational answer (chunks 01–07); state 20x only as direction.
2. **Re-verify the 20x RFC status** (including RFC 0024 and the KSI definitions) **before** relying on any 20x mechanic — the RFC track is active and moving.
3. **Use the OSCAL-Foundation mirror** for the OSCAL baselines; never the retired GSA repo.
4. **Label every 20x statement as emerging** — do not present a 20x concept as a current binding requirement.

## 7. Output template — settled-vs-emerging summary

```
Topic: <authorization path | package | evidence | format>
  SETTLED (Rev 5, binding today):  <the current Rev 5 answer + citation>
  DIRECTION (FedRAMP 20x, emerging): <the 20x trajectory — KSIs / RFC 0024 / OSCAL>
  Caveat: 20x is direction, not a current binding requirement; re-verify RFC status before relying on it.
```

## 8. Anti-hallucination

- **FedRAMP 20x is an emerging direction, NOT a current binding rule.** Do not state 20x mechanics (KSIs, machine-readable packages, RFC 0024) as current requirements a CSP certifies against today. The settled process is Rev 5 (chunks 01–07).
- **The GSA OSCAL repo `github.com/GSA/fedramp-automation` is retired (404)** — use the **OSCAL-Foundation/fedramp-resources** mirror for the OSCAL baselines [FEDRAMP-REV5-BASELINES §counts].
- **Re-verify the 20x RFC status** (e.g., RFC 0024 and the KSIs) **before relying on it** — the 20x RFC track is active and changing.
- **20x advances the presumption of adequacy**, but the presumption itself is settled M-24-15 policy (`chunks/03-authorization-paths.md`); do not conflate the direction with the existing rule.
- This skill encodes public FedRAMP/OMB/NIST text current to 2026-06 and is **not authorization or legal advice**.
