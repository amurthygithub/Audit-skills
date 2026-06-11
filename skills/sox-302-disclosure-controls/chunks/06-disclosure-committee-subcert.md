---
chunk_id: 06-disclosure-committee-subcert
parent_skill: sox-302-disclosure-controls
topic: "The disclosure committee (recommended, not mandated — Release 33-8124) and the sub-certification cascade (house framework): how process owners / entities sub-certify up to the PEO/PFO; coverage and exception roll-up; multi-entity groups"
load_when: "user asks how to set up a disclosure committee, design a sub-certification cascade, roll up sub-certifications, or run the certification process across multiple entities"
---

# Chunk 06 — Disclosure Committee & Sub-Certification Cascade

**Read this label first and carry it through every output: the disclosure committee and the sub-certification cascade are RECOMMENDED PRACTICE / a HOUSE FRAMEWORK — they are NOT a rule requirement.** The SEC **recommended** (did not mandate) a disclosure committee in the 2002 adopting release (SEC Release 33-8124). What the **rules** require is the officer certification (§240.13a-14), the DC&P evaluation (§240.13a-15(b)), and the disclosures (Items 307/308). The committee and cascade are how issuers operationalize that certification — a sound practice, but never assert them as legally mandated.

## 1. The disclosure committee (recommended practice)

A disclosure committee is a cross-functional group (finance, legal, IR, IT, operations, internal audit) that the SEC **recommended** issuers establish to support the officers' certification by gathering and vetting disclosure. It is a **practice**, not a codified obligation. A charter typically defines:
- **Mandate:** assist the PEO/PFO in designing, maintaining, and evaluating DC&P (the rule duty stays with the officers).
- **Membership:** owners of each disclosure stream (financial AND non-financial — risk factors, legal, MD&A, cyber; see `chunks/02`).
- **Cadence:** convene each quarter ahead of the periodic filing (aligned to the §240.13a-15(b) evaluation — `chunks/04`).
- **Output:** a documented recommendation supporting the officers' DC&P effectiveness conclusion.

Label the charter and every artifact as **house framework / recommended practice**.

## 2. The sub-certification cascade (house framework)

A **sub-certification cascade** is a practice in which process owners or legal entities each certify ("sub-certify") their area up to the group PEO/PFO, who rely on those sub-certifications in making the top-level §302 certification. It is a **framework**, not a rule. A typical design:
1. **Map** each disclosure-relevant area or entity to a **sub-certifier** (a controller, process owner, or entity officer).
2. Each sub-certifier attests **clean** or flags an **exception** (with a note) for the period.
3. **Roll up:** count clean vs exception; route every exception to the disclosure committee and the officers.
4. The top-level certification is supported by the cascade, but the **rule obligation remains the PEO's and PFO's** — sub-certifications are evidence, not a substitute (`chunks/03`).

### Procedure — design and roll-up

```
1. Enumerate entities / process owners in scope for the period.
2. Assign one sub-certifier per area/entity; confirm coverage (no gaps).
3. Collect sub-certifications: status in {clean, exception}; exception_note.
4. Roll up:  total = count(all);  exceptions = count(status==exception);
             clean = total - exceptions;  gaps = areas with no sub-certifier.
5. Top-level cert is "clean" only if exceptions == 0 AND the DC&P conclusion
   is effective (an unremediated MW makes DC&P not effective — chunks/07).
6. Route every exception and gap to the disclosure committee and officers.
```

The roll-up counts are mechanical: order-independent and recomputed from the list (see `use-cases/uc-01-mw-interplay.md` and `use-cases/uc-03-multientity-subcert.md`).

## 3. Multi-entity groups and the FPI evaluation split

In a group, each legal entity is mapped to a sub-certifier rolling up to the **group** PEO/PFO. The **evaluation frequency** differs by entity type (a **rule** fact, unlike the cascade itself):
- **Domestic** entities: DC&P evaluated **each fiscal quarter** [CFR-17-240.13a-15 §b].
- **Foreign private issuers (FPIs):** DC&P evaluated **each fiscal year** [CFR-17-240.13a-15 §b].

So a 15-entity group splits its evaluation cadence between quarterly (domestic) and annual (FPI) — see `use-cases/uc-03-multientity-subcert.md` (12 quarterly / 3 annual). **Coverage** (every in-scope entity mapped to a sub-certifier) is checked from the entity list; gaps are flagged and must be closed before the officers certify.

## 4. Output template — sub-cert roll-up (labeled house framework)

```
SUB-CERTIFICATION ROLL-UP — [period]   (house framework; not a rule artifact)
  Entities/areas in scope ......... N
  Sub-certifiers assigned ......... M     Coverage gaps: [list]  (must be 0)
  Clean ........................... C
  Exceptions ...................... E     -> route each to disclosure committee
  Evaluation cadence: domestic = quarterly; FPI = annual
  Top-level cert clean? ........... (E == 0 AND DC&P conclusion = effective)
```

## 5. Anti-hallucination

- **The disclosure committee and sub-certification cascade are recommended practice / a house framework — never a rule mandate.** The SEC recommended (did not require) a disclosure committee (Release 33-8124). Label every charter, cascade, and roll-up as practice.
- **The rule obligation stays with the PEO and PFO** [CFR-17-240.13a-14 §a]; sub-certifications are supporting evidence, not a legal substitute for the officers' certification.
- The **evaluation-cadence split** (domestic quarterly / FPI annual) **is** a rule fact [CFR-17-240.13a-15 §b] — distinct from the cascade, which is practice.
