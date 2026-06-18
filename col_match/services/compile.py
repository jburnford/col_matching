"""Compile ParsedEntries (one per entry-version) into per-person Biographies
with per-fact edition provenance and OCR year-voting.

Most people have one version (their entry chain). Multiple versions arise
from the 1948 reformat or OCR drift breaking a chain; merging across versions
is conservative: compatible given names AND compatible birth years AND >=2
overlapping career events. Ambiguity -> separate biographies (a missed merge
is recoverable; a wrong one is not).

Year voting: each version's attesting editions reprint the same entry, giving
independent OCR readings. A parsed year that appears in fewer than half of
the attestation texts is flagged year_minority (never silently corrected).
"""

from __future__ import annotations

import os
import re
from collections import defaultdict

from rapidfuzz import fuzz

from .schema import (
    BioEvent,
    Biography,
    EntryVersion,
    Honour,
    ParsedEntry,
    ProvenancedYear,
    RawEntry,
)

_NORM = re.compile(r"[^a-z0-9 ]")

# era abbreviation drift: 1883 prints "temporary clerk", 1930 "temp. clk." —
# token-level expansion so position comparison sees through it
_POS_ABBREV = {
    "clk": "clerk", "clks": "clerks", "sec": "secretary", "secy": "secretary",
    "asst": "assistant", "ast": "assistant", "dir": "director",
    "gov": "governor", "govt": "government", "offr": "officer",
    "mag": "magistrate", "comsnr": "commissioner", "commnr": "commissioner",
    "comsr": "commissioner", "commr": "commissioner", "dist": "district",
    "survr": "surveyor", "treas": "treasurer", "educ": "education",
    "agric": "agriculture", "insp": "inspector", "inspr": "inspector",
    "supt": "superintendent", "dep": "deputy", "regr": "registrar",
    "registr": "registrar", "acctnt": "accountant", "accnt": "accountant",
    "engr": "engineer", "engnr": "engineer", "prin": "principal",
    "med": "medical", "snr": "senior", "senr": "senior", "jun": "junior",
    "junr": "junior", "gen": "general", "agt": "agent", "cls": "class",
    "cl": "class", "temp": "temporary", "actg": "acting", "ag": "acting",
    "stip": "stipendiary", "col": "colonial", "exec": "executive",
    "leg": "legislative", "coun": "council", "mem": "member",
    "pres": "president", "ch": "chief", "just": "justice",
}


# Victorian forename abbreviations (period dropped by OCR/_norm). Only
# unambiguous expansions — "Ed."/"Will."/"Bert." are deliberately omitted.
# Used so "Edwd Geo" and "Edward George" are recognized as the same person
# (the Broadrick split) and so abbreviated forenames yield real initials.
_FORENAME_ABBREV = {
    "geo": "george", "jas": "james", "jno": "john", "wm": "william",
    "chas": "charles", "thos": "thomas", "robt": "robert", "richd": "richard",
    "edwd": "edward", "edw": "edward", "fredk": "frederick", "fred": "frederick",
    "hy": "henry", "hen": "henry", "jos": "joseph", "danl": "daniel",
    "saml": "samuel", "benjn": "benjamin", "benj": "benjamin",
    "alexr": "alexander", "archd": "archibald", "herbt": "herbert",
    "matt": "matthew", "nichs": "nicholas", "walt": "walter",
    "augs": "augustus", "cuthbt": "cuthbert", "fras": "francis",
    "geoff": "geoffrey", "gilbt": "gilbert", "leon": "leonard",
    "reg": "reginald", "chris": "christopher", "montr": "montagu",
}


def _norm(s: str | None) -> str:
    return _NORM.sub("", (s or "").lower()).strip()


def _canon_token(t: str) -> str:
    """Normalized forename token, abbreviations expanded ("edwd"->"edward")."""
    n = _norm(t)
    return _FORENAME_ABBREV.get(n, n)


def _pos_norm(s: str | None) -> str:
    # hyphens/slashes are word separators in titles ("surveyor-general",
    # "vice-principal", "asst.-supt."); _norm deletes them and fuses the words,
    # hiding both the tokens and their abbreviation expansions. Split first.
    spaced = re.sub(r"[-/]", " ", s or "")
    return " ".join(_POS_ABBREV.get(t, t) for t in _norm(spaced).split())


def _initials(given: str | None) -> list[str]:
    return [t[0].upper() for t in re.split(r"[ .]+", given or "") if t and t[0].isalpha()]


def _names_compatible(a: str | None, b: str | None) -> bool:
    """Initials match full names; contradictory full names never merge."""
    ta = [t for t in re.split(r"[ .]+", a or "") if t]
    tb = [t for t in re.split(r"[ .]+", b or "") if t]
    if not ta or not tb:
        return True
    for x, y in zip(ta, tb):
        if len(x) == 1 or len(y) == 1:
            if x[0].upper() != y[0].upper():
                return False
        elif _canon_token(x) != _canon_token(y):
            return False
    return True


def _token_match(x: str, y: str) -> bool:
    if len(x) == 1 or len(y) == 1:
        return x[0].upper() == y[0].upper()
    return _canon_token(x) == _canon_token(y)


def _token_match_ocr(x: str, y: str) -> bool:
    """As _token_match but full tokens tolerate one OCR character
    ("Lachlan"/"Lauchlan"). Only for paths with external physical evidence."""
    if len(x) == 1 or len(y) == 1:
        return x[0].upper() == y[0].upper()
    from rapidfuzz.distance import Levenshtein

    cx, cy = _canon_token(x), _canon_token(y)
    return cx == cy or Levenshtein.distance(cx, cy, score_cutoff=1) <= 1


def _names_ocr_compatible(a: str | None, b: str | None) -> bool:
    ta = [t for t in re.split(r"[ .]+", a or "") if t]
    tb = [t for t in re.split(r"[ .]+", b or "") if t]
    if not ta or not tb:
        return True
    short, long_ = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    i = 0
    for tok in long_:
        if i < len(short) and _token_match_ocr(short[i], tok):
            i += 1
    return i == len(short)


def _names_subseq_compatible(a: str | None, b: str | None) -> bool:
    """Like _names_compatible but tolerant of dropped forenames: the shorter
    name's tokens must appear, in order, within the longer's ("Miles" within
    "Geoffrey Miles"). Used only when birth years independently agree."""
    ta = [t for t in re.split(r"[ .]+", a or "") if t]
    tb = [t for t in re.split(r"[ .]+", b or "") if t]
    if not ta or not tb:
        return True
    short, long_ = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    i = 0
    for tok in long_:
        if i < len(short) and _token_match(short[i], tok):
            i += 1
    return i == len(short)


def _events_overlap(p: ParsedEntry, q: ParsedEntry) -> int:
    n = 0
    for ea in p.events:
        if ea.year_start is None:
            continue
        for eb in q.events:
            if eb.year_start is None or abs(ea.year_start - eb.year_start) > 1:
                continue
            if ea.place and eb.place and _norm(ea.place) == _norm(eb.place):
                n += 1
                break
            if fuzz.token_set_ratio(_pos_norm(ea.position), _pos_norm(eb.position)) >= 80:
                n += 1
                break
    return n


def _education_sim(p: ParsedEntry, q: ParsedEntry) -> float:
    """Similarity of the printed education clauses (near-unique per person
    when long enough)."""
    a, b = _norm(p.education), _norm(q.education)
    if len(a) < 12 or len(b) < 12:
        return 0.0
    return fuzz.token_set_ratio(a, b)


def _shared_honour_year(p: ParsedEntry, q: ParsedEntry) -> bool:
    """The same decoration awarded in the same year is near-unique within a
    surname."""
    a = {(_norm(h.award), h.year) for h in p.honours if h.year}
    b = {(_norm(h.award), h.year) for h in q.honours if h.year}
    return bool(a & b)


def _full_name_equal(p: ParsedEntry, q: ParsedEntry) -> bool:
    """Both entries spell out a multi-token given name and the token sequences
    are equal (OCR-tolerant, one edit per token). A matching full forename
    string ("Edward Blackwell", "Michael Francis Joseph") is near-unique within
    a surname — far stronger than a shared first forename, and a father/son
    would have to share every middle name AND a year-aligned career event."""
    ta = [_canon_token(t) for t in re.split(r"[ .]+", p.given_names or "") if len(_canon_token(t)) > 2]
    tb = [_canon_token(t) for t in re.split(r"[ .]+", q.given_names or "") if len(_canon_token(t)) > 2]
    if len(ta) < 2 or len(ta) != len(tb):
        return False
    from rapidfuzz.distance import Levenshtein
    return all(x == y or Levenshtein.distance(x, y, score_cutoff=1) <= 1
               for x, y in zip(ta, tb))


def _shared_terminal_year(p: ParsedEntry, q: ParsedEntry) -> bool:
    """Same death/retirement year — near-unique within a surname."""
    return bool(p.terminal and q.terminal and p.terminal.year and q.terminal.year
                and p.terminal.year == q.terminal.year)


def _one_digit_year(y1: int, y2: int) -> bool:
    """The two 4-digit years differ in exactly one position — the signature of
    an OCR digit confusion (1834/1884, 1879/1889), i.e. almost certainly the
    SAME person's birth year misread, not a real generational difference."""
    s1, s2 = str(y1), str(y2)
    return len(s1) == len(s2) == 4 and sum(a != b for a, b in zip(s1, s2)) == 1


def _dated_events(p: ParsedEntry) -> list:
    return [e for e in p.events if e.year_start is not None]


def _early_window_overlap(p: ParsedEntry, q: ParsedEntry) -> int:
    """Count career events that AGREE (year +/-1, same place or position
    token_set>=80) within the EARLY half of the longer entry's career.

    Duplicate fragments of one person share the early, stable career; later
    clauses accumulate and diverge (one fragment stops earlier). Scoring the
    longer form's first half against the other isolates that shared identity
    core (Jim's framing: first quarter/half of the longest form)."""
    da, db = _dated_events(p), _dated_events(q)
    if not da or not db:
        return 0
    longer, other = (p, q) if len(da) >= len(db) else (q, p)
    dl = _dated_events(longer)
    yrs = [e.year_start for e in dl]
    lo, hi = min(yrs), max(yrs)
    cut = lo + max(1, round((hi - lo) * 0.5))
    early = [e for e in dl if e.year_start <= cut]
    n = 0
    for ea in early:
        for eb in _dated_events(other):
            if abs(ea.year_start - eb.year_start) > 1:
                continue
            if ea.place and eb.place and _norm(ea.place) == _norm(eb.place):
                n += 1
                break
            if ea.position and eb.position and \
                    fuzz.token_set_ratio(_pos_norm(ea.position), _pos_norm(eb.position)) >= 80:
                n += 1
                break
    return n


def _early_career_same_person(p: ParsedEntry, q: ParsedEntry) -> bool:
    """Birth-year-tolerant same-person test for duplicate fragments whose
    surname block or birth year kept them apart. Several independent acceptance
    paths, each a strong same-person signal (calibrated against birth-year
    ground truth — see measure_dedup_signal.py / measure_dedup_tail.py):

      1. >=2 early-career event agreements AND near-identical education
         (education is near-unique; early events alone are too generic);
      2. an exact multi-token full forename AND a year-aligned event;
      3. a shared honour-year AND a year-aligned event;
      4. a shared death/retirement year AND a year-aligned event.

    Paths 2-4 reach the tail with thin careers / no education. A year-aligned
    shared event is the father/son guard on those paths (two generations can't
    hold the same post in the same year). Birth year is treated as OCR-noisy,
    not a hard block: a LARGE, non-one-digit gap (a possible father/son) still
    demands a second corroborator beyond a single event."""
    em = _early_window_overlap(p, q)
    hy = _shared_honour_year(p, q)
    ty = _shared_terminal_year(p, q)
    ok = ((em >= 2 and _education_sim(p, q) >= 85)
          or (em >= 1 and _full_name_equal(p, q))
          or (em >= 1 and hy)
          or (em >= 1 and ty))
    if not ok:
        return False
    if p.birth_year and q.birth_year:
        gap = abs(p.birth_year - q.birth_year)
        if gap > 2 and not _one_digit_year(p.birth_year, q.birth_year):
            return em >= 2 or hy or ty
    return True


def _should_merge(p: ParsedEntry, q: ParsedEntry) -> bool:
    """Conservative same-person test (names already compatible, birth years
    already non-contradictory). Each path needs two independent anchors."""
    overlap = _events_overlap(p, q)
    if overlap >= 2:
        return True
    same_birth = bool(p.birth_year and q.birth_year and p.birth_year == q.birth_year)
    if overlap >= 1 and (same_birth or _shared_honour_year(p, q)
                         or _education_sim(p, q) >= 85):
        return True
    if same_birth and _education_sim(p, q) >= 85:
        return True
    return False


def _vote_years(parsed: ParsedEntry, version: EntryVersion,
                texts_by_entry: dict[str, str]) -> None:
    texts = [texts_by_entry[eid] for eid in version.entry_ids if eid in texts_by_entry]
    if len(texts) < 3:
        return
    half = len(texts) / 2
    for i, ev in enumerate(parsed.events):
        for y in (ev.year_start, ev.year_end):
            if y is None:
                continue
            support = sum(1 for t in texts if str(y) in t)
            if support < half:
                parsed.flags.append(f"year_minority:{i}:{y}:{support}/{len(texts)}")


def recover_places_from_positions(parsed_entries: list[ParsedEntry],
                                  data_dir: str) -> int:
    """Split a place the parser left inside the position string back out into
    the place field. The services sections often print "<post>, <place>" where
    <place> is an abbreviated/dotted colony ("asst. res., N. Nigeria") the
    clause parser's tail lookup missed; the gazetteer now knows these forms, so
    recover them here — benefiting both parser tiers without re-parsing. Only
    an exact gazetteer hit on the tail is acted on (conservative). Returns the
    number of events fixed."""
    from . import gazetteer

    n = 0
    for p in parsed_entries:
        for ev in p.events:
            if ev.place or not ev.position or "," not in ev.position:
                continue
            head, tail = ev.position.rsplit(",", 1)
            hit = gazetteer.lookup(tail.strip(), data_dir)
            if hit and head.strip():
                ev.place = hit
                ev.position = head.strip()
                n += 1
    return n


def recover_places_from_prose(parsed_entries: list[ParsedEntry],
                              data_dir: str) -> int:
    """Attach a colony that the entry PROSE states mid-clause but the parser
    missed. `rules_parse` resolves a place only from a clause's LAST comma
    segment (or its prefix); a colony in an EARLIER segment ("puisne judge,
    Uganda, and mem. ct. of appeal, 1934") is dropped, leaving the event
    place-less or wrongly inheriting the previous clause's place. Here, for a
    dated event with no confidently-printed place, scan the non-last comma
    segments of its text span for a gazetteer-resolvable colony and, when one
    is found that differs from the current place, attach it as printed-quality.

    Conservative by construction: only an exact gazetteer hit (or segment-prefix
    hit) on a whole comma segment is acted on, and the downstream matcher still
    independently re-gates colony+tenure+position+ambiguity on the result, so a
    mis-attached colony cannot force a match the other gates reject. Returns the
    number of events fixed."""
    from . import gazetteer

    n = 0
    for p in parsed_entries:
        for ev in p.events:
            if ev.year_start is None:
                continue
            if ev.place and not ev.place_inherited:
                continue  # already a confidently-printed place
            segs = [s.strip(" ,.") for s in (ev.text_span or "").split(",")
                    if s.strip(" ,.")]
            if len(segs) < 2:
                continue
            hit = None
            for seg in segs[:-1]:  # the parser already tried the last segment
                hit = gazetteer.lookup(seg, data_dir) or gazetteer.lookup_prefix(seg, data_dir)
                if hit:
                    break
            if not hit:
                continue
            if ev.place and gazetteer.norm(ev.place) == gazetteer.norm(hit):
                continue  # same colony it already inherited — nothing to fix
            ev.place = hit
            ev.place_inherited = False
            n += 1
    return n


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def compile_biographies(
    parsed_entries: list[ParsedEntry],
    versions: dict[str, EntryVersion],
    raw_texts: dict[str, str],
    record_merge_pairs: list[dict] | None = None,
    llm_merge_groups: list[list[str]] | None = None,
) -> tuple[list[Biography], dict]:
    # 1. year voting per version
    for p in parsed_entries:
        v = versions.get(p.version_id)
        if v is not None:
            _vote_years(p, v, raw_texts)

    # 2. global union-find; two blocking passes feed the same parent map.
    index = {id(p): k for k, p in enumerate(parsed_entries)}
    parent = list(range(len(parsed_entries)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    merged_pairs = 0

    def consider(p: ParsedEntry, q: ParsedEntry, name_test, *, strict: bool = False) -> None:
        nonlocal merged_pairs
        if not name_test(p.given_names, q.given_names):
            return
        if p.birth_year and q.birth_year and p.birth_year != q.birth_year:
            return
        if strict:
            # surnames differ (OCR variants): birth year is the blocking key
            # so it cannot double as a merge anchor — demand career evidence
            ok = (_events_overlap(p, q) >= 2
                  or (_events_overlap(p, q) >= 1
                      and (_education_sim(p, q) >= 85 or _shared_honour_year(p, q))))
        else:
            ok = _should_merge(p, q)
        if ok:
            ri, rj = find(index[id(p)]), find(index[id(q)])
            if ri != rj:
                parent[ri] = rj
                merged_pairs += 1

    # pass A: surname + first initial (the common case)
    blocks: dict[str, list[ParsedEntry]] = defaultdict(list)
    for p in parsed_entries:
        ini = _initials(p.given_names)
        blocks[f"{_norm(p.surname)}|{ini[0] if ini else '?'}"].append(p)
    for members in blocks.values():
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                consider(members[i], members[j], _names_compatible)

    # pass B: surname + birth year — catches dropped forenames ("Geoffrey
    # Miles Clifford" later printed "Miles Clifford"); birth-year equality is
    # the anchor, name order-subsequence the guard
    by_birth: dict[str, list[ParsedEntry]] = defaultdict(list)
    for p in parsed_entries:
        if p.birth_year:
            by_birth[f"{_norm(p.surname)}|{p.birth_year}"].append(p)
    for members in by_birth.values():
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                consider(members[i], members[j], _names_subseq_compatible)

    # pass C: birth year alone, OCR-tolerant surname ("Macgregor" vs OCR
    # "Macregor" sit in different surname blocks) — edit distance <=2 on
    # surnames of usable length, everything else as pass B
    from rapidfuzz.distance import Levenshtein

    by_year: dict[int, list[ParsedEntry]] = defaultdict(list)
    for p in parsed_entries:
        if p.birth_year and len(_norm(p.surname)) >= 5:
            by_year[p.birth_year].append(p)
    for members in by_year.values():
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                a, b = _norm(members[i].surname), _norm(members[j].surname)
                max_d = 1 if min(len(a), len(b)) < 8 else 2
                if a != b and Levenshtein.distance(a, b, score_cutoff=max_d) <= max_d:
                    consider(members[i], members[j], _names_subseq_compatible, strict=True)

    # pass D: record co-claims from a previous attach run — two biographies
    # that matched the SAME printed record-line are one person (subject to
    # OCR-tolerant name compatibility and birth non-contradiction; the shared
    # physical record is the second anchor)
    record_merges = 0
    if record_merge_pairs:
        by_version = {}
        for k, p in enumerate(parsed_entries):
            by_version[p.version_id] = k
        for pair in record_merge_pairs:
            ka, kb = by_version.get(pair["version_a"]), by_version.get(pair["version_b"])
            if ka is None or kb is None:
                continue
            p, q = parsed_entries[ka], parsed_entries[kb]
            if not _names_ocr_compatible(p.given_names, q.given_names):
                continue
            if p.birth_year and q.birth_year and p.birth_year != q.birth_year:
                continue
            ra, rb = find(ka), find(kb)
            if ra != rb:
                parent[ra] = rb
                record_merges += 1

    # pass E: early-career identity merge (birth-year-tolerant). Catches the
    # duplicate fragments that ALL prior passes miss — a garbled/truncated
    # surname (different surname block) or an OCR-noisy/absent birth year keeps
    # them apart. Block by (spelled forename token + surname SUFFIX): a dropped
    # headword prefix (Griffiths->FFITHS) preserves the suffix, and a shared
    # spelled forename is the same-person signal the ambiguity guard trusts.
    # Merge only on `_early_career_same_person` (>=2 early-career agreements +
    # near-identical education). Env COL_NO_DEDUP_EARLY=1 reverts.
    early_merges = 0
    if os.environ.get("COL_NO_DEDUP_EARLY") != "1":
        from rapidfuzz.distance import Levenshtein as _Lev

        eblocks: dict[tuple[str, str], list[ParsedEntry]] = defaultdict(list)
        for p in parsed_entries:
            sur = _norm(p.surname)
            if len(sur) < 5:
                continue
            suffix = sur[-4:]
            seen_tokens = set()
            for tok in re.split(r"[ .]+", p.given_names or ""):
                t = _canon_token(tok)
                if len(t) > 2 and t not in seen_tokens:
                    seen_tokens.add(t)
                    eblocks[(t, suffix)].append(p)
        for members in eblocks.values():
            if len(members) < 2 or len(members) > 400:
                continue
            for i in range(len(members)):
                for j in range(i + 1, len(members)):
                    a, b = members[i], members[j]
                    if find(index[id(a)]) == find(index[id(b)]):
                        continue
                    if not _names_ocr_compatible(a.given_names, b.given_names):
                        continue
                    sa, sb = _norm(a.surname), _norm(b.surname)
                    # surname relation: exact / OCR dist<=2 / truncation-suffix
                    rel = (sa == sb
                           or _Lev.distance(sa, sb, score_cutoff=2) <= 2
                           or (len(min(sa, sb, key=len)) >= 5
                               and max(sa, sb, key=len).endswith(min(sa, sb, key=len))
                               and 1 <= abs(len(sa) - len(sb)) <= 3))
                    if not rel:
                        continue
                    if _early_career_same_person(a, b):
                        ri, rj = find(index[id(a)]), find(index[id(b)])
                        if ri != rj:
                            parent[ri] = rj
                            early_merges += 1

    # pass F: human/LLM-adjudicated merges (data/services/dedup/llm_merges.jsonl).
    # Each group is a set of version_ids an adjudicator confirmed are ONE person
    # after reading full career + education + birth (OCR-tolerant). Authoritative
    # — unioned directly; eval_known still gates the result. Used for the
    # ambiguous tail that no deterministic signal can safely merge.
    # COL_NO_LLM_DEDUP=1 reverts.
    llm_merges = 0
    if llm_merge_groups and os.environ.get("COL_NO_LLM_DEDUP") != "1":
        vindex = {p.version_id: k for k, p in enumerate(parsed_entries)}
        for group in llm_merge_groups:
            ks = [vindex[v] for v in group if v in vindex]
            for k in ks[1:]:
                ra, rb = find(ks[0]), find(k)
                if ra != rb:
                    parent[ra] = rb
                    llm_merges += 1

    groups: dict[int, list[ParsedEntry]] = defaultdict(list)
    for k, p in enumerate(parsed_entries):
        groups[find(k)].append(p)
    bios = [_compose(group, versions) for group in groups.values()]

    # bio_id slugs can collide: same surname+givens and same birth (or first
    # event) year across DISTINCT un-merged groups. bio_id is the join key
    # for every downstream artifact, so a collision silently conflates two
    # people — the exact failure this pipeline exists to prevent. De-collide
    # deterministically: keep the earliest-attested bio's slug, suffix the
    # rest -2, -3, ... ordered by lead version_id.
    by_slug: dict[str, list[Biography]] = defaultdict(list)
    for b in bios:
        by_slug[b.bio_id].append(b)
    slug_collisions = 0
    for slug, same in by_slug.items():
        if len(same) < 2:
            continue
        slug_collisions += len(same) - 1
        same.sort(key=lambda b: min(b.version_ids))
        for k, b in enumerate(same[1:], start=2):
            b.bio_id = f"{slug}-{k}"

    stats = {
        "parsed_entries": len(parsed_entries),
        "biographies": len(bios),
        "cross_version_merges": merged_pairs,
        "record_coclaim_merges": record_merges,
        "early_career_merges": early_merges,
        "llm_dedup_merges": llm_merges,
        "bio_id_collisions_suffixed": slug_collisions,
        "with_birth_year": sum(1 for b in bios if b.birth_year),
        "flagged": sum(1 for b in bios if b.flags),
    }
    return bios, stats


def _compose(group: list[ParsedEntry], versions: dict[str, EntryVersion]) -> Biography:
    group = sorted(group, key=lambda p: len(p.events), reverse=True)
    lead = group[0]
    editions_of = {
        p.version_id: (versions[p.version_id].attesting_editions
                       if p.version_id in versions else [])
        for p in group
    }
    all_editions = sorted({e for eds in editions_of.values() for e in eds})

    # given names: fullest variant wins
    given = max((p.given_names or "" for p in group), key=len) or None

    birth = None
    for p in group:
        if p.birth_year is not None:
            birth = ProvenancedYear(value=p.birth_year, editions=editions_of[p.version_id])
            break

    # merge events across versions: same year + similar position = same event
    events: list[BioEvent] = []
    for p in group:
        for ev in p.events:
            placed = None
            for be in events:
                if be.year_start == ev.year_start and (
                    (_norm(be.place) == _norm(ev.place) and be.place)
                    or fuzz.token_set_ratio(_norm(be.position), _norm(ev.position)) >= 75
                ):
                    placed = be
                    break
            if placed is None:
                events.append(BioEvent(
                    position=ev.position, place=ev.place,
                    year_start=ev.year_start, year_end=ev.year_end,
                    editions=list(editions_of[p.version_id]),
                    place_inherited=ev.place_inherited,
                ))
            else:
                placed.editions = sorted(set(placed.editions) | set(editions_of[p.version_id]))
                if ev.place and not placed.place:
                    placed.place = ev.place
                    placed.place_inherited = ev.place_inherited
                elif ev.place and not ev.place_inherited and placed.place_inherited:
                    placed.place = ev.place
                    placed.place_inherited = False
    events.sort(key=lambda e: (e.year_start is None, e.year_start or 0))

    honours: dict[str, Honour] = {}
    for p in group:
        for h in p.honours:
            key = _norm(h.award)
            if key not in honours or (h.year and not honours[key].year):
                honours[key] = h

    terminal = next((p.terminal for p in group if p.terminal), None)
    flags = sorted({f for p in group for f in p.flags})
    # propagate place_inherited indices only from the lead (event order source)
    bio_id = f"{_slug(lead.surname)}_{_slug(given or 'x')}_" + (
        f"b{birth.value}" if birth else f"e{events[0].year_start if events else 0}"
    )
    return Biography(
        bio_id=bio_id, surname=lead.surname, given_names=given,
        birth_year=birth, version_ids=[p.version_id for p in group],
        editions=all_editions, honours=sorted(honours.values(), key=lambda h: h.award),
        events=events, terminal=terminal, flags=flags,
    )
