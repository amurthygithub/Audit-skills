# Industry: SaaS / Cloud-Native Technology

SaaS companies delivering multi-tenant products need ISACA methodology for SOC 2 readiness, COBIT maturity assessments, and ITGC/ITAC testing for customer assurance.

## 1. Posture

| Variant | Typical Audit Drivers | Frameworks |
|---------|----------------------|------------|
| B2B SaaS (commercial) | SOC 2 Type II, ISO 27001 | COBIT APO13 (Managed Security), ITGC |
| B2B SaaS (FedRAMP-bound) | FedRAMP authorization, 800-53 | COBIT + NIST cross-reference |
| B2B SaaS (healthcare) | HIPAA Business Associate | COBIT DSS05, APO14 |
| B2B SaaS (fintech) | SOC 2 + SOX readiness | ITGC testing (all categories) |

## 2. Boundary

Multi-tenancy drives boundary complexity. The SaaS product is the system; tenant isolation (logical or physical) is a key ITGC control. Identity federation (SAML/OIDC) from customer IdP is common.

## 3. Inheritance Pattern

SaaS companies inherit physical/environmental controls from hyperscaler (AWS, Azure, GCP). Application-layer controls (AC-2 app accounts, AU-2 app events, SC-13 crypto) are SaaS-implemented. COBIT BAI objectives guide SDLC and change management.

## 4. Regulator/Customer Relationship

Customers impose SOC 2, ISO 27001, or custom audit requirements. COBIT 2019 maturity assessments are increasingly requested by enterprise buyers. The SaaS company's CISO typically acts as audit owner.

## 5. Top Use Cases

- **UC-01** - SaaS COBIT 2019 maturity assessment
- **UC-02** - ITGC finding in 5-part observation format

## 6. Pain Points

- Multi-tenant control inheritance: documenting what the SaaS inherits vs implements
- SOC 2 + COBIT + ISO 27001 stack: audit scope creep from multiple frameworks
- Continuous monitoring bandwidth: SOC 2 annual + customer audits + maturity assessments
- Application-layer controls: hyperscaler package does not cover app-layer
- COBIT maturity scoring: distinguishing "ad hoc" from "repeatable" in startup environments

## 7. References

- COBIT 2019: Focus Area for Cloud Computing
- Cloud Controls Matrix (CSA CCM v4)
- AICPA SOC 2 + COBIT crosswalks
- ISACA IT Audit Programs for cloud services
