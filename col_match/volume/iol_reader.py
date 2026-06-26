"""Edition discovery + duplicate-volume collapse for the India Office List OCR.

The IOL OCR (``iol_ocr_1860-1940/``) is fundamentally different from the
Colonial Office List OCR: there is **no** ``result.json`` of layout blocks — each
edition is a flowed markdown file (``<edition>.md``) plus an ``.html`` twin and a
page-level ``<edition>_metadata.json`` (``pages[]`` with ``token_count``; no
per-block bbox/category). So this corpus gets its own reader (this module +
``iol_bios.py``) rather than reusing ``reader.py``'s block loader.

Editions are organised under decade directories (``1860s/`` … ``1940s/``), one
subdirectory per edition. The publication was renamed several times, so the
directory prefix (the "family") is era-dependent:

    iacsl   Indian Army & Civil Service List      (1861+)
    il      India List, Civil and Military        (1882-1895)
    iliol   India List / India Office List         (1896-1937)
    iol     India Office List                      (1896-1937, alt OCR run)
    iobol   India Office and Burma Office List     (1938+)

The same physical volume is sometimes OCR'd twice under two families (e.g.
``iol_1936`` and ``iliol_1936``). Those MUST be collapsed to one source before
extraction or every affected officer doubles. Half-yearly editions (``_jan`` /
``_jul``) are NOT duplicates and are both kept — they are distinct attestations.
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent.parent
IOL_OCR_ROOT = Path(os.environ.get("IOL_OCR_ROOT", _REPO / "iol_ocr_1860-1940"))

# Ordered alternation: longer prefixes first so `il` doesn't shadow `iliol`/`iol`.
_DIR_RE = re.compile(r"^(iacsl|iliol|iobol|iol|il)_(\d{4})(?:_([a-z]+))?$", re.I)

# Era-preferred family when one (year, month) is OCR'd under several prefixes.
# First present wins; ties fall back to the largest markdown file.
_ERA_PREF = ["iobol", "iliol", "iol", "iacsl", "il"]


@dataclass(frozen=True)
class EditionKey:
    family: str
    year: int
    month: str | None          # "jan" | "jul" | None (annual)
    dirpath: Path

    @property
    def tag(self) -> str:
        """Stable per-edition id used in bio_ids and cache filenames."""
        return f"{self.year}" + (f"_{self.month}" if self.month else "")

    @property
    def html_path(self) -> Path:
        return self.dirpath / f"{self.dirpath.name}.html"

    @property
    def md_path(self) -> Path:
        return self.dirpath / f"{self.dirpath.name}.md"

    @property
    def meta_path(self) -> Path:
        return self.dirpath / f"{self.dirpath.name}_metadata.json"

    @property
    def has_body(self) -> bool:
        # HTML is the segmentation source (clean <p><b>name</b>—body</p>);
        # fall back to markdown only if the HTML twin is absent.
        return self.html_path.exists() or self.md_path.exists()


def _scan(root: Path) -> list[EditionKey]:
    found: list[EditionKey] = []
    for decade in sorted(root.glob("*s")):
        if not decade.is_dir():
            continue
        for d in sorted(decade.iterdir()):
            if not d.is_dir():
                continue
            m = _DIR_RE.match(d.name)
            if not m:
                continue
            fam, year, month = m.group(1).lower(), int(m.group(2)), m.group(3)
            found.append(EditionKey(fam, year, (month or None), d))
    return found


def _pick(cands: list[EditionKey]) -> EditionKey:
    """Choose the canonical OCR run for one (year, month) volume."""
    by_fam = {c.family: c for c in cands}
    for fam in _ERA_PREF:
        if fam in by_fam and by_fam[fam].has_body:
            return by_fam[fam]
    # no preferred family has a body — largest HTML wins
    def _size(c: EditionKey) -> int:
        p = c.html_path if c.html_path.exists() else c.md_path
        return p.stat().st_size if p.exists() else 0
    with_body = [c for c in cands if c.has_body]
    return max(with_body or cands, key=_size)


def available_editions(root: Path | None = None) -> tuple[list[EditionKey], list[dict]]:
    """Return (selected editions, source-selection audit rows).

    Collapses duplicate OCR runs of one physical volume; keeps half-yearly
    editions separate. Editions missing a markdown body are skipped with a
    warning (the OCR tree is populated by an active rsync and may be partial).
    """
    root = root or IOL_OCR_ROOT
    groups: dict[tuple[int, str | None], list[EditionKey]] = {}
    for ek in _scan(root):
        groups.setdefault((ek.year, ek.month), []).append(ek)

    selected: list[EditionKey] = []
    audit: list[dict] = []
    for key in sorted(groups, key=lambda k: (k[0], k[1] or "")):
        cands = groups[key]
        winner = _pick(cands)
        if not winner.has_body:
            print(f"[iol_reader] WARN no markdown body for {key} "
                  f"({[c.dirpath.name for c in cands]}) — skipping", file=sys.stderr)
            continue
        selected.append(winner)
        if len(cands) > 1:
            audit.append({
                "year": key[0], "month": key[1],
                "chosen": winner.dirpath.name,
                "dropped": [c.dirpath.name for c in cands if c is not winner],
            })
    return selected, audit


def load_edition(ek: EditionKey) -> tuple[str, list[int]]:
    """Return (HTML text, per-page token counts). The HTML carries clean
    ``<p><b>headword</b>—body</p>`` bio paragraphs; token counts come from the
    page-level metadata.json (empty list if absent — provenance then degrades to
    char offsets only)."""
    src = ek.html_path if ek.html_path.exists() else ek.md_path
    body = src.read_text(encoding="utf-8")
    page_tokens: list[int] = []
    if ek.meta_path.exists():
        try:
            meta = json.loads(ek.meta_path.read_text(encoding="utf-8"))
            page_tokens = [int(p.get("token_count", 0)) for p in meta.get("pages", [])]
        except Exception:
            page_tokens = []
    return body, page_tokens
