# Limits and disclaimers — PCI DSS assessment skill

## Future-dated requirements banner — read this first

**Every "future-dated" requirement in PCI DSS v4.0.1 is IN FORCE — it has been mandatory
since 31 March 2025.** The v4.0.1 text still prints the "best practice until 31 March 2025"
applicability notes (33 such markers in the main body) because those notes were written before
the date passed. They are NOT optional and NOT future obligations. This skill always presents
them as fully effective requirements; it never describes a v4.0.1 requirement as "coming
later," "best practice," or "phased in." A reader who sees one of those notes in the standard
must read it as "in effect now."

## Validation levels are brand-defined, not PCI SSC facts

Merchant and service-provider **validation levels (Level 1, Level 2, …) are defined by the
individual payment brands and acquirers — not by PCI SSC and not by the standard.** The
thresholds (transaction volumes, the triggers that mandate a ROC vs. an SAQ, the levels
themselves) vary by brand and by acquirer agreement and change over time. Wherever a level
appears in the fixtures or use cases it is labeled "brand-defined." The skill never asserts a
level threshold as a PCI DSS fact, and it always notes that **a payment brand or acquirer may
mandate a full ROC regardless of SAQ eligibility.**

## Defined vs. customized vs. compensating — three distinct mechanisms

These are three separate things and the skill keeps them distinct:

- **Defined approach** — meet the requirement exactly as written in the standard, validated
  against its stated testing procedures.
- **Customized approach (Appendix D/E)** — meet the requirement's *objective* by a different
  method that is expected to meet or exceed the security of the defined requirement. It is
  **TRA-driven** (requires a documented Targeted Risk Analysis) and is **not** triggered by an
  inability to comply. Several requirements have no customized-approach option.
- **Compensating control (Appendix B/C)** — for an **existing defined requirement** an entity
  **cannot meet because of a legitimate business or technical constraint**. It must meet the
  intent and rigor of the original requirement and is documented with the **four Compensating
  Controls Worksheet elements** (constraints, original objective, identified risk, controls in
  place). It is **constraint-driven**.

Confusing these is the most common substantive error in PCI scoping; the chunks and use cases
label which mechanism applies in every example.

## PAN is never shown in examples (a data-handling teaching point)

This skill never displays a Primary Account Number (PAN), and no example, fixture, or doc ever
contains one — not even a fake-but-realistic one. This is deliberate: handling PAN safely is
itself a PCI DSS teaching point (Req 3 protects stored account data; account data = cardholder
data + sensitive authentication data). The fixtures describe *architecture* (does a server
touch PAN? is the page outsourced?) without ever instantiating a card number.

## What this skill is NOT

- **Not a QSA engagement.** This skill does not produce a Report on Compliance (ROC), sign an
  Attestation of Compliance (AOC), or act as a Qualified Security Assessor. It describes ROC/AOC
  mechanics; it does not perform a validated assessment. A QSA engagement (or a qualified ISA)
  is required where one is mandated.
- **Not legal advice.** Card-brand compliance programs, acquirer contracts, fines, and
  liability questions require qualified counsel and your acquirer; this skill is an
  interpretive aid, not a determination.
- **PAN / CHD / SAD never enter telemetry.** Cardholder data, sensitive authentication data,
  and PAN must never appear in a telemetry event or a seed — see `telemetry/redaction.md`. The
  seeds carry only org-level and architecture facts; there is no wall-clock dependence (all date
  math runs off the seed `as_of_date`).

## Licence note — paraphrase and cite, never reproduce

The PCI DSS standard text is licensed under the PCI SSC "Read and Copy License" (internal use /
study only; **no redistribution or modification**). This skill therefore **paraphrases and
cites** the standard — it references requirement IDs, section numbers, and structure, and uses
only short attributed excerpts. It **never reproduces bulk verbatim standard text** in any file
in this repo. Facts are machine-verified against the maintainer's local licensed copy (stored
outside the repo); the repo stores identifiers, counts, structure, and original paraphrase
only.

## No crosswalk rows in v1 (OLIR pointer)

v1 of this skill encodes **no crosswalk rows** (PCI → CSF, 800-53, or otherwise).
`data/crosswalks/` is intentionally empty. The authoritative mapping is the NIST OLIR final
informative reference "PCI-DSS-4.0.1-to-CSF-v2.0" (PCI SSC-submitted). The skill points to the
OLIR program and the NIST CSF informative-references catalog; it asserts no row of its own. Row
encoding is deferred to a later extraction pass.

## v4.0.1 is the only active version

**PCI DSS v4.0.1 (June 2024) is the only currently active version.** v4.0 retired 2024-12-31;
v3.2.1 retired 2024-03-31. v4.0.1 is a "limited revision" — no new or deleted requirements vs
v4.0. No successor (v4.1 / v5) was announced as of the last currency check (2026-06-11).
**Version currency is this skill's #1 trust factor — re-verify the active version, the SAQ
catalog versions, and that no successor has been published before any client use.** This volatile
content is isolated in `chunks/08-currency-and-program-context.md` so a single file is re-checked
at each G4 pass.

## When to escalate to a human

- Any compliance *determination* (a ROC/AOC, a level assignment, an acquirer dispute) — those
  belong to a QSA/ISA and your acquirer, not to this skill.
- A disputed scope boundary (whether a system is in or out of scope drives the entire
  assessment; segmentation must be validated, not assumed).
- A compensating-control or customized-approach decision a client intends to rely on — the
  documented justification is the entity's responsibility and an assessor's call.
- Any reliance on version currency or SAQ-catalog facts — re-verify the standard's status first.

## Anti-hallucination posture

This skill is born-vetted (process v3): every identifier and count was extracted mechanically
from the official PCI DSS v4.0.1 PDF (the maintainer's licensed copy, retrieved 2026-06-11) into
`docs/pci-dss-assessment-fact-sheet.md` (repo root), and a standing CI test diffs the seed
inventory against that fact sheet. Currency claims (active version, future-dated-now-in-force,
SAQ catalog versions, OLIR crosswalk status) were settled by live source checks — see
`docs/acceptance-gate.md`. If you find a factual error, file an issue or open a PR — the skill
is maintained rigorously.
