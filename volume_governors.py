#!/usr/bin/env python3
"""Extract gubernatorial succession lists from the Colonial Office Lists.

Pilot of the context-layer extraction (see volume_block_index.py): the
per-colony "Governors." / "Governors of X." sections print the full
historical succession of governors/administrators — cumulative, reprinted
every edition. Two printed forms, both handled:

  table:  <td>1612. Daniel Tucker.</td>            (year-name cells)
  text :  "Sir Robert W. Duff, P.C., G.C.M.G., 29th May, 1893. Lord ..."
          (run-on records terminated by a date)

The front-matter cross-colony snapshot tables ("COLONIAL GOVERNORS, &c.")
are a different animal (current-year panel with salaries) — skipped here.

Cross-edition dedup: lists are cumulative, so the same governorship appears
in dozens of editions; merged on (colony_canon, year, fuzzy surname), keeping
the latest edition's spelling and all source years.

Outputs data/volume/governors/{governors.jsonl, GOVERNORS.md}.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import distance

from col_match.services import rules_parse
from col_match.volume import reader
from volume_careers import canon_colony

ROOT = Path("data/volume")
OUT = ROOT / "governors"

# head-of-territory commissioner successions ("High Commissioners since
# 1878", "COMMISSIONERS", "List of Commissioners since 1893") sit under
# roster-shaped titles the block index classes as `establishment`, so they
# are admitted by TITLE; the prefix guard excludes District/Native/Land
# Commissioners (subordinate cadres, not heads of territory).
_COMMISSIONER_TITLE = re.compile(
    r"^(LIST OF (PRESIDENTS AND )?)?(HIGH )?COMMISSIONERS"
    r"( AND GOVERNORS)?( SINCE \d{4})?\s*\.?$", re.I)

_SNAPSHOT_TITLE = re.compile(
    r"COLONIAL GOVERNORS|DOMINION GOVERNORS"      # cross-colony snapshot panel
    r"|BOARD OF|^§|CLASSES OF GOVERNORS",         # school boards / regulations
    re.I)
_MONTH = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|"
          r"July?|Aug(?:ust)?|Sep(?:t|tember)?|Oct(?:ober)?|Nov(?:ember)?|"
          r"Dec(?:ember)?)\.?")
# record terminator: ", 21st November, 1895." / ", 1891." / ", 1883, and 13th December, 1886."
_DATE_TAIL = re.compile(
    rf"((?:\d{{1,2}}(?:st|nd|rd|th)?\s+{_MONTH},?\s+)?(1[6-9]\d\d))"
    rf"(?:[,;]?\s*(?:and|to)\s+(?:\d{{1,2}}(?:st|nd|rd|th)?\s+{_MONTH},?\s+)?(1[6-9]\d\d))?"
    r"\s*[.;]")
_CELL_ENTRY = re.compile(r"^(1[6-9]\d\d)\.?\s+(.+?)\.?$")
_TAG = re.compile(r"<[^>]+>")
_RANK = re.compile(
    r"^(?:The\s+)?(?:Rt\.?\s?Hon(?:ourable)?\.?|Right\s+Hon(?:ourable)?\.?|"
    r"His\s+Excellency|H\.E\.|Hon\.?|Sir|Lord|Earl(?:\s+of)?|Viscount|Baron|"
    r"Marquess(?:\s+of)?|Duke\s+of|Lady|Dame|Capt(?:ain)?\.?|Col(?:onel)?\.?|"
    r"Maj(?:or)?\.?(?:-Gen(?:eral)?\.?)?|Gen(?:eral)?\.?|Lieut\.?(?:-Col(?:onel)?\.?|"
    r"-Gen(?:eral)?\.?)?|Lt\.?(?:-Col\.?|-Gen\.?)?|Adm(?:iral)?\.?|Commodore|"
    r"Brig(?:adier)?\.?(?:-Gen\.?)?|Rev\.?|Dr\.?|Mr\.?|Esq\.?)\s+", re.I)
_OFFICE = re.compile(
    r"^(Lieut\.?-Gov(?:ernor)?\.?|Lt\.?-Gov\.?|Administrator|President|"
    r"Acting\s+Governor|Ag\.\s*Gov\.?|Officer\s+Administering|Commissioner|"
    r"High\s+Commissioner|Resident|Deputy\s+Governor|Gov(?:ernor)?\.?(?:-Gen(?:eral)?\.?)?)"
    r"\s*[,.:]?\s*", re.I)


_DOT_LEADER = re.compile(r"\s*(?:\.\s+){2,}|\.{3,}")
_TRAIL_OFFICE = re.compile(
    r"\s*[,;]?\s*(?:Acting\s*[-–]?\s*Governor|Administrator|Officer\s+Admin\w*"
    r"|Lieut\.?-Gov\w*)\b.*$"
    rf"|\s+(?:{_MONTH})\s*(?:to|[-–])\s*(?:{_MONTH}).*$", re.I)


def _parse_person(seg: str) -> tuple[str | None, str | None, str, list[str]] | None:
    """'Gen. Sir H. W. Norman, G.C.B., G.C.M.G.' ->
    (office, given, surname, honours); None if no name-shaped content."""
    # table cells glue dot-leaders + trailing office/month text onto the name
    # ("G. R. Le Hunte . . . Acting - Governor Aug. to Dec") — cut both
    seg = _DOT_LEADER.split(seg)[0]
    seg = _TRAIL_OFFICE.sub("", seg)
    seg = seg.strip(" ,;—–-")
    office = None
    m = _OFFICE.match(seg)
    if m and not _RANK.match(seg):
        office = m.group(1).rstrip(" ,.:")
        seg = seg[m.end():]
    # strip stacked rank prefixes
    while True:
        m = _RANK.match(seg)
        if not m:
            break
        seg = seg[m.end():]
    parts = [p.strip() for p in seg.split(",") if p.strip()]
    honours, name_parts = [], []
    for p in parts:
        p2 = p.rstrip(".")
        if rules_parse._DOTTED_CAPS.match(p2) or rules_parse._known_honour(p2):
            honours.append(p2)
        elif not honours and not name_parts:
            name_parts.append(p)
        elif not honours:
            name_parts.append(p)
        # after honours start, remaining segments are offices held ("Chief
        # Justice") — ignored for the succession record
    if not name_parts:
        return None
    name = name_parts[0].strip(" .")
    toks = name.split()
    if not toks or not re.match(r"^[A-Z]", toks[-1]):
        return None
    surname = toks[-1].strip(".,")
    given = " ".join(toks[:-1]).strip(" .,") or None
    if len(surname) < 2 or not re.match(r"^[A-Za-z'’\-]+$", surname):
        return None
    if surname.lower() in _NOT_SURNAME:
        return None
    return office, given, surname, honours


# words that survive parsing but are never governor surnames (ditto marks,
# stray table labels, ranks, months)
_NOT_SURNAME = {
    "gov", "governor", "general", "revenue", "capt", "captain", "confirmed",
    "sir", "ditto", "population", "vacant", "thos", "wm", "jas", "chas",
    "january", "february", "march", "april", "may", "june", "july", "august",
    "september", "october", "november", "december", "lieutenant-governor",
    "administrator", "acting", "office", "commission",
}


def parse_text_block(text: str) -> list[dict]:
    """Run-on succession prose -> records."""
    out = []
    pos = 0
    for m in _DATE_TAIL.finditer(text):
        seg = text[pos:m.start()].strip()
        pos = m.end()
        person = _parse_person(seg)
        if person is None:
            continue
        office, given, surname, honours = person
        out.append({"office": office, "given": given, "surname": surname,
                    "honours": honours, "year": int(m.group(2)),
                    "date": m.group(1).strip(", "),
                    "year2": int(m.group(3)) if m.group(3) else None})
    return out


_YEAR_LEAD = re.compile(r"\b(1[6-9]\d\d)(?:\s*[-–]\s*(1[6-9]\d\d))?\.?\s+(?=[A-Z])")


def parse_text_yearfirst(text: str) -> list[dict]:
    """Year-FIRST run-ons: '1897 Sir Alfred Moloney, K.C.M.G. 1900 Sir R. B.
    Llewelyn, K.C.M.G. ...' — the other common succession print format."""
    out = []
    marks = list(_YEAR_LEAD.finditer(text))
    for m, nxt in zip(marks, marks[1:] + [None]):
        seg = text[m.end(): nxt.start() if nxt else len(text)].strip(" .;")
        person = _parse_person(seg)
        if person is None:
            continue
        office, given, surname, honours = person
        out.append({"office": office, "given": given, "surname": surname,
                    "honours": honours, "year": int(m.group(1)),
                    "date": None,
                    "year2": int(m.group(2)) if m.group(2) else None})
    return out


def parse_table_block(text: str) -> list[dict]:
    """Year-name cell tables -> records."""
    out = []
    for cell in re.split(r"</t[dh]>", text):
        cell = _TAG.sub(" ", cell)
        cell = re.sub(r"\s+", " ", cell).strip()
        m = _CELL_ENTRY.match(cell)
        if not m:
            continue
        person = _parse_person(m.group(2))
        if person is None:
            continue
        office, given, surname, honours = person
        out.append({"office": office, "given": given, "surname": surname,
                    "honours": honours, "year": int(m.group(1)),
                    "date": None, "year2": None})
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    locs = defaultdict(list)                    # year -> [(page, block, ...)]
    for line in open(ROOT / "block_index.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if ((r["section"] == "governors_list"
             and not _SNAPSHOT_TITLE.search(r["title"]))
                or _COMMISSIONER_TITLE.match((r["title"] or "").strip())):
            locs[r["year"]].append(r)

    raw = []
    for year in sorted(locs):
        blocks = reader.load_volume(year, "col")
        bmap = {(b.page, b.index): b for b in blocks}
        for r in locs[year]:
            b = bmap.get((r["page"], r["block"]))
            if b is None:
                continue
            if r["category"] == "table":
                recs = parse_table_block(b.text)
            else:                     # try both prose formats, keep the richer
                a = parse_text_block(b.text)
                z = parse_text_yearfirst(b.text)
                recs = a if len(a) >= len(z) else z
            colony = canon_colony(r["colony"]) if r["colony"] else None
            if colony is None:
                continue
            for rec in recs:
                rec.update({"colony": colony, "edition": year,
                            "title": r["title"], "page": r["page"]})
                raw.append(rec)

    # ---------------------------- cross-edition dedup (lists are cumulative)
    merged: dict[tuple, dict] = {}
    for rec in sorted(raw, key=lambda r: r["edition"]):
        sur = rec["surname"].lower()
        key = None
        for cand in (sur,):
            k = (rec["colony"], rec["year"], cand, (rec["office"] or "").lower())
            if k in merged:
                key = k
                break
        if key is None:  # fuzzy surname (OCR wobble across editions)
            for (c, y, s, o), v in merged.items():
                if c == rec["colony"] and y == rec["year"] \
                        and o == (rec["office"] or "").lower() \
                        and abs(len(s) - len(sur)) <= 2 \
                        and distance.Levenshtein.distance(s, sur, score_cutoff=2) <= 2:
                    key = (c, y, s, o)
                    break
        if key is None:
            key = (rec["colony"], rec["year"], sur, (rec["office"] or "").lower())
            merged[key] = {**{k: rec[k] for k in
                              ("colony", "office", "given", "surname", "honours",
                               "year", "year2", "date")},
                           "editions": [rec["edition"]]}
        else:
            v = merged[key]
            v["editions"].append(rec["edition"])
            # latest edition wins on spelling/detail
            for f in ("given", "surname", "date", "year2", "office"):
                if rec.get(f):
                    v[f] = rec[f]
            v["honours"] = sorted(set(v["honours"]) | set(rec["honours"]))

    govs = sorted(merged.values(), key=lambda g: (g["colony"], g["year"]))
    with (OUT / "governors.jsonl").open("w", encoding="utf-8") as fh:
        for g in govs:
            g["n_editions"] = len(set(g.pop("editions")))
            fh.write(json.dumps(g, ensure_ascii=False) + "\n")

    # -------------------------------------------------------------- report
    by_colony = Counter(g["colony"] for g in govs)
    multi = sum(1 for g in govs if g["n_editions"] >= 2)
    lines = ["# Gubernatorial successions extracted", "",
             f"- raw records: {len(raw):,} -> {len(govs):,} distinct "
             f"governorships after cross-edition merge "
             f"({multi:,} attested in >=2 editions)",
             f"- colonies: {len(by_colony)}; year span "
             f"{min(g['year'] for g in govs)}–{max(g['year'] for g in govs)}",
             "", "## Colonies by governorship count", ""]
    for c, n in by_colony.most_common(20):
        yrs = [g["year"] for g in govs if g["colony"] == c]
        lines.append(f"- {c}: {n} ({min(yrs)}–{max(yrs)})")
    lines += ["", "## Sample succession (GOLD COAST)", ""]
    for g in [g for g in govs if g["colony"] == "GOLD COAST"][:25]:
        h = ", ".join(g["honours"][:3])
        lines.append(f"- {g['year']}: {g['given'] or ''} {g['surname']}"
                     f"{' (' + g['office'] + ')' if g['office'] else ''}"
                     f"{' — ' + h if h else ''} [{g['n_editions']} eds]")
    (OUT / "GOVERNORS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:14]))
    print(f"\nwrote {OUT}/governors.jsonl, GOVERNORS.md")


if __name__ == "__main__":
    main()
