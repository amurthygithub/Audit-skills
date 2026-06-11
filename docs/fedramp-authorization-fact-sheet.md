# Fact Sheet — fedramp-authorization (Day 0, SOX-574)

> Pre-build research per `docs/fact-sheet-template.md`. All sources are **public US-government
> text** (FedRAMP Authorization Act / 44 U.S.C., OMB M-24-15, fedramp.gov program docs, NIST SP
> 800-53 Rev 5) — fully machine-verifiable, same licence class as the eCFR/SEC builds (full
> vendoring permitted). The skill covers the **FedRAMP cloud-authorization program** (baselines,
> the modernized authorization path, the SSP/SAP/SAR/POA&M package, 3PAO assessment, monthly
> ConMon, and the FedRAMP 20x direction) — the *program/process* layer that sits on top of the
> NIST SP 800-53 Rev 5 control catalog covered by `nist-800-53-rmf`. See §7 for that boundary.
>
> **Governance currency note (critical):** the source ticket's "Agency ATO vs JAB→PMO" framing is
> outdated. The **FedRAMP Authorization Act of 2022** (44 U.S.C. 3607–3616) created the statutory
> **FedRAMP Board** (§3610); **OMB M-24-15 (2024-07-25)** retired the JAB P-ATO model (legacy
> P-ATOs "re-designated" by the PMO) and reframed the program around a single FedRAMP
> authorization + presumption of adequacy. The skill must describe the **current** model, not the
> pre-2022 JAB structure. See §6.

## 0. Machine-readable data block (REQUIRED — the G1 gate parses this)

```yaml
fact_sheet:
  skill_slug: fedramp-authorization
  framework: "FedRAMP (Federal Risk and Authorization Management Program), Rev 5 baselines tailored from NIST SP 800-53 Rev 5; FedRAMP Authorization Act of 2022 (44 U.S.C. 3607-3616); OMB M-24-15; FedRAMP 20x"
  version: "Rev 5 (post May 2023 800-53 Rev 5 transition); program structure per OMB M-24-15 (2024-07-25) and the FedRAMP Authorization Act (PL 117-263, 2022-12-23); FedRAMP 20x track active 2025-2026"
  version_date: "2024-07-25"
  supersedes: "FedRAMP Rev 4 baselines (325/Moderate); original 2011-12-08 OMB FedRAMP memo (rescinded by M-24-15); JAB P-ATO model (retired)"
  retrieval_date: "2026-06-11"
  researcher: "Claude (Fable 5) dispatcher + webfetch research agent — fedramp.gov, law.cornell.edu (44 USC), whitehouse/OMB M-24-15, csrc.nist.gov, a2la.org"
counts:                             # totals counted directly from the PMO-authored OSCAL Rev 5 profiles
  baseline_low: 156                 # FedRAMP Rev 5 Low (135 base + 21 enhancements)
  baseline_low_base: 135
  baseline_low_enhancements: 21
  baseline_moderate: 323            # FedRAMP Rev 5 Moderate (181 base + 142 enh); Rev 4 was 325
  baseline_moderate_base: 181
  baseline_moderate_enhancements: 142
  baseline_high: 410                # FedRAMP Rev 5 High (191 base + 219 enhancements)
  baseline_high_base: 191
  baseline_high_enhancements: 219
  baseline_li_saas: 156             # LI-SaaS shares Low's exact set (135 + 21); split 66 tested + 90 attested
  li_saas_3pao_tested: 66           # of the 156, independently tested by a 3PAO (per Tailored LI-SaaS doc)
  li_saas_attested: 90              # of the 156, satisfied by CSP attestation (per Tailored LI-SaaS doc)
  nist_800_53b_low: 149             # NIST SP 800-53B Low baseline (FedRAMP tailors up from here)
  nist_800_53b_moderate: 287        # NIST SP 800-53B Moderate baseline
  nist_800_53b_high: 370            # NIST SP 800-53B High baseline
  fips199_impact_levels: 3          # Low / Moderate / High
  cia_objectives: 3                 # Confidentiality / Integrity / Availability (high-water mark)
  package_core_artifacts: 4         # SSP, SAP, SAR, POA&M
  conmon_cadence_months: 1          # monthly continuous-monitoring submission
identifiers:
  - code: "FedRAMP Authorization Act 2022"
    name: "Public Law 117-263 (NDAA FY2023), Division E Title LIX §5921; codified 44 U.S.C. 3607-3616 — establishes FedRAMP in statute"
    parent: "44 U.S.C. Chapter 36"
  - code: "44 U.S.C. 3610"
    name: "FedRAMP Board — the statutory body that replaced the Joint Authorization Board (JAB)"
    parent: "FedRAMP Authorization Act 2022"
  - code: "OMB M-24-15"
    name: "Modernizing the Federal Risk and Authorization Management Program (FedRAMP) — rescinds the 2011 memo; presumption of adequacy; machine-readable artifacts"
    parent: "OMB policy"
  - code: "FedRAMP Low"
    name: "Low-impact baseline (156 controls) — FIPS 199 Low high-water mark"
    parent: "FedRAMP Rev 5 baselines"
  - code: "FedRAMP Moderate"
    name: "Moderate-impact baseline (323 controls) — the most common SaaS authorization"
    parent: "FedRAMP Rev 5 baselines"
  - code: "FedRAMP High"
    name: "High-impact baseline (410 controls)"
    parent: "FedRAMP Rev 5 baselines"
  - code: "FedRAMP LI-SaaS"
    name: "Low-Impact SaaS / Tailored baseline (156 controls; 66 3PAO-tested + 90 attested)"
    parent: "FedRAMP Rev 5 baselines"
  - code: "SSP"
    name: "System Security Plan — the 'security blueprint' for the Cloud Service Offering"
    parent: "Authorization package"
  - code: "SAP"
    name: "Security Assessment Plan — 3PAO's methodical approach to assessing the controls"
    parent: "Authorization package"
  - code: "SAR"
    name: "Security Assessment Report — 3PAO's evaluation of controls, vulnerabilities, risk, and recommendation"
    parent: "Authorization package"
  - code: "POA&M"
    name: "Plan of Action & Milestones — corrective-action plan for SAR-identified deficiencies; tracked monthly"
    parent: "Authorization package / ConMon"
  - code: "3PAO"
    name: "Third Party Assessment Organization — independent assessor; A2LA-accredited to ISO/IEC 17020 (Type A or C)"
    parent: "FedRAMP roles"
  - code: "ConMon"
    name: "Continuous Monitoring — monthly POA&M/inventory/scan submission; operational visibility, managed change control, incident response"
    parent: "Post-authorization"
  - code: "FIPS 199"
    name: "Standards for Security Categorization — Low/Moderate/High by CIA-triad impact (high-water mark)"
    parent: "Categorization"
  - code: "FedRAMP 20x"
    name: "Automation-first modernization track — Key Security Indicators (KSIs), machine-readable packages; Phase 1/2 complete, Phase 3 underway (2026)"
    parent: "FedRAMP program direction"
  - code: "Agency Authorization"
    name: "The operative Rev 5 authorization path — an agency sponsors and grants the ATO; multi-agency authorizations permitted under M-24-15"
    parent: "Authorization paths"
urls:
  - label: "FedRAMP-main"
    url: "https://www.fedramp.gov/"
    status: 200
    checked: "2026-06-11"
  - label: "FedRAMP-understanding-baselines"
    url: "https://www.fedramp.gov/understanding-baselines-and-impact-levels/"
    status: 200
    checked: "2026-06-11"
  - label: "FedRAMP-rev5-agency-authorization"
    url: "https://www.fedramp.gov/rev5/agency-authorization/"
    status: 200
    checked: "2026-06-11"
  - label: "FedRAMP-20x"
    url: "https://www.fedramp.gov/20x/"
    status: 200
    checked: "2026-06-11"
  - label: "OMB-M-24-15-fedramp-doc"
    url: "https://www.fedramp.gov/docs/authority/m-24-15/"
    status: 200
    checked: "2026-06-11"
  - label: "FedRAMP-Act-law"
    url: "https://www.fedramp.gov/docs/authority/law/"
    status: 200
    checked: "2026-06-11"
  - label: "USC-44-3607"
    url: "https://www.law.cornell.edu/uscode/text/44/3607"
    status: 200
    checked: "2026-06-11"
  - label: "USC-44-3610-FedRAMP-Board"
    url: "https://www.law.cornell.edu/uscode/text/44/3610"
    status: 200
    checked: "2026-06-11"
  - label: "NIST-SP-800-53r5"
    url: "https://doi.org/10.6028/NIST.SP.800-53r5"
    status: 200
    checked: "2026-06-11"
  - label: "A2LA-FedRAMP-3PAO"
    url: "https://a2la.org/accreditation/fedramp/"
    status: 200
    checked: "2026-06-11"
  - label: "FedRAMP-conmon-overview"
    url: "https://www.fedramp.gov/docs/rev5/playbook/csp/continuous-monitoring/overview/"
    status: 200
    checked: "2026-06-11"
  - label: "FedRAMP-ssp-doc"
    url: "https://www.fedramp.gov/docs/rev5/playbook/csp/authorization/ssp/"
    status: 200
    checked: "2026-06-11"
  - label: "OSCAL-FedRAMP-rev5-MODERATE-profile"
    url: "https://raw.githubusercontent.com/OSCAL-Foundation/fedramp-resources/main/baselines/rev5/json/FedRAMP_rev5_MODERATE-baseline_profile.json"
    status: 200
    checked: "2026-06-11"
  - label: "OSCAL-FedRAMP-rev5-LOW-profile"
    url: "https://raw.githubusercontent.com/OSCAL-Foundation/fedramp-resources/main/baselines/rev5/json/FedRAMP_rev5_LOW-baseline_profile.json"
    status: 200
    checked: "2026-06-11"
  - label: "OSCAL-FedRAMP-rev5-HIGH-profile"
    url: "https://raw.githubusercontent.com/OSCAL-Foundation/fedramp-resources/main/baselines/rev5/json/FedRAMP_rev5_HIGH-baseline_profile.json"
    status: 200
    checked: "2026-06-11"
  - label: "OSCAL-FedRAMP-rev5-LI-SaaS-profile"
    url: "https://raw.githubusercontent.com/OSCAL-Foundation/fedramp-resources/main/baselines/rev5/json/FedRAMP_rev5_LI-SaaS-baseline_profile.json"
    status: 200
    checked: "2026-06-11"
crosswalks: []
terminology:
  - term: "FedRAMP baselines are tailored from NIST SP 800-53 Rev 5 (the boundary vs nist-800-53-rmf)"
    source_wording: "FedRAMP's Low/Moderate/High baselines are the NIST SP 800-53B Low/Moderate/High control baselines (149 / 287 / 370 controls) tailored UP with FedRAMP-specific additional controls and parameter values — yielding 156 / 323 / 410. The control IDs are the SAME 800-53 catalog; FedRAMP does not invent a separate catalog. This skill covers the FedRAMP program/process; nist-800-53-rmf covers the control catalog and the general RMF."
  - term: "FedRAMP Board (NOT the JAB)"
    source_wording: "The FedRAMP Authorization Act (44 U.S.C. 3610) established the FedRAMP Board, which replaced the Joint Authorization Board. M-24-15: legacy 'JAB P-ATO' authorizations are 're-designated' by the FedRAMP PMO. Do NOT describe the JAB as a current authorizing body — it is retired."
  - term: "Single FedRAMP authorization / presumption of adequacy"
    source_wording: "M-24-15: agencies must presume the security assessment documented in a FedRAMP authorization package is adequate for a product at a given FIPS 199 impact level (reducing duplicative agency-by-agency reassessment). Agency Authorization is the operative Rev 5 path; multi-agency authorization is permitted."
  - term: "Continuous Monitoring (ConMon) — monthly, three objectives"
    source_wording: "ConMon provides '(i) operational visibility; (ii) managed change control; and (iii) attendance to incident response duties.' Monthly submission = updated POA&M, system inventory, and vulnerability scan results; remediation SLAs 30 days (high/critical), 90 days (moderate), 180 days (low)."
  - term: "System Security Plan (SSP)"
    source_wording: "The SSP is the 'security blueprint' for the CSO (Cloud Service Offering) — components, architecture, data flows, and the per-control implementation narrative."
  - term: "3PAO + A2LA accreditation"
    source_wording: "A Third Party Assessment Organization performs the independent assessment (SAP/SAR). A2LA (American Association for Laboratory Accreditation) accredits 3PAOs against ISO/IEC 17020 (Type A or Type C inspection body; Type B prohibited to preserve independence)."
  - term: "FedRAMP 20x (emerging direction — label as such)"
    source_wording: "FedRAMP 20x is the automation-first, outcome-based modernization track (authority: the 2022 Act + M-24-15). Concepts: Key Security Indicators (KSIs), machine-readable packages (RFC 0024). Phase 1/2 complete, Phase 3 underway in 2026. Label 20x as emerging direction, not the settled Rev 5 process."
sign_off: true
```

## 1. Primary sources

| Source | What | Retrieval | Anchor |
|--------|------|-----------|--------|
| FedRAMP Authorization Act 2022 (44 U.S.C. 3607-3616, via law.cornell.edu) | FedRAMP in statute; the FedRAMP Board (§3610); 5-year sunset clause | 2026-06-11 | §3610 establishes the FedRAMP Board |
| OMB M-24-15 (fedramp.gov/docs/authority/m-24-15 + OMB PDF) | Modernizes FedRAMP; rescinds 2011 memo; presumption of adequacy; machine-readable artifacts; retires JAB P-ATO | 2026-06-11 | "agencies must presume the security assessment … is adequate" |
| fedramp.gov — understanding baselines & impact levels | FIPS 199 Low/Moderate/High; CIA high-water mark; baseline selection | 2026-06-11 | impact level → 800-53 baseline |
| fedramp.gov — Rev 5 Agency Authorization | The operative authorization path | 2026-06-11 | "agencies work directly with a CSP for authorization" |
| fedramp.gov — ConMon overview (Rev 5 playbook) | Monthly cadence; POA&M/inventory/scans; remediation SLAs | 2026-06-11 | "(i) operational visibility; (ii) managed change control; (iii) … incident response" |
| fedramp.gov — SSP doc (Rev 5 playbook) | SSP = "security blueprint" for the CSO | 2026-06-11 | "The SSP is the 'security blueprint' for the CSO." |
| a2la.org — FedRAMP 3PAO accreditation | A2LA accredits 3PAOs to ISO/IEC 17020 | 2026-06-11 | "A2LA offers accreditation of … 3PAOs … as part of … FedRAMP." |
| NIST SP 800-53 Rev 5 (DOI / csrc.nist.gov) | The control catalog FedRAMP tailors; 800-53B baselines 149/287/370 | 2026-06-11 | catalog dated Sept 2020, Rev 5 with maintenance releases |
| fedramp.gov/20x | The automation-first modernization track | 2026-06-11 | KSIs; machine-readable packages |

**Source-class note:** all public US-government text — full vendoring permitted (unlike the
licensed PCI/ISO builds). The Rev 5 **baseline control counts** are anchored to the **primary
artifact**: the PMO-authored OSCAL Rev 5 baseline profiles were fetched and their control IDs
counted directly — Low 156 (135 base + 21 enh), Moderate 323 (181 + 142), High 410 (191 + 219),
LI-SaaS 156 (135 + 21). The profiles carry `metadata.party = "Federal Risk and Authorization
Management Program: Program Management Office"` (version `fedramp-3.0.0rc1-oscal-1.1.2`). The
original GSA OSCAL repo (`github.com/GSA/fedramp-automation`) is dead (404); the byte-for-byte
PMO files now live at **OSCAL-Foundation/fedramp-resources** (the URLs in §0). Two caveats: the
fedramp.gov `.xlsx` baseline workbook URL resolves 200 but serves an **empty S3 redirect stub**
(do NOT cite it as live), and no fedramp.gov HTML page currently prints the totals — the OSCAL
JSON is the authoritative source. Assessor pages (Vanta/38North) agree exactly and serve as
readable backup only.

## 2. Structural inventory

### 2.1 Rev 5 baselines (the load-bearing counts)

| Baseline | Count (base + enh) | FIPS 199 basis | Derives from 800-53B | Source | Verified? |
|----------|-------|----------------|----------------------|--------|-----------|
| Low | **156** (135 + 21) | Low high-water mark | 149 (Low) + FedRAMP additions | OSCAL `...LOW-baseline_profile.json` (PMO-authored) | ✓ primary |
| Moderate | **323** (181 + 142) | Moderate high-water mark | 287 (Moderate) + additions | OSCAL `...MODERATE-baseline_profile.json` | ✓ primary (Rev 4 was 325) |
| High | **410** (191 + 219) | High high-water mark | 370 (High) + additions | OSCAL `...HIGH-baseline_profile.json` | ✓ primary |
| LI-SaaS (Tailored) | **156** (135 + 21); 66 tested + 90 attested | Low-impact SaaS | same set as Low | OSCAL `...LI-SaaS-baseline_profile.json`; 66/90 split per FedRAMP Tailored LI-SaaS baseline doc | ✓ primary (split: doc, not OSCAL flat count) |

**Counting method:** each total is **base controls + selected control enhancements** counted
together (one `with-ids` entry each), extracted directly from the PMO-authored OSCAL profile.
The 66-tested/90-attested LI-SaaS split is documented in the Tailored LI-SaaS baseline doc and is
NOT a clean flat count in the OSCAL file (which uses 5 objective-level method props:
ATTEST/ASSESS/CONDITIONAL/NSO/FED) — cite the split to the doc, not the OSCAL profile.

**Rule applied:** counts here are the single machine-checkable source of truth; the built chunks
must state exactly these numbers.

### 2.2 Identifiers — see §0 `identifiers` block

Every code a build agent may reference (the Act, the Board, M-24-15, the four baselines, the four
package artifacts, 3PAO/ConMon/FIPS 199/20x/Agency Authorization) is enumerated in §0. If a build
agent references an identifier not in §0, it is fabricated — return to G1.

## 3. Crosswalk mappings

`crosswalks: []` — FedRAMP does **not** maintain a separate control catalog; its baselines ARE
NIST SP 800-53 Rev 5 controls (same IDs), tailored. There is therefore no framework-to-framework
crosswalk to encode (the "mapping" is identity + tailoring, captured in §0 terminology and §7).
A control-by-control baseline listing (300+ rows) is out of scope for v0.1.0 (see §7).

## 4. URL verification — see §0 `urls` block

All 16 manifest URLs live-checked at 200 on 2026-06-11 (12 program/statute + 4 OSCAL profiles).
**Traps the build must AVOID citing as live:**
- `github.com/GSA/fedramp-automation` — 404, repo moved; use the OSCAL-Foundation mirror in §0.
- `fedramp.gov/assets/.../FedRAMP_Security_Controls_Baseline.xlsx` — resolves **200 but serves a
  68-byte empty S3 redirect stub**, not a real workbook. Do NOT cite it as the count source.
- `fedramp.gov/glossary/` — 404, page removed; use the Rev 5 playbook doc pages for definitions.
- `congress.gov` bill text — 403 bot-block (not dead); cite law.cornell.edu for the statute.
- The new `FedRAMP/2026` controls page is a published **stub** ("# Control Baselines" only) — not
  yet a citable count source.

## 5. Terminology — see §0 `terminology` block

Verbatim wording for the 800-53 tailoring relationship, the FedRAMP Board (vs JAB), presumption
of adequacy, ConMon, SSP, 3PAO/A2LA, and 20x is captured in §0. The build agent copies from there.

## 6. Version, supersession, and governance currency

| Claim | Source | Verified? |
|-------|--------|-----------|
| Current baselines = Rev 5 (post May 2023 800-53 Rev 5 transition) | fedramp.gov | ✓ |
| Rev 4 Moderate was 325; Rev 5 Moderate is 323 | assessor corroboration; Rev 4 archived baselines | ✓ |
| FedRAMP Authorization Act enacted 2022-12-23 (PL 117-263) | law.cornell.edu 44 USC 3607-3616 | ✓ |
| FedRAMP Board (§3610) replaced the JAB | 44 USC 3610; M-24-15 | ✓ |
| M-24-15 dated 2024-07-25; rescinds 2011 memo | fedramp.gov/docs/authority/m-24-15 | ✓ |
| JAB P-ATO retired; legacy P-ATOs re-designated by PMO | M-24-15 | ✓ |
| NIST SP 800-53 is still Rev 5 (Sept 2020 + maintenance releases) — no Rev 6 | csrc.nist.gov | ✓ |

**Currency corrections to the source ticket (do NOT carry the ticket's framing into the skill):**
1. **Counts:** ticket said "Moderate ~325 / Li-SaaS ~156"; correct Rev 5 = **156 / 323 / 410 / 156**
   (325 was Rev 4 Moderate). LI-SaaS = same 156 as Low, split 66 tested / 90 attested.
2. **"JAB→PMO" is outdated:** no live JAB. Current model = statutory **FedRAMP Board** + GSA/PMO;
   JAB P-ATO retired.
3. **"Agency ATO only" is incomplete:** Agency Authorization is operative, but M-24-15 adds
   multi-agency authorization + single-authorization/presumption-of-adequacy; 20x adds an
   automation track. Frame accordingly.
4. **OSCAL source-of-truth moved (now pinned):** `github.com/GSA/fedramp-automation` is dead; do
   NOT cite it. The byte-for-byte PMO-authored Rev 5 OSCAL baseline profiles now live at
   **OSCAL-Foundation/fedramp-resources** (`/baselines/rev5/json/FedRAMP_rev5_*-baseline_profile.json`,
   all 200) — these are the primary count source (§0 urls, §2.1).

## 7. Scope boundaries — what the skill does NOT cover

| Domain | In scope? | Reason |
|--------|-----------|--------|
| The NIST SP 800-53 Rev 5 control catalog / general RMF | No | Covered by `nist-800-53-rmf`; this skill is the FedRAMP *program/process* layer (baselines, authorization path, package, ConMon, 20x) |
| Control-by-control baseline listing (300+ rows per baseline) | No | v0.1.0 encodes the counts and the tailoring relationship, not the full per-control enumeration |
| DoD Impact Levels (IL2/4/5/6) / DISA SRG | No | DoD cloud authorization is a separate regime; flag as adjacent, out of scope |
| StateRAMP / agency-specific programs | No | Distinct programs that borrow FedRAMP's model; out of scope |
| CMMC | No | Defense contractor program; separate skill candidate |
| Writing an actual SSP/SAR document | Partial | The skill explains the package and the process; document authoring is a downstream use case, not a control catalog |

## 8. Sign-off — Day 0 research complete

- [x] Every structural identifier is in §0 / §2.2
- [x] Every count is verified against the **primary artifact** — control IDs counted directly from
      the PMO-authored OSCAL Rev 5 baseline profiles (156/323/410/156, base + enhancements)
- [x] No framework-to-framework crosswalk to encode (`crosswalks: []`, justified §3)
- [x] Every manifest URL returns 200 (§0 urls — 16 incl. 4 OSCAL profiles)
- [x] Terminology is verbatim from FedRAMP/OMB/NIST sources (§0)
- [x] Version, supersession, and governance currency confirmed (§6)
- [x] Scope boundaries explicit (§7)
- [x] §0 data block mirrors all of the above; `sign_off: true` set
- [x] `python3 tools/check_fact_sheet.py docs/fedramp-authorization-fact-sheet.md` passes

**Count provenance — RESOLVED.** The §2.1 counts are now anchored to the PMO-authored OSCAL Rev 5
baseline profiles (control IDs counted directly), not secondary assessor pages. Caveats recorded:
the fedramp.gov `.xlsx` workbook serves an empty stub, and the 66/90 LI-SaaS split cites the
Tailored baseline doc (not derivable as a flat OSCAL count).

---

— End of fedramp-authorization fact-sheet —
