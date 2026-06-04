# Industry Index -- aicpa-soc-reporting

Each industry view shows SOC reporting posture, typical boundary, subservice patterns, regulator/customer relationship, top use cases, and pain points.

| Industry | File | Top use cases | Notes |
|----------|------|---------------|-------|
| Multi-tenant SaaS / cloud-native technology | saas-technology.md | UC-01, UC-02 | SOC 2 Type II is table-stakes; common carve-out for IaaS provider |
| Financial services (banks, fintech, payment processors) | financial-services.md | UC-01 | SOC 1 for ICFR; SOC 2 for security/availability; FFIEC/GLBA overlay |
| Healthcare (BAA-covered health-tech, payer, provider) | healthcare.md | UC-01 | SOC 2 + HITRUST; HIPAA Security Rule; Privacy criteria typically in scope |
| Public sector / gov-tech | public-sector.md | UC-02 | FedRAMP mapping; SOC 2 as complementary to FedRAMP authorization |

## How industries are modeled

1. Posture -- typical SOC type (SOC 1/2/3) and TSC categories.
2. Boundary -- what is "the system" in this context.
3. Subservice organization pattern -- IaaS, PaaS, payment processors, etc.
4. Regulator / customer relationship -- which entities request the SOC report and why.
5. Top use cases -- links to `use-cases/`.
6. Pain points -- what auditors and service organizations get wrong in this industry.
7. References -- industry-specific guidance.
