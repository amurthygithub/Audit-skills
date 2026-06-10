# NIST Work — Collation

**Source:** Linear project "Audit-Skills → Paid MCP" (e143eff0-2836-4818-9835-9490a9f3e6e7)
**Pulled:** 2026-06-05
**Purpose:** Single-page view of every NIST-related issue, what shipped, what's pending, and dependencies. Use this when planning the next NIST work and when answering "what's the state of NIST" questions.

---

## Summary

| Status | Count | Issues |
|--------|-------|--------|
| ✅ Done | 2 | SOX-566 (skill), SOX-620 (Wk 2 LI post) |
| 🟡 Open | 2 | SOX-569 (CSF 2.0 skill), SOX-574 (FedRAMP skill) |

The original A1 deliverable (NIST SP 800-53 RMF) is **shipped and live** at github.com/amurthygithub/Audit-skills/skills/nist-800-53-rmf (v0.2.1, 29 tests, all linters green). The two remaining open issues are follow-on skills in the same NIST family.

---

## ✅ Done

### SOX-566 — A1 — Skill: nist-800-53-rmf
**State:** Done
**Priority:** P2
**Parent:** SOX-563 (Epic 2 — CORPUS)
**Drip:** Week 2
**Effort:** L

**Standard:** NIST SP 800-53 Rev 5 (+5.1.1), SP 800-37 Rev 2 RMF, SP 800-53A Rev 5, FIPS 199/200.
**Persona:** IT.

**Covers:** 20 control families (~1,000 controls), Low/Mod/High baselines, RMF 7-step lifecycle (Prepare→Categorize→Select→Implement→Assess→Authorize→Monitor), 800-53A assessment procedures, control inheritance. Anchor of the IT pillar — everything cross-references it.

**Examples shipped (use cases):**
- B13: FedRAMP-bound SaaS categorizes FIPS-199 Moderate (~325 controls, 40 tailored out, AC-2 AWS inheritance)
- B14: federal agency RMF Step 6 (SAR 22 findings → POA&M, AO risk-accepts 14, ATO w/ conditions)
- B15: enterprise fin-svcs maps SOC 2 → 800-53 Mod (71% overlap, 94 gap controls)

**Shipped artifacts:**
- `skills/nist-800-53-rmf/SKILL.md` (router, ≤300 lines, 12 sections)
- `skills/nist-800-53-rmf/chunks/01..09-*.md` (8 chunks: categorize, baseline, implement, assess, authorize, monitor, crosswalk, questionnaire-reuse)
- `skills/nist-800-53-rmf/industries/` (3: FedRAMP SaaS, federal agency, fin-svcs crosswalk)
- `skills/nist-800-53-rmf/use-cases/` (3: FedRAMP Moderate, agency ATO, SOC 2 ↔ 800-53)
- `skills/nist-800-53-rmf/data/` (generators + seeds + crosswalks)
- `skills/nist-800-53-rmf/tests/` (29 tests, all green)
- `skills/nist-800-53-rmf/telemetry/` (schema, instrument, redaction, baseline)
- `skills/nist-800-53-rmf/docs/` (architecture, limits, changelog, acceptance-gate)
- `skills/nist-800-53-rmf/README.md` (consumer one-pager)
- Cross-skill references in coso, isaca, aicpa, workpapers

**Quality:** 5-lens review + 5-practitioner review + fix waves (1 + 2 + 3) resolved 30+ findings. All 29 tests pass; all 3 CI checks (PR title, lint, pytest) green on main.

---

### SOX-620 — LI Post Wk 2 — NIST 800-53 control baseline picker (FIPS 199 triage)
**State:** Done
**Priority:** P2
**Parent:** SOX-587 (GTM Act 1, Wk 1–4)
**Drip:** Week 2

**Description:** Tuesday artifact drop — publish the A1 skill to the public repo. Post the FIPS 199 categorization triage: classify system as Low/Mod/High impact, map to ~325 controls. Cite NIST FIPS 199 and 800-53 Rev 5.

**Status:** LinkedIn post published (amurthy, 2026-06-04). Repo link included. Closed in Linear.

---

## 🟡 Open

### SOX-569 — A4 — Skill: nist-csf-2  **(highest priority, P2)**
**State:** Todo
**Priority:** P2
**Parent:** SOX-563 (Epic 2 — CORPUS)
**Drip:** Week 5
**Effort:** M
**Depends on:** SOX-566 (A1, for informative references between CSF and 800-53)

**Standard:** NIST CSF 2.0 (Feb 2024).
**Persona:** BOTH (IT + executive).

**Covers:** 6 Functions (GOVERN/IDENTIFY/PROTECT/DETECT/RESPOND/RECOVER), Categories/Subcategories, Tiers 1–4, Profiles (Current/Target gap), Organizational + Community Profiles, CSF↔800-53 references. The "bridge" skill — most executive-legible → most shareable.

**Examples planned:**
- B22: SaaS first Organizational Profile (Tier 1→3, GOVERN gap, 9-subcategory roadmap)
- B23: enterprise fin-svcs board maturity report (6-function radar, GV.RM+DE.CM lagging, 12-mo $ plan)
- B24: mid-market mfr Current/Target gap mapped to 800-53 Mod for 14 lagging subcategories

**Why it's the natural next NIST skill:**
- P2 (vs. SOX-574 P3 for FedRAMP)
- Logical follow-on to A1 (CSF 2.0 explicitly cross-references 800-53)
- "Bridge" skill — most executive-legible → highest social share count → best GTM lever for Wk 5
- Reuses data/ artifacts from A1 (HIPAA, PCI, ISO 27001, SOC 2 crosswalks all apply)

**Build cost:** M effort, similar shape to A1 (router + ~7 chunks + 3 industries + 3 UCs + 30+ tests). Could be done in 1–2 days of focused work.

---

### SOX-574 — A8 — Skill: fedramp-authorization
**State:** Todo
**Priority:** P3
**Parent:** SOX-563 (Epic 2 — CORPUS)
**Drip:** Week 9
**Effort:** M
**Depends on:** SOX-566 (A1, load-bearing)

**Standard:** FedRAMP Rev 5 (aligned to 800-53 Rev 5); OMB M-24-15; FedRAMP 20x (flag emerging).
**Persona:** IT.

**Covers:** Rev 5 baselines (Li-SaaS/Low/Mod/High), authorization paths (Agency ATO vs JAB→PMO), SSP/SAP/SAR/POA&M package, 3PAO assessment, ConMon monthly cadence, FedRAMP 20x direction.

**Examples planned:**
- B34: SaaS FedRAMP Moderate via Agency ATO (SSP ~325 controls, 3PAO SAP/SAR, 40-item POA&M, ConMon)
- B35: cloud vendor Li-SaaS (~156 controls, readiness assessment)
- B36: Big-4 3PAO assessment of Moderate CSP (control-test sampling, IaaS inheritance, 18 findings → POA&M)

**Why P3:**
- Duplicates a lot of 800-53 RMF skill content (control selection, RMF steps, ATO process)
- Primary value-add is the FedRAMP-specific wrapper (PMO templates, ConMon, 3PAO process) — narrower audience
- Drip scheduled for Wk 9 of GTM, after the act 2/3 teasers

**Status note:** The FedRAMP-specific wrapper (PMO templates, ConMon, SAR header, ATO letter format, inheritance gating) is already in the nist-800-53-rmf skill as a *side note* (added during fix wave 1, see cross-skill fixes from b12). A standalone FedRAMP skill would be a focused extraction + more templates.

---

## Adjacent / Cross-references (not NIST-titled, but reference NIST)

These mention NIST/800-53 in their description:

| ID | State | P | Title | Why it touches NIST |
|----|-------|---|-------|---------------------|
| SOX-587 | Todo | P2 | GTM Act 1 (Wk 1–4) — Compound the free-skill audience | LI drip umbrella. SOX-620 (Wk 2 NIST post) is done under it. |
| SOX-585 | Todo | P3 | PULSE — Reg Change Detector | Renewal heartbeat. Catches NIST 800-53 / CSF revisions. |
| SOX-618 | Backlog | P1 | Phase 0.3 — Tier 0.5 Source-Text Acquisition Plan | Catalogs CSF 2.0 + NIST OSCAL as free sources. |
| SOX-612 | Backlog | P1 | Phase 1.5 — Golden Reference Cases | FIN SIEVE MUS reference case mentions 800-53. |
| SOX-598 | Backlog | P3 | Wave 1 coverage build (post-launch Q1) — ~18 T1 targets | Coverage atlas expansion; CSF 2.0 likely a T1 target. |
| SOX-589 | Todo | P2 | GTM Act 3 (Wk 9–10) — Early-access waitlist | Teases CSF 2.0 skill as paid MCP differentiator. |

---

## Recommended next NIST move

1. **This week:** no NIST work — user wants to plan next week fresh. (User said "let us keep it to next week.")
2. **Next week, priority order:**
   - **SOX-569 (P2, nist-csf-2):** build the skill using the [`skill-design-template.md`](skill-design-template.md) template. Reuses A1 data/ + crosswalks. 1–2 days. Ships Wk 5 drip.
   - SOX-574 (P3, fedramp-authorization): defer to Wk 9 per the GTM schedule.
3. **Cross-cutting:** when building CSF 2.0, do the crosswalks as JSON (CSF subcategory → 800-53 control, similar to existing SOC 2 → 800-53 crosswalk) so the data/ crosswalks/ folder grows consistently.

---

## Status code meanings

- ✅ **Done** — Linear state "Done"
- 🟡 **Open** — Linear state "Todo" or "In Progress" or "Backlog" (actionable)
- ⏸ **Backlog** — Linear state "Backlog" (deferred / not for current cycle)
