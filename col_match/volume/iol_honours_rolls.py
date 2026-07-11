"""Honours-roll extraction from India Office List HTML: the three Indian
orders (Star of India, Indian Empire, Crown of India), grade-sectioned
membership rolls with appointment dates.

Print shape (surveyed 1875, 1901, 1935 — docs/IOL_VS_COL.md §2):

    <h1>THE MOST EXALTED ORDER OF THE STAR OF INDIA.</h1>
    <p>KNIGHTS GRAND COMMANDERS (G.C.S.I.).</p>          <- grade section
    <p>Sir John Prescott Hewett, K.B.E., C.I.E., 12 Dec., 1911.</p>
    <ol><li>4 *Sir Richard Temple, Bart., C.I.E., 1 Jan., 1878.</li>...

Era drift: 1870s grade labels are italic Title-Case with no letter code
and members mostly carry NO date; numbered <li> lists (sometimes inside
two-column <table>s) vs one-<p>-per-member; EXTRA / HONORARY / ADDITIONAL
sub-sections; royals and princely styles as very long name strings.

Value for identity QA: the roll is an EXTERNAL, per-person source of
award grade + exact appointment date — the anchor A1 (grade precedence)
and A6 (rare-honour duplicates) lack, since only 56% of bio honour
mentions are dated. Records keep name_raw untouched; the cleaned name is
best-effort (prefix/honours/date stripped), matching happens downstream.
"""

from __future__ import annotations

import html as _html
import re
from dataclasses import dataclass, field

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_BR = re.compile(r"<br\s*/?>", re.I)
_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
_BLOCK = re.compile(r"<(p|li|h2|h3)\b[^>]*>(.*?)</\1>", re.I | re.S)

ORDERS = [
    ("STAR OF INDIA", "Star of India",
     {"GC": "GCSI", "KC": "KCSI", "C": "CSI"}),
    ("INDIAN EMPIRE", "Indian Empire",
     {"GC": "GCIE", "KC": "KCIE", "C": "CIE"}),
    ("CROWN OF INDIA", "Crown of India", {"M": "CI"}),
]

# grade-section label: letters code wins; else the wording
_CODE = re.compile(r"\(\s*((?:[A-Z]\.\s*){2,5})\)")
_GRADE_WORDS = [
    (re.compile(r"KNIGHTS?\s+GRAND\s+COMMANDERS?", re.I), "GC"),
    (re.compile(r"KNIGHTS?\s+COMMANDERS?", re.I), "KC"),
    (re.compile(r"COMPANIONS?", re.I), "C"),
    (re.compile(r"MEMBERS?", re.I), "M"),
]
_SECTION_FLAGS = [
    ("honorary", re.compile(r"\bHONORARY\b", re.I)),
    ("extra", re.compile(r"\bEXTRA\b", re.I)),
    ("additional", re.compile(r"\bADDITIONAL\b", re.I)),
]

_DATE = re.compile(
    r"(\d{1,2})\s+(Jan|Feb|Mar|March|April|Apr|May|June|Jun|July|Jul|Aug"
    r"|Sept|Sep|Oct|Nov|Dec)\.?,?\s+(1[89]\d\d)")
_YEAR_ONLY = re.compile(r"\b(1[89]\d\d)\b")
_MONTH_N = {"jan": 1, "feb": 2, "mar": 3, "march": 3, "apr": 4, "april": 4,
            "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8,
            "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12}

_LETTERS_TOK = re.compile(r"^(?:[A-Z]\.\s*){1,6}[A-Z]?\.?$|^(?:Bart|Bt"
                          r"|A\.?D\.?C)\.?$")
_SEQ = re.compile(r"^\s*\*?\s*(\d{1,3})\s+")
_BOILER = re.compile(
    r"^(INSTITUTED|SOVEREIGN|GRAND MASTER|THE VICEROY|H\.?M\.? THE"
    r"|CONSISTING|REGISTRAR|SECRETARY|CHANCELLOR|KING OF ARMS"
    r"|\{|\(?\d+ (Indian|Native|European))", re.I)

_PREFIX = re.compile(
    r"^((?:Gen(?:eral)?|Lieut|Lt|Col(?:onel)?|Major|Maj|Capt(?:ain)?"
    r"|Field[- ]?Marshall?|Admiral|Air|Brig(?:adier)?|Commander|Surgn?"
    r"|The|Right|Rt|Most|Hon(?:ourable)?|His|Her|H\.?[REHM]\.?[HM]?\.?"
    r"|Sir|Dame|Dr|Rev|Excellency|Highness|Majesty|Exalted|V\.?C)\.?"
    r"[ .,-]+)+", re.I)


def _text(fragment: str) -> str:
    return _WS.sub(" ", _html.unescape(_TAG.sub(" ", fragment))).strip()


@dataclass
class RollEntry:
    edition_year: int
    edition_tag: str
    order: str
    grade: str                    # GCSI/KCSI/CSI/GCIE/KCIE/CIE/CI
    section_flags: list[str] = field(default_factory=list)
    seq: int | None = None
    name_raw: str = ""
    name: str = ""                # best-effort clean
    honours: list[str] = field(default_factory=list)
    appt_day: int | None = None
    appt_month: int | None = None
    appt_year: int | None = None
    char_offset: int = 0

    def to_json(self) -> dict:
        return self.__dict__.copy()


def _grade_label(txt: str, letters: dict[str, str]) -> str | None:
    """Grade token if `txt` is a grade-section label for this order."""
    t = txt.strip()
    if len(t) > 120:
        return None
    m = _CODE.search(t)
    if m:
        code = re.sub(r"[^A-Z]", "", m.group(1))
        for tok in letters.values():
            if code == tok:
                return tok
    # wording form — only when label-shaped (caps or italic-short, ends '.')
    if not (t.isupper() or (len(t) < 60 and t.rstrip(". )0123456789(").
                            replace(",", "").istitle())):
        return None
    if _DATE.search(t):
        return None
    for rx, key in _GRADE_WORDS:
        if rx.search(t):
            return letters.get(key)
    return None


def _parse_member(txt: str) -> dict | None:
    """One roll line -> {seq, name_raw, name, honours, date parts} or None."""
    t = txt.strip()
    if len(t) < 8 or _BOILER.match(t):
        return None
    seq = None
    m = _SEQ.match(t)
    if m:
        seq = int(m.group(1))
        t = t[m.end():]
    t = t.lstrip("*†‡ ").rstrip()
    if not t or not t[0].isupper():
        return None
    day = month = year = None
    dm = None
    for dm in _DATE.finditer(t):
        pass                       # last date on the line = appointment date
    if dm:
        day = int(dm.group(1))
        month = _MONTH_N.get(dm.group(2).lower())
        year = int(dm.group(3))
        t_body = (t[:dm.start()] + t[dm.end():]).strip(" .,")
    else:
        t_body = t.strip(" .,")
        ym = None
        for ym in _YEAR_ONLY.finditer(t_body):
            pass
        if ym and len(t_body) - ym.end() < 15:
            year = int(ym.group(1))
            t_body = t_body[:ym.start()].strip(" .,")
    t_body = re.sub(r"\(\s*(Additional|Hon\.?(orary)?|Extra)\.?\s*\)", "",
                    t_body, flags=re.I).strip(" .,")
    # split trailing honour letter-groups off the name
    segs = [s.strip() for s in t_body.split(",")]
    name_end = len(segs)
    honours = []
    for i in range(len(segs) - 1, 0, -1):
        s = re.sub(r"\s*\(Hon\.?\)\s*", "", segs[i]).strip(" .")
        if s and _LETTERS_TOK.match(s + "."):
            honours.insert(0, s)
            name_end = i
        elif s and _LETTERS_TOK.match(s):
            honours.insert(0, s)
            name_end = i
        else:
            break
    name = ", ".join(segs[:name_end]).strip(" .,")
    clean = _PREFIX.sub("", name).strip(" .,")
    if not clean or not re.search(r"[A-Za-z]{3}", clean):
        return None
    return {"seq": seq, "name_raw": txt.strip()[:300], "name": clean[:160],
            "honours": honours, "day": day, "month": month, "year": year}


_ORDER_HEAD = re.compile(
    r"ORDER OF THE (STAR OF INDIA|INDIAN EMPIRE|CROWN OF INDIA)", re.I)

# other decorations / lists that follow the three orders WITHOUT an h-tag
# heading — they end the current roll (parse them as their own layer later:
# Kaisar-i-Hind carries many women recipients, OBI/IOM the Indian ranks)
_RESET_HEAD = re.compile(
    r"\b(KAISAR-I-HIND|ORDER OF BRITISH INDIA|INDIAN ORDER OF MERIT"
    r"|DISTINGUISHED SERVICE|ROYAL VICTORIAN ORDER|ST\.?\s?MICHAEL"
    r"|ORDER OF THE BATH|IMPERIAL SERVICE ORDER|VICTORIA CROSS"
    r"|ROYAL RED CROSS|ALBERT MEDAL|EDWARD MEDAL|ORDER OF ST\.? JOHN"
    r"|WHO ARE MEMBERS OF THE ORDER|ADDENDUM|ALPHABETICAL LIST"
    r"|WAR SERVICES|WARRANT OF PRECEDENCE|TABLE OF PRECEDENCE)\b")
_ALL_TOKENS = {tok: (nm, letters) for _, nm, letters in ORDERS
               for tok in letters.values()}
_PROSE_WORDS = re.compile(
    r"\b(table|pay|salary|salaries|allowance|includes?|printed|spoken"
    r"|domicile|performing|special|following|regulations?|provided"
    r"|whereof|shall|which|are|is|was|were)\b", re.I)


def _name_shaped(txt: str) -> bool:
    """Undated <p> member gate: short, capitalized-dominant, no digits."""
    toks = txt.replace(",", " ").split()
    if not 2 <= len(toks) <= 14 or any(ch.isdigit() for ch in txt):
        return False
    if _PROSE_WORDS.search(txt):
        return False
    caps = sum(1 for w in toks if w[0].isupper() or w[0] in "({")
    return caps / len(toks) >= 0.65


def extract_rolls(ek) -> list[RollEntry]:
    """All Indian-order roll entries for one edition. Linear state machine:
    order context switches at order headings (h-tag OR bare gap text — the
    1935 OCR leaves the Indian Empire / Crown headings outside any tag),
    grade at section labels, and any other h-tag heading ends the roll."""
    from . import iol_reader
    html, _ = iol_reader.load_edition(ek)

    order_name: str | None = None
    letters: dict[str, str] = {}
    grade: str | None = None
    flags: list[str] = []
    out: list[RollEntry] = []

    def handle_label(txt: str) -> bool:
        """Order/grade/reset headings — printed as h-tags, <p> labels OR
        bare gap text (the 1935 OCR leaves both the order headings and the
        HONORARY/EXTRA grade labels outside any element). True = consumed."""
        nonlocal order_name, letters, grade, flags
        if len(txt) > 120:
            return False
        m = _ORDER_HEAD.search(txt)
        if m and len(txt) < 90:
            key = m.group(1).upper()
            for k, nm, lt in ORDERS:
                if k == key:
                    order_name, letters, flags = nm, lt, []
                    # single-grade order prints no grade label at all
                    grade = "CI" if nm == "Crown of India" else None
                    return True
        if _RESET_HEAD.search(txt) and sum(
                1 for c in txt if c.islower()) < len(txt) * 0.3:
            order_name, grade = None, None
            return True
        if order_name:
            g = _grade_label(txt, letters)
            if g:
                grade = g
                flags = [f for f, rx in _SECTION_FLAGS if rx.search(txt)]
                return True
            cm = _CODE.search(txt)
            if cm:
                tok = re.sub(r"[^A-Z]", "", cm.group(1))
                if tok in _ALL_TOKENS and tok not in letters.values():
                    # grade code of another Indian order = missed switch
                    order_name, letters = _ALL_TOKENS[tok]
                    grade = tok
                    flags = [f for f, rx in _SECTION_FLAGS if rx.search(txt)]
                    return True
                if tok not in _ALL_TOKENS and len(tok) >= 2 \
                        and any(rx.search(txt) for rx, _ in _GRADE_WORDS):
                    # section of a NON-Indian order (C.M.G., G.C.V.O., ...)
                    grade = None
                    return True
        return False

    pos = 0
    for bm in _BLOCK.finditer(html):
        for gline in _TAG.sub("\n", html[pos:bm.start()]).split("\n"):
            g = _WS.sub(" ", _html.unescape(gline)).strip()
            if g:
                handle_label(g)
        pos = bm.end()
        tag, inner = bm.group(1).lower(), bm.group(2)
        block_txt = _text(inner)
        if not block_txt:
            continue
        if handle_label(block_txt):
            continue
        if tag != "p" and tag != "li":
            if order_name:            # foreign heading ends the roll
                order_name, grade = None, None
            continue
        if not (order_name and grade):
            continue
        is_li = tag == "li"
        pieces = [inner] if is_li else _BR.split(inner)
        for piece in pieces:
            txt = _text(piece)
            if not txt:
                continue
            # wrapped continuation of the previous entry
            if out and out[-1].order == order_name and (
                    txt[0].islower() or _DATE.match(txt)
                    or _LETTERS_TOK.match(txt.split(",")[0].strip())):
                prev = out[-1]
                merged = _parse_member(prev.name_raw + " " + txt)
                if merged:
                    prev.name_raw = merged["name_raw"]
                    prev.name = merged["name"]
                    prev.honours = merged["honours"]
                    prev.appt_day = merged["day"]
                    prev.appt_month = merged["month"]
                    prev.appt_year = merged["year"]
                continue
            mrec = _parse_member(txt)
            if not mrec:
                continue
            # <p> members without a date or honours must be name-shaped
            # (prose paragraphs otherwise leak in after a roll ends)
            if not is_li and not mrec["year"] and not mrec["honours"] \
                    and not _name_shaped(txt):
                continue
            out.append(RollEntry(
                edition_year=ek.year, edition_tag=ek.tag,
                order=order_name, grade=grade,
                section_flags=list(flags), seq=mrec["seq"],
                name_raw=mrec["name_raw"], name=mrec["name"],
                honours=mrec["honours"], appt_day=mrec["day"],
                appt_month=mrec["month"], appt_year=mrec["year"],
                char_offset=bm.start()))

    # rolls print appointment dates universally from ~1890; a group that is
    # mostly undated in the dated era is a false region (a glossary or TOC
    # line mentioning the order) — drop it wholesale
    if ek.year >= 1890:
        from collections import Counter as _C
        dated = _C()
        total = _C()
        for r in out:
            total[(r.order, r.grade)] += 1
            if r.appt_year:
                dated[(r.order, r.grade)] += 1
        out = [r for r in out
               if dated[(r.order, r.grade)] / total[(r.order, r.grade)] >= 0.5]
    return out
