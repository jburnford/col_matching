"""Deterministic (rules) parsing tier for services entries.

Parses an EntryVersion's canonical text into a ParsedEntry. Returns None when
the entry can't be FULLY accounted for — any clause containing a year that
doesn't parse cleanly fails the whole entry to the LLM tier. The rules tier
therefore never emits a sloppy parse; validate.py applies the same gates to
both tiers.

Entry grammar (all eras):
  SURNAME, [titles] Given Names[, honours (year), ...].—[B. yyyy;] [ed. ...;]
  position, place, date; position, date; ...; retired, yyyy.
"""

from __future__ import annotations

import re

from . import gazetteer
from .schema import CareerEvent, EntryVersion, Honour, ParsedEntry, Terminal

_DASH_SPLIT = re.compile(r"\s*[—–]\s*")

# honours: dotted-caps clumps (K.C.M.G., C.B.E., D.S.O.) and knighthood forms
_HONOUR = re.compile(
    r"^((?:[A-Z]\.\s?){2,}[A-Z]?\.?|Kt\.?|Knt\.?(?:\s?Bach\.?)?|Bart\.?|Bt\.?"
    r"|[A-Z][A-Za-z.'’ ]+)\s*(?:\((\d{4})\))?\s*\.?$"
)
_DOTTED_CAPS = re.compile(r"^(?:[A-Z]\.\s?){2,}[A-Z]?\.?$|^(?:Kt|Knt|Bart|Bt)\.?$")
# orders/decorations/degrees that can open the post-surname segment list;
# anything else dotted in first position is treated as initials, not honours
_KNOWN_HONOURS = {
    "GCMG", "KCMG", "CMG", "GCB", "KCB", "CB", "GBE", "KBE", "CBE", "OBE",
    "MBE", "GCVO", "KCVO", "CVO", "MVO", "GCSI", "KCSI", "CSI", "GCIE",
    "KCIE", "CIE", "DSO", "MC", "VC", "DFC", "AFC", "ISO", "ED", "KT", "KNT",
    "BART", "BT", "QC", "KC", "LLD", "LLB", "LLM", "MD", "MB", "BS", "BSC",
    "MSC", "BA", "MA", "PHD", "DCL", "FRGS", "MRAS", "FRCS", "MRCS", "FRS",
    "CPM", "OBI",
}


def _known_honour(token: str) -> bool:
    return re.sub(r"[^A-Za-z]", "", token).upper() in _KNOWN_HONOURS

_TITLE_WORD = re.compile(
    r"^(?:THE|HON|RT|REV|VEN|SIR|DAME|LADY|MISS|MRS|MR|DR|PROF"
    r"|CAPT(?:AIN)?|MAJ(?:OR)?|COL(?:ONEL)?|LIEUT(?:ENANT)?|LT|GEN(?:ERAL)?"
    r"|BRIG(?:ADIER)?|ADM(?:IRAL)?|CMDR|COMMANDER|COMMANDANT|SQN|FLT|WING"
    r"|BREVET|AIR|VICE|REAR|COMMODORE|SURGEON)\.?,?$",
    re.I,
)


def _is_title(token: str) -> bool:
    """True for simple titles and hyphenated compounds (BRIG.-GEN., LIEUT.-COL.)."""
    parts = [p for p in token.split("-") if p.strip(". ,")]
    return bool(parts) and all(_TITLE_WORD.match(p.strip(", ")) for p in parts)

_MONTH = r"(?:Jan|Feb|Mar|Apr|Apl|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)[a-z]*\.?"
# trailing date on a clause: [day] [Month][, ] [Month to Month] YEAR [to YEAR|-YY]
_DATE_TAIL = re.compile(
    rf"[,\s]*(?:on\s+)?(?:\d{{1,2}}(?:st|nd|rd|th)?\s+)?(?:{_MONTH}\s*(?:to\s+(?:\d{{1,2}}(?:st|nd|rd|th)?\s+)?{_MONTH}\s*)?)?,?\s*"
    rf"(1[789]\d\d)(?:\s*(?:to|[-–—])\s*(?:(?:\d{{1,2}}(?:st|nd|rd|th)?\s+)?{_MONTH}\s*)?,?\s*(1[789]\d\d|\d{{1,2}}))?\s*[.)\]]*$"
)
# multi-event clause: "reg.-gen., 1887, and M.L.C., 1889" splits on ", and"
_AND_SPLIT = re.compile(r",\s+and\s+|\s+and\s+(?=[A-Z])")
_ANY_YEAR = re.compile(r"\b1[789]\d\d\b")

_BIRTH = re.compile(r"^b(?:orn)?\.?,?\s*(?:at\s+[A-Za-z .,'-]+,\s*)?(1[789]\d\d)\b[.,]?\s*(.*)$", re.I)
_EDUCATION = re.compile(r"^ed(?:uc(?:ated)?)?\.?,?\s", re.I)
_MIL = re.compile(r"^(?:on\s+)?(?:mil|war|active)\.?\s?serv", re.I)
_TERMINAL = re.compile(
    r"^(retired|retd|resigned|resig|died|pensioned|invalided)\b\.?,?\s*(.*)$", re.I
)
_TERMINAL_KIND = {
    "retired": "retired", "retd": "retired", "pensioned": "pensioned",
    "resigned": "resigned", "resig": "resigned", "died": "died",
    "invalided": "invalided",
}
_DITTO = re.compile(r"^(?:do|ditto)\.?$", re.I)


def _expand_year_end(start: int, end_raw: str | None) -> int | None:
    if not end_raw:
        return None
    if len(end_raw) == 4:
        return int(end_raw)
    # "1914-19" -> 1919; "1883-4" -> 1884
    return int(str(start)[: 4 - len(end_raw)] + end_raw)


def _parse_name_block(block: str, parsed: ParsedEntry) -> bool:
    block = block.strip().rstrip(".")
    if "," not in block:
        return False
    surname, rest = block.split(",", 1)
    parsed.surname = surname.strip()
    if not parsed.surname:
        return False
    segments = [s.strip() for s in rest.split(",") if s.strip()]
    titles: list[str] = []
    given: list[str] = []
    seen_given = False
    for i, seg in enumerate(segments):
        m = _HONOUR.match(seg)
        if m and (_DOTTED_CAPS.match(m.group(1).strip()) or m.group(2)):
            # dotted-caps honour, or anything carrying an award year — BUT
            # the first segment is given names unless it's a known honour
            # ("BRACE, T. E. D." has initials, not a decoration)
            if seen_given or _known_honour(m.group(1)) or m.group(2):
                parsed.honours.append(
                    Honour(award=m.group(1).strip().rstrip("."), year=int(m.group(2)) if m.group(2) else None)
                )
                continue
        if seen_given:
            # post-given non-honour segment (residence etc.) -> note
            parsed.notes.append(seg)
            parsed.flags.append(f"name_block_extra:{seg[:40]}")
            continue
        # first non-honour segment: titles + given names
        for tok in seg.split():
            if not seen_given and _is_title(tok):
                titles.append(tok)
            else:
                seen_given = True
                given.append(tok)
        seen_given = True
    parsed.title_rank = " ".join(titles) or None
    parsed.given_names = " ".join(given).strip(" .") or None
    return True


def _parse_event_clause(
    clause: str, prev_position: str | None, prev_place: str | None, data_dir: str
) -> list[tuple[CareerEvent, bool]] | None:
    """Parse one career clause into >=1 (event, place_inherited) tuples.
    None = not a cleanly parseable dated event (caller decides what's next)."""
    dm = _DATE_TAIL.search(clause)
    if not dm:
        return None
    year_start = int(dm.group(1))
    year_end = _expand_year_end(year_start, dm.group(2))
    remainder = clause[: dm.start()].strip(" ,.")
    if _ANY_YEAR.search(remainder):
        # multiple events in one clause ("reg.-gen., 1887, and M.L.C., 1889"):
        # try the ", and" split; every part must itself parse as a dated event
        parts = _AND_SPLIT.split(clause)
        if len(parts) < 2:
            return None
        out: list[tuple[CareerEvent, bool]] = []
        for part in parts:
            sub = _parse_event_clause(part.strip(" ,."), prev_position, prev_place, data_dir)
            if sub is None or len(sub) != 1:
                return None
            out.extend(sub)
            prev_position, prev_place = sub[0][0].position, sub[0][0].place
        return out

    position: str | None
    place: str | None
    place_inherited = False
    if not remainder or _DITTO.match(remainder):
        position, place = prev_position, prev_place
        place_inherited = not remainder
    else:
        segs = [s.strip() for s in remainder.split(",") if s.strip()]
        hit = gazetteer.lookup(segs[-1], data_dir)
        if hit is not None:
            place = hit
            position = ", ".join(segs[:-1]) or prev_position
        else:
            # place embedded in the segment ("Ceylon civ. ser.", "G.C. rwy.")
            # or a dotted office abbreviation ("assigned to the C.O.")
            hit = gazetteer.lookup_prefix(segs[-1], data_dir) or gazetteer.lookup_office(remainder)
            if hit is not None:
                place = hit
                position = remainder
            else:
                place = prev_place
                place_inherited = place is not None
                position = remainder
        if _DITTO.match(position or ""):
            position = prev_position
    event = CareerEvent(
        position=position, place=place,
        year_start=year_start, year_end=year_end, text_span=clause,
        place_inherited=place_inherited and place is not None,
    )
    return [(event, place_inherited)]


def parse_rules(version: EntryVersion, data_dir: str) -> ParsedEntry | None:
    """Parse one entry deterministically; None routes it to the LLM tier."""
    parts = _DASH_SPLIT.split(version.canonical_text, 1)
    if len(parts) != 2:
        return None
    name_block, career = parts
    parsed = ParsedEntry(version_id=version.version_id, surname="", parser="rules")
    if not _parse_name_block(name_block, parsed):
        return None

    clauses = [c.strip() for c in re.split(r"\s*;\s*", career) if c.strip()]
    if not clauses:
        return None

    prev_position: str | None = None
    prev_place: str | None = None
    for idx, clause in enumerate(clauses):
        is_last = idx == len(clauses) - 1

        # late-era entries end with "(Nig. Govt. service.)" etc. after the
        # final date — peel trailing parentheticals off into notes first
        pm = re.search(r"\s*\(([^()]{0,60})\)\.?\s*$", clause)
        if pm and not _ANY_YEAR.search(pm.group(1)):
            parsed.notes.append(pm.group(1))
            clause = clause[: pm.start()].rstrip(" .,")

        m = _BIRTH.match(clause)
        if m and parsed.birth_year is None and idx <= 1:
            parsed.birth_year = int(m.group(1))
            if m.group(2):
                parsed.notes.append(m.group(2))
            continue
        if _EDUCATION.match(clause):
            parsed.education = clause
            continue
        if _MIL.match(clause):
            parsed.notes.append(clause)
            continue
        if is_last:
            t = _TERMINAL.match(clause)
            if t:
                year_m = _ANY_YEAR.search(t.group(2) or "")
                parsed.terminal = Terminal(
                    kind=_TERMINAL_KIND[t.group(1).lower().rstrip(".")],
                    year=int(year_m.group()) if year_m else None,
                    text_span=clause,
                )
                continue

        events = _parse_event_clause(clause, prev_position, prev_place, data_dir)
        if events:
            for event, inherited in events:
                parsed.events.append(event)
                if inherited and event.place is not None:
                    parsed.flags.append(f"place_inherited:{len(parsed.events) - 1}")
                prev_position, prev_place = event.position, event.place
            continue

        # undated clause: harmless narrative only if it carries no year at all
        if not _ANY_YEAR.search(clause):
            parsed.notes.append(clause)
            continue
        # clause has a year but didn't parse -> the whole entry goes to the LLM
        return None

    if not parsed.events:
        return None
    return parsed
