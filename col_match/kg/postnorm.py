"""POST-NORMALIZE pass over LLM structs — deterministic cleanup of the
systematic, high-confidence error patterns found in the structuring audits
(docs/STRUCT_ERROR_CATALOG.md).

Runs after structuring (before or alongside validate). It only makes changes it
can justify from the struct ALONE, with high confidence; genuinely ambiguous
cases are left untouched for validate / the LLM. Every change is appended to a
``changes`` list so nothing is silent — the same 0-FP discipline as validate.

Covers (from the catalog):
  * Knight Bachelor split  -> merge ``KT``/``KNT`` + ``BACH`` into one honour
  * ditto / do. positions  -> carry the previous event's position
  * ditto / do. / null place + inheritance -> forward-fill + fix the flag
  * place_inherited on the first event, or with a null place -> false
  * over-claimed terminal contradicted by a later-dated event -> drop
  * honorifics folded into given_names (HON./RT. HON./SIR/"honorary") -> strip
  * "officer in chief" mis-expansion -> "officer in charge"
  * org_type=military with no military signal in the position -> civil

It does NOT try to recover information lost upstream (e.g. an ``off.`` that was
pre-expanded to "officer" when the source meant "office") — that is fixed by not
pre-expanding ambiguous abbreviations on the next run (see normalize.py).
"""

from __future__ import annotations

import re

# ditto markers (dot/space/quote tolerant)
_DITTO = {"ditto", "do"}
# acting vs non-acting cues inside a position string
_ACTING_CUE = re.compile(r"\b(ag|actg|acting|acted)\b\.?", re.I)
# tokens the LLM mistakes for "acting" (temporary / secondment / accountant) —
# they set is_acting=true with no real acting cue in the position
_NONACTING = re.compile(
    r"\b(temp|tempy|temporary|secon|seconded|secondment|acct|acctt|acctnt|accountant)\b", re.I)
# leading honorific / rank / title tokens to strip from given_names (dot/case
# tolerant). Civil honorifics + military ranks (incl. hyphenated compounds, which
# are split on '-' before lookup). Bare peerage nouns (baron/earl/lord/viscount)
# are deliberately EXCLUDED — they can be genuine given names and only appear as
# titles when preceded by an ordinal, which we strip separately.
_HONORIFICS = {
    "the", "rt", "right", "hon", "honble", "honourable", "honorable",
    "honorary", "sir", "dame", "rev", "revd", "reverend", "dr", "prof",
    "capt", "captain", "lieut", "lieutenant", "lt", "col", "colonel",
    "major", "maj", "gen", "general", "brig", "brigadier", "admiral", "adml",
    "marshal", "commander", "commdr", "cdr", "bart", "bt", "baronet", "kt", "knight",
}
_ORDINAL = re.compile(r"\d+(st|nd|rd|th)\.?$", re.I)
_TERMINAL_NONDEATH = {"resigned", "retired", "resigns", "retire", "retires"}


def _key(s: str | None) -> str:
    return re.sub(r"[^a-z]", "", (s or "").lower())


def _is_ditto(s: str | None) -> bool:
    return _key(s) in _DITTO


def _merge_honours(honours: list, changes: list) -> list:
    """Collapse a split Knight Bachelor (``KT``/``KNT`` [+ year] adjacent to
    ``BACH``) into one ``Knight Bachelor`` honour; also fix a single award whose
    text is literally 'KT BACH' / 'KNT BACH'."""
    out: list = []
    i = 0
    n = len(honours)
    while i < n:
        h = honours[i]
        k = _key(h.get("award"))
        nxt = honours[i + 1] if i + 1 < n else None
        nk = _key(nxt.get("award")) if nxt else ""
        if k in {"kt", "knt", "knight"} and nk in {"bach", "bachelor"}:
            yr = h.get("year") or (nxt or {}).get("year")
            out.append({"award": "Knight Bachelor", "year": yr})
            changes.append(f"honour: merged {h.get('award')!r}+{nxt.get('award')!r} -> 'Knight Bachelor'")
            i += 2
            continue
        if k in {"ktbach", "kntbach", "knightbach"}:
            out.append({"award": "Knight Bachelor", "year": h.get("year")})
            changes.append(f"honour: normalized {h.get('award')!r} -> 'Knight Bachelor'")
            i += 1
            continue
        # an order's "Mily."/"Civ." division split off as its own award -> fold
        # the suffix (and its year) back into the preceding real order
        if k in {"mily", "military", "civ", "civil"} and out:
            div = "Military" if k.startswith(("mil",)) else "Civil"
            prev = out[-1]
            out[-1] = {"award": f"{prev.get('award')} ({div})",
                       "year": prev.get("year") or h.get("year")}
            changes.append(f"honour: folded {h.get('award')!r} into {prev.get('award')!r}")
            i += 1
            continue
        # a honorific fabricated into an award ("honorary F" from 'Hon. Frederick')
        # — leading honorific token followed only by initials -> drop
        toks = (h.get("award") or "").split()
        if toks and _key(toks[0]) in _HONORIFICS \
                and all(len(_key(t)) <= 1 for t in toks[1:]):
            changes.append(f"honour: dropped honorific fragment {h.get('award')!r}")
            i += 1
            continue
        out.append(h)
        i += 1
    return out


def _fix_given(given: str | None, changes: list) -> str | None:
    """Strip a leading run of honorific tokens and a trailing parenthetical
    (an electoral riding the LLM sometimes folds in)."""
    if not given:
        return given
    g = re.sub(r"\s*\([^)]*\)?\s*$", "", given).strip()      # trailing "(Riding)"/"(Riding"
    toks = g.split()
    j = 0
    while j < len(toks):
        raw = toks[j]
        # split hyphenated compounds ("Lieut.-General") and require every part
        # to be a title token; or a peerage ordinal ("1st", "2nd")
        subs = [s for s in re.split(r"[-/]", raw) if _key(s)]
        if _ORDINAL.match(raw) or (subs and all(_key(s) in _HONORIFICS for s in subs)):
            j += 1
        else:
            break
    g2 = " ".join(toks[j:]).strip()
    if g2 != (given or "").strip():
        changes.append(f"given_names: {given!r} -> {g2!r}")
    return g2 or None


def _fix_events(events: list, changes: list) -> list:
    """Resolve ditto positions/places, forward-fill inherited places, and fix
    impossible place_inherited flags."""
    out = []
    prev_pos = None
    prev_place = None
    for i, ev in enumerate(events):
        ev = dict(ev)
        pos, place = ev.get("position"), ev.get("place")

        if _is_ditto(pos):
            if prev_pos:
                changes.append(f"event[{i}] position {pos!r} -> {prev_pos!r} (ditto)")
                ev["position"] = pos = prev_pos

        if place is not None and not isinstance(place, str):
            place = str(place)
        if _is_ditto(place):
            if i > 0 and prev_place:
                changes.append(f"event[{i}] place {ev.get('place')!r} -> {prev_place!r} (ditto)")
                ev["place"] = place = prev_place
                ev["place_inherited"] = True
            else:
                ev["place"] = place = None     # ditto with nothing to carry
        elif place is None and ev.get("place_inherited") and i > 0 and prev_place:
            changes.append(f"event[{i}] inherited place -> {prev_place!r}")
            ev["place"] = place = prev_place

        # a first event cannot inherit; inheritance requires a resolved place
        if i == 0 and ev.get("place_inherited"):
            ev["place_inherited"] = False
            changes.append("event[0] place_inherited true -> false (no prior event)")
        if not ev.get("place") and ev.get("place_inherited"):
            ev["place_inherited"] = False
            changes.append(f"event[{i}] place_inherited true but place null -> false")
        # inheritance means "same place as before"; an explicit, different place
        # is not inherited (only the position carried)
        if ev.get("place_inherited") and ev.get("place") and prev_place \
                and _key(ev["place"]) != _key(prev_place):
            ev["place_inherited"] = False
            changes.append(f"event[{i}] place_inherited true but place differs from prior -> false")

        # is_acting: trust the acting cue in the position. Set true when present
        # but flag missing; clear when a non-acting token (temp./secon./acctt.)
        # is what tripped a false positive.
        pos_s = ev.get("position") or ""
        if _ACTING_CUE.search(pos_s):
            if not ev.get("is_acting"):
                ev["is_acting"] = True
                changes.append(f"event[{i}] is_acting false -> true (acting cue in position)")
        elif ev.get("is_acting") and _NONACTING.search(pos_s):
            ev["is_acting"] = False
            changes.append(f"event[{i}] is_acting true -> false (temporary/secondment/accountant, not acting)")

        # year_end fabrication on POINT appointments: the LLM duplicates the
        # start into year_end (zero-length span). Safe to null — the event stays
        # anchored to year_start. (A "ye==next-event-start" rule was tried and
        # REJECTED: it destroyed legitimate source ranges like "1914-16" whenever
        # the next post happened to start the same year the prior one ended.)
        ys, ye = ev.get("year_start"), ev.get("year_end")
        if ye is not None and ys is not None and ye == ys:
            ev["year_end"] = None
            changes.append(f"event[{i}] year_end=={ys} (point appointment) -> null")

        # "officer in chief" -> "officer in charge" (commander-in-chief untouched)
        if ev.get("position"):
            fixed = re.sub(r"\bofficer in chief\b", "officer in charge", ev["position"], flags=re.I)
            if fixed != ev["position"]:
                changes.append(f"event[{i}] position 'officer in chief' -> 'officer in charge'")
                ev["position"] = fixed

        # NOTE: org_type military->civil is intentionally NOT corrected here.
        # The military signal often lives in the source dates/context, not the
        # position noun, so a position-only rule over-fires (it downgraded ~35%
        # of structs in testing). org_type is better fixed at the prompt (default
        # civil unless an explicit military rank/branch appears) on a future run.

        if ev.get("position"):
            prev_pos = ev["position"]
        if ev.get("place"):
            prev_place = ev["place"]
        out.append(ev)
    return out


def _guard_terminal(struct: dict, events: list, changes: list) -> dict | None:
    """Drop a non-death terminal (resigned/retired) that a later-dated event
    contradicts — the career visibly continued, so it was a mid-career role end."""
    term = struct.get("terminal")
    if not term:
        return term
    status = _key(term.get("status"))
    ty = term.get("year")
    if status in _TERMINAL_NONDEATH and ty:
        later = [e.get("year_start") for e in events if e.get("year_start") and e["year_start"] > ty]
        if later:
            changes.append(f"terminal {term.get('status')} {ty} dropped (event in {max(later)} follows)")
            return {}
    return term


def normalize_struct(struct: dict) -> tuple[dict, list[str]]:
    """Return ``(cleaned_struct, changes)``. ``changes`` lists every applied
    transformation; empty list means the struct was already clean."""
    changes: list[str] = []
    out = dict(struct)
    out["given_names"] = _fix_given(struct.get("given_names"), changes)
    out["honours"] = _merge_honours(struct.get("honours") or [], changes)
    events = _fix_events(struct.get("events") or [], changes)
    out["events"] = events
    out["terminal"] = _guard_terminal(struct, events, changes)
    return out, changes
