"""Services-section biography extraction from layout-aware OCR blocks.

The services section ("RECORD of the Public Services of Officers …") is a run
of ``text`` blocks, one biography per block, each opening with an intact
uppercase headword surname (FLANAGAN, FLEISCHER …). Unlike the old flowed
markdown, headwords are NOT truncated here, so segmentation is a block-native
rule: a block whose text starts with the headword shape begins a new biography;
any following non-headword text block continues it (column / page spillover).

Career parsing reuses the deterministic ``col_match.services.rules_parse`` —
its grammar is format-agnostic on entry text. Entries the rules tier cannot
fully account for are emitted with ``parser="unparsed"`` and their raw text, to
be re-parsed by the Qwen LLM tier on the GPU box (see ``llm.py``).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..services import rules_parse
from ..services.corpus import era_for_year
from ..services.schema import EntryVersion
from .reader import Block

# Headword: CAPS surname (Mc/Mac/O'/de internal lowercase allowed), then comma.
_HEADWORD = re.compile(r"^([A-Z][A-Za-z'’\-]{1,}(?: [A-Z][A-Za-z'’\-]+)*),\s+\S")
_DASH = re.compile(r"[—–]")
# Section start marker (a title block in the new OCR).
# header wording varies by era: "RECORD of the Public Services of Officers …"
# (1883–1940s) and "RECORD OF SERVICES" (late editions).
_SECTION_START = re.compile(r"record\s+of\s+(?:the\s+)?(?:public\s+)?services?\b", re.I)
# Hard stop: an index / errata run after the services section.
_SECTION_STOP = re.compile(r"^(INDEX|ERRATA|ADDENDA|CORRIGENDA)\b", re.I)


def _caps_fraction(surname: str) -> float:
    letters = [c for c in surname if c.isalpha()]
    return sum(c.isupper() for c in letters) / len(letters) if letters else 0.0


def _is_headword(text: str) -> bool:
    m = _HEADWORD.match(text)
    return bool(m) and _caps_fraction(m.group(1)) >= 0.7


def _join(parts: list[str]) -> str:
    out = ""
    for piece in (p.strip() for p in parts):
        if out.endswith("-") and piece[:1].islower():
            out = out[:-1] + piece
        else:
            out = (out + " " + piece).strip()
    return re.sub(r"\s+", " ", out)


def _surname_key(text: str) -> str:
    return re.sub(r"[^A-Z]", "", text.split(",", 1)[0].upper())


@dataclass
class VolumeBio:
    bio_id: str
    edition_year: int
    surname: str
    given_names: str | None
    birth_year: int | None
    honours: list[dict]
    events: list[dict]                      # position/place/year_start/year_end
    raw_text: str
    parser: str                             # rules | unparsed
    provenance: list[dict] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        return self.__dict__


# density-fallback tunables (block-index windows over the whole volume)
_DWIN = 60          # blocks per density window
_DMIN = 12          # headword text blocks per window to count as "inside" the section
_DMIN_RUN = 200     # smallest plausible services section (headword blocks)


def _find_section_by_density(blocks: list[Block]) -> tuple[int, int] | None:
    """Fallback when the header wording dodges the regex (e.g. 1939): the
    services section is by far the densest contiguous run of headword-shaped
    ``text`` blocks. Mirrors the windowed-density idea in services/segment.py,
    but over OCR blocks instead of markdown lines."""
    hw = [i for i, b in enumerate(blocks)
          if b.category == "text" and _is_headword(b.text)]
    if len(hw) < _DMIN_RUN:
        return None
    counts: dict[int, int] = {}
    for i in hw:
        counts[i // _DWIN] = counts.get(i // _DWIN, 0) + 1
    inside = {w for w, c in counts.items() if c >= _DMIN}
    if not inside:
        return None
    # longest contiguous run of dense windows, tolerating 1-window gaps
    best = (0, -1, -1)  # (n_headwords, first_window, last_window)
    w = min(inside)
    hi_w = max(inside)
    while w <= hi_w:
        if w not in inside:
            w += 1
            continue
        end, gap = w, 0
        for v in range(w + 1, hi_w + 1):
            if v in inside:
                end, gap = v, 0
            else:
                gap += 1
                if gap > 1:
                    break
        n = sum(counts.get(x, 0) for x in range(w, end + 1))
        if n > best[0]:
            best = (n, w, end)
        w = end + gap + 1
    if best[0] < _DMIN_RUN:
        return None
    lo_blk = best[1] * _DWIN
    hi_blk = (best[2] + 1) * _DWIN
    in_run = [i for i in hw if lo_blk <= i < hi_blk]
    return in_run[0], min(in_run[-1] + 30, len(blocks))


def find_services_section(blocks: list[Block]) -> tuple[int, int] | None:
    """Return (start_idx, end_idx) into ``blocks`` bounding the services run,
    or None. Start = first block whose text matches the section header; end =
    an INDEX/ERRATA stop, else end of volume. Falls back to headword-block
    density when the header wording isn't recognized (header text varies by
    era and one variant zeroed out 1939)."""
    start = None
    for i, b in enumerate(blocks):
        if b.category in ("title", "header", "text") and _SECTION_START.search(b.text):
            start = i
            break
    if start is None:
        return _find_section_by_density(blocks)
    end = len(blocks)
    for i in range(start + 1, len(blocks)):
        if blocks[i].category in ("title", "header") and _SECTION_STOP.match(blocks[i].text):
            end = i
            break
    return start, end


def extract_bios(blocks: list[Block], data_dir: str) -> tuple[list[VolumeBio], dict]:
    """Segment + parse the services section. Returns (bios, stats)."""
    bounds = find_services_section(blocks)
    stats: dict = {"section": None, "n_blocks": 0, "n_bios": 0, "rules_ok": 0, "unparsed": 0}
    if bounds is None:
        return [], stats
    lo, hi = bounds
    stats["section"] = [lo, hi]
    region = [b for b in blocks[lo:hi] if b.category == "text"]
    stats["n_blocks"] = len(region)

    year = blocks[lo].edition_year
    doc = blocks[lo].doc
    era = era_for_year(year)

    bios: list[VolumeBio] = []
    cur_parts: list[str] = []
    cur_prov: list[dict] = []

    def close() -> None:
        if not cur_parts:
            return
        text = _join(cur_parts)
        # require a name/career separator — drops stray non-entry text blocks
        if len(text) < 25 or not _DASH.search(text):
            cur_parts.clear()
            cur_prov.clear()
            return
        head = cur_prov[0]
        bio_id = f"{doc}{year}-p{head['page']}b{head['block']}"
        version = EntryVersion(
            version_id=bio_id + ".v",
            surname_key=_surname_key(text),
            canonical_text=text,
            era=era,
            edition_year=year,
            entry_ids=[bio_id],
            attesting_editions=[year],
        )
        parsed = rules_parse.parse_rules(version, data_dir)
        if parsed is not None:
            bio = VolumeBio(
                bio_id=bio_id, edition_year=year, surname=parsed.surname,
                given_names=parsed.given_names, birth_year=parsed.birth_year,
                honours=[h.model_dump() for h in parsed.honours],
                events=[e.model_dump() for e in parsed.events],
                raw_text=text, parser="rules",
                provenance=list(cur_prov), flags=list(parsed.flags),
            )
        else:
            surname = text.split(",", 1)[0].strip()
            bio = VolumeBio(
                bio_id=bio_id, edition_year=year, surname=surname,
                given_names=None, birth_year=None, honours=[], events=[],
                raw_text=text, parser="unparsed",
                provenance=list(cur_prov), flags=["rules_failed"],
            )
        bios.append(bio)
        cur_parts.clear()
        cur_prov.clear()

    for b in region:
        if _is_headword(b.text):
            close()
        cur_parts.append(b.text)
        cur_prov.append(b.prov)
    close()

    stats["n_bios"] = len(bios)
    stats["rules_ok"] = sum(b.parser == "rules" for b in bios)
    stats["unparsed"] = sum(b.parser == "unparsed" for b in bios)
    return bios, stats
