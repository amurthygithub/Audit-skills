---
industry: manufacturing
parent_skill: nist-csf-2
title: "Manufacturing — CSF 2.0 alongside CMMC, NIST 800-171, IEC 62443, and IATF 16949"
version: 0.1.0
status: active
frameworks: [NIST-CSF-2.0, CMMC-L1, CMMC-L2, CMMC-L3, NIST-SP-800-171-Rev3, NIST-SP-800-172, IEC-62443-3-3, IEC-62443-4-2, IATF-16949, ISO-21434, NIST-SP-800-82-Rev3, NIST-SP-800-53-Rev5.1.1]
primary_personas: [CISO at a DoD supplier, VP Manufacturing Operations, OT/ICS Security Lead, Quality Director (IATF), Plant Manager, Defense Contract Management Agency (DCMA) reviewer]
regulatory_anchors: [32-CFR-Part-170, DFARS-252.204-7012, NIST-SP-800-171-Rev3, CMMC-L2-final-rule-Oct-2024, IEC-62443-3-3-2013]
last_verified: "2026-06-07"
---


# Manufacturing — CSF 2.0 alongside CMMC, 800-171, IEC 62443, and IATF 16949

This file is the **industry view** for discrete manufacturing organizations (industrial, automotive, aerospace) using CSF 2.0 alongside their pre-existing operational technology (OT) and federal-supply-chain regulatory stack. It covers both civilian manufacturing and manufacturers that are DoD suppliers (CMMC L1 or L2). It does **not** cover federal civilian agencies themselves (see `public-sector.md`) or pure OT/ICS environments (which would require a dedicated IEC 62443 skill).

## Manufacturing Framing (6 Questions)

### 1. Why do DoD suppliers need CSF 2.0 if they already need CMMC L2?

CMMC L2 mandates 110 controls from NIST SP 800-171 Rev 3 [NIST-SP-800-171-Rev3] and requires a third-party assessment (C3PAO) for Level 2 certification. CSF 2.0 is a voluntary, outcome-based framework that operates at a different level of abstraction:

- **CMMC L2 is a compliance floor** — "do you have these 110 controls implemented?" It is pass/fail at the assessment-objective level.
- **CSF 2.0 is a maturity and governance posture** — "how well does your cybersecurity program perform across 6 outcome-oriented Functions, and what is your organizational Tier?"

The practical rationale: a manufacturer can pass a CMMC L2 assessment (meeting all 110 control requirements) and still have a disorganized program — no board oversight, no supply chain governance, no continuous improvement cycle. CSF 2.0's GOVERN function (`GV.OC`, `GV.RM`, `GV.OV`) exposes these gaps. Conversely, a manufacturer that builds a CSF Current Profile first has a structured gap analysis that directly informs the CMMC L2 System Security Plan (SSP) and the Plan of Action and Milestones (POA&M). The frameworks are complementary, not competitive.

### 2. How does CSF 2.0 GOVERN map to the C-Suite ownership that CMMC L2 expects (the "affirming official" requirement)?

CMMC requires a senior company official to **affirm** CMMC compliance and submit the affirmation to the Supplier Performance Risk System (SPRS). This "affirming official" — typically the CEO, CFO, or General Counsel — signs a legal attestation that the scores in the CMMC assessment are true. This maps directly to CSF 2.0:

| CMMC L2 affirming official requirement | CSF 2.0 Subcategories |
|----------------------------------------|------------------------|
| Senior official affirms compliance status in SPRS | `GV.OV-01` (cybersecurity performance reviewed), `GV.OV-02` (strategy reviewed/adjusted) |
| Senior official is accountable for CUI protection | `GV.RR-01` (leadership accountable for cyber risk) |
| Senior official allocates adequate resources | `GV.RR-03` (adequate resources allocated) |
| Compliance status is communicated to DoD | `GV.RR-02` (roles, responsibilities, authorities communicated) |
| Board-level awareness of CMMC status | `GV.OC-01` (mission understood), `GV.OC-03` (legal/regulatory understood) |

Source: CMMC 32 CFR Part 170 (32 CFR 170.20 affirming official definition); mapped interpretively to CSF 2.0 Subcategories [NIST-CSF-2.0 §2.2].

The affirming official is the **single strongest bridge between CMMC and CSF 2.0 GOVERN**. If a manufacturer's affirming official cannot explain what risk posture the CSF Current Profile describes, the governance chain is broken.

### 3. What's the relationship between CSF Tiers (1-4) and CMMC L1/L2/L3 levels?

These are **different scales on different axes**:

| Dimension | CSF 2.0 Tiers | CMMC Levels |
|-----------|---------------|-------------|
| What it measures | Organizational maturity (how well programs are managed) | Control implementation (which controls are in place) |
| Scale | Tier 1 (Partial) → Tier 4 (Adaptive) | Level 1 (FCI, 15 controls) → Level 3 (CUI + APT, 110+35 controls) |
| Assessment type | Self-assessment (voluntary) | L1: self-assessment; L2: C3PAO assessment; L3: DIBCAC |
| Outcome | A posture description per Function | A certification level |
| Relationship | A Tier 4 org can be at CMMC L1; a Tier 2 org can be at CMMC L3 | Independent of Tier |

There is no normative mapping from CSF Tier to CMMC Level. The practical alignment: a manufacturer at CSF Tier 2 (Risk Informed) should be able to achieve CMMC L2 self-assessment readiness; a manufacturer at CSF Tier 3 (Repeatable) should have the program maturityThere is no normative mapping from CSF Tier to CMMC Level. The practical alignggle with even CMMC L1 self-assessment because the program is ad hoc.

### 4. How does CSF 2.0 bridge IT and OT cybersecurity?

Manufacturing environments have two distinct technology stacks:

- **IT (Information Technology)**: ERP, email, HR systems, file servers, customer portals, engineering workstations — traditional cybersecurity domain; standard CSF Subcategories apply.
- **OT (Operational Technology)**: PLCs, SCADA, DCS, HMIs, MES, building automation, sensors, actuators — availability- and safety-critical; standard IT controls (e.g., aggressive patching, active scanning, password rotation) may cause downtime or safety incidents.

CSF 2.0 bridges IT and OT by operating at the **outcome level** rather than the control level. A Subcategory like `PR.IR-01` (network segmentation) applies to both IT (VLANs, firewalls, ZTNA) and OT (IEC 62443 zones and conduits, Purdue model segmentation). The **mechanism** differs, but the **outcome** is the same.

NIST SP 800-82 Rev 3 [NIST-SP-800-82-Rev3] is the authoritative bridge document: it applies 800-53 controls to OT environments with OT-specific implementation guidance. CSF 2.0's `GV.SC` (supply chain) covers both IT vendors (Microsoft, Cisco) and OT vendors (Rockwell, Siemens, ABB, Schneider Electric). The IT/OT convergence also affects `ID.AM` (asset inventory must cover both IT and OT assets), `DE.CM` (passive OT monitoring vs active IT scanning), and `RS.MI` (OT incident containment differs from IT containment).

### 5. What about IEC 62443 zones and conduits — how do they map to CSF 2.0 IDs?

IEC 62443 [IEC-62443-3-3-2013] organizes industrial automation security around **zones** (logical groupings of assets with shared security requirements) and **conduits** (communication channels between zones). This is a fundamentally different abstraction than CSF 2.0's function-based outcome taxonomy. The mapping is interpretive, not authoritative.

| IEC 62443 concept | Most relevant CSF 2.0 Subcategories (interpretive) | Rationale |
|-------------------|---------------------------------------------------|-----------|
| Zone definition (62443-3-3 §4) | `ID.AM-01` (asset inventory), `ID.AM-02` (software inventory) | You must identify assets before you can zone them |
| Conduit security (62443-3-3 §5) | `PR.IR-01` (network segmentation), `PR.AA-05` (access permissions) | Conduits control communication between zones |
| Security Level (SL) 1-4 per zone | CSF Tiers 1-4 (interpretive) | SL-T = Target SL; SL-A = Achieved SL; gap = remediation plan |
| System security requirements (62443-3-3 §5) | `PR.PS-01` (configuration mgmt), `PR.DS-01` (data-at-rest) | 62443 foundational requirements map to PROTECT categories |
| Component requirements (62443-4-2) | `PR.PS-02` (software integrity), `PR.PS-03` (vulnerability mgmt) | Component-level security maps to platform security |
| Risk assessment (62443-3-2) | `ID.RA-01` (vulnerabilities), `ID.RA-04` (threats), `ID.RA-05` (likelihood/impact) | 62443 zone-based risk assessment maps to ID.RA |
| Patch management (62443-3-3 SR 3.2) | `PR.PS-03` (vulnerability mgmt), `ID.RA-01` | OT patching is constrained by availability requirements |
| Remote access (62443-3-3 SR 2.1) | `PR.AA-05` (access permissions), `PR.AA-03` (MFA) | OT remote access is a high-risk vector |
| Intrusion detection (62443-3-3 SR 6.2) | `DE.CM-01` (network monitoring), `DE.AE-02` (event correlation) | OT IDS uses passive monitoring; IT IDS uses active |
| Incident response (62443-3-3 SR 7.1) | `RS.MA-01` (IR plan executed), `RS.AN-03` (analysis performed) | OT IR must account for safety and physical process impact |

The bridge document is NIST SP 800-82 Rev 3 [NIST-SP-800-82-Rev3], which applies NIST security controls to OT environments and includes ICS-specific overlay guidance for 800-53 controls. IEC 62443 is a paid ISO standard; the mapping above is derived from public summaries and practitioner experience, not from a NIST-published crosswalk.

### 6. Where does NIST 800-171 (110 controls) sit in a CSF 2.0 Profile (106 Subcategories)?

NIST SP 800-171 Rev 3 [NIST-SP-800-171-Rev3] has 14 control families with approximately 110 requirements organized into 320 assessment objectives. CSF 2.0 [NIST-CSF-2.0] has 106 Subcategories across 22 Categories. The mapping is **not 1:1**:

- **1-to-many**: A single CSF Subcategory typically maps to 1-5 800-171 controls. `PR.AA-01` (identity management) maps to 03.01.01, 03.05.01, 03.05.02, 03.05.03, 03.05.04, 03.05.05, 03.05.07, 03.05.11, 03.05.12, 03.15.01 — 10 different 800-171 controls [NIST IR spreadsheet, 800-171 Rev 3 column].
- **Many-to-1**: Multiple CSF Subcategories may map to the same 800-171 control when that control supports multiple outcomes.
- **Not all 800-171 controls map cleanly**: Some 800-171 controls (particularly physical security in family 03.10) have partial mappings to CSF Subcategories; some details are lost in the outcome-to-control translation.

The practical approach for a DoD supplier: build a CSF Current Profile first (assess all 106 Subcategories for maturity), then map the lagging Subcategories to their corresponding 800-171 controls. The 800-171 controls that are fully implemented become the SSP; the gaps become the POA&M.

## Crosswalk Tables

### Table 1: CSF 2.0 Function → CMMC L2 Practice Domain

CMMC L2 organizes its 110 practices into 14 domains (aligned with 800-171 Rev 3 families). The table below maps CSF Functions to the CMMC domains most relevant to each Function. CMMC is operational (control-focused); CSF is outcome-based.

| CSF 2.0 Function | Primary CMMC L2 Practice Domains (interpretive) | Notes |
|------------------|------------------------------------------------|-------|
| GOVERN (GV) | Governance is not a CMMC domain; maps to the affirming official requirement and SPRS submission | CMMC does not have a governance practice domain — this is the gap CSF fills |
| IDENTIFY (ID) | Risk Assessment (RA), System and Information Integrity (SI), Security Assessment (CA) | CMMC domains 3.11 (RA), 3.14 (SI), 3.12 (CA) |
| PROTECT (PR) | Access Control (AC), Awareness & Training (AT), Audit & Accountability (AU), Configuration Management (CM), Identification & Authentication (IA), Maintenance (MA), Media Protection (MP), Physical Protection (PE), Personnel Security (PS), System & Communications Protection (SC) | The bulk of CMMC L2 practices — 10 of 14 domains |
| DETECT (DE) | Audit & Accountability (AU), Security Assessment (CA), System & Information Integrity (SI) | Monitoring, auditing, and event detection |
| RESPOND (RS) | Incident Response (IR) | CMMC domain 3.06 |
| RECOVER (RC) | Incident Response (IR), Contingency Planning | Recovery is partially represented in the IR domain |

Source: CMMC L2 scoping guide and 32 CFR Part 170 [32-CFR-Part-170]; CSF Function definitions from [NIST-CSF-2.0 §2.1]. CMMC domain-to-CSF mapping is interpretive — CMMC does not publish a CSF 2.0 crosswalk.

**Key insight**: CMMC L2 has no governance domain. CSF 2.0's GOVERN function fills this gap for manufacturers. A CMMC L2-certified manufacturer without a GOVERN assessment has no board-level cyber risk posture — a deficiency that the DoD affirming official requirement partially addresses but that CSF 2.0 assesses comprehensively.

### Table 2: CSF 2.0 Subcategory → NIST 800-171 Rev 3 Control Mapping

Representative mapping (15 rows). 800-171 has ~110 requirements organized into 14 families; CSF has 106 Subcategories. The mapping is 1-to-many in most cells. All rows sourced from the NIST CSF 2.0 Informative References spreadsheet [NIST-CSF-2.0 IR, 800-171 Rev 3 column].

| CSF Subcategory | 800-171 Rev 3 Controls (per NIST IR spreadsheet) | 800-171 Family |
|-----------------|--------------------------------------------------|---------------|
| `GV.OC-03` (legal/regulatory) | 03.01.01, 03.02.01, 03.03.01, 03.04.01, 03.05.01, 03.06.01, 03.07.01, 03.08.01, 03.09.01, 03.10.01, 03.11.01, 03.12.01, 03.13.01, 03.14.01, 03.17.01 | Cross-family (all policy/procedure controls) |
| `GV.RR-01` (leadership accountable) | 03.02.01, 03.07.01, 03.09.04, 03.09.05 | Awareness, Personnel, and Maintenance |
| `GV.SC-03` (C-SCRM integrated) | 03.11.01, 03.11.04, 03.15.01, 03.17.01, 03.17.03 | Risk Assessment, System & Services Acquisition |
| `ID.AM-01` (hardware inventory) | 03.04.01, 03.04.03 | Configuration Management |
| `ID.RA-01` (vulnerabilities) | 03.11.03, 03.12.01, 03.12.02, 03.14.01, 03.14.02, 03.14.06 | Risk Assessment, System & Information Integrity |
| `PR.AA-01` (identity management) | 03.01.01, 03.05.01, 03.05.02, 03.05.03, 03.05.04, 03.05.05, 03.05.07, 03.05.11, 03.05.12, 03.15.01 | Access Control, Identification & Authentication |
| `PR.AA-03` (MFA / authenticator mgmt) | 03.01.11, 03.05.01, 03.05.02, 03.05.03, 03.05.04, 03.05.07, 03.05.12 | Access Control, Identification & Authentication |
| `PR.AA-05` (access permissions) | 03.01.01, 03.01.02, 03.01.03, 03.01.04, 03.01.05, 03.01.06, 03.01.08, 03.01.10, 03.01.12 | Access Control |
| `PR.AT-02` (role-based training) | 03.02.01, 03.02.02, 03.02.03, 03.02.04 | Awareness & Training |
| `PR.DS-01` (data-at-rest) | 03.08.09, 03.12.05, 03.13.01, 03.13.04, 03.13.06, 03.13.08, 03.13.10, 03.13.11, 03.14.02, 03.14.06 | Media, System & Communications, System & Information Integrity |
| `PR.PS-01` (configuration management) | 03.04.01, 03.04.02, 03.04.03, 03.04.04, 03.04.05, 03.04.06, 03.04.07, 03.04.08 | Configuration Management |
| `PR.IR-01` (network segmentation) | 03.01.03, 03.13.01, 03.13.02, 03.13.04, 03.13.07 | Access Control, System & Communications Protection |
| `DE.CM-01` (network monitoring) | 03.01.01, 03.03.03, 03.04.03, 03.12.03, 03.13.01, 03.13.06, 03.14.06 | Multi-family |
| `RS.MA-01` (IR plan executed) | 03.06.02, 03.06.05, 03.17.03 | Incident Response, System & Services Acquisition |
| `RC.RP-01` (recovery executed) | 03.06.01, 03.06.05 | Incident Response |

Source: NIST CSF 2.0 Informative References spreadsheet, retrieved 2026-06-07 from `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`. 800-171 Rev 3 control IDs use the 03.XX.YY format [NIST-SP-800-171-Rev3]. This table covers a representative subset; the full mapping (all 106 Subcategories) is in `chunks/08-informative-references-crosswalk.md` §3.

### Table 3: CSF 2.0 → IEC 62443 Mapping

Representative mapping (12 rows). IEC 62443 [IEC-62443-3-3-2013] is a zone/conduit-based industrial automation security standard; CSF 2.0 is function/outcome-based. The mapping is **interpretive** — NIST does not publish an authoritative CSF-to-62443 crosswalk. The bridge is NIST SP 800-82 Rev 3 [NIST-SP-800-82-Rev3].

| CSF 2.0 Subcategory | IEC 62443 Reference (interpretive) | Interpretation |
|----------------------|-----------------------------------|----------------|
| `ID.AM-01` (asset inventory) | 62443-3-3 SR 7.8 (inventory of assets in zones) | Asset discovery is prerequisite to zone definition |
| `ID.AM-02` (software inventory) | 62443-3-3 SR 7.8, 62443-4-2 CR 7.8 | Software inventory per zone |
| `ID.RA-01` (vulnerabilities) | 62443-3-3 SR 3.2 (patch management), SR 3.1 (security functionality verification) | OT vulnerability management differs from IT — patching windows are constrained |
| `ID.RA-04` (threats) | 62443-3-2 (security risk assessment for IACS) | 62443-3-2 defines zone-and-conduit risk assessment methodology |
| `PR.AA-05` (access permissions) | 62443-3-3 SR 2.1 (authorization enforcement), SR 2.5 (session lock) | Access control per zone |
| `PR.IR-01` (network segmentation) | 62443-3-3 SR 5.1 (network segmentation), SR 5.2 (zone boundary protection) | The strongest mapping — 62443 is built on segmentation |
| `PR.PS-01` (configuration management) | 62443-3-3 SR 7.6 (configuration management) | Configuration management for IACS components |
| `PR.PS-03` (vulnerability management) | 62443-3-3 SR 3.2 (patch management), SR 3.4 (malicious code protection) | OT patching requires testing in non-production environment |
| `DE.CM-01` (network monitoring) | 62443-3-3 SR 6.2 (continuous monitoring), SR 6.1 (auditable events) | OT monitoring is passive; active scanning risks process disruption |
| `DE.AE-02` (event correlation) | 62443-3-3 SR 6.2 (continuous monitoring) | Event correlation across IT and OT domains |
| `RS.MA-01` (IR plan executed) | 62443-3-3 SR 7.1 (incident response planning), SR 7.2 (incident response execution) | OT IR must include safety response procedures |
| `RC.RP-01` (recovery executed) | 62443-3-3 SR 7.4 (recovery and reconstitution) | OT recovery must consider physical process restart safety |

Source: IEC 62443-3-3 [IEC-62443-3-3-2013] public summaries; NIST SP 800-82 Rev 3 [NIST-SP-800-82-Rev3] for ICS security guidance. IEC 62443 is a paid ISO standard; the specific control references (SR/CR numbers) should be verified against the full standard text.

### Table 4: CSF 2.0 → IATF 16949 / Automotive Cybersecurity (ISO 21434)

Representative mapping (10 rows). IATF 16949 [IATF-16949] is the automotive quality management standard; ISO 21434 [ISO-21434] is the automotive cybersecurity engineering standard (published 2021 as ISO/SAE 21434:2021). Both are paid ISO standards. The mapping is interpretive.

| CSF 2.0 Subcategory | IATF 16949 / ISO 21434 Reference (interpretive) | Interpretation |
|----------------------|------------------------------------------------|----------------|
| `GV.OC-01` (mission understood) | IATF 16949 §5.1 (leadership and commitment), §4.1 (understanding context) | Quality management context includes cybersecurity risk |
| `GV.RR-01` (leadership accountable) | IATF 16949 §5.1.1 (leadership accountability for QMS) | Quality leadership accountability extends to cybersecurity |
| `GV.SC-05` (contracts with C-SCRM) | IATF 16949 §8.4 (control of externally provided products) | Supplier quality management includes cybersecurity requirements |
| `GV.PO-01` (policy established) | IATF 16949 §5.2 (quality policy) | Cybersecurity policy parallels quality policy |
| `ID.AM-01` (asset inventory) | ISO 21434 §15.3 (item definition, cybersecurity relevance) | Automotive item definition maps to asset identification |
| `ID.RA-01` (vulnerabilities) | ISO 21434 §15.6 (threat analysis and risk assessment — TARA) | TARA is the automotive cybersecurity risk assessment methodology |
| `PR.PS-01` (configuration management) | IATF 16949 §7.1.3.2.3 (production tooling management) | Configuration control of production tooling and software |
| `DE.CM-01` (continuous monitoring) | ISO 21434 §15.10 (cybersecurity monitoring) | Vehicle-level cybersecurity monitoring post-production |
| `RS.MA-01` (IR plan executed) | ISO 21434 §15.10 (incident response) | Automotive cybersecurity incident response |
| `RC.RP-01` (recovery executed) | ISO 21434 §15.10 (remediation, product recall) | Automotive recovery includes over-the-air updates and product recall |

Source: IATF 16949:2016 [IATF-16949] and ISO/SAE 21434:2021 [ISO-21434] public summaries. Both are paid ISO standards; verify specific clause references against the full text. Automotive cybersecurity is a relatively new discipline; the ISO 21434 standard was published in 2021 and is still maturing in implementation practice.

### Table 5: IT/OT Convergence — Which CSF Subcategories Apply to IT, OT, or Both

This is a unique manufacturing concern. The table classifies representative Subcategories by domain applicability.

| CSF Subcategory | IT | OT | Both | Notes |
|-----------------|----|----|------|-------|
| `GV.OC-01` (mission understood) | | | X | Mission includes both business continuity (IT) and production continuity (OT) |
| `GV.SC-04` (suppliers prioritized) | | | X | IT vendors (Microsoft, Cisco) AND OT vendors (Rockwell, Siemens, ABB) |
| `ID.AM-01` (hardware inventory) | | | X | IT hardware + OT hardware (PLCs, HMIs, drives) — different CMDB approaches |
| `ID.AM-02` (software inventory) | | | X | IT software (OS, DB) + OT firmware (PLC logic, HMI runtime) |
| `ID.RA-01` (vulnerabilities) | | | X | IT vuln scanning (active) vs OT vuln assessment (passive or offline) |
| `PR.AA-01` (identity management) | | | X | IT Active Directory vs OT local authentication; shared accounts are common in OT |
| `PR.AA-03` (MFA) | X | | | OT systems often lack MFA capability; compensating controls required (62443 SR 2.1) |
| `PR.AT-02` (role-based training) | | | X | IT security training vs OT safety/security combined training |
| `PR.DS-01` (data-at-rest) | | | X | IT encryption vs OT data integrity (recipe, setpoints) — encryption may impact OT latency |
| `PR.PS-03` (vulnerability management) | X | (partial) | | IT patching (monthly) vs OT patching (annual or biennial maintenance windows) |
| `PR.IR-01` (network segmentation) | | | X | IT VLANs vs OT Purdue model segmentation (IT/OT DMZ, zones, conduits) |
| `DE.CM-01` (network monitoring) | | | X | IT active monitoring (IDS/IPS, SIEM) vs OT passive monitoring (protocol-aware, non-intrusive) |
| `DE.AE-02` (event correlation) | | | X | IT SIEM correlation vs OT SOC that understands OT protocols (Modbus, DNP3, OPC-UA) |
| `RS.MA-01` (IR plan executed) | | | X | IT IR (isolate, wipe, restore) vs OT IR (safe shutdown, physical isolation, process hold) |
| `RS.AN-03` (analysis performed) | | | X | IT forensics (disk images, memory dumps) vs OT forensics (PLC logic comparison, historian data) |
| `RC.RP-01` (recovery executed) | | | X | IT recovery (restore from backup) vs OT recovery (reload PLC logic, validate safety interlocks, controlled restart) |

Source: NIST SP 800-82 Rev 3 [NIST-SP-800-82-Rev3] (§4 OT topologies, §5 threats, §6 countermeasures); IEC 62443 [IEC-62443-3-3-2013] for zone/conduit model; practitioner experience. The IT/OT split is interpretive — some manufacturers operate converged IT/OT SOCs; others maintain strict separation.

## What's Unique to Manufacturing

### IT/OT Convergence

A discrete manufacturer runs two parallel technology stacks that must coexist securely. The IT side (ERP — SAP/Oracle, email — Exchange/O365, engineering — CAD/CAM/PLM, customer portals, HR systems) is a standard enterprise IT environment that fits CSF 2.0's PROTECT/DETECT/RESPOND/RECOVER cycle. The OT side (PLCs — Rockwell ControlLogix, Siemens S7; SCADA — Wonderware, Ignition, FactoryTalk; MES — Apriso, SAP ME; DCS — Honeywell, Emerson DeltaV; building automation, sensors, drives) has fundamentally different constraints: patching windows measured in years not months, authentication that cannot support MFA, protocols (Modbus, DNP3, PROFINET, EtherNet/IP) that lack encryption, and safety interlocks that must remain operational during a cyber incident.

CSF 2.0's outcome-based approach is valuable here because it avoids prescribing specific controls (which might be unsafe in OT) and instead asks: "Does the organization achieve the outcome of network segmentation?" — leaving the implementation choice (Purdue model with IDMZ vs IEC 62443 zones/conduits vs software-defined segmentation) to the OT engineer. This is also why the IEC 62443 crosswalk (Table 3) is interpretive: 62443 specifies zone-level security requirements; CSF asks whether the outcome is achieved.

The `GV.SC` (supply chain) Category is particularly affected by IT/OT convergence. A manufacturer's supply chain includes both IT vendors (cloud, SaaS, infrastructure) and OT vendors (automation equipment, industrial control components, engineering services). CSF 2.0's `GV.SC-04` (suppliers prioritized by criticality) must account for the fact that a critical OT vendor (the sole PLC supplier for a production line) has different assessment criteria than a critical IT vendor (the email provider). The 10 `GV.SC` Subcategories provide the granularity to handle both.

### The CMMC "Affirming Official" Requirement

The CMMC final rule (32 CFR Part 170, published October 15, 2024) [32-CFR-Part-170] requires a senior company official to affirm CMMC compliance status and submit the affirmation to SPRS. This "affirming official" is typically the CEO, CFO, or General Counsel — someone with legal authority to bind the company. The affirming official signs under penalty of the False Claims Act (31 U.S.C. 3729-3733).

This requirement is the single strongest governance mechanism in CMMC and directly maps to CSF 2.0 GOVERN:

- `GV.OV-01` (cybersecurity performance reviewed): The affirming official must review the assessment results before affirming.
- `GV.RR-01` (leadership accountable): The affirming official is the accountable party.
- `GV.RR-02` (roles and authorities communicated): The affirming official's role must be documented and understood internally.
- `GV.OC-03` (legal/regulatory requirements understood): The affirming official must understand CMMC regulatory requirements.

For a CISO at a DoD supplier, the affirming official is the board-access point: the CISO builds the CSF Current Profile and the CMMC L2 SSP; the affirming official reviews them, understands the residual risk, and signs the SPRS affirmation. The CSF Profile is the artifact that makes the risk legible to the affirming official.

### The "Unfunded Mandate" Problem

CMMC L2 requires 110 controls from NIST 800-171 Rev 3. For a small machine shop (50-200 employees, $10M-$50M annual revenue) that wants to bid on DoD work, the compliance cost is estimated at $50,000-$150,000 for the assessment alone [VERIFY: DoD CMMC cost estimate documentation], plus implementation costs (MFA, SIEM, encryption, policy development) that can reach $250,000-$750,000. For a small manufacturer with 5% net margin on $30M revenue ($1.5M profit), a $500,000 compliance program is one-third of annual profit.

CSF 2.0 helps prioritize: a Current Profile with 106 scored Subcategories identifies which outcomes are already achieved (e.g., `PR.IR-01` network segmentation may already exist via the Purdue model), which are partially achieved (e.g., `PR.AA-03` MFA is deployed in IT but not OT), and which are not implemented (e.g., `GV.SC-07` ongoing supplier risk monitoring). The manufacturer can then build a Target Profile that selects the minimum Subcategories needed to close the CMMC L2 gap, phased over 12-24 months. This is more capital-efficient than implementing all 110 controls in parallel.

### Safety-Cybersecurity Overlap

In manufacturing, a cyber incident can cause physical harm. A compromised PLC can disable safety interlocks, over-pressurize a vessel, over-speed a turbine, or bypass emergency stops. A compromised HMI can display false process values to an operator. A ransomware attack on the MES can halt production, but the safety risk comes from the uncontrolled state transition when processes are interrupted mid-cycle.

This changes the risk equation for several CSF Subcategories:

- `DE.AE` (Adverse Event Analysis): In manufacturing, an adverse event is not just a data breach — it could be a near-miss safety incident caused by a cyber event. Correlation of OT logs (process historian, alarm history) with IT logs (firewall, SIEM) is essential.
- `RS.MI` (Incident Mitigation): OT incident mitigation prioritizes safety over containment. The first response to a detected compromise in a manufacturing cell may be a controlled process shutdown, not network isolation. The IR plan must integrate with the plant's safety management system.
- `RC.RP` (Recovery Plan Execution): OT recovery requires validating that safety interlocks, alarms, and emergency shutdowns are functional before restart. IT recovery validates data integrity; OT recovery validates process safety.
- `GV.RM-02` (Risk Appetite): The board must set a cyber risk appetite that accounts for physical safety risk. A manufacturer that tolerates "moderate" cyber risk in IT may need "low" risk tolerance in OT because of the safety dimension.

## Cross-References

- `chunks/01-functions-categories.md` — the 6 Functions, 22 Categories, and 106 Subcategories that anchor every table in this file.
- `chunks/05-govern-function.md` — the GOVERN function, especially `GV.RR-01`, `GV.RR-02`, and `GV.OV-01` which map to the CMMC affirming official requirement.
- `chunks/08-informative-references-crosswalk.md` — the authoritative 800-171 mapping (§3) and the 1-to-many pattern (§6) that applies to every 800-171 row in Table 2.
- `nist-800-53-rmf` — CMMC L2 is built on 800-171 which is a subset of 800-53; the RMF skill covers the full control catalog including the PM and SR families that map to GOVERN.
- `audit-workpapers` — for DCMA audits, CMMC L2 C3PAO assessments, and the 5-part finding format used in POA&M items.
- `isaca-audit-methodology` — for the audit perspective on CMMC L2 and COBIT 2019 governance maturity assessment of the affirming official's oversight function.

## Anti-Hallucination

- **CMMC L2 final rule was published October 15, 2024 (32 CFR Part 170); prior to that it was the CMMC 2.0 interim model.** Verify the current CMMC version and rule status before any mapping. As of 2026-06-07, CMMC Phase 1 Implementation is active (Nov 10, 2025 – Nov 9, 2026), focused primarily on Level 1 and Level 2 self-assessments. The DoD CIO CMMC page was verified via `https://dodcio.defense.gov/CMMC/` [CMMC-2.0].

- **CMMC L1 (Federal Contract Information, FCI) is 15 controls derived from FAR 52.204-21; CMMC L2 (Controlled Unclassified Information, CUI) requires 110 controls from NIST 800-171 Rev 3; CMMC L3 (high-value CUI) adds enhanced requirements from NIST 800-172 Rev 3.** NIST SP 800-172 Rev 3 [NIST-SP-800-172] was published May 2026 — verify the current version against `https://csrc.nist.gov/pubs/sp/800/172/r3/final`.

- **NIST 800-171 Rev 3 was published May 2024 (superseding Rev 2 from January 2021).** The control count and structure changed — verify the current version at `https://csrc.nist.gov/pubs/sp/800/171/r3/final` [NIST-SP-800-171-Rev3] before mapping. The 800-171 Rev 3 control IDs use the 03.XX.YY format (e.g., 03.01.01 for Access Control policy).

- **CSF 2.0 has 106 Subcategories; NIST 800-171 has approximately 110 controls.** The mapping is 1-to-many in places (one Subcategory may map to multiple 800-171 controls) and 1-to-1 in others. There is no clean 1:1 crosswalk. All Table 2 rows are sourced from the NIST CSF 2.0 Informative References spreadsheet; any row not explicitly sourced should be verified against the current spreadsheet at `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`.

- **IEC 62443 zones and conduits are a fundamentally different abstraction than CSF Functions/Subcategories.** IEC 62443 organizes security around network segmentation; CSF organizes around governance and process outcomes. The crosswalk in Table 3 is **interpretive, not authoritative**. NIST SP 800-82 Rev 3 [NIST-SP-800-82-Rev3] (published September 2023) is the bridge document. Verify against `https://csrc.nist.gov/pubs/sp/800/82/r3/final`.

- **NIST SP 800-172 Rev 3 was published May 2026**, not 2021. The earlier version (SP 800-172, not marked as a revision) was published February 2021. CMMC L3 references the current version. Verify at `https://csrc.nist.gov/pubs/sp/800/172/r3/final` [NIST-SP-800-172].

- **IATF 16949 and ISO 21434 are paid ISO standards.** The clause references in Table 4 are derived from public summaries and practitioner experience; verify against the full standard text. ISO/SAE 21434:2021 is the current automotive cybersecurity standard.

- **The IT/OT convergence table (Table 5) is based on practitioner experience and NIST SP 800-82 Rev 3 [NIST-SP-800-82-Rev3].** The OT column is a judgment call for many Subcategories — the applicability depends on the specific OT architecture, the Purdue model level, and whether the manufacturer operates a converged or separate IT/OT security program. Always verify per-manufacturer.

- **CSF Tiers are not CMMC Levels.** A manufacturer at CSF Tier 2 can be CMMC L2 compliant; a manufacturer at CSF Tier 4 can be at CMMC L1. These are independent axes. Do not equate them.

- **The affirming official requirement is a legal attestation under penalty of the False Claims Act.** This file describes the governance mapping to CSF 2.0; it is not legal advice. The affirming official should consult counsel before signing.
