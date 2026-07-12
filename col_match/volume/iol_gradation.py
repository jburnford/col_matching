"""Gradation-list extraction from the India Office List OCR: the seniority
rosters that fill 37-54% of the pre-1886 semiannual volumes and persist in
the annuals to the 1900s.

Two grammars (surveyed 1865, 1875, 1885, 1901):

CIVIL — covenanted civil servants per establishment::

    <h2>GRADATION LIST OF COVENANTED CIVIL SERVANTS ON THE
        BENGAL ESTABLISHMENT.</h2>
    <h3><i>First Class.</i></h3>
    <p align=center>1848</p>                 <- year of entry (covenant year)
    <p>Oldfield, R. C., Judge of High Court of Judicature, N.W. Provs.</p>

ARMY — officers by rank::

    <h2>MAJOR-GENERALS (87).</h2>
    <p align=center>1867</p>                 <- year of promotion to the rank
    <li>1819 Bayley, J. W., M.S.C., 13 Mar.</li>
        ^first commission        ^corps ^promotion day (year = group)

Both grammars also print inside two-column <table> cells in some OCR runs;
cells are processed in document order (column-major per cell, no
interleaving). Value: each entry is (person, grade/class, seniority year,
current appointment) — two attestations per year back to 1861, twenty-five
years before the biographical record begins.
"""

from __future__ import annotations

import html as _html
import re
from dataclasses import dataclass, field

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_BR = re.compile(r"<br\s*/?>", re.I)
_BLOCK = re.compile(r"<(p|h1|h2|h3|li|table)\b[^>]*>(.*?)</\1>", re.I | re.S)
_INNER = re.compile(r"<(p|li|h3)\b[^>]*>(.*?)</\1>", re.I | re.S)

_CIVIL_HEAD = re.compile(
    r"GRADATION LIST OF (?:THE )?(?:COVENANTED )?CIVIL SERVANTS?"
    r"(?: ON THE (.{3,40}?) ESTABLISHMENT)?", re.I)
_CLASS = re.compile(r"^(First|Second|Third|Fourth|Fifth|Sixth)\s+Class\.?$",
                    re.I)
_RANKS = ("GENERALS", "LIEUTENANT-GENERALS", "LIEUT.-GENERALS",
          "MAJOR-GENERALS", "COLONELS", "LIEUTENANT-COLONELS",
          "LIEUT.-COLONELS", "MAJORS", "CAPTAINS", "LIEUTENANTS",
          "SECOND LIEUTENANTS", "ENSIGNS", "CORNETS", "SURGEONS-GENERAL",
          "DEPUTY SURGEONS-GENERAL", "BRIGADE-SURGEONS", "SURGEONS-MAJOR",
          "SURGEONS")
_RANK_HEAD = re.compile(
    r"^(" + "|".join(re.escape(r) for r in _RANKS) +
    r")\s*(?:\(\d+\))?[.,]?$", re.I)
_YEAR_GROUP = re.compile(r"^\*?\s*(1[789]\d\d)\.?\s*$")
_DATE_TAIL = re.compile(
    r",?\s*(\d{1,2})\s+(Jan|Feb|Mar|March|Apr|April|May|June|Jun|July|Jul"
    r"|Aug|Sept|Sep|Oct|Nov|Dec)\.?\s*$")
_MONTH_N = {"jan": 1, "feb": 2, "mar": 3, "march": 3, "apr": 4, "april": 4,
            "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8,
            "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12}
_LETTERS = re.compile(r"^(?:[A-Z][a-z]?\.?\s*){1,6}$")
_CORPS = re.compile(
    r"^(B|M|Bo)\.?(S\.?C|I|C|A|E|N|Inf|Cav|Art)\.?$|^(S\.?C|R\.?E|R\.?A"
    r"|M\.?S\.?C|B\.?S\.?C|Bo\.?S\.?C|I\.?S\.?C|St\.?C)\.?$")
_FURL = re.compile(r"[—-]\s*on\s+(furl(ough)?|leave)\.?\s*$", re.I)


def _text(fragment: str) -> str:
    return _WS.sub(" ", _html.unescape(_TAG.sub(" ", fragment))).strip()


@dataclass
class GradationRecord:
    edition_year: int
    edition_tag: str
    list_type: str               # civil | army
    establishment: str | None    # BENGAL / MADRAS / BOMBAY / None
    section: str | None          # civil class or army rank
    group_year: int | None       # civil: entry year; army: promotion year
    surname: str = ""
    given: str | None = None
    honours: list[str] = field(default_factory=list)
    corps: str | None = None     # army: B.S.C. / Bo.I. / M.I. ...
    appointment: str | None = None   # civil: current substantive post
    commission_year: int | None = None   # army: first commission
    promo_day: int | None = None
    promo_month: int | None = None
    on_furlough: bool = False
    raw: str = ""
    char_offset: int = 0

    def to_json(self) -> dict:
        return self.__dict__.copy()


def _parse_civil(t: str) -> dict | None:
    furl = bool(_FURL.search(t))
    t = _FURL.sub("", t).strip(" .,")
    segs = [s.strip() for s in t.split(",")]
    if len(segs) < 2 or not segs[0] or not segs[0][0].isupper():
        return None
    surname = segs[0]
    if len(surname) > 30 or sum(c.isdigit() for c in surname):
        return None
    given = None
    i = 1
    # "Sir Henry T." / "R. C." / "A. Rivers" name field
    if segs[1] and (segs[1][0].isupper() or segs[1].startswith(("Sir", "Lord",
                                                                "Hon"))):
        if _LETTERS.match(segs[1]) or len(segs[1].split()) <= 4:
            given = segs[1]
            i = 2
    honours, rest = [], []
    for s in segs[i:]:
        if _LETTERS.match(s.replace(" ", "")) and len(s) <= 12 and rest == []:
            honours.append(s.rstrip("."))
        else:
            rest.append(s)
    appointment = ", ".join(rest).strip(" .,") or None
    return {"surname": surname, "given": given, "honours": honours,
            "appointment": appointment, "furl": furl}


def _parse_army(t: str) -> dict | None:
    m = re.match(r"^\*?\s*(1[789]\d\d)\s+(.+)$", t.strip())
    if not m:
        return None
    commission = int(m.group(1))
    rest = m.group(2).strip()
    day = month = None
    dm = _DATE_TAIL.search(rest)
    if dm:
        day, month = int(dm.group(1)), _MONTH_N.get(dm.group(2).lower())
        rest = rest[:dm.start()].strip(" .,")
    rest = re.sub(r"[†‡*]", "", rest)
    segs = [s.strip() for s in rest.split(",") if s.strip()]
    if not segs or not segs[0] or not segs[0][0].isupper():
        return None
    surname = segs[0]
    if len(surname) > 30:
        return None
    given = corps = None
    honours = []
    for s in segs[1:]:
        sn = s.replace(" ", "")
        if corps is None and _CORPS.match(sn):
            corps = s.rstrip(".")
        elif given is None and (_LETTERS.match(s) and len(s) <= 16
                                or s.startswith(("Sir", "Lord"))):
            given = s
        elif _LETTERS.match(sn) and len(sn) <= 10:
            # later letter groups: corps if none yet, else honours
            if corps is None and _CORPS.match(sn):
                corps = s.rstrip(".")
            else:
                honours.append(s.rstrip("."))
    return {"surname": surname, "given": given, "honours": honours,
            "corps": corps, "commission": commission, "day": day,
            "month": month}


def extract_gradation(ek) -> list[GradationRecord]:
    """All gradation entries for one edition (iol_reader.EditionKey)."""
    from . import iol_bios, iol_reader
    html, _ = iol_reader.load_edition(ek)
    sec = iol_bios.find_services_section(html)
    skip = sec or (len(html), len(html))

    mode: str | None = None       # civil | army
    establishment: str | None = None
    section: str | None = None
    group_year: int | None = None
    idle = 0                      # non-yielding blocks since last entry
    out: list[GradationRecord] = []

    def handle_heading(txt: str) -> bool:
        nonlocal mode, establishment, section, group_year, idle
        t = txt.strip().rstrip(".")
        if not t or len(t) > 100:
            return False
        cm = _CIVIL_HEAD.search(t)
        if cm:
            mode, establishment = "civil", (cm.group(1) or "").strip() or None
            section, group_year, idle = None, None, 0
            return True
        rm = _RANK_HEAD.match(t)
        if rm:
            mode = mode if mode == "army" else "army"
            section, group_year, idle = rm.group(1).upper(), None, 0
            return True
        clm = _CLASS.match(t)
        if clm and mode == "civil":
            section, group_year = f"{clm.group(1)} Class".title(), None
            return True
        # page running headers repeat the list title without the civil-
        # servants continuation — consume them WITHOUT killing the mode
        if mode and re.match(r"^(GRADATION LIST|ARMY LIST|RETIRED)\b", t):
            return True
        if mode and re.search(r"continued\)?$", t, re.I):
            return True
        return False

    def feed(txt: str, offset: int) -> None:
        nonlocal group_year, idle
        if not (mode and txt):
            return
        ym = _YEAR_GROUP.match(txt)
        if ym:
            group_year = int(ym.group(1))
            idle = 0
            return
        rec = _parse_army(txt) if mode == "army" else _parse_civil(txt)
        if rec is None:
            idle += 1
            return
        idle = 0
        if mode == "army":
            out.append(GradationRecord(
                ek.year, ek.tag, "army", establishment, section, group_year,
                rec["surname"], rec["given"], rec["honours"], rec["corps"],
                None, rec["commission"], rec["day"], rec["month"], False,
                txt[:200], offset))
        else:
            out.append(GradationRecord(
                ek.year, ek.tag, "civil", establishment, section, group_year,
                rec["surname"], rec["given"], rec["honours"], None,
                rec["appointment"], None, None, None, rec["furl"],
                txt[:200], offset))

    pos = 0
    for bm in _BLOCK.finditer(html):
        if skip[0] <= bm.start() < skip[1]:
            pos = bm.end()
            continue
        # labels also print as bare gap text between elements (1860s OCR)
        for gline in _TAG.sub("\n", html[pos:bm.start()]).split("\n"):
            g = _WS.sub(" ", _html.unescape(gline)).strip()
            if g:
                if not handle_heading(g) and mode:
                    feed(g, bm.start())
        pos = bm.end()
        tag, inner = bm.group(1).lower(), bm.group(2)
        if tag == "table":
            if not mode:
                continue
            for im in _INNER.finditer(inner):
                t = _text(im.group(2))
                if not handle_heading(t):
                    for piece in _BR.split(im.group(2)):
                        feed(_text(piece), bm.start())
            continue
        txt = _text(inner)
        if not txt:
            continue
        if handle_heading(txt):
            continue
        if tag in ("h1", "h2", "h3"):
            mode = None               # foreign heading ends the list
            continue
        if not mode:
            continue
        if idle > 25:
            mode = None
            continue
        # unwrap: many entries wrap across <br/> lines; a line starting
        # lowercase or with a bare abbreviation continues the previous
        pieces = _BR.split(inner) if tag == "p" else [inner]
        buf = ""
        for piece in pieces:
            t = _text(piece)
            if not t:
                continue
            if buf and (t[0].islower() or len(t) < 12
                        and not _YEAR_GROUP.match(t)
                        and not re.match(r"^\*?1[789]\d\d\s", t)):
                buf += " " + t
                continue
            if buf:
                feed(buf, bm.start())
            buf = t
        if buf:
            feed(buf, bm.start())
    return out
