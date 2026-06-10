"""Citation registry enforcement (SOX-609).

data/registry/citations.json is the canonical source of truth for every
citation label and URL. Per-skill §10 manifests are vendored views; these
tests keep them in sync, which makes same-label-different-URL drift (the
FedRAMP/COSO/AICPA inconsistencies found 2026-06-09) impossible.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO / "data" / "registry" / "citations.json"
REGISTRY = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))["citations"]

SKILLS = sorted(
    p.parent for p in (REPO / "skills").glob("*/SKILL.md") if p.parent.name != "TEMPLATE"
)
SKILL_IDS = [s.name for s in SKILLS]


def manifest_rows(skill: Path):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"^##\s*10\.\s*References.*?\n(.*?)(?=^##\s|\Z)", text, re.MULTILINE | re.DOTALL)
    assert m, f"{skill.name}: no §10 manifest found"
    rows = []
    for line in m.group(1).splitlines():
        if not line.startswith("|") or set(line) <= set("|- :"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 6 and cells[0] != "Label":
            rows.append({"label": cells[0], "url": cells[5]})
    assert rows, f"{skill.name}: §10 manifest table parsed to zero rows"
    return rows


class TestRegistryWellFormed:
    def test_entries_complete(self):
        assert len(REGISTRY) >= 75
        for label, e in REGISTRY.items():
            for field in ("title", "publisher", "identifier", "url", "retrieval_date", "cited_by"):
                assert e.get(field), f"{label}: missing/empty '{field}'"
            assert e["url"].startswith("https://"), f"{label}: non-https URL {e['url']}"
            assert "<" not in e["url"], f"{label}: placeholder URL"

    def test_no_orphan_entries(self):
        cited = set()
        for skill in SKILLS:
            cited.update(r["label"] for r in manifest_rows(skill))
        orphans = set(REGISTRY) - cited
        assert not orphans, f"registry entries cited by no skill: {sorted(orphans)}"

    def test_cited_by_matches_disk(self):
        actual = defaultdict(set)
        for skill in SKILLS:
            for r in manifest_rows(skill):
                actual[r["label"]].add(skill.name)
        for label, e in REGISTRY.items():
            assert sorted(actual[label]) == e["cited_by"], (
                f"{label}: registry cited_by {e['cited_by']} != disk {sorted(actual[label])}"
            )


@pytest.mark.parametrize("skill", SKILLS, ids=SKILL_IDS)
def test_manifest_synced_with_registry(skill: Path):
    """Every manifest row must exist in the registry with the identical URL."""
    for r in manifest_rows(skill):
        assert r["label"] in REGISTRY, (
            f"{skill.name}: manifest cites '{r['label']}' which is not in "
            f"data/registry/citations.json — add it to the registry first (it is the source of truth)"
        )
        canonical = REGISTRY[r["label"]]["url"]
        assert r["url"] == canonical, (
            f"{skill.name}: '{r['label']}' URL {r['url']} != canonical {canonical} — "
            f"manifests must use the registry URL verbatim"
        )
