# Example: SOC 2 Type II Examination

**Skill**: aicpa-soc-reporting
**Scenario**: You are a service auditor planning a SOC 2 Type II examination for "DataVault Corp.", a cloud data storage provider handling customer PII and financial data.

---

## Prompt

```
Plan and document a SOC 2 Type II examination for DataVault Corp.
- Cloud data storage provider (SaaS)
- Handles customer PII and financial data
- Subject to GDPR and CCPA
- Uses AWS infrastructure with ISO 27001:2022 certification
- Examination period: January 1 - December 31, 2026
- Trust Services Categories: Security, Availability, Confidentiality

Provide the engagement plan, TSC criteria mapping, testing approach,
and draft management assertion and auditor opinion.
```

## Expected Agent Output Structure

### 1. Engagement Planning (§5)

- **Engagement type**: SOC 2 Type II (design AND operating effectiveness)
- **AT-C section**: AT-C 105 + AT-C 205
- **Categories in scope**: Security (CC6-CC9), Availability (A1.1-A1.3), Confidentiality (C1.1-C2.2)
- **Period**: January 1 - December 31, 2026
- **Service auditor**: [Firm name]

### 2. TSC Criteria Mapping (§7)

**Common Criteria (33 primary CC)**:

| CC | Title | COSO Principle(s) | Key Control |
|----|-------|--------------------|----|
| CC1.1 | Integrity/ethics | P1 | Code of conduct enforced |
| CC1.2 | Accountability | P5 | Role-based access accountability |
| CC1.3 | Organizational structure | P3 | Org chart, reporting lines |
| CC1.4 | Competence | P4 | Hiring/training program |
| CC1.5 | Board oversight | P2 | Board charter, quarterly reviews |
| CC2.1 | Quality information | P13 | Data quality controls |
| CC2.2 | Internal communication | P14 | Security awareness program |
| CC2.3 | External communication | P15 | Privacy notice, breach notification |
| CC3.1 | Objectives clarity | P6 | Security objectives documented |
| CC3.2 | Risk identification | P7 | Risk assessment process |
| CC3.3 | Fraud risk | P8 | Fraud risk assessment |
| CC3.4 | Change impact | P9 | Change management risk assessment |
| CC4.1 | Monitoring evals | P16 | Internal audit, penetration testing |
| CC4.2 | Deficiency communication | P17 | Incident response, reporting |
| CC5.1 | Control activities | P10 | Security controls selection |
| CC5.2 | IT controls | P11 | AWS security configuration |
| CC5.3 | Policy deployment | P12 | Information security policy |
| CC6.1-6.8 | Logical access | P10, P11 | IAM, MFA, SSO |
| CC7.1-7.4 | System operations | P10, P11 | Monitoring, incident detection |
| CC8.1-8.2 | Change management | P11 | CI/CD pipeline controls |
| CC9.1-9.2 | Risk mitigation | P10 | Third-party risk management |

**Additional Criteria**:
- **Availability**: A1.1 (backup/recovery), A1.2 (availability SLA), A1.3 (incident recovery)
- **Confidentiality**: C1.1 (confidential information identification), C1.2 (confidentiality commitments), C2.1 (confidentiality controls), C2.2 (data retention/disposal)

### 3. Testing Approach (§6)

**Test of Operating Effectiveness**:

| TSC Criterion | Test Procedure | Sample Size | Frequency |
|--------------|----------------|-------------|-----------|
| CC6.1 (Logical access) | Review IAM policies, test provisioning/deprovisioning | 25 changes | Monthly |
| CC6.2 (Registration/auth) | Test MFA enrollment, password policy | 25 users | Quarterly |
| CC6.3 (Role-based access) | Re-perform access review for privileged roles | All admin accounts | Quarterly |
| CC7.1 (System monitoring) | Review CloudWatch alerts, verify response | 25 incidents | Ongoing |
| CC8.1 (Change management) | Trace 25 changes through approval → deployment | 25 changes | Monthly |
| A1.1 (Backup/recovery) | Verify backup completion, test restoration | 12 months + 1 restore test | Monthly |
| C1.2 (Confidentiality) | Review DLP alerts, verify encryption | 25 DLP events | Ongoing |

### 4. Management Assertion (§9.1/9.2 template)

Per the AICPA skill's Type II template, management asserts:
- Description of system covers all 5 components per TSP Section 100
- Commitment addresses all 3 categories (Security, Availability, Confidentiality)
- Statement covers BOTH suitability of design AND operating effectiveness
- Covers the full 12-month period

### 5. Auditor Opinion (§15.2 decision tree)

```
IF no exceptions OR exceptions are not significant enough to warrant
   attention → UNQUALIFIED opinion
IF exceptions warrant attention but controls still achieve criteria
   → UNQUALIFIED with explanatory paragraph
IF controls did NOT achieve criteria → QUALIFIED opinion
IF unable to obtain sufficient evidence → DISCLAIMER

For compound issues (multiple exceptions):
  Assess EACH exception independently first
  THEN assess whether combined effect changes the opinion
  DOCUMENT combined assessment per QG10
```

### 6. Cross-References

**GDPR Mapping (§20.4)**:
- Art. 5(1)(b) Purpose limitation → CC3.1, C1.1
- Art. 5(1)(c) Data minimization → CC3.1, C1.2
- Art. 5(1)(f) Integrity/confidentiality → CC6.1, CC7.1
- Art. 32 Security of processing → CC6.1-6.8, CC7.1-7.4

**ISO 27001:2022 (§20.2)**:
- A.5 Organizational controls → CC1-CC5
- A.6 People controls → CC1.4, CC6.2
- A.7 Physical controls → CC6.1 (physical access component)
- A.8 Technological controls → CC6.3-6.8, CC7-CC8

---

## Key Agent Behaviors to Verify

1. **Terminology enforcement**: Uses "service auditor" (not "auditor"), "management assertion" (not "representation letter"), "Trust Services Criteria" (not "Principles")
2. **CC1.2→P5, CC1.5→P2**: Non-sequential COSO mapping preserved correctly
3. **GDPR article descriptions**: Art 5(1)(b) = purpose limitation, Art 5(1)(c) = data minimization (NOT transposed)
4. **Type II template**: Covers BOTH design AND operating effectiveness for the full period
5. **Compound issues**: Decision tree handles multiple exceptions with combined assessment
6. **No SAS 70 / SSAE 16 references**: Agent uses current AT-C standards only