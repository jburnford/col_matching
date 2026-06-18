"""Match compiled Biographies to COL_Official stints (the graph's per-colony
career segments).

Semantics: a biography event is an APPOINTMENT (start date); its tenure runs
until the next dated event in the same biography (or terminal year). A stint
is the run of editions in which the resulting posting was listed — editions
lag appointments and are sparse, so alignment is tenure-overlap, not
year-equality.

Conservatism:
- candidate gate: exact normalized surname + initial-sequence compatibility;
- a single event matches a stint only when colony, tenure overlap AND a
  corroborating dimension (position similarity against the stint's printed
  positions, or a shared honour) all agree — three independent dimensions;
- two tenure-overlapping events in the stint's colony also suffice;
- events whose place was inherited from a previous clause can only ever add
  support, never establish a match;
- ambiguity guard: if two different officials' stints in the same colony and
  overlapping years both pass for one biography — or two biographies both
  pass for one stint — at comparable strength, ALL of them are dropped and
  counted as ambiguous. A missed link is recoverable; a wrong one is not.
"""

from __future__ import annotations

import os
import re
from collections import defaultdict

from rapidfuzz import fuzz, process
from rapidfuzz import distance

from . import gazetteer
from .compile import _pos_norm
from .schema import Agreement, Biography, StintMatch

_NORM = re.compile(r"[^a-z0-9 ]")

POSITION_SIM = 60          # token_set_ratio threshold for position agreement
HIGH_POS_INHERITED = 85    # position bar for an inherited place to establish a match
OPEN_TENURE_YEARS = 12     # cap for an open-ended final appointment
AMBIGUITY_MARGIN = 25      # strength gap required to keep the stronger of two
MAX_DROP = 3               # max leading chars an OCR headword may lose (Griffiths->FFITHS)
MIN_TRUNC_LEN = 5          # min surviving suffix length for a truncation match
TRUNC_POS = 70             # printed-position bar for a truncation match (> POSITION_SIM)


def _norm(s: str | None) -> str:
    return _NORM.sub("", (s or "").lower()).strip()


def _initials(given: str | None) -> list[str]:
    return [t[0].upper() for t in re.split(r"[ .]+", given or "") if t and t[0].isalpha()]


def _names_compatible(bio_given: str | None, official_given: str | None) -> bool:
    """Initial sequences must align as an ordered subsequence — tolerant of a
    dropped forename on either side ("Geoffrey Miles" vs "Miles"). Collisions
    this loosens are handled by the ambiguity guard."""
    a, b = _initials(bio_given), _initials(official_given)
    if not a or not b:
        return True
    short, long_ = (a, b) if len(a) <= len(b) else (b, a)
    i = 0
    for x in long_:
        if i < len(short) and short[i] == x:
            i += 1
    return i == len(short)


def _surname_of_official(name: str | None) -> str:
    return _norm((name or "").split(",", 1)[0])


def _colony_norm(colony: str | None, data_dir: str) -> str:
    hit = gazetteer.lookup(colony or "", data_dir)
    return _norm(hit or colony)


def _tenures(bio: Biography) -> list[tuple[int, int, int]]:
    """(event_index, start, end) for placed events; end = next dated event's
    start (career events are sequential), else terminal year, else capped."""
    dated = [(i, ev) for i, ev in enumerate(bio.events) if ev.year_start is not None]
    out = []
    for k, (i, ev) in enumerate(dated):
        if not ev.place:
            continue
        if ev.year_end is not None:
            end = ev.year_end
        else:
            nxt = next((e.year_start for _, e in dated[k + 1:] if e.year_start > ev.year_start), None)
            if nxt is not None:
                end = nxt
            elif bio.terminal and bio.terminal.year:
                end = bio.terminal.year
            else:
                end = ev.year_start + OPEN_TENURE_YEARS
        out.append((i, ev.year_start, end))
    return out


def _surname_block(
    bio: Biography, by_surname: dict[str, list[dict]], surname_keys: list[str]
) -> tuple[list[dict], bool]:
    """Exact surname block, else OCR-tolerant fuzzy surname retrieval
    (guarded: length-scaled edit distance, and callers demand a STRONG
    evidence bar for fuzzy hits)."""
    key = _norm(bio.surname)
    if key in by_surname:
        return by_surname[key], False
    if len(key) < 5:
        return [], False
    # short OCR-garbled surnames need a 2-edit window too (TYSEN~Tyson is
    # dist 1, but HORNYEY~Hornby, PIEVAR~Phear, JEROVIS~Jervois are dist 2 in
    # len 6-7 names the old `<8 -> 1` rule could never retrieve). The fuzzy
    # path is governed by `_align(require_strong=True)` — colony+tenure+
    # position/honour corroboration is mandatory and `_disambiguate` forbids a
    # fuzzy hit displacing or tying an exact-surname one — so the wider block
    # only surfaces candidates; the strong bar and the FP gate still decide.
    max_dist = 2
    out = []
    for k, _dist, _idx in process.extract(
        key, surname_keys, scorer=distance.Levenshtein.distance,
        score_cutoff=max_dist, limit=8,
    ):
        out.extend(by_surname[k])
    return out, True


def _truncation_index(surname_keys: list[str]) -> dict[str, list[str]]:
    """suffix -> official surname keys for which that suffix is the key with a
    1..MAX_DROP leading-char prefix dropped. Models the services-section OCR
    headword truncation (Griffiths->FFITHS, Camacho->MACHO): the clean record
    surname exists, only the bio's bold entry-header lost its first 1-3 chars.
    Built ONCE over officials (O(officials)); a per-bio scan of every surname
    key would be O(bios*keys) and is avoided."""
    index: dict[str, list[str]] = defaultdict(list)
    for k in surname_keys:
        if len(k) < 6:
            continue
        for d in range(1, MAX_DROP + 1):
            suf = k[d:]
            if len(suf) >= MIN_TRUNC_LEN:
                index[suf].append(k)
    return index


def _truncation_block(
    bio_key: str, trunc_index: dict[str, list[str]],
    by_surname: dict[str, list[dict]],
) -> list[dict]:
    """Officials whose surname key is `bio_key` with a small dropped prefix —
    i.e. `bio_key` is a clean suffix of the official's surname (the OCR
    headword-truncation signal). The exact key is excluded (it is the normal
    exact-surname block)."""
    out: list[dict] = []
    for k in trunc_index.get(bio_key, ()):
        if k == bio_key:
            continue
        out.extend(by_surname[k])
    return out


def match_biographies(
    bios: list[Biography], officials: list[dict], data_dir: str
) -> tuple[list[StintMatch], dict]:
    by_surname: dict[str, list[dict]] = defaultdict(list)
    for o in officials:
        by_surname[_surname_of_official(o["name"])].append(o)

    surname_keys = list(by_surname)
    trunc_on = os.environ.get("COL_NO_TRUNC") != "1"
    trunc_index = _truncation_index(surname_keys) if trunc_on else {}

    candidates: list[tuple[StintMatch, int]] = []  # (match, strength)
    for bio in bios:
        cands, fuzzy = _surname_block(bio, by_surname, surname_keys)
        tried: set = set()
        for official in cands:
            tried.add(official["id"])
            given_off = (official["name"].split(",", 1)[1].strip()
                         if "," in (official["name"] or "") else None)
            if not _names_compatible(bio.given_names, given_off):
                continue
            result = _align(bio, official, data_dir, require_strong=fuzzy)
            if result is not None:
                candidates.append(result)
        if trunc_on:
            for official in _truncation_block(_norm(bio.surname), trunc_index, by_surname):
                if official["id"] in tried:
                    continue
                tried.add(official["id"])
                given_off = (official["name"].split(",", 1)[1].strip()
                             if "," in (official["name"] or "") else None)
                if not _names_compatible(bio.given_names, given_off):
                    continue
                result = _align(bio, official, data_dir, require_strong=True, trunc=True)
                if result is not None:
                    candidates.append(result)

    bio_given = {b.bio_id: b.given_names for b in bios}
    off_name = {o["id"]: o["name"] for o in officials}
    matches, ambiguous = _disambiguate(candidates, bio_given, off_name)
    stats = {
        "biographies": len(bios),
        "candidate_matches": len(candidates),
        "dropped_ambiguous": ambiguous,
        "matches": len(matches),
        "bios_matched": len({m.bio_id for m in matches}),
        "stints_matched": len({m.official_id for m in matches}),
    }
    return matches, stats


def _cooc_scan(bio: Biography, official: dict, colony: str,
               data_dir: str) -> list[tuple[int, int]]:
    """PER-EDITION CO-OCCURRENCE: the bio's attesting editions and the stint's
    records come from the same printed volumes. A services entry in edition
    Y means the person is serving somewhere in Y (retirees stay only if
    honoured) — so the bio's current posting at Y should appear in Y's
    staff lists: same colony, same year, similar position. Each agreeing
    edition-year is an independent confirmation. Returns (year, position
    score) per agreeing edition."""
    records_by_year: dict[int, list[str]] = defaultdict(list)
    for r in official["records"]:
        if r.get("position_raw"):
            records_by_year[r["year"]].append(r["position_raw"])
    terminal_year = bio.terminal.year if bio.terminal and bio.terminal.year else None
    cooc_years = []
    for y in bio.editions:
        if y not in records_by_year:
            continue
        if terminal_year and y > terminal_year + 1:
            continue  # honoured retirees stay listed; post-retirement years prove nothing
        current = None
        for ev in bio.events:
            if ev.year_start is not None and ev.year_start <= y and ev.place:
                current = ev
        if current is None:
            continue
        # currency guard: a posting decades stale can't vouch for year Y —
        # a same-name successor may hold the listed job by then
        cur_end = current.year_end or current.year_start + OPEN_TENURE_YEARS
        if y > cur_end + 2:
            continue
        if colony not in gazetteer.colony_targets(current.place, data_dir):
            continue
        best = max((fuzz.token_set_ratio(_pos_norm(current.position), _pos_norm(p))
                    for p in records_by_year[y]), default=0)
        if best >= 55:
            cooc_years.append((y, best))
    return cooc_years


def _align(bio: Biography, official: dict, data_dir: str,
           require_strong: bool = False,
           trunc: bool = False) -> tuple[StintMatch, int] | None:
    colony = gazetteer.norm(official["colony"] or "")
    fy, ly = official["first_year"], official["last_year"]
    if fy is None or ly is None:
        return None
    # a stint can't begin before the person could have served: birth-year
    # sanity is a hard kill independent of name/colony evidence
    if bio.birth_year and fy < bio.birth_year.value + 15:
        return None
    if bio.terminal and bio.terminal.kind == "died" and bio.terminal.year \
            and fy > bio.terminal.year:
        return None
    stint_positions = [r["position_raw"] for r in official["records"] if r.get("position_raw")]
    stint_honours = {_norm(h) for r in official["records"] for h in (r.get("honors") or [])}
    bio_honours = {_norm(h.award) for h in bio.honours}

    agreements: list[Agreement] = []
    strength = 0
    best_printed_pos = 0       # max pos_score over genuinely printed (non-inherited) events
    honour_any = False
    promote_inherited = os.environ.get("COL_NO_INHERIT_POS") != "1"

    cooc_years = _cooc_scan(bio, official, colony, data_dir)
    if cooc_years:
        years = [y for y, _ in cooc_years]
        avg = sum(s for _, s in cooc_years) / len(cooc_years)
        agreements.append(Agreement(
            kind="edition_cooccurrence", bio_event_index=-1,
            record_year=years[0],
            detail=f"printed:{len(years)}yrs {years[:6]} pos~{avg:.0f}",
        ))
        if len(years) >= 2:
            strength = max(strength, 100 + min(len(years), 6) * 10 + int(avg) // 4)
    for i, start, end in _tenures(bio):
        ev = bio.events[i]
        if colony not in gazetteer.colony_targets(ev.place, data_dir):
            continue
        if end < fy - 1 or start > ly + 1:
            continue
        pos_score = 0
        for pos in stint_positions:
            pos_score = max(pos_score, fuzz.token_set_ratio(_pos_norm(ev.position), _pos_norm(pos)))
        honour_hit = bool(stint_honours & bio_honours)
        if not ev.place_inherited:
            best_printed_pos = max(best_printed_pos, pos_score)
        if honour_hit:
            honour_any = True
        # An inherited place is normally weak evidence (it may have been carried
        # across a missed colony change), so it can only ADD support. BUT a
        # near-exact position match (>=HIGH_POS_INHERITED) on top of exact
        # surname+initials+colony+tenure is strong independent evidence that the
        # carry is correct (TURNER: HK printed 1948, inherited tail, the 1955 HK
        # "Assistant Commissioner" stint matches at pos 100). Promote those to
        # printed-quality. Env COL_NO_INHERIT_POS=1 reverts.
        promoted = (ev.place_inherited and pos_score >= HIGH_POS_INHERITED
                    and promote_inherited)
        weak_place = ev.place_inherited and not promoted
        strong = (pos_score >= POSITION_SIM or honour_hit) and not weak_place
        kind = "colony_tenure_position" if pos_score >= POSITION_SIM else (
            "colony_tenure_honour" if honour_hit else "colony_tenure")
        detail = (f"{'inherited' if weak_place else 'printed'}:{ev.place}"
                  f"@{start}-{end} pos~{pos_score}" + (" honour" if honour_hit else ""))
        agreements.append(Agreement(kind=kind, bio_event_index=i, record_year=fy, detail=detail))
        strength = max(strength, pos_score + (20 if honour_hit else 0)
                       - (30 if weak_place else 0))
        if strong:
            strength = max(strength, 100 + pos_score)

    if not agreements:
        return None
    cooc = next((a for a in agreements if a.kind == "edition_cooccurrence"), None)
    cooc_n = int(cooc.detail.split("yrs")[0].split(":")[1]) if cooc else 0
    has_strong = any(a.kind not in ("colony_tenure", "edition_cooccurrence")
                     for a in agreements if not a.detail.startswith("inherited")) \
        or cooc_n >= 2
    printed = [a for a in agreements if a.detail.startswith("printed")]
    if trunc:
        # OCR headword-truncation surname: the surname evidence is the WEAKEST
        # of any path (a clean suffix of the official surname), so the other
        # dimensions must be strong and INDEPENDENT of initials:
        #   1. a real shared SPELLED forename (not just compatible initials —
        #      excludes the initials-only coincidence OWELL->Powell/Howell);
        #   2. a genuinely printed place event scoring >= TRUNC_POS (a higher
        #      bar than POSITION_SIM), OR a shared honour, OR >=2 cooc years.
        given_off = (official["name"].split(",", 1)[1].strip()
                     if "," in (official["name"] or "") else None)
        trunc_strong = best_printed_pos >= TRUNC_POS or honour_any or cooc_n >= 2
        if not (_shared_spelled_forename(bio.given_names, given_off)
                and printed and trunc_strong):
            return None
        strength -= 20
    elif require_strong:
        # OCR-fuzzy surname: position/honour corroboration is mandatory and
        # the surname mismatch itself costs strength in disambiguation
        if not (has_strong and printed):
            return None
        strength -= 20
    elif not (has_strong and printed):
        # the bare "two tenure overlaps" path is gone: it accepted matches
        # with no position/honour/co-occurrence corroboration at all
        # (measured false positives at pos~23)
        return None
    return (
        StintMatch(bio_id=bio.bio_id, official_id=official["id"],
                   n_agreements=len(agreements), agreements=agreements,
                   fuzzy_surname=require_strong),
        strength,
    )


def _shared_spelled_forename(a: str | None, b: str | None) -> bool:
    """True iff `a` and `b` share at least one SPELLED-OUT forename token
    (length > 1), OCR-tolerant (one edit). A shared spelled forename is the
    signal that two same-surname biographies are duplicate fragments of one
    person rather than distinct same-name people. Pure-initial agreement is
    deliberately NOT enough — that is exactly the single-initial collision the
    ambiguity guard exists to catch."""
    from .compile import _token_match_ocr

    ta = [t for t in re.split(r"[ .]+", a or "") if len(t) > 1 and t[0].isalpha()]
    tb = [t for t in re.split(r"[ .]+", b or "") if len(t) > 1 and t[0].isalpha()]
    return any(_token_match_ocr(x, y) for x in ta for y in tb)


def _tight_name_match(bio_given: str | None, off_name: str) -> bool:
    """True iff a biography's name matches a stint official's name TIGHTLY, not
    just as a loose subsequence: after stripping honorifics, the initial
    sequences are EQUAL, or a spelled-out forename is shared. This rejects the
    initial-deficient coincidence ("Edward" [E] vs "H. E. S" [H,E,S]) that
    `_align`'s subsequence gate accepts and the ambiguity guard normally
    backstops."""
    og = off_name.split(",", 1)[1] if "," in off_name else ""
    bt = _strip_honorifics([t for t in re.split(r"[ .]+", bio_given or "") if t and t[0].isalpha()])
    ot = _strip_honorifics([t for t in re.split(r"[ .]+", og) if t and t[0].isalpha()])
    if not bt or not ot:
        return False
    if [t[0].upper() for t in bt] == [t[0].upper() for t in ot]:
        return True
    return _shared_spelled_forename(bio_given, og)


def _all_same_person(bio_ids: list[str], bio_given: dict[str, str]) -> bool:
    """True iff every distinct biography in a stint contest is, pairwise, a
    confident duplicate of the others (shared spelled forename). Then the
    contest is illusory — duplicate fragments of one person both matched the
    stint — and keeping the link cannot mis-assign the career."""
    ids = list(dict.fromkeys(bio_ids))
    if len(ids) < 2:
        return True
    return all(
        _shared_spelled_forename(bio_given.get(ids[i], ""), bio_given.get(ids[j], ""))
        for i in range(len(ids)) for j in range(i + 1, len(ids))
    )


_HONORIFICS = {
    "the", "hon", "hony", "honorary", "sir", "lady", "dame", "dr", "rev", "revd",
    "mr", "mrs", "miss", "rt", "right", "col", "colonel", "capt", "captain",
    "maj", "major", "lieut", "lt", "lieutenant", "gen", "general", "brig",
    "brigadier", "adm", "admiral", "commodore", "cmdr", "commander", "prof",
    "professor", "sgt", "sergeant", "mister", "esq",
    # chiefly / non-British titles that print before the name like a rank
    "ratu", "raja", "rajah", "tunku", "tengku", "dato", "datuk",
}


def _strip_honorifics(tokens: list[str]) -> list[str]:
    return [t for t in tokens if t.rstrip(".").lower() not in _HONORIFICS]


def _same_official(oid_a: str, oid_b: str, off_name: dict[str, str]) -> bool:
    """True iff two stint records are the SAME official re-listed (a printed
    honorific/initial variant — "Drew, John Michael" vs "Drew, The Hon. J. M.",
    "Hill, S. J." vs "Hill, Col. Stephen J."), not two distinct same-name
    people. Same surname, and — after stripping honorifics — EQUAL initial
    sequences (so "Edward" [E] vs "H. E. S" [H,E,S] is NOT unified: the extra
    H/S initials are unexplained), or a shared spelled-out forename with
    non-contradictory initials."""
    na, nb = off_name.get(oid_a, ""), off_name.get(oid_b, "")
    if _surname_of_official(na) != _surname_of_official(nb):
        return False
    ga = na.split(",", 1)[1] if "," in na else ""
    gb = nb.split(",", 1)[1] if "," in nb else ""
    ta = _strip_honorifics([t for t in re.split(r"[ .]+", ga) if t and t[0].isalpha()])
    tb = _strip_honorifics([t for t in re.split(r"[ .]+", gb) if t and t[0].isalpha()])
    if not ta or not tb:
        return True            # one side was only honorifics: cannot contradict
    ia = [t[0].upper() for t in ta]
    ib = [t[0].upper() for t in tb]
    if ia == ib:
        return True
    return _shared_spelled_forename(ga, gb) and _names_compatible(ga, gb)


def _disambiguate(
    candidates: list[tuple[StintMatch, int]],
    bio_given: dict[str, str] | None = None,
    off_name: dict[str, str] | None = None,
) -> tuple[list[StintMatch], int]:
    """Drop comparable-strength competitors on either side of the match —
    EXCEPT when the "competitors" are actually the same entity (duplicate
    biography fragments contesting one stint, or one official re-listed under a
    bio's colony). Those are not genuine contests and dropping them only loses
    true links."""
    _refine = os.environ.get("COL_NO_AMBIG_REFINE") != "1"
    bio_given = bio_given or {}
    off_name = off_name or {}
    by_stint: dict[str, list[tuple[StintMatch, int]]] = defaultdict(list)
    by_bio_colony: dict[tuple[str, str], list[tuple[StintMatch, int]]] = defaultdict(list)
    for m, s in candidates:
        by_stint[m.official_id].append((m, s))
        # colony is recoverable from the official id suffix-free form; use id's
        # middle segment (id = name___colony___first_year)
        colony = m.official_id.split("___")[1] if "___" in m.official_id else ""
        by_bio_colony[(m.bio_id, colony)].append((m, s))

    dropped: set[int] = set()

    for group in by_stint.values():
        if len(group) < 2:
            continue
        # exact-surname matches categorically outrank fuzzy-surname ones
        if any(not m.fuzzy_surname for m, _ in group):
            for m, _ in group:
                if m.fuzzy_surname:
                    dropped.add(id(m))
            group = [t for t in group if not t[0].fuzzy_surname]
            if len(group) < 2:
                continue
        # duplicate-fragment contest: all contesting bios are one person AND
        # each matches the stint's official name tightly (not an initial-
        # deficient subsequence) -> keep every link (the career is correctly
        # attached however many bio fragments represent the person). Tightness
        # is required because `_align` accepts loose subsequence name matches
        # that this guard would otherwise (correctly) suppress.
        on = off_name.get(group[0][0].official_id, "")
        if _refine and _all_same_person([m.bio_id for m, _ in group], bio_given) and \
                all(_tight_name_match(bio_given.get(m.bio_id, ""), on) for m, _ in group):
            continue
        group.sort(key=lambda t: t[1], reverse=True)
        best_s = group[0][1]
        if group[1][1] >= best_s - AMBIGUITY_MARGIN:
            for m, _ in group:          # no clear winner: drop them all
                dropped.add(id(m))
        else:
            for m, _ in group[1:]:
                dropped.add(id(m))

    # multiple stints of the same colony for one bio are fine ONLY if their
    # year ranges don't overlap (re-listings across editions); overlapping
    # same-colony stints are usually distinct same-name people -- unless the two
    # stints are the SAME official re-listed (honorific/initial variant), which
    # corroborates rather than contests
    for key, group in by_bio_colony.items():
        if len(group) < 2:
            continue
        # tight-beats-loose: when a bio matches a same-colony stint TIGHTLY
        # (initials equal / shared spelled forename), any same-colony stint it
        # matches only via a loose initial-deficient subsequence ("Edward" [E]
        # vs "H. E. S" [H,E,S]) is a namesake the loose `_align` name gate let
        # through -- drop it. A missed link is recoverable; this wrong one is
        # the classic de Kretser trap.
        if _refine:
            bg = bio_given.get(group[0][0].bio_id, "")
            tights = [_tight_name_match(bg, off_name.get(m.official_id, "")) for m, _ in group]
            if any(tights) and not all(tights):
                for (m, _), t in zip(group, tights):
                    if not t:
                        dropped.add(id(m))
                group = [g for g, t in zip(group, tights) if t]
                if len(group) < 2:
                    continue
        spans = []
        for m, s in group:
            try:
                fy = int(m.official_id.rsplit("___", 1)[1])
            except ValueError:
                fy = 0
            spans.append((fy, m, s))
        spans.sort(key=lambda t: t[0])
        for (fa, ma, sa), (fb, mb, sb) in zip(spans, spans[1:]):
            if fb <= fa + 3:                # overlapping/near starts: ambiguous
                # exact surname categorically outranks a fuzzy/truncation
                # surname (mirrors the by_stint rule): a weak fuzzy candidate
                # must not knock out a strong exact match for the same
                # bio+colony — drop only the fuzzy one, keep the exact.
                if ma.fuzzy_surname != mb.fuzzy_surname:
                    dropped.add(id(ma if ma.fuzzy_surname else mb))
                    continue
                if _refine and _same_official(ma.official_id, mb.official_id, off_name):
                    continue                # same person re-listed: corroboration
                if abs(sa - sb) < AMBIGUITY_MARGIN:
                    dropped.add(id(ma))
                    dropped.add(id(mb))

    kept = [m for m, _ in candidates if id(m) not in dropped]
    return kept, len(candidates) - len(kept)
