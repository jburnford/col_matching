#!/usr/bin/env python3
"""Melt the statistical tables (finance / trade / population) into long-format
cells, and derive a colony-year panel.

The layout-aware OCR renders tables as pseudo-HTML. One generic parser melts
every table into (colony, edition, section, table_label, row_label, col_label,
value) cells; a panel view then keeps cells whose row label parses as a year.
The table's OWN header (thead colspan rows like "EXPORTS.") outranks the
governing section title, which lags across page breaks.

Outputs data/volume/context/:
  table_cells.jsonl      every melted cell
  colony_year_panel.csv  (colony, year, metric, value) for year-row cells
  CONTEXT_TABLES.md      coverage report
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.volume import reader
from volume_careers import canon_colony

ROOT = Path("data/volume")
OUT = ROOT / "context"
SECTIONS = {"finance", "trade", "population", "currency_banking"}

_ROW = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
_CELL = re.compile(r"<(t[dh])([^>]*)>(.*?)</t[dh]>", re.S)
_TAG = re.compile(r"<[^>]+>")
_NUM = re.compile(r"^[£$]?\s*(\d[\d,]*(?:\.\d+)?)$")
_YEAR_ROW = re.compile(r"(?:census[, ]+)?(1[6-9]\d\d)(?:\s*[-/]\s*\d{1,4})?\.?$", re.I)

# semantic metric classes — the same series is worded differently across
# editions ("EXPORTS." table label vs an Exports column inside a "Revenue and
# Expenditure." block), so the panel keys on class, not wording. The COLUMN
# label outranks the table label, which outranks the section title.
_CLASSES = [
    ("EXPORTS", re.compile(r"export", re.I)),
    ("IMPORTS", re.compile(r"import", re.I)),
    ("REVENUE", re.compile(r"revenue", re.I)),
    ("EXPENDITURE", re.compile(r"expenditure", re.I)),
    ("DEBT", re.compile(r"debt|loan", re.I)),
    ("POPULATION", re.compile(r"population|census|inhabitant|male|female", re.I)),
    ("SHIPPING", re.compile(r"shipping|tonnage|vessels|entered|cleared", re.I)),
]


def _metric_class(*texts: str | None) -> str | None:
    for t in texts:
        if not t:
            continue
        for name, rx in _CLASSES:
            if rx.search(t):
                return name
    return None


def _is_metric_label(t: str | None) -> bool:
    return bool(t) and any(rx.search(t) for _, rx in _CLASSES)


_QUAL_NORM = re.compile(r"[^a-z]+")


def _qual(col: str) -> str:
    q = _QUAL_NORM.sub(" ", col.lower().replace("£", "")).strip()
    return q or "value"


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", _TAG.sub(" ", s)).strip(" .·…")


def melt_table(html: str) -> tuple[str | None, list[dict]]:
    """-> (table_label, cells). Column labels from the last full thead row;
    colspan-spanning thead rows become the table label."""
    rows = _ROW.findall(html)
    col_labels: list[str] = []
    table_label = None
    cells = []
    for row in rows:
        parsed = [(kind, attrs, _clean(body)) for kind, attrs, body in _CELL.findall(row)]
        if not parsed:
            continue
        texts = [t for _, _, t in parsed]
        is_header = all(k == "th" for k, _, _ in parsed)
        if is_header:
            if len(parsed) == 1 and "colspan" in parsed[0][1]:
                if texts[0]:
                    table_label = texts[0]
            elif sum(bool(t) for t in texts) >= 2:
                col_labels = texts
            elif len([t for t in texts if t]) == 1 and not col_labels:
                table_label = table_label or next(t for t in texts if t)
            continue
        # body row: first cell = row label; a full-width colspan cell is a
        # sub-section label ("WEST INDIES—cont.") — becomes the table label
        if len(parsed) == 1 and "colspan" in parsed[0][1]:
            if texts[0]:
                table_label = texts[0]
            continue
        row_label, values = texts[0], texts[1:]
        labels = col_labels[1:] if len(col_labels) > 1 else []
        for i, v in enumerate(values):
            if not v:
                continue
            col = labels[i] if i < len(labels) else f"col{i+1}"
            m = _NUM.match(v)
            cells.append({"row": row_label, "col": col, "raw": v,
                          "num": float(m.group(1).replace(",", "")) if m else None})
    return table_label, cells


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    locs = defaultdict(list)
    for line in open(ROOT / "block_index.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if r["section"] in SECTIONS and r["category"] == "table" and r["colony"]:
            locs[r["year"]].append(r)

    n_tables = n_cells = 0
    panel_rows = []
    coverage = defaultdict(set)             # (colony, section) -> years
    with (OUT / "table_cells.jsonl").open("w", encoding="utf-8") as fh:
        for year in sorted(locs):
            bmap = {(b.page, b.index): b for b in reader.load_volume(year, "col")}
            for r in locs[year]:
                b = bmap.get((r["page"], r["block"]))
                if b is None:
                    continue
                colony = canon_colony(r["colony"])
                if colony is None:
                    continue
                label, cells = melt_table(b.text)
                if not cells:
                    continue
                n_tables += 1
                for c in cells:
                    n_cells += 1
                    fh.write(json.dumps({
                        "edition": year, "colony": colony, "section": r["section"],
                        "title": r["title"][:60], "table_label": label, **c,
                        "page": r["page"], "block": r["block"],
                    }, ensure_ascii=False) + "\n")
                    ym = _YEAR_ROW.match(c["row"].lower())
                    if ym and c["num"] is not None:
                        cls = _metric_class(c["col"], label, r["title"], r["section"])
                        if cls is None:
                            continue
                        subunit = (label if label and not _is_metric_label(label)
                                   and not label.isupper() else None)
                        metric = f"{cls}:{_qual(c['col'])}" + \
                                 (f"[{subunit}]" if subunit else "")
                        panel_rows.append((colony, int(ym.group(1)), metric[:90],
                                           c["num"], c["raw"], year))
                        coverage[(colony, r["section"])].add(int(ym.group(1)))

    # panel: same (colony, data-year, metric) is reprinted in many editions —
    # MAJORITY VOTE across editions kills one-off OCR digit garble ('£393k'
    # misread as '£893k' in a single scan); ties break to the latest edition
    grouped = defaultdict(list)
    for colony, dy, metric, num, raw, ed in panel_rows:
        grouped[(colony, dy, metric)].append((num, raw, ed))
    best = {}
    disagree = 0
    for k, vals in grouped.items():
        votes = Counter(num for num, _, _ in vals)
        if len(votes) > 1:
            disagree += 1
        top_n = max(votes.values())
        winners = {n for n, c in votes.items() if c == top_n}
        num, raw, ed = max((v for v in vals if v[0] in winners), key=lambda v: v[2])
        best[k] = (num, raw, ed, len(vals), len(votes))
    print(f"panel points with cross-edition disagreement: {disagree:,} of "
          f"{len(best):,} ({100*disagree/max(len(best),1):.1f}%) — majority-voted")
    with (OUT / "colony_year_panel.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["colony", "year", "metric", "value", "raw", "edition",
                    "n_attestations", "n_distinct_values"])
        for (colony, dy, metric), (num, raw, ed, na, nd) in sorted(best.items()):
            w.writerow([colony, dy, metric, num, raw, ed, na, nd])

    col_years = defaultdict(set)
    for (colony, dy, _m) in best:
        col_years[colony].add(dy)
    lines = ["# Context tables melted", "",
             f"- tables parsed: {n_tables:,}; cells: {n_cells:,}",
             f"- colony-year panel: {len(best):,} (colony, year, metric) points, "
             f"{len(col_years)} colonies",
             "", "## Deepest colony series (distinct data-years)", ""]
    for c, ys in sorted(col_years.items(), key=lambda kv: -len(kv[1]))[:15]:
        lines.append(f"- {c}: {len(ys)} years ({min(ys)}–{max(ys)})")
    lines += ["", "## Sample: GOLD COAST revenue/trade points", ""]
    shown = 0
    for (colony, dy, metric), (num, raw, ed, na, nd) in sorted(best.items()):
        if colony == "GOLD COAST" and "total" in metric.lower() and shown < 12:
            lines.append(f"- {dy} {metric}: {raw} [{na} attestations, "
                         f"{nd} distinct]")
            shown += 1
    (OUT / "CONTEXT_TABLES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:12]))
    print(f"\nwrote {OUT}/table_cells.jsonl, colony_year_panel.csv, CONTEXT_TABLES.md")


if __name__ == "__main__":
    main()
