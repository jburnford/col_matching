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

# Salary tokens that terminate a roster record. The layout-aware OCR renders
# the pound-sterling "l." as "/" on many pages ("1,600/, and duty allowance,
# 320/."), so both spellings are salary delimiters; "to/–/plus/by" chains are
# swallowed so scale tails don't spawn junk chunks.
_SALARY_UNIT = r"(?:l\.|/(?!\d))"
_SALARY = re.compile(
    r"(?:Rs\.?\s?[\d,]+(?:\.\d+)?|£\s?[\d,]+|\$\s?[\d,]+"
    rf"|\b\d[\d,]*\s?{_SALARY_UNIT}"
    rf"(?:\s*(?:to|by|plus|and|[-–—])\s*[\d,]+\s?{_SALARY_UNIT})*)"
)
# Colony-name shaped running header (all-caps words, &, hyphen, apostrophe;
# matched AFTER _header_norm, so page-spread compounds appear as "A--B").
_COLONY_HEADER = re.compile(r"^[A-Z][A-Z'’.&\- ]{2,70}\.?$")
_DASHES = re.compile(r"\s*(?:[—–]|--+)\s*")
_EDGE_NUM = re.compile(r"^\d+\s+|\s+\d+$")
# 1946-53 restructured staff lists run under "STAFFS : NIGERIA" headers.
_STAFFS = re.compile(r"^STAFFS?\s*[:;]\s*(.+)$", re.I)


def _header_norm(text: str) -> str:
    """Strip edge page numbers, normalize em/en dashes to '--', tidy spaces."""
    t = re.sub(r"\s+", " ", text.strip()).strip(". ")
    t = _EDGE_NUM.sub("", t).strip()
    return _DASHES.sub("--", t)


def _set_key(t: str) -> str:
    return re.sub(r"\s+", " ", t.upper().replace(".", "")).strip()


# Volume running titles that ALTERNATE with colony headers page-by-page:
# ignore them, the current colony stays in force on the facing page.
_IGNORE_HEADERS = {_set_key(k) for k in (
    "COLONIAL OFFICE LIST", "THE COLONIAL OFFICE LIST",
    "DOMINIONS OFFICE LIST", "THE DOMINIONS OFFICE LIST",
    "DOMINIONS OFFICE AND COLONIAL OFFICE LIST",
    "DOMINIONS OFFICE AND COLONIAL OFFICE LIS",           # OCR truncation
    "COMMONWEALTH RELATIONS OFFICE LIST",
    "THE COMMONWEALTH RELATIONS OFFICE LIST", "THE COLONIAL OFFICE",
)}
# Back-matter / front-matter sections: the colony scope ENDS here. Without the
# reset, everything after the last chapter (index, honours rolls, obituaries,
# adverts) inherited that chapter's colony — e.g. 8.5k phantom "ZANZIBAR"
# records in col1946.
_RESET_HEADERS = {_set_key(k) for k in (
    "CONTENTS", "INDEX", "ERRATA", "ADDENDA", "CORRIGENDA", "PREFACE",
    "APPENDIX", "APPENDICES", "OBITUARY", "ADVERTISEMENTS", "ADVERTISER",
    "WATERLOW & SONS LIMITED", "ORDER OF THE BRITISH EMPIRE",
    "COLONIAL ASSOCIATIONS", "INFORMATION AS TO COLONIAL APPOINTMENTS",
    "COLONIAL REGULATIONS", "INSTITUTIONS", "GENERAL INFORMATION",
    "IMPERIAL INSTITUTE", "ROYAL COLONIAL INSTITUTE",
    "IMPERIAL SERVICE ORDER", "KNIGHTS BACHELORS", "EMIGRATION",
    "ORDER OF ST MICHAEL AND ST GEORGE",
    "THE MOST DISTINGUISHED ORDER OF ST MICHAEL AND ST GEORGE",
    "TABLE OF PRECEDENCE", "EXPLANATION OF CERTAIN ABBREVIATIONS",
    "HARRISON AND SONS", "PUBLIC REVENUE AND EXPENDITURE",
    "LIST OF PARLIAMENTARY PAPERS ON COLONIAL AFFAIRS", "GEOGRAPHICAL INDEX",
    "LOCAL AND IMPERIAL ACTS OF GENERAL IMPORTANCE",
)}


def _colony_signal(text: str) -> tuple[str, str | None]:
    """Classify a header/title string: ('set', colony) | ('reset', None) |
    ('ignore', None)."""
    t = _header_norm(text)
    key = _set_key(t)
    if key in _RESET_HEADERS:
        return "reset", None
    if key in _IGNORE_HEADERS or not t:
        return "ignore", None
    m = _STAFFS.match(t)
    if m:
        t = m.group(1).strip().strip(". ")
    # colon hierarchy headers ("MALAYA: STRAITS SETTLEMENTS.", "LEEWARD
    # ISLANDS: DOMINICA.", 1930s editions) — same compound semantics as "--"
    t = re.sub(r"\s*:\s*", "--", t).strip("- ")
    if _COLONY_HEADER.match(t) and not any(ch.isdigit() for ch in t) and len(t) >= 3:
        return "set", t
    return "ignore", None


def colony_vocab(blocks) -> set[str]:
    """Colony names attested by this volume's running headers (compound
    segments included) — gates title-based chapter starts so a stray all-caps
    title can't invent a colony."""
    vocab: set[str] = set()
    for b in blocks:
        if b.category != "header":
            continue
        sig, col = _colony_signal(b.text)
        if sig == "set" and col:
            for seg in col.split("--"):
                seg = re.sub(r"^THE\s+", "", seg.strip(), flags=re.I)
                if seg:
                    vocab.add(_set_key(seg))
    return vocab


def _title_colony(text: str, vocab: set[str]) -> str | None:
    """Chapter-start titles ('WESTERN AUSTRALIA.', 'BARBADOS') mark the real
    boundary pages before the running header catches up — accept them only
    when the volume's own headers corroborate the name."""
    sig, col = _colony_signal(text)
    if sig != "set" or not col or "--" in col:
        return None
    key = _set_key(re.sub(r"^THE\s+", "", col, flags=re.I))
    return col if key in vocab else None
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
    # geographic/administrative words that pair into name-shaped bigrams
    # ("Northern Territories", "Eastern Province") — never person names here
    "territory", "territories", "provincial", "northern", "southern",
    "eastern", "western", "central", "colony", "protectorate", "division",
}


def _is_position_word(tok: str) -> bool:
    t = tok.lower().strip(".,")
    return t in _POSITION_WORD or t.rstrip("s") in _POSITION_WORD
_PARTICLES = {"de", "del", "della", "di", "da", "van", "von", "le", "la", "du",
              "des", "den", "ter", "st", "st.", "mac", "mc", "o'"}
_TRAIL_PAREN = re.compile(
    r"\((?:acting|vacant|on leave|temp\.?|ag\.?|supernumerary|seconded|retired"
    r"|[^)]*designate[^)]*)\)\.?", re.I)
_LEAD_AND = re.compile(r"^(?:and|&)\s+", re.I)
_INITIALS = re.compile(r"\b[A-Z]\.")


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
    if _is_position_word(core):
        return None
    given = " ".join(given_toks).strip(" .,") or None
    # a name should not itself read as a position phrase
    if given and all(_is_position_word(g) for g in given.split()):
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


def _seg_is_person(seg: str) -> tuple[str, str | None, list[str]] | None:
    """Stricter person test for name-run splitting: a segment is a person only
    if it parses as a name AND shows person morphology — a title prefix
    ("Capt. …"), initials ("C. F. D. O. Rew"), or >=2 mixed-case tokens
    ("John Maxwell"). A single bare capitalised word ("Ashanti") is NOT a
    person; it stays with the position text."""
    raw = _LEAD_AND.sub("", seg.strip())
    parsed = _parse_name(raw)
    if parsed is None:
        return None
    first_tok = raw.split()[0] if raw.split() else ""
    if rules_parse._is_title(first_tok) or _INITIALS.search(raw):
        return parsed
    toks = [t for t in raw.split() if t.strip(".,")]
    if len(toks) >= 2 and all(re.match(r"^[A-Z][a-z'’\-]", t) for t in toks[:2]) \
            and not any(_is_position_word(t) for t in toks):
        return parsed
    return None


def _parse_record_chunk(chunk: str) -> list[tuple[str | None, str, str | None, list[str]]]:
    """chunk (position + name-run + honours, salary already stripped) ->
    list of (position, surname, given, honours). Period rosters bind ONE
    position to a RUN of names ("Provincial Commissioners, A, B, C, … salary"),
    so every person-shaped segment after the position becomes its own record,
    all sharing the position; honour-only segments attach to the record they
    follow."""
    segs = [s.strip() for s in chunk.split(",") if s.strip()]
    if not segs:
        return []
    out: list[tuple[str | None, str, str | None, list[str]]] = []
    position_parts: list[str] = []
    for seg in segs:
        if _is_honour_seg(_TRAIL_PAREN.sub("", seg).strip()):
            if out:                       # honour rides with the preceding name
                out[-1][3].append(_TRAIL_PAREN.sub("", seg).strip().rstrip("."))
            continue
        person = _seg_is_person(seg)
        if person is not None:
            surname, given, honours = person
            out.append((None, surname, given, list(honours)))
        elif not out:
            position_parts.append(seg)    # still reading the position
        # else: trailing junk between/after names ("and duty allowance") — skip
    if not out:
        # fall back to the permissive right-most-name rule so simple
        # "Position, Name." records without person morphology still parse
        honours = []
        while segs and _is_honour_seg(segs[-1]):
            honours.insert(0, segs.pop().rstrip("."))
        if not segs:
            return []
        name = _parse_name(segs[-1])
        if name is None:
            return []
        surname, given, name_honours = name
        position = ", ".join(segs[:-1]).strip(" .:—–-") or None
        return [(position, surname, given, honours + name_honours)]
    position = ", ".join(position_parts).strip(" .:—–-") or None
    return [(position, s, g, h) for _, s, g, h in out]


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

    vocab = colony_vocab(blocks[:upper])
    for b in blocks[:upper]:
        stats["blocks_scanned"] += 1
        if b.category == "header":
            sig, h = _colony_signal(b.text)
            if sig == "reset":
                colony, department, in_roster = None, None, False
            elif sig == "set" and h != colony:
                colony = h
                department = None
                in_roster = False
                seen_colonies.add(h)
            continue
        if b.category == "title":
            sig, _ = _colony_signal(b.text)
            if sig == "reset":
                colony, department, in_roster = None, None, False
                continue
            tcol = _title_colony(b.text, vocab)
            if tcol is not None and tcol != colony:
                colony, department, in_roster = tcol, None, False
                seen_colonies.add(tcol)
                continue
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
        rec_no = 0
        for chunk, salary in chunks:
            for position, surname, given, honours in _parse_record_chunk(chunk):
                block_had += 1
                rid = f"{b.doc}{b.edition_year}-p{b.page}b{b.index}r{rec_no}"
                rec_no += 1
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
    vocab = colony_vocab(blocks[:upper])
    for b in blocks[:upper]:
        if b.category == "header":
            sig, h = _colony_signal(b.text)
            if sig == "reset":
                colony, department, in_roster = None, None, False
            elif sig == "set" and h != colony:
                colony, department, in_roster = h, None, False
            continue
        if b.category == "title":
            sig, _ = _colony_signal(b.text)
            if sig == "reset":
                colony, department, in_roster = None, None, False
                continue
            tcol = _title_colony(b.text, vocab)
            if tcol is not None and tcol != colony:
                colony, department, in_roster = tcol, None, False
                continue
            if _PROFILE_TITLE.search(b.text):
                in_roster = False
            elif _ROSTER_TITLE.search(b.text):
                in_roster, department = True, b.text.strip().rstrip(".")
            continue
        if b.category == "text" and colony is not None and in_roster and len(b.text) > 15:
            out.append({"colony": colony, "department": department,
                        "text": b.text, "provenance": b.prov})
    return out
