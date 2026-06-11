---
chunk_id: 07-material-weakness-and-change
parent_skill: sox-302-disclosure-controls
topic: "A new material weakness or significant deficiency and its effect on the §302 DC&P conclusion; material-change disclosure; ¶5 disclosure to auditors/audit committee; the cyber-8-K timeliness DC&P touchpoint (Item 1.05, 4 business days); remediation-period certification language"
load_when: "user asks what a material weakness does to the certification, how to disclose a control change, the ¶5 disclosure, the cyber 8-K timeliness, or remediation-period certification language"
---

# Chunk 07 — Material Weakness & Change

This chunk handles the edge that consumers most need: a newly identified **material weakness (MW)** or **significant deficiency (SD)**, what it does to the §302 DC&P conclusion, and the related change and timely-disclosure obligations — including the **non-financial** cyber 8-K timeliness touchpoint.

## 1. MW → DC&P conclusion (the derivable logic)

Because ICFR is the financial-reporting subset of DC&P (`chunks/02-dcp-vs-icfr.md`):

- An **unremediated material weakness in a disclosure-relevant area** means the company's DC&P were **not effective** for that area as of period end. The officers cannot certify DC&P "effective"; they disclose "not effective" under Item 307 [Reg-S-K-Item-307 §a]. This is the conclusion `use-cases/uc-01-mw-interplay.md` derives.
- **Remediation flips the conclusion.** Once the MW is remediated (and the remediated controls are tested and operating), the DC&P conclusion can return to "effective" for a later period. The conclusion is **fact-driven** by the MW's status and area — not a fixed label.
- A **significant deficiency** (less severe than an MW) does not by itself force a "not effective" DC&P conclusion, but it must still be evaluated and is disclosable to the auditors and audit committee under ¶5.

Mechanically: `DC&P not effective` ⇐ (`affects_disclosure_relevant_area` AND NOT `remediated`).

## 2. The ¶5 disclosure to auditors and the audit committee

The existence of **any** ICFR significant deficiency or material weakness (or any fraud involving management or employees with a significant ICFR role) triggers the certification **¶5** obligation to disclose it to the issuer's auditors and the audit committee [SOX-302-Statute-15USC7241 §a]. This is independent of the public DC&P effectiveness conclusion: even an SD that does not flip the DC&P conclusion is a ¶5 disclosure item. See `chunks/03-the-six-certifications.md`.

## 3. Material-change disclosure — Item 308(c) and ¶6

A change in ICFR during the quarter (fourth quarter for an annual report) that **materially affected, or is reasonably likely to materially affect, ICFR** is disclosed under **Item 308(c)** [Reg-S-K-Item-308 §a] and noted in certification **¶6** (`chunks/03`). Identifying, remediating, or newly discovering an MW during the period is the kind of change that drives this disclosure. (The Item 308(a) annual ICFR **report** itself is §404(a) — `coso-internal-controls`.)

## 4. The cyber 8-K timeliness touchpoint (non-financial DC&P)

A material cybersecurity incident must be reported on **Form 8-K Item 1.05 within 4 business days of the issuer's determination that the incident is material** (added by SEC Release 33-11216, 2023). This is a **DC&P** timeliness matter — DC&P must "allow timely decisions regarding required disclosure" (`chunks/02`) — and it is **non-financial**:

- A failure to report the incident within the 4-business-day window is a **DC&P** failure (the disclosure process did not surface a required non-financial disclosure in time).
- It is **never** an ICFR matter — it does not concern the reliability of financial reporting. Do not classify a missed cyber 8-K as an ICFR deficiency.
- This is the canonical example of a DC&P failure that is not an ICFR failure (`chunks/02 §4`).

## 5. Output template — MW disclosure + remediation-period certification language

```
MATERIAL WEAKNESS DISCLOSURE
Management identified a material weakness in internal control over financial
reporting as of [period-end], relating to [area]. [Describe the deficiency.]
EFFECT ON DISCLOSURE CONTROLS AND PROCEDURES (Item 307)
As a result of the material weakness described above, the [PEO] and [PFO]
concluded that the company's disclosure controls and procedures were NOT
effective as of [period-end date].
DISCLOSURE TO AUDITORS AND AUDIT COMMITTEE (certification para. 5)
The material weakness was disclosed to the company's independent auditors and
the audit committee.
REMEDIATION
[Describe the remediation plan and status. Until the remediated controls have
operated for a sufficient period and been tested, the disclosure controls and
procedures continue to be concluded NOT effective for the affected area.]
CHANGES IN ICFR (Item 308(c) / certification para. 6)
[Describe the change during the quarter that materially affected, or is
 reasonably likely to materially affect, ICFR.]
```

## 6. Anti-hallucination

- An **unremediated MW in a disclosure-relevant area forces a "not effective" DC&P conclusion** [Reg-S-K-Item-307 §a]; remediation can flip it back. The conclusion is fact-driven, never a fixed label.
- **Any SD/MW (or qualifying fraud) triggers the ¶5 disclosure** to the auditors and audit committee [SOX-302-Statute-15USC7241 §a], independent of the public DC&P conclusion.
- The **cyber 8-K Item 1.05 deadline is 4 business days from the materiality determination** — a non-financial **DC&P** timeliness matter, **never** an ICFR matter (`chunks/02`).
- Item 308(c) discloses an ICFR **change**; the §404(a) annual ICFR **report** (Item 308(a)) is `coso-internal-controls` territory [Reg-S-K-Item-308 §a].
