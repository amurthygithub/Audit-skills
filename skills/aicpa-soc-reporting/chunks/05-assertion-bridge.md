---
chunk_id: 05-assertion-bridge
parent_skill: aicpa-soc-reporting
topic: "Management Assertion Letter Templates and Bridge Letter Template"
load_when: "user asks about management assertions, representation letters, bridge letters, or gap period coverage"
---

# Chunk 05 -- Management Assertion and Bridge Letter Templates

## Type I Assertion (2 paragraphs)

```
[Service Organization Letterhead]
[Date]
To: [CPA Firm Name / Practitioner Name]
RE: Management's Assertion -- [System Name] [SOC 1 / SOC 2 / SOC for Cybersecurity / SOC for Supply Chain] Type I

We assert that:

1. The description of the [System Name] system in Section II of the report fairly presents the [System Name] system as it relates to the [Description Criteria / Trust Services Criteria / Cybersecurity Description Criteria]. The criteria we used to prepare the description were [specify criteria reference].

2. The controls described in the system description were suitably designed to provide reasonable assurance that the [control objectives / trust service criteria] would be achieved if the controls operated effectively as of [Date].

Sincerely,
[Management Representative Name]
[Title]
[Service Organization Name]
```

## Type II Assertion (3 paragraphs)

```
[Service Organization Letterhead]
[Date]
To: [CPA Firm Name / Practitioner Name]
RE: Management's Assertion -- [System Name] [SOC 1 / SOC 2 / SOC for Cybersecurity / SOC for Supply Chain] Type II

We assert that:

1. The description of the [System Name] system in Section II of the report fairly presents the [System Name] system as it relates to the [Description Criteria / Trust Services Criteria / Cybersecurity Description Criteria]. The criteria we used to prepare the description were [specify criteria reference].

2. The controls described in the system description were suitably designed to provide reasonable assurance that the [control objectives / trust service criteria] would be achieved if the controls operated effectively throughout the period from [Start Date] to [End Date].

3. The controls described in the system description operated effectively throughout the period from [Start Date] to [End Date] to provide reasonable assurance that the [control objectives / trust service criteria] were achieved.

Sincerely,
[Management Representative Name]
[Title]
[Service Organization Name]
```

Key rules:
- Type I: 2 paragraphs (fair presentation + design suitability).
- Type II: 3 paragraphs (fair presentation + design suitability + operating effectiveness).
- If management refuses to provide the assertion, the practitioner MUST withdraw per AT-C 205.
- Always ensure the assertion is signed and dated.

## Bridge Letter Template

```
[Service Organization Letterhead]
[Date]
RE: Bridge Letter -- [System Name] SOC 2 Type II Report
Period Covered: [Report End Date] to [Current Date / Expected Next Report Date]

Dear [User Entity / Relevant Party]:

This letter supplements the SOC 2 Type II report issued by [CPA Firm Name] dated [Report Date], covering [Start Date] to [End Date].

During the period from [Report End Date] to [Current Date]:

1. There [have / have not] been material changes to the system description.
   [If changes: describe each material change, its nature, and timing.]

2. There [have / have not] been material changes to the design of controls.
   [If changes: describe each change and impact on control objectives.]

3. There [have / have not] been exceptions in the operating effectiveness of controls.
   [If exceptions: describe each, nature, cause, and corrective action.]

4. The CUECs and CSOCs disclosed in the SOC 2 Type II report [remain / do not remain] appropriate.
   [If not: describe changes and updated controls.]

This letter is a management representation only and does not provide auditor assurance. It is not a substitute for a SOC 2 Type II report.

Sincerely,
[Management Representative Name]
[Title]
[Service Organization Name]
```

Key rules:
- Issued by MANAGEMENT, not the CPA.
- Provides NO auditor assurance -- must explicitly state this.
- Covers gap period (typically 3-6 months) between report end and current/next report date.
- Typical gap: SOC 2 covers Jan 1-Dec 31; bridge letter covers Jan 1-Jun 30 while next report is prepared.
- Always include the disclaimer that it is not a SOC report.

## Citations
- [AT-C-205]
See SKILL.md Section 10.
