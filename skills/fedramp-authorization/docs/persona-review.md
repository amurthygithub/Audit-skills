# Persona Review — fedramp-authorization (G4.5, SOX-574)

Consumer-ready gate. One §5.11 source-of-truth pass (webfetch, live) + a 4-persona panel
(FedRAMP 3PAO Lead Assessor, SaaS Startup Head of Compliance, State Gov IT Audit Director,
Healthcare CISO). **Findings are hypotheses** — every CRITICAL/HIGH and every currency claim was
verified at the source before action (the panel's currency claims were sent back for a live second
pass; the verdicts are in `## Currency verification` below).

## Headline

The §5.11 pass found **no CRITICAL/HIGH factual errors** in the load-bearing facts: all four Rev 5
baseline counts (156/323/410/156, with base+enhancement splits) were re-counted directly from the
PMO-authored OSCAL profiles; governance (FedRAMP Board = 44 USC 3610; JAB P-ATO retired; M-24-15
dated 2024-07-25), the FIPS 199 high-water mark, the ConMon cadence, A2LA/ISO-17020, and all three
UC↔seed↔oracle derivations were verified with verbatim quotes.

The personas surfaced **one real defect I had introduced** (the LI-SaaS 66/90 split — a Rev 4
figure asserted as a Rev 5 fact, baked into the oracle), three currency tightenings, and a set of
feature-depth gaps now split to their own tickets.

## Currency verification (live, 2026-06-11)

| claim challenged | verdict | source |
|---|---|---|
| LI-SaaS "66 tested / 90 attested" split | **WRONG** — Rev 4 figure (`REV_4_FedRAMP-Tailored-LI-SaaS-Requirements.docx`); the Rev 5 OSCAL profile gives per-control method designations (ASSESS/ATTEST/NSO/FED), no clean flat split | Rev 5 OSCAL LI-SaaS profile (re-counted) |
| StateRAMP rebrand | **CONFIRMED** — StateRAMP → GovRAMP (dba), announced 2025-02-14 | govramp.org |
| 30/90/180 ConMon SLA | **CORRECT for Rev 5 today**; RFC-0012 / VDR Standard is draft ("MUST NOT be used in draft form"), effective only for 20x Low | fedramp.gov/rfcs/0012 |
| FedRAMP 20x "emerging" framing | **ACCURATE but understated** — live pilot authorizations exist (Phase 1 Low complete, Phase 2 Moderate underway); not yet the default Rev 5 path | fedramp.gov/20x |

## Findings → resolutions

| persona | severity | finding | resolution |
|---|---|---|---|
| §5.11 | (defect) | LI-SaaS "66 tested + 90 attested" asserted as an OSCAL-verified Rev 5 constant in ~25 places + the oracle; it is a Rev 4 figure not reproducible from the Rev 5 profile | **FIXED** — removed the flat split from the stub/oracle/expected/eval/fact-sheet and all prose; the skill now states the 156 total + the Rev 5 method-designation structure (ASSESS/ATTEST/NSO/FED) and explicitly flags 66/90 as Rev 4 |
| 3PAO | CRITICAL | (same LI-SaaS 66/90 issue) | **FIXED** (as above) |
| 3PAO | CRITICAL | 30/90/180 SLA presented with no caveat; VDR/RFC-0012 in flight | **FIXED** — added an SLA-currency caveat (chunk 06): 30/90/180 is the Rev 5 standard as of 2026-06 (per the ConMon Strategy Guide / vuln-scan requirements, not the overview page), with RFC-0012/VDR flagged as in-flight (effective for 20x Low, not yet Rev 5) |
| 3PAO | HIGH | SAR severity has no **Critical** tier; finding modeled as a boolean pass/fail with no 800-53A assessment objectives / Risk Exposure Table | **PARTIAL FIX + ticketed SOX-675** — added a Critical/High/Moderate/Low Risk-Exposure-Table note (chunk 07); the stub already buckets Critical at 30 days. Full 800-53A assessment-objective model → SOX-675 |
| 3PAO | MEDIUM | Binary inherited-vs-owned model; real FedRAMP has Shared/Hybrid controls whose customer portion stays in the CSP's POA&M | **PARTIAL FIX + ticketed SOX-676** — added a Shared/Hybrid caveat (chunk 05); full 5-category origination model → SOX-676 |
| 3PAO | MEDIUM | M-24-15 program-authorization path omitted (Agency Auth named as sole path) | **ACCEPTED-with-rationale** — chunk 03 already covers multi-agency authorization + presumption of adequacy; the broader 20x/program path set is tracked in chunk 08 and SOX-677 |
| 3PAO / 5.11 | LOW | A2LA Type-A/C-not-B and the SAR-finding definition cited to the A2LA landing page (which doesn't state them) | **ACCEPTED-with-rationale** — the facts are correct (FedRAMP 3PAO Obligations v3.3 + A2LA program requirements); citation-anchor strengthening noted for a future pass |
| SaaS | CRITICAL | LI-SaaS Rev 4 vs Rev 5 + the 66/90 split | **FIXED** (as above) |
| SaaS | CRITICAL | 20x treated as purely prospective; for a founder choosing a path now, 20x Low may be the cheaper route | **FIXED** — chunk 08 now states 20x's live-pilot status while keeping "not yet the default Rev 5 path"; path-selection decision aid → SOX-677 |
| SaaS | HIGH | No cost/time/staffing model; the README quickstart is a Python snippet, not a plain-language decision tree | **ticketed SOX-677** |
| SaaS | HIGH | Agency-sponsor prerequisite buried (no sponsor = no ATO) | **PARTIAL FIX + ticketed SOX-677** — chunk 03 now flags the sponsor as the gating prerequisite; a full business-development playbook → SOX-677 |
| SaaS | LOW | No SOC 2-reuse lever to lower FedRAMP cost | **ticketed SOX-677** |
| State Gov | HIGH | "public-sector" industry view is purely federal (zero state/local/legislature content) | **ticketed SOX-678** |
| State Gov | HIGH | "StateRAMP" named in 5 places — rebranded to GovRAMP (2025-02-14) | **FIXED** — updated to "GovRAMP (formerly StateRAMP)" everywhere |
| State Gov | HIGH | Presumption of adequacy stated as a universal rule (it binds federal agencies, not a state legislature) | **FIXED** — chunk 03 scopes the presumption to federal agencies; state/local entities governed by their own law |
| State Gov | MEDIUM | 20x downplayed | **FIXED** (chunk 08 status note) |
| State Gov | MEDIUM/LOW | No resource-constrained oversight model; no legislative-reporting UC; sunset not dated | **ticketed SOX-678** (the sunset date 2027-12-23 is captured in the chunk-01 currency flag) |
| Healthcare | CRITICAL | The **BAA** is never mentioned in the healthcare view | **FIXED** — added a "BAA is the operative HIPAA instrument" subsection + anti-hallucination bullet (industries/healthcare.md): FedRAMP ATO and a signed BAA are both required, neither substitutes |
| Healthcare | HIGH | hipaa handoff has an undisclosed hole (sibling covers Subpart C only; breach notification / Privacy Rule out of scope of both) | **FIXED** — added the handoff-boundary disclosure |
| Healthcare | HIGH | PHI→Moderate under-anchored (clinical PHI often High; SP 800-122 supplement uncited) | **ACCEPTED-with-rationale + ticketed SOX-679** — healthcare.md already says "PHI drives at least Moderate, often High; rarely Low"; the 800-60/800-122 elevation mechanism → SOX-679 |
| Healthcare | MEDIUM/LOW | Overlap framing one-directional (no gap checklist); I/A for clinical systems not operationalized | **ticketed SOX-679** |

## Scope split (per the approved slice pattern)

v0.1.0 ships the correctness/currency/honesty fixes above. Feature-depth gaps are their own tickets:
**SOX-675** (SAR/800-53A depth + Critical tier), **SOX-676** (5-category control origination),
**SOX-677** (SaaS GTM usability), **SOX-678** (state/local GovRAMP lens), **SOX-679** (healthcare depth).

## What was NOT re-checked (residual risk)

- The exact per-control ASSESS/ATTEST counts in the Rev 5 LI-SaaS profile (the skill deliberately
  states only the 156 total + the method-designation structure, not a count).
- The 800-53B 149/287/370 baseline tables row-by-row (verified by net-delta cross-check, not a
  row count).
- Per-control 800-53 semantics (the skill makes no per-control scope claims — that is
  `nist-800-53-rmf`).
- Internal build claims (test counts, token budgets) — out of §5.11 scope.
