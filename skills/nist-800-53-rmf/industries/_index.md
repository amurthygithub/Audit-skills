# Industry Index — nist-800-53-rmf

Every published skill in this library carries industry views that show how the skill is applied in a specific industry context. Each view lists: the typical FIPS 199 posture, the dominant inheritance pattern, the system boundary characteristics, the customer/regulator relationship, the most common pain-points, and the linked use cases.

| Industry | File | Top use cases | Notes |
|----------|------|---------------|-------|
| Federal SaaS (FedRAMP-bound) | public-sector.md | UC-01 | Cloud service offering seeking FedRAMP authorization; typical Moderate or High baseline; large inheritance from hyperscaler (AWS, Azure, GCP) |
| Federal civilian agency | public-sector.md | UC-02 | On-prem or agency-operated system; tight AO accountability; no FedRAMP marketplace publication; agency-tailored RMF |
| Commercial financial services | financial-services.md | UC-03 | SOC 2 baseline already in place; mapping to 800-53 for federal customers or board risk view |
| Healthcare payer / provider | healthcare.md | (planned UC-04) | HIPAA Security Rule baseline; crosswalk to 800-53 for federal grants or contracts; CUI overlay possible |
| SaaS / cloud-native technology | saas-technology.md | UC-01, UC-03 | Multi-tenant SaaS; FedRAMP-bound variants and commercial variants; inheritance from hyperscaler |

## How industries are modeled in this skill

For each industry, the file in this folder follows the same shape:

1. **Posture** — typical FIPS 199 categorization and the dominant baseline.
2. **Boundary** — what is "the system" in this context (a single agency system, a multi-tenant SaaS, a service org's offering).
3. **Inheritance pattern** — what is typically inherited from a cloud provider, what is system-specific, what is hybrid.
4. **Regulator / customer relationship** — AO relationship, customer-required overlay (FedRAMP, DoD IL4/IL5/IL6, CMMC).
5. **Top use cases** — links to `use-cases/`.
6. **Pain points** — what auditors and system owners get wrong in this industry.
7. **References** — industry-specific guidance documents.
