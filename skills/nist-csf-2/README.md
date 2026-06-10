---
name: nist-csf-2
description: "NIST Cybersecurity Framework 2.0 — 6 Functions (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER), 22 Categories, 106 Subcategories, Tiers 1-4, Organizational Profile. Apply this skill when the user asks about CSF 2.0, organizational cyber maturity, FFIEC-era migration to CSF (the CAT was sunset Aug 2025), SOC 2-to-CSF mapping, or executive cyber reporting."
category: audit-framework
risk: informational
source: NIST CSWP 29 (Feb 26, 2024)
date_added: 2026-06-09
version: 0.1.0
status: draft
industries: [financial-services, public-sector, saas-technology, manufacturing]
frameworks: [NIST-CSF-2.0, NIST-SP-800-53-Rev5.1.1, NIST-SP-800-171, NY-DFS-Part-500, SOX-404, CMMC-L1, CMMC-L2, IEC-62443-3-3, ISO-27001-2022, SOC-2-Type-II, CISA-CPG]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
context_budget:
  always_loaded_tokens: 3500
  per_call_typical_tokens: 7000
  per_call_max_tokens: 16000
  per_call_p90_tokens: 9000
tags: [cybersecurity, framework, nist, csf, governance, risk-management, executive, board, audit-committee, profile-maturity, gap-analysis, fedramp, ffiec, oco, nydfs, cmmc]
---

# NIST CSF 2.0 — nist-csf-2

The "bridge" skill: the framework most likely to be a practitioner's *first* encounter (especially at executive level), with hand-offs to `nist-800-53-rmf`, `aicpa-soc-reporting`, `isaca-audit-methodology`, `coso-internal-controls`, and `audit-workpapers`.

## When to use

- The user asks about CSF 2.0, NIST Cybersecurity Framework, organizational cyber maturity, Tiers, Profiles, or the GOVERN function
- The user is a board, audit committee, CISO, or executive who wants a maturity narrative (not a control checklist)
- The user has SOC 2 / ISO 27001 and wants a strategic overlay (CSF 2.0 doesn't replace these; it complements them)
- The user is preparing for FedRAMP, FFIEC/OCC examinations, or CMMC and wants a Profile-based assessment
- The user is at a Series-A SaaS with no CISO and wants a defensible 90-day posture plan

## When NOT to use

- The task is a specific 800-53 ATO engagement (use `nist-800-53-rmf` instead)
- The task is a SOC 2 audit cycle (use `aicpa-soc-reporting` instead)
- The task is purely OT/ICS / industrial automation (CSF 2.0's mapping to IEC 62443 is partial; use a dedicated IEC 62443 skill)
- The user is a Big 4 auditor writing a financial-statement audit opinion (use `audit-workpapers` + `isaca-audit-methodology`)

## 30-second quick start

```python
import sys, json
sys.path.insert(0, "skills/nist-csf-2/tests")  # stub executor

from nist_csf_2_stub import run_skill

# UC-01: First Organizational Profile (Series-A SaaS) — the shipped seed
payload = json.load(open("skills/nist-csf-2/data/seeds/uc-01-input.json"))
out = run_skill("UC-01", payload)

# NOTE: the stub is a deterministic reference executor — its tiers come from a documented
# demo heuristic over the SEED's status sample (all 6 Functions; unscored RECOVER -> T1).
# It demonstrates output structure; it does NOT perform an assessment.
print(out["classification"])                                  # → "FIRST_ORGANIZATIONAL_PROFILE"
print(out["current_profile"]["current_tier_by_function"])     # → {'GV':'T1','ID':'T2','PR':'T2','DE':'T2','RS':'T1','RC':'T1'}
```

## 5-minute walkthrough

1. Read `SKILL.md` (the router) — 12 sections with the §11 routing table
2. Open the relevant chunk (or industry) based on §11
3. For an executive conversation, start with `chunks/05-govern-function.md` (the 6 GOVERN Categories are the board narrative)
4. For a 90-day implementation, use `chunks/07-implementation-playbook.md` (the 90-day quick wins list)
5. For a cross-framework mapping, use `chunks/08-informative-references-crosswalk.md` (the CSF↔800-53/800-171/ISO 27001/HIPAA tables)

## Cross-references to other skills

- `nist-800-53-rmf` — for 800-53 control-by-control depth (the foundational skill; CSF 2.0 is the strategic overlay)
- `aicpa-soc-reporting` — for SOC 2 Type II report content, TSC mapping, engagement lifecycle
- `isaca-audit-methodology` — for the IT audit lens (CISA domains, COBIT 2019, ITAF)
- `coso-internal-controls` — for SOX 404 / ICFR work (financial services)
- `audit-workpapers` — for the 5-part C-C-C-E-R finding format and PCAOB AS 1215 workpaper structure

## Industries covered (4)

- [financial-services](industries/financial-services.md) — FFIEC CAT, OCC Heightened Standards, NY DFS Part 500, SOX 404
- [public-sector](industries/public-sector.md) — FISMA, RMF, OMB A-130, BOD 18-01, FedRAMP, state-RMF variants, CISA CPGs
- [saas-technology](industries/saas-technology.md) — SOC 2, ISO 27001, CAIQ v4, customer questionnaire gauntlet
- [manufacturing](industries/manufacturing.md) — CMMC L1/L2/L3, NIST 800-171 (Rev 2 = the CMMC L2 set), IEC 62443, IT/OT convergence

Healthcare (HIPAA + HITRUST) deliberately deferred to v1.0 per project decision.

## Use cases (3)

- UC-01 — First Organizational Profile (50-FTE Series-A SaaS, Tier 1→2 in 90 days, 5-item roadmap)
- UC-02 — Board cyber posture report (6-function radar, $24B bank, 12-month $2.0M capital plan)
- UC-03 — CSF → 800-171 Rev 2 crosswalk for CMMC L2 (240-FTE aerospace DoD supplier, 14 lagging Subcategories)

## What this skill is NOT

- Not a certification (CSF 2.0 has no certification path; ISO 27001 is the certifiable alternative)
- Not a substitute for 800-53 (CSF 2.0 is outcome-based; 800-53 is control-based)
- Not a substitute for a legal opinion (regulatory compliance requires legal review)
- Not a substitute for professional judgment (Tier selection and Subcategory scoring require practitioner judgment)

See `docs/limits-and-disclaimers.md` for the full limits and disclaimers.

## Version history

- 0.1.0 (2026-06-08) — Initial release: 8 chunks, 4 industries, 3 UCs, 7 test files + stub

See `docs/changelog.md` for the full version history.

## Process notes

- 5-lens review + 5-practitioner review of Wave 1 router + chunks (8 CRITICAL + 17 HIGH + 9 MEDIUM + 8 LOW caught and fixed)
- §5.11 source-of-truth verification gate applied to all 4 industries; G4.5 persona vetting + live re-verification 2026-06-10 (see docs/persona-review.md)
- All "108 subcategory" references corrected to 106 (108 is CSF 1.1 count, 106 is CSF 2.0)
- Crosswalk tables in `chunks/08` transcribed from the NIST Informative References spreadsheet (re-verify rows against the live spreadsheet before client use)
- The Wave 1 build lesson: agents without authoritative source access produce plausible content; only webfetch-verified checks catch fabricated IDs and wrong counts
