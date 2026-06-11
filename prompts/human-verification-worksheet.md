# Human-verification worksheet — licensed-source facts (process v3.1, SOX-618)

Generated at G1 for any skill whose framework text is licence-restricted (ISO, COSO). The
worksheet is the interface between the agent-built fact sheet and the human who holds the
licensed copy: agents write the claims, the human verifies them, agents ingest the result.
No licensed text crosses the boundary in either direction — claims are original paraphrase
with clause pointers; corrections come back as the human's own words.

## Generator instructions (agent, G1)

Produce `docs/builds/{{skill_slug}}/human-verification-worksheet.md` from the fact sheet's ({{skill_slug}})
`pending_human_verification` rows:

- One row per claim, **sorted in clause/control order** so verification is a single
  front-to-back read of the document.
- Row format (table): `# | claim (paraphrase, the skill's own words) | source pointer
  (edition + clause/control, e.g. "27001:2022+A1 §6.1.3(d)") | check (what exactly to
  confirm — a condition, a list-length, a modal verb strength) | verdict | correction`.
- `verdict` is filled by the human: `CONFIRMED` or `CORRECTED` (with the correction column
  holding the human's own restatement — never copied text).
- Header block: skill slug, fact-sheet path, licensed source identification (standard,
  edition, amendment, supplier, purchase date from `source-texts/manifest.json`), worksheet
  generation date, row count.
- Footer block (human fills): `verified_by:` name, `copy:` exact licensed artifact,
  `date:`, `rows confirmed:` N, `rows corrected:` N, signature line.

## Verification instructions (human)

1. Open the licensed copy (outside the repo). Read front to back; the worksheet rows arrive
   in the same order.
2. For each row: confirm the paraphrase captures the requirement's substance — pay
   attention to modal strength (shall vs should), list completeness (the check column says
   how many items/conditions to expect), and scope qualifiers ("where applicable",
   "as appropriate").
3. Write corrections in your own words. Do not copy sentences from the standard into the
   worksheet.
4. Sign the footer. The signed worksheet is the verification evidence the acceptance gate
   cites.

## Ingestion instructions (agent, after sign-off)

- For every `CONFIRMED` row: flip the fact-sheet row to
  `verification: human-licensed-copy (<copy>, <date>)`.
- For every `CORRECTED` row: apply the correction to the fact sheet FIRST, then flip it.
  A correction that changes a count or identifier cascades like any fact-sheet change
  (inventory-diff reruns).
- The G1 gate fails while any `pending_human_verification` row remains.
- At G4, generate a delta worksheet for (a) any claims added since the signed worksheet and
  (b) a ~10-row spot-recheck sample; the human signs the delta the same way.
