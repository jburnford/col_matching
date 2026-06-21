"""VALIDATE pass — Python reviews the LLM, never the reverse.

Deterministic guards over the generative step (the old project's 0-FP
discipline: "the model never gets the last word"). Anything the LLM emits that
is not supported by the source entry text is dropped or flagged — it can never
silently enter the KG.

Checks per structured biography:
  * every event year (year_start/year_end) must appear verbatim in the source;
  * every NON-inherited place must appear (token-wise) in the source — guards
    against a hallucinated/upgraded colony;
  * birth_year, honour award-years, terminal year must appear in the source;
  * sanity: year ordering and a plausible career span.
Dropped items are recorded in ``flags`` for audit, not silently discarded.
"""

from __future__ import annotations

import re

_YEAR = re.compile(r"\b1[789]\d\d\b")
# abbreviated ranges the source prints: "1900-02", "1884-5", "1914-19"
_YEAR_RANGE = re.compile(r"\b(1[789]\d\d)\s*[-–—]\s*(\d{1,2})\b")
_WORD = re.compile(r"[A-Za-z]+")
_MAX_SPAN = 75   # years; longer than a plausible single career -> flag


def _years_in(text: str) -> set[int]:
    years = {int(y) for y in _YEAR.findall(text)}
    # expand abbreviated end-years ("1900-02" -> 1902, "1884-5" -> 1885) so a
    # legitimate event year_end isn't dropped as "not in source".
    for start, end in _YEAR_RANGE.findall(text):
        years.add(int(start[: 4 - len(end)] + end))
    return years


def _place_supported(place: str, source_lower: str) -> bool:
    """A place is supported if any of its alphabetic tokens of length >=4
    appears in the source (OCR-tolerant; handles 'N. Nigeria' -> 'Nigeria',
    'Cape of Good Hope' -> 'Cape'/'Good'/'Hope')."""
    toks = [t.lower() for t in _WORD.findall(place) if len(t) >= 4]
    if not toks:  # very short place ('Uva', 'Aden') — require exact substring
        return place.lower() in source_lower
    return any(t in source_lower for t in toks)


def validate_struct(struct: dict, source_text: str,
                    extra_years=None, extra_places=None) -> dict:
    """Return a cleaned copy of ``struct`` with unsupported facts dropped, a
    human-readable ``flags`` list, and a structured ``_review`` list (one packet
    per drop: ``{field_path, flagged_value, reason, action}``) so each dropped
    fact can be routed to an independent reviewer LLM instead of vanishing.

    ``extra_years``/``extra_places`` are reviewer-confirmed values (each backed
    by a real source quote, verified by the caller) that should NOT be dropped
    even when the deterministic source scan misses them — the merge-back path
    for the second-LLM review (0-FP preserved: the caller gates the quote)."""
    src = source_text.lower()
    src_years = _years_in(source_text) | set(extra_years or ())
    _extra_places = {p.lower() for p in (extra_places or ())}
    flags: list[str] = []
    review: list[dict] = []
    out = dict(struct)

    def flag(path, value, reason, action, msg):
        flags.append(msg)
        review.append({"field_path": path, "flagged_value": value,
                       "reason": reason, "action": action})

    # birth year
    if struct.get("birth_year") and struct["birth_year"] not in src_years:
        flag("birth_year", struct["birth_year"], "year not found in source", "nulled",
             f"birth_year {struct['birth_year']} not in source -> null")
        out["birth_year"] = None

    # honours: award-year must be in source (else drop the year, keep award)
    hon = []
    for i, h in enumerate(struct.get("honours") or []):
        hy = h.get("year")
        if hy and hy not in src_years:
            flag(f"honours[{i}].year", hy, f"award {h.get('award')!r} year not in source",
                 "nulled", f"honour {h.get('award')} year {hy} not in source -> null")
            h = {**h, "year": None}
        hon.append(h)
    out["honours"] = hon

    # events
    kept = []
    for i, ev in enumerate(struct.get("events") or []):
        ys, ye = ev.get("year_start"), ev.get("year_end")
        if ys and ys not in src_years:
            flag(f"events[{i}]", ev, f"year_start {ys} not in source", "event_dropped",
                 f"event[{i}] year_start {ys} not in source -> dropped")
            continue
        if ye and ye not in src_years:
            flag(f"events[{i}].year_end", ye, "year_end not in source", "nulled",
                 f"event[{i}] year_end {ye} not in source -> null")
            ev = {**ev, "year_end": None}
        place = ev.get("place")
        if place and not ev.get("place_inherited") and not _place_supported(place, src) \
                and place.lower() not in _extra_places:
            flag(f"events[{i}].place", place, "place tokens not in source", "nulled",
                 f"event[{i}] place {place!r} unsupported -> null")
            ev = {**ev, "place": None}
        if ys and ye and ye < ys:
            flag(f"events[{i}].year_end", ye, f"year_end < year_start {ys}", "nulled",
                 f"event[{i}] year_end<{ys} -> null")
            ev = {**ev, "year_end": None}
        kept.append(ev)
    out["events"] = kept

    # terminal year
    term = struct.get("terminal")
    if term and term.get("year") and term["year"] not in src_years:
        flag("terminal.year", term["year"], "terminal year not in source", "nulled",
             f"terminal year {term['year']} not in source -> null")
        out["terminal"] = {**term, "year": None}

    # career span sanity (a warning, not a drop -> flag only, no review packet)
    eyears = [e["year_start"] for e in kept if e.get("year_start")]
    if eyears and max(eyears) - min(eyears) > _MAX_SPAN:
        flags.append(f"career span {max(eyears)-min(eyears)}y > {_MAX_SPAN} (check dedup)")

    out["flags"] = flags
    out["_review"] = review
    return out
