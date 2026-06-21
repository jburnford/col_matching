"""Detect (and help recover) CONCATENATED biographies.

OCR sometimes merges several printed entries into one `raw_text` — the page
break between people was lost, so two-to-six distinct persons share a single
bio block. Structuring only captured the FIRST, so the rest are missing persons
(~0.8% of entries; audit finding, docs/STRUCT_ERROR_CATALOG.md).

The reliable boundary signal in this OCR is the header→body em-dash `—`: each
printed entry opens with an UPPERCASE surname/title header and then a dash. A
single entry has one such dash; a concatenated block has several, each preceded
by an uppercase-dominant header. The comma after the surname is NOT reliable
(`ARMSTRONG J. R.—` has none), so we key on the dash + caps-fraction, not commas.

`persons(raw_text)` returns the detected person headers with their split offsets
(offset 0 = the original first person; later offsets = recovered persons).
"""

from __future__ import annotations

import re

_DASH = re.compile(r"[—–]")
# a header candidate: from string start or a sentence boundary ". ", up to the
# header→body dash. Bounded length so a long body can't masquerade as a header.
_HEADER = re.compile(r"(?:^|\.\s+)([A-Z][A-Za-z0-9'’.,()\-/ ]{1,120}?)\s*[—–]")


def _caps_fraction(s: str) -> float:
    al = [c for c in s if c.isalpha()]
    return sum(c.isupper() for c in al) / len(al) if al else 0.0


def _is_header(h: str) -> bool:
    """Uppercase-dominant and carries a surname-like all-caps token."""
    return _caps_fraction(h) >= 0.6 and bool(re.search(r"\b[A-Z]{2,}\b", h))


def _refine_start(header: str) -> int:
    """Offset within a captured header where the true header begins — strips
    only PREVIOUS-BODY text the capture swept in ('Guiana, 1955. EU CHEOW
    CHYE.' -> offset of 'EU'). Body intrusion contains lowercase; a real header
    (incl. internal periods like 'ST. QUINTIN') is all-caps, so we cut only at a
    '. ' whose prefix has lowercase AND whose suffix is still caps-dominant."""
    best = 0
    for m in re.finditer(r"\.\s+", header):
        prefix, suffix = header[: m.start()], header[m.end():]
        if re.search(r"[a-z]", prefix) and _caps_fraction(suffix) >= 0.7:
            best = m.end()
    return best


def persons(raw_text: str) -> list[dict]:
    """Detected person headers in reading order. Each item:
    {surname_guess, header, start} where `start` is the char offset in raw_text
    at which that person's segment begins (the first is always 0)."""
    found: list[dict] = []
    for m in _HEADER.finditer(raw_text):
        h = m.group(1).strip()
        if not _is_header(h):
            continue
        # tighten the boundary to the surname run inside the captured header
        rel = _refine_start(m.group(1))
        start = m.start(1) + rel
        # surname = up to the first comma (surnames keep internal periods:
        # 'ST. QUINTIN, C.' -> 'ST. QUINTIN')
        surname = m.group(1)[rel:].split(",", 1)[0].strip().rstrip(".") or None
        found.append({"surname_guess": surname, "header": h, "start": start})
    if not found:
        return [{"surname_guess": None, "header": None, "start": 0}]
    found[0]["start"] = 0          # the entry's own header always anchors at 0
    return found


def segments(raw_text: str) -> list[tuple[str, str]]:
    """Split a (possibly concatenated) raw_text into (surname_guess, segment)
    pairs, one per detected person, using the header offsets."""
    ps = persons(raw_text)
    out = []
    for i, p in enumerate(ps):
        end = ps[i + 1]["start"] if i + 1 < len(ps) else len(raw_text)
        out.append((p["surname_guess"], raw_text[p["start"]:end].strip()))
    return out


def n_persons(raw_text: str) -> int:
    return len(persons(raw_text))


def scan_corpus(persons_path, bios_glob: str = "data/kg/bios/*.jsonl") -> list[dict]:
    """Scan every canonical bio named by the persons spine for concatenated
    entries (2+ person headers). Returns one row per concatenated entry:
    {person_id, canonical_bio_id, n_persons, header_surnames, split_offsets}."""
    import glob
    import json

    bio = {}
    for f in glob.glob(bios_glob):
        for l in open(f, encoding="utf-8"):
            b = json.loads(l)
            bio[b["bio_id"]] = b.get("raw_text", "")
    out = []
    for l in open(persons_path, encoding="utf-8"):
        p = json.loads(l)
        ps = persons(bio.get(p["canonical_bio_id"], ""))
        if len(ps) >= 2:
            out.append({
                "person_id": p["person_id"],
                "canonical_bio_id": p["canonical_bio_id"],
                "n_persons": len(ps),
                "header_surnames": [x["surname_guess"] for x in ps],
                "split_offsets": [x["start"] for x in ps],
            })
    return out
