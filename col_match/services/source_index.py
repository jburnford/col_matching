"""Resolve a (printed place, edition year) to the staff-list OCR file(s).

The per-colony staff-list OCR lives at
``{source_ocr_dir}/{year}_manual_parsed/{TERRITORY}.txt`` — 69 edition-year
directories, ~45 territory files each, names varying across editions
(``MALAYA``, ``FEDERATION_OF_MALAYA``, ``MALAYA_STRAITS_SETTLEMENTS`` are all
the same place in different years). This module bridges the graph/biography
place vocabulary to those filenames.

Design note: the resolver only needs good *recall*. Recovery confirms a record
by finding the surname in the returned file's text, so an over-inclusive match
is harmless — a wrong file simply yields "surname not present", never a
fabricated record. We therefore match generously (normalized prefix either
direction) and let the OCR text be the real gate.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

from . import gazetteer

_YEAR_DIR = re.compile(r"^(\d{4})_manual_parsed$")
_NORM = re.compile(r"[^a-z]")
# filename decorations to drop before normalizing
_FILE_NOISE = re.compile(r"(_ref|_colony|_protectorate|_and_dependencies)$", re.I)


def _terr_key(filename: str) -> str:
    """Normalize a territory filename stem to the gazetteer's [a-z] space."""
    stem = _FILE_NOISE.sub("", filename)
    return _NORM.sub("", stem.lower())


class SourceIndex:
    """Index of edition-year staff-list files, keyed (year, territory_key)."""

    def __init__(self, source_ocr_dir: str):
        self.root = Path(source_ocr_dir).expanduser()
        # year -> list of (territory_key, path)
        self.by_year: dict[int, list[tuple[str, Path]]] = {}
        for d in sorted(self.root.glob("*_manual_parsed")):
            m = _YEAR_DIR.match(d.name)
            if not m:  # the non-year 'colony_manual_parsed' dir, etc.
                continue
            year = int(m.group(1))
            entries: list[tuple[str, Path]] = []
            for f in d.glob("*.txt"):
                if ":Zone.Identifier" in f.name:  # Windows ADS clutter
                    continue
                key = _terr_key(f.stem)
                if key:
                    entries.append((key, f))
            if entries:
                self.by_year[year] = entries
        self.years = sorted(self.by_year)

    def _match_in_year(self, year: int, targets: set[str]) -> list[Path]:
        out: list[Path] = []
        for key, path in self.by_year.get(year, ()):
            for t in targets:
                # exact match always; substring either direction only for
                # targets long enough not to collide (e.g. 'straitssettlements'
                # is a suffix of 'malayastraitssettlements'). Short targets
                # ('co', 'ss') must match exactly.
                if key == t or (len(t) >= 4 and (t in key or key in t)):
                    out.append(path)
                    break
        return out

    def resolve(self, place: str | None, year: int, data_dir: str,
                window: int = 2) -> list[Path]:
        """Files for `place` at `year`. Tries the exact edition year, then the
        nearest years within +/-`window` (staff lists carry forward, so an
        adjacent edition usually still lists the same officer)."""
        if not place:
            return []
        targets = {gazetteer.norm(t) for t in
                   gazetteer.colony_targets(place, data_dir)}
        targets.add(gazetteer.norm(place))
        targets.discard("")
        if not targets:
            return []
        # exact year first, then spiral outward
        order = [year] + [year + d for w in range(1, window + 1)
                          for d in (w, -w)]
        seen: set[Path] = set()
        out: list[Path] = []
        for y in order:
            for p in self._match_in_year(y, targets):
                if p not in seen:
                    seen.add(p)
                    out.append(p)
            if out:  # nearest edition with any hit wins; don't keep spiraling
                break
        return out

    def coverage(self, data_dir: str, colonies: list[str],
                 years: list[int]) -> dict:
        """Diagnostic: for each colony, which of `years` resolve to a file."""
        table = {}
        for c in colonies:
            hit = [y for y in years if self.resolve(c, y, data_dir, window=0)]
            table[c] = {"resolved_years": len(hit), "total_years": len(years)}
        return table


@lru_cache(maxsize=4)
def load_index(source_ocr_dir: str) -> SourceIndex:
    return SourceIndex(source_ocr_dir)
