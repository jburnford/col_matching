"""Civil-list (establishment roster) extraction from India Office List HTML.

The per-government civil lists — the IOL analogue of the Colonial Office
List staff rosters — print one office per line inside ``<br/>``-separated
``<p>`` blocks, the office usually in a leading ``<i>`` span::

    <p><i>Secretary</i>—P. C. Tallents, C.S.I., C.I.E., I.C.S. (offg.).<br/>
    <i>Deputy Secretary</i>—W. Christie, M.C., I.C.S.</p>

Era drift this module absorbs (surveyed 1896-1947, docs/IOL_VS_COL.md §2):
  * separator: comma (1896-1920s) vs em-dash (1930s+);
  * the ``<i>`` markup vanishes in some OCR runs (1896, 1925) — offices are
    then recognised by an office-vocabulary gate on the pre-separator text;
  * plural offices carry several holders ("Deputy Secretaries, A, B, and C");
  * holders wear rank prefixes (Lieut.-Col.), Indian honorifics
    (Khan Bahadur, Rai Sahib), honour clusters (C.S.I., O.B.E.) and service
    tags (I.C.S., I.M.S., S.C.), with acting/officiating flags
    ((offg.) (actg.) (sub. pro. temp.) (provl.) (tempy.));
  * context: government from section headings (GOVERNMENT OF BENGAL /
    "BENGAL."), department from ALL-CAPS paragraphs and <h2>/<h3>, branch
    from Title-Case "... Branch." lines.

Scope: the office—holder grammar ONLY. Gradation lists, commission name
lists, honours rolls and the Record of Services are separate layers. The
scan is bounded to before the Record of Services (via iol_bios).

Records are cheap to audit: every one carries the raw line + char offset.
"""

from __future__ import annotations

import html as _html
import re
from dataclasses import dataclass, field

from . import iol_bios

_PARA = re.compile(r"<(p|h1|h2|h3)\b[^>]*>(.*?)</\1>", re.I | re.S)
_LEAD_I = re.compile(r"^\s*<i\b[^>]*>(.*?)</i>", re.I | re.S)
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_BR = re.compile(r"<br\s*/?>", re.I)

# ------------------------------------------------------------------ vocab --

# a line's office segment must contain one of these to parse (gate against
# bios, precedence warrants, prose). Lower-cased match on the office text.
_OFFICE_WORDS = (
    "secretary", "secretaries", "adviser", "advisers", "registrar",
    "superintendent", "commissioner", "commissioners", "member", "members",
    "director", "officer", "officers", "attach", "governor", "president",
    "chairman", "collector", "magistrate", "judge", "judges", "chaplain",
    "surgeon", "physician", "engineer", "inspector", "accountant",
    "controller", "comptroller", "auditor", "treasurer", "librarian",
    "curator", "principal", "professor", "agent", "consul", "resident",
    "minister", "examiner", "solicitor", "translator", "interpreter",
    "clerk", "assistant", "deputy", "aide", "aides", "private sec",
    "commandant", "conservator", "warden", "master", "manager",
    "postmaster", "chemist", "geologist", "botanist", "archaeolog",
    "epigraphist", "statistician", "actuary", "analyst", "bacteriolog",
    "entomolog", "meteorolog", "electrician", "architect", "receiver",
    "remembrancer", "sheriff", "coroner", "administrator",
)

_FLAG = re.compile(
    r"\(\s*(offg|actg|acting|officiating|provl|tempy|temp|sub\.? pro\.? tem"
    r"p?|on deputation|on leave|addl|additional|vacant)\.?\s*\)", re.I)

# honour / qualification / service letter-groups: dotted caps like C.S.I.,
# K.C.I.E., O.B.E., I.C.S., plus a few undotted or mixed forms.
_LETTERS = re.compile(
    r"^(?:[A-Z][a-z]?\.\s*){1,6}[A-Z]?\.?$|^(?:CIE|CSI|KCSI|KCIE|OBE|CBE|MBE"
    r"|KBE|GBE|CMG|KCMG|GCMG|CB|KCB|GCB|CVO|KCVO|MVO|GCVO|DSO|MC|VC|ISO|VD"
    r"|ICS|IMS|IA|ISC|IPS|IFS|ISE|IES|RE|RA|RN|SC|LL\.?D|D\.?Litt|D\.?Sc"
    r"|M\.?P|K\.?C|Q\.?C|F\.?R\.?S)\.?$")

# post-name suffixes that are NOT holders (baronetcy, parliament, silk, bar)
_SUFFIX = re.compile(
    r"^(Bart|Bt|Esq|Jun|Sen|M\.?P|K\.?C|Q\.?C|Barr|Bar-at-law"
    r"|Barrister(-at-law)?)\.?$", re.I)

# prose leaking through the office/holder grammar
_PROSE_OFFICE = re.compile(
    r"\b(is|was|are|were|be|been|upon|which|whom|whose|has|have|had|shall"
    r"|will|may|conferred|vested|described)\b", re.I)
_BAD_NAME = re.compile(
    r"\d|\b(Notification|No|Dept|Act|Regulation|Rules?|Chapter|Section"
    r"|page|vide|ibid|ditto|vacant)\b", re.I)

# tenure-date sentences that trail governor/council entries — attach to the
# current holder, never open a new one. May arrive glued to a final honour
# ("G.C.I.E. Assumed charge of office").
_TENURE = re.compile(
    r"\b(Appointed|Reappointed|Assumed charge|Took (his|her) seat|Retired"
    r"|Resigned|Created|Succeeded|Entered upon)\b")

_RANKS = (
    "sir", "dr", "mr", "mrs", "miss", "rev", "revd", "hon", "the hon",
    "the right hon", "right hon", "the rt. hon", "rt. hon", "his highness",
    "his excellency", "h.e", "col", "colonel", "lieut", "lt", "lieutenant",
    "major", "maj", "capt", "captain", "general", "gen", "brig", "brigadier",
    "admiral", "commander", "cdr", "wing commander", "air commodore",
    "sqn", "squadron leader", "surgn", "surgeon", "asst",
)
_INDIAN_HONORIFICS = (
    "khan bahadur", "khan sahib", "rai bahadur", "rai sahib", "rao bahadur",
    "rao sahib", "raja", "rana", "nawab", "nawabzada", "sardar", "pandit",
    "maulvi", "maulana", "munshi", "mirza", "sheikh", "shaikh", "syed",
    "sayyid", "diwan bahadur", "dewan bahadur", "babu", "lala", "seth",
    "thakur", "chaudhuri", "kunwar", "sardar bahadur",
)

_SERVICE_TAGS = {"ICS", "IMS", "IA", "ISC", "IPS", "IFS", "ISE", "IES",
                 "SC", "RE", "RA", "RN"}


def _text(fragment: str) -> str:
    return _WS.sub(" ", _html.unescape(_TAG.sub(" ", fragment))).strip()


def _lk(s: str) -> str:
    """letters-only key for a dotted group: 'C.S.I.' -> 'CSI'."""
    return re.sub(r"[^A-Z]", "", s.upper())


def _is_letters(tok: str) -> bool:
    return bool(_LETTERS.match(tok.strip()))


def _office_shaped(s: str) -> bool:
    low = s.lower()
    return any(w in low for w in _OFFICE_WORDS) and len(s) < 120


@dataclass
class CivilRecord:
    edition_year: int
    edition_tag: str
    government: str | None
    department: str | None
    branch: str | None
    office: str
    name: str
    honours: list[str] = field(default_factory=list)
    service: str | None = None
    prefix: str | None = None          # rank / honorific prefix as printed
    acting: bool = False
    flags: list[str] = field(default_factory=list)
    raw_line: str = ""
    char_offset: int = 0
    page_est: int | None = None

    def to_json(self) -> dict:
        return self.__dict__.copy()


# --------------------------------------------------------------- headings --

_GOVT = re.compile(
    r"^(GOVERNMENT OF .{3,40}|OFFICE OF THE SECRETARY OF STATE.*|OFFICE OF"
    r" THE HIGH COMMISSIONER.*|(THE )?INDIA OFFICE|(THE )?BURMA OFFICE"
    r"|(THE SETTLEMENT OF |ADMINISTRATION OF )ADEN( SETTLEMENT)?"
    r"|(THE )?INDIAN STATES( AND AGENCIES)?"
    r"|(THE )?SECRETARY OF STATE FOR INDIA( IN COUNCIL)?[ ,.]*.{0,25}"
    r"|THE INDIA (OFFICE )?LIST( AND OFFICE LIST)?)\.?$")

# sections whose office-shaped lines are NOT establishment rosters —
# chronological head-of-administration lists, honours rolls, precedence
# tables, gradation/army seniority lists, annuitant/retired/casualty lists.
# They RESET the government context (suppress records) rather than stop the
# scan: in pre-1896 volumes several of these are FRONT matter and the civil
# lists resume after them.
_SUPPRESS = re.compile(
    r"^(CHRONOLOGICAL LISTS?\b.*|THE MOST EXALTED ORDER\b.*|THE MOST EMINENT"
    r" ORDER\b.*|ORDER OF THE INDIAN EMPIRE.*|IMPERIAL ORDER OF THE CROWN.*"
    r"|ORDER OF THE STAR OF INDIA.*|ORDER OF THE BATH.*"
    r"|WARRANT OF PRECEDENCE.*|TABLE OF PRECEDENCE.*"
    r"|GRADATION LISTS?\b.*|ARMY LIST.*|STAFF CORPS.*|.*ANNUITANTS.*"
    r"|RETIRED (LIST|OFFICERS).*|OFFICERS RETIRED.*|CASUALTIES.*"
    r"|INVALID AND REDUCED PENSIONERS.*|.*PENSION (LIST|FUND).*)\.?$")

# bare-caps province headings (1896-1920s layout). Keep tight: known units.
_PROVINCES = (
    "BENGAL", "MADRAS", "BOMBAY", "PUNJAB", "BURMA", "ASSAM", "SIND",
    "UNITED PROVINCES", "UNITED PROVINCES OF AGRA AND OUDH",
    "NORTH-WESTERN PROVINCES AND OUDH", "N.W. PROVINCES AND OUDH",
    "CENTRAL PROVINCES", "CENTRAL PROVINCES AND BERAR", "BIHAR AND ORISSA",
    "BIHAR", "ORISSA", "NORTH-WEST FRONTIER PROVINCE", "BALUCHISTAN",
    "DELHI", "AJMER-MERWARA", "COORG", "ANDAMANS AND NICOBARS",
    "GOVERNMENT OF INDIA", "EASTERN BENGAL AND ASSAM",
)
_PROV_KEY = {re.sub(r"[^A-Z]", "", p): p for p in _PROVINCES}

_DEPT = re.compile(r"^[A-Z][A-Z .,&()'’-]{3,80}$")
_BRANCH = re.compile(r"^[A-Z][A-Za-z .,&()'-]{2,60}(Branch|Board of Revenue)\.?$")


def _classify_heading(txt: str, level: str) -> tuple[str, str] | None:
    """(kind, value) where kind in government|department|branch, or None.

    ``level``: "h1"/"h2"/"h3" for real headings, "gap" for a bare-text
    heading the OCR left outside any element (the 1935 GOVERNMENT OF INDIA
    prints that way), "p" for a paragraph.

    Bare province names ("COORG.") also occur in plain paragraphs (indexes,
    precedence lists) and as sub-locations at <h3> (the Mint's BOMBAY /
    CALCUTTA), so they set the GOVERNMENT only from a top-level heading
    (h1/h2/gap); at h3 they demote to department context. "GOVERNMENT OF X"
    is unambiguous anywhere."""
    t = txt.rstrip(". ").strip()
    if not t or len(t) > 90:
        return None
    if _GOVT.match(t):
        v = t
        # all forms of the London office head normalize to one label
        if re.match(r"^(THE )?INDIA OFFICE$|^OFFICE OF THE SECRETARY OF STATE"
                    r"|^(THE )?SECRETARY OF STATE FOR INDIA"
                    r"|^THE INDIA (OFFICE )?LIST", v):
            v = "INDIA OFFICE (LONDON)"
        elif re.search(r"\bADEN\b", v):
            v = "ADEN"
        elif "INDIAN STATES" in v:
            v = "INDIAN STATES"
        return ("government", v)
    if re.sub(r"[^A-Z]", "", t) in _PROV_KEY:
        prov = _PROV_KEY[re.sub(r"[^A-Z]", "", t)]
        if level in ("h1", "h2", "gap"):
            # caller confirms with a head-of-government lookahead: bare
            # province names also head sub-groupings in all-India lists
            return ("province", prov)
        if level == "h3":
            return ("department", prov)
        return None
    if level == "gap":
        return None                    # gaps only yield govt-level headings
    if _BRANCH.match(t):
        return ("branch", t)
    if _DEPT.match(t) and not any(ch.islower() for ch in t):
        return ("department", t)
    return None


# ------------------------------------------------------------ line parsing --

def _split_office(line_html: str) -> tuple[str, str] | None:
    """(office, rest) from one civil-list line, or None if not office-shaped.

    Prefer the leading <i> span; fall back to the pre-separator text when the
    OCR dropped the italics. Separator: em-dash, else the first comma."""
    m = _LEAD_I.match(line_html)
    if m:
        office = _text(m.group(1)).strip(" ,—-:;")
        rest = _text(line_html[m.end():]).lstrip(" ,—–:;-")
        if office and _office_shaped(office) and rest \
                and not _PROSE_OFFICE.search(office):
            return office, rest
        return None
    txt = _text(line_html)
    for sep in ("—", "–"):
        if sep in txt:
            office, rest = txt.split(sep, 1)
            if _office_shaped(office.strip()) and rest.strip() \
                    and len(office.strip()) < 90 \
                    and not _PROSE_OFFICE.search(office):
                return office.strip(" ,"), rest.strip(" ,")
            return None
    if "," in txt:
        office, rest = txt.split(",", 1)
        if _office_shaped(office.strip()) and rest.strip() \
                and len(office.strip()) < 70 \
                and not _PROSE_OFFICE.search(office):
            return office.strip(), rest.strip()
    return None


def _startswith_any(low: str, words: tuple[str, ...]) -> str | None:
    for w in sorted(words, key=len, reverse=True):
        if low.startswith(w + " ") or low.startswith(w + ".") or low == w:
            return w
    return None


def _split_holders(rest: str) -> list[dict]:
    """Split the post-office text into holder dicts.

    Walk comma/semicolon segments: letters-groups (honours/services) attach
    to the current holder; a name-shaped segment opens a new one. 'and X'
    splits. Trailing parenthetical flags attach to the current holder."""
    holders: list[dict] = []
    cur: dict | None = None

    def close():
        nonlocal cur
        if cur and cur["name"]:
            holders.append(cur)
        cur = None

    segs: list[str] = []
    for chunk in re.split(r";", rest):
        segs.extend(s.strip() for s in chunk.split(",") if s.strip())
        segs.append(";")            # holder boundary marker
    if segs and segs[-1] == ";":
        segs.pop()

    for seg in segs:
        if seg == ";":
            close()
            continue
        flags = [f.lower().rstrip(".") for f in _FLAG.findall(seg)]
        seg_clean = _FLAG.sub("", seg).strip(" .")
        if not seg_clean:
            if cur is not None and flags:
                cur["flags"].extend(flags)
            continue
        # explicit 'and X' -> new holder
        if re.match(r"^and\s+", seg_clean, re.I):
            close()
            seg_clean = re.sub(r"^and\s+", "", seg_clean, flags=re.I)
        tm = _TENURE.search(seg_clean)
        if tm:
            # honours glued in front of the tenure phrase still belong to
            # the holder; the phrase itself becomes a tenure flag
            head = seg_clean[:tm.start()].strip(" .,")
            if cur is not None:
                if head and _is_letters(head):
                    cur["honours"].append(head.rstrip("."))
                cur["flags"].append(
                    "tenure:" + seg_clean[tm.start():].strip()[:60])
                cur["flags"].extend(flags)
            continue
        if re.match(r"^\d", seg_clean) or seg_clean.split()[0].lower() in (
                "vice", "vise"):
            # date fragments ("7th April"), year tails, "vice X retired"
            if cur is not None and flags:
                cur["flags"].extend(flags)
            continue
        if _is_letters(seg_clean) or _SUFFIX.match(seg_clean):
            if cur is not None:
                key = _lk(seg_clean)
                if _SUFFIX.match(seg_clean):
                    cur["flags"].append("suffix:" + key.lower())
                elif key in _SERVICE_TAGS and not cur["service"]:
                    cur["service"] = key
                else:
                    cur["honours"].append(seg_clean.rstrip("."))
                cur["flags"].extend(flags)
            continue
        # name-shaped segment -> new holder (prefix peeled)
        if _BAD_NAME.search(seg_clean) or len(seg_clean.split()) > 6:
            if cur is not None and flags:
                cur["flags"].extend(flags)
            continue
        low = seg_clean.lower()
        prefix_parts = []
        while True:
            w = _startswith_any(low, _INDIAN_HONORIFICS) \
                or _startswith_any(low, _RANKS)
            if not w:
                break
            prefix_parts.append(seg_clean[:len(w)])
            seg_clean = seg_clean[len(w):].lstrip(" .-")
            low = seg_clean.lower()
        if not seg_clean or not seg_clean[0].isupper():
            # a prefix with no name (or prose residue) — attach as flagish
            if cur is not None and flags:
                cur["flags"].extend(flags)
            continue
        # "E. J. Turner and A. R. B. Vaux" — two holders in one segment
        parts = re.split(r"\s+and\s+", seg_clean)
        if len(parts) > 1 and all(p and p[0].isupper() and " " in p
                                  for p in parts):
            for p in parts:
                close()
                cur = {"name": p.strip(), "honours": [], "service": None,
                       "prefix": " ".join(prefix_parts) or None,
                       "flags": list(flags)}
                prefix_parts = []
            continue
        close()
        cur = {"name": seg_clean, "honours": [], "service": None,
               "prefix": " ".join(prefix_parts) or None, "flags": flags}
    close()
    return holders


# ----------------------------------------------------------------- driver --

def _unwrap_lines(inner: str) -> list[str]:
    """<br/>-split a paragraph and rejoin wrapped continuations (a line that
    doesn't open a new office belongs to the previous line)."""
    parts = [p for p in _BR.split(inner) if _text(p)]
    out: list[str] = []
    for p in parts:
        if out and not _LEAD_I.match(p):
            head = _text(p)
            # continuation: starts lowercase, or is letters-groups, or the
            # previous line ended mid-name (comma/'and'/open paren)
            prev = _text(out[-1])
            if (head and (head[0].islower() or _is_letters(head.split(",")[0].strip())
                          or prev.endswith((",", "and", "(", "-")))):
                out[-1] = out[-1] + " " + p
                continue
        out.append(p)
    return out


def extract_civil(ek) -> list[CivilRecord]:
    """All civil-list records for one edition (an iol_reader.EditionKey)."""
    from . import iol_reader
    html, page_tokens = iol_reader.load_edition(ek)

    # bound: stop before the Record of Services
    sec = iol_bios.find_services_section(html)
    limit = sec[0] if sec else len(html)

    # page estimation (mirrors iol_bios: cumulative token mass ~ char mass)
    cum, total = [], sum(page_tokens) or 1
    run = 0
    for t in page_tokens:
        run += t
        cum.append(run / total)

    def page_of(off: int) -> int | None:
        if not page_tokens:
            return None
        frac = off / max(len(html), 1)
        import bisect
        return bisect.bisect_left(cum, frac) + 1

    _HOG = re.compile(   # head-of-government marker opening a real section
        r"(Chief Commissioner|Lieutenant[- ]Governor|Lieut\.?-Governor"
        r"|Governor|Agent to the Governor-General|Resident\b)", re.I)

    # everything before the first government heading is the London office
    government, department, branch = "INDIA OFFICE (LONDON)", None, None
    started = False        # no records until a real government heading
    records: list[CivilRecord] = []
    pos = 0
    for m in _PARA.finditer(html):
        if m.start() >= limit:
            break

        def _apply(kind_val, lookahead_at: int) -> bool:
            """Update context from one classified heading; True = stop."""
            nonlocal government, department, branch, started
            kind, val = kind_val
            if kind == "province":
                # real province section iff a head-of-government follows
                window = html[lookahead_at:lookahead_at + 2500]
                kind = "government" if _HOG.search(_text(window)) \
                    else "department"
            if kind == "government":
                government, department, branch = val, None, None
                started = True
            elif kind == "department":
                department, branch = val, None
            else:
                branch = val
            return False

        # bare-text headings in the gap between elements (some OCR runs
        # leave section heads outside any tag, e.g. 1935 GOVERNMENT OF INDIA)
        for gline in _TAG.sub("\n", html[pos:m.start()]).split("\n"):
            g = _WS.sub(" ", _html.unescape(gline)).strip()
            if g and len(g) < 90:
                if _SUPPRESS.match(g.rstrip(". ")):
                    government, department, branch = None, None, None
                    continue
                gh = _classify_heading(g, "gap")
                if gh:
                    _apply(gh, m.start())
        pos = m.end()
        tag, inner = m.group(1).lower(), m.group(2)
        txt = _text(inner)
        if not txt:
            continue
        if tag != "p" and _SUPPRESS.match(txt.rstrip(". ")):
            government, department, branch = None, None, None
            continue
        head = _classify_heading(txt, tag) \
            if (tag != "p" or len(txt) < 90) else None
        if head:
            kind, val = head
            if kind in ("government", "province"):
                _apply((kind, val), m.end())
            elif kind == "department":
                # ignore all-caps lines that are actually running headers of
                # non-roster sections; cheap gate: must end DEPARTMENT/OFFICE/
                # COUNCIL/STAFF/SECRETARIAT/BOARD/BRANCH/ESTABLISHMENT or be short
                if re.search(r"(DEPARTMENT|OFFICE|COUNCIL|STAFF|SECRETARIAT|"
                             r"BOARD|BRANCH|ESTABLISHMENT|COMMISSION|SURVEY|"
                             r"COLLEGE|COURT|MINT|POLICE|JAIL|CUSTOMS|MARINE)"
                             r"S?\.?$", txt.rstrip(". ")):
                    department, branch = txt.rstrip(". "), None
            else:
                branch = val
            continue
        if tag != "p" or not started or government is None:
            continue
        for line in _unwrap_lines(inner):
            so = _split_office(line)
            if not so:
                continue
            office, rest = so
            base_words = office.split("(")[0].strip().lower().split()
            plural = bool(base_words and re.search(
                r"(ies|ers|ors|ants|als|ents|ates|hes|members|aides)$",
                base_words[-1]))
            for h in _split_holders(rest):
                records.append(CivilRecord(
                    edition_year=ek.year, edition_tag=ek.tag,
                    government=government, department=department,
                    branch=branch, office=office,
                    name=h["name"], honours=h["honours"],
                    service=h["service"], prefix=h["prefix"],
                    acting=any(f.startswith(("offg", "actg", "acting",
                                             "officiating"))
                               for f in h["flags"]),
                    flags=sorted(set(h["flags"])),
                    raw_line=_text(line)[:300],
                    char_offset=m.start(), page_est=page_of(m.start())))
                if not plural and len(records) >= 2 \
                        and records[-2].raw_line == records[-1].raw_line:
                    # singular office with >1 holder: co-holder or actg pair —
                    # legitimate (successor listed); keep both, flag
                    records[-1].flags = sorted(set(records[-1].flags
                                                   + ["coholder"]))
    return records
