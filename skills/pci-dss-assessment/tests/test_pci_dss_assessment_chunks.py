"""Smoke tests for the 8 PCI DSS assessment chunks.

Mirrors the audit-workpapers / hipaa-security-rule pattern: each chunk must
exist, have valid YAML frontmatter, declare its chunk_id, and fit within the
200-line per-chunk limit.
"""

from __future__ import annotations

from pathlib import Path

import pytest

CHUNKS_DIR = Path(__file__).resolve().parent.parent / "chunks"
EXPECTED_CHUNKS = [
    "01-scope-and-applicability.md",
    "02-scoping-and-segmentation.md",
    "03-saq-selection.md",
    "04-requirements-1-6.md",
    "05-requirements-7-12.md",
    "06-validation-roc-aoc.md",
    "07-approaches-and-compensating-controls.md",
    "08-currency-and-program-context.md",
]


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_file_exists(filename):
    path = CHUNKS_DIR / filename
    assert path.exists(), f"Expected chunk at {path}"


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_under_line_limit(filename):
    path = CHUNKS_DIR / filename
    if not path.exists():
        pytest.skip(f"{filename} not yet shipped")
    line_count = len(path.read_text().splitlines())
    assert line_count <= 200, f"{filename} is {line_count} lines (> 200 limit)"


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_has_yaml_frontmatter(filename):
    path = CHUNKS_DIR / filename
    if not path.exists():
        pytest.skip(f"{filename} not yet shipped")
    text = path.read_text()
    assert text.startswith("---\n"), f"{filename} must start with YAML frontmatter"
    assert "\n---\n" in text or text.endswith("\n---\n"), f"{filename} must terminate frontmatter"


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_id_matches_filename(filename):
    path = CHUNKS_DIR / filename
    if not path.exists():
        pytest.skip(f"{filename} not yet shipped")
    text = path.read_text()
    expected_id = filename.replace(".md", "")
    assert f"chunk_id: {expected_id}" in text, (
        f"{filename} must declare chunk_id: {expected_id}"
    )
