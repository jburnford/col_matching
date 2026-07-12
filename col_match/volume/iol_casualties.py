"""Casualties-list extraction from the India Office List OCR: the
DEATHS / RESIGNED / RETIRED / DISMISSED change-lists of the semiannual
volumes (1861-1895) plus the year-end RETIREMENTS tables of later annuals.

This is the corpus's person-EXIT event layer — exact death, resignation
and retirement dates at six-month granularity, per establishment:

    CASUALTIES—BENGAL. CIVIL ESTABLISHMENT. DEATHS.
    Name.            Date.        Place.
    D. R. Parke      1 Oct. 64    India

Print shapes absorbed (surveyed 1865, 1875, 1892, 1930):
  * flowed text rows (1860s);
  * HTML <table> rows, name and date in separate cells, dates often piped
    "| 15 Aug. 74 |" (1870s-80s);
  * per-department <p>/<br> runs glued to the civil lists, labels as bare
    gap text — "CASUALTIES.RETIRED. <p>Rev. G. T. Carruthers, 29th Sept.
    1891</p> DIED <p>..." (1890s);
  * bordered RETIREMENTS tables with a Name./Date. thead (1920s-30s).

Death dates are the strongest over-merge killer (any event after death =
two persons fused), which roadmap Tier C1 wanted from Wikidata — for the
1861-95 cohort it is sitting in the corpus itself.
"""

from __future__ import annotations

import html as _html
import re
from dataclasses import dataclass

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_BR = re.compile(r"<br\s*/?>", re.I)
_BLOCK = re.compile(r"<(p|h1|h2|h3|table)\b[^>]*>(.*?)</\1>", re.I | re.S)
_TR = re.compile(r"<tr[^>]*>(.*?)</tr>", re.I | re.S)
_TD = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.I | re.S)

_CAS_HEAD = re.compile(r"^CASUALTIES\.?(?:[—-]\s*([A-Z][A-Z .]+?))?\.?$")
_EVENT = {
    "death": re.compile(r"^(DEATHS?|DEAD|DIED)\.?$", re.I),
    "retired": re.compile(r"^(RETIRED|RETIREMENTS?)\.?$", re.I),
    "resigned": re.compile(r"^(RESIGNED|RESIGNATIONS?)\.?$", re.I),
    "dismissed": re.compile(r"^(DISMISSED|REMOVED)\.?$", re.I),
    "invalided": re.compile(r"^(INVALIDED)\.?$", re.I),
}
_ESTAB = re.compile(
    r"^([A-Z][A-Z .&'-]{3,50}(ESTABLISHMENT|DEPARTMENT|SERVICE|CORPS"
    r"|OFFICERS))\.?$")

_DATE = re.compile(
    r"(?:(\d{1,2})(?:st|nd|rd|th)?\s+)?"
    r"(Jan|Feb|Mar|March|April|Apr|May|June|Jun|July|Jul|Aug|Sept|Sep|Oct"
    r"|Nov|Dec)\.?,?\s*(\d{2,4})")
_MONTH_N = {"jan": 1, "feb": 2, "mar": 3, "march": 3, "apr": 4, "april": 4,
            "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8,
            "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12}
_NOTE = re.compile(r"\(([^)]{2,40})\)")
_HEADER_ROW = re.compile(r"^(Name|Date|Place|Rank)[. |]*$", re.I)


def _text(fragment: str) -> str:
    return _WS.sub(" ", _html.unescape(_TAG.sub(" ", fragment))).strip()


@dataclass
class CasualtyRecord:
    edition_year: int
    edition_tag: str
    presidency: str | None       # BENGAL / MADRAS / BOMBAY / None
    establishment: str | None
    event: str                   # death / retired / resigned / ...
    name: str
    day: int | None
    month: int | None
    year: int | None
    place: str | None
    note: str | None             # parenthetical ("Retired", rank notes)
    raw: str
    char_offset: int

    def to_json(self) -> dict:
        return self.__dict__.copy()


def _year4(yy: int, edition_year: int) -> int:
    if yy >= 100:
        return yy
    cent = edition_year - edition_year % 100
    y = cent + yy
    return y - 100 if y > edition_year + 1 else y


def _parse_row(txt: str, edition_year: int) -> dict | None:
    """One casualty row -> {name, day, month, year, place, note} or None."""
    t = txt.strip(" |")
    if len(t) < 5 or _HEADER_ROW.match(t):
        return None
    dm = _DATE.search(t)
    if not dm:
        return None
    name = t[:dm.start()].strip(" ,|.\"'“”")
    # leading ditto marks inherit nothing recoverable; drop the mark
    name = re.sub(r'^["„»]\s*', "", name).strip()
    if not name or not name[0].isupper() or len(name) > 70 \
            or sum(c.isdigit() for c in name) > 2:
        return None
    note = None
    nm = _NOTE.search(name)
    if nm:
        note = nm.group(1)
        name = _NOTE.sub("", name).strip(" ,")
    tail = t[dm.end():].strip(" ,|.")
    place = tail if 0 < len(tail) <= 30 and not any(
        c.isdigit() for c in tail) else None
    return {"name": name, "note": note,
            "day": int(dm.group(1)) if dm.group(1) else None,
            "month": _MONTH_N.get(dm.group(2).lower()),
            "year": _year4(int(dm.group(3)), edition_year),
            "place": place}


def extract_casualties(ek) -> list[CasualtyRecord]:
    """All casualty rows for one edition (iol_reader.EditionKey)."""
    from . import iol_bios, iol_reader
    html, _ = iol_reader.load_edition(ek)
    # skip the Record of Services span, but keep scanning AFTER it — the
    # late annuals print their RETIREMENTS tables at the very back
    sec = iol_bios.find_services_section(html)
    skip = sec or (len(html), len(html))

    presidency: str | None = None
    establishment: str | None = None
    event: str | None = None
    active = 0            # blocks of casualty-context left before decay
    last_year: int | None = None   # ditto-year carry, ACROSS page-tables
    out: list[CasualtyRecord] = []

    def _one_label(t: str) -> bool:
        nonlocal presidency, establishment, event, active
        m = _CAS_HEAD.match(t)
        if m:
            presidency = (m.group(1) or "").strip(". ") or presidency
            establishment, event = None, None
            active = 60
            return True
        for ev, rx in _EVENT.items():
            if rx.match(t):
                if active or ev == "retired":   # RETIREMENTS tables stand alone
                    event = ev
                    active = max(active, 30)
                return True
        em = _ESTAB.match(t)
        if em and active:
            establishment = em.group(1).rstrip(". ")
            event = None
            return True
        return False

    def handle_label(txt: str) -> bool:
        t = txt.strip()
        if not t or len(t) > 70:
            return False
        # running headers: "RETIREMENTS—continued." (the <i> split can also
        # leave a bare "RETIREMENTS—" fragment) — treat as the plain label
        t = re.sub(r"[—–-]\s*(continued\.?)?$", "", t, flags=re.I).strip()
        if not t:
            return True                # pure "continued." fragment: consume
        if _one_label(t):
            return True
        # glued labels ("CIVIL ESTABLISHMENT.RESIGNED.") — handle each piece
        parts = [p.strip() for p in t.split(".") if p.strip()]
        if 1 < len(parts) <= 3:
            hit = False
            for p in parts:
                hit = _one_label(p + ".") or hit
            return hit
        return False

    pos = 0
    for bm in _BLOCK.finditer(html):
        if skip[0] <= bm.start() < skip[1]:
            pos = bm.end()
            continue
        # labels frequently print as bare gap text between elements
        for gline in _TAG.sub("\n", html[pos:bm.start()]).split("\n"):
            g = _WS.sub(" ", _html.unescape(gline)).strip()
            if g and not handle_label(g) and g.isupper() and len(g) > 4 \
                    and active:
                active = 0            # foreign caps heading ends the run
        pos = bm.end()
        tag, inner = bm.group(1).lower(), bm.group(2)

        if tag == "table":
            if not (active and event):
                continue
            for tr in _TR.finditer(inner):
                cells = [_text(c.group(1)) for c in _TD.finditer(tr.group(1))]
                cells = [c.strip(" .") for c in cells]
                row = " ".join(c for c in cells if c)
                rec = None
                if len(cells) >= 3 and cells[0] and cells[-1]:
                    # Name | Service/Appointment | Date columns; the date
                    # column dittos the year with a bare `"`
                    dm = _DATE.search(cells[-1])
                    day = month = year = None
                    if dm:
                        day = int(dm.group(1)) if dm.group(1) else None
                        month = _MONTH_N.get(dm.group(2).lower())
                        year = _year4(int(dm.group(3)), ek.year)
                        last_year = year
                    else:
                        pm = re.match(
                            r'^(\d{1,2})\s+([A-Za-z]+)\.?,?\s*["”„]?$',
                            cells[-1])
                        if pm and _MONTH_N.get(pm.group(2).lower()) \
                                and last_year:
                            day = int(pm.group(1))
                            month = _MONTH_N[pm.group(2).lower()]
                            year = last_year
                    name = cells[0].strip(' ,"')
                    if year and name and name[0].isupper() \
                            and not _HEADER_ROW.match(name) \
                            and len(name) < 70:
                        svc = cells[1].strip(' ,"') or None \
                            if len(cells) > 2 else None
                        rec = {"name": name, "note": None, "day": day,
                               "month": month, "year": year, "place": None,
                               "service": svc}
                if rec is None:
                    rec = _parse_row(row, ek.year)
                    if rec:
                        rec["service"] = None
                        if rec["year"]:
                            last_year = rec["year"]
                if rec:
                    out.append(CasualtyRecord(
                        ek.year, ek.tag, presidency,
                        rec.get("service") or establishment, event,
                        rec["name"], rec["day"], rec["month"], rec["year"],
                        rec["place"], rec["note"], row[:200], bm.start()))
                    active = max(active, 12)   # yielding rows keep the run alive
            active -= 1
            continue

        txt = _text(inner)
        if not txt:
            continue
        if handle_label(txt):
            continue
        if tag != "p":
            if txt.isupper() and active:
                active = 0            # real heading ends the run
            continue
        if not (active and event):
            continue
        for piece in _BR.split(inner):
            ptxt = _text(piece)
            if not ptxt:
                continue
            rec = _parse_row(ptxt, ek.year)
            if rec:
                out.append(CasualtyRecord(
                    ek.year, ek.tag, presidency, establishment, event,
                    rec["name"], rec["day"], rec["month"], rec["year"],
                    rec["place"], rec["note"], ptxt[:200], bm.start()))
                active = max(active, 12)       # yielding rows keep the run alive
        active -= 1
    return out
