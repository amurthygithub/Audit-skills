---
uc_id: UC-02
title: "CUEC/CSOC Identification for a Multi-Tenant SaaS"
industries: [saas-technology]
frameworks: [SOC-2-TSC-2017]
inputs:
  system_description: "Multi-tenant SaaS platform on AWS, uses Stripe for payments, SendGrid for email. 200 enterprise customers."
  tsc_categories: [Security, Availability, Confidentiality]
procedure:
  - "chunks/06-cuec-csoc-inheritance.md -- Step 1: Identify all subservice organizations (AWS, Stripe, SendGrid)."
  - "chunks/06-cuec-csoc-inheritance.md -- Step 2: Determine inclusive vs carve-out for each subservice org."
  - "chunks/06-cuec-csoc-inheritance.md -- Steps 3-6: Document CSOCs for carve-out orgs; identify CUECs for customer-facing controls."
  - "chunks/02-engagement-type-decision.md -- Confirm SOC 2 engagement type."
expected_outputs:
  subservice_list: "List of 3 subservice organizations with method (carve-out) and CSOCs for each."
  cuec_list: "At least 4 CUECs with specific control objective links."
  method_rationale: "Explanation of why carve-out was chosen (all three orgs have their own SOC reports)."
oracle:
  type: schema_match
  assertion: "Output contains >= 3 subservice organizations identified; >= 4 CUECs documented; each CSOC linked to a TSC criterion; carve-out rationale provided."
data_refs:
  - "data/seeds/uc-02-input.json (planned)"
tests:
  - "tests/test_oracle.py::test_uc_02_oracle (planned)"
status: stub
---

# UC-02 -- CUEC/CSOC Identification for a Multi-Tenant SaaS

## Scenario

PayFlow SaaS provides a payment processing platform on AWS. They use Stripe for payment gateway, SendGrid for transactional emails. 200 enterprise customers. Customers request a SOC 2 Type II.

## Walk-through

1. Identify Subservice Organizations (chunk 06 Step 1):
   - AWS (IaaS): compute, storage, networking
   - Stripe: payment processing
   - SendGrid: email delivery

2. Determine Method (chunk 06 Step 2): Management elects CARVE-OUT for all three — the standard election where each subservice org has its own SOC report users can obtain (hyperscalers/processors will not provide the written assertion the inclusive method requires).

3. Document CSOCs (chunk 06 Step 3):
   - AWS: Infrastructure access controls (IAM), data center physical security, network security (VPC, security groups), encryption at rest (KMS). Mapped to CC6.1, CC6.4, CC6.6, CC6.7.
   - Stripe: Payment processing security controls, PCI DSS compliance. Mapped to CC6.6, C1.2 (Processing Integrity is not in scope for this examination).
   - SendGrid: Email delivery infrastructure security. Mapped to CC6.1.

4. Document CUECs (chunk 06 CUEC Steps 1-3):
   - CUEC-01: User access provisioning -- customers must manage user accounts on the platform. Linked to CC6.2.
   - CUEC-02: Customer tenant authentication configuration -- customers must enforce SSO/MFA for their users. Linked to CC6.1.
   - CUEC-03: Segregation of duties -- customers must segregate initiator and approver roles. Linked to CC6.3 (role-based access considering segregation of duties).
   - CUEC-04: Incident notification -- customers must notify PayFlow of security incidents. Linked to CC7.3.
   - CUEC-05: Customer-managed encryption keys -- optional; customers may bring their own keys. Linked to CC6.6.

5. Impact on Report (chunk 06 Step 4): Carve-out -> Opinion excludes subservice controls; CSOCs assumed effective. Disclosed in Section II.

## Output Sample
```yaml
subservice_organizations:
  - name: AWS
    service: IaaS (compute, storage, networking)
    method: carve-out
    csocs:
      - {criterion: CC6.1, control: "AWS IAM access controls"}
      - {criterion: CC6.4, control: "AWS data center physical security"}
      - {criterion: CC6.6, control: "AWS VPC, security groups"}
  - name: Stripe
    service: Payment processing
    method: carve-out
    csocs:
      - {criterion: CC6.6, control: "Stripe payment security"}
      - {criterion: C1.2, control: "Stripe protection of confidential payment data"}
  - name: SendGrid
    service: Email delivery
    method: carve-out
    csocs:
      - {criterion: CC6.1, control: "SendGrid infrastructure security"}

cuecs:
  - {id: CUEC-01, criterion: CC6.2, description: "User access provisioning on the platform"}
  - {id: CUEC-02, criterion: CC6.1, description: "Customer tenant authentication configuration (SSO/MFA)"}
  - {id: CUEC-03, criterion: CC1.2, description: "Segregation of duties at user entity level"}
  - {id: CUEC-04, criterion: CC7.3, description: "Incident notification to service org"}
  - {id: CUEC-05, criterion: CC6.6, description: "Customer-managed encryption keys"}

method_rationale: "All three subservice organizations maintain independent SOC reports. Carve-out method applied to avoid duplicative testing and acknowledge practitioner's inability to directly test subservice controls."
```
