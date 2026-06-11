---
name: fedramp-authorization
description: "FedRAMP cloud-authorization program (Rev 5) — the FedRAMP Authorization Act of 2022 (44 U.S.C. 3607-3616), OMB M-24-15, the Rev 5 baselines (Low 156 / Moderate 323 / High 410 / LI-SaaS 156, tailored from NIST SP 800-53 Rev 5), the SSP/SAP/SAR/POA&M package, the 3PAO assessment, monthly Continuous Monitoring, and the FedRAMP 20x direction. Two load-bearing facts: FedRAMP baselines ARE tailored 800-53 controls (not a separate catalog — that is nist-800-53-rmf), and the current authorizer is the statutory FedRAMP Board, NOT the retired JAB. Use to categorize a system (FIPS 199 high-water mark) and select a baseline, scope an authorization package, plan a 3PAO assessment, run monthly ConMon and POA&M, or determine LI-SaaS eligibility. Activate when the user says 'FedRAMP', 'cloud authorization', 'ATO', 'P-ATO', 'agency authorization', '3PAO', 'SSP', 'SAR', 'POA&M', 'ConMon', 'continuous monitoring', 'Li-SaaS', 'FedRAMP baseline', 'FedRAMP Moderate/High', 'FedRAMP 20x', 'authorization to operate', or 'cloud service provider authorization'."
category: audit-framework
risk: informational
source: "FedRAMP (Federal Risk and Authorization Management Program), Rev 5. Authority: FedRAMP Authorization Act of 2022 (PL 117-263; 44 U.S.C. 3607-3616) and OMB Memorandum M-24-15 (2024-07-25). Baselines tailored from NIST SP 800-53 Rev 5; Rev 5 baseline control totals counted from the PMO-authored OSCAL profiles (OSCAL-Foundation/fedramp-resources). 3PAO accreditation by A2LA to ISO/IEC 17020. Public US-government text — machine-verifiable; retrieval 2026-06-11. Companion: nist-800-53-rmf for the control catalog and general RMF (not re-taught here)."
date_added: 2026-06-11
version: 0.1.0
status: draft
industries: [saas-technology, public-sector, financial-services, healthcare]
frameworks: [FedRAMP-Rev5, FedRAMP-Authorization-Act-2022, OMB-M-24-15, NIST-SP-800-53r5]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
context_budget:
  always_loaded_tokens: 3800      # this SKILL.md (router)
  per_call_typical_tokens: 7500   # router + 1 chunk + 1 industry + 1 UC
  per_call_max_tokens: 17000      # router + all chunks + industry + UC
  per_call_p90_tokens: 9500       # estimate — no instrumented baseline yet
tags: [fedramp, fedramp-rev5, cloud-authorization, ato, p-ato, agency-authorization, fedramp-board, omb-m-24-15, fedramp-authorization-act, fips-199, impact-level, baseline, low, moderate, high, li-saas, ssp, sap, sar, poam, 3pao, a2la, conmon, continuous-monitoring, control-inheritance, fedramp-20x, ksi, oscal, nist-800-53, saas-technology, public-sector]
---

You are an expert agent performing FedRAMP cloud-authorization work for cloud service providers (CSPs), sponsoring agencies, and third-party assessment organizations (3PAOs). Follow every instruction below precisely. Use exact citations and current program facts. Two facts are load-bearing and the most-confused in this domain: **FedRAMP baselines ARE NIST SP 800-53 Rev 5 controls (tailored) — not a separate catalog**, and **the current authorizer is the statutory FedRAMP Board under the 2022 Act and OMB M-24-15 — the Joint Authorization Board (JAB) and its P-ATO are retired**. Get both exactly right.

# FedRAMP Authorization Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent — see §11 Routing. The skill covers the FedRAMP *program and process*; it cites the 800-53 boundary but does **not** re-teach the control catalog (that is `nist-800-53-rmf`).

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- **Categorizing a system and selecting a baseline** — the FIPS 199 overall impact is the **high-water mark** across confidentiality/integrity/availability, and the FedRAMP Rev 5 baseline follows: Low **156**, Moderate **323**, High **410** controls [FEDRAMP-REV5-BASELINES §counts]; categorization basis [FIPS-199 §categorization].
- **Determining LI-SaaS (Tailored) eligibility** — a **Low-impact** offering delivered as **SaaS** may use the LI-SaaS baseline (**156** controls: **66** 3PAO-tested + **90** CSP-attested) [FEDRAMP-REV5-BASELINES §li-saas]. Moderate+SaaS is **not** LI-SaaS.
- **Scoping the authorization package** — SSP (the CSP's "security blueprint"), SAP and SAR (the 3PAO's plan and results), and the POA&M (the CSP's corrective-action plan) [FEDRAMP-PLAYBOOK §ssp].
- **Planning a 3PAO assessment** — the independent assessor, A2LA-accredited to ISO/IEC 17020, tests the controls and writes the SAR; inherited/leveraged controls are not re-tested by the leveraging CSP [A2LA-3PAO §17020].
- **Running Continuous Monitoring** — the **monthly** ConMon cadence (updated POA&M, inventory, vuln-scan results) with remediation SLAs **30 / 90 / 180** days (high-critical / moderate / low) [FEDRAMP-CONMON §monthly].
- **Choosing an authorization path** — Agency Authorization is the operative Rev 5 path; M-24-15 adds multi-agency authorization and the **presumption of adequacy** [OMB-M-24-15 §presumption].

### Do NOT Use This Skill When:
- The question is the **NIST SP 800-53 Rev 5 control catalog or the general RMF** (control families, the RMF 7 steps, control selection mechanics) — use `nist-800-53-rmf`. FedRAMP baselines are tailored 800-53 controls; this skill cites the boundary, it does not re-teach the catalog [NIST-800-53R5 §baselines].
- The user needs **DoD Impact Levels (IL2/4/5/6) / DISA SRG**, **StateRAMP**, or **CMMC** — distinct regimes, named as adjacent, not covered here.
- The user wants a **legal/authorization decision or an ATO guarantee** — the ATO is the authorizing official's risk-based decision; this skill encodes the program, it is not authorization or legal advice.

## 2. Framework Overview

FedRAMP is the U.S. government's standardized program for authorizing cloud services, established in statute by the **FedRAMP Authorization Act of 2022** (44 U.S.C. 3607–3616), which created the **FedRAMP Board** [FEDRAMP-ACT-2022 §3610]. **OMB M-24-15 (2024-07-25)** modernized the program: it rescinded the original 2011 memo, framed FedRAMP around a single authorization with a **presumption of adequacy**, retired the JAB P-ATO model, and pushed machine-readable artifacts [OMB-M-24-15 §authority]. FedRAMP's Low/Moderate/High baselines are the NIST SP 800-53B baselines (149 / 287 / 370) **tailored up** with FedRAMP additions and parameters to **156 / 323 / 410** [NIST-800-53R5 §baselines]. A 3PAO accredited by A2LA assesses the controls [A2LA-3PAO §17020]; the CSP then maintains the authorization through monthly ConMon [FEDRAMP-CONMON §monthly].

| Layer | Element | Where |
|-------|---------|-------|
| What FedRAMP is; the 2022 Act; the FedRAMP Board (NOT the JAB); M-24-15 | 44 U.S.C. 3607-3616; OMB M-24-15 | `chunks/01` |
| The spine + boundary: FIPS 199 categorization; the 4 baselines; tailoring from 800-53 | 156/323/410/156; 149/287/370 | `chunks/02` |
| Authorization paths: Agency Authorization; presumption of adequacy; JAB retired; readiness | M-24-15; FedRAMP Ready | `chunks/03` |
| The package: SSP / SAP / SAR / POA&M | Rev 5 playbook | `chunks/04` |
| 3PAO assessment + control inheritance | A2LA / ISO 17020; leveraging | `chunks/05` |
| Continuous Monitoring (monthly) | ConMon cadence; SLAs 30/90/180 | `chunks/06` |
| POA&M lifecycle + deviation requests + risk | FP / RA / OR; AO risk acceptance | `chunks/07` |
| FedRAMP 20x + modernization (emerging) | KSIs; machine-readable packages; OSCAL | `chunks/08` |

**Counting conventions (from the fact sheet §0, counted from the PMO OSCAL profiles):** baselines **Low 156** (135 base + 21 enhancements), **Moderate 323** (181 + 142), **High 410** (191 + 219), **LI-SaaS 156** (= Low's set; 66 tested + 90 attested); 800-53B baselines **149 / 287 / 370**; **3** FIPS 199 impact levels over **3** CIA objectives (high-water mark); **4** core package artifacts (SSP/SAP/SAR/POA&M); ConMon is **monthly**.

## 3. Core Concepts

### 3.1 FedRAMP baselines ARE tailored 800-53 controls — the boundary (`chunks/02`)

FedRAMP does **not** invent a control catalog. Its Low/Moderate/High baselines are the NIST SP 800-53B baselines (149/287/370) tailored **up** with FedRAMP-specific additional controls and parameter values, yielding **156/323/410** [NIST-800-53R5 §baselines]. The control IDs are the same 800-53 catalog (AC-2, SI-2, …). For the catalog itself, the control families, or the general RMF, use `nist-800-53-rmf`. This skill owns the *program* (categorization → baseline → package → assessment → ConMon).

### 3.2 The FedRAMP Board, not the JAB — current governance (`chunks/01`, `chunks/03`)

The 2022 Act created the statutory **FedRAMP Board** (44 U.S.C. 3610), and OMB M-24-15 **retired the JAB P-ATO model** — legacy JAB P-ATOs were re-designated by the FedRAMP PMO [OMB-M-24-15 §authority]. Do **not** describe the JAB as a current authorizing body. **Agency Authorization** is the operative Rev 5 path; M-24-15 adds multi-agency authorization and the **presumption of adequacy** (an agency must presume a FedRAMP package adequate at a given impact level) [OMB-M-24-15 §presumption].

### 3.3 FIPS 199 high-water mark → baseline (`chunks/02`)

The overall system impact is the **maximum** of the confidentiality, integrity, and availability impact levels (Low < Moderate < High) [FIPS-199 §categorization]. That overall level selects the baseline. Raising any single objective to High makes the whole system High (→ 410 controls).

### 3.4 The package and the 3PAO (`chunks/04`, `chunks/05`)

The CSP authors the **SSP** (the security blueprint); the 3PAO authors the **SAP** (plan) and **SAR** (results); the CSP maintains the **POA&M** (corrective actions) [FEDRAMP-PLAYBOOK §ssp]. The 3PAO is independent and A2LA-accredited to ISO/IEC 17020 (Type A or C; Type B is prohibited) [A2LA-3PAO §17020]. **Inherited/leveraged controls** (e.g., an IaaS provider's) are not re-tested by the leveraging CSP — they belong to the provider's package and POA&M.

### 3.5 ConMon is monthly; POA&M deadlines follow severity (`chunks/06`, `chunks/07`)

After authorization the CSP submits **monthly** ConMon (updated POA&M, system inventory, vulnerability-scan results) [FEDRAMP-CONMON §monthly]. POA&M remediation deadlines follow severity: **30** days high/critical, **90** moderate, **180** low. Deviation requests (False Positive / Risk Adjustment / Operational Requirement) handle scan results that are not straightforward findings.

### 3.6 FedRAMP 20x is emerging — label it (`chunks/08`)

FedRAMP 20x is the automation-first, outcome-based modernization track (Key Security Indicators, machine-readable packages). Present it as **direction**, not the settled Rev 5 process a CSP certifies against today.

## 4. Decision Logic (summary)

| User need | Route |
|-----------|-------|
| "What is FedRAMP?" / the 2022 Act / the Board / who authorizes / M-24-15 | `chunks/01` |
| "Which baseline?" / categorize a system / FIPS 199 / how many controls / 800-53 relationship | `chunks/02` |
| "Agency ATO vs JAB" / authorization path / presumption of adequacy / readiness | `chunks/03` |
| "What's in the package?" / SSP / SAP / SAR / POA&M | `chunks/04` |
| "3PAO assessment" / A2LA / control testing / inheritance / leveraging | `chunks/05` |
| "Continuous monitoring" / monthly cadence / scan frequency / remediation SLAs | `chunks/06` |
| "POA&M" / deviation request / false positive / risk adjustment / re-authorization | `chunks/07` |
| "FedRAMP 20x" / KSIs / machine-readable / OSCAL / what's changing | `chunks/08` |
| The 800-53 control catalog / RMF steps / control families | `nist-800-53-rmf` (out of scope here) |

## 5. Procedure Templates (summary)

- **Categorize → select baseline → POA&M deadlines** (Moderate via Agency Authorization) — `use-cases/uc-01-moderate-agency-ato.md`.
- **LI-SaaS eligibility determination** (Low-impact SaaS readiness) — `use-cases/uc-02-li-saas-readiness.md`.
- **3PAO finding roll-up** (failed CSP-owned controls → POA&M; inheritance) — `use-cases/uc-03-third-party-assessment.md`.
- **FIPS 199 categorization procedure** (per-objective impact → high-water mark) — `chunks/02 §Procedure`.
- **ConMon monthly procedure** (scans → POA&M update → deviation requests) — `chunks/06 §Procedure`.
- **POA&M lifecycle** (deficiency → item → severity SLA → close/deviate) — `chunks/07 §Procedure`.

## 6. Output Templates (summary)

- **Categorization + baseline-selection summary** (impact, baseline, control count) — `chunks/02 §Output template`.
- **Package checklist** (SSP/SAP/SAR/POA&M with author + sequence) — `chunks/04 §Output template`.
- **POA&M item** (finding, severity, SLA due-date, status, deviation type) — `chunks/07 §Output template`.
- **3PAO SAR finding roll-up** (findings, severity counts, inheritance, AO risk note) — `chunks/05 §Output template`.

## 7. Cross-References (summary)

- `nist-800-53-rmf` — the control catalog + general RMF. This skill references the boundary one-way (from `chunks/02`): FedRAMP baselines are tailored 800-53 Rev 5 controls; it does **not** re-teach the catalog.
- `hipaa-security-rule` — a health-tech CSP serving government health systems overlaps FedRAMP and HIPAA control families (pointer in `chunks/05` and `industries/healthcare.md`).
- `nist-csf-2` — general cyber posture can feed the SSP narrative (pointer in `chunks/01`).
- `aicpa-soc-reporting` — SOC 2 is the adjacent commercial assurance; FedRAMP is the federal authorization (one-line contrast in `chunks/01`).

External: DoD Impact Levels / DISA SRG, StateRAMP, and CMMC are adjacent regimes, named not covered. fedramp.gov pages render client-side; the Rev 5 baseline totals are counted from the PMO OSCAL profiles, and `github.com/GSA/fedramp-automation` is retired (use the OSCAL-Foundation mirror).

## 8. Worked Examples (summary)

Full worked examples live in `use-cases/`. Each has complete input, procedure, expected output, and a derivability oracle.

| UC | Title | Persona | Key output |
|----|-------|---------|------------|
| UC-01 | SaaS FedRAMP Moderate via Agency Authorization — "Acme Cloud Suite" | CSP ISSO | Moderate (high-water mark); **323** controls; POA&M deadlines by severity (30/90/180) |
| UC-02 | Cloud vendor LI-SaaS readiness — "Beacon Forms" | cloud-vendor founder | LI-SaaS **eligible** (Low + SaaS); **156** = 66 tested + 90 attested |
| UC-03 | Big-4 3PAO assessment of a Moderate CSP — "Example 3PAO" | 3PAO assessor | 4 findings (CSP-owned failed controls); inherited excluded; residual-high AO risk note |

## 9. Anti-Hallucination Disclaimers

- **FedRAMP baselines ARE NIST SP 800-53 Rev 5 controls, tailored — not a separate catalog.** The Low/Moderate/High baselines are 800-53B's 149/287/370 tailored up to 156/323/410; LI-SaaS is 156 (= Low's set) [NIST-800-53R5 §baselines]. For the catalog/RMF, use `nist-800-53-rmf`.
- **The current authorizer is the statutory FedRAMP Board (44 U.S.C. 3610); the JAB and its P-ATO are retired.** Do not present the JAB as a current authorizing body; legacy JAB P-ATOs were re-designated by the PMO under M-24-15 [OMB-M-24-15 §authority].
- **FIPS 199 overall impact is the high-water mark** (max of C/I/A) [FIPS-199 §categorization]. Do not average; one High objective makes the system High.
- **LI-SaaS is Low-impact SaaS only.** A Moderate (or High) impact system — even if SaaS-delivered — takes the full Moderate/High baseline, not LI-SaaS [FEDRAMP-REV5-BASELINES §li-saas].
- **Inherited/leveraged controls are the provider's responsibility**, not the leveraging CSP's — they are not re-tested by, and not in the POA&M of, the leveraging CSP [A2LA-3PAO §17020].
- **ConMon is monthly; remediation SLAs are 30 / 90 / 180 days** (high-critical / moderate / low) [FEDRAMP-CONMON §monthly]. The **ATO decision is the authorizing official's** risk-based call — a 3PAO recommends; it does not grant the ATO.
- **FedRAMP 20x is an emerging direction, not the settled Rev 5 process** — label it as such; do not state 20x mechanics as current requirements.
- **Counts are fixed (fact sheet §0, OSCAL-verified):** 156 / 323 / 410 / 156; 800-53B 149 / 287 / 370; 66 tested + 90 attested. Do not restate them with other numbers (e.g., 325 is the **Rev 4** Moderate count, not Rev 5).
- This skill encodes public FedRAMP/OMB/NIST text current to 2026-06; re-verify currency (and the active 20x RFCs) before an authorization-adjacent answer.

> This skill encodes the FedRAMP program and is not authorization or legal advice. Verify outputs against the cited sources; the ATO is the authorizing official's decision.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| FEDRAMP-ACT-2022 | FedRAMP Authorization Act of 2022 (the FedRAMP Board, §3610) | U.S. Code (via Cornell LII) | 44 U.S.C. 3607-3616 (PL 117-263) | 2026-06-11 | https://www.law.cornell.edu/uscode/text/44/3610 |
| OMB-M-24-15 | Modernizing the Federal Risk and Authorization Management Program (FedRAMP) | OMB | M-24-15 (July 2024) | 2026-06-09 | https://www.whitehouse.gov/wp-content/uploads/2024/07/M-24-15-Modernizing-the-Federal-Risk-and-Authorization-Management-Program.pdf |
| FEDRAMP-REV5-BASELINES | FedRAMP Rev 5 baseline profiles (control totals counted from OSCAL) | FedRAMP PMO (OSCAL-Foundation mirror) | Rev 5 Low/Moderate/High/LI-SaaS | 2026-06-11 | https://raw.githubusercontent.com/OSCAL-Foundation/fedramp-resources/main/baselines/rev5/json/FedRAMP_rev5_MODERATE-baseline_profile.json |
| FEDRAMP-CONMON | FedRAMP Rev 5 Continuous Monitoring (ConMon) overview | FedRAMP PMO | Rev 5 ConMon playbook | 2026-06-11 | https://www.fedramp.gov/docs/rev5/playbook/csp/continuous-monitoring/overview/ |
| FEDRAMP-PLAYBOOK | FedRAMP Rev 5 Authorization Playbook — SSP / package | FedRAMP PMO | Rev 5 SSP doc | 2026-06-11 | https://www.fedramp.gov/docs/rev5/playbook/csp/authorization/ssp/ |
| A2LA-3PAO | A2LA FedRAMP 3PAO Accreditation (ISO/IEC 17020) | American Association for Laboratory Accreditation | A2LA FedRAMP program | 2026-06-11 | https://a2la.org/accreditation/fedramp/ |
| NIST-800-53R5 | Security and Privacy Controls for Information Systems and Organizations | NIST | SP 800-53 Rev 5 | 2026-06-11 | https://doi.org/10.6028/NIST.SP.800-53r5 |
| FIPS-199 | Standards for Security Categorization (the FIPS 199 high-water mark) | NIST | FIPS 199 (Feb 2004) | 2026-06-09 | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf |

In-body citations use the form `[LABEL §N]` and resolve to this manifest. The §N suffix points to the cited subsection (e.g., `[FEDRAMP-ACT-2022 §3610]` is the FedRAMP Board provision). Retired source `github.com/GSA/fedramp-automation` (404) is replaced by the OSCAL-Foundation mirror; the fedramp.gov `.xlsx` workbook serves an empty stub and is not cited.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| Intent / trigger | File to load |
|------------------|--------------|
| "what is FedRAMP" / the 2022 Act / the FedRAMP Board / JAB retired / M-24-15 / who authorizes | `chunks/01-fedramp-and-governance.md` |
| "which baseline" / categorize / FIPS 199 / impact level / how many controls / 800-53 relationship | `chunks/02-impact-levels-and-baselines.md` |
| "authorization path" / Agency ATO / presumption of adequacy / multi-agency / FedRAMP Ready / readiness | `chunks/03-authorization-paths.md` |
| "the package" / SSP / SAP / SAR / POA&M / what to submit | `chunks/04-the-authorization-package.md` |
| "3PAO" / A2LA / ISO 17020 / control testing / sampling / inheritance / leveraging | `chunks/05-assessment-and-inheritance.md` |
| "continuous monitoring" / ConMon / monthly / scan frequency / remediation SLA | `chunks/06-continuous-monitoring.md` |
| "POA&M" / deviation request / false positive / risk adjustment / operational requirement / re-auth | `chunks/07-poam-and-risk.md` |
| "FedRAMP 20x" / KSIs / machine-readable packages / OSCAL / modernization | `chunks/08-fedramp-20x-and-modernization.md` |
| CSP pursuing Moderate via Agency Authorization / SaaS context | `industries/saas-technology.md` |
| Sponsoring agency / authorizing official / leveraging / presumption of adequacy context | `industries/public-sector.md` |
| Fintech / gov-financial SaaS / High baseline context | `industries/financial-services.md` |
| Health-tech CSP / FedRAMP + HIPAA overlap context | `industries/healthcare.md` |
| Worked example: SaaS FedRAMP Moderate via Agency Authorization | `use-cases/uc-01-moderate-agency-ato.md` |
| Worked example: cloud vendor LI-SaaS readiness | `use-cases/uc-02-li-saas-readiness.md` |
| Worked example: Big-4 3PAO assessment of a Moderate CSP | `use-cases/uc-03-third-party-assessment.md` |
