#!/usr/bin/env python3
"""Batch classifier for the unmatched-bio debugging loop.

Samples unmatched biographies (stratified across edition decades), replays the
real match gates against the current (augmented) target with the recovered-place
overlay applied, searches the raw OCR for the no-candidate cases, and assigns a
fine-grained FAILURE CLASS to each — aggregating the evidence needed to fix the
class (which roll-ups are missing, which position pairs fail, etc.).

Writes match_issues.html: a living log of every class with a status
(fixed / easy / medium / hard / llm) and concrete examples.

Usage:  python3 classify_unmatched.py --n 240 --seed 0
        COL_USE_AUGMENTED=1 python3 classify_unmatched.py   # use augmented target
"""
import argparse
import html
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein

from col_match.services import gazetteer
from col_match.services.candidates import _annotate
from col_match.services.compile import _names_compatible
from col_match.services.infer_colony import apply_recovered_places
from col_match.services.match import (POSITION_SIM, _initials, _norm,
                                       _surname_of_official)
from col_match.services.recover import (_given_of, _name_segment,
                                        _position_context, _read, _surname_hit)
from col_match.services.schema import Biography
from col_match.services.source_index import load_index

DD = Path("data/services")
SRC = Path("~/textasdatacolonialofficelist").expanduser()

# class -> (status, one-line description)
CLASS_INFO = {
    "ambiguity_drop":   ("medium", "PASS-BAR exact candidate(s) dropped by the ambiguity guard (competing same-name stints)"),
    "fuzzy_surname":    ("medium", "best candidate only matches on an OCR-fuzzy surname (e.g. Hornyey~Hornby)"),
    "colony_not_rolled":("easy",   "same-surname+initials record exists but bio place doesn't roll up to its colony"),
    "placeless_strong": ("medium", "strong-position events are place-less (Tier A didn't pin a colony); only a weak placed event compared"),
    "position_fuzz":    ("easy",   "colony+tenure agree but position similarity < bar (abbreviation/wording gap)"),
    "tenure_gap":       ("hard",   "same colony but stint years don't overlap the bio's tenure"),
    "multiname_blob":   ("llm",    "only candidate is a backfill multi-name grade-list blob (officers never split out)"),
    "extraction_gap":   ("llm",    "surname present in raw OCR (initials-compatible) but no graph record — never extracted"),
    "namesake_no_record":("hard",  "only same-surname record is a different person in another colony — this person was never extracted / not in service"),
    "no_record":        ("hard",   "surname absent from graph AND raw OCR — not in colonial service, or OCR-garbled name"),
    "duplicate":        ("medium", "an obvious duplicate biography exists (career split across bio fragments)"),
    "other":            ("hard",   "did not fit a class"),
}


def load_bios():
    return [Biography.model_validate_json(l)
            for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]


def load_officials():
    import os
    aug = DD / "graph_cache" / "officials_augmented.jsonl"
    p = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else DD / "graph_cache" / "officials.jsonl"
    return [json.loads(l) for l in p.open(encoding="utf-8")], p.name


def matched_ids():
    m = set()
    for fn in ("record_attachments", "stint_matches"):
        p = DD / "matches" / f"{fn}.jsonl"
        if p.exists():
            for l in p.open(encoding="utf-8"):
                if l.strip():
                    m.add(json.loads(l)["bio_id"])
    return m


def is_blob(name):
    return name.count(";") >= 3 or len(name) > 80


def classify(bio, by_surname, surname_keys, bio_counts, idx, ev):
    """Return (cls, detail) for one unmatched bio. `ev` collects aggregate evidence."""
    bsur = _norm(bio.surname)
    block = list(by_surname.get(bsur, []))
    fuzzy_block = []
    for k in surname_keys:
        if k != bsur and len(k) >= 5 and Levenshtein.distance(k, bsur, score_cutoff=2) <= 2:
            fuzzy_block.extend(by_surname[k])

    exact_c, fuzzy_c = [], []
    for o in block:
        c = _annotate(bio, o, False, str(DD), bio_counts, by_surname)
        if c:
            exact_c.append((o, c))
    for o in fuzzy_block:
        c = _annotate(bio, o, True, str(DD), bio_counts, by_surname)
        if c:
            fuzzy_c.append((o, c))

    # PASS-BAR exact candidate that didn't become a match -> ambiguity drop
    passed = [(o, c) for o, c in exact_c if c.phase1_passed_bar]
    if passed:
        return "ambiguity_drop", f"{len(passed)} pass-bar exact candidate(s); competing -> dropped"

    if exact_c:
        # pick the most-promising exact candidate (colony ok first, then best position)
        exact_c.sort(key=lambda t: (-sum(ch.passed for ch in t[1].checks), -t[1].best_position_score))
        o, c = exact_c[0]
        chk = {ch.name: ch for ch in c.checks}
        colony_ok = chk["colony"].passed
        tenure_ok = chk["tenure_overlap"].passed
        pos_ok = chk["position_sim"].passed
        if not colony_ok:
            # same-person signal despite colony-name mismatch? (a real roll-up
            # gap) vs just a different-colony namesake (no record for this person)
            corroborated = any(cc.cooc_years or cc.best_position_score >= POSITION_SIM
                               for _o, cc in exact_c)
            places = sorted({e.place for e in bio.events if e.place})
            if corroborated:
                ev["rollup"][(tuple(places[:3]), o["colony"])] += 1
                return "colony_not_rolled", f"places {places[:3]} vs record colony '{o['colony']}' (corroborated)"
            return "namesake_no_record", f"only same-surname record is a different person in '{o['colony']}'"
        if colony_ok and not pos_ok:
            # is a stronger-position event place-less?
            placeless_strong = any((not e.place) and e.position and len(e.position) > 4
                                   for e in bio.events)
            ev["posfuzz"][(c.best_position_score // 10 * 10)] += 1
            detail = next((ch.detail for ch in c.checks if ch.name == "position_sim"), "")
            if placeless_strong:
                return "placeless_strong", detail
            return "position_fuzz", detail
        if colony_ok and not tenure_ok:
            return "tenure_gap", chk["tenure_overlap"].detail
        return "other", "exact candidate passes colony+tenure+position but no match?"

    if fuzzy_c:
        o, c = fuzzy_c[0]
        if is_blob(o.get("name", "")):
            return "multiname_blob", o["id"][:60]
        return "fuzzy_surname", f"bio '{bio.surname}' ~ record '{o['name']}'"

    # no same-surname official: search raw OCR
    years = set(bio.editions or [])
    for e in bio.events:
        if e.year_start:
            years.add(e.year_start)
    found_colony = None
    for y in sorted(years):
        for _k, path in idx.by_year.get(y, ()):
            text, lines = _read(str(path))
            if not _surname_hit(text, bsur):
                continue
            for line in lines:
                if not _surname_hit(line, bsur):
                    continue
                seg = _name_segment(line, bsur)
                if seg and _names_compatible(bio.given_names, _given_of(seg, bsur)):
                    found_colony = path.stem
                    break
            if found_colony:
                break
        if found_colony:
            break
    if found_colony:
        ev["extraction_gap_colony"][found_colony] += 1
        return "extraction_gap", f"surname in OCR: {found_colony}"
    return "no_record", "surname absent from graph and OCR (these years)"


def dup_exists(bio, by_bio_surname, matched):
    bsur = _norm(bio.surname)
    for b in by_bio_surname.get(bsur, ()):
        if b.bio_id != bio.bio_id and _names_compatible(bio.given_names, b.given_names):
            return b.bio_id
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=240)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    bios = load_bios()
    apply_recovered_places(bios, str(DD))
    officials, src = load_officials()
    matched = matched_ids()

    by_surname = defaultdict(list)
    for o in officials:
        by_surname[_surname_of_official(o["name"])].append(o)
    surname_keys = list(by_surname)
    bio_counts = defaultdict(int)
    by_bio_surname = defaultdict(list)
    for b in bios:
        bio_counts[_norm(b.surname)] += 1
        by_bio_surname[_norm(b.surname)].append(b)

    unmatched = [b for b in bios if b.bio_id not in matched
                 and any(e.year_start and e.place for e in b.events)]
    # stratify by decade
    by_dec = defaultdict(list)
    for b in unmatched:
        by_dec[(min(b.editions) // 10 * 10) if b.editions else 0].append(b)
    rng = random.Random(args.seed)
    for v in by_dec.values():
        rng.shuffle(v)
    sample, decades = [], sorted(by_dec)
    while len(sample) < args.n and any(by_dec[d] for d in decades):
        for d in decades:
            if by_dec[d]:
                sample.append(by_dec[d].pop())
            if len(sample) >= args.n:
                break
    idx = load_index(str(SRC))

    ev = {"rollup": Counter(), "posfuzz": Counter(), "extraction_gap_colony": Counter()}
    counts = Counter()
    examples = defaultdict(list)
    dup_count = 0
    for b in sample:
        cls, detail = classify(b, by_surname, surname_keys, bio_counts, idx, ev)
        counts[cls] += 1
        if dup_exists(b, by_bio_surname, matched):
            dup_count += 1
        if len(examples[cls]) < 12:
            examples[cls].append((b, detail))

    write_html(len(unmatched), len(sample), counts, examples, ev, dup_count, src)
    print(f"unmatched(placed)={len(unmatched)}  sampled={len(sample)}  target={src}")
    for cls, n in counts.most_common():
        st = CLASS_INFO.get(cls, ("?", ""))[0]
        print(f"  {n:4d} ({n*100//len(sample):2d}%) [{st:6s}] {cls}")
    print(f"  (duplicate bio present in {dup_count} of {len(sample)} sampled)")
    print("wrote match_issues.html")


def write_html(n_unmatched, n_sample, counts, examples, ev, dup_count, src):
    def esc(s):
        return html.escape(str(s))
    rows = []
    for cls, n in counts.most_common():
        st, desc = CLASS_INFO.get(cls, ("?", ""))
        rows.append(f"<tr><td>{esc(cls)}</td><td class=s-{st}>{st}</td>"
                    f"<td style='text-align:right'>{n}</td>"
                    f"<td style='text-align:right'>{n*100//n_sample}%</td><td>{esc(desc)}</td></tr>")
    secs = []
    for cls, n in counts.most_common():
        st, desc = CLASS_INFO.get(cls, ("?", ""))
        items = "".join(
            f"<li><b>{esc(b.surname)}, {esc(b.given_names)}</b> "
            f"<code>{esc(b.bio_id)}</code> ed={esc(b.editions)}<br>"
            f"<span class=d>{esc(det)}</span></li>"
            for b, det in examples.get(cls, []))
        secs.append(f"<h3>{esc(cls)} <span class=s-{st}>[{st}]</span> "
                    f"&middot; {n} ({n*100//n_sample}%)</h3><p>{esc(desc)}</p><ul>{items}</ul>")
    # aggregated fix evidence
    roll = "".join(f"<tr><td>{esc(p)}</td><td>{esc(c)}</td><td style='text-align:right'>{n}</td></tr>"
                   for (p, c), n in ev["rollup"].most_common(25))
    egc = "".join(f"<tr><td>{esc(c)}</td><td style='text-align:right'>{n}</td></tr>"
                  for c, n in ev["extraction_gap_colony"].most_common(20))
    doc = f"""<!doctype html><meta charset=utf-8><title>COL match issues</title>
<style>
body{{font:14px/1.5 system-ui,sans-serif;max-width:1000px;margin:2em auto;padding:0 1em;color:#222}}
table{{border-collapse:collapse;width:100%;margin:1em 0}} td,th{{border:1px solid #ddd;padding:4px 8px}}
th{{background:#f4f4f4;text-align:left}} code{{background:#f0f0f0;padding:0 3px;font-size:12px}}
.d{{color:#666;font-size:12px}} h3{{margin-top:1.6em}}
.s-easy{{color:#127a12;font-weight:600}} .s-medium{{color:#b8860b;font-weight:600}}
.s-hard{{color:#b00;font-weight:600}} .s-llm{{color:#8000a0;font-weight:600}} .s-fixed{{color:#888}}
</style>
<h1>COL biography &rarr; record: unmatched-issue log</h1>
<p>Match target: <code>{esc(src)}</code>. Unmatched (with a placed dated event):
<b>{n_unmatched:,}</b>. Sampled this run: <b>{n_sample}</b> (stratified by edition decade).
Status legend: <span class=s-easy>easy</span> (local 0-FP fix) &middot;
<span class=s-medium>medium</span> (tuning/dedup, some risk) &middot;
<span class=s-hard>hard</span> (genuine tail) &middot; <span class=s-llm>llm</span> (needs metered re-extraction).
A duplicate bio was present in {dup_count}/{n_sample} sampled.</p>
<h2>Class distribution</h2>
<table><tr><th>class</th><th>status</th><th>n</th><th>%</th><th>description</th></tr>{''.join(rows)}</table>
<h2>Candidate easy fixes &mdash; missing roll-ups (bio places &rarr; record colony)</h2>
<table><tr><th>bio places</th><th>record colony (no roll-up)</th><th>n</th></tr>{roll}</table>
<h2>Extraction-gap colonies (surname in OCR, no record)</h2>
<table><tr><th>colony file</th><th>n</th></tr>{egc}</table>
<h2>Examples by class</h2>
{''.join(secs)}
"""
    Path("match_issues.html").write_text(doc, encoding="utf-8")


if __name__ == "__main__":
    main()
