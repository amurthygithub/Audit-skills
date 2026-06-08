---
industry: financial-services
parent_skill: nist-csf-2
title: "Financial services — CSF 2.0 alongside OCC, FFIEC, SOX, and NY DFS"
version: 0.1.0
status: active
frameworks: [NIST-CSF-2.0, FFIEC-CAT, OCC-Heightened-Standards, SOX-404, NY-DFS-500, PCI-DSS-4.0.1, GLBA-Safeguards, NIST-SP-800-53-Rev5.1.1]
primary_personas: [CRO, CISO, Head of Operational Risk, Internal Audit Partner]
regulatory_anchors: [OCC-2014-13, FFIEC-CAT-2017, 12-CFR-30, NY-DFS-23-NYCRR-500]
last_verified: "2026-06-07"
---

## Summary

A regulated bank or financial-services firm operates under examiners from the OCC, FDIC, Federal Reserve, state banking departments, and (if in New York) the DFS. CSF 2.0 is not a replacement for this regulatory stack — it is the common-language bridge that lets the board, the CRO, the CISO, and the examiners talk about cyber maturity in the same terms. This industry view shows how CSF 2.0 fits into a financial-services engagement that is already saturated with FFIEC CAT, OCC Heightened Standards, SOX 404 ITGCs, NY DFS Part 500, and PCI DSS.

## The 6-question banker framing

### Q1: Why do we need CSF 2.0 if we already have FFIEC CAT?

FFIEC CAT (2017) is a supervisory examination tool — it produces a maturity score that examiners use to calibrate examination scope. CSF 2.0 is a voluntary, outcome-based framework that produces an Organizational Profile the board can use for strategic planning, resource allocation, and quarterly risk-committee reporting. FFIEC CAT tells you what the examiner thinks; CSF 2.0 tells you where you want to go. A bank can score "Advanced" on FFIEC CAT Cybersecurity Controls but be Tier 1 (Partial) on CSF 2.0 GOVERN because the governance maturity scale is different. The two frameworks are complementary, not redundant. Source: FFIEC CAT 2017 [FFIEC-CAT] and NIST CSF 2.0 CSWP 29 [NIST-CSF-2.0].

### Q2: How does CSF 2.0 GOVERN function map to the board cyber risk governance that OCC Heightened Standards expects?

OCC Heightened Standards (12 CFR 30 Appendix D, effective September 2014) require a formal risk governance framework with eight core expectations: (1) board oversight, (2) risk appetite framework, (3) risk management program, (4) three lines of defense, (5) risk reporting, (6) strategic planning, (7) talent management, and (8) compensation alignment. CSF 2.0's GOVERN Categories map to these expectations with a governance-first lens. GV.OV (Oversight) maps to board oversight and risk reporting; GV.RM (Risk Management Strategy) maps to risk appetite framework; GV.RR maps to three lines of defense and talent management; GV.PO maps to risk management program; GV.OC maps to strategic planning. See Table 2 for the full mapping. Source: 12 CFR 30 Appendix D [OCC-Heightened-Standards] and NIST CSF 2.0 Section 2.2 [NIST-CSF-2.0].

### Q3: What is the relationship between the CSF Tiers (1-4) and FFIEC CAT's maturity levels?

CSF 2.0 uses four Tiers: 1 (Partial), 2 (Risk Informed), 3 (Repeatable), 4 (Adaptive) [NIST-CSF-2.0 Section 3.1]. FFIEC CAT 2017 uses five maturity levels per domain: Baseline, Evolving, Intermediate, Advanced, Innovative. These serve different purposes: CSF Tiers describe organizational maturity (how well the org integrates cyber risk into enterprise risk); FFIEC CAT levels describe supervisory assessment of specific domains. An organization can score Advanced on FFIEC CAT's Cybersecurity Controls domain while sitting at CSF Tier 2 (Risk Informed) overall because CSF Tiers require org-wide integration that FFIEC CAT domain scoring does not. Interpretive — no official crosswalk exists between the two maturity scales. Source: FFIEC CAT 2017 [FFIEC-CAT] and NIST CSF 2.0 Section 3.1 [NIST-CSF-2.0].

### Q4: How do CSF 2.0 Subcategories correlate to NY DFS 500?

NY DFS Part 500 (23 NYCRR 500, amended November 2023) contains 17 sections that prescribe specific cybersecurity controls for DFS-regulated entities. CSF 2.0 Subcategories can serve as the evidence framework for demonstrating compliance — a Current Profile scored at "Largely" or "Fully" across the applicable Subcategories provides a defensible map to the DFS examiner. See Table 3 for a representative crosswalk of 20 Subcategories. Source: 23 NYCRR Part 500 [NY-DFS-500] and NIST CSF 2.0 Section 2.3 [NIST-CSF-2.0].

### Q5: Where does CSF 2.0 supplement SOX 404 ITGCs?

SOX 404 ITGCs cover four areas: Access to Programs and Data, Program Changes, Computer Operations, and Program Development. CSF 2.0 supplements ITGCs in three ways: (1) It adds a governance layer (GOVERN) that SOX ITGCs do not address — the board's role in cyber risk appetite, third-party governance, and oversight; (2) It adds response and recovery outcomes (RESPOND, RECOVER) that SOX ITGCs do not measure; (3) It adds continuous monitoring (DE.CM) as a first-class set of outcomes. Where CSF overlaps with ITGCs (Access in PR.AA, Change Management in PR.PS, Operations in DE.CM), the overlap is "supplementary evidence, not duplicative testing." See Table 4. Source: PCAOB AS 2201 and NIST CSF 2.0 Section 2.3 [NIST-CSF-2.0].

### Q6: What is the cheapest path from a 2024 FFIEC CAT baseline to a 2026 CSF 2.0 Profile?

The lowest-cost path is a "crosswalk-first, assess-second" approach: (1) Map the FFIEC CAT 2017 domain scores to CSF 2.0 Functions using Table 1 (one-time exercise, approximately 2 days); (2) Identify the 6-10 Subcategories where FFIEC CAT's Inherent Risk Profile is "High" but the CSF Subcategory is unassessed — these are the gaps; (3) Score only those Subcategories in a Current Profile (do not attempt a full 106-Subcategory assessment); (4) Publish the partial Current Profile as a "FFIEC CAT to CSF 2.0 gap bridge." Total effort: 5-7 days for a mid-size bank. Use `chunks/03-current-profile.md` for the scoring template and `chunks/04-target-profile-and-gap.md` for the gap methodology.

## Table 1: CSF 2.0 Function to FFIEC CAT Domain mapping

| CSF 2.0 Function | FFIEC CAT Domain | Relationship | Source |
|------------------|------------------|-------------|--------|
| GOVERN (GV) | Cyber Risk Management and Oversight | GOVERN covers board governance, risk appetite, and policy — the supervisory lens that FFIEC CAT Domain 1 measures. GV.SC aligns with External Dependency Management. | NIST-CSF-2.0 Section 2.2; FFIEC CAT 2017 Domain 1 |
| IDENTIFY (ID) | Threat Intelligence and Collaboration; Cyber Risk Management and Oversight | Asset identification (ID.AM) and risk assessment (ID.RA) support FFIEC CAT's inherent risk profiling and threat intelligence gathering. | NIST-CSF-2.0 Section 2.2; FFIEC CAT 2017 Domains 1-2 |
| PROTECT (PR) | Cybersecurity Controls | Direct alignment — FFIEC CAT Domain 3 (Cybersecurity Controls) maps to PROTECT Categories (PR.AA access, PR.DS data, PR.PS platform, PR.IR resilience). | NIST-CSF-2.0 Section 2.2; FFIEC CAT 2017 Domain 3 |
| DETECT (DE) | Cybersecurity Controls (continuous monitoring subset) | DE.CM maps to FFIEC CAT's controls around detection, monitoring, and logging within Domain 3. | NIST-CSF-2.0 Section 2.2; FFIEC CAT 2017 Domain 3 |
| RESPOND (RS) | Cyber Incident Management and Resilience | RS Categories (Management, Analysis, Mitigation, Reporting) map to FFIEC CAT Domain 5's incident response and reporting expectations. | NIST-CSF-2.0 Section 2.2; FFIEC CAT 2017 Domain 5 |
| RECOVER (RC) | Cyber Incident Management and Resilience | RC.RP (Recovery Planning) and RC.CO (Restoration of Assets) map to FFIEC CAT Domain 5's recovery and resilience testing. | NIST-CSF-2.0 Section 2.2; FFIEC CAT 2017 Domain 5 |

Note: FFIEC CAT Domain 4 (External Dependency Management) spans GOVERN (GV.SC) and IDENTIFY (ID.AM, ID.RA). The mapping is interpretive — FFIEC CAT and CSF 2.0 use different decomposition logic.

## Table 2: CSF 2.0 GOVERN to OCC Heightened Standards (12 CFR 30 Appendix D)

| CSF 2.0 GOVERN Category | OCC Heightened Standards Expectation | Relationship | Source |
|--------------------------|--------------------------------------|-------------|--------|
| GV.OC (Organizational Context) | Strategic Planning | GV.OC requires understanding mission, objectives, and dependencies — the foundation for the strategic planning expectation. | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.A [OCC-Heightened-Standards] |
| GV.RM (Risk Management Strategy) | Risk Appetite Framework | GV.RM-02 (risk appetite defined) and GV.RM-03 (ERM integration) directly address the OCC requirement for a formal risk appetite statement approved by the board. | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.B |
| GV.RM (Risk Management Strategy) | Risk Management Program | GV.RM-01 through GV.RM-04 provide the strategic risk direction that the OCC expects from a comprehensive risk management program. | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.C |
| GV.RR (Roles, Responsibilities, Authorities) | Three Lines of Defense | GV.RR Subcategories define roles and accountability across the first line (business units), second line (risk management), and third line (internal audit). | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.D |
| GV.RR (Roles, Responsibilities, Authorities) | Talent Management | GV.RR-04 (personnel resourced and trained) maps to OCC's expectation for qualified risk management personnel. | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.F |
| GV.OV (Oversight) | Board Oversight | GV.OV-01 through GV.OV-03 address board review, strategic adjustment, and performance measurement — the core of the OCC board oversight expectation. | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.A |
| GV.OV (Oversight) | Risk Reporting | GV.OV-02 (performance reviewed and strategy adjusted) requires the reporting cadence that OCC expects from management to the board. | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.E |
| GV.PO (Policy) | Risk Management Program | GV.PO-01 and GV.PO-02 require formal, board-approved cybersecurity policy — central to the OCC's documented risk management program expectation. | NIST-CSF-2.0 Section 2.2; 12 CFR 30 App D Section III.C |
| GV.SC (Supply Chain Risk) | Risk Management Program (third-party extension) | GV.SC extends the OCC risk management program expectation to third-party and supply-chain cyber risk. | NIST-CSF-2.0 Section 2.2; OCC Bulletin 2023-17 [VERIFY: exact bulletin number for interagency TPRM guidance] |

Note: OCC Heightened Standards apply to banks over $50B in assets under 12 CFR 30 Appendix D. Mid-size and community banks follow 12 CFR 30 Appendix A (Safety and Soundness Standards), which is less prescriptive. The mapping above assumes a large-bank context.

## Table 3: CSF 2.0 Subcategory to NY DFS Part 500 mapping (representative)

| CSF 2.0 Subcategory | NY DFS 500 Section | Mapping Rationale | Source |
|---------------------|--------------------|-------------------|--------|
| GV.OC-03 (legal/regulatory requirements understood) | Section 500.00-500.01 | Foundational — the entity must identify DFS as the relevant regulatory body. | NIST-CSF-2.0; NY-DFS-500 |
| GV.RR-01 (roles and responsibilities established) | Section 500.04(a) | Requires a CISO designation with defined responsibilities. | NIST-CSF-2.0; NY-DFS-500 Section 500.04(a) |
| GV.RR-03 (communication of roles) | Section 500.04(b) | Requires CISO to report in writing at least annually to the board or senior governing body. | NIST-CSF-2.0; NY-DFS-500 Section 500.04(b) |
| GV.PO-01 (policy established) | Section 500.03 | Requires a written cybersecurity policy approved by the board or senior governing body. | NIST-CSF-2.0; NY-DFS-500 Section 500.03 |
| GV.PO-02 (policy reviewed and maintained) | Section 500.03 | Requires policy review at least annually. | NIST-CSF-2.0; NY-DFS-500 Section 500.03 |
| GV.OV-01 (performance reviewed) | Section 500.04(b) | CISO annual reporting requirement drives performance review. | NIST-CSF-2.0; NY-DFS-500 Section 500.04(b) |
| GV.SC-03 (supplier risk managed) | Section 500.11 | Requires written third-party service provider security policy and due diligence. | NIST-CSF-2.0; NY-DFS-500 Section 500.11 |
| GV.RM-02 (risk appetite defined) | Section 500.09 | Requires a written risk assessment that informs the cybersecurity program. | NIST-CSF-2.0; NY-DFS-500 Section 500.09 |
| ID.AM-01 (assets inventoried) | Section 500.09 | Risk assessment requires understanding of information systems and nonpublic information. | NIST-CSF-2.0; NY-DFS-500 Section 500.09 |
| PR.AA-01 (identities and credentials managed) | Section 500.07 | Requires access privilege management based on least privilege. | NIST-CSF-2.0; NY-DFS-500 Section 500.07 |
| PR.AA-05 (network integrity protected) | Section 500.12 | Requires Multi-Factor Authentication for access to information systems. | NIST-CSF-2.0; NY-DFS-500 Section 500.12 |
| PR.AT-01 (personnel trained) | Section 500.14 | Requires cybersecurity awareness training for all personnel. | NIST-CSF-2.0; NY-DFS-500 Section 500.14 |
| PR.DS-01 (data at rest protected) | Section 500.15 | Requires encryption of nonpublic information at rest and in transit. | NIST-CSF-2.0; NY-DFS-500 Section 500.15 |
| PR.PS-02 (software maintained) | Section 500.08 | Requires written application security procedures, guidelines, and standards. | NIST-CSF-2.0; NY-DFS-500 Section 500.08 |
| PR.IR-01 (incident response plan) | Section 500.16 | Requires a written incident response plan. | NIST-CSF-2.0; NY-DFS-500 Section 500.16 |
| DE.CM-01 (networks monitored) | Section 500.14(b) / 500.09 | Risk assessment and monitoring requirements imply continuous monitoring. | NIST-CSF-2.0; NY-DFS-500 Section 500.14(b) |
| RS.MA-03 (incidents reported) | Section 500.17(a) | Requires notification to DFS within 72 hours of determining a cybersecurity incident has occurred. | NIST-CSF-2.0; NY-DFS-500 Section 500.17(a) |
| RS.AN-01 (incidents analyzed) | Section 500.16 | Incident response plan must include root cause analysis and investigation procedures. | NIST-CSF-2.0; NY-DFS-500 Section 500.16 |
| RC.RP-01 (recovery plan executed) | Section 500.16 | Business continuity and disaster recovery plan requirements within the incident response plan. | NIST-CSF-2.0; NY-DFS-500 Section 500.16 |
| PR.AA-02 (physical access managed) | Section 500.03 | Cybersecurity policy must address access controls including physical access. | NIST-CSF-2.0; NY-DFS-500 Section 500.03 |

Note: This table is representative, not exhaustive. DFS Part 500 is a prescriptive regulation; CSF 2.0 is an outcome-based framework. Some DFS requirements (e.g., Section 500.17(a) 72-hour notification) are specific regulatory mandates with no exact CSF 2.0 match. No authoritative crosswalk from CSF 2.0 to NY DFS Part 500 has been published by DFS or NIST; mappings are interpretive. [VERIFY: Confirm exact NY DFS 500 section numbers for the amended (November 2023) version against 23 NYCRR 500.]

## Table 4: CSF 2.0 to SOX 404 ITGC overlap

| CSF 2.0 Subcategory | SOX 404 ITGC Area | Overlap | Type |
|----------------------|-------------------|---------|------|
| PR.AA-01 (identities and credentials managed) | Access to Programs and Data | User access provisioning, recertification, and privileged access management. | Overlapping — test once, use for both |
| PR.AA-04 (access permissions managed) | Access to Programs and Data | Segregation of duties and least privilege for financial systems. | Overlapping |
| PR.PS-01 (configuration baselines) | Program Changes | Baseline configurations and change control over financial reporting systems. | Overlapping |
| PR.PS-02 (software maintained) | Program Changes | Patch management and system updates for in-scope applications. | Overlapping |
| PR.DS-01 (data at rest protected) | Computer Operations | Backup and recovery of financial data — shared evidence. | Overlapping |
| DE.CM-01 (networks monitored) | Computer Operations | Monitoring and logging of financial system activity. | Supplementary — CSF adds threat detection beyond ITGC ops monitoring |
| PR.IR-01 (continuity plans) | Computer Operations | Disaster recovery and business continuity for financial systems. | Overlapping |
| RC.RP-01 (recovery plan executed) | Computer Operations | Recovery testing for financial applications. | Overlapping |
| ID.AM-01 (assets inventoried) | Program Development | Asset inventory supports scoping of ITGC-covered systems. | Supplementary — CSF adds rigor to scoping |
| GV.OV-01 (performance reviewed) | (none) | Governance oversight of ITGC effectiveness. | Supplementary only — no SOX ITGC equivalent |
| GV.SC-03 (supplier risk managed) | (supplemental to Access) | Third-party access to financial systems. | Supplementary — CSF extends ITGC to the supply chain |

Callout: SOX 404 ITGCs and CSF 2.0 Subcategories overlap in operational controls (access, change, operations) but are not interchangeable. SOX ITGCs are tested for financial reporting risk (is there a risk of material misstatement?). CSF 2.0 Subcategories are assessed for cybersecurity risk (is the org resilient against threats?). An organization can have clean SOX ITGCs with no material weaknesses and a weak CSF PROTECT Profile — or vice versa. The overlap columns in this table represent "test once, evidence shared" opportunities, not framework equivalence. Source: PCAOB AS 2201 [SOX-404] and NIST CSF 2.0 Section 2.3 [NIST-CSF-2.0].

## What is unique to financial services

**The exam-driven reality.** A bank's CSF 2.0 Profile is not an internal-only document. OCC, FDIC, Federal Reserve, and state examiners will read it. The Profile becomes part of the examination record, and discrepancies between the Profile's self-assessment and the examiner's findings can become Matters Requiring Attention (MRAs) or Matters Requiring Immediate Attention (MRIAs). This makes the interpretive mappings in Tables 1-4 operationally significant — the bank must be able to defend every Tier rating and every "Largely" or "Fully" Subcategory score with evidence that satisfies both the framework logic and the examiner's expectations.

**The supervisory letter / MRA implications of a weak GOVERN function.** A bank that scores Tier 1 (Partial) on CSF 2.0 GOVERN is effectively telling its examiners that board oversight, risk appetite, and third-party governance are ad hoc. In a post-SolarWinds regulatory environment, this is a red flag that can trigger a targeted examination of the bank's third-party risk management program and, in severe cases, a formal enforcement action. Conversely, a Tier 3 (Repeatable) GOVERN Profile provides evidence that the board's cyber risk governance meets or exceeds OCC Heightened Standards expectations, potentially reducing examination intensity.

**The vendor-risk amplification.** A bank's cyber risk is its vendors' cyber risk, and examiners know it. CSF 2.0's GV.SC (Cybersecurity Supply Chain Risk Management) is the single most-examined Category for a financial institution. The bank must demonstrate not just a third-party risk program but a fourth-party view — knowing who the vendor's vendors are, and how a disruption at that layer cascades into the bank's operations. This goes beyond FFIEC CAT Domain 4 (External Dependency Management) by requiring the governance layer (GV.SC-01 through GV.SC-06) that examiners now expect post-2023 Interagency Guidance on Third-Party Relationships.

## Cross-references to skill chunks and sibling skills

- `chunks/01-functions-categories.md` — the function structure and 1.1-to-2.0 delta; load first to understand the 6-Function taxonomy used in Tables 1-4.
- `chunks/05-govern-function.md` — GOVERN deep-dive, especially GV.SC (Supply Chain Risk), GV.OV (Oversight), and the per-Category evidence examples needed to satisfy OCC Heightened Standards expectations.
- `chunks/08-informative-references-crosswalk.md` — the CSF 2.0 to 800-53 Rev 5 / 5.1.1 mapping; use for banks that also maintain an 800-53 view for FedRAMP or federal contract compliance.
- `nist-800-53-rmf` — the sibling control-catalog skill; a bank serving federal customers (e.g., processing Treasury disbursements) will likely run 800-53 alongside CSF 2.0. See that skill's `industries/financial-services.md` for the 800-53 overlay pattern.
- `coso-internal-controls` — the SOX 404 ICFR skill; Table 4 shows which CSF Subcategories supplement ITGCs; COSO's Significant Deficiency / Material Weakness classification is the severity taxonomy that the audit committee and external auditor use (CSF 2.0 has no equivalent — gap items are prioritized, not classified).
- `audit-workpapers` — the 5-part C-C-C-E-R (Condition, Criteria, Cause, Effect, Recommendation) finding format is the expected audit-report structure for presenting CSF gap items to the board audit committee.

## Anti-hallucination

- "FFIEC CAT maturity levels are NOT the same as CSF Tiers. FFIEC CAT uses a 5-level supervisory maturity scale (Baseline, Evolving, Intermediate, Advanced, Innovative) across 5 domains for examination purposes [FFIEC CAT 2017 Assessment]. CSF 2.0 uses a 4-level organizational maturity scale (Partial, Risk Informed, Repeatable, Adaptive) for the org's own cybersecurity risk governance [NIST-CSF-2.0 Section 3.1]. One is a supervisory tool; the other is a self-assessment framework. Do not conflate 'Advanced' with 'Tier 4' or 'Evolving' with 'Tier 2.' Source: FFIEC CAT 2017 and NIST CSF 2.0 CSWP 29."

- "OCC Heightened Standards (12 CFR 30 Appendix D) apply to banks over $50B in assets. Mid-size and community banks follow 12 CFR 30 Appendix A (Safety and Soundness Standards), which is far less prescriptive on risk governance. Do not apply the Heightened Standards Table (Table 2) to a community bank without qualification. Source: 12 CFR Part 30 [12-CFR-30]."

- "NY DFS Part 500 Section 500.17(a) requires notification to the Superintendent within 72 hours of determining a cybersecurity incident has occurred [NY-DFS-500]. CSF 2.0 does not encode a specific incident reporting timeline. Do not imply that CSF 2.0 compliance satisfies the DFS 500 notification requirement — the regulation is the binding obligation; CSF 2.0 is the evidence framework. Source: 23 NYCRR 500 [NY-DFS-500]."

- "SOX 404 ITGCs and CSF 2.0 Subcategories overlap but are not interchangeable. SOX ITGCs are tested for financial reporting risk (PCAOB AS 2201). CSF 2.0 Subcategories are assessed for cybersecurity risk [NIST-CSF-2.0 Section 2.3]. An org can have clean SOX ITGCs with no material weaknesses and a weak CSF PROTECT Profile — or vice versa. Table 4 identifies evidence-sharing opportunities, not framework equivalence."

- "[VERIFY]: The OCC Heightened Standards URL provided (bulletin-2014-13.html) returned an unrelated FFIEC joint statement on ATM attacks when fetched. The actual OCC Heightened Standards were codified in 12 CFR 30 Appendix D (effective September 2014). Confirm the correct OCC Bulletin number (possibly 2014-45 or a Federal Register final rule citation) and update the `regulatory_anchors` frontmatter field accordingly."

- "[VERIFY]: The FFIEC CAT 2017 source URL (ffiec.gov/cyberassessmenttool.htm) returned HTTP 403 on multiple retrieval attempts. The domain structure and maturity-level taxonomy used in this file are based on known FFIEC CAT 2017 documentation but could not be confirmed via live fetch. Once access is restored, verify: (a) exact maturity-level names (Baseline/Evolving/Intermediate/Advanced/Innovative), (b) exact domain names (especially whether Domain 5 is 'Cyber Incident Management and Resilience' or a different name), and (c) whether there is a 2024 or 2025 update (the FFIEC announced a CAT 2.0 modernization effort)."

- "[VERIFY]: Table 3 (CSF 2.0 Subcategory to NY DFS 500) is a representative interpretive mapping. No authoritative crosswalk from CSF 2.0 to NY DFS Part 500 has been published by DFS or NIST as of the `last_verified` date. Each mapping should be reviewed by qualified counsel before being presented to a DFS examiner. Confirm Section 500.17(a) is the 72-hour notification provision in the amended (November 2023) regulation — it was previously Section 500.13 in the pre-amendment version."

- "[VERIFY]: OCC Bulletin 2023-17 was referenced in Table 2 and the unique-to-financial-services section. Confirm the exact bulletin number and title for the 2023 Interagency Guidance on Third-Party Relationships. The OCC's own Quick Access menu links to `/news-issuances/bulletins/2023/bulletin-2023-17.html` under 'Third-Party Relationships: Interagency Guidance on Risk Management' — confirm this is the correct citation or use the Federal Register citation instead."
