# Industry: Healthcare (BAA-covered Health-tech, Payers, Providers)

## 1. Posture

Healthcare organizations subject to HIPAA need SOC 2 with Privacy criteria for PHI. HITRUST CSF certification is increasingly common as a parallel or complementary framework. SOC 2 Type II with Security + Availability + Confidentiality + Privacy is the typical scope.

| Scenario | SOC Type | TSC Categories | Notes |
|----------|----------|----------------|-------|
| Health-tech SaaS (EHR, telehealth, analytics) | SOC 2 Type II | Security + Availability + Confidentiality + Privacy | BAA required; Privacy criteria maps to HIPAA |
| Healthcare payer / claims processor | SOC 2 Type II | Security + Availability + Processing Integrity + Confidentiality + Privacy | All five TSC categories often in scope |
| Health data exchange / interoperability platform | SOC 2 Type II | Security + Availability + Confidentiality + Privacy | HITRUST CSF certification often paired |
| Medical device SaaS | SOC 2 Type II | Security + Availability + Processing Integrity | FDA premarket cybersecurity guidance overlay |

## 2. Boundary

The system includes the health-tech platform, PHI processing pipelines, and any interfaces to EHR systems. PHI flow diagrams are critical for defining the boundary.

## 3. Subservice Organizations

- IaaS provider (AWS/Azure/GCP): Carve-out with BAA from the cloud provider.
- EHR integration partners: Typically within scope if data flows through; carve-out if partner has own SOC 2 + HITRUST.
- Clinical data repositories: Carve-out or inclusive depending on integration depth.

## 4. Regulatory Overlay

- HIPAA Security Rule (45 CFR 164.302-318)
- HIPAA Privacy Rule (45 CFR 164.500-534)
- HITECH Act breach notification
- HITRUST CSF (if certified)
- GDPR (if EU patient data)
- State-level privacy laws (e.g., CCPA/CPRA for California residents)

## 5. Top Use Cases
- UC-01: Full SOC 2 Type II examination (adapted for health-tech with Privacy criteria)

## 6. HITRUST CSF Integration

HITRUST CSF maps to (a) SOC 2 TSC criteria, (b) HIPAA Security Rule, and (c) NIST 800-53 simultaneously. Category-level mapping:

| TSC Category | HITRUST Domain | Notes |
|-------------|---------------|-------|
| CC1-CC5 (COSO-aligned) | Domain 1: Information Protection Program + Domain 17: Risk Management | HITRUST adds maturity scoring |
| CC6 (Access Controls) | Domain 11: Access Control | Point-of-focus granularity differs |
| CC7 (System Operations) | Domain 12: Audit Logging & Monitoring + Domain 15: Incident Management | Audit logging overlap |
| A1-A3 (Availability) | Domain 16: BC/DR | HITRUST RTO/RPO requirements |
| P1-P8 (Privacy) | Domain 19: Data Protection & Privacy | GDPR alignment included |

The skill helps with SOC 2 to HITRUST gap analysis, but does NOT provide a full HITRUST validated assessment. HITRUST MyCSF is the definitive tool for point-of-focus mappings. See `data/seeds/tsc-to-hitrust.json` for the crosswalk seed.

## 7. Medical Device Security

For medical device SaaS and IoMT (Internet of Medical Things):
- **FDA premarket cybersecurity guidance:** SOC 2 must demonstrate device-level controls for authentication, encryption, and update integrity
- **IoMT segmentation:** CC6.1-CC6.3 apply to device-to-platform authentication; network segmentation is a compensating control
- **Device identity lifecycle:** provisioning, decommissioning, and credential rotation map to CC6.1, CC7.2

## 8. Break-Glass Access

Break-glass (emergency access) procedures map to CC6.1 (logical access security measures) with HIPAA 164.312(a)(2)(ii) Emergency Access Procedure (a REQUIRED implementation specification). CC6.3 governs role changes/removals — not emergency access. For healthcare:
- Break-glass bypasses standard access controls in clinical emergencies
- Must be logged (CC7.2) and reviewed (CC7.3)
- Cannot be an unchecked backdoor; must trigger post-hoc review within 24 hours
- Audit logging for break-glass events must be tamper-evident

## 9. BAA Chain and SOC 2 CUEC

HIPAA Business Associate Agreements form a chain of liability for PHI:
- Each BAA obligates the downstream vendor to the same HIPAA compliance level
- A vendor's SOC 2 report (scope, period, exceptions) informs your BAA oversight; its CUEC list states what the vendor requires of YOU — CUECs are your obligations, not evidence about the vendor
- When reviewing a vendor's SOC 2 as a CUEC: verify the Privacy criteria (P1-P8) are in scope for PHI-handling vendors
- Gap: if a vendor's SOC 2 excludes Privacy criteria but they handle PHI, the BAA chain may be at risk

## 10. Pain Points

- Privacy criteria complexity: P1-P8 require detailed privacy program documentation; many health-tech companies underestimate the Privacy criteria scope.
- BAA management: Each customer BAA must align with CUEC disclosures.
- Incident response: HIPAA breach notification timelines (60 days) impose stricter requirements than typical SOC reporting.
- HITRUST vs SOC 2 overlap: Many organizations pursue both; mapping and avoiding duplicate effort is complex.
- Subservice complexity: Multiple subservice organizations (cloud, EHR connectors, analytics platforms) create intricate CSOC disclosure requirements.

## 7. References
- AICPA TSP Section 100 (2017 TSC, 2022 revised)
- HIPAA Security Rule (45 CFR 164.302-318)
- HITRUST CSF v11
- NIST SP 800-66 Rev 2 (HIPAA Security Rule implementation)
