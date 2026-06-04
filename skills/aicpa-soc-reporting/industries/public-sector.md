# Industry: Public Sector / Government Technology

## 1. Posture

Public sector organizations and gov-tech vendors use SOC reports primarily as complementary evidence for FedRAMP authorizations or as a bridge to NIST 800-53. SOC 2 is increasingly accepted by federal agencies as part of vendor due diligence. State and local governments may accept SOC 2 as primary evidence of security controls.

| Scenario | SOC Type | Relationship to FedRAMP/NIST |
|----------|----------|------------------------------|
| Gov-tech SaaS (federal customer) | SOC 2 Type II | Complements FedRAMP authorization; SOC 2 may accelerate agency ATO |
| State/local government SaaS | SOC 2 Type II | Often accepted as primary security evidence; no FedRAMP requirement |
| Federal contractor (non-CSP) | SOC 2 Type II | NIST 800-171/CMMC primary; SOC 2 as supplementary |
| Public cloud service offering | SOC 2 Type II + FedRAMP | FedRAMP is the primary authorization; SOC 2 supports commercial customers |

## 2. Boundary

The system boundary for SOC 2 is typically narrower than the FedRAMP authorization boundary. SOC 2 focuses on the commercial service offering; FedRAMP covers the entire cloud service stack.

## 3. Subservice Organizations

- IaaS provider: Carve-out. The FedRAMP-authorized IaaS provider's package provides inheritance.
- Identity provider (Login.gov, etc.): Carve-out if FedRAMP authorized.

## 4. Regulatory Overlay

- FedRAMP Authorization Act (44 USC 3609 et seq.)
- OMB A-130
- NIST SP 800-53 Rev 5
- FIPS 199 (categorization)
- CMMC 2.0 (for defense contractors)

## 5. Top Use Cases
- UC-02: CUEC/CSOC identification (adapted for gov-tech boundary)

## 6. Pain Points

- SOC 2 / FedRAMP boundary mismatch: The SOC 2 system description may not align with the FedRAMP authorization boundary. Managing two descriptions creates audit complexity.
- Evidence reuse: Can SOC 2 evidence be reused for FedRAMP? Sometimes, but the assessment rigor differs.
- CUEC in government context: Government user entity controls (e.g., agency security policies) are often mandatory but poorly documented.
- Dual audit timing: Managing SOC 2 annual cycle alongside FedRAMP continuous monitoring.

## 7. References
- AICPA TSP Section 100 (2017 TSC)
- FedRAMP Authorization Boundary Guidance
- NIST SP 800-53 Rev 5
- OMB A-130
