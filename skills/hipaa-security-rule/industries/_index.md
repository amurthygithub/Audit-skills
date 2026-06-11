---
title: "Industry views for the HIPAA Security Rule (45 CFR Part 164 Subpart C)"
parent_skill: hipaa-security-rule
type: industries-index
last_verified: "2026-06-10"
---

# Industry views — HIPAA Security Rule

The Security Rule is one regulation with one standard set (22 standards), but it lands very differently on a 6,000-staff hospital system, a 40-person health-tech SaaS, a bank's benefits function, and a state Medicaid agency. Each industry view shows the sector-specific angle: which standards dominate, which addressable dispositions recur, and which adjacent regimes (SOC 2, ERISA plan documents, public-records law) get confused with Subpart C obligations.

## Available industry views (alphabetical)

| Industry | File | When to use | Sector angle | Anchor standards |
|---|---|---|---|---|
| Financial services | financial-services.md | Employer sponsoring a group health plan (bank, asset manager, insurance group HR), or a health insurer as a covered entity. | §164.314(b) plan-document amendment specs (all Required); the §164.504(f)(2)(iii) adequate-separation firewall; insurers running the full CE program over claims platforms. | 164.314(b)(1)–(2), 164.308(b)(1), 164.314(a)(1) |
| Healthcare | healthcare.md | Hospital, provider system, or clinic as a covered entity. Workforce churn, medical devices/legacy clinical systems, OCR readiness. | Scale flips addressable math; §164.312(b) audit controls on devices that cannot log (a standard — no disposition path); the three OCR-ready artifacts. | 164.308(a)(1), 164.308(a)(3), 164.312(b), 164.308(a)(8) |
| Public sector | public-sector.md | State Medicaid/health agency, public hospital, county health program. Hybrid entities, interagency BAs, public-records pressure. | Hybrid-entity boundary (Subpart A pointer); public-records vs the 6-year RETENTION floor of §164.316(b)(2)(i) (retention, never a review cadence); other-arrangements path for interagency sharing. | 164.316(b)(2)(i), 164.314(a)(2)(ii), 164.308(b)(3) |
| SaaS technology | saas-technology.md | Health-tech SaaS or cloud vendor handling ePHI as a business associate. Direct liability, subprocessor chains, cloud shared responsibility. | BA direct liability; BAA flow-down per §164.308(b)(2); inherited facility controls as documented dispositions; SOC 2 evidence reuse labeled overlap-not-equivalence. | 164.308(b)(2), 164.314(a)(2)(i), 164.312(a)(2)(iv) |

## How the views map to the use cases

- `healthcare.md` → UC-02 (Bellbrook Regional Health, hospital CE readiness assessment).
- `saas-technology.md` → UC-01 (CareSync Relay, BA risk analysis + addressable dispositions) and UC-03 (Meridian HIT Consulting, solo BA).
- `financial-services.md` and `public-sector.md` → no dedicated seeded UC in v1; both reuse the UC-02 readiness method and the UC-03 BAA-check method with a sector-specific system inventory.

## Industries not in scope (use a different skill or view)

| Need | Where to go instead |
|---|---|
| Executive cyber-maturity narrative on top of HIPAA compliance | `nist-csf-2` (its healthcare industry view is deferred to its v1.0; when it ships it will reference INTO this skill rather than restate Subpart C facts) |
| SOC 2 report content and engagement lifecycle for a BA | `aicpa-soc-reporting` (pair with `saas-technology.md` here for the evidence-reuse pattern) |
| NIST control-catalog depth (800-53) for a government health agency | `nist-800-53-rmf` — the HIPAA crosswalk is deferred to SOX-638; no mapping rows asserted yet |
| Privacy Rule, Breach Notification mechanics, 42 CFR Part 2, state privacy law | Out of this skill's scope entirely (see chunk 01, scope and general rules) |

## How to use an industry view

1. Open the view matching your sector and read the framing questions first — they answer the most common scoping mistakes (e.g., "isn't HIPAA our customers' problem?", "is the 6-year rule a review cycle?").
2. Use the anchor standards column above to jump into the right chunks.
3. Treat each view's anti-hallucination section as the known-traps list for that sector; every house convention is labeled where it appears.
4. For a seeded, test-verified worked example, follow the view's use-case cross-reference — the seeds in `data/seeds/` are the contract.
