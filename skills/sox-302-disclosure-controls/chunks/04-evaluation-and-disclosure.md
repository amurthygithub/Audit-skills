---
chunk_id: 04-evaluation-and-disclosure
parent_skill: sox-302-disclosure-controls
topic: "13a-15(b) quarterly DC&P evaluation; Item 307 disclose-the-DC&P-conclusion; Item 308(a)/(c) ICFR report and changes; the evidence the evaluation rests on; effectiveness-conclusion language"
load_when: "user asks how to evaluate DC&P, the quarterly evaluation cadence, what to disclose under Item 307 or Item 308, or how to phrase the effectiveness conclusion"
---

# Chunk 04 — Evaluation and Disclosure

Paragraph 4(c) of the certification requires the officers to **evaluate** DC&P effectiveness and present their conclusion. This chunk covers the evaluation requirement (§240.13a-15(b)), the disclosure of the DC&P conclusion (Item 307), and the ICFR report and change disclosure (Item 308).

## 1. The DC&P evaluation — §240.13a-15(b)

> "Each such issuer's management must evaluate, with the participation of the issuer's principal executive and principal financial officers … the effectiveness of the issuer's disclosure controls and procedures, as of the end of each fiscal quarter," except that a foreign private issuer evaluates "as of the end of each fiscal year" and a registered investment company evaluates within the 90-day period before each certifying report's filing date [CFR-17-240.13a-15 §b].

- **Cadence:** domestic issuers — **each fiscal quarter**; FPIs — **each fiscal year**. This split drives the multi-entity cascade in `chunks/06-disclosure-committee-subcert.md`.
- **Participation:** the evaluation is management's, performed **with the participation of** the PEO and PFO — the same officers who certify.
- **As-of date:** the evaluation is "as of the end of" the period; the conclusion in the certification (¶4(c)) is the as-of-period-end conclusion.

A separate evaluation under §240.13a-15(d) covers **changes in ICFR** during the quarter (or fiscal year for an FPI) that materially affected, or are reasonably likely to materially affect, ICFR — this feeds Item 308(c) and certification ¶6.

## 2. Evidence the evaluation rests on

The rule does not prescribe a single method, but a defensible DC&P evaluation typically draws on:
- the design and operation of the disclosure process (close calendar, sub-certifications, disclosure-committee review — `chunks/06`);
- the results of any ICFR testing (because ICFR is the financial subset of DC&P — `chunks/02`);
- the inventory of disclosure items, financial and non-financial, in scope for the period;
- open items: identified significant deficiencies, material weaknesses, and any late or missed disclosures (e.g., an 8-K timeliness issue — `chunks/07`).

The conclusion is the officers' reasoned judgment that DC&P were, or were not, **effective** at the reasonable-assurance level as of period end.

## 3. Disclosing the DC&P conclusion — Item 307

> "Disclose the conclusions of the registrant's principal executive and principal financial officers … regarding the effectiveness of the registrant's disclosure controls and procedures (as defined in §240.13a-15(e) …) as of the end of the period covered by the report, based on the evaluation of these controls and procedures required by paragraph (b) of §240.13a-15 …" [Reg-S-K-Item-307 §a]

Item 307 is where the DC&P **effectiveness conclusion** is publicly disclosed (typically in the report's Controls and Procedures item). It is the disclosure counterpart to certification ¶4(c). If an unremediated material weakness in a disclosure-relevant area exists, the officers conclude DC&P **not effective** and say so here — see `chunks/07` and `use-cases/uc-01-mw-interplay.md`.

## 4. The ICFR report and change disclosure — Item 308

- **Item 308(a)** — management's **annual** report on ICFR: a statement of responsibility, the framework used, and management's assessment of ICFR effectiveness as of fiscal-year end, including disclosure of any material weakness. Management **may not conclude ICFR is effective if one or more material weaknesses exist** [Reg-S-K-Item-308 §a]. This is the §404(a) deliverable — covered in depth by `coso-internal-controls`; do not re-teach §404 here.
- **Item 308(c)** — disclose any **change in ICFR** identified in connection with the §240.13a-15(d) evaluation that occurred during the last fiscal quarter (fourth quarter for an annual report) that has materially affected, or is reasonably likely to materially affect, ICFR [Reg-S-K-Item-308 §a]. This pairs with certification ¶6.
- The §404(b) auditor attestation and the newly-public/EGC exemptions live in `chunks/05-section-302-vs-404.md` [Reg-S-K-Item-308 §b].

## 5. Output template — effectiveness conclusion + Item 307 language

```
EVALUATION OF DISCLOSURE CONTROLS AND PROCEDURES
As of the end of the period covered by this report, management, with the
participation of the [PEO] and [PFO], evaluated the effectiveness of the
company's disclosure controls and procedures (as defined in Rule 13a-15(e)).
[Effective case]   Based on that evaluation, the [PEO] and [PFO] concluded
  that the company's disclosure controls and procedures were effective as of
  [period-end date].
[Not-effective case]   Based on that evaluation, and because of the material
  weakness in internal control over financial reporting described in
  [reference], the [PEO] and [PFO] concluded that the company's disclosure
  controls and procedures were NOT effective as of [period-end date].
CHANGES IN INTERNAL CONTROL OVER FINANCIAL REPORTING (Item 308(c))
[Describe any change during the quarter that materially affected, or is
 reasonably likely to materially affect, ICFR — or state there was none.]
```

## 6. Anti-hallucination

- DC&P is evaluated **each fiscal quarter** (FPI: each fiscal year) [CFR-17-240.13a-15 §b]; the often-cited "90-day" window is the **investment-company** rule, not the general issuer rule.
- Item 307 discloses the **DC&P** conclusion; Item 308 covers the **ICFR** report and changes [Reg-S-K-Item-307 §a] [Reg-S-K-Item-308 §a]. Keep DC&P and ICFR disclosures distinct (`chunks/02`).
- Management **cannot** conclude ICFR is effective with one or more material weaknesses present [Reg-S-K-Item-308 §a]. The §404(a) report and §404(b) attestation are `coso-internal-controls` territory.
