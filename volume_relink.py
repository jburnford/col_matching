#!/usr/bin/env python3
"""Standalone bios↔roster RE-linker over the merged record files.

volume_link.py regenerates records.jsonl from raw OCR (rules tier only), which
would wipe the merged Qwen records. This driver instead RELOADS the existing
per-edition bios.jsonl + records.jsonl (rules + qwen, source-flagged), re-runs
col_match.volume.match.link_volume, and rewrites links.jsonl / summary.json /
report.md in place. records.jsonl is never touched.

  python3 volume_relink.py                 # all data/volume/col* editions
  python3 volume_relink.py --years 1888,1921
  python3 volume_relink.py --out data/volume/RELINK.md
"""

from __future__ import annotations

import argparse
import json
from dataclasses import fields
from pathlib import Path

from col_match.config import Config
from col_match.volume.bios import VolumeBio
from col_match.volume.roster import VolumeRecord
from col_match.volume import match as match_mod
from volume_link import _dump, _write_report

_BIO_FIELDS = {f.name for f in fields(VolumeBio)}
_REC_FIELDS = {f.name for f in fields(VolumeRecord)}


def _load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def relink(ed_dir: Path, cfg: Config) -> dict | None:
    bios_p, recs_p, summ_p = (ed_dir / n for n in
                              ("bios.jsonl", "records.jsonl", "summary.json"))
    if not (bios_p.exists() and recs_p.exists() and summ_p.exists()):
        return None
    summary = json.loads(summ_p.read_text())
    old_rate = summary.get("bio_link_rate", 0.0)
    old_links = summary.get("match", {}).get("links", 0)

    bios = [VolumeBio(**{k: v for k, v in row.items() if k in _BIO_FIELDS})
            for row in _load_jsonl(bios_p)]
    rec_rows = _load_jsonl(recs_p)
    source = {row["record_id"]: row.get("source", "rules") for row in rec_rows}
    records = [VolumeRecord(**{k: v for k, v in row.items() if k in _REC_FIELDS})
               for row in rec_rows]

    links, mstats = match_mod.link_volume(bios, records, cfg.data_dir)
    by_src = {"rules": 0, "qwen": 0}
    for ln in links:
        by_src[source.get(ln.record_id, "rules")] += 1
    mstats["links_by_record_source"] = by_src

    n_bios = summary.get("bios", {}).get("n_bios", 0)
    new_rate = mstats["bios_linked"] / n_bios if n_bios else 0.0
    summary["match"] = mstats
    summary["bio_link_rate"] = round(new_rate, 4)
    summary["roster"]["n_records"] = len(records)   # merged count
    summary["relink"] = {"old_bio_link_rate": old_rate, "old_links": old_links,
                         "records_rules": sum(1 for s in source.values() if s == "rules"),
                         "records_qwen": sum(1 for s in source.values() if s == "qwen")}

    _dump(ed_dir / "links.jsonl", links)
    _write_report(ed_dir / "report.md", summary, links, records)
    summ_p.write_text(json.dumps(summary, indent=2, default=int))
    return summary


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="data/volume")
    ap.add_argument("--years", help="comma-separated subset")
    ap.add_argument("--out", default="data/volume/RELINK.md")
    args = ap.parse_args()

    cfg = Config.from_env()
    root = Path(args.root)
    only = {int(y) for y in args.years.split(",")} if args.years else None
    rows = []
    for ed_dir in sorted(root.glob("col*")):
        if not ed_dir.is_dir():
            continue
        year = int(ed_dir.name[3:])
        if only and year not in only:
            continue
        s = relink(ed_dir, cfg)
        if s is None:
            print(f"{ed_dir.name}: missing inputs, skipped")
            continue
        m, r = s["match"], s["relink"]
        rows.append((year, s["bios"]["n_bios"], r["records_rules"], r["records_qwen"],
                     m["links"], m["bios_linked"], r["old_bio_link_rate"],
                     s["bio_link_rate"], m["links_by_record_source"]["qwen"]))
        print(f"col{year}: bios {rows[-1][1]:5d} | recs {r['records_rules']+r['records_qwen']:6d} "
              f"({r['records_qwen']} qwen) | links {m['links']:5d} "
              f"({m['links_by_record_source']['qwen']} to qwen) | linked "
              f"{m['bios_linked']:5d} | rate {r['old_bio_link_rate']*100:.1f}% -> "
              f"{s['bio_link_rate']*100:.1f}%")

    lines = ["# Bio↔roster relink over merged (rules+qwen) records", "",
             "| year | bios | rules recs | qwen recs | links | links→qwen | bios linked | old rate | new rate |",
             "|---|---|---|---|---|---|---|---|---|"]
    tb = te = 0
    for y, nb, nr, nq, nl, bl, orr, nrr, lq in rows:
        lines.append(f"| {y} | {nb:,} | {nr:,} | {nq:,} | {nl:,} | {lq:,} | {bl:,} "
                     f"| {orr*100:.1f}% | {nrr*100:.1f}% |")
        tb += nb; te += bl
    if rows:
        lines += ["", f"**Total:** {te:,}/{tb:,} bios linked "
                  f"(**{te/tb*100:.1f}%**) across {len(rows)} editions."]
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
