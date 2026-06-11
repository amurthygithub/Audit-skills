# Acceptance gate — FedRAMP Cloud Authorization skill

Born-vetted build (SOX-574, process v3, M5 cycle 4): this gate is seeded from the verified rows of
the Day 0 fact sheet (`docs/fedramp-authorization-fact-sheet.md`, repo root), which was transcribed
from public US-government text — the FedRAMP Authorization Act of 2022 (44 U.S.C. 3607-3616,
law.cornell.edu), OMB M-24-15 (2024-07-25), fedramp.gov Rev 5 playbook pages, A2LA, and NIST SP
800-53 Rev 5 / 800-53B — with the Rev 5 baseline control counts **counted directly from the
PMO-authored OSCAL Rev 5 baseline profiles** (OSCAL-Foundation/fedramp-resources). Every row cites a
public identifier or source label; counts resolve to the fact sheet §0 `counts` block. All facts were
retrieved 2026-06-11.

## §5.11 verification table (seeded 2026-06-11)

| # | claim | source label | how verified | status |
|---|-------|--------------|--------------|--------|
| 1 | FedRAMP Rev 5 **Low** baseline = **156** controls (135 base + 21 enhancements) | FEDRAMP-REV5-BASELINES (OSCAL LOW profile); fact sheet §0 `baseline_low` | control IDs counted directly from the PMO-authored OSCAL `...LOW-baseline_profile.json` (base + selected enhancements) | VERIFIED |
| 2 | FedRAMP Rev 5 **Moderate** baseline = **323** controls (181 base + 142 enhancements) | FEDRAMP-REV5-BASELINES (OSCAL MODERATE profile); fact sheet §0 `baseline_moderate` | counted directly from the PMO OSCAL `...MODERATE-baseline_profile.json`; Rev 4 was 325 | VERIFIED |
| 3 | FedRAMP Rev 5 **High** baseline = **410** controls (191 base + 219 enhancements) | FEDRAMP-REV5-BASELINES (OSCAL HIGH profile); fact sheet §0 `baseline_high` | counted directly from the PMO OSCAL `...HIGH-baseline_profile.json` | VERIFIED |
| 4 | FedRAMP **LI-SaaS (Tailored)** baseline = **156** controls (= Low's exact set; 135 + 21) | FEDRAMP-REV5-BASELINES (OSCAL LI-SaaS profile); fact sheet §0 `baseline_li_saas` | counted directly from the PMO OSCAL `...LI-SaaS-baseline_profile.json`; shares Low's set | VERIFIED |
| 5 | LI-SaaS = **156** controls assigned per-control **method designations** (ASSESS / ATTEST / NSO / FED) in the Rev 5 OSCAL profile — **NOT** a flat "66 tested / 90 attested" split | FEDRAMP-REV5-BASELINES (Rev 5 OSCAL LI-SaaS profile) | G4.5 §5.11 re-count: the "66/90" figure traces only to the **Rev 4** doc `REV_4_FedRAMP-Tailored-LI-SaaS-Requirements.docx` and is NOT reproducible from the Rev 5 profile — the skill no longer asserts it | CORRECTED (G4.5) |
| 6 | NIST SP 800-53B baselines = **149 / 287 / 370** (Low / Moderate / High); FedRAMP tailors **up** from these | NIST-800-53R5; fact sheet §0 `nist_800_53b_low/moderate/high` | NIST SP 800-53B baseline counts; FedRAMP additions yield 156/323/410 | VERIFIED |
| 7 | FIPS 199 has **3** impact levels (Low / Moderate / High) over **3** CIA objectives; overall impact is the **high-water mark** (max of C/I/A) | FIPS-199; fact sheet §0 `fips199_impact_levels` / `cia_objectives` | fedramp.gov understanding-baselines: impact level → 800-53 baseline; one High objective makes the system High | VERIFIED |
| 8 | The authorization package has **4** core artifacts: **SSP / SAP / SAR / POA&M** | FEDRAMP-PLAYBOOK; fact sheet §0 `package_core_artifacts` + `identifiers` | fedramp.gov Rev 5 playbook; SSP = the "security blueprint" for the CSO | VERIFIED |
| 9 | The **SSP** is the CSP-authored "security blueprint" for the Cloud Service Offering | FEDRAMP-PLAYBOOK; fact sheet §0 terminology "System Security Plan (SSP)" | fedramp.gov SSP doc: "The SSP is the 'security blueprint' for the CSO." | VERIFIED |
| 10 | The **SAP** (plan) and **SAR** (results) are authored by the 3PAO; the **POA&M** is the CSP's corrective-action plan, tracked monthly | FEDRAMP-PLAYBOOK; fact sheet §0 `identifiers` (SAP/SAR/POA&M) | Rev 5 playbook: 3PAO authors SAP/SAR; CSP maintains the POA&M | VERIFIED |
| 11 | FedRAMP was established in statute by the **FedRAMP Authorization Act of 2022** (PL 117-263; codified 44 U.S.C. 3607-3616) | FEDRAMP-ACT-2022; fact sheet §0 `identifiers` + §1 | law.cornell.edu 44 U.S.C. 3607-3616; enacted 2022-12-23 (NDAA FY2023, Division E) | VERIFIED |
| 12 | The Act created the statutory **FedRAMP Board** (44 U.S.C. 3610), which **replaced the JAB** | FEDRAMP-ACT-2022 §3610; fact sheet §0 `identifiers` + §6 | 44 U.S.C. 3610; the Board is the statutory body replacing the Joint Authorization Board | VERIFIED |
| 13 | **OMB M-24-15** (dated **2024-07-25**) modernized FedRAMP: rescinds the 2011 memo; presumption of adequacy; machine-readable artifacts | OMB-M-24-15; fact sheet §0 `version_date` + §6 | fedramp.gov/docs/authority/m-24-15; M-24-15 supersedes the original 2011-12-08 OMB FedRAMP memo | VERIFIED |
| 14 | The **JAB P-ATO model is retired**; legacy JAB P-ATOs were **re-designated by the FedRAMP PMO** under M-24-15 | OMB-M-24-15; fact sheet §0 terminology "FedRAMP Board (NOT the JAB)" + §6 | M-24-15: do NOT describe the JAB as a current authorizing body — it is retired | VERIFIED |
| 15 | **Agency Authorization** is the operative Rev 5 path; M-24-15 adds multi-agency authorization + the **presumption of adequacy** | OMB-M-24-15; fact sheet §0 terminology "Single FedRAMP authorization / presumption of adequacy" | M-24-15: agencies must presume a FedRAMP package adequate at a given FIPS 199 impact level | VERIFIED |
| 16 | The **3PAO** is an independent assessor accredited by **A2LA** to **ISO/IEC 17020** (Type A or C; Type B prohibited for independence) | A2LA-3PAO; fact sheet §0 `identifiers` (3PAO) + terminology "3PAO + A2LA accreditation" | a2la.org/accreditation/fedramp: A2LA accredits 3PAOs against ISO/IEC 17020 | VERIFIED |
| 17 | **Inherited / leveraged** controls (e.g., an IaaS provider's) are not re-tested by, and not in the POA&M of, the leveraging CSP | A2LA-3PAO; fact sheet §0 + §2.2 (FedRAMP roles) | inherited controls belong to the provider's package and POA&M, not the leveraging CSP's | VERIFIED |
| 18 | **ConMon** is **monthly** (cadence = 1 month): updated POA&M, system inventory, vulnerability-scan results | FEDRAMP-CONMON; fact sheet §0 `conmon_cadence_months` + terminology "Continuous Monitoring (ConMon)" | fedramp.gov ConMon overview; monthly submission of POA&M / inventory / scans | VERIFIED |
| 19 | ConMon serves three objectives: **(i) operational visibility; (ii) managed change control; (iii) incident-response duties** | FEDRAMP-CONMON; fact sheet §0 terminology "Continuous Monitoring (ConMon) — monthly, three objectives" | fedramp.gov ConMon overview, verbatim: "(i) operational visibility; (ii) managed change control; and (iii) attendance to incident response duties" | VERIFIED |
| 20 | POA&M remediation SLAs are **30 / 90 / 180 days** (high-critical / moderate / low) | FEDRAMP-CONMON; fact sheet §0 terminology "Continuous Monitoring" | fedramp.gov ConMon overview: 30 days (high/critical), 90 (moderate), 180 (low) | VERIFIED |
| 21 | **FIPS 199** categorization basis = Low / Moderate / High by CIA-triad impact (high-water mark) | FIPS-199; fact sheet §0 `identifiers` (FIPS 199) | fedramp.gov understanding-baselines-and-impact-levels | VERIFIED |
| 22 | **FedRAMP baselines ARE tailored 800-53 Rev 5 controls** (same IDs) — FedRAMP does NOT maintain a separate catalog (the boundary vs `nist-800-53-rmf`) | NIST-800-53R5; fact sheet §0 terminology "FedRAMP baselines are tailored from NIST SP 800-53 Rev 5" + §3 `crosswalks: []` | the control IDs are the SAME 800-53 catalog; the "mapping" is identity + tailoring (no crosswalk to encode) | VERIFIED |
| 23 | **FedRAMP 20x** is the automation-first, outcome-based modernization track — **emerging direction**, not the settled Rev 5 process (KSIs; machine-readable packages) | fact sheet §0 `identifiers` (FedRAMP 20x) + terminology "FedRAMP 20x (emerging direction — label as such)" | fedramp.gov/20x; authority = the 2022 Act + M-24-15; label as direction, not current requirement | VERIFIED |
| 24 | Count currency: **325 is the Rev 4 Moderate count, not Rev 5** (Rev 5 Moderate = 323); NIST SP 800-53 is still **Rev 5** (no Rev 6) | fact sheet §6 (version & supersession) | Rev 4 archived baselines vs the Rev 5 OSCAL profiles; csrc.nist.gov (800-53 Rev 5 + maintenance releases) | VERIFIED |
| 25 | Source traps avoided: `github.com/GSA/fedramp-automation` is **404** (use the OSCAL-Foundation mirror); the fedramp.gov `.xlsx` baseline workbook resolves 200 but serves an **empty S3 redirect stub** (not cited as the count source) | fact sheet §4 (URL verification traps) | the byte-for-byte PMO OSCAL profiles now live at OSCAL-Foundation/fedramp-resources; the workbook URL is an empty stub | VERIFIED |
| 26 | UC-01 derivation: overall FIPS 199 impact = `max(C, I, A)`; the baseline count is looked up from the level (Low 156 / Moderate 323 / High 410); each POA&M due-date = `identified_date + severity_SLA` | recomputation from `data/seeds/uc-01-*.json` | oracle re-derives overall=Moderate, baseline_controls=323, poam due-dates from severity (30/90/180); stub agrees | VERIFIED |
| 27 | UC-02 derivation: LI-SaaS eligible iff `overall == Low AND saas_delivery`; eligible → 156 controls (method-designated, no flat split); Moderate+SaaS → NOT eligible (full Moderate, 323) | recomputation from `data/seeds/uc-02-*.json` | oracle re-derives eligibility from the seed and asserts the stub returns NO flat tested/attested split; the Moderate+SaaS perturbation is refused as ineligible | VERIFIED |
| 28 | UC-03 derivation: findings = `tested AND not passed AND not inherited`; POA&M item count = len(findings); inherited-and-failed controls excluded; a residual high finding raises the AO risk note | recomputation from `data/seeds/uc-03-*.json` | oracle re-derives 4 findings / poam_item_count 4 / inherited-2 excluded; the ATO itself is the AO's, not derived | VERIFIED |

## Standing enforcement

- The structural-count rows (1-8) are re-asserted by the consistency / inventory-diff test, which
  parses the fact sheet §0 `counts` block and asserts the chunk-stated baselines match the OSCAL-
  verified totals (156 / 323 / 410 / 156; 800-53B 149 / 287 / 370) — drift between the chunks and the
  mechanically counted profiles fails the build.
- Rows 12 / 14 (the FedRAMP Board replaced the JAB; the JAB P-ATO is retired) are the load-bearing
  governance-currency claims the skill exists to teach — the adversarial suite asserts the JAB is
  never named as a current authorizer.
- Row 23 (FedRAMP 20x = emerging) is the volatile claim: the active 20x RFCs MUST be re-verified at
  every G4 pass — the track is moving.
- Row 22 (FedRAMP baselines ARE tailored 800-53 controls) is the load-bearing boundary vs
  `nist-800-53-rmf`; the skill cites the boundary and never re-teaches the catalog.

## Sign-off

Seeded 2026-06-11 from the Day 0 fact sheet's verified rows (SOX-574, born-vetted build, M5 cycle 4).
The Rev 5 baseline counts are anchored to the PMO-authored OSCAL Rev 5 baseline profiles (control IDs
counted directly), not secondary assessor pages. G4.5 persona-vetting evidence lands within the same
build PR. The skill ships `status: draft` v0.1.0 pending Epic 6 reliability measurement.
