---
uc_id: UC-03
title: "15-entity group designs a §302 sub-certification cascade up to the group PEO/PFO — 14 covered / 1 gap (Entity-14), and the FPI annual-vs-quarterly DC&P-evaluation split lands at 12 domestic (quarterly) / 3 foreign private issuers (annual)"
industries: [manufacturing]
frameworks: [SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15, Reg-S-K-Item-307, Reg-S-K-Item-308]
inputs:
  group: "Meridian Group — parent filer Meridian Holdings Inc (data/seeds/uc-03-input.json)"
  entities: "15 legal entities, each with a sub-certifier and a coverage flag; 12 domestic, 3 foreign private issuers (FPI) (data/seeds/uc-03-input.json)"
  as_of_date: "2026-06-11"
procedure:
  - "chunks/06-disclosure-committee-subcert.md — Design the sub-certification cascade (house framework): map every entity to a sub-certifier rolling up to the group PEO/PFO who sign the §302 certification [CFR-17-240.13a-14 §240.13a-14(a)]."
  - "chunks/06-disclosure-committee-subcert.md — Run the coverage check: recount covered entities, flag every gap; an uncovered entity is a hole in the accumulation-and-communication chain."
  - "chunks/04-evaluation-and-disclosure.md — Split the DC&P-evaluation frequency: domestic issuers evaluate each fiscal quarter; foreign private issuers evaluate each fiscal year [CFR-17-240.13a-15 §240.13a-15(b)]."
  - "chunks/02-dcp-vs-icfr.md — Anchor the cascade in DC&P's accumulation-and-communication requirement: information must reach management to allow timely decisions regarding required disclosure [CFR-17-240.13a-15 §240.13a-15(e)]."
  - "chunks/01-section-302-overview.md — Confirm the group PEO/PFO are the two signing officers; sub-certifications support, but do not replace, their certification [SOX-302-Statute-15USC7241 §7241(a)]."
  - "chunks/03-the-six-certifications.md — A covered-entity exception that bears on ICFR significant deficiencies/material weaknesses also feeds the cert ¶5 disclosure [SOX-302-Statute-15USC7241 §7241(a)(5)]."
  - "SKILL.md §1–§11 — route the multi-entity cascade design through the §302 procedure."
expected_outputs:
  classification: "CASCADE_GAPS_1"
  entities_total: 15
  entities_covered: 14
  coverage_gaps: ["Entity-14"]
  fully_covered: false
  quarterly_eval_entities: 12
  annual_eval_entities: 3
oracle:
  - "entities_total == 15 (recounted from the entity list)"
  - "entities_covered == 14; coverage_gaps == ['Entity-14']; entities_covered + len(coverage_gaps) == entities_total (footing); fully_covered == False"
  - "classification == CASCADE_GAPS_1 (one gap)"
  - "quarterly_eval_entities == 12 (domestic, each fiscal quarter); annual_eval_entities == 3 (FPI, each fiscal year); the two foot to 15 [CFR-17-240.13a-15 §240.13a-15(b)]"
  - "expected-seed agreement: uc-03-expected.json fields equal the recomputed values"
data_refs:
  - data/seeds/uc-03-input.json
  - data/seeds/uc-03-expected.json
tests:
  - tests/test_sox_302_disclosure_controls_oracle.py::test_uc_03_oracle
  - tests/test_sox_302_disclosure_controls_metamorphic.py::test_uc03_entity_order_invariance
  - tests/test_sox_302_disclosure_controls_adversarial.py::test_uc03_empty_entities_zero_coverage
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-03 — Multi-entity §302 sub-certification cascade (Meridian Group)

## §1 Context and persona

**Meridian Group** is a fictional multi-entity, multi-segment group whose parent filer is **Meridian Holdings Inc**. The group comprises **15 legal entities** — 12 domestic and 3 **foreign private issuers (FPI)**. The persona is the **Big-4 SOX advisor / group controller** designing the §302 **sub-certification cascade**: every entity's controller sub-certifies up to the group PEO/PFO who sign the consolidated certification.

The seed `data/seeds/uc-03-input.json` is the tested fixture; every count below is recomputed from it by `tests/test_sox_302_disclosure_controls_oracle.py::test_uc_03_oracle`.

## §2 The sub-cert framework is a house framework

The sub-certification cascade is a **house framework, not a rule requirement**. The §302 certification is signed by exactly **two** officers — the group **PEO and PFO** [SOX-302-Statute-15USC7241 §7241(a); CFR-17-240.13a-14 §240.13a-14(a)]. The SEC *recommended* a disclosure committee in Release 33-8124 but did not mandate sub-certifications. A multi-entity group nonetheless builds a cascade so the two signing officers can rely on a structured, documented chain: each entity's controller sub-certifies, the segment leads roll up, and the group PEO/PFO certify on top. Sub-certifications **support** the officers' certification; they do not replace it, and they do not change who is legally on the hook.

The cascade exists to satisfy DC&P's **accumulation-and-communication** requirement: information required to be disclosed must be "accumulated and communicated to the issuer's management … as appropriate to allow timely decisions regarding required disclosure" [CFR-17-240.13a-15 §240.13a-15(e)]. In a 15-entity group, the cascade *is* that communication channel.

## §3 Coverage check — 14 covered / 1 gap (Entity-14)

Each of the 15 entities maps to a sub-certifier with a coverage flag. The check recounts coverage and flags every gap:

| Entity | Type | Sub-certifier | Covered |
|--------|------|---------------|---------|
| Entity-01 | domestic | Controller-Entity-01 | yes |
| Entity-02 | domestic | Controller-Entity-02 | yes |
| Entity-03 | domestic | Controller-Entity-03 | yes |
| Entity-04 | domestic | Controller-Entity-04 | yes |
| Entity-05 | domestic | Controller-Entity-05 | yes |
| Entity-06 | domestic | Controller-Entity-06 | yes |
| Entity-07 | domestic | Controller-Entity-07 | yes |
| Entity-08 | domestic | Controller-Entity-08 | yes |
| Entity-09 | domestic | Controller-Entity-09 | yes |
| Entity-10 | domestic | Controller-Entity-10 | yes |
| Entity-11 | fpi | Controller-Entity-11 | yes |
| Entity-12 | fpi | Controller-Entity-12 | yes |
| Entity-13 | fpi | Controller-Entity-13 | yes |
| Entity-14 | domestic | Controller-Entity-14 | **no — GAP** |
| Entity-15 | domestic | Controller-Entity-15 | yes |

**Coverage: 15 total — 14 covered / 1 gap.** The single gap is **Entity-14**, a domestic entity with no completed sub-certification in scope. `coverage_gaps == ["Entity-14"]`, `fully_covered == False`, and the engagement classifies `CASCADE_GAPS_1`. The footing holds: 14 covered + 1 gap = 15. A coverage gap is a hole in the accumulation-and-communication chain — the group PEO/PFO cannot rely on a sub-certification that was never obtained, so Entity-14 is the remediation priority before the certification is signed.

## §4 FPI evaluation-frequency split — 12 quarterly / 3 annual

The DC&P-evaluation **frequency** depends on issuer type. Management evaluates DC&P effectiveness as of the end of **each fiscal quarter** — but a **foreign private issuer** evaluates as of the end of **each fiscal year** [CFR-17-240.13a-15 §240.13a-15(b)]. Splitting the 15 entities by type:

- **12 domestic entities → quarterly DC&P evaluation** (`quarterly_eval_entities == 12`).
- **3 foreign private issuers → annual DC&P evaluation** (`annual_eval_entities == 3`).

The two foot to 15. The cascade design therefore runs the domestic sub-certifications on a quarterly cadence and the three FPI sub-certifications on an annual cadence, while the group-level §302 certification itself is filed with each periodic report.

**Scoping nuance (the registrant drives frequency).** The annual DC&P-evaluation frequency under 13a-15(b) attaches to a **foreign private issuer that is itself an SEC registrant** — not to a foreign *subsidiary* inside a domestic filer's consolidated group. A domestic parent's consolidated DC&P evaluation is quarterly regardless of its foreign-sub composition. This UC treats the 3 FPI entities as **separate FPI registrants** (the seed's `type: fpi`); a foreign entity that were merely a consolidated subsidiary of a domestic filer would fall under that filer's quarterly cadence, not the FPI annual one.

## §5 Order invariance and the empty-list edge

The cascade roll-up is **order-invariant**: reversing the entity list changes none of the counts — covered, gaps, and the quarterly/annual split are all the same (`test_uc03_entity_order_invariance`). The adversarial edge: an **empty** entity list yields zero coverage, an empty gap list, and `CASCADE_GAPS_0` — the cascade never invents entities (`test_uc03_empty_entities_zero_coverage`).

## §6 Oracle — every count is derivable

`tests/test_sox_302_disclosure_controls_oracle.py::test_uc_03_oracle` recomputes every count independently from `uc-03-input.json`:

- `entities_total == 15` (recounted).
- `entities_covered == 14`; `coverage_gaps == ["Entity-14"]`; `entities_covered + len(coverage_gaps) == entities_total`; `fully_covered == False`; `classification == CASCADE_GAPS_1`.
- `quarterly_eval_entities == 12` (domestic); `annual_eval_entities == 3` (FPI); the two foot to 15.
- Expected-seed agreement: `uc-03-expected.json` equals the recomputed values.

Metamorphic: reversing the entity order changes nothing. Adversarial: an empty entity list yields zero coverage and `CASCADE_GAPS_0`.

## §7 Anti-hallucination

- **Meridian Group / Meridian Holdings Inc are fictional**; the seed is the tested fixture. Org names, the 14/1 coverage, and the 12/3 split are exactly as seeded.
- **The sub-certification cascade is a house framework, not a rule mandate** — the §302 certification is signed by the PEO and PFO (two officers); sub-certifications support but do not replace it (Release 33-8124 recommended, did not mandate).
- **The FPI annual-vs-quarterly split is a rule fact** [CFR-17-240.13a-15 §240.13a-15(b)] — domestic issuers evaluate DC&P each fiscal quarter, foreign private issuers each fiscal year.
- **A coverage gap is not a §302 violation by itself** — it is a process gap in the house framework that the group must close before relying on the cascade; the legal certification remains the PEO/PFO's.
- **DC&P ≠ ICFR and §302 ≠ §404** — the cascade is a DC&P accumulation-and-communication mechanism, not a §404 ICFR assessment.
