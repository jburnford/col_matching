#!/usr/bin/env python3
"""Extract the Colonial Office's OWN front matter: the London side of empire.

Every edition opens (after the adverts) with "THE COLONIAL OFFICE.":
  - SECRETARIES OF STATE FOR THE COLONIES FROM 1854 — succession list
  - UNDER-SECRETARIES OF STATE (Permanent. / Parliamentary. / Assistant.)
  - THE ESTABLISHMENT OF THE COLONIAL OFFICE — the CO's staff roster
  - DIVISIONS AND DEPARTMENTS — per-department staff assignments
None of it was extracted before: it precedes the first colony running header,
so the roster walker had colony=None. This extractor scopes the zone (first
"THE COLONIAL OFFICE" title -> first colony header), reuses the succession
parsers from volume_governors and the record parsers from roster.py with
colony "COLONIAL OFFICE (LONDON)".

Outputs data/volume/context/:
  co_succession.jsonl   Secretaries/Under-Secretaries of State (merged)
  co_staff.jsonl        per-edition CO establishment records
  CO_OFFICE.md          report
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import distance

from col_match.volume import reader, roster
from volume_governors import parse_text_block, parse_text_yearfirst

ROOT = Path("data/volume")
OUT = ROOT / "context"

_ZONE_START = re.compile(r"^THE COLONIAL OFFICE\.?$", re.I)
_SOS = re.compile(r"SECRETARIES OF STATE", re.I)
_USS = re.compile(r"UNDER[- ]SECRETARIES", re.I)
_USS_SUB = {"permanent": "Permanent Under-Secretary",
            "parliamentary": "Parliamentary Under-Secretary",
            "assistant": "Assistant Under-Secretary",
            "legal": "Legal Assistant Under-Secretary"}
_ESTAB = re.compile(r"ESTABLISHMENT|DIVISION|DEPARTMENT|ADVISERS|CROWN AGENTS"
                    r"|OVERSEA SETTLEMENT|AUDIT", re.I)


_ROWRE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
_CELLRE = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S)
_TAGRE = re.compile(r"<[^>]+>")
_YEARCELL = re.compile(r"^(1[6-9]\d\d)(?:\s*[-–]\s*(\d{2,4}))?[,.]?")
_DATECELL = re.compile(r"(\d{1,2}\s+\w{3,5}\.?,?\s+)?(\d{2,4})\s*$")


def _cl(s: str) -> str:
    return re.sub(r"\s+", " ", _TAGRE.sub(" ", s)).strip()


def _yy(tok: str) -> int | None:
    """'98' -> 1898, '07' -> 1907, '1907' -> 1907."""
    if len(tok) == 4 and tok.isdigit():
        return int(tok)
    if len(tok) == 2 and tok.isdigit():
        v = int(tok)
        return 1800 + v if v >= 50 else 1900 + v
    return None


def parse_succession_table(html: str) -> list[dict]:
    """Paired-cell succession tables: <td>1854, June 10.</td><td>Right Hon.
    Sir G. Grey, Bart.</td> — possibly two pairs per row (two columns)."""
    from volume_governors import _parse_person
    out = []
    for row in _ROWRE.findall(html):
        cells = [_cl(c) for c in _CELLRE.findall(row)]
        i = 0
        while i < len(cells) - 1:
            m = _YEARCELL.match(cells[i])
            if m and cells[i + 1]:
                person = _parse_person(cells[i + 1])
                if person is not None:
                    _office, given, surname, honours = person
                    y2 = _yy(m.group(2)) if m.group(2) else None
                    out.append({"given": given, "surname": surname,
                                "honours": honours, "year": int(m.group(1)),
                                "year2": y2, "date": cells[i][:30]})
                i += 2
            else:
                i += 1
    return out


def parse_promotion_matrix(html: str) -> list[dict]:
    """The CO establishment matrix: rows = person, columns = grade, cells =
    promotion date into that grade -> per-person promotion ladders."""
    from volume_governors import _parse_person
    rows = _ROWRE.findall(html)
    grades: list[str] = []
    out = []
    for row in rows:
        cells = [_cl(c) for c in _CELLRE.findall(row)]
        if not cells:
            continue
        if cells[0].lower().startswith("name"):
            grades = [re.sub(r"^[†‡§*|]+\s*", "", c).strip(" .") for c in cells[1:]]
            continue
        if not grades or not cells[0]:
            continue
        person = _parse_person(cells[0])
        if person is None:
            continue
        _o, given, surname, honours = person
        promotions = []
        for g, cell in zip(grades, cells[1:]):
            dm = _DATECELL.search(cell)
            if dm:
                y = _yy(dm.group(2))
                if y:
                    promotions.append({"grade": g, "date": cell.strip(" ."),
                                       "year": y})
        if promotions:
            out.append({"surname": surname, "given_names": given,
                        "honours": honours, "promotions": promotions})
    return out


def co_zone(blocks) -> tuple[int, int] | None:
    start = None
    for i, b in enumerate(blocks):
        if b.category == "title" and _ZONE_START.match(b.text.strip()) and b.page > 4:
            start = i
            break
    if start is None:
        return None
    for j in range(start + 1, len(blocks)):
        if blocks[j].category == "header":
            sig, _h = roster._colony_signal(blocks[j].text)
            if sig == "set":
                return start, j
    return start, min(start + 2000, len(blocks))


def extract_edition(year: int) -> tuple[list[dict], list[dict]]:
    blocks = reader.load_volume(year, "col")
    zone = co_zone(blocks)
    succession, staff = [], []
    if zone is None:
        return succession, staff
    mode = None            # 'sos' | 'uss' | 'staff' | None
    office = None
    department = None
    for b in blocks[zone[0]:zone[1]]:
        if b.category == "title":
            t = b.text.strip().rstrip(".")
            tl = t.lower()
            if _USS.search(t):          # before _SOS: "UNDER-SECRETARIES OF
                mode, office = "uss", "Under-Secretary of State"  # STATE" contains it
            elif _SOS.search(t):
                mode, office = "sos", "Secretary of State for the Colonies"
            elif mode == "uss" and tl in _USS_SUB:
                office = _USS_SUB[tl]
            elif _ESTAB.search(t) and len(t) < 70:
                mode, department = "staff", t
            continue
        if mode is None or b.category not in ("text", "table"):
            continue
        if mode in ("sos", "uss"):
            if b.category == "table":
                recs = parse_succession_table(b.text)
            else:
                a = parse_text_block(b.text)
                z = parse_text_yearfirst(b.text)
                recs = a if len(a) >= len(z) else z
            for rec in recs:
                rec.update({"office": office, "edition": year})
                succession.append(rec)
        elif mode == "staff":
            if b.category == "table":
                matrix = parse_promotion_matrix(b.text)
                if matrix:
                    for m in matrix:
                        staff.append({"edition": year, "department": department,
                                      "position": None, "salary": None,
                                      "page": b.page, **m})
                    continue
                # simple cell tables: each cell is "Position, Name, honours"
                for row in _ROWRE.findall(b.text):
                    for cell in (_cl(c) for c in _CELLRE.findall(row)):
                        for position, surname, given, honours in \
                                roster._parse_record_chunk(cell):
                            staff.append({
                                "edition": year, "department": department,
                                "position": position, "surname": surname,
                                "given_names": given, "honours": honours,
                                "salary": None, "page": b.page})
                continue
            chunks = roster._split_records(b.text)
            if not chunks and ("—" in b.text or "–" in b.text):
                chunks = roster._split_records_emdash(b.text)
            for chunk, salary in chunks:
                for position, surname, given, honours in roster._parse_record_chunk(chunk):
                    staff.append({
                        "edition": year, "department": department,
                        "position": position, "surname": surname,
                        "given_names": given, "honours": honours,
                        "salary": salary, "page": b.page,
                    })
    return succession, staff


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    years = sorted(int(d.name[3:]) for d in ROOT.glob("col[0-9]*"))
    all_succ, all_staff = [], []
    for y in years:
        s, st = extract_edition(y)
        all_succ.extend(s)
        all_staff.extend(st)

    # merge successions across editions (cumulative lists)
    merged = {}
    for rec in sorted(all_succ, key=lambda r: r["edition"]):
        sur = rec["surname"].lower()
        key = (rec["office"], rec["year"], sur)
        if key not in merged:
            hit = None
            for (o, yy, s), v in merged.items():
                if o == rec["office"] and yy == rec["year"] \
                        and distance.Levenshtein.distance(s, sur, score_cutoff=2) <= 2:
                    hit = (o, yy, s)
                    break
            key = hit or key
        if key in merged:
            v = merged[key]
            v["n_editions"] += 1
            if rec.get("given") and len(rec["given"] or "") > len(v["given"] or ""):
                v["given"] = rec["given"]
            v["honours"] = sorted(set(v["honours"]) | set(rec["honours"]))
        else:
            merged[key] = {**{k: rec.get(k) for k in
                              ("office", "given", "surname", "honours",
                               "year", "date")}, "n_editions": 1}
    succ = sorted(merged.values(), key=lambda r: (r["office"] or "", r["year"]))

    with (OUT / "co_succession.jsonl").open("w", encoding="utf-8") as fh:
        for r in succ:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (OUT / "co_staff.jsonl").open("w", encoding="utf-8") as fh:
        for r in all_staff:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    by_office = Counter(r["office"] for r in succ)
    staff_eds = Counter(r["edition"] for r in all_staff)
    lines = ["# Colonial Office front matter extracted", "",
             f"- succession records: {len(all_succ):,} raw -> {len(succ):,} "
             f"distinct appointments",
             f"- CO staff records: {len(all_staff):,} across "
             f"{len(staff_eds)} editions (median {sorted(staff_eds.values())[len(staff_eds)//2] if staff_eds else 0}/edition)",
             "", "## Succession by office", ""]
    lines += [f"- {o}: {n}" for o, n in by_office.most_common()]
    lines += ["", "## Secretaries of State (sample, post-1890)", ""]
    for r in [r for r in succ if r["office"] and "Secretary of State" in r["office"]
              and r["office"].startswith("Secretary") and r["year"] >= 1890][:15]:
        lines.append(f"- {r['year']}: {r['given'] or ''} {r['surname']} "
                     f"[{r['n_editions']} eds]")
    (OUT / "CO_OFFICE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:12]))
    print(f"\nwrote {OUT}/co_succession.jsonl, co_staff.jsonl, CO_OFFICE.md")


if __name__ == "__main__":
    main()
