#!/usr/bin/env python3
"""audit_governors.py — cross-check bio-derived governorship YEARS against the
Colonial Office List's own structured *governors tables*.

Why: a person's career-event years come from a single anchor bio (free text,
OCR'd), so a copy-forward typo like Guggisberg's "Br. Guiana, 1923" (really
1928) rides through. But every colony entry ALSO prints a "Governors since …"
table — name + exact appointment date — which is structured, independent and
repeated across editions. Where a person's bio governorship year disagrees with
the table, the table wins. Output = flagged conflicts, ready to fold into
data/kg/career_event_corrections.json.

Pass 1 (this run): parse the governors tables into (colony, name, year) rows.
Pass 2: join to the careers spine by surname+colony and flag year mismatches.
"""
import json, re, glob, collections, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OCR = ROOT / "raw_ocr" / "json"

# ---- colony gazetteer: label -> qid, from the shipped places.json -----------
def load_gazetteer():
    pl = json.load(open(ROOT / "docs" / "data" / "places.json"))
    g = {}
    for qid, v in pl.items():
        lab = v["label"]
        norm = _norm_colony(lab)
        if norm:
            g[norm] = qid
        # also index without the parenthetical qualifier already stripped by _norm
    return g, pl

_STOP = r"\b(colony|protectorate|protectorates|and|of|the|province|state|territory|settlements?|crown|islands?|british|its?|dependencies)\b"
def _norm_colony(s):
    s = re.sub(r"\(.*?\)", "", s)                 # drop "(Province)", "(British Raj)"
    s = re.sub(r"[^a-z ]", " ", s.lower())
    s = re.sub(_STOP, " ", s)
    return re.sub(r"\s+", " ", s).strip()

# ---- block walking ----------------------------------------------------------
def blocks_of(path):
    d = json.load(open(path))
    out = []
    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("text"), str):
                out.append((o.get("category"), o["text"]))
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(d)
    return out

GOV_TITLE = re.compile(r"^Governors?(?:-General)?\b", re.I)
# colony embedded in the title: "Governors of Queensland", "Governors-General of the Union"
TITLE_COLONY = re.compile(r"^Governors?(?:-General)?\s+of\s+(?:the\s+)?(.+?)(?:\s+since.*)?[.*¶†]*$", re.I)
ROW = re.compile(r"<td>(.*?)</td>\s*<td>(.*?)</td>", re.S)
YEAR = re.compile(r"\b(1[89]\d{2})\b")

def is_colony_header(cat, t):
    return cat == "title" and t.strip().upper() == t.strip() and len(t.strip()) >= 4 and re.search(r"[A-Z]{4,}", t)

def parse_edition(path, gaz):
    bl = blocks_of(path)
    recs = []
    last_header = None
    for i, (cat, t) in enumerate(bl):
        if is_colony_header(cat, t):
            n = _norm_colony(t)
            if n in gaz:
                last_header = (t.strip(), gaz[n])
        if cat == "title" and GOV_TITLE.match(t.strip()):
            # colony: prefer the one named in the title, else the nearest matched header
            colony_qid, colony_src = None, None
            m = TITLE_COLONY.match(t.strip())
            if m:
                n = _norm_colony(m.group(1))
                if n in gaz:
                    colony_qid, colony_src = gaz[n], "title"
            if not colony_qid and last_header:
                colony_qid, colony_src = last_header[1], "header"
            # the table block is usually the next block
            for j in (i + 1, i + 2):
                if j < len(bl) and bl[j][0] == "table":
                    for nm, dt in ROW.findall(bl[j][1]):
                        nm = re.sub(r"<.*?>", "", nm)
                        nm = re.sub(r"[.\s]*\.[.\s]*$", "", nm).strip()  # OCR leader dots
                        nm = re.sub(r"\s+", " ", nm).strip(" .¶†*")
                        ym = YEAR.search(dt)
                        if nm and ym and colony_qid:
                            recs.append({"colony_qid": colony_qid, "name": nm,
                                         "year": int(ym.group(1)), "colony_src": colony_src,
                                         "title": t.strip()})
                    break
    return recs

def main():
    gaz, pl = load_gazetteer()
    all_recs = []
    eds = sorted(glob.glob(str(OCR / "ColonialOfficeList*.pdf" / "result.json")))
    for path in eds:
        ed = re.search(r"List(\d{4})", path).group(1)
        recs = parse_edition(path, gaz)
        for r in recs: r["edition"] = ed
        all_recs.extend(recs)
    print(f"parsed {len(eds)} editions → {len(all_recs)} governor-table rows")
    src = collections.Counter(r["colony_src"] for r in all_recs)
    print("colony source:", dict(src))
    print("distinct colonies:", len({r['colony_qid'] for r in all_recs}))
    # sanity: British Guiana (Q918126) rows
    bg = [r for r in all_recs if r["colony_qid"] == "Q918126"]
    print(f"\nBritish Guiana rows: {len(bg)} — sample:")
    for r in sorted({(r['name'], r['year']) for r in bg}):
        print("  ", r)
    out = ROOT / "data" / "kg" / "governors_table_rows.jsonl"
    with out.open("w") as f:
        for r in all_recs: f.write(json.dumps(r) + "\n")
    print("\nwrote", out)

if __name__ == "__main__":
    main()
