# Industry: Financial Services (commercial)

Commercial financial services (banks, insurance, capital markets, payments, fintech) often have a robust SOC 2 baseline but need to **map to NIST 800-53** when:

- They are a federal contractor or subcontractor processing federal data (e.g., a bank that processes Treasury disbursements, a fintech that processes USDA payments).
- They serve federal customers and need to support a customer's FedRAMP or agency ATO.
- The board or risk committee wants a comprehensive control framework beyond SOC 2 / TSC.
- They are pursuing a DoD contract (CMMC 2.0) — CMMC references NIST 800-171, which references 800-53.
- They serve a regulated industry that cross-references 800-53 (e.g., financial services regulators' expectations on third-party risk).

## 1. Posture

| Sub-sector | Typical categorization | Baseline | Why 800-53 |
|------------|------------------------|----------|------------|
| Commercial bank — consumer-facing | High (if PII at scale) or Moderate | Mod/High | Federal contract; board-level third-party risk program |
| Insurance carrier | Moderate | Mod | State insurance regulator references; large federal contract exposure |
| Capital markets / broker-dealer | Moderate or High | Mod/High | FINRA / SEC examination; federal contract exposure |
| Payments / fintech | High (PCI-DSS scope + PII) | High (when federal) | Federal contract; PCI overlay; large PII volume |
| RegTech / compliance SaaS | Moderate (FedRAMP-bound variants) | Mod | Selling to federal agencies; FedRAMP authorization unlocks federal market |
| Custodian / trust bank | High | High | Fiduciary responsibility; federal contract exposure; PII at scale |

## 2. Boundary

- For most commercial entities, the "system" is whatever product or service is in scope of a federal contract. A bank may run multiple systems: a core banking platform, a customer-facing mobile app, a back-office analytics system. Each may have a separate authorization boundary.
- The 800-53 application is **overlay-only** — it does not replace SOC 2, PCI-DSS, or HIPAA Security Rule. The 800-53 view is the crosswalk; the underlying controls are still tested per their native framework.

## 3. Inheritance pattern

- **Inheritance depends on the deployment model**: a traditional bank running its own data centers/colocation has no native cloud inheritance, while a cloud-hosted fintech (like UC-03's AWS SaaS) inherits the provider's physical/environmental/hypervisor controls — see chunks/04 §Common control & inheritance model.
- **FedRAMP inheritance possible** if the entity uses a FedRAMP-authorized IaaS/PaaS (e.g., AWS GovCloud, Azure Government). Otherwise, the entity implements controls at the cloud layer.
- **Third-party (SOC 2, ISO 27001) inheritance** — common controls (e.g., HR, training, vendor risk) can be inherited from the corporate common-controls catalog and reused in the 800-53 view.

## 4. Regulator / customer relationship

- **No federal AO** unless the entity is a federal contractor. The entity's "AO" is typically a senior risk officer (CRO, CISO) who signs the 800-53 mapping memo.
- **Regulators** (OCC, FDIC, FRB, state insurance, SEC, FINRA) impose their own expectations (FFIEC IT Examination Handbook, NYDFS 23 NYCRR 500, etc.). The 800-53 mapping supports but does not replace these.
- **Customers** (federal agencies) may require a 800-53 mapping as part of a procurement or a system interconnection agreement.

## 5. Top use cases

- **UC-03 — Enterprise fin-svcs maps SOC 2 → 800-53 Moderate** (`use-cases/uc-03-soc2-to-800-53.md`)

## 6. Pain points (fin-svcs)

- **Two control libraries, one operating model** — the entity must maintain both SOC 2 controls and the 800-53 mapping. The crosswalk is a one-time investment that pays back only if it is integrated with the control testing program.
- **Mapping the unmappable** — SOC 2's CC series (Common Criteria) is a coarse-grained set; 800-53 has ~325 controls at Moderate. The entity must either (a) implement many 800-53 controls above the SOC 2 baseline or (b) document "compensating" or "N/A" with strong rationale. The latter is the common path.
- **Privacy and GLBA** — GLBA Safeguards Rule (16 CFR Part 314) requires a comprehensive information security program. 800-53 covers this; SOC 2 covers less of it explicitly. The 800-53 view supports the GLBA program.
- **Third-party risk** — FFIEC and NYDFS expect a third-party risk program; the 800-53 SR family (Supply Chain Risk Management, added in Rev 5) supports this.
- **Audit scope creep** — a SOC 2 + 800-53 + ISO 27001 + PCI + HIPAA stack can quickly expand audit scope. Use a single underlying control set with multiple framework views.

## 7. References

- AICPA Trust Services Criteria 2017 (SOC 2)
- ISO/IEC 27001:2022
- PCI DSS v4.0
- 16 CFR Part 314 (GLBA Safeguards Rule)
- FFIEC IT Examination Handbook
- 23 NYCRR 500 (NYDFS Cybersecurity)
- NIST SP 800-53 Rev 5 / 5.1.1
- NIST SP 800-171 Rev 2 / Rev 3 (for CUI scenarios)
- 32 CFR Part 2002 (CUI)
