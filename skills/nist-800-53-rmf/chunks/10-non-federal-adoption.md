---
chunk_id: 10-non-federal-adoption
parent_skill: nist-800-53-rmf
topic: "Non-federal adoption paths — who authorizes absent a federal AO (state/local authorizing authority, non-federal senior official); state RMF adoption (CA SAM, TX DIR/TX-RAMP, NASCIO); resource-constrained risk-based scoping (family prioritization, sampling, prior-evidence reuse, multi-year rotation); the non-federal authorization-decision report shape"
load_when: "user asks about state/local RMF, non-federal adoption, who risk-accepts without a federal AO, a state authorization, GAGAS/Yellow Book finding context, resource-constrained or small-shop assessment scoping, or applying 800-53/RMF outside the federal government"
---

# Chunk 10 — Non-federal adoption paths

NIST 800-53 and the RMF are a **federal** standard, but the control catalog and the seven-step
process are routinely adopted by **state and local governments, tribes, public universities, and
private partners**. When they are, the **controls and the RMF steps are the same** — but the
**authorization machinery is not**: there is no federal Authorizing Official (AO), no FISMA
statutory authority, and no FedRAMP PMO. This chunk gives the **non-federal model** so the skill's
"state-RMF" support is real and does not assume federal-only machinery (CFACTS/CSAM, a federal AO,
the FedRAMP Marketplace) that a non-federal entity does not have.

## 1. Who authorizes absent a federal AO

In the federal model the **AO is a designated official with statutory authority** (FISMA / OMB
A-130) who formally accepts residual risk and signs the ATO [OMB-A-130 §risk-acceptance]. Outside
the federal government there is **no automatic equivalent** — the entity must **designate an
authorizing authority** to play the AO's role:

| Non-federal context | Who risk-accepts (the AO-equivalent) |
|---------------------|--------------------------------------|
| State / local government | The **state CISO**, the **agency head/secretary**, or a designated **authorizing authority** under the state's IT-security statute or administrative code |
| Public university / health system | The **CISO** or a **governance/IT risk board** chartered to accept system risk |
| Private / commercial partner (adopting 800-53 voluntarily, e.g. for a contract) | A **senior accountable executive** (CISO/CIO) or the body the partner's policy names |

The **decision logic is identical** to the federal model (`chunks/06-authorize.md`): authorize /
authorize-with-conditions / deny, with documented residual risk, rationale, and a re-review
trigger [NIST-SP-800-37-Rev2 §Step6]. What changes is the **signatory and the governing policy** —
name the authorizing authority and its authority source explicitly in the package; do not assume a
"federal AO" exists.

## 2. State RMF adoption — the same catalog, a state overlay

Many states adopt 800-53 through **their own catalog or overlay**, not as a separate framework:

- **CA SAM** — California's State Administrative Manual (§5300-series) incorporates 800-53 with
  state overlays for agencies under the California Department of Technology.
- **TX DIR** — the Texas DIR Security Control Standards Catalog maps to 800-53; **TX-RAMP** mirrors
  FedRAMP for cloud services used by Texas state agencies, on the 800-53 catalog.
- **NASCIO-aligned state standards** — many states publish a state security standard (often
  NASCIO-informed) that adopts the 800-53 families with state-specific boundaries, AO
  designations, and assessment cadences.

The state's **authoritative publication governs** the specific overlay, the authorization
boundary, the authorizing authority, and the cadence. This skill gives the **model**; consult the
state's own standard for the binding specifics. (Federal-overlay programs for specific data —
IRS Pub 1075 for FTI, MARS-E for ACA/CMS data, SSA overlays for benefits-eligibility systems —
are a related but distinct topic; see the scope note in §6.)

## 3. Resource-constrained risk-based scoping (small shops)

A small state agency or non-federal team **cannot fully enumerate ~1,000 controls** every cycle.
The federal full-enumeration procedure (`chunks/04-implement.md`, `chunks/05-assess.md`) is the
ceiling, not the only path. **Risk-based scoping** keeps the assessment defensible and feasible:

1. **Family prioritization.** Start with the control families that carry the most risk for the
   system's data and threats (e.g., AC, IA, AU, SC, IR, CP for a public-facing benefits system),
   and address lower-risk families on a slower cadence.
2. **Control sampling within a family.** Where a family has many enhancements, assess a
   risk-weighted sample plus all high-impact controls, rather than every enhancement every cycle.
3. **Prior-evidence reuse.** A control assessed in a prior cycle with **no change** to its
   implementation can **carry its prior result forward** with a documented "no-change"
   attestation, rather than a full re-test.
4. **Multi-year assessment rotation.** Under the OMB A-130 **ongoing-authorization / ISCM** model,
   assess roughly **one-third of the controls each year on a 3-year cycle** so the full set is
   covered over time, instead of all-at-once annually [OMB-A-130 §ISCM].
5. **Leverage inherited / common controls.** Controls inherited from a shared service or an
   authorized cloud provider are assessed in the provider's package, not re-tested locally
   (`chunks/04-implement.md §inheritance`).

Document the scoping rationale (which families/controls, why, and the cadence) so the authorizing
authority can accept the **assessment scope** as risk-based, not arbitrary.

## 4. The non-federal authorization report shape

A non-federal adoption produces an **authorization-decision record**, not necessarily a federal
"ATO letter": the authorizing authority, the scope assessed, the residual risk accepted, the
conditions, and the re-review trigger. For **GAGAS / Yellow Book** engagements (a state auditor or
an IG-style review), use the **C-C-C-E-R finding** (Condition / Criteria / Cause / Effect /
Recommendation) plus a **management response** from `audit-workpapers` — name the addressee and the
responsible official. (The full Yellow Book report wrapper — report elements, questioned costs,
distribution — is tracked separately as **SOX-672**.)

## 5. Output template — non-federal authorization decision record

```yaml
authorization_decision_record:
  system: <name>
  adopting_entity: <state agency | university | partner>
  authorizing_authority: <role/title>          # the AO-equivalent — name it
  authority_source: <state statute / admin code / board charter / contract>
  framework_basis: "NIST SP 800-53 Rev 5 via <state overlay, e.g. CA SAM / TX DIR / entity standard>"
  assessment_scope: <risk-based — families/controls assessed this cycle + rotation plan>
  decision: <authorize | authorize-with-conditions | deny>
  residual_risk_accepted: <description>
  conditions:
    - <condition + date>
  re_review_trigger: <date | significant change | annual>
  signed: <authorizing authority, title, date>
```

## 6. Anti-hallucination & scope

- **The 800-53 catalog and the RMF process are the same off-federal; the authorization machinery is
  not.** Do not assume a federal AO, FISMA authority, CFACTS/CSAM, or the FedRAMP PMO exist for a
  non-federal entity — name the **designated authorizing authority** instead.
- **State overlays and authorizing authorities vary by jurisdiction.** This chunk gives the model;
  the **state's / entity's authoritative publication governs** the binding specifics. Do not state
  a specific state's boundary, AO designation, or cadence as fact without its publication.
- **Risk-based scoping is defensible, not a shortcut to skip controls.** Document the rationale and
  the rotation so the authorizing authority accepts the scope; high-impact controls are not
  deferred.
- **Data-specific federal overlays (IRS Pub 1075 / MARS-E / SSA) are out of scope here** — a
  benefits-eligibility-overlay build is tracked separately (**SOX-680**). This chunk covers the
  general non-federal authorization model, not a specific overlay's control set.

## Citations in this chunk

- `[NIST-SP-800-37-Rev2 §Step6]` — the RMF authorization step (same logic, non-federal signatory)
- `[OMB-A-130 §ISCM]` — ongoing authorization / continuous monitoring (the rotation model)
- `[IRS-Pub-1075]` — named as an out-of-scope data overlay (SOX-639 split)

See `## 10. References & Citation Manifest` in SKILL.md.
