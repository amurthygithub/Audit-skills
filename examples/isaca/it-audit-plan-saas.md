# Example: ISACA IT Audit Plan for SaaS Company

**Skill**: isaca-audit-methodology
**Scenario**: You are an IT audit manager planning a COBIT 2019-based IT audit for "CloudPay Inc.", a mid-market SaaS payment processing company ($200M ARR, 500 employees).

---

## Prompt

```
I need to plan an IT audit for CloudPay Inc., a SaaS payment processing company.
They process $2B in annual transactions, use AWS/Azure multi-cloud, and have
recently deployed GenAI for customer support chatbots. 

Please help me:
1. Select the COBIT 2019 governance and management objectives in scope
2. Build the audit risk assessment using Risk IT
3. Design the ITGC testing program
4. Plan the ITAC testing for the payment processing application
5. Determine the audit approach (substantive vs controls-reliance)
```

## Expected Agent Output Structure

### 1. COBIT 2019 Scoping (§4.1-4.6)

The agent should apply the COBIT 2019 goals cascade:

- **Enterprise Goals**: EG01 (Stakeholder value), EG04 (Business continuity), EG08 (Compliance with external laws)
- **Alignment Goals**: AP01 (IT-related business goals), AP04 (Managed availability/capacity), AP06 (Managed compliance)
- **Governance Objectives**: EDM01 (Governance framework), EDM03 (Compliance), EDM05 (Portfolio)
- **Management Objectives**: APO01 (IT management framework), APO12 (Managed risk), APO13 (Managed security), BAI06 (Managed IT changes), BAI09 (Managed assets), DSS01 (Operations), DSS05 (Security), MEA01 (Performance), MEA02 (Internal compliance)

### 2. Risk Assessment (§10.1)

The agent should use the Risk Score formula:

| ID | Risk | Likelihood | Impact | CRF | Risk Score | Priority |
|----|------|-----------|--------|-----|-----------|----------|
| R1 | Data breach — payment card data | 4 | 5 | 1.5 (Weak access controls) | 30 | Critical |
| R2 | Cloud misconfiguration — data exposure | 3 | 5 | 1.0 (Moderate controls) | 15 | High |
| R3 | GenAI data leakage — customer PII in prompts | 4 | 4 | 2.0 (No controls) | 32 | Critical |
| R4 | Unauthorized code deployment (no change management) | 3 | 4 | 1.5 (Partial controls) | 18 | High |
| R5 | RPO/RTO failure — disaster recovery | 2 | 5 | 1.0 (Tested annually) | 10 | Medium |

### 3. ITGC Testing Program (§6.4)

The agent should structure ITGC testing across:

**Access Management (APO13, DSS05)**:
- Test user provisioning/deprovisioning for AWS, Azure, ERP, payment gateway
- Sample: Last 25 terminations — verify access removed within 24 hours
- Test quarterly access review for privileged accounts

**Change Management (BAI06)**:
- Test change request → approval → deployment → post-impl review cycle
- Sample: 25 changes in last 6 months
- Verify emergency change procedures and documentation

**IT Operations (DSS01)**:
- Test backup completion and restoration testing
- Verify monitoring/alerting for critical systems
- Review incident response procedures and SLAs

**Physical/Environmental**: Out of scope (cloud-hosted)

### 4. ITAC Testing (§6.5)

For the payment processing application:

| Application Control | Test Procedure | Sample | Assertion |
|---------------------|---------------|--------|-----------|
| Three-way match (PO/GRN/Invoice) | Re-perform match for 25 transactions | 25 | Completeness, Accuracy |
| Credit limit validation | Test boundary: at limit, over limit | Boundary | Existence |
| Duplicate payment detection | Run duplicate check on 1,000 payments | 1,000 | Occurrence |
| Automated reconciliation | Verify reconciliation config and re-perform | 5 instances | Completeness |

### 5. Audit Approach Decision (§13)

```
IF ITGC assessments = Effective AND ITAC testing feasible AND population size > 500
  → CONTROLS-RELIANCE approach
  → Reduced substantive testing (sample from ITAC-relied controls)
ELSE
  → SUBSTANTIVE approach
  → Full substantive testing required

CURRENTPAY ASSESSMENT:
  ITGC: Access management = Ineffective (CRF 1.5), Change management = Partially effective
  → ITGC NOT fully effective → CANNOT rely on ITAC
  → APPROACH: SUBSTANTIVE with modified scope
  → Increase substantive sample sizes per AS 2315
```

---

## Key Agent Behaviors to Verify

1. **Risk formula applied correctly**: Risk Score = (Likelihood × Impact) × CRF, not just L×I
2. **COBIT objectives traceable**: Each objective linked via goals cascade
3. **ITGC→ITAC dependency enforced**: Agent refuses ITAC-reliance when ITGC ineffective
4. **GenAI risk addressed**: Agent applies emerging technology guidance (§21)
5. **Anti-hallucination rule**: Agent does NOT cite fabricated ITAF standard numbers