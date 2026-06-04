---
chunk_id: 06-cuec-csoc-inheritance
parent_skill: aicpa-soc-reporting
topic: "CUEC and CSOC Identification Guidance, Inclusive vs Carve-out Method Decision Logic"
load_when: "user asks about CUECs, CSOCs, subservice organizations, inclusive method, carve-out method, or control dependencies"
---

# Chunk 06 -- CUEC and CSOC Identification

## Complementary User Entity Controls (CUECs)

Definition: Controls that user entities (customers) are expected to have in place for the service organization's controls to achieve their objectives.

### CUEC Identification (5 steps)
1. For each control objective or TSC criterion, ask: "Does this control depend on actions taken by the user entity?"
2. If YES, document the CUEC: state the specific action, explain why necessary, describe consequence if user entity does not implement it.
3. Common CUEC categories:
   - User access provisioning and maintenance (adding/removing users)
   - Data input validation before submission
   - Segregation of duties at user entity level
   - Review and approval of transactions processed by service org
   - Physical security of endpoints accessing service org's system
   - Customer-managed encryption key management
   - Incident notification to the service org
   - Business continuity planning at user entity level
   - Privacy notice and consent management at user entity level
4. CUECs must be disclosed in: Section II of SOC 1 and SOC 2 reports. NOT required in SOC 3 (abridged).
5. Service auditor has NO responsibility to evaluate suitability of CUECs. This must be stated.

## Complementary Subservice Organization Controls (CSOCs)

Definition: Controls at a subservice organization that management assumes are operating effectively under the carve-out method.

### CSOC Identification (6 steps)
1. Identify all subservice organizations (e.g., IaaS provider, payment processor, email service).
2. Determine presentation method (see below): carve-out -> identify CSOCs; inclusive -> test directly.
3. For carve-out, document CSOCs:
   - Identify subservice organization by name
   - Describe services provided
   - List controls at subservice org that management assumes effective
   - Explain how CSOCs relate to control objectives/criteria
4. CSOCs must be disclosed in: Section II of SOC 1/SOC 2 if carve-out method used.
5. Service auditor tests ONLY the service organization's controls, NOT CSOCs. Exceptions in CSOCs may affect opinion.
6. Common CSOC categories:
   - Infrastructure access controls at IaaS provider
   - Data center physical security (subservice data center)
   - Network security controls operated by cloud provider
   - Payment processing security controls
   - Encryption and key management at subservice level

## Inclusive vs Carve-out Decision Logic

Step 1: Does the service organization use subservice organizations?
  -> NO: Not applicable. No CSOCs needed.
  -> YES: Proceed to Step 2.

Step 2: Can practitioner obtain sufficient evidence about subservice organization's controls?
  -> YES: Consider INCLUSIVE method.
     Advantages: More comprehensive opinion, no CSOC gap.
     Requirements: Subservice org willing to be examined, description included in scope, controls tested directly.
     Best when: Subservice org has its own SOC report or is cooperative.
  -> NO: Use CARVE-OUT method.
     Advantages: Practical when subservice org is uncooperative or examination infeasible.
     Requirements: Must disclose CSOCs; management assumes subservice controls effective.
     Limitations: Practitioner does NOT test subservice controls; exceptions in CSOCs may affect opinion.
     Best when: Subservice org has its own SOC report user entity can review separately.

Step 3: Document the decision in system description.

Step 4: Impact on practitioner's report:
  Inclusive -> Opinion covers subservice organization controls.
  Carve-out -> Opinion excludes subservice org controls; CSOCs assumed but not tested.

Always ask whether subservice organizations exist before drafting the system description. List common types (cloud IaaS, payment processors, CDNs, email services, managed security services) and ask if any are used.

## Citations
- [AT-C-205] [AT-C-320]
See SKILL.md Section 10.
