---
name: nist-800-53-rmf
description: "Perform NIST SP 800-53 Rev 5 control selection, implementation, assessment, and continuous monitoring using the NIST Risk Management Framework (SP 800-37 Rev 2 RMF). Covers FIPS 199 categorization, baseline selection (Low/Moderate/High), 800-53A assessment procedures, control inheritance (FedRAMP/shared services/cloud), SAR/POA&M and ATO determination. Activate when performing RMF Step 2 (categorize), Step 3 (select), Step 4 (implement), Step 5 (assess), Step 6 (authorize), or Step 7 (monitor); when mapping SOC 2 / ISO 27001 / PCI / HIPAA to 800-53; when planning or executing a FedRAMP authorization; or when responding to a federal/DoD assessment."
category: audit
risk: high
source: "NIST SP 800-53 Rev 5 (2024 security & privacy control catalog), SP 800-37 Rev 2 (RMF), SP 800-53A Rev 5 (assessment procedures), FIPS 199 (categorization), FIPS 200 (minimum security requirements), SP 800-30 Rev 1 (risk assessment), SP 800-137 (ISCM), SP 800-61 Rev 2 (IR), OMB A-130, FedRAMP modernization memo OMB M-24-15"
date_added: 2026-05-25
version: 0.2.0
status: draft
industries: [public-sector, saas-technology, financial-services, healthcare, other]
frameworks: [NIST-SP-800-53-Rev5, NIST-SP-800-37-Rev2, NIST-SP-800-53A-Rev5, FIPS-199, FIPS-200, NIST-SP-800-30-Rev1, FedRAMP-Rev5, OMB-A-130, SOC-2-TSC-2017, ISO-27001-2022, PCI-DSS-v4.0, HIPAA-Security-Rule]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
token_baseline_target:
  input_p90: 14000
  output_p90: 4500
context_budget:
  always_loaded_tokens: 3000      # this SKILL.md (router)
  per_call_typical_tokens: 6000   # router + 1 chunk + 1 industry + 1 UC
  per_call_max_tokens: 15000      # router + all chunks + industry + UC
  per_call_p90_tokens: 8000       # measured after first instrumented run
tags: [nist, 800-53, 800-37, rmf, fips-199, fedramp, ato, sar, poam, control-baseline, iscm, cybersecurity, it-audit, public-sector, saas, govtech, defense, baselining, crosswalk, csf, iso-27001, pci, hipaa, soc2, board-deck, questionnaire-reuse, caic, sig-lite, vsaq]
---

You are an expert agent performing NIST 800-53 / RMF-based security and privacy work. Follow every instruction below precisely. Use official NIST/FIPS terminology exclusively.

# NIST 800-53 RMF Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent. See §11 Routing for the table.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Performing FIPS 199 security categorization of an information system.
- Selecting or tailoring a NIST SP 800-53 Rev 5 control baseline (Low/Moderate/High).
- Walking the NIST RMF (SP 800-37 Rev 2) — Prepare → Categorize → Select → Implement → Assess → Authorize → Monitor.
- Drafting or reviewing a System Security Plan (SSP), Security Assessment Report (SAR), Plan of Action & Milestones (POA&M), or Authorization Decision Letter.
- Performing (or supporting) a FedRAMP authorization (Low/Moderate/High) or agency ATO.
- Mapping SOC 2 TSC / ISO 27001:2022 / PCI DSS v4.0 / HIPAA Security Rule / NIST CSF 2.0 → NIST 800-53.
- Performing continuous monitoring (Step 7) — ISCM strategy, control assessments, POA&M management, configuration change management.
- Responding to a federal, DoD, intelligence-community, or state-RMF assessment finding.
- Inheritance analysis — which controls the system inherits from a cloud provider versus which it must implement itself.
- Reusing NIST 800-53 / FedRAMP evidence for customer security questionnaires (CAIQ, SIG Lite, VSAQ).
- Using the board-ready audit committee deck template (see aicpa-soc-reporting/assets/board_deck_template.md).

### Do NOT Use This Skill When:
- The user needs a financial-statement audit opinion (use the AICPA SOC or PCAOB skill instead).
- The user needs pure penetration testing (use a security testing methodology).
- The user wants a legal interpretation of FISMA, FedRAMP authorization boundaries, or OMB memos (consult counsel).
- The system is purely commercial with no federal nexus and no customer-imposed 800-53 obligation — start with the COSO/SOC 2 skill and return to this one only if the crosswalk shows an 800-53 requirement.
- Replacing a qualified ISSO, ISSM, AO, or 3PAO. This skill encodes the framework; it does not certify the practitioner.

## 2. Framework Overview

The NIST 800-53 / RMF stack is the U.S. federal government's primary cybersecurity and privacy control catalog and the process by which systems are authorized to operate.

| Layer | Document | Role |
|-------|----------|------|
| Categorize | [FIPS-199] | Categorize CIA |
| Categorize (min reqs) | [FIPS-200] | Minimum security requirements per FIPS 199 |
| Risk assessment | [NIST-SP-800-30-Rev1] | Threat, vulnerability, likelihood, impact |
| Control catalog | [NIST-SP-800-53-Rev5] | 20 control families, ~1,000 controls |
| Select | NIST SP 800-37 Rev 2 RMF Step 3 | Choose baseline, tailor, document |
| Implement | NIST SP 800-37 Rev 2 RMF Step 4 | Apply controls; document in SSP |
| Assess | [NIST-SP-800-53A-Rev5] | Assessment procedures; SAR |
| Authorize | NIST SP 800-37 Rev 2 RMF Step 6 | ATO letter, ATO with conditions, Denial |
| Monitor | NIST SP 800-37 Rev 2 RMF Step 7; [NIST-SP-800-137] | ISCM strategy, ongoing assessment, change control |
| Process | [NIST-SP-800-37-Rev2] | The seven-step RMF |

**FedRAMP overlay:** [FedRAMP-Rev5] defines a process and authorization boundary above RMF. FedRAMP Rev 5 is the de-facto requirement for any cloud service offering used by U.S. federal agencies. The PT (privacy) and SR (supply chain) families were added in Rev 5.

### 2.1 Related frameworks (crosswalk context)

The 800-53 control catalog is the de-facto hub of the U.S. compliance ecosystem. The following frameworks are commonly crosswalked to or from 800-53 — see `chunks/09-crosswalk.md` for the point-of-control mappings:

- **NIST CSF 2.0** ([NIST-CSF-2.0]) — the Cybersecurity Framework (Function/Category/Subcategory hierarchy) maps cleanly to 800-53 control families; used for executive-level risk reporting.
- **NIST SP 800-66 Rev 2** ([NIST-SP-800-66-Rev2]) — implements the HIPAA Security Rule; the 800-53 ↔ HIPAA mapping is the de-facto standard for HIPAA-covered entities seeking federal contracts.
- **HIPAA Security Rule** ([HIPAA-Security-Rule]) — 45 CFR § 164.302–164.318; crosswalked to 800-53 for federal-grant and contract scenarios.
- **ISO 27001:2022** ([ISO-27001-2022]) — international ISMS standard; Annex A controls map to 800-53 with ~70% overlap.
- **PCI DSS v4.0** ([PCI-DSS-v4.0]) — payment card industry; 12 requirements map to a subset of 800-53 families.
- **SOC 2 / TSC 2017** ([SOC-2-TSC-2017]) — the AICPA Trust Services Criteria align to the COSO 2013 framework (CC1-CC5 mirror the 17 COSO principles); mapping to 800-53 is many-to-many via published crosswalks, never 1:1.
- **CMMC 2.0** ([CMMC-2.0]) — DoD's cybersecurity maturity model; Level 2 = the 110 NIST SP 800-171 requirements (a CUI-focused subset, narrower than 800-53 Moderate), Level 3 adds selected SP 800-172 requirements.
- **OMB M-24-15** ([OMB-M-24-15]) — Modernizing FedRAMP (July 2024); sets FedRAMP modernization direction and agency reuse expectations.

Each chunk can be crosswalked to any of these via `data/crosswalks/`.

## 3. Core Concepts

### 3.1 The RMF — seven steps

```
Prepare ──► Categorize ──► Select ──► Implement ──► Assess ──► Authorize ──► Monitor
  ▲                                                                          │
  └──────────────── continuous improvement / re-authorize ◄───────────────────┘
```

- **Prepare (Step 1)** — context, mission, risk tolerance, roles.
- **Categorize (Step 2)** — FIPS 199 impact (Low/Moderate/High) for C, I, A.
- **Select (Step 3)** — baseline; tailor; produce SSP (initial).
- **Implement (Step 4)** — deploy controls; update SSP.
- **Assess (Step 5)** — 3PAO (FedRAMP) or independent assessor; produces SAR.
- **Authorize (Step 6)** — AO reviews SAR + POA&M; issues ATO, ATO w/ conditions, or Denial.
- **Monitor (Step 7)** — ISCM; annual control assessment; change control; incident-driven re-assessment.

### 3.2 Control families (20 (incl. PT and SR))

AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, **PT (Rev 5)**, RA, SA, SC, SI, **SR (Rev 5)**. See `chunks/03-baseline.md` for the full table and baseline counts.

### 3.3 Common control & inheritance

- **Common control** — implemented at org level; inheritable.
- **System-specific** — implemented at system level.
- **Hybrid** — partly inherited, partly system-specific.
- **Inheritance** (FedRAMP) — system inherits from cloud provider when boundary, narrative, and assessment evidence are inherited via the provider's package.
- **Inheritance** (Agency ATO, non-FedRAMP) — agency-operated systems or commercial services not under FedRAMP may inherit common controls from the agency's enterprise common-control catalog or from a commercial IaaS/SaaS provider with a current SOC 2 Type II + ISO 27001 certification. The inheritor must validate the source provider's assessment currency (report date within 12 months), map provider controls to 800-53 via a crosswalk, and document residual controls. Agency-to-agency inheritance (e.g., shared services) requires an MOU or ISA that defines the shared boundary, assessment responsibility, and incident notification. The AO must explicitly accept inherited control evidence during ATO review.

## 4. Decision Logic (summary)

Full logic in chunks. Summary:

- **Categorize** — high-water mark across C, I, A. `chunks/02-categorize.md §Decision logic`.
- **Select baseline** — table lookup from system category. `chunks/03-baseline.md`.
- **Assess** — for each objective, determination = satisfied / other_than_satisfied / N/A. `chunks/05-assess.md`.
- **Finding severity → POA&M risk** — see `chunks/05-assess.md §Finding severity`.
- **ATO decision** — see `chunks/06-authorize.md §ATO decision logic`.
- **Inheritance** — see `chunks/04-implement.md §Common control & inheritance model`.

## 5. Procedure Templates (summary)

- **Categorize** — `chunks/02-categorize.md §Procedure` (6 steps).
- **Select + tailor** — `chunks/03-baseline.md §Procedure` (7 steps).
- **Implement** — `chunks/04-implement.md §Procedure` (5 steps).
- **Assess** — `chunks/05-assess.md §Procedure` (6 steps).
- **Authorize** — `chunks/06-authorize.md §Procedure` (4 steps).
- **Monitor (ISCM)** — `chunks/07-monitor.md §Procedure` (6 steps).
- **Crosswalk** — `chunks/09-crosswalk.md §Procedure` (use `data/crosswalks/`).

## 6. Output Templates (summary)

- **FIPS 199 categorization** YAML — `chunks/02-categorize.md §Output template`.
- **Control selection** YAML — `chunks/03-baseline.md §Output template`.
- **SSP §10 implementation status** YAML — `chunks/04-implement.md §SSP template`.
- **SAR finding** YAML — `chunks/05-assess.md §Output template`.
- **POA&M item** YAML — `chunks/06-authorize.md §POA&M template`.
- **ATO decision letter** text — `chunks/06-authorize.md §ATO letter template`.
- **ISCM strategy** YAML — `chunks/07-monitor.md §SSP §13 template`.

## 7. Cross-References (summary)

See `chunks/09-crosswalk.md` for the full table. Quick map:

- `isaca-audit-methodology` — ITGC, COBIT, ISACA risk-based planning.
- `coso-internal-controls` — COSO ICIF, SOX 404, AS 2201.
- `aicpa-soc-reporting` — SOC 1/2/3, TSC criteria.
- `audit-workpapers` — AS 1215, AS 1105, sampling.

External: SOC 2, ISO 27001, PCI DSS, HIPAA, NIST CSF, ISO 27701, FedRAMP, CMMC.

## 8. Worked Examples (summary)

Full worked examples live in `use-cases/`. Each has complete input, procedure, expected output, and oracle.

| UC | Title | Industry | Key output |
|----|-------|----------|------------|
| UC-01 | FedRAMP-bound SaaS categorizes FIPS-199 Moderate | saas-technology, public-sector | Categorization, baseline, inheritance map |
| UC-02 | Federal agency Step 6 authorization: SAR 22 findings → POA&M, AO risk-accepts 14, ATO w/ conditions | public-sector | ATO letter, POA&M, residual-risk memo |
| UC-03 | Enterprise fin-svcs maps SOC 2 → 800-53 Moderate (SOC 2 to 800-53 mapping, 94 gap controls) | financial-services, saas-technology | Crosswalk, gap list, remediation plan |

## 9. Anti-Hallucination Disclaimers

- **Control counts** (~325 Moderate, ~421 High) are derived; verify against current NIST publication.
- **800-53A objectives** enumeration varies by control; not the same as enhancement enumeration.
- **Rev 5** — confirm the correct baseline revision applies.
- **FedRAMP High ≠ NIST 800-53 High** — FedRAMP adds controls. Consult fedramp.gov.
- **Categorization** is professional judgment; this skill encodes the framework.
- **AO authority** is statutory; the skill does not designate AOs.

> This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| NIST-SP-800-53-Rev5 | Security and Privacy Controls for Information Systems and Organizations | NIST | Rev 5 (Sept 2020) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| NIST-SP-800-37-Rev2 | Risk Management Framework for Information Systems and Organizations | NIST | Rev 2 (Dec 2018) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/37/r2/final |
| NIST-SP-800-53A-Rev5 | Assessing Security and Privacy Controls | NIST | Rev 5 (Jan 2022) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/53/a/r5/final |
| FIPS-199 | Standards for Security Categorization | NIST | FIPS 199 (Feb 2004) | 2026-05-25 | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf |
| FIPS-200 | Minimum Security Requirements for Federal Information and Information Systems | NIST | FIPS 200 (Mar 2006) | 2026-05-25 | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.200.pdf |
| NIST-SP-800-30-Rev1 | Guide for Conducting Risk Assessments | NIST | Rev 1 (Sept 2012) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/30/r1/final |
| NIST-SP-800-60 | Guide for Mapping Types of Information and Information Systems to Security Categories (Vol I & II) | NIST | Rev 1 (Aug 2008; current as of 2026) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final |
| NIST-SP-800-137 | Information Security Continuous Monitoring | NIST | Sept 2011 | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/137/final |
| FedRAMP-Rev5 | FedRAMP Baselines and ConMon Strategy Guide | FedRAMP PMO | Rev 5 | 2026-05-25 | https://www.fedramp.gov |
| OMB-M-24-15 | Modernizing the Federal Risk and Authorization Management Program (FedRAMP) | OMB | M-24-15 (July 2024) | 2026-06-09 | https://www.whitehouse.gov/wp-content/uploads/2024/07/M-24-15-Modernizing-the-Federal-Risk-and-Authorization-Management-Program.pdf |
| OMB-A-130 | Managing Information as a Strategic Resource | OMB | July 28, 2016 | 2026-05-25 | https://www.whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/memoranda/2016/m-16-17.pdf |
| SOC-2-TSC-2017 | Trust Services Criteria | AICPA | 2017 (TSP §100, 2022 revised points of focus) | 2026-05-25 | https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 |
| ISO-27001-2022 | Information security management systems — Requirements | ISO/IEC | 2022 | 2026-05-25 | https://www.iso.org/standard/27001 |
| PCI-DSS-v4.0 | Payment Card Industry Data Security Standard | PCI SSC | v4.0 (Mar 2022) | 2026-05-25 | https://www.pcisecuritystandards.org/document_library |
| HIPAA-Security-Rule | 45 CFR § 164.302–164.318 | HHS | as amended | 2026-05-25 | https://www.hhs.gov/hipaa/for-professionals/security/ |
| NIST-SP-800-66-Rev2 | Implementing the HIPAA Security Rule | NIST | Rev 2 (Feb 2024) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/66/r2/final |
| NIST-CSF-2.0 | Cybersecurity Framework | NIST | 2.0 (Feb 2024) | 2026-05-25 | https://www.nist.gov/cyberframework |
| CMMC-2.0 | Cybersecurity Maturity Model Certification | DoD | 2.0 | 2026-05-25 | https://dodcio.defense.gov/CMMC/ |
| IRS-Pub-1075 | IRS Publication 1075 | IRS | as amended | 2026-06-08 | https://www.irs.gov/pub/irs-pdf/p1075.pdf |

In-body citations use the form `[LABEL §N]` and resolve to this manifest.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| User intent | Load chunk(s) | Industry hint | Use case |
|-------------|---------------|---------------|----------|
| "Categorize this system" / "FIPS 199" / "Step 2" | `chunks/02-categorize.md` | match industry | UC-01 |
| "Select baseline" / "tailor controls" / "Step 3" | `chunks/03-baseline.md` | match industry | UC-01 |
| "Implement controls" / "draft SSP" / "Step 4" | `chunks/04-implement.md` | match industry | UC-01, UC-02 |
| "Assess controls" / "800-53A" / "draft SAR" / "Step 5" | `chunks/05-assess.md` | match industry | UC-02 |
| "Issue ATO" / "ATO with conditions" / "denial" / "POA&M" / "Step 6" | `chunks/06-authorize.md` | match industry | UC-02 |
| "Continuous monitoring" / "ISCM" / "ConMon" / "Step 7" | `chunks/07-monitor.md` | match industry | UC-02 |
| "Map SOC 2 / ISO 27001 / HIPAA / PCI / CSF to 800-53" | `chunks/09-crosswalk.md` | match industry | UC-03 |
| "Full FedRAMP Moderate engagement" | chunks/02, 03, 04, 05, 06 | public-sector | UC-01 |
| "Agency ATO with conditions" | chunks/02, 03, 04, 05, 06 | public-sector | UC-02 |
| "CAIQ" / "SIG Lite" / "VSAQ" / "customer questionnaire" / "FedRAMP reuse" / "questionnaire evidence" | `chunks/08-questionnaire-reuse.md` | match industry | — |
| "High-level question" / "framework overview" | this SKILL.md only | — | — |

**Industries** (load matching file from `industries/`): public-sector, saas-technology, financial-services, healthcare, manufacturing, retail-ecommerce, energy-utilities, other.

**Use cases** (load matching file from `use-cases/`): UC-01 (FedRAMP Moderate), UC-02 (agency ATO), UC-03 (SOC 2 → 800-53).


## 9.1 Cross-Framework Severity Reconciliation

**NIST "Critical" vs ISACA/COSO "Material Weakness":** The NIST RMF severity “Critical” (imminent system compromise; active exploitation; catastrophic impact to C/I/A; treated at the High end of the FedRAMP POA&M risk scale — High findings remediate within 30 days under FedRAMP ConMon) is NOT equivalent to ISACA/COSO/AS 2201 “Material Weakness” (MW). A NIST finding at Moderate severity may correspond to a deficiency in internal control that, in aggregate, constitutes a material weakness under the COSO framework if it affects financial reporting. Conversely, a NIST Critical finding may not be a financial-reporting material weakness if it does not affect the financial statement assertions.

**Reconciliation guidance:** When mapping NIST 800-53 findings to ISACA/COSO deficiency classifications:
- Aggregate NIST findings by financial-reporting impact, not by NIST severity alone.
- A single NIST High or Critical finding on a financial system component may be a Significant Deficiency (SD) or Material Weakness (MW).
- Multiple NIST Low/Moderate findings may aggregate to an SD or MW if they share a common control deficiency that affects financial reporting.
- Document the aggregation rationale in the SAR §5 or a companion memo.

## 12. Operational Quick-Reference

The minimum cycle (always-loaded; no chunk needed for the high-level flow):

1. **Categorize** the system → `chunks/02-categorize.md`. Output: FIPS 199 YAML.
2. **Select** the baseline → `chunks/03-baseline.md`. Output: control selection YAML.
3. **Implement** → `chunks/04-implement.md`. Update SSP §10.
4. **Assess** using 800-53A → `chunks/05-assess.md`. Produce SAR.
5. **Authorize** → `chunks/06-authorize.md`. Produce ATO letter + POA&M.
6. **Monitor** → `chunks/07-monitor.md`. Maintain ISCM strategy.

For non-federal mappings → `chunks/09-crosswalk.md` + `data/crosswalks/`.
