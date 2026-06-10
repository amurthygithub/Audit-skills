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

SaaS companies inherit physical/environmental controls from the hyperscaler (AWS, Azure, GCP) -- in COBIT terms, parts of DSS01 (Managed Operations) and the facility aspects of DSS05 are provider-side. The SaaS company implements the application layer itself: logical access and identity (DSS05.04), security-event monitoring of its stack (DSS05.07), data protection (APO14), and IT change control (BAI06/BAI07). ITGC testing scope follows this split: test the SaaS-implemented controls directly; cover inherited controls via the provider's SOC 2 report.

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

- Cloud Controls Matrix (CSA CCM v4, 17 domains)
- COBIT Focus Area: Information Security; COBIT 2019 for Small and Medium Enterprises (ISACA)
- AICPA SOC 2 + COBIT crosswalks
- ISACA Cloud Audit Program
