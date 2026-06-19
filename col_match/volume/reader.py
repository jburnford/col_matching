"""Block loader + provenance model for the new layout-aware OCR.

The new OCR stores one ``result.json`` per edition under
``<OCR_ROOT>/json/<Doc><YEAR>.pdf/result.json`` — a list of pages, each a list
of blocks ``{"bbox": [x0, y0, x1, y1], "category": str, "text": str}``. The
block order within ``result.json`` is already the OCR's reading order (verified
on 1921: services-section bios appear alphabetically; roster sections appear
header → establishment-title → roster-text in print order), so we PRESERVE the
given order rather than re-deriving it from bbox.

Every block is wrapped as a :class:`Block` carrying its provenance key
``(edition_year, page, index, bbox)`` — the stable citation back to the raw OCR.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

# Root of the new (Infinity-2) OCR tree. Resolution order:
#   1. COL_OCR_ROOT env override;
#   2. the in-repo copy (raw_ocr/, so the repo is self-contained on GitHub);
#   3. the original external location under ~/plato.
import os

_REPO_OCR = Path(__file__).resolve().parent.parent.parent / "raw_ocr"
_EXTERNAL_OCR = Path.home() / "plato" / "colonial_office_lists"
OCR_ROOT = Path(
    os.environ.get("COL_OCR_ROOT")
    or (_REPO_OCR if (_REPO_OCR / "json").is_dir() else _EXTERNAL_OCR)
)


@dataclass(frozen=True)
class Block:
    """One OCR block with its provenance key."""

    edition_year: int
    doc: str             # "col" | "dol" | "cro" — document family
    page: int            # 0-based page index in result.json
    index: int           # 0-based block index within the page (reading order)
    category: str        # text | title | header | footer | table | figure | ...
    text: str
    bbox: tuple[int, int, int, int]

    @property
    def prov(self) -> dict:
        """JSON-serialisable provenance citation back to the raw OCR block."""
        return {
            "edition_year": self.edition_year,
            "doc": self.doc,
            "page": self.page,
            "block": self.index,
            "bbox": list(self.bbox),
        }


def _doc_family(dirname: str) -> str:
    low = dirname.lower()
    if low.startswith("dominions"):
        return "dol"
    if low.startswith("commrel"):
        return "cro"
    return "col"


def resolve_volume_path(year: int, doc: str = "col", ocr_root: Path | None = None) -> Path:
    """Locate the result.json for an edition. ``doc`` selects the document
    family: col=ColonialOfficeList, dol=DominionsOfficeList, cro=CommRelOffList.
    Tolerates the stray leading-space directory names in the OCR tree."""
    root = (ocr_root or OCR_ROOT) / "json"
    stem = {
        "col": "ColonialOfficeList",
        "dol": "DominionsOfficeList",
        "cro": "CommRelOffList",
    }[doc]
    matches = sorted(root.glob(f"*{stem}{year}.pdf/result.json"))
    if not matches:
        raise FileNotFoundError(f"no {doc} result.json for {year} under {root}")
    return matches[0]


def available_years(doc: str = "col", ocr_root: Path | None = None) -> list[int]:
    root = (ocr_root or OCR_ROOT) / "json"
    stem = {"col": "ColonialOfficeList", "dol": "DominionsOfficeList", "cro": "CommRelOffList"}[doc]
    years = []
    for p in root.glob(f"*{stem}*.pdf"):
        tail = p.name.split(stem, 1)[1].split(".pdf", 1)[0].strip()
        if tail.isdigit():
            years.append(int(tail))
    return sorted(years)


def load_volume(year: int, doc: str = "col", ocr_root: Path | None = None) -> list[Block]:
    """Read one edition into a flat, reading-ordered list of :class:`Block`."""
    path = resolve_volume_path(year, doc, ocr_root)
    family = _doc_family(path.parent.name)
    pages = json.loads(path.read_text(encoding="utf-8"))
    blocks: list[Block] = []
    for pi, page in enumerate(pages):
        if not isinstance(page, list):
            continue
        for bi, b in enumerate(page):
            bbox = b.get("bbox") or [0, 0, 0, 0]
            blocks.append(
                Block(
                    edition_year=year,
                    doc=family,
                    page=pi,
                    index=bi,
                    category=b.get("category", ""),
                    text=(b.get("text") or "").strip(),
                    bbox=tuple(int(x) for x in bbox[:4]),
                )
            )
    return blocks
