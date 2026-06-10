---
chunk_id: 07-opinion-lifecycle-sampling
parent_skill: aicpa-soc-reporting
topic: "CPA Opinion Types and Determination Logic, Complete Engagement Lifecycle, Sampling Guidance for Type II"
load_when: "user asks about SOC opinion types, qualified/adverse/disclaimer opinions, exception evaluation, engagement lifecycle phases, or Type II sampling"
---

# Chunk 07 -- Opinion Types, Engagement Lifecycle, Sampling

## Opinion Types

| Opinion | When Issued | Language |
|---------|-------------|----------|
| Unqualified (Clean) | Description fairly presented; controls suitably designed and operating effectively | "In our opinion, in all material respects..." |
| Qualified | Exceptions exist but limited in scope | "Except for the matters described... in all other material respects..." |
| Adverse | Controls not suitably designed or not operating effectively across engagement scope | "In our opinion, the description does not fairly present..." |
| Disclaimer | Practitioner unable to obtain sufficient evidence | "We were unable to obtain sufficient appropriate evidence..." |

## Opinion Determination (5-step)

Step 1: Was sufficient appropriate evidence obtained?
  -> YES: Proceed to Step 2.
  -> NO: Can more evidence be obtained through extended procedures?
     YES -> obtain, return to Step 1.
     NO -> Scope limitation: if the possible effects are material but NOT pervasive -> QUALIFIED opinion;
           if material AND pervasive -> DISCLAIMER OF OPINION (or withdraw). The materiality/pervasiveness
           axis governs every modification decision (AT-C 205).

Step 2: Are there exceptions in FAIR PRESENTATION of description?
  -> YES, material misstatement affecting entire description -> ADVERSE on description fairness.
  -> YES, limited to specific aspects -> QUALIFIED.
  -> NO: Proceed to Step 3.

Step 3: Are there exceptions in DESIGN SUITABILITY?
  -> YES, controls not suitably designed across ALL or most objectives -> ADVERSE.
  -> YES, limited to specific controls -> QUALIFIED.
  -> NO: Proceed to Step 4.

Step 4: (Type II only) Exceptions in OPERATING EFFECTIVENESS?
  -> YES, pervasive and affects multiple objectives -> ADVERSE.
  -> YES, limited to specific controls/periods -> QUALIFIED.
  -> NO: UNQUALIFIED (CLEAN) OPINION.

Step 5 (Compound Exceptions): When multiple exceptions exist, evaluate each independently, then assess cumulative effect. Multiple qualified exceptions may rise to adverse if they collectively indicate pervasive control failure. Document the rationale for aggregate assessment.

For each exception document: nature (what happened), cause (why), effect (impact on control objective), corrective action, compensating controls.

## Engagement Lifecycle (4 phases)

### Phase 1: Scoping and Readiness
1. Classify engagement type (chunk 02).
2. Determine Type I vs Type II (chunk 02).
3. Define system boundaries (in scope, explicitly excluded).
4. Select TSC categories (chunk 03). Security always; A, PI, C, P optional.
5. Identify subservice organizations (chunk 06). Determine inclusive vs carve-out.
6. Perform readiness assessment (gap analysis): map existing controls to TSC criteria, identify gaps, document severity.
7. Develop remediation plan: prioritize by risk, establish timelines, assign ownership.
8. Establish examination period (Type II): no AICPA-prescribed minimum; 12 months standard, 3-month initial periods common. Ensure all remediated controls operational before period start.
9. Engage CPA practitioner: confirm independence (AICPA Code of Conduct), licensing, peer review enrollment. Execute engagement letter.

### Phase 2: Evidence Gathering and Examination
1. Management prepares system description per Description Criteria.
2. Management prepares written assertion (chunk 05).
3. Practitioner obtains understanding: walkthroughs, interviews, documentation review, observation.
4. Practitioner tests design suitability (Type I and II): evaluate whether each control appropriately designed.
5. Practitioner tests operating effectiveness (Type II only): determine sample sizes (see below), execute test procedures.
6. Practitioner evaluates system description fairness.
7. Practitioner evaluates management's assertion.
8. Practitioner evaluates CUECs and CSOCs (chunk 06).

### Phase 3: Report Issuance
1. Draft report per templates (chunk 04).
2. Determine opinion type (above).
3. Verify all required sections (chunk 04 checklist).
4. Management review and sign-off.
5. Practitioner issues final report.
6. Issue bridge letter if applicable (chunk 05).

### Phase 4: Ongoing Monitoring
1. Continuous monitoring of controls between examination periods.
2. Remediate exceptions identified in prior reports.
3. Document material changes to the system.
4. Prepare for next examination: update description, reassess risk, adjust scope, establish new period.

## Sampling Guidance for Type II

| Control Frequency | Minimum Sample Size | Notes |
|-------------------|---------------------|-------|
| Daily | 25-40 | Select across entire period; coverage of all months |
| Weekly | 10-20 | Spread selections across period |
| Monthly | 2-5 | Select from different months |
| Quarterly | 1-2 | Select from each quarter |
| Annual | 1-2 | Test single annual occurrence or min 1 |
| Per occurrence (triggered) | All or statistical sample | For low-volume triggered controls, test all |

### Deviation Rate Analysis
1. Calculate: Actual Deviation Rate = (deviations / sample size) x 100.
2. Compare to expected (tolerable) deviation rate (typically 0-5% depending on control criticality).
3. Evaluate:
   - Actual <= Expected -> operating effectively (consider increased sample for confirmation).
   - Actual > Expected but < Material threshold -> document deviation, evaluate compensating controls, consider qualified opinion.
   - Actual >= Material threshold -> not operating effectively, may result in qualified or adverse opinion.
4. For each exception document: nature, cause, effect, corrective action, compensating controls.

## Cross-Reference Mapping Summary

TSC -> COSO: CC1-P1-5 (non-seq), CC2-P13-15, CC3-P6-9, CC4-P16-17, CC5-P10-12, CC6-9-P12 (supplemental).
TSC -> ISO 27001:2022: CC6-5.15-5.18/6.5-6.8/7.1-7.9/8.1-8.28, A1-5.29-5.30/8.14-8.15, PI1-8.7-8.16, C1-5.12-5.13/8.10-8.12, P1-8-5.34/ISO27701.
TSC -> NIST 800-53 Rev 5: CC6-AC/PE/IA, CC7-AU/SI/CP, CC8-CM/SA, CC9-RA/SR, P1-8-PT/AR/DI.
TSC -> COBIT 2019: CC1-EDM01-03, CC2-APO01-02, CC3-APO12-13, CC4-MEA01-03, CC6-DSS05-06, CC7-DSS01-04, CC8-BAI06-07, CC9-APO10/APO12.
GDPR -> TSC Privacy (P1-P8): P1.1-Art13-14, P2.1-Art6-7/Art9, P3.1-Art5(1)(b)(c), P4.1-Art5(1)(e)/Art17, P5.1-Art15, P6.1-Art44-49, P7.1-Art77-79, P8.1-Art24/Art32.

Key Distinction: ISO 27001 is certifiable with fixed Annex A controls. SOC 2 uses criteria-based evaluation. ISO covers entire ISMS; SOC 2 scoped to specific systems and TSC categories.

## Citations
- [AT-C-205] [AT-C-320] [TSP-Section-100] [COSO-2013] [ISO-27001-2022] [NIST-SP-800-53-Rev5] [GDPR] [AICPA-Code-of-Conduct]
See SKILL.md Section 10.
