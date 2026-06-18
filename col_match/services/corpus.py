"""Volume discovery and era classification for the services-section corpus.

The corpus is one directory per scanned volume, each containing
``olmocr_results.md`` (full-volume markdown from olmOCR). Services sections
exist in every Colonial Office List edition 1883-1966 except 1946, plus the
1935 Dominions Office List; pre-1883 editions and the Commonwealth Relations
Office Lists never carried one.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# Editions known to lack a services section despite being in the corpus.
# 1946: slim postwar restart (1948 preface: biographical notes restored).
# 1952: paper shortage — its own preface says the Record of Services
#       "has had to be omitted altogether".
_EXCLUDED_YEARS = {1946, 1952}
_MIN_YEAR = 1883

# Format eras (entry shape changes; see docs/approach.md).
ERA_EARLY = "early"  # 1883-1912: CAPS surname, no birth year, long entries
ERA_MID = "mid"      # 1913-1940: CAPS surname + "B. YYYY"
ERA_LATE = "late"    # 1948-1966: Title-case surname + "b. yyyy; ed. ..."

_VOLUME_RE = re.compile(r"^(colonial-office-list|dominions-office-list)-(\d{4})$")


@dataclass(frozen=True)
class Volume:
    name: str          # directory name, e.g. "colonial-office-list-1930"
    year: int
    era: str
    path: Path         # .../olmocr_results.md

    @property
    def slug(self) -> str:
        """Short id used in entry ids, e.g. "col1930" / "dol1935"."""
        prefix = "dol" if self.name.startswith("dominions") else "col"
        return f"{prefix}{self.year}"


def era_for_year(year: int) -> str:
    if year <= 1912:
        return ERA_EARLY
    if year <= 1940:
        return ERA_MID
    return ERA_LATE


def discover_volumes(corpus_dir: str | Path) -> list[Volume]:
    """Return services-bearing volumes, sorted by year."""
    corpus = Path(corpus_dir)
    volumes = []
    for child in sorted(corpus.iterdir()):
        m = _VOLUME_RE.match(child.name)
        if not m:
            continue
        year = int(m.group(2))
        if year < _MIN_YEAR or year in _EXCLUDED_YEARS:
            continue
        md = child / "olmocr_results.md"
        if not md.is_file():
            continue
        volumes.append(Volume(name=child.name, year=year, era=era_for_year(year), path=md))
    return volumes


def get_volume(corpus_dir: str | Path, name_or_year: str) -> Volume:
    """Look up one volume by directory name or bare year (COL assumed)."""
    if name_or_year.isdigit():
        name_or_year = f"colonial-office-list-{name_or_year}"
    for vol in discover_volumes(corpus_dir):
        if vol.name == name_or_year:
            return vol
    raise KeyError(f"no services-bearing volume {name_or_year!r}")
