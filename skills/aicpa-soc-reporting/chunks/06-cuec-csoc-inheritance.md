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
5. The service auditor does not TEST CUECs (they operate at user entities), but DOES evaluate whether the disclosed CUECs are relevant and complete as part of assessing the fairness of the description. The report states that the criteria are met only if CUECs operate effectively at user entities.

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
5. Service auditor tests ONLY the service organization's controls, NOT CSOCs. Under carve-out, CSOCs are not tested at all — REPORT USERS must evaluate them by obtaining the subservice organization's own SOC report (check scope, period coverage, and exceptions there).
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

Step 2: Which presentation method does MANAGEMENT elect? (This is management's description-presentation
decision, not the practitioner's evidence call.)
  -> INCLUSIVE method.
     Advantages: More comprehensive report; no CSOC gap for users.
     HARD REQUIREMENTS: the subservice organization's management must provide its own written assertion
     and representations, its description is included in scope, and its controls are tested directly.
     Best when: subservice org is closely related/cooperative and will sign an assertion (rare for
     hyperscalers — AWS/Azure/GCP will not).
  -> CARVE-OUT method (the default in practice).
     Requirements: disclose the subservice org and the CSOCs; management assumes subservice controls effective.
     Limitations: practitioner does NOT test subservice controls; report users evaluate CSOC coverage via
     the subservice org's own SOC report.
     Best when: the subservice org has its own SOC report users can obtain (the standard hyperscaler case).

Step 3: Document the decision in system description.

Step 4: Impact on practitioner's report:
  Inclusive -> Opinion covers subservice organization controls.
  Carve-out -> Opinion excludes subservice org controls; CSOCs assumed but not tested.

Always ask whether subservice organizations exist before drafting the system description. List common types (cloud IaaS, payment processors, CDNs, email services, managed security services) and ask if any are used.

## Citations
- [AT-C-205] [AT-C-320]
See SKILL.md Section 10.
