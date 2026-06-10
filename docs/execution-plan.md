# Execution Plan v1 — Vetting → Debt → New Builds → Harness

**Ticket:** SOX-643 · **Date:** 2026-06-10 · **Owner:** solo maintainer
**Status:** ACTIVE — this is the sequence we execute against. Update it when milestones close or priorities change; stale plans are worse than no plans.

---

## 1. Where we are

- **6 skills shipped**, **4/6 G4.5-vetted** (nist-800-53-rmf, audit-workpapers, coso-internal-controls, aicpa-soc-reporting). Every vetting run found 4–8 CRITICALs that structural gates missed — fabricated criteria, SEC-prohibited report language, invented citations. The pattern is consistent: smoke tests pass because skills are internally coherent; persona vetting + Tier-2 live-source verification is what catches "consistently wrong."
- **Process v2 is live** (AGENTS.md): G0–G6 pipeline, verification tiers (Tier 3 concurrence ≠ verification), §3.3.1 per-skill vetting runbook, citation registry as source of truth, pre-merge §5.11 with verbatim quotes.
- **Unvetted:** isaca-audit-methodology, nist-csf-2.
- **Structural-gap tickets filed from vetting:** SOX-637–642 (all Todo under SOX-633).
- **Stale pre-process-v2 tickets:** SOX-627–631 (§5.11 URL/content fixes filed before vetting; overlap with merged vetting PRs is unreconciled).
- **New builds frozen** since the consumer-ready pivot; A-wave queue: SOX-567/568/570/572–576.
- **Epic 6 harness** (SOX-599–606) not started — all reliability claims are still N=1 smoke tests.

## 2. Sequencing principles

1. **Correctness before depth.** Wrong content that misleads a consumer outranks missing content that's honestly labeled.
2. **Vet before promote.** No GTM amplification of a skill until it has passed G4.5. Library-wide claims ("consumer-ready") only when 6/6 are vetted.
3. **Public-source-first for new builds.** Order new skills by Tier-2 verifiability of their authoritative source. A skill whose canonical text is free and public (CFR, SEC releases, NIST pubs) can be fully verified at build time; paywalled standards (ISO 27001, COSO pub) need a Day-0 source-acquisition plan (SOX-618) before G1 can pass honestly.
4. **Measure before claiming reliability.** "Passes all defined gates" until Epic 6 produces N≥20 multi-model numbers; never "guaranteed."
5. **Interleave depth with builds.** Alternate one new skill with one structural-gap ticket per cycle so the shipped library deepens while the catalog grows. One skill per session by default (token control); parallel runs only by explicit choice.
6. **Build-time vetting, not retrofit.** Every new skill carries G4.5 inside its build PR. The retrofit sweep (SOX-636) is the last time vetting happens after shipping.

## 3. The sequence

### M1 — Finish the vetting sweep (SOX-636) — NEXT UP
| step | what | tickets |
|---|---|---|
| 1 | Vet **isaca-audit-methodology** per §3.3.1 (personas + smokes → verify → fix → §5.11 → merge). Fold SOX-630 (CISA domain weights, dead ITAF URL, COBIT design factors) into this run — same files, same verification pass. | SOX-636, SOX-630 |
| 2 | Vet **nist-csf-2** per §3.3.1. Its crosswalk chunk (08-informative-references) gets full Tier-2 row verification — the aicpa/rmf lesson says crosswalk seeds are where fabrication concentrates. | SOX-636 |
| 3 | Library-wide claim update: README + AGENTS state "6/6 G4.5-vetted (LLM-vetted — a filter, not a certification)". Close SOX-636. | SOX-636 |

**Exit:** 6/6 vetted, zero unresolved CRITICAL/HIGH library-wide, file structural-gap tickets for both skills (the SOX-637-pattern).
**Est:** 2 sessions, ~0.5–0.9M tokens per skill (observed range).

### M2 — Backlog reconciliation + small correctness debt
| step | what | tickets |
|---|---|---|
| 1 | Audit SOX-627/628/629/631 against the merged vetting PRs (#32–#37): close what's already fixed, fold live remainders into the per-skill gap tickets. The backlog must reflect disk reality. | SOX-627–631 |
| 2 | **SOX-637** — rmf UC-03 data coherence: derivable crosswalk headline, non-circular oracle, 93-vs-94 record fix. Smallest open correctness item in a vetted skill. | SOX-637 |
| 3 | Epic 7 (SOX-607) overlap pass: SOX-609 done, SOX-616 (linter) and parts of SOX-617 already exist via process v2 — close or re-scope so the same work isn't tracked twice. | SOX-607 children |

**Exit:** every open ticket maps to real remaining work; rmf UC-03 honest.
**Est:** 1 session.

### M3 — First new skill through full G0–G6: **hipaa-security-rule (SOX-572)**
The proving run for process v2 on a *build* (every prior G4.5 was a retrofit).

**Why HIPAA before ISO 27001 (re-orders the A-wave):** the authoritative source is 45 CFR Part 164 Subpart C — free, public, stable — so 100% of claims are Tier-2 verifiable at build time. ISO 27001 is paywalled; running it first would force either recall-based content (the exact failure mode vetting kept finding) or a blocked G1. Second payoff: the HIPAA Day-0 fact sheet (full Subpart C standard/implementation-spec inventory with Required/Addressable flags) is **exactly the input SOX-638 needs**.

| step | what | tickets |
|---|---|---|
| 1 | G0–G1: ticket → branch → Day-0 fact sheet (full Subpart C inventory, verbatim quotes, machine-readable YAML) → `check_fact_sheet.py` gate | SOX-572 |
| 2 | G2–G4: design doc → build → versioned-prompt verification | SOX-572 |
| 3 | G4.5 inside the build PR: personas + smokes + §5.11 pre-merge | SOX-572 |
| 4 | **SOX-638** immediately after, reusing the fact sheet: rmf HIPAA crosswalk completion (12 → full Subpart C coverage) + healthcare UC for both skills | SOX-638 |

**Exit:** first born-vetted skill shipped; SOX-572 + SOX-638 closed; process-v2 lessons folded back into AGENTS.md.
**Est:** 2–3 sessions.

### M4 — Epic 6 harness, minimum viable slice (SOX-600 → SOX-601)
Can start in parallel with M3 (disjoint files) if running parallel sessions; otherwise directly after.

| step | what | tickets |
|---|---|---|
| 1 | V1: shared harness runner + fixture schema; run against 2 pilot skills (1 vetted retrofit + hipaa-security-rule) | SOX-600 |
| 2 | V2: synthetic input generation (start with 1–2 generators, not all 4) | SOX-601 |
| 3 | Publish per-skill reliability rows (pass rate over N≥20 runs, ≥2 models) in each `acceptance-gate.md`; update the SOX-633 DoD from "smoke N=1" to measured | SOX-600, SOX-603 |

**Exit:** "fully tested" stops meaning "22 pytest cases" and starts meaning a measured pass rate.
**Est:** 2 sessions for the slice; V3–V7 stay sequenced behind it in Epic 6.

### M5 — Wave build-out, interleaved (repeat until queue drains)
Cadence: **one new skill, then one structural-gap ticket**, repeating. New-skill order by source verifiability + funnel value:

| cycle | new skill (G0–G6, born-vetted) | then structural ticket |
|---|---|---|
| 1 | **iso-27001-isms** (SOX-567) — gate on a Day-0 source plan per SOX-618; if the full standard text can't be acquired, scope to what's publicly verifiable and label the rest | SOX-642 (aicpa: AU-C 402 user-auditor track, SOC 1 depth, first-timer playbook) |
| 2 | **pci-dss-assessment** (SOX-568) — PCI DSS v4.x is a free download; strong SaaS-funnel pull | SOX-641 (coso: UC-02 rework, Green Book layer, 404(a) path) |
| 3 | **sox-302-disclosure-controls** (SOX-570) — public SEC/PCAOB sources; adjacent to existing coso audience | SOX-640 (workpapers: company-side content, ITGC sampling, GAGAS formats) |
| 4 | **fedramp-authorization** (SOX-574) — public; deepens the 3PAO persona that found the most CRITICALs | SOX-639 (rmf: non-federal adoption paths) |
| 5 | **gdpr-dpia-privacy** (SOX-573), then **pcaob-as-deepening** (SOX-575), **soc-for-cybersecurity** (SOX-576, Backlog) | gap tickets filed in M1 for isaca/csf-2 |

**Est:** ~2 sessions per cycle. Harness (M4) runs against each new skill as it ships.

### M6 — GTM re-engagement (Epic 4) — gated on M1
- LI cadence (SOX-621–625) restarts once "6/6 vetted" is true — the posts can now make an honest quality claim no competitor library can.
- Acts 2–4 (SOX-588–590) track ARGUS/Epic 3 readiness and stay out of this plan's critical path.

## 4. Standing gates (apply to every milestone)

1. PR-only to main; squash-merge after 3/3 CI green; `--admin` waives review only (solo maintainer), never CI.
2. Every CRITICAL/HIGH persona finding verified (Tier 1/2) before fixing — findings are hypotheses.
3. No source → caveat, never a new specific claim. Tier 3 concurrence is not verification.
4. New citations enter `data/registry/citations.json` first; manifests match verbatim.
5. Crosswalk seeds: every row Tier-2 verified at build time.
6. Cost discipline: one skill per session by default; report token spend per milestone.

## 5. Decision log

| date | decision | rationale |
|---|---|---|
| 2026-06-10 | Vet last 2 skills before crosswalk shore-up | Remaining crosswalk debt is labeled incompleteness; unvetted skills carry unknown falsehoods (4–8 CRITICALs per skill observed) |
| 2026-06-10 | hipaa-security-rule jumps the A-wave queue ahead of iso-27001-isms | Public authoritative source → 100% Tier-2 verifiable build; fact sheet feeds SOX-638 directly; ISO paywall needs SOX-618 first |
| 2026-06-10 | Epic 6 starts as a minimum slice (V1+V2), not the full V1–V7 ladder | Measured reliability on shipped skills beats a complete harness for unshipped ones |
