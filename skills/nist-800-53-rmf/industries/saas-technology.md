# Industry: SaaS / Cloud-Native Technology

A "SaaS / cloud-native technology" entity is a software company that delivers its product as a multi-tenant service. This is a broad industry that overlaps with **public-sector** (when the SaaS is FedRAMP-bound), **financial services** (when the SaaS serves banks), **healthcare** (when the SaaS processes PHI), and others. This file captures the industry-specific 800-53 posture that is **common across SaaS** regardless of the vertical served.

## 1. Posture

| Variant | Typical categorization | Baseline | Inheritance |
|---------|------------------------|----------|-------------|
| B2B SaaS, commercial customers only | Not 800-53-bound | — | None — start with SOC 2 / ISO 27001; return to 800-53 only when a federal contract or customer demand requires it |
| B2B SaaS with federal customers (FedRAMP-bound) | Moderate or High | FedRAMP Mod/High | High — most controls inherited from hyperscaler |
| B2B SaaS with DoD customers (CMMC-bound) | Depends on CUI category | 800-171 (L1–L3) | Moderate — hyperscaler with DoD IL4/IL5 (Azure Government, AWS GovCloud) |
| B2B SaaS with healthcare customers (PHI processing) | Moderate or High | HIPAA Security Rule + 800-53 crosswalk | Variable — if the SaaS is a BAA-covered business associate, the HIPAA controls apply; 800-53 is a crosswalk, not the native framework |
| B2B SaaS in financial services (fintech SaaS) | Moderate or High | SOC 2 + 800-53 crosswalk | Variable — depends on whether federal contracts exist |

## 2. Boundary

- The system is the SaaS product as deployed in the cloud. Multi-tenancy means the security boundary must be explicit:
  - **Tenant isolation** — logical (per-tenant DB schema, row-level security) or physical (per-tenant DB).
  - **Identity** — federated identity (SAML, OIDC) from the customer's IdP; service-provider accounts for admins.
  - **Data residency** — region pinning (US-only, EU-only) where required.
- The boundary document is critical for the SSP. The network diagram, the data-flow diagram, and the customer responsibility matrix (CRM) all live in the SSP §1 / §8.

## 3. Inheritance pattern

The typical SaaS inheritance pattern is:

| Layer | Owns | Inherits |
|-------|------|----------|
| Hyperscaler (AWS, Azure, GCP) | Physical, environmental, network baseline, KMS, hypervisor, IAM service (configuration remains customer responsibility) | — |
| Platform (Kubernetes, OS, container runtime) | Configuration management, vulnerability scanning, OS hardening (or shared) | Hyperscaler layers below |
| Application (the SaaS) | All app-layer controls (AC-2 app accounts, AU-2 app events, SC-13 crypto use, SI-10 input validation) | Physical/environmental/network/KMS from the hyperscaler; platform hardening from the platform layer |

The common mistake is to assume inheritance that doesn't exist. The hyperscaler's FedRAMP package lists which controls the customer inherits; if a control is on the customer-responsibility list, the SaaS must implement it.

## 4. Regulator / customer relationship

- **No federal AO** unless the SaaS is FedRAMP-bound or DoD-bound. The SaaS's "AO" is the CISO or VP Engineering.
- **Customers** may impose their own 800-53 requirements (e.g., a federal customer requires the SaaS to map controls and provide a SOC 2 + 800-53 crosswalk).
- **Sub-processors** — the SaaS inherits some controls from its sub-processors (e.g., Auth0 for identity, Datadog for monitoring, Snowflake for analytics). The SaaS's vendor risk management program is the SOC 2 + 800-53 SR family in action.

## 5. Top use cases

- **UC-01 — FedRAMP-bound SaaS categorizes FIPS-199 Moderate** (`use-cases/uc-01-fedramp-moderate.md`)
- **UC-03 — Enterprise fin-svcs maps SOC 2 → 800-53** (`use-cases/uc-03-soc2-to-800-53.md`)

## 6. Pain points (SaaS)

- **Multi-tenant inheritance** — the SaaS is both a customer of the hyperscaler (inherits) and a service provider to its customers (whom it provides inheritance to). Both directions must be documented.
- **Application-layer controls** — the hyperscaler's package does not cover app-layer controls. The SaaS must implement and test these itself; the 3PAO will sample heavily here.
- **CMMC, FedRAMP, and ISO 27001 in parallel** — many SaaS companies pursue all three. The 800-53 view is the underlying catalog; the other frameworks are crosswalks.
- **Continuous monitoring** — FedRAMP ConMon is monthly vulnerability scanning, annual assessment, POA&M management. This is a significant operating cost; budget for it before authorizing.
- **Customer responsibility matrix drift** — the CRM is a living document. When the SaaS adds a feature, the CRM changes; the new control must be tested in the next annual assessment.
- **Bring Your Own Key (BYOK)** — a customer wanting to hold the encryption keys changes the SC-13 / SC-12 / SC-17 inheritance model. Document this as a special configuration.

## 7. References

- FedRAMP Authorization Boundary Guidance
- FedRAMP Customer Responsibility Matrix templates
- NIST SP 800-53 Rev 5 / 5.1.1
- NIST SP 800-218 (Secure Software Development Framework — SSDF)
- Cloud Controls Matrix (CSA CCM v4)
- SOC 2 + 800-53 crosswalk — see `data/crosswalks/soc2-to-800-53-mod.json`
- AICPA SOC 2 + CMMC crosswalks
