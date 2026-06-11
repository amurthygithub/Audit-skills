---
title: "Industry views for FedRAMP cloud authorization (Rev 5; FedRAMP Authorization Act of 2022, 44 U.S.C. 3607-3616; OMB M-24-15)"
parent_skill: fedramp-authorization
type: industries-index
last_verified: "2026-06-11"
---

# Industry views — FedRAMP cloud authorization

FedRAMP is one program — categorize a system (FIPS 199 high-water mark), select a Rev 5 baseline (Low 156 / Moderate 323 / High 410 / LI-SaaS 156), build the SSP/SAP/SAR/POA&M package, pass a 3PAO assessment, and run monthly ConMon — but it lands very differently on a SaaS vendor chasing its first ATO, the sponsoring agency that grants and leverages it, a fintech that needs the High baseline, and a health-tech CSP that must also satisfy HIPAA. Each industry view shows the sector-specific angle: which baseline dominates, which authorization-path question recurs, and which adjacent regime gets confused with the FedRAMP authorization.

Two facts are load-bearing in every view: **FedRAMP baselines ARE tailored NIST SP 800-53 Rev 5 controls** (not a separate catalog — that is `nist-800-53-rmf`), and **the current authorizer is the statutory FedRAMP Board under the 2022 Act and OMB M-24-15 — the JAB and its P-ATO are retired** [FEDRAMP-ACT-2022 §3610; OMB-M-24-15 §authority].

## Available industry views (alphabetical)

| Industry | File | When to use | Sector angle | Anchor sources |
|---|---|---|---|---|
| Financial services | financial-services.md | Fintech or gov-financial SaaS whose data impact pushes the system to the **High** baseline (410). | Data-impact categorization to High; the stricter ConMon expectations; the High-vs-Moderate control delta (410 vs 323). | FEDRAMP-REV5-BASELINES, FIPS-199, FEDRAMP-CONMON |
| Healthcare | healthcare.md | Health-tech CSP serving government health systems; PHI workloads in a federal cloud. | FedRAMP + HIPAA overlap (the control families that double-count); PHI workload categorization; pointer to `hipaa-security-rule`. | FEDRAMP-REV5-BASELINES, FIPS-199, NIST-800-53R5 |
| Public sector | public-sector.md | Sponsoring agency / authorizing official (AO) leveraging a package and granting the ATO. | Leveraging a package; the **presumption of adequacy**; ConMon oversight; the ATO decision; multi-agency reuse. | OMB-M-24-15, FEDRAMP-CONMON, FEDRAMP-PLAYBOOK |
| SaaS technology | saas-technology.md | CSP pursuing **Moderate via Agency Authorization** — the most common path. | SSP (~323 controls), 3PAO SAP/SAR, a ~40-item POA&M, monthly ConMon; categorization → Moderate → 323. | FEDRAMP-REV5-BASELINES, FEDRAMP-PLAYBOOK, A2LA-3PAO, FEDRAMP-CONMON |

## How the views map to the use cases

- `saas-technology.md` → UC-01 (Acme Cloud Suite — Moderate via Agency Authorization; categorize → 323 controls → POA&M severity SLAs).
- `saas-technology.md` (LI-SaaS branch) → UC-02 (Beacon Forms — Low-impact SaaS LI-SaaS readiness; 156 controls, method-designated; Rev 4 "66/90" not asserted).
- `public-sector.md` / 3PAO-assessor angle → UC-03 (Example 3PAO assessing Acme Cloud Suite — CSP-owned failed controls become findings; inherited excluded; residual-high AO risk note).
- `financial-services.md` → no dedicated seeded UC in v1; it reuses the UC-01 categorization method with a High-impact categorization (any objective High → overall High → 410).
- `healthcare.md` → no dedicated seeded UC in v1; it reuses the UC-01 / UC-02 categorization method with a PHI workload and a pointer to `hipaa-security-rule`.

## Industries not in scope (use a different skill or regime)

| Need | Where to go instead |
|---|---|
| The NIST SP 800-53 Rev 5 control catalog / general RMF (families, the RMF steps, selection mechanics) | `nist-800-53-rmf` — this skill cites the boundary (FedRAMP baselines are tailored 800-53 controls) and does not re-teach the catalog [NIST-800-53R5 §baselines] |
| HIPAA Security Rule mechanics behind a health-tech CSP's PHI workload | `hipaa-security-rule` — pair with `healthcare.md` for the FedRAMP + HIPAA overlap |
| DoD Impact Levels (IL2/4/5/6) / DISA SRG, GovRAMP (formerly StateRAMP), or CMMC | Distinct regimes — named as adjacent, not covered here |
| SOC 2 as the adjacent commercial assurance vs FedRAMP's federal authorization | `aicpa-soc-reporting` — one-line contrast only |

## How to use an industry view

1. Open the view matching your sector and read the framing questions first — they answer the most common scoping mistakes ("which baseline?", "is Moderate+SaaS LI-SaaS?", "who grants the ATO?", "do inherited controls go in our POA&M?").
2. Use the anchor-sources column to jump into the right chunks (`chunks/01`–`chunks/08`) and SKILL.md §1–§11.
3. Treat each view's anti-hallucination section as the known-traps list for that sector — the JAB-retired fact, the fixed baseline counts (156/323/410/156), and the "20x is emerging direction" caveat appear wherever they are relevant.
4. For a seeded, test-verified worked example, follow the view's use-case cross-reference — the seeds in `data/seeds/` are the contract and the oracles recompute every number.
