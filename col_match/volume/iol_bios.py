"""Biography segmentation from India Office List HTML editions.

The IOL "Record of Services" section renders as one ``<p>`` per biography, the
headword in a leading ``<b>`` span::

    <h2>RECORD OF SERVICES.</h2>
    <p><b>ABBOTT, JOHN, B.A. (Oxon), late Indian C.S. (b. 28th Sept., 1884).</b>—Educ. at …</p>
    <p><b>ABBAS, ASGHAR (see Asghar Abbas).</b></p>

This is cleaner than the markdown twin (which splits long headwords across
lines), so segmentation is paragraph-native: the bio section is bounded by the
``RECORD OF SERVICES`` heading and the next heading; each ``<p>`` with a bold
headword and a career em-dash is one biography; bold ``(see X)`` paragraphs with
no body are cross-reference aliases.

Mirrors ``volume/bios.py`` and emits the same ``VolumeBio`` so everything
downstream (clustering, structuring) is unchanged. Provenance is page-level
(estimated from per-page token mass) since the HTML carries no coordinates.
"""

from __future__ import annotations

import bisect
import html as _html
import json
import re
from pathlib import Path

from ..services import rules_parse
from ..services.corpus import era_for_year
from ..services.schema import EntryVersion
from . import iol_reader
from .bios import VolumeBio, _is_headword, _surname_key, _DASH

_HEAD = re.compile(r"<h[12][^>]*>(.*?)</h[12]>", re.I | re.S)
_PARA = re.compile(r"<p\b[^>]*>(.*?)</p>", re.I | re.S)
_BOLD = re.compile(r"<b\b[^>]*>(.*?)</b>", re.I | re.S)
_LEAD_BOLD = re.compile(r"\s*<b\b[^>]*>(.*?)</b>", re.I | re.S)  # bold at paragraph start
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_SERVICES = re.compile(r"record\s+of\s+(?:the\s+)?(?:public\s+)?services?", re.I)
_SEE = re.compile(r"\(\s*see\b[^)]*\)", re.I)
_BIRTH = re.compile(r"\(\s*b\.\s*[^)]{0,40}?(1[0-9]{3})")

_DENSITY_WIN = 120_000   # chars to look ahead when scoring a section heading
_DENSITY_MIN = 40        # min bio-shaped paragraphs to accept a heading


def _text(fragment: str) -> str:
    """HTML fragment -> plain text (tags dropped, entities decoded, ws collapsed)."""
    return _WS.sub(" ", _html.unescape(_TAG.sub(" ", fragment))).strip()


def _caps_first(s: str) -> bool:
    """First alpha token is uppercase-dominant (a headword/name start)."""
    m = re.match(r"[^A-Za-z]*([A-Za-z][A-Za-z'’.\-]*)", s)
    if not m:
        return False
    w = [c for c in m.group(1) if c.isalpha()]
    return len(w) >= 2 and sum(c.isupper() for c in w) / len(w) >= 0.6


def _lead_bold(para_inner: str) -> str | None:
    """The bold headword if the paragraph starts with a name-shaped bold span.
    Bolding is inconsistent (dropped entirely deeper in the OCR), so this is a
    parsing bonus, not the segmentation trigger."""
    m = _LEAD_BOLD.match(para_inner)
    if not m:
        return None
    head = _text(m.group(1))
    return head if _caps_first(head) else None


def _bio_shaped(para_inner: str) -> bool:
    """A paragraph opens a biography if its text starts with a headword surname.
    (``<b>`` is unreliable — present early, gone later — so segment on the
    headword shape of the paragraph text, like the markdown path.)"""
    return _is_headword(_text(para_inner))


def find_services_section(html: str) -> tuple[int, int] | None:
    """Return (start, end) char offsets bounding the Record-of-Services run.

    The heading recurs (a table-of-contents copy and the real section), so pick
    the ``RECORD OF SERVICES`` heading followed by the densest run of bio-shaped
    paragraphs; end at the next heading."""
    heads = [(m.start(), m.end(), _text(m.group(1))) for m in _HEAD.finditer(html)]
    svc = [_SERVICES.search(h[2]) is not None for h in heads]
    # qualifying services headings = those followed by a dense run of bios.
    # The real section heading is the LAST such (earlier copies are
    # table-of-contents entries), so its body isn't truncated at the next copy.
    qualifying = []
    for (start, end, _), is_svc in zip(heads, svc):
        if not is_svc:
            continue
        window = html[end:end + _DENSITY_WIN]
        density = sum(_bio_shaped(m.group(1)) for m in _PARA.finditer(window))
        if density >= _DENSITY_MIN:
            qualifying.append(end)
    if not qualifying:
        return None
    sec_start = max(qualifying)
    # end at the next non-services heading after the section start
    nxt = [h[0] for h, is_svc in zip(heads, svc)
           if h[0] >= sec_start and not is_svc]
    return sec_start, (min(nxt) if nxt else len(html))


def _parse_headword(head: str, body: str) -> tuple[str, str | None, int | None]:
    """(surname, given_names, birth_year) from the isolated headword + full body.

    ``head`` is the bold span when present, else the body up to the career dash."""
    head = head.split("—", 1)[0].split("--", 1)[0]
    surname = head.split(",", 1)[0].strip()
    given = None
    if "," in head:
        field = re.split(r"[,(]", head.split(",", 1)[1], 1)[0].strip(" .")
        given = field or None
    bm = _BIRTH.search(body)
    return surname, given, (int(bm.group(1)) if bm else None)


def _page_index(char_off: int, total_chars: int, page_tokens: list[int]) -> int | None:
    if not page_tokens or total_chars <= 0:
        return None
    total = sum(page_tokens)
    if total <= 0:
        return None
    cum, acc = [], 0
    for t in page_tokens:
        acc += t
        cum.append(acc / total)
    return bisect.bisect_left(cum, char_off / total_chars)


def extract_edition(ek: iol_reader.EditionKey, data_dir: str):
    """Segment + parse one edition. Returns (bios, xrefs, stats)."""
    html, page_tokens = iol_reader.load_edition(ek)
    total_chars = len(html)
    stats = {"edition": ek.dirpath.name, "section": None, "n_para": 0,
             "n_bios": 0, "n_xref": 0, "rules_ok": 0, "headword": 0}

    bounds = find_services_section(html)
    if bounds is None:
        stats["section"] = "NOT_FOUND"
        return [], [], stats
    lo, hi = bounds
    stats["section"] = [lo, hi]
    year, era = ek.year, era_for_year(ek.year)

    bios: list[VolumeBio] = []
    xrefs: list[dict] = []
    # Accumulate paragraphs into bios: a paragraph that starts with a name-shaped
    # bold span opens a new biography; following non-bold paragraphs continue it
    # (a long entry is split across <p> at column / page breaks).
    cur_parts: list[str] = []
    cur_bold: str = ""
    cur_pos: int = lo

    def close() -> None:
        nonlocal cur_parts, cur_bold
        if not cur_parts:
            return
        bold, parts = cur_bold, cur_parts
        cur_parts, cur_bold = [], ""
        text = " ".join(p for p in parts if p).strip()
        if len(text) < 12:
            return
        # headword = the bold span if present, else the text up to the career dash
        head = bold or text.split("—", 1)[0].split("--", 1)[0]
        # cross-reference alias: "(see X)" headword, no career body
        if _SEE.search(head) and not _DASH.search(text):
            xrefs.append({"surname": head.split(",", 1)[0].strip(),
                          "target": _SEE.search(head).group(0),
                          "raw_text": text, "edition_year": year})
            return
        if not _DASH.search(text):
            return
        surname, given, birth = _parse_headword(head, text)
        if not surname:
            return
        bio_id = f"iol{ek.tag}-c{cur_pos}"
        prov = [{"family": ek.family, "year": year, "month": ek.month,
                 "char_offset": cur_pos,
                 "page_est": _page_index(cur_pos, total_chars, page_tokens)}]
        events, honours, parser, flags = [], [], "headword", []
        version = EntryVersion(
            version_id=bio_id + ".v", surname_key=_surname_key(text),
            canonical_text=text, era=era, edition_year=year,
            entry_ids=[bio_id], attesting_editions=[year],
        )
        try:
            parsed = rules_parse.parse_rules(version, data_dir)
        except Exception:
            parsed = None
        if parsed is not None:
            events = [e.model_dump() for e in parsed.events]
            honours = [h.model_dump() for h in parsed.honours]
            parser, flags = "rules", list(parsed.flags)
        bios.append(VolumeBio(
            bio_id=bio_id, edition_year=year, surname=surname, given_names=given,
            birth_year=birth, honours=honours, events=events, raw_text=text,
            parser=parser, provenance=prov, flags=flags,
        ))

    for pm in _PARA.finditer(html, lo, hi):
        stats["n_para"] += 1
        inner = pm.group(1)
        text = _text(inner)
        if not text:
            continue
        if _is_headword(text):        # new biography (headword surname start)
            close()
            cur_bold = _lead_bold(inner) or ""   # bonus clean headword when bolded
            cur_pos = pm.start()
            cur_parts = [text]
        elif cur_parts:               # continuation of the current biography
            cur_parts.append(text)
    close()

    stats["n_bios"] = len(bios)
    stats["n_xref"] = len(xrefs)
    stats["rules_ok"] = sum(b.parser == "rules" for b in bios)
    stats["headword"] = sum(b.parser == "headword" for b in bios)
    return bios, xrefs, stats


def extract_all_editions(data_dir: str, cache_dir: str | Path | None = None,
                         refresh: bool = False) -> list[dict]:
    """Extract bios across every IOL edition (duplicate volumes collapsed).

    Per-edition bios cache to ``cache_dir`` (default data/kg/bios/). Writes a
    source-selection audit (``edition_sources.jsonl``), captured cross-reference
    aliases (``xrefs.jsonl``), and a no-bio-section audit
    (``editions_no_bios.jsonl``) into the cache's parent (the KG output root)."""
    cache = Path(cache_dir) if cache_dir else Path("data/kg/bios")
    cache.mkdir(parents=True, exist_ok=True)
    out_root = cache.parent

    editions, audit = iol_reader.available_editions()
    with (out_root / "edition_sources.jsonl").open("w", encoding="utf-8") as fh:
        for row in audit:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    out: list[dict] = []
    all_xrefs: list[dict] = []
    no_bios: list[dict] = []
    for ek in editions:
        cf = cache / f"iol{ek.tag}.jsonl"
        xf = cache / f"iol{ek.tag}.xref.jsonl"
        if cf.exists() and not refresh:
            rows = [json.loads(l) for l in cf.open(encoding="utf-8")]
            out.extend(rows)
            if not rows:
                no_bios.append({"edition": ek.dirpath.name, "year": ek.year,
                                "family": ek.family, "cached": True})
            if xf.exists():
                all_xrefs.extend(json.loads(l) for l in xf.open(encoding="utf-8"))
            continue
        bios, xrefs, stats = extract_edition(ek, data_dir)
        if not bios:
            no_bios.append({"edition": ek.dirpath.name, "year": ek.year,
                            "family": ek.family, "section": stats["section"]})
        rows = [b.to_json() for b in bios]
        with cf.open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        with xf.open("w", encoding="utf-8") as fh:
            for x in xrefs:
                fh.write(json.dumps(x, ensure_ascii=False) + "\n")
        print(f"[iol_bios] {stats['edition']}: {stats['n_bios']} bios "
              f"({stats['rules_ok']} rules / {stats['headword']} headword), "
              f"{stats['n_xref']} xref, section={stats['section']}")
        out.extend(rows)
        all_xrefs.extend(xrefs)

    with (out_root / "xrefs.jsonl").open("w", encoding="utf-8") as fh:
        for x in all_xrefs:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")
    with (out_root / "editions_no_bios.jsonl").open("w", encoding="utf-8") as fh:
        for row in no_bios:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"[iol_bios] {len(editions)} editions -> {len(out)} bios, "
          f"{len(all_xrefs)} xrefs, {len(no_bios)} editions with no Record-of-Services section")
    return out
