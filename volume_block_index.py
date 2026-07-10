#!/usr/bin/env python3
"""Block-level content index of the Colonial Office List volumes.

Maps every OCR block to (colony, section class, governing title) so we can
see WHAT the volumes contain beyond the rosters and bios — the planning map
for extracting the economic / political / social context layers of the
knowledge graph.

Rules-first: the profile chapters are internally signposted by printed
section titles ("Revenue and Expenditure.", "Population.", "Governors."), so
classification is keyword-on-title; the roster/bios machinery supplies the
establishment and services classes. Blocks with no governing title (or an
unrecognized one) are the residue; when the Qwen title-classification pass
has run (data/volume/qwen_title_results.jsonl from nibi/qwen_title_worker.py)
its per-title labels apply as a fallback tier — rows carry
section_source = "rules" | "qwen_title" so the tiers stay distinguishable.

Outputs:
  data/volume/block_index.jsonl   one line per text/table block
  data/volume/INVENTORY.md        corpus survey by section x era + coverage
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.volume import bios as bios_mod
from col_match.volume import reader, roster

ROOT = Path("data/volume")

# ordered: first match wins
_TAXONOMY: list[tuple[str, str]] = [
    ("governors_list", r"\bgovernors\b|governors of|administrators of|high commissioners of"),
    ("honours_roll", r"companions|knights|order of|dames|imperial service order"),
    ("obituary", r"obituary"),
    ("history", r"history|historical"),
    ("geography", r"situation|area|geograph|climate|physical features|general description|boundaries"),
    ("population", r"population|census|inhabitants|vital statistics"),
    ("constitution", r"constitution|government\b|franchise|local government|administration\b"),
    ("councils", r"executive council|legislative council|legislative assembly|privy council|house of assembly"),
    ("finance", r"revenue|expenditure|finance|taxation|public debt|tariff|budget"),
    ("currency_banking", r"currency|banking|coinage|exchange"),
    ("trade", r"imports|exports|trade|commerce|shipping|staple|crops|products|industr|occupations|marketing|agricultur(?!al department)|mining|fisheries"),
    ("infrastructure", r"communication|railway|road|harbour|harbor|port\b|telegraph|telephone|broadcasting|aviation|post office|postal"),
    ("land_labour", r"land policy|land tenure|crown lands|immigration|emigration|labour|labor|development plan"),
    ("social", r"education(?! department)|school|health|hospital|religion|ecclesiastic|church|welfare|housing"),
    ("justice", r"justice|judicial(?! establishment| department)|laws|legal|crime"),
    ("defence", r"defence|defense|military|militia|volunteer|garrison"),
    ("agents_consuls", r"consuls|agents"),
    ("regulations", r"regulations|rules|^§|precedency|passages|instructions"
                    r"|^part [ivx]+|introduction|\bact\b"),
    ("papers", r"parliamentary|papers|publications|bibliograph"),
    # establishment/membership variants outside the roster-title regex
    ("establishment", r"\bmembers\b|\bstaff\b|minist(?:er|r)|court of directors"
                      r"|supreme court|magistrate|\bmarine\b|native affairs"
                      r"|imperial conference|secretary's office|secretary"),
    ("imperial_institutions", r"royal botanic|bureau of hygiene|imperial institute"
                              r"|colonial office|distribution of business"
                              r"|crown agents|royal colonial institute"),
    ("geography", r"description|statistics|^general$|chief towns|dependencies"),
    ("land_labour", r"\bland\b"),
    ("infrastructure", r"postage"),
]
_TAX_RE = [(name, re.compile(pat, re.I)) for name, pat in _TAXONOMY]

_EST = re.compile(roster._ROSTER_TITLE.pattern, re.I)


def classify_title(title: str | None) -> str | None:
    if not title:
        return None
    t = title.strip().rstrip(".")
    for name, rx in _TAX_RE:
        if rx.search(t):
            return name
    if _EST.search(t):
        return "establishment"
    return None


_QWEN_TITLES: dict[str, str] | None = None


def _qwen_title_map() -> dict[str, str]:
    """title[:80] -> section from the GPU title-classification pass; 'other'
    and 'garbled' verdicts stay residue (they are labels, not sections)."""
    global _QWEN_TITLES
    if _QWEN_TITLES is None:
        _QWEN_TITLES = {}
        p = ROOT / "qwen_title_results.jsonl"
        if p.exists():
            for line in p.open(encoding="utf-8"):
                r = json.loads(line)
                cls = r.get("class")
                if cls and cls not in ("other", "garbled"):
                    _QWEN_TITLES[r["title"]] = cls
    return _QWEN_TITLES


def index_volume(year: int, out_fh) -> list[dict]:
    blocks = reader.load_volume(year, "col")
    sec = bios_mod.find_services_section(blocks)
    vocab = roster.colony_vocab(blocks)
    colony = None
    title = None
    zone = None      # back-matter section name (the reset header): OBITUARY,
    #                  ORDER OF ST MICHAEL AND ST GEORGE, INDEX, ...
    rows = []
    for i, b in enumerate(blocks):
        if b.category == "header":
            sig, h = roster._colony_signal(b.text)
            if sig == "reset":
                colony, title = None, None
                zone = re.sub(r"\s+", " ", b.text.strip().strip(". "))
            elif sig == "set" and h != colony:
                colony, title, zone = h, None, None
            continue
        if b.category == "title":
            sig, _ = roster._colony_signal(b.text)
            if sig == "reset":
                colony, title = None, None
                zone = re.sub(r"\s+", " ", b.text.strip().strip(". "))
                continue
            tcol = roster._title_colony(b.text, vocab)
            if tcol is not None:
                colony, title = tcol, None
                continue
            title = re.sub(r"\s+", " ", b.text.strip())
            continue
        if b.category not in ("text", "table"):
            continue
        source = "rules"
        if sec and sec[0] <= i < sec[1]:
            section = "services_bios"
        else:
            section = classify_title(title)
            if section == "establishment" or (section == "councils" and b.category == "text"):
                section = "establishment"
            elif section is None:
                # back-matter zone rescues title-less blocks (the zone header
                # RESETS the title, so obituaries/honours rolls landed untitled)
                zsec = classify_title(zone)
                if zsec in ("obituary", "honours_roll"):
                    section = zsec
                elif title is not None and (title or "")[:80] in _qwen_title_map():
                    section = _qwen_title_map()[(title or "")[:80]]
                    source = "qwen_title"
                else:
                    section = "untitled" if title is None else "other_titled"
        rows.append({"year": year, "page": b.page, "block": b.index,
                     "category": b.category, "colony": colony,
                     "section": section, "section_source": source,
                     "title": (title or "")[:80],
                     "zone": zone, "chars": len(b.text)})
    for r in rows:
        out_fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return rows


def main() -> None:
    all_rows = []
    with (ROOT / "block_index.jsonl").open("w", encoding="utf-8") as fh:
        for d in sorted(ROOT.glob("col[0-9]*")):
            year = int(d.name[3:])
            rows = index_volume(year, fh)
            all_rows.extend(rows)
            print(f"col{year}: {len(rows):,} blocks indexed", flush=True)

    # ------------------------------------------------------------- inventory
    def era(y):
        return f"{10 * (y // 10)}s"

    by_sec = defaultdict(lambda: Counter())
    tables = Counter()
    chars = Counter()
    eds_cov = defaultdict(set)
    col_cov = defaultdict(set)
    for r in all_rows:
        by_sec[r["section"]][era(r["year"])] += 1
        chars[r["section"]] += r["chars"]
        if r["category"] == "table":
            tables[r["section"]] += 1
        eds_cov[r["section"]].add(r["year"])
        if r["colony"]:
            col_cov[r["section"]].add(r["colony"])

    eras = sorted({era(r["year"]) for r in all_rows})
    lines = ["# Colonial Office List — block-level content inventory", "",
             f"{len(all_rows):,} text/table blocks across 68 editions "
             f"({sum(chars.values())/1e6:.0f}M chars). Section = printed title "
             "keyword class; `untitled`/`other_titled` = the Qwen-indexing residue.",
             "",
             "| section | blocks | Mchars | tables | editions | colonies | " +
             " | ".join(eras) + " |",
             "|---|---|---|---|---|---|" + "---|" * len(eras)]
    for s, cnt in sorted(by_sec.items(), key=lambda kv: -sum(kv[1].values())):
        row = (f"| {s} | {sum(cnt.values()):,} | {chars[s]/1e6:.1f} | "
               f"{tables[s]:,} | {len(eds_cov[s])} | {len(col_cov[s])} | ")
        row += " | ".join(f"{cnt.get(e, 0):,}" for e in eras) + " |"
        lines.append(row)
    (ROOT / "INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nwrote {ROOT}/block_index.jsonl + INVENTORY.md")


if __name__ == "__main__":
    main()
