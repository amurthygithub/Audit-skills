# Industry: Public Sector (federal civilian agency & federal SaaS / FedRAMP)

The public sector is the **native habitat** of NIST 800-53 / RMF. This industry view covers two related but distinct contexts:

- **Federal civilian agency** — an agency (e.g., Treasury, HHS, DHS component) operates the system under FISMA, with an internal or shared AO.
- **Federal SaaS / FedRAMP-bound cloud service offering** — a service provider (CSP) seeks a FedRAMP authorization (sponsored by an agency) so the offering can be reused across agencies.

## 1. Posture

| Context | Typical categorization | Baseline | Inheritance |
|---------|------------------------|----------|-------------|
| Federal civilian agency — enterprise IT (HR, finance, email) | Moderate | 800-53 Rev 5 Mod | Limited — agency-specific data center; common controls may be at agency level |
| Federal civilian agency — public-facing transaction system (tax filing, benefits application) | Moderate or High | Mod/High | Often partly inheriting from a FedRAMP-authorized PaaS/SaaS (e.g., Login.gov, cloud.gov) |
| Federal SaaS (CSP) — Low-impact SaaS (e.g., internal collaboration) | Low | FedRAMP Low | High — most controls inherited from hyperscaler (AWS, Azure, GCP FedRAMP-authorized offerings) |
| Federal SaaS (CSP) — general-purpose SaaS (e.g., case management, HR) | Moderate | FedRAMP Moderate | High — most controls inherited from hyperscaler; the CSP implements application-layer and configuration-level controls |
| Federal SaaS (CSP) — high-impact SaaS (e.g., law-enforcement data, financial systems, PII at scale) | High | FedRAMP High | Moderate — even on a High-authorized hyperscaler, the CSP must implement most application-layer controls and a meaningful set of system-specific controls |

## 2. Boundary

- **Agency context:** the system is bounded by the agency's authorization boundary. All sub-systems and applications that share a security posture are typically in-scope. Common controls (org-wide) live in a separate authorization or are referenced from the system's SSP.
- **CSP / FedRAMP context:** the system is the CSP's offering as deployed in the cloud. The boundary is documented in the SSP with a network diagram, data-flow diagram, and a customer responsibility matrix (CRM) that lists which controls the customer (agency) is responsible for versus which the CSP inherits.

## 3. Inheritance pattern (CSP / FedRAMP)

| Control family | Hyperscaler-inherited | CSP / customer responsibility |
|----------------|-----------------------|------------------------------|
| AC-2 Account management | Partial (IAM roles, federated identity) | Application-layer accounts, service accounts, agency admins |
| AU-2 Auditable events | Partial (cloud-level audit logs) | Application events, business logic events, retention |
| CM-2 Baseline configuration | Most (cloud-side baselines) | Application CI/CD, configuration drift detection |
| IA-2 Identification & auth | Partial (cloud IAM) | Application MFA, agency SSO via SAML/OIDC |
| SC-7 Boundary protection | Most (VPC, security groups) | Application-layer WAF rules, API gateway |
| SC-13 Cryptographic protection | Most (KMS, HSM) | Application use of crypto modules (FIPS 140-3 validated) |
| SI-2 Flaw remediation | Partial (cloud patching) | Application patching, dependency scanning |
| IR-4 Incident handling | Partial (cloud-side detection) | Application incident triage, customer notification |
| RA-5 Vulnerability monitoring | Partial (cloud-side scans) | Application-layer scans, dependency scans, container scans |

**Always document the inheritance in the SSP §8 / §10 and the CRM.** The 3PAO will sample inherited controls against the cloud provider's package; the CSP will be tested on customer-responsibility controls.

## 4. Regulator / customer relationship

- **Agency context:** the AO is a designated agency official (often the CIO or a senior executive). The agency's Office of Inspector General (OIG) audits FISMA compliance annually. The system's authorization package is reviewed by the AO at issuance and re-reviewed annually.
- **CSP / FedRAMP context:** the CSP is sponsored by an agency that consumes the service. The FedRAMP PMO reviews the package. Once authorized, the package is published to the FedRAMP Marketplace and any federal agency can issue its own ATO inheriting from the FedRAMP authorization. The CSP must operate a continuous monitoring program (ConMon) — monthly vulnerability scans, annual assessment, POA&M management, significant-change notifications.

## 5. Top use cases

- **UC-01 — FedRAMP-bound SaaS categorizes FIPS-199 Moderate** (`use-cases/uc-01-fedramp-moderate.md`)
- **UC-02 — Federal agency Step 6 authorization with SAR and POA&M** (`use-cases/uc-02-agency-ato.md`)

## 6. Pain points (federal / FedRAMP)

- **Boundary clarity** — drawing the line between hyperscaler, CSP, and agency. Document the boundary in the SSP and the CRM.
- **Inheritance vs. assumption** — the CSP must not assume a control is inherited without explicit citation. If the hyperscaler's FedRAMP package says "customer responsibility" for a control, the CSP must implement it.
- **Continuous monitoring bandwidth** — ConMon is real work. Annual assessment, monthly scans, significant change review, POA&M updates. Build the operating model before authorizing.
- **POA&M risk acceptance vs. remediation** — FedRAMP does not allow indefinite risk acceptance. POA&M items have a remediation date and a status; items past their date are subject to escalation.
- **Privacy (Rev 5)** — the privacy control family (PT) is sometimes overlooked. If the system processes PII, the PT controls apply, and a PIA may be required.
- **PII inventory and data flow** — the agency's or CSP's data inventory must support the categorization and the privacy assessment.



## State RMF variants

Several states have adopted RMF-based frameworks that are **adaptations** of the federal NIST 800-53 / RMF process — not separate frameworks — tailored to state IT environments:

- **CA SAM (State Administrative Manual)** — California's SAM §5300-series incorporates NIST 800-53 controls with state-specific overlays for agencies under the California Department of Technology.
- **TX DIR (Texas Department of Information Resources)** — Texas DIR Security Control Standards Catalog (SCSC) maps to 800-53 Rev 4/Rev 5 with state-specific modifications. See the DIR Security and Risk Management Framework.
- **TX-RAMP** — Texas Risk and Authorization Management Program mirrors FedRAMP for cloud services used by Texas state agencies, using 800-53 as the underlying control catalog with state-specific overlays.

These state adaptations share the core 800-53 control families and RMF process but have unique authorization boundaries, AO designations, and assessment cadences. Consult the state's authoritative publication for the specific overlay and process. [NIST-SP-800-53-Rev5]

**For the non-federal authorization *mechanics*** — who risk-accepts absent a federal AO (a state CISO / agency head / designated authorizing authority), resource-constrained risk-based scoping for small shops (family prioritization, sampling, prior-evidence reuse, multi-year rotation), and the non-federal authorization-decision report shape — see **`chunks/10-non-federal-adoption.md`**. This industry view (above) covers the **federal / FedRAMP** posture; chunk 10 covers the state/local & non-federal adoption model.

## 7. References

- NIST SP 800-37 Rev 2 — RMF
- NIST SP 800-53 Rev 5
- FedRAMP Authorization Act (44 USC §3609 et seq.) and FedRAMP Authorization Boundary Guidance
- OMB A-130 — Managing Information as a Strategic Resource
- OMB Memo M-24-15 — Modernizing the Federal Risk and Authorization Management Program (FedRAMP)
- FedRAMP Continuous Monitoring Strategy Guide
- NIST SP 800-66 Rev 2 — HIPAA Security Rule (if the system processes PHI)
- 32 CFR Part 2002 — Controlled Unclassified Information (CUI) (if applicable)
- NIST SP 800-171 Rev 2 / Rev 3 (if non-federal systems processing CUI)
