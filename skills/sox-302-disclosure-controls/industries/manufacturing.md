---
industry: manufacturing
parent_skill: sox-302-disclosure-controls
title: "Manufacturing — multi-entity / multi-segment groups: the §302 sub-certification cascade across legal entities, the foreign-private-issuer annual-vs-quarterly evaluation split, and coverage-gap control"
version: 0.1.0
status: active
frameworks: [SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15, Reg-S-K-Item-307, Reg-S-K-Item-308]
primary_personas: [Group controller, Big-4 SOX advisor, SEC-reporting manager, Segment finance lead]
regulatory_anchors: [SOX-302, SEC-Release-33-8124, Foreign-Private-Issuer-evaluation-frequency]
last_verified: "2026-06-11"
---

# Manufacturing — the multi-entity group lens

A diversified manufacturer typically reports as a **multi-entity, multi-segment group**: a parent filer over dozens of legal entities — domestic and foreign — spread across business segments and geographies. The §302 certification is signed by **two** group officers (the PEO and PFO), but they must rely on a structured **sub-certification cascade** that reaches every entity. This view applies the skill to the multi-entity group. The UC-03 engagement (`use-cases/uc-03-multientity-subcert.md`, Meridian Group — 15 entities, parent Meridian Holdings Inc) is the worked example.

## The multi-entity framing

### Who actually signs the §302 certification in a 15-entity group?

Only the **group PEO and PFO** [SOX-302-Statute-15USC7241 §7241(a); CFR-17-240.13a-14 §240.13a-14(a)]. Entity controllers do not sign the SEC-filed certification — they **sub-certify** up the chain. The sub-certification cascade is a **house framework, not a rule** (the SEC recommended a disclosure committee in Release 33-8124; it did not mandate sub-certifications). Its purpose is to let the two signing officers rely on a documented chain that satisfies DC&P's accumulation-and-communication requirement [CFR-17-240.13a-15 §240.13a-15(e)] across entities the officers never see directly. Sub-certifications support the certification; they never replace it, and the legal exposure stays with the PEO/PFO.

### How do we know the cascade actually covers every entity?

By running a **coverage check** and flagging every gap. Each entity maps to a sub-certifier with a coverage flag; the check recounts covered entities and lists the uncovered ones. In UC-03, 15 entities yield **14 covered / 1 gap** (Entity-14), classification `CASCADE_GAPS_1`, with the footing covered + gaps = total. A coverage gap is a hole in the accumulation-and-communication chain — the group PEO/PFO cannot rely on a sub-certification that was never obtained, so the gap is a remediation priority **before** the certification is signed. A gap is a process failure in the house framework, not by itself a §302 violation.

### Foreign subsidiaries: quarterly or annual DC&P evaluation?

It depends on issuer type. Management evaluates DC&P effectiveness as of the end of **each fiscal quarter** — but a **foreign private issuer** evaluates as of the end of **each fiscal year** [CFR-17-240.13a-15 §240.13a-15(b)]. This is a **rule fact**, not a house convention. In UC-03 the 15 entities split into **12 domestic (quarterly evaluation) / 3 foreign private issuers (annual evaluation)**, footing to 15. The cascade design runs the domestic sub-certifications on a quarterly cadence and the three FPI sub-certifications annually, while the group-level §302 certification is filed with each periodic report.

### How does a segment material weakness propagate up?

If an entity's sub-certification flags an ICFR significant deficiency or material weakness, it feeds two things: the group DC&P effectiveness conclusion (a disclosure-relevant MW can turn it not effective — the UC-01 logic) and the cert ¶5 disclosure to the auditors and audit committee [SOX-302-Statute-15USC7241 §7241(a)(5)]. The cascade is the mechanism by which a segment-level issue reaches the group officers in time.

## What's unique to multi-entity manufacturers

- **The cascade is the program.** With dozens of entities, the sub-certification cascade and its coverage footing are the central control; design it explicitly and label it a house framework.
- **The FPI split is a rule, not a convention.** Domestic quarterly vs FPI annual DC&P evaluation is dictated by §240.13a-15(b); get the entity typing right.
- **Coverage gaps are the recurring failure.** A newly acquired or newly material subsidiary that never entered the cascade is the classic gap; the coverage check catches it.
- **Segment and geographic complexity widens DC&P scope.** Multiple segments mean more non-financial disclosure (segment risk factors, legal proceedings, environmental matters) — all DC&P scope.

## Anti-hallucination

- **The sub-certification cascade is a house framework, not a rule** — only the group PEO and PFO sign the §302 certification [SOX-302-Statute-15USC7241 §7241(a); CFR-17-240.13a-14 §240.13a-14(a)]; Release 33-8124 recommended a disclosure committee but mandated no sub-certifications.
- **The FPI annual-vs-quarterly split is a rule fact** [CFR-17-240.13a-15 §240.13a-15(b)] — domestic issuers evaluate each fiscal quarter, foreign private issuers each fiscal year.
- **A coverage gap is a process gap, not automatically a §302 violation** — it must be closed before the cascade is relied on; the legal certification remains the officers'.
- **DC&P ≠ ICFR and §302 ≠ §404** — the cascade is a DC&P accumulation-and-communication mechanism, not a §404 ICFR assessment.
- **This is not legal advice** — foreign-private-issuer status and entity materiality turn on specific facts; confirm with counsel.

## Cross-references

- `use-cases/uc-03-multientity-subcert.md` — the worked 15-entity cascade: 14 covered / 1 gap (Entity-14), 12 quarterly / 3 annual.
- `chunks/06-disclosure-committee-subcert.md` — the sub-certification cascade and coverage roll-up (house framework).
- `chunks/04-evaluation-and-disclosure.md` — the DC&P-evaluation frequency split (domestic quarterly / FPI annual).
- `chunks/07-material-weakness-and-change.md` — how a segment-level material weakness propagates to the group DC&P conclusion and the ¶5 disclosure.
- `coso-internal-controls` (sibling skill) — authoritative for the §404 ICFR assessment mechanics the cascade's MW findings feed at year-end.
