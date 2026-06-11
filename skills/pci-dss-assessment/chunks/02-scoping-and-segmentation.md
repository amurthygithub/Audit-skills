---
chunk_id: 02-scoping-and-segmentation
parent_skill: pci-dss-assessment
topic: "CDE scoping; connected-to and security-impacting systems; segmentation to reduce scope; scope as the highest-leverage decision; assessor sampling"
load_when: "user asks what is in scope, how to scope a CDE, what connected-to/security-impacting means, how segmentation reduces scope, or how assessors sample"
---

# Chunk 02 — Scoping and Segmentation

Scope is the highest-leverage decision in a PCI DSS assessment: it sets which of the 249 defined requirements apply, which validation path fits (`chunks/03`), and how much evidence an assessor must gather. PCI DSS expects scope to be **confirmed at least annually** and before each assessment (paraphrased intent of Req 12.5.2), and re-confirmed when the environment changes.

## 1. The three scope bands

| Band | Definition (paraphrased) | In scope? |
|------|--------------------------|-----------|
| **CDE systems** | Store, process, or transmit account data (CHD/SAD), or are on the same network segment as systems that do | Yes |
| **Connected-to / security-impacting systems** | Can connect to or could affect the security of the CDE (e.g., authentication servers, logging/SIEM, patch/jump hosts, admin tooling) — without themselves handling account data | Yes |
| **Out-of-scope systems** | Cannot store/process/transmit account data and cannot impact CDE security, demonstrated by validated isolation | No |

The middle band is the one most often under-scoped: a directory server, a SIEM, a jump host, a patch server, or a backup system that touches the CDE is **in scope** even though account data never flows through it.

## 2. The scope in/out rule (house decision convention)

> **House convention — engagement-decision logic, not verbatim standard text.** For an inventoried system component, classify it: **in scope** if it stores/processes/transmits account data (**CDE**) OR can connect to / affect the security of the CDE (**connected/security-impacting**); **out of scope** only if isolation from the CDE is implemented AND validated. In-scope count = CDE + connected; out-of-scope systems must be defensible, not assumed.

This rule **applies** the standard's scoping criteria; it is labeled as decision logic so it is never mistaken for the standard's own wording. The default for an unproven system is **in scope** — out-of-scope status must be earned through demonstrated isolation.

## 3. Segmentation reduces scope

**Segmentation** isolates the CDE from the rest of the network so that out-of-scope systems are demonstrably unable to affect CDE security. It is not required, but it is the primary lever to **shrink the in-scope footprint** and therefore the assessment burden:

- Without segmentation, the entire network is typically in scope.
- With effective segmentation, only the CDE plus connected-to/security-impacting systems remain in scope; isolated segments fall out.
- Segmentation effectiveness must be **validated** (penetration testing of segmentation controls — Req 11.4.5; service providers test more frequently per Req 11.4.6). Segmentation that is asserted but not validated does not reduce scope.

**Monotonicity:** moving systems from CDE/connected into a validated out-of-scope segment can only **decrease or hold** the in-scope count — never increase it. The skill's scope arithmetic respects this.

## 4. Procedure — CDE scope determination

1. **Inventory** all system components in the environment (Req 12.5.1 maintains this inventory).
2. **Map account-data flows** — where PAN/CHD/SAD enters, is stored, processed, transmitted, and leaves.
3. **Tag each system** `cde` (handles account data or shares its segment), `connected` (connects to / can impact the CDE), or `out` (validated isolation).
4. **Compute scope:** in-scope = count(`cde`) + count(`connected`); out-of-scope = count(`out`); footing check: in + out = total.
5. **Validate segmentation** for every `out` claim (penetration test of the isolation controls).
6. **Re-confirm** annually and on change.

## 5. Output template — scope inventory

| Field | Meaning |
|-------|---------|
| `system` | named component |
| `scope_tag` | `cde` / `connected` / `out` |
| `data_flow_note` | what account data, if any, it handles |
| `isolation_evidence` | for `out`: how isolation is validated |

Rollup: `total_systems`, `cde_systems`, `in_scope_systems` (cde+connected), `out_of_scope_systems`, with `in_scope + out_of_scope == total` enforced.

**Worked illustration (UC-02 shape):** a 14-system retail inventory tagged 5 `cde` (POS terminals, payment switch, card vault, store controller, e-comm web), 4 `connected` (AD, SIEM, jump host, patch server, backup), and the remainder `out` (corp email, HR, guest wifi, dev sandbox) yields **9 in scope, 5 out of scope** — see `use-cases/uc-02-roc-segmentation.md`. Reordering the inventory does not change the counts.

## 6. Assessor sampling

When the population of similar in-scope components (e.g., hundreds of identical POS terminals across stores) is large, an assessor may **sample** representative items rather than test every one — provided standardized, centrally managed configuration processes are in place and the sample is justified and documented. Sampling reduces testing effort; it never reduces **scope**. The full population remains in scope even when only a sample is tested. Sampling rationale belongs in the ROC (`chunks/06`).

## 7. Common scoping errors

- Treating connected-to systems (directory, logging, admin) as out of scope because "no card data flows through them."
- Claiming segmentation without a validating penetration test.
- Forgetting that **shared infrastructure** (hypervisors, cloud control planes, shared services) inherits scope from the workloads it hosts.
- Letting scope drift between annual confirmations after environment changes.
