# Industry: Healthcare

Healthcare organizations (hospitals, health systems, payers, medical device manufacturers, health IT vendors) use ISACA/COBIT methodology for HIPAA compliance, HITRUST certification, and IT governance over clinical and administrative systems.

## 1. Posture

| Context | Audit Drivers | Frameworks |
|---------|-------------|------------|
| Hospital / health system | HIPAA Security Rule, HITECH, Joint Commission | COBIT APO13, DSS05 + HIPAA crosswalk |
| Health insurer / payer | HIPAA, state insurance regulators, ACA | COBIT governance + CMS MARS-E |
| Medical device manufacturer | FDA 21 CFR Part 820, ISO 13485, IEC 62304 | COBIT BAI objectives + FDA QSR |
| Health IT / EHR vendor | ONC Health IT Certification, HIPAA | COBIT APO13, BAI07 + ONC criteria |
| Business Associate | HIPAA BAA compliance, customer audits | ITGC testing + HIPAA Administrative Safeguards |

## 2. Boundary

Healthcare audit scope spans clinical systems (EHR, PACS, LIS), administrative/financial systems (billing, claims), medical devices (networked infusion pumps, patient monitors), and business associate relationships. ePHI data flows across all boundaries and must be tracked.

## 3. Inheritance Pattern

Covered entities inherit controls from business associates via BAAs. COBIT EDM objectives map to board-level governance of clinical IT risk. Cloud-hosted EHR/practice management systems inherit physical controls from the cloud provider; application-layer PHI controls (access, audit logging, encryption) are the covered entity's responsibility.

### HIPAA Crosswalk (COBIT to HIPAA Security Rule)

| COBIT Objective | HIPAA Safeguard | Mapping |
|-----------------|-----------------|---------|
| APO13 (Managed Security) | 164.308 Administrative Safeguards | Risk analysis, security management process |
| DSS05 (Managed Security Services) | 164.312 Technical Safeguards | Access control, audit controls, integrity |
| DSS01 (Managed Operations) | 164.310 Physical Safeguards | Facility access, workstation security |
| APO14 (Managed Data) | 164.312(c)(1) Integrity | ePHI integrity controls |
| BAI07 (Managed Change) | 164.308(a)(2) Assigned Security Responsibility | Change management accountability |
| MEA03 (Managed Compliance) | 164.308(a)(8) Evaluation | Periodic technical and non-technical evaluation |

### HITRUST CSF Scope

HITRUST CSF v11 integrates HIPAA, NIST, ISO, and COBIT controls. Organizations pursuing HITRUST certification should assess COBIT maturity alongside HITRUST control maturity. COBIT APO13 directly maps to HITRUST control domain 0 (Information Security Management Program).

## 4. Regulator/Customer Relationship

OCR (HHS Office for Civil Rights) enforces HIPAA. State attorneys general bring parallel actions. The FDA regulates medical device cybersecurity. CMS and state insurance commissioners regulate payers. COBIT MEA03 supports ongoing HIPAA compliance monitoring and OCR audit readiness.

### Key Healthcare-Specific Controls

- **Break-glass access**: Emergency access to ePHI without pre-authorization; COBIT DSS05.02 maps to identity and access management.
- **Minimum necessary**: HIPAA requires limiting PHI access to the minimum needed; ITGC access recertification supports this.
- **Audit logging**: HIPAA requires logging of all ePHI access; COBIT DSS05.04 maps to security event monitoring.
- **Business Associate Agreements (BAAs)**: Contractual controls with vendors handling ePHI; COBIT APO10 (Managed Vendors) supports vendor risk management.
- **Medical device security**: Networked medical devices require segmentation, patching, and lifecycle management; COBIT BAI03/BAI07 apply.

## 5. Top Use Cases

- **HIPAA Security Rule compliance assessment** using COBIT APO13, DSS05, MEA03
- **HITRUST readiness** with COBIT maturity as a governance baseline
- **ITGC testing for EHR/clinical systems** (access controls, change management, audit logging)
- **Business Associate risk assessment** using COBIT APO10 vendor management
- **Medical device cybersecurity** governance using COBIT BAI objectives

## 6. Pain Points

- HIPAA + HITRUST + COBIT stack: three overlapping frameworks create scope creep
- ePHI data flow mapping: identifying all systems that store, process, or transmit ePHI
- Medical device inventory: discovering and governing legacy clinical devices on the network
- Break-glass vs least privilege: balancing emergency access with access control rigor
- BAA enforcement: verifying that business associates maintain required controls
- Legacy EHR systems: platforms that predate modern access controls and audit logging

## 7. References

- HIPAA Security Rule (45 CFR Part 160 and Subparts A and C of Part 164)
- HITECH Act (Title XIII of ARRA, 2009)
- HITRUST CSF v11
- FDA Guidance: Content of Premarket Submissions for Management of Cybersecurity in Medical Devices
- FDA Guidance: Postmarket Management of Cybersecurity in Medical Devices
- ONC Health IT Certification Program (21st Century Cures Act)
- CMS Information Security ARS (Acceptable Risk Safeguards) / MARS-E 2.2
- NIST SP 800-66 Rev 2 (Implementing the HIPAA Security Rule)
- COBIT 2019: Focus Area for Information Security
