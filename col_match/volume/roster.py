"""By-colony staff-list (roster) extraction from layout-aware OCR blocks.

Within an edition, colony establishment sections run: a running ``header`` block
carrying the colony name (``CEYLON.``, repeated each page), ``title`` blocks for
the department / province / establishment, and ``text`` blocks holding the
roster itself in the period shape ``Position, [Title] Name[, honours], Salary.``
repeated. Salaries (``Rs. 20,250`` / ``700l.`` / ``£1,000``) are strong record
delimiters; the name is the right-most non-honour segment before the salary.

This is a deterministic, recall-leaning parser — noise records simply fail to
match anything downstream (the within-volume matcher gates hard on
surname+initials+colony). Garbled blocks the rules tier mis-handles are the
Qwen LLM tier's job on the GPU box (see ``llm.py``); this module emits the
deterministic pass and flags blocks it could not parse.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..services import rules_parse
from .reader import Block

# Salary tokens that terminate a roster record.
_SALARY = re.compile(
    r"(?:Rs\.?\s?[\d,]+(?:\.\d+)?|£\s?[\d,]+|\$\s?[\d,]+"
    r"|\b\d[\d,]*l\.(?:\s*(?:to|[-–—])\s*[\d,]*l\.)?)"
)
# Colony-name shaped running header (all-caps words, &, hyphen, apostrophe).
_COLONY_HEADER = re.compile(r"^[A-Z][A-Z'’.&\- ]{2,40}\.?$")
# Headers that are NOT colonies.
_NOT_COLONY = {
    "COLONIAL OFFICE LIST", "DOMINIONS OFFICE LIST",
    "COMMONWEALTH RELATIONS OFFICE LIST", "CONTENTS", "INDEX", "ERRATA",
    "ADVERTISEMENTS", "ADVERTISER",
}
# Titles that open / belong to a roster region.
_ROSTER_TITLE = re.compile(
    r"establishment|government|gov(?:ernment)? agenc|judicial|legislat|executive"
    r"|council|department|secretariat|police|constabulary|customs|medical|sanitary"
    r"|education|public works|p\.?w\.?d|treasury|audit|survey|civil service|judiciary"
    r"|magistracy|ecclesiastic|post(?:al)? office|railway|prison|forest|agricultur"
    r"|district|province|circuit|commission", re.I,
)
# Titles that mark colony-profile prose (NOT a roster).
_PROFILE_TITLE = re.compile(
    r"constitution|population|area|statistic|history|geograph|finance|revenue"
    r"|trade|commerce|currency|bank|climate|import|export|shipping|product|religion"
    r"|language|communication|telegraph|note", re.I,
)
# Position words that must never be taken as a surname.
_POSITION_WORD = {
    "agent", "officer", "secretary", "governor", "commissioner", "magistrate",
    "judge", "assistant", "clerk", "treasurer", "registrar", "surveyor",
    "inspector", "superintendent", "auditor", "director", "collector",
    "member", "president", "chairman", "engineer", "principal", "warden",
    "department", "establishment", "province", "district", "council", "office",
    "service", "vacant", "acting",
}
_PARTICLES = {"de", "del", "della", "di", "da", "van", "von", "le", "la", "du",
              "des", "den", "ter", "st", "st.", "mac", "mc", "o'"}
_TRAIL_PAREN = re.compile(r"\((?:acting|vacant|on leave|temp\.?|ag\.?)\)\.?", re.I)


@dataclass
class VolumeRecord:
    record_id: str
    edition_year: int
    colony: str                 # raw running-header colony name
    department: str | None      # nearest roster title
    position: str | None
    name_raw: str
    surname: str
    given_names: str | None
    honours: list[str]
    salary: str | None
    snippet: str
    provenance: dict = field(default_factory=dict)

    def to_json(self) -> dict:
        return self.__dict__


def _is_honour_seg(seg: str) -> bool:
    s = seg.strip().rstrip(".")
    return bool(rules_parse._DOTTED_CAPS.match(s)) or rules_parse._known_honour(s)


def _parse_name(seg: str) -> tuple[str, str | None, list[str]] | None:
    """seg -> (surname, given_names, honours) or None if not a person name."""
    seg = _TRAIL_PAREN.sub("", seg).strip().strip(".").strip()
    if not seg:
        return None
    tokens = seg.split()
    # peel leading titles (Sir, Hon., Capt., Lieut.-Col. …)
    honours: list[str] = []
    while tokens and rules_parse._is_title(tokens[0]):
        tokens.pop(0)
    # peel trailing honour tokens (dotted caps / known awards)
    while tokens and (rules_parse._DOTTED_CAPS.match(tokens[-1].rstrip(".")) or
                      rules_parse._known_honour(tokens[-1])):
        honours.insert(0, tokens.pop().rstrip(","))
    if not tokens:
        return None
    # surname = last token, absorbing a preceding particle (de Livera, Mc …)
    surname = tokens[-1].strip(",")
    given_toks = tokens[:-1]
    if given_toks and given_toks[-1].lower().strip(".") in _PARTICLES:
        surname = given_toks.pop() + " " + surname
    # validity: real surname, not a position word, starts uppercase
    core = surname.split()[-1]
    if not re.match(r"^[A-Z][A-Za-z'’.\-]{1,}$", core):
        return None
    if core.lower().strip(".") in _POSITION_WORD:
        return None
    given = " ".join(given_toks).strip(" .,") or None
    # a name should not itself read as a position phrase
    if given and all(g.lower().strip(".") in _POSITION_WORD for g in given.split()):
        return None
    return surname, given, honours


def _split_records(text: str) -> list[tuple[str, str | None]]:
    """Cut a roster text block into (record_text, salary) on salary markers."""
    out: list[tuple[str, str | None]] = []
    prev = 0
    for m in _SALARY.finditer(text):
        chunk = text[prev:m.start()].strip(" .,;:—–-")
        if chunk:
            out.append((chunk, m.group()))
        prev = m.end()
    return out


_EMDASH = re.compile(r"\s*[—–]\s*")


def _split_records_emdash(text: str) -> list[tuple[str, str | None]]:
    """Late-era rosters print ``Position—Name, honours.`` (em-dash, usually no
    salary). Bind each position (tail before a dash) to the name run after it,
    up to the next position-dash. Returns (record_text, None)."""
    parts = _EMDASH.split(text)
    if len(parts) < 2:
        return []
    out: list[tuple[str, str | None]] = []
    for k in range(len(parts) - 1):
        # position = last clause of parts[k]; name run = first clause of parts[k+1]
        position = re.split(r"(?<=[.])\s+|;\s+", parts[k].strip())[-1]
        nxt = parts[k + 1].strip()
        name_run = re.split(r"(?<=[.])\s+|;\s+", nxt)[0]
        chunk = f"{position}, {name_run}".strip(" ,")
        if chunk:
            out.append((chunk, None))
    return out


def _parse_record_chunk(chunk: str) -> tuple[str | None, str, str | None, list[str]] | None:
    """chunk (position + name + honours, salary already stripped) ->
    (position, surname, given, honours) or None."""
    segs = [s.strip() for s in chunk.split(",") if s.strip()]
    if not segs:
        return None
    # drop trailing honour-only segments, remember them
    honours: list[str] = []
    while segs and _is_honour_seg(segs[-1]):
        honours.insert(0, segs.pop().rstrip("."))
    if not segs:
        return None
    # right-most remaining segment is the name; the rest is the position
    name = _parse_name(segs[-1])
    if name is None:
        return None
    surname, given, name_honours = name
    position = ", ".join(segs[:-1]).strip(" .:—–-") or None
    return position, surname, given, honours + name_honours


def extract_records(
    blocks: list[Block], stop_at: int | None = None
) -> tuple[list[VolumeRecord], dict]:
    """Walk blocks up to ``stop_at`` (typically the services-section start);
    track current colony from running headers and emit roster records."""
    stats = {"blocks_scanned": 0, "roster_blocks": 0, "n_records": 0, "colonies": 0}
    records: list[VolumeRecord] = []
    colony: str | None = None
    department: str | None = None
    in_roster = False
    seen_colonies: set[str] = set()
    upper = stop_at if stop_at is not None else len(blocks)

    for b in blocks[:upper]:
        stats["blocks_scanned"] += 1
        if b.category == "header":
            h = b.text.strip().rstrip(".").strip()
            if _COLONY_HEADER.match(b.text) and h.upper() not in _NOT_COLONY \
                    and not any(ch.isdigit() for ch in h) and len(h) >= 3:
                if h != colony:
                    colony = h
                    department = None
                    in_roster = False
                    seen_colonies.add(h)
            continue
        if b.category == "title":
            if _PROFILE_TITLE.search(b.text):
                in_roster = False
            elif _ROSTER_TITLE.search(b.text):
                in_roster = True
                department = b.text.strip().rstrip(".")
            continue
        if b.category != "text" or colony is None:
            continue
        # require a title-gated roster region — profile prose (which can also
        # carry "Rs. …" figures, e.g. municipal debt) precedes the
        # establishment title, so a salary-only gate leaks sentences as records.
        if not in_roster:
            continue
        chunks = _split_records(b.text)
        if not chunks and ("—" in b.text or "–" in b.text):
            chunks = _split_records_emdash(b.text)
        if not chunks:
            continue
        block_had = 0
        for ci, (chunk, salary) in enumerate(chunks):
            parsed = _parse_record_chunk(chunk)
            if parsed is None:
                continue
            position, surname, given, honours = parsed
            block_had += 1
            rid = f"{b.doc}{b.edition_year}-p{b.page}b{b.index}r{ci}"
            records.append(VolumeRecord(
                record_id=rid, edition_year=b.edition_year, colony=colony,
                department=department, position=position,
                name_raw=(given + " " if given else "") + surname,
                surname=surname, given_names=given, honours=honours,
                salary=salary, snippet=chunk[:160], provenance=b.prov,
            ))
        if block_had:
            stats["roster_blocks"] += 1

    stats["n_records"] = len(records)
    stats["colonies"] = len(seen_colonies)
    return records, stats


def collect_roster_blocks(
    blocks: list[Block], stop_at: int | None = None
) -> list[dict]:
    """Raw text blocks inside title-gated roster regions, with their colony /
    department context and provenance — the worklist for the Qwen LLM tier to
    re-extract records from (higher recall on run-on lists than the
    deterministic parser). Mirrors the gating in :func:`extract_records`."""
    out: list[dict] = []
    colony: str | None = None
    department: str | None = None
    in_roster = False
    upper = stop_at if stop_at is not None else len(blocks)
    for b in blocks[:upper]:
        if b.category == "header":
            h = b.text.strip().rstrip(".").strip()
            if _COLONY_HEADER.match(b.text) and h.upper() not in _NOT_COLONY \
                    and not any(ch.isdigit() for ch in h) and len(h) >= 3 and h != colony:
                colony, department, in_roster = h, None, False
            continue
        if b.category == "title":
            if _PROFILE_TITLE.search(b.text):
                in_roster = False
            elif _ROSTER_TITLE.search(b.text):
                in_roster, department = True, b.text.strip().rstrip(".")
            continue
        if b.category == "text" and colony is not None and in_roster and len(b.text) > 15:
            out.append({"colony": colony, "department": department,
                        "text": b.text, "provenance": b.prov})
    return out
