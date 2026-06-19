"""Cross-edition person clustering + richest-entry selection.

A person recurs across many editions; within an active career their entry is
cumulative and lossless, but the section condenses post-war (see
memory bio-evolution-across-editions). So we cluster the same person across all
editions and pick the **richest = longest of the latest pre-1940 attestations**
as the canonical entry to parse; the other attestations are kept for provenance
and to extend the career past 1939.

Clustering is conservative (over-splitting is safer than over-merging for a KG):
bios merge only on a strong key — same surname-key + birth year (±1 for OCR) +
compatible given-name initials, or, when no birth year is printed, identical
spelled multi-token given names. Reuses the abbreviation-aware name comparison
from services/compile.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from ..services.compile import _names_compatible, _norm
from ..volume import reader
from ..volume.bios import VolumeBio, extract_bios

_SURKEY = re.compile(r"[^A-Z]")
_CONDENSE_CUTOFF = 1940   # entries from <= this year are the rich era; later ones condense


def surname_key(b: dict) -> str:
    return _SURKEY.sub("", (b.get("surname") or b["raw_text"].split(",", 1)[0]).upper())


def _first_initial(b: dict) -> str:
    g = (b.get("given_names") or "").strip()
    return g[0].upper() if g[:1].isalpha() else ""


def _spelled_given(b: dict) -> str:
    """Normalized given-name string if it carries >=1 spelled (multi-char)
    token, else '' (initials-only — too weak to cluster on without a birth year)."""
    g = (b.get("given_names") or "").strip()
    toks = [t for t in re.split(r"[ .]+", g) if t]
    if any(len(t) > 1 for t in toks):
        return _norm(g)
    return ""


@dataclass
class Person:
    person_id: str
    surname: str
    given_names: str | None
    birth_year: int | None
    editions: list[int]
    canonical: dict                      # the richest VolumeBio dict
    attestations: list[dict] = field(default_factory=list)  # all bio dicts, incl. canonical

    def to_json(self) -> dict:
        return {
            "person_id": self.person_id,
            "surname": self.surname,
            "given_names": self.given_names,
            "birth_year": self.birth_year,
            "editions": sorted(set(self.editions)),
            "canonical_bio_id": self.canonical["bio_id"],
            "canonical_edition": self.canonical["edition_year"],
            "n_attestations": len(self.attestations),
            "attestation_bio_ids": [a["bio_id"] for a in self.attestations],
            "provenance": self.canonical.get("provenance", []),
        }


class _UF:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        self.p[self.find(a)] = self.find(b)


def _birth(b: dict) -> int | None:
    return b.get("birth_year")


def _same_person(a: dict, b: dict) -> bool:
    """Strong, conservative same-person test within a surname bucket."""
    if not _names_compatible(a.get("given_names"), b.get("given_names")):
        return False
    ba, bb = _birth(a), _birth(b)
    if ba is not None and bb is not None:
        if abs(ba - bb) <= 1:                       # birth year (OCR-tolerant)
            return _first_initial(a) == _first_initial(b) or not (_first_initial(a) and _first_initial(b))
        return False                                # different birth years -> different people
    # at least one lacks a birth year: require identical spelled given names
    sa, sb = _spelled_given(a), _spelled_given(b)
    return bool(sa) and sa == sb


def cluster_bios(bios: list[dict]) -> list[list[dict]]:
    """Union-find clustering within surname buckets."""
    buckets: dict[str, list[int]] = defaultdict(list)
    for i, b in enumerate(bios):
        buckets[surname_key(b)].append(i)
    uf = _UF(len(bios))
    for idxs in buckets.values():
        # O(k^2) within a surname bucket; buckets are small (rare-surname) to
        # moderate. Pairwise is fine at this corpus scale.
        for x in range(len(idxs)):
            for y in range(x + 1, len(idxs)):
                if _same_person(bios[idxs[x]], bios[idxs[y]]):
                    uf.union(idxs[x], idxs[y])
    groups: dict[int, list[dict]] = defaultdict(list)
    for i, b in enumerate(bios):
        groups[uf.find(i)].append(b)
    return list(groups.values())


def _richness(b: dict) -> int:
    return len(re.findall(r"\b1[789]\d\d\b", b["raw_text"])) * 100 + len(b["raw_text"])


def select_canonical(cluster: list[dict]) -> dict:
    """Richest = longest of the latest PRE-condensation attestations; if a
    person only appears post-1940, take their richest there."""
    pre = [b for b in cluster if b["edition_year"] <= _CONDENSE_CUTOFF]
    pool = pre or cluster
    latest = max(b["edition_year"] for b in pool)
    finalists = [b for b in pool if b["edition_year"] >= latest - 3]  # within ~one edition cycle
    return max(finalists, key=_richness)


def build_persons(bios: list[dict]) -> list[Person]:
    persons: list[Person] = []
    for cluster in cluster_bios(bios):
        canon = select_canonical(cluster)
        births = [b["birth_year"] for b in cluster if b.get("birth_year")]
        persons.append(Person(
            person_id="kgp_" + canon["bio_id"],
            surname=canon.get("surname") or canon["raw_text"].split(",", 1)[0],
            given_names=canon.get("given_names"),
            birth_year=births[0] if births else None,
            editions=[b["edition_year"] for b in cluster],
            canonical=canon,
            attestations=sorted(cluster, key=lambda b: b["edition_year"]),
        ))
    return persons


def load_all_bios(docs: tuple[str, ...], data_dir: str,
                  cache_dir: str | Path | None = None, refresh: bool = False) -> list[dict]:
    """Extract bios across every services-bearing edition of the given docs.

    Caches per-edition bios to ``cache_dir`` (default data/kg/bios/) so reruns
    skip the expensive full-corpus re-extraction (~7 min cold)."""
    cache = Path(cache_dir) if cache_dir else Path("data/kg/bios")
    cache.mkdir(parents=True, exist_ok=True)
    out: list[dict] = []
    for doc in docs:
        for year in reader.available_years(doc):
            cf = cache / f"{doc}{year}.jsonl"
            if cf.exists() and not refresh:
                out.extend(json.loads(l) for l in cf.open(encoding="utf-8"))
                continue
            blocks = reader.load_volume(year, doc)
            bios, _ = extract_bios(blocks, data_dir)
            rows = [b.to_json() for b in bios]
            with cf.open("w", encoding="utf-8") as fh:
                for r in rows:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            out.extend(rows)
    return out
