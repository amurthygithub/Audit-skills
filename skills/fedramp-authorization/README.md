# FedRAMP Cloud Authorization (Rev 5) — fedramp-authorization

The framework skill for the **FedRAMP cloud-authorization program** (Rev 5) — the **FedRAMP Authorization Act of 2022** (44 U.S.C. 3607-3616), **OMB M-24-15** (2024-07-25), the Rev 5 baselines (Low **156** / Moderate **323** / High **410** / LI-SaaS **156**, tailored from NIST SP 800-53 Rev 5), the SSP/SAP/SAR/POA&M package, the 3PAO assessment, monthly Continuous Monitoring, and the FedRAMP 20x direction. The skill exists to get two load-bearing facts exactly right — **FedRAMP baselines ARE tailored 800-53 controls** (not a separate catalog — that is `nist-800-53-rmf`), and **the current authorizer is the statutory FedRAMP Board, NOT the retired JAB** — and to build the categorization → baseline → package → assessment → ConMon process around them.

Status: **draft v0.1.0**, on Tier 0 Spine, 65 skill-local tests passing (oracle, grounding, trace, metamorphic, adversarial, telemetry, chunk suites) plus root-level lint/consistency/registry suites, linter-clean. The skill uses the **router + chunks pattern** — `SKILL.md` is the router, the deep-dive content lives in 8 chunk files (≤200 lines each) loaded on demand. The skill body is real (full decision logic, output templates, citation manifest); the bundled executor is a deterministic stub in this version, and the LLM-backed executor ships later (like the other Spine skills).

## What it does

- Categorizes a system and selects its baseline: the FIPS 199 overall impact is the **high-water mark** across confidentiality / integrity / availability, and the Rev 5 baseline follows — Low **156**, Moderate **323**, High **410** controls.
- Determines **LI-SaaS (Tailored)** eligibility: a **Low-impact** offering delivered as **SaaS** may use the LI-SaaS baseline (**156** controls = **66** 3PAO-tested + **90** CSP-attested). Moderate+SaaS is **not** LI-SaaS.
- Scopes the **authorization package** — SSP (the CSP's "security blueprint"), SAP and SAR (the 3PAO's plan and results), and the POA&M (the CSP's corrective-action plan).
- Plans the **3PAO assessment** and computes the SAR finding roll-up: the assessor (A2LA-accredited to ISO/IEC 17020) tests the controls; inherited/leveraged controls are not re-tested by, and not in the POA&M of, the leveraging CSP.
- Runs **monthly Continuous Monitoring** and computes POA&M remediation deadlines from severity (SLAs **30 / 90 / 180** days — high-critical / moderate / low).

## When to use

- A CSP needs a system **categorized** (FIPS 199 high-water mark) and the **baseline + control count** selected, or POA&M remediation deadlines reasoned from SAR findings.
- A cloud vendor needs an **LI-SaaS eligibility determination** (Low-impact SaaS readiness) and the 66-tested / 90-attested Tailored split.
- A 3PAO (or an agency reviewer) needs a **SAR finding roll-up** with inheritance handled and a residual-risk note for the authorizing official.
- A sponsoring agency needs the **Agency Authorization** path, the **presumption of adequacy**, and the leveraging / ATO-decision framing.

## When NOT to use

- The **NIST SP 800-53 Rev 5 control catalog or the general RMF** (control families, the RMF 7 steps, control-selection mechanics) — use `nist-800-53-rmf`. FedRAMP baselines are tailored 800-53 controls; this skill cites the boundary, it does not re-teach the catalog.
- **DoD Impact Levels (IL2/4/5/6) / DISA SRG**, **StateRAMP**, or **CMMC** — distinct regimes, named as adjacent, not covered here.
- A **legal/authorization decision or an ATO guarantee** — the ATO is the authorizing official's risk-based decision; this skill encodes the program, it is not authorization or legal advice.

## Use cases (3)

- **UC-01 — SaaS FedRAMP Moderate via Agency Authorization** (Acme Cloud Suite, CSP ISSO): per-objective FIPS 199 (C=Moderate, I=Low, A=Low) → overall **Moderate** (high-water mark) → **323** controls; each SAR finding's POA&M deadline = identified-date + the severity SLA (30 / 90 / 180 days) (`FEDRAMP_MODERATE`).
- **UC-02 — Cloud vendor LI-SaaS readiness** (Beacon Forms, cloud-vendor founder): all three CIA objectives Low + SaaS-delivered → LI-SaaS **eligible**; Tailored baseline **156** = **66** 3PAO-tested + **90** CSP-attested (`LI_SAAS_ELIGIBLE`). Moderate+SaaS would flip to the full Moderate baseline.
- **UC-03 — Big-4 3PAO assessment of a Moderate CSP** (Example 3PAO LLP): a control-test set of 8 controls → **4** findings (failed controls the CSP **owns**, not inherited); inherited-and-failed excluded; POA&M item count = 4; a residual-high finding raises the authorizing-official risk note (`SAR_FINDINGS_4`).

Every UC is seed-backed with **derivability oracles**: the tests recompute each expected number independently from `data/seeds/` (the high-water-mark categorization, the baseline-count lookup, each POA&M due-date, the inheritance-aware finding roll-up) — no expected value is echoed from the stub's own code path.

## Acronym key

| Acronym | Expansion |
|---------|-----------|
| FedRAMP | Federal Risk and Authorization Management Program |
| CSP | Cloud Service Provider |
| 3PAO | Third Party Assessment Organization (independent assessor) |
| SSP | System Security Plan — the CSP's "security blueprint" for the offering |
| SAP | Security Assessment Plan — the 3PAO's approach to assessing the controls |
| SAR | Security Assessment Report — the 3PAO's results, vulnerabilities, and recommendation |
| POA&M | Plan of Action & Milestones — the CSP's corrective-action plan (tracked monthly) |
| ConMon | Continuous Monitoring — the monthly POA&M / inventory / scan submission |
| ATO | Authorization to Operate — the authorizing official's risk-based decision |
| AO | Authorizing Official — grants (or declines) the ATO |
| FIPS 199 | Standards for Security Categorization — Low/Moderate/High by CIA-triad impact (high-water mark) |
| LI-SaaS | Low-Impact SaaS (Tailored) baseline — Low-impact + SaaS-delivered only |
| KSI | Key Security Indicator — a FedRAMP 20x automation-era construct |
| OSCAL | Open Security Controls Assessment Language — the machine-readable artifact format |

## 30-second quick start

```python
import sys, json

sys.path.insert(0, "skills/fedramp-authorization/tests")  # stub executor

from fedramp_authorization_stub import run_skill

payload = json.load(open("skills/fedramp-authorization/data/seeds/uc-01-input.json"))
out = run_skill("UC-01", payload)
print(out["overall_impact"])      # -> "Moderate" (high-water mark of C/I/A)
print(out["baseline_controls"])   # -> 323     (Moderate Rev 5 baseline)
print(out["poam_open"])           # -> 5       (one POA&M item per SAR finding)
print(out["poam"][0]["remediation_due"])  # -> "2025-03-31" (identified + 30d, High severity)
```

The stub is a **deterministic** reference executor — it COMPUTES its outputs from the seed facts (derivability oracles), it does not echo a hardcoded result, and it does not perform a FedRAMP authorization. The LLM-backed executor (the V3 eval lane) replaces it later and, like the other skills, needs an API key / model access to run; the stub needs neither.

## Caveats that govern everything here

1. **FedRAMP baselines ARE NIST SP 800-53 Rev 5 controls, tailored — not a separate catalog.** The Low/Moderate/High baselines are 800-53B's 149 / 287 / 370 tailored **up** with FedRAMP additions and parameters to **156 / 323 / 410**; the control IDs are the same 800-53 catalog (AC-2, SI-2, …). For the catalog or the general RMF, use `nist-800-53-rmf`.
2. **The current authorizer is the statutory FedRAMP Board (44 U.S.C. 3610); the JAB and its P-ATO are retired.** OMB M-24-15 retired the JAB P-ATO model — legacy JAB P-ATOs were re-designated by the FedRAMP PMO. Do not present the JAB as a current authorizing body. **Agency Authorization** is the operative Rev 5 path.
3. **FedRAMP 20x is an emerging direction, not the settled Rev 5 process.** KSIs and machine-readable packages are presented as direction, never as current requirements a CSP certifies against today.

## Industries covered (4)

- [saas-technology](industries/saas-technology.md) — CSP pursuing **Moderate via Agency Authorization** (the most common path; SSP ~323 controls, monthly ConMon) (UC-01)
- [public-sector](industries/public-sector.md) — the **sponsoring agency / AO side**: leveraging a package, the presumption of adequacy, the ATO decision, multi-agency reuse
- [financial-services](industries/financial-services.md) — fintech / gov-financial SaaS needing the **High baseline** (410): the High-vs-Moderate delta, stricter ConMon
- [healthcare](industries/healthcare.md) — health-tech CSP serving government health systems: **FedRAMP + HIPAA** overlap, PHI-workload categorization

## Cross-references to other skills

- `nist-800-53-rmf` — authoritative for the 800-53 Rev 5 control catalog and the general RMF; this skill references the boundary one-way (FedRAMP baselines are tailored 800-53 controls), it does not re-teach the catalog
- `hipaa-security-rule` — a health-tech CSP serving government health systems overlaps FedRAMP and HIPAA control families
- `nist-csf-2` — general cyber posture can feed the SSP narrative (pointer only)
- `aicpa-soc-reporting` — SOC 2 is the adjacent commercial assurance; FedRAMP is the federal authorization (one-line contrast)

## What this skill is NOT

- Not authorization or legal advice — the ATO is the authorizing official's risk-based decision, and no output here is an authorization guarantee
- Not the 800-53 control catalog or general RMF (it references the boundary; `nist-800-53-rmf` owns the catalog)
- Not DoD Impact Levels / DISA SRG, StateRAMP, or CMMC (named as adjacent regimes only)
- Not a per-control baseline enumeration — v0.1.0 encodes the four totals (OSCAL-verified) and the tailoring relationship, not the 300+-row per-control listing

## Public-source note

Every fact in this skill is grounded in **public US-government text**: the FedRAMP Authorization Act of 2022 (44 U.S.C. 3607-3616, via law.cornell.edu), OMB M-24-15 (2024-07-25), the fedramp.gov Rev 5 playbook (SSP, ConMon), the A2LA 3PAO accreditation program (ISO/IEC 17020), and NIST SP 800-53 Rev 5 / 800-53B. The Rev 5 baseline counts (156 / 323 / 410 / 156) are counted directly from the **PMO-authored OSCAL Rev 5 baseline profiles** (the OSCAL-Foundation/fedramp-resources mirror; the retired `github.com/GSA/fedramp-automation` repo and the empty fedramp.gov `.xlsx` workbook stub are not cited). No real FedRAMP package data: the seeded CSPs/systems (Acme Cloud Suite, Beacon Forms, Example 3PAO) are fictional and the seeds carry structural facts only. Counts are Rev 5 as of 2026-06 (325 is the Rev 4 Moderate count, not Rev 5) — re-verify currency and the active 20x RFCs before an authorization-adjacent answer.
