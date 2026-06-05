# Industry: Public Sector

Federal agencies, state/local governments, and government contractors adopting FISMA, FedRAMP, or FISMA-aligned state regulations often use COBIT 2019 for IT governance alongside NIST 800-53 for security controls.

## 1. Posture

| Context | Audit Drivers | Frameworks |
|---------|-------------|------------|
| Federal civilian agency | FISMA, OMB A-130, agency OIG audits | COBIT EDM governance + NIST 800-53 |
| Federal system (on-prem) | FISMA annual assessment | COBIT APO13, DSS05 + NIST 800-53 |
| State/local government | State FISMA-aligned regulations | COBIT governance + NIST CSF 2.0 |
| Government contractor | CMMC 2.0, DFARS 252.204-7012 | COBIT maturity + NIST 800-171 |

## 2. Boundary

Agency authorization boundaries drive audit scope. The system is defined by the SSP (System Security Plan). COBIT governance objectives map to agency-level IT governance committees and CIO oversight.

## 3. Inheritance Pattern

Common controls are shared across the agency. System-specific controls are implemented by the system owner. COBIT EDM05 (stakeholder transparency) supports FISMA reporting requirements.

## 4. Regulator/Customer Relationship

The Authorizing Official (AO) is a designated agency executive. The OIG audits FISMA compliance annually. The FedRAMP PMO reviews cloud service offerings. COBIT MEA03 (compliance) maps to ongoing FISMA assessment.

## 5. Top Use Cases

- **UC-01** - COBIT 2019 maturity assessment (agency governance)

## 6. Pain Points

- Two frameworks: NIST 800-53 for security + COBIT for governance; agencies often struggle to integrate both
- Authorization boundary: drawing the line between common controls and system-specific controls
- Continuous monitoring: FISMA annual assessment + quarterly POA&M reporting
- COBIT maturity: agencies often rate low on COBIT due to bureaucratic process constraints, not capability gaps

## 7. References

- NIST SP 800-37 Rev 2 (RMF)
- NIST SP 800-53 Rev 5/5.1.1
- FIPS 199, FIPS 200
- OMB A-130
- FedRAMP Authorization Boundary Guidance
- COBIT 2019: Focus Area for Cybersecurity (NIST CSF 2.0 aligned)
