# Industry: Financial Services (Banks, Fintech, Payment Processors)

## 1. Posture

Financial services organizations typically need both SOC 1 (for ICFR) and SOC 2 (for security/availability). SOC 1 is driven by user entity auditors who need assurance on controls relevant to their own financial statement audits. SOC 2 is driven by vendor due diligence from banks and enterprise customers.

| Scenario | SOC Type | TSC Categories | Notes |
|----------|----------|----------------|-------|
| Payroll processor | SOC 1 Type II | N/A (management-defined control objectives) | User entity auditors need ICFR assurance |
| Payment processor / PSP | SOC 1 Type II + SOC 2 Type II | Security + Availability + Processing Integrity | Dual reports; PI added for transaction integrity |
| Banking SaaS / core banking platform | SOC 2 Type II | Security + Availability + Confidentiality | FFIEC/GLBA overlay; OCC/FDIC exam expectations |
| Fintech (lending, wealth management, insurance) | SOC 2 Type II | Security + Availability + Confidentiality | Regulator may accept SOC 2 as evidence of IT controls |

## 2. Boundary

The system is typically the service platform (payroll, payment processing, banking, or wealth platform). For fintech with multiple products, each may be a separate SOC engagement or a combined scope.

## 3. Subservice Organizations

- IaaS provider: Carve-out (standard).
- Core banking system provider: Often carve-out if the provider has its own SOC report.
- Payment network (Visa/Mastercard/etc.): Typically outside SOC scope; PCI DSS applies instead.
- Data aggregators (Plaid, Yodlee): Carve-out if they have own SOC; otherwise inclusive.

## 4. Regulatory Overlay

- FFIEC IT Examination Handbook (for banks)
- GLBA Safeguards Rule (financial institutions)
- PCI DSS v4.0 (if cardholder data is processed)
- OCC/FDIC/FRB examination expectations
- SOX 404 / PCAOB AS 2201 (for publicly traded fintech)

## 5. Top Use Cases
- UC-01: Full SOC 2 Type II examination (adapted for fintech)

## 6. Pain Points

- Dual SOC 1 + SOC 2: Managing two parallel engagements with potentially overlapping control sets.
- Control objective definition: SOC 1 control objectives are management-defined, not standardized; mis-scoping leads to user auditor pushback.
- Regulatory overlap: FFIEC, GLBA, PCI, SOX each impose additional expectations beyond SOC.
- ICFR scope creep: User entity auditors may request control objectives beyond what management defined.
- Bridge letter demand: Banks frequently request bridge letters during the gap period.

## 7. References
- AICPA TSP Section 100 (2017 TSC)
- FFIEC IT Examination Handbook
- GLBA Safeguards Rule (16 CFR Part 314)
- PCI DSS v4.0
