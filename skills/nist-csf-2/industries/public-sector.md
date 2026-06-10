---
industry: public-sector
parent_skill: nist-csf-2
title: "Public sector -- CSF 2.0 alongside FISMA, NIST RMF, OMB A-130, and state RMF variants"
version: 0.1.0
status: active
frameworks: [NIST-CSF-2.0, FISMA, NIST-SP-800-37-Rev2, NIST-SP-800-53-Rev5.1.1, NIST-SP-800-171-Rev3, OMB-A130, BOD-18-01, CISA-CPG, FedRAMP-Moderate, FedRAMP-High, CJIS-Security-Policy-v6.0, IRS-Pub-1075, CA-SAM, TX-DIR, TX-RAMP]
primary_personas: [Agency CIO, Agency CISO, Authorizing Official (AO), State CISO, City CIO, Internal Inspector General]
regulatory_anchors: [44-USC-3551-FISMA, OMB-A130-Circular, BOD-18-01, FedRAMP-Act-2022, CA-SAM-5305, TX-TGC-2054-0593, IRS-Pub-1075]
last_verified: "2026-06-10"
---

## The 6-question public-sector framing

### Q1 -- Why do federal civilian agencies need CSF 2.0 if they already have NIST RMF (800-37)?

RMF (NIST SP 800-37 Rev 2) provides a disciplined 7-step process for authorizing individual information systems to operate: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. Each step produces documentation -- SSP, SAR, POA&M -- that lives at the system level. CSF 2.0 operates at the organizational level: its 6 Functions, 22 Categories, and 106 Subcategories describe cybersecurity outcomes the entire agency should achieve, across all systems, suppliers, and governance layers. The key distinction: an agency can have every system individually authorized under RMF and still have poor organizational cybersecurity posture (no risk appetite statement, no board oversight, no supply chain risk program). CSF 2.0 makes those gaps visible. The two frameworks are complementary, not redundant -- RMF answers "is this system authorized?" while CSF 2.0 answers "as an agency, what cybersecurity outcomes are we achieving, and how rigorously do we govern them?" [NIST-CSF-2.0 Section 1.2; NIST-SP-800-37-Rev2 Section 1.1]

### Q2 -- How does CSF 2.0 GOVERN map to FISMA annual reporting to OMB and CISA?

FISMA (44 USC §3554(c) — agency-head duties; §3553 is OMB/DHS authority) requires each agency to submit an annual report on the agency information security program to OMB, CISA, and relevant congressional committees. The FISMA CIO metrics framework, administered by CISA, evaluates specific control areas on a maturity scale. CSF 2.0 GOVERN function directly overlaps with these FISMA metrics: GV.OC (Organizational Context) maps to the Program Management metric -- the agency documented mission and regulatory inventory. GV.RM (Risk Management Strategy) maps to the Risk Management metric -- risk appetite, ERM integration. GV.SC (Supply Chain) maps to the Supply Chain Risk Management metric -- supplier inventory, third-party monitoring. GV.PO (Policy) maps to Policy and Procedures completeness. GV.OV (Oversight) maps to both Continuous Monitoring and IG Findings metrics. GV.RR (Roles) maps to Senior Leadership Accountability. Table 2 provides the concrete mapping. [FISMA-2014; OMB-A130 Section 5]

### Q3 -- What is the relationship between CSF Tiers (1-4) and the RMF authorization to operate (ATO) lifecycle?

CSF Tiers characterize the rigor of the agency's risk governance and management practices (NIST: not maturity levels). An ATO is a point-in-time authorization decision by an Authorizing Official for a specific system. They operate at fundamentally different levels: a system can have a valid ATO while the agency operates at Tier 1 (Partial -- ad hoc, reactive processes). Conversely, an agency at Tier 4 (Adaptive) still requires individual system ATOs; the Tier describes the maturity of the processes producing those ATOs. The practical intersection: at Tier 3-4, an agency has standardized RMF processes, automated ConMon, a functioning Risk Executive Function, and consistent ATO packages. At Tier 1-2, the agency likely has inconsistent documentation, manual processes, and delayed reauthorizations. The GOVERN Tier specifically acts as a practical ceiling -- an agency at Tier 1 in GOVERN cannot credibly operate at Tier 3 in PROTECT. [NIST-CSF-2.0 Section 3.1; NIST-SP-800-37-Rev2 Section 3.16]

### Q4 -- How do state and local governments map to federal frameworks (CA SAM, TX DIR, TX-RAMP)?

State and local governments are not directly bound by FISMA, which applies to federal agencies. However, many states have adopted RMF/CSF-based frameworks through statute, executive order, or administrative code. California SAM Section 5305 adopts 800-53 with state-specific overlays under CDT authority. Texas TAC 202 and DIR SCSC reference 800-53 with TX modifications, including TX-RAMP (SB 475, 2021) which mirrors FedRAMP for state cloud procurement. New York ITS publishes the Risk and Regulatory Framework incorporating both 800-53 and CSF. Florida Statutes Section 282.318 explicitly references NIST CSF in law. Each state designates its own Authorizing Official (typically the State CISO or CIO), sets its own assessment cadence (annual or biennial), and relies on the State Auditor or state IG for audit. Table 4 provides the full mapping. (Verify CA SAM 5305 current edition, NY RRF, and FL §282.318 against current state publications; TX statutes verified 2026-06-10: §2054.0593 = TX-RAMP, §2054.515 = biennial assessment.)

### Q5 -- Where does CSF 2.0 supplement CISA Cross-Sector Cybersecurity Performance Goals (CPGs)?

CISA published **CPG 2.0 on December 11, 2025** (superseding v1.0.1 of March 2023, which had 38 goals): roughly **34 goals with IDs like 1.A, 2.B, organized under the six CSF 2.0 Functions** -- Govern (1.x), Identify (2.x), Protect (3.x), Detect (4.x), Respond (5.x), Recover (6.x) (verified at cisa.gov, 2026-06-10). The CPGs are a minimum baseline for critical infrastructure -- intentionally much shorter than the 106 CSF Subcategories so small and medium entities can realistically implement them. CSF 2.0 supplements CPGs with the full outcome catalog: CPGs tell you the highest-impact practices to do first; CSF 2.0 tells you what comes next across all 22 Categories. Federal civilian agencies should already meet the CPGs through their 800-53 implementation (and are required to use the CSF itself per EO 13800); for state and local governments, CPGs are a practical on-ramp. Table 3 maps CPG 2.0's function groups to CSF. [CISA-CPG]

### Q6 -- What is the difference between FedRAMP authorized cloud services and a CSF 2.0 Profile for the agency that uses them?

FedRAMP authorization is a specific, system-level 800-53 control assessment for a cloud service offering (CSO), conducted by a third-party assessment organization (3PAO) and approved under the FedRAMP Board governance model (the JAB was replaced in 2024; one "FedRAMP Authorized" designation). A CSF 2.0 Profile is the agency self-assessment of its cybersecurity outcomes across all 106 Subcategories -- including GOVERN (policy, risk appetite, supply chain, oversight), DETECT (monitoring), RESPOND (IR), and RECOVER -- not just the controls a cloud provider implements. The FedRAMP-authorized cloud service feeds into the agency Profile as evidence for specific Subcategories (GV.SC for supply chain risk, PR.AA for identity management, PR.DS for data security), but covers only a subset. An agency Profile also covers on-premises systems, policy governance, workforce training, incident response maturity, and recovery planning. The FedRAMP authorization is evidence for the Profile; the Profile is the agency posture statement. [FedRAMP-Authorization-Act-2022; NIST-CSF-2.0 Section 3.2]

## Table 1 -- CSF 2.0 Function to RMF Step mapping

The 6 CSF Functions map to the 7 RMF Steps (Prepare=1, Categorize=2, Select=3, Implement=4, Assess=5, Authorize=6, Monitor=7 per NIST SP 800-37 Rev 2). This mapping is interpretive: CSF describes outcomes; RMF describes process steps. Source: NIST CSRC about-rmf page, retrieved 2026-06-07. [NIST-CSF-2.0 Section 2; NIST-SP-800-37-Rev2 Section 2.4]

| CSF Function | Prepare (S1) | Categorize (S2) | Select (S3) | Implement (S4) | Assess (S5) | Authorize (S6) | Monitor (S7) |
|---|---|---|---|---|---|---|---|
| **GOVERN (GV)** | Heavy -- GV.OC, GV.RM, GV.RR, GV.PO set during Prepare | Light -- GV.OC informs categorization scope | Light -- GV.RM sets risk appetite for control selection | Moderate -- GV.PO policies implemented | Light -- GV.OV feeds assessment criteria | Moderate -- GV.OV informs authorization decision | Heavy -- GV.OV continuous review; GV.SC supply chain monitoring |
| **IDENTIFY (ID)** | Moderate -- ID.AM inventory begins | Heavy -- ID.RA risk assessment informs FIPS 199 categorization | Light -- ID.IM improvement planning | Light -- ID.AM inventory updated | Light -- ID.RA gaps identified | Light | Moderate -- ID.AM inventory maintained; ID.RA re-assessed |
| **PROTECT (PR)** | Light -- PR.AT training planning | Light | Heavy -- PR controls map to selected 800-53 families | Heavy -- PR controls deployed and documented | Heavy -- PR controls assessed by control assessor | Moderate -- PR implementation status informs ATO | Heavy -- PR controls continuously evaluated |
| **DETECT (DE)** | Light -- DE.CM monitoring architecture | | | Moderate -- DE monitoring tools deployed | Moderate -- DE.AE analysis tested | Light | Heavy -- DE.CM continuous monitoring is the backbone of Step 7 |
| **RESPOND (RS)** | Moderate -- RS.MA IR plan developed | | | Moderate -- RS procedures implemented | Moderate -- RS plan tested | Light -- RS capability considered in ATO | Moderate -- RS plans updated from monitoring data |
| **RECOVER (RC)** | Moderate -- RC.RP contingency plan | | | Moderate -- RC recovery procedures | Moderate -- RC plan tested | Light -- RC capability considered in ATO | Moderate -- RC plans exercised and updated |

Key takeaway: GOVERN maps most heavily to Prepare and Monitor -- the bookend steps of RMF. IDENTIFY maps most heavily to Categorize. PROTECT and DETECT map most heavily to Select/Implement/Assess and Monitor. RESPOND and RECOVER are spread across multiple steps with no single dominant cell.

## Table 2 -- CSF 2.0 GOVERN to FISMA CIO metrics

FISMA CIO metrics are reported annually to OMB and CISA per 44 USC §3554(c). Each GOVERN Category maps to FISMA metric domains. This mapping is interpretive -- the FISMA CIO metrics framework evolves annually under CISA management. [FISMA-2014; OMB-A130 Section 5] [VERIFY: current FY FISMA CIO metrics from CISA]

| GOVERN Category | FISMA CIO metric domain | How the Category feeds the metric |
|---|---|---|
| **GV.OC** | Program Management | Documented mission, stakeholder inventory, and regulatory mapping underpin the program management score |
| **GV.RM** | Risk Management | Risk appetite statement and ERM integration feed the risk metric |
| **GV.SC** | Supply Chain Risk Management | Supplier inventory, contract requirements, and third-party monitoring feed the SCRM metric; GV.SC-05 and GV.SC-07 are the most assessable |
| **GV.PO** | Policy and Procedures | Policy existence, currency, and communication underpin policy completeness score |
| **GV.OV** | Continuous Monitoring / IG Findings | Performance review cadence, audit findings status, and strategy adjustment feed both ConMon and IG findings metrics |
| **GV.RR** | Senior Leadership Accountability | CIO/CISO designation, workforce allocation, and accountability documentation feed the leadership metric |

## Table 3 -- CSF 2.0 to CISA CPG 2.0 mapping (function-group level)

CPG 2.0 (Dec 11, 2025) organizes ~34 goals under the six CSF 2.0 Functions with IDs of the form `<function-number>.<letter>` (e.g., 1.A "Establish Cybersecurity Responsibilities"). The mapping below is at the function-group level -- map individual goals to Subcategories from the published CPG checklist, not from this table. [CISA-CPG]

| CPG 2.0 group | CSF 2.0 Function | Representative CSF Subcategories | Notes |
|---|---|---|---|
| Govern goals (1.x) | GOVERN (GV) | GV.RR-01, GV.PO-01, GV.SC-01, GV.OV-01 | Responsibilities, policy, supply chain, oversight |
| Identify goals (2.x) | IDENTIFY (ID) | ID.AM-01..05, ID.RA-01 | Asset inventories, vulnerability identification |
| Protect goals (3.x) | PROTECT (PR) | PR.AA-01/-03/-05, PR.DS-01/-02, PR.AT-01/-02, PR.PS-01/-02 | IAM/MFA/least privilege, data protection, training (PR.AT has only -01 and -02 in CSF 2.0), platform security |
| Detect goals (4.x) | DETECT (DE) | DE.CM-01, DE.AE-02 | Monitoring, adverse-event analysis |
| Respond goals (5.x) | RESPOND (RS) | RS.MA-01..03, RS.AN-03, RS.MI-01/-02, RS.CO-02 | IR plan, analysis, mitigation, notification |
| Recover goals (6.x) | RECOVER (RC) | RC.RP-01..03 | Recovery execution and communication |

For federal civilian agencies: the CPGs should already be covered by the agency 800-53 implementation. For state/local governments: CPGs are a practical on-ramp to full CSF 2.0.

## Table 4 -- State RMF / CSF variants

States have adopted frameworks adapting the federal RMF/CSF model. Variants share the core NIST catalog but differ in authorization authority, assessment cadence, and compliance requirements. [VERIFY: CA SAM 5300-series current URL; TX DIR SCSC current edition; NY RRF; FL Section 282.318]

| State / Framework | Relationship to CSF 2.0 | Control baseline | Key difference from federal |
|---|---|---|---|
| **CA SAM 5305** (California State Administrative Manual) | CA SAM Section 5300-series adopts 800-53 with state overlays. CDT is the oversight authority. CSF 2.0 Profiles can map to SAM criteria. | 800-53 Rev 5 with CA overlays | State agencies under CDT authority; separate from federal FISMA reporting |
| **TX DIR / TAC 202** (Texas Dept. of Information Resources) | TAC Ch 202 references 800-53 for state agencies. DIR publishes Security Control Standards Catalog (SCSC). | 800-53 with TX modifications | TX Gov Code §2054.515 mandates the biennial information security assessment (§2054.0593 is the TX-RAMP cloud statute); DIR has direct oversight |
| **TX-RAMP** (Texas Risk and Authorization Mgmt Program) | Mirrors FedRAMP for cloud services used by TX agencies. Mandated by SB 475 (87th TX Legislature, 2021). | 800-53 with TX overlays; FedRAMP-equivalent | TX DIR certifies cloud services at Level 1/Level 2; mandatory for state procurement |
| **NY RRF** (NY State Risk and Regulatory Framework) | NY ITS publishes RRF incorporating 800-53 and CSF. NY DFS Part 500 (financial services) is separate but maps to CSF 2.0. | 800-53 Rev 5; DFS Part 500 for financial sector | Dual-track: RRF for agencies; DFS Part 500 for financial entities |
| **FL Cybersecurity Standards** (Florida Digital Services) | FL Statutes Section 282.318 mandates NIST CSF-based standards for state agencies. | 800-53 / CSF 2.0 hybrid | FL explicitly references NIST CSF in statute, making CSF 2.0 adoption a statutory requirement |
| **CJIS Security Policy v6.0** (multi-state) | FBI CJIS applies to any state/local agency accessing CJIS. Policy-based standard (not RMF); maps to 800-53. Can be expressed as CSF 2.0 Profile. | 800-53 Moderate/Low with CJIS overlays | Federally mandated overlay for law enforcement systems -- most common cross-state control baseline |

Approximately 30 states have some form of cybersecurity regulation. Verify the current state publication before mapping to CSF 2.0.

## What is unique to public sector

The public sector operates under a fundamentally different risk management regime than any other sector: it is ATO-driven, binding-directive-governed, and statutorily audited. Three dimensions make CSF 2.0 adoption distinct from private-sector adoption.

The ATO-driven reality. Federal civilian agencies do not "complete" CSF 2.0 -- they authorize systems per RMF Step 6 (ATOs traditionally run up to 3 years, or operate as ongoing authorization under continuous monitoring; the ANNUAL cycle is FISMA reporting, not the ATO), and CSF 2.0 Profiles describe the agency cybersecurity posture across all systems, including the governance processes that produce those ATOs. (EO 13800 requires agency heads to use the CSF to manage agency cyber risk; FISMA requires the RMF/800-53 machinery — both apply.) The practical pattern: each major system holds a valid ATO with a System Security Plan (SSP), Security Assessment Report (SAR), and Plan of Action and Milestones (POA&M). The agency CSF 2.0 Profile aggregates these system-level artifacts into an enterprise-level posture statement covering all 106 Subcategories. The most important intersection is Continuous Monitoring (RMF Step 7): the ConMon program directly feeds the DE.CM (Continuous Monitoring), GV.OV (Oversight), and GV.SC (Supply Chain) Subcategory scores. An agency with strong ConMon -- automated vulnerability scans, monthly POA&M review, significant-change tracking, annual control assessments -- will score well on CSF 2.0 Profile assessments. An agency doing annual point-in-time ATOs without continuous monitoring will score poorly across DETECT and GOVERN. The CSF 2.0 Profile makes the distinction between "authorized" and "mature" visible in a way the ATO alone cannot.

The BOD 18-01 binding operational directive reality. CISA Binding Operational Directive 18-01 ("Enhance Email and Web Security," October 2017) is a compulsory direction issued to federal civilian Executive Branch agencies under FISMA authority (44 USC Section 3553). Unlike CSF 2.0 voluntary Subcategories, BOD 18-01 mandates specific technical configurations with explicit deadlines: DMARC at p=reject within one year, STARTTLS within 90 days, HTTPS-only with HSTS within 120 days, disabling SSLv2/SSLv3, RC4, and 3DES ciphers. These requirements map directly to CSF 2.0 Subcategories -- PR.PS-01 (configuration management), PR.DS-02 (data-in-transit protection), PR.IR-01 (network resilience) -- but BOD 18-01 is required, not advisory. For an agency building a CSF 2.0 Profile, BOD 18-01 compliance is a floor, not a ceiling: BOD 18-01 covers email and web security for internet-facing systems; CSF 2.0 covers the full spectrum of cybersecurity outcomes. Critically, BOD 18-01 does NOT apply to the Department of Defense, Intelligence Community, or statutorily defined National Security Systems (per Section 3553(d)-(e)). BOD 18-01 (2017) is the email/web example only — the operative directives for current work include BOD 22-01 (Known Exploited Vulnerabilities) and BOD 23-01 (asset visibility); verify the applicable BODs for the agency in question.

The state and local landscape. As of 2026, approximately 30 states have enacted some form of cybersecurity regulation, statute, or administrative standard for state agencies. The coverage is uneven: California, Texas, New York, and Florida have comprehensive RMF/CSF adoption with state-specific overlays; approximately 15-20 states reference NIST 800-53 or CSF without a full RMF program; and a handful are in early stages of adopting any formal standard. Municipalities typically follow their state framework or adopt CSF 2.0 / CIS Controls v8 as a maturity benchmark. Several cross-state control baselines apply regardless of a state own framework: CJIS Security Policy (v6.0, Dec 27, 2024 — v5.9 is superseded; audits may still run against v5.9.x during transition) (for law enforcement agencies accessing FBI CJIS systems), IRS Publication 1075 (for agencies receiving Federal Tax Information), and HIPAA Security Rule (for state agencies functioning as covered entities). Key structural differences from the federal pattern: states predominantly align to the NIST CSF (per NASCIO surveys) rather than running full federal-style RMF programs; security leadership is the State CISO/CIO; the assessment cadence varies by state (TX biennial per TGC §2054.515; others annual); the audit authority is the State Auditor or state-level Inspector General, with reporting to the state CIO/CISO and legislature, not OMB/CISA. SLTT support structures the federal model lacks: **MS-ISAC** membership for threat intel and incident support, **StateRAMP** for cloud authorization, **CIS Controls** (especially IG1) as the practical small-agency baseline, and NASCIO for peer benchmarking. For a CSF 2.0 engagement with a state or local government, identify the applicable statute, determine which frameworks the state has adopted and with what overlays, and confirm the assessment cadence. Do not assume the federal RMF process applies without modification.

## Cross-references

- `chunks/01-functions-categories.md` -- The 6 Functions, 22 Categories, 106 Subcategories structural reference. Table 1 above is the industry-specific layer.
- `chunks/05-govern-function.md` -- Deep dive GOVERN. GV.SC maps to FedRAMP/TX-RAMP providers; GV.OV maps to FISMA reporting; GV.RR maps to CIO/CISO/AO accountability.
- `chunks/08-informative-references-crosswalk.md` -- CSF to 800-53 Rev 5.1.1 mappings. The bridge between CSF 2.0 Profiles (outcomes) and RMF system ATOs (controls).
- `nist-800-53-rmf` -- The foundational skill. RMF = process for authorizing systems; CSF 2.0 = framework for assessing organizational outcomes. The public-sector view sits at the intersection.
- `audit-workpapers` -- For IG audit findings. IG audits evaluate FISMA compliance; CSF 2.0 Profiles structure findings by Function/Category and track Subcategory remediation.

## Anti-hallucination

- **RMF Step numbers**: Prepare=Step 1, Categorize=Step 2, Select=Step 3, Implement=Step 4, Assess=Step 5, Authorize=Step 6, Monitor=Step 7 (per NIST SP 800-37 Rev 2, December 2018). Confirmed on NIST CSRC RMF project page at csrc.nist.gov/projects/risk-management/about-rmf, retrieved 2026-06-07.

- **FedRAMP authorizations have NO statutory expiration clock**: the FedRAMP Authorization Act (PL 117-263, codified at 44 USC 3607-3616) sets no authorization duration -- authorizations are sustained through continuous monitoring (with annual assessments). An earlier version of this file invented a "12-month ATO" rule; there is none. Also note the JAB was replaced by the **FedRAMP Board** in 2024, with a single "FedRAMP Authorized" designation. Verify current guidance at fedramp.gov.

- **State RMF variants are NOT identical to federal RMF**: CA SAM 5305, TX DIR TAC 202, TX-RAMP, NY RRF, and FL Cybersecurity Standards have state-specific control baselines that may differ from FedRAMP Moderate or the federal 800-53 Moderate baseline. Assessment cadences vary: TX biennial (TGC §2054.515 — §2054.0593 is the TX-RAMP cloud statute), CA annual, FL annual. AO designation differs per state. Verify against the current state publication before mapping.

- **BOD 18-01 scope**: Applies to all federal civilian Executive Branch agencies under FISMA (44 USC Section 3553). Not applicable to DoD, IC, or National Security Systems (44 USC Section 3553(d)-(e)). Subsequent BODs (18-02, 19-01, etc.) have different scopes.

- **CISA CPG 2.0** (Dec 11, 2025): ~34 goals with IDs 1.A-6.A grouped under the six CSF 2.0 Functions (v1.0.1 of March 2023 had 38 goals; the title has never contained "ICS"). Not exhaustive -- CSF 2.0 has 106 Subcategories. CPGs are a minimum baseline for critical infrastructure; federal agencies should already meet them through 800-53 implementation.

- **800-53 Rev 5.1.1 is current authoritative**: As of June 2026, NIST SP 800-53 Rev 5.1.1 maps to CSF 2.0 in the Informative References spreadsheet. Rev 5.2.0 is published as draft. Verify the agency RMF program version before producing crosswalks.

- **CJIS Security Policy is policy-based, not RMF-based** (current version: v6.0, issued Dec 27, 2024; verified at le.fbi.gov 2026-06-10 — transition audits may still reference v5.9.x): CJIS does not use the RMF 7-step process or issue ATOs. CJIS requirements map to 800-53 controls and can be expressed as a CSF 2.0 Organizational Profile.

- **IRS Pub 1075 is a safeguarding standard, not an RMF framework**: IRS Pub 1075 applies to agencies receiving FTI. It references 800-53 with IRS-specific requirements. CSF 2.0 Profiles for tax agencies should address Pub 1075 under GV.OC, PR.DS, and PR.AA. [VERIFY: IRS Pub 1075 current edition]
