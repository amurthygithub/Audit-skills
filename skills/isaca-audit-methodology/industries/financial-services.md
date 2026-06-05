# Industry: Financial Services

Financial services (banks, insurance, capital markets, payments, fintech) typically have robust SOC 2 or SOX ICFR baselines but need ISACA/COBIT methodology for IT audit scope and governance assessment.

## 1. Posture

| Sub-sector | Typical audit drivers | Dominant frameworks |
|-----------|----------------------|---------------------|
| Commercial bank | SOX 404, GLBA, FFIEC | COBIT 2019 + COSO 2013 |
| Insurance carrier | State insurance regulator, SOX | COBIT APO objectives |
| Capital markets | SEC/FINRA examination | COBIT + COSO |
| Payments/fintech | PCI DSS, SOX, GDPR | ITGC testing (all 4 categories) |
| Custodian/trust bank | Fiduciary duty, ERISA | COBIT EDM governance, ITGC |

## 2. Boundary

The audit scope typically includes core banking platforms, digital channels, data warehouses, and third-party service providers. ITGC testing spans the entire technology stack.

## 3. Inheritance Pattern

Third-party SOC 1/SOC 2 reports provide inheritance for sub-service organizations. COBIT EDM objectives map to board governance; COBIT APO objectives map to management controls. ITGC test results determine ITAC reliance for SOX testing.

## 4. Regulator/Customer Relationship

OCC, FDIC, FRB, SEC, FINRA, and state insurance commissioners impose overlapping requirements. COBIT 2019 focus areas (Risk Management, Compliance, Information Security) align with regulatory expectations.

## 5. Top Use Cases

- **UC-02** - ITGC finding in 5-part observation format

## 6. Pain Points

- SOX 404 scoping: determining which ITGC/ITAC affect ICFR
- Third-party risk: FFIEC expectations for vendor oversight
- Control rationalization: maintaining one underlying control set with multiple framework views
- Audit cycle alignment: COBIT maturity assessments vs annual SOX testing

## 7. References

- FFIEC IT Examination Handbook
- 23 NYCRR 500 (NYDFS Cybersecurity)
- 16 CFR Part 314 (GLBA Safeguards Rule)
- COBIT 2019: Focus Area guides for risk management and compliance
