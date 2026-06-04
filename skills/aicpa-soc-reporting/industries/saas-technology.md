# Industry: SaaS / Cloud-Native Technology

## 1. Posture

Multi-tenant SaaS companies are the most common SOC 2 consumers. SOC 2 Type II is table-stakes for enterprise sales. Typical TSC categories: Security (always) + Availability (if SLA-backed) + Confidentiality (if handling customer data with specific confidentiality requirements).

| Scenario | Typical SOC Type | TSC Categories | Subservice Pattern |
|----------|-----------------|----------------|---------------------|
| B2B SaaS, early stage, first enterprise customer asking | SOC 2 Type I | Security | Carve-out (AWS/Azure/GCP) |
| B2B SaaS, established, annual renewal cycle | SOC 2 Type II | Security + Availability + Confidentiality | Carve-out (IaaS) |
| SaaS with PII (HR, health-tech, fintech) | SOC 2 Type II | Security + Confidentiality + Privacy | Carve-out (IaaS) |
| SaaS with financial transaction processing | SOC 2 Type II | Security + Availability + PI | Carve-out (IaaS + payment processor) |

## 2. Boundary

The system is the SaaS platform as deployed in the cloud. The boundary is documented with a network diagram, data-flow diagram, and a customer responsibility matrix (CRM) that lists CUECs. Typical CUECs: user access provisioning, data input validation, customer-managed encryption keys.

## 3. Inheritance and Subservice Organizations

- IaaS provider (AWS/Azure/GCP): Almost always carve-out. The IaaS provider has its own SOC 2 report. CSOCs include infrastructure access controls, data center physical security, network security.
- Payment processor: Carve-out. CSOCs cover payment processing security.
- CDN / Email service: Typically carve-out or scoped out.

## 4. Customer Relationship

Customers (user entities) request the SOC 2 report as part of vendor due diligence. Typical cycle: annual SOC 2 Type II, bridge letter for in-between periods. SOC 3 rarely requested; most customers want the detailed SOC 2 with CUECs and CSOCs.

## 5. Top Use Cases
- UC-01: Full SOC 2 Type II examination walkthrough
- UC-02: CUEC/CSOC identification for a multi-tenant SaaS

## 6. Pain Points

- Evidence collection: SaaS companies often underestimate the volume of evidence needed for Type II (continuous operating effectiveness over 12 months).
- CUEC identification: Misidentifying or omitting CUECs leads to user entity confusion and potential opinion qualification.
- Change management: SaaS CI/CD means frequent changes. CC8 (change management) testing is often the area with most exceptions.
- Vendor risk management: CC9.2 requires documented vendor risk management. Many SaaS companies treat this as an afterthought.
- Readiness gap: First-time SOC 2 companies often have significant gaps in CC3.2 (risk assessment), CC4.1 (monitoring), and CC9.2 (vendor risk).

## 7. References
- AICPA TSP Section 100 (2017 TSC, 2022 revised)
- Cloud Security Alliance (CSA)
- AWS/Azure/GCP SOC reports (for CSOC identification)
