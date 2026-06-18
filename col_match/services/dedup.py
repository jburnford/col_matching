"""Cross-edition dedup: collapse ~200k entry instances into distinct
EntryVersions (the unit of parsing).

A person's entry is reprinted nearly verbatim year after year, usually with a
clause appended as the career grows. Within a (surname, first-initial) block,
entries are chained chronologically when the later text is the same as /
a prefix-extension of / highly similar to the earlier text. Each chain emits
one EntryVersion whose canonical text is the longest attestation. The 1948
reformat naturally breaks chains (compressed rewrite) — a person then has a
second version; that's fine, provenance keeps both.

Merging here is conservative by construction: two same-name people only
collapse if their *printed careers* are near-identical, which for real text
means they are the same person.
"""

from __future__ import annotations

import re
from collections import defaultdict

from rapidfuzz import fuzz

from .schema import EntryVersion, RawEntry

# similarity gates (0-100)
_SIM_FULL = 85.0      # whole-text similarity
_SIM_PREFIX = 88.0    # earlier text vs prefix of later text (career grew)

_TITLES = {
    "SIR", "HON", "THE", "REV", "DR", "MR", "CAPT", "CAPTAIN", "MAJ", "MAJOR",
    "COL", "COLONEL", "LIEUT", "LT", "GEN", "GENERAL", "BRIG", "ADM", "CMDR",
    "COMMANDER", "PROF", "MISS", "MRS", "LADY", "DAME", "VEN", "RT",
}


def surname_key(text: str) -> str:
    head = text.split(",", 1)[0]
    return re.sub(r"[^A-Z]", "", head.upper())


def first_initial(text: str) -> str:
    """First given-name initial after the surname, skipping titles/honours."""
    rest = text.split(",", 1)[1] if "," in text else ""
    rest = re.split(r"[—–]", rest, 1)[0]
    for token in re.split(r"[ ,.]+", rest):
        if not token:
            continue
        bare = re.sub(r"[^A-Za-z]", "", token).upper()
        if not bare or bare in _TITLES:
            continue
        # honours like KCMG / CBE / DSO are all-caps clumps; skip clumps of
        # 2-6 caps that aren't plausibly a name? Names are also caps in early
        # eras — use position: honours come after names, so the FIRST
        # non-title token is the given name (or initial).
        return bare[0]
    return "?"


def _block_key(e: RawEntry) -> str:
    return f"{surname_key(e.raw_text)}|{first_initial(e.raw_text)}"


def _same_version(earlier: str, later: str) -> bool:
    if fuzz.ratio(earlier, later) >= _SIM_FULL:
        return True
    # career grew: earlier text ~ prefix of later
    if len(later) > len(earlier):
        return fuzz.ratio(earlier, later[: len(earlier) + 40]) >= _SIM_PREFIX
    return False


def dedup_entries(entries: list[RawEntry]) -> tuple[list[EntryVersion], dict]:
    """Chain near-duplicate entries across editions into EntryVersions."""
    blocks: dict[str, list[RawEntry]] = defaultdict(list)
    for e in entries:
        blocks[_block_key(e)].append(e)

    versions: list[EntryVersion] = []
    for key, members in blocks.items():
        members.sort(key=lambda e: (e.edition_year, e.entry_id))
        chains: list[list[RawEntry]] = []
        for e in members:
            best = None
            for chain in chains:
                tail = chain[-1]
                if tail.edition_year == e.edition_year:
                    continue  # same-volume duplicates already handled (twins)
                if _same_version(tail.raw_text, e.raw_text):
                    best = chain
                    break
            if best is not None:
                best.append(e)
            else:
                chains.append([e])
        for chain in chains:
            canonical = max(chain, key=lambda e: len(e.raw_text))
            versions.append(
                EntryVersion(
                    version_id=f"{chain[0].entry_id}.v",
                    surname_key=key,
                    canonical_text=canonical.raw_text,
                    era=canonical.era,
                    edition_year=canonical.edition_year,
                    entry_ids=[e.entry_id for e in chain],
                    attesting_editions=sorted({e.edition_year for e in chain}),
                )
            )

    stats = {
        "instances": len(entries),
        "versions": len(versions),
        "ratio": round(len(entries) / max(len(versions), 1), 2),
        "singletons": sum(1 for v in versions if len(v.entry_ids) == 1),
    }
    return versions, stats
