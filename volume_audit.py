#!/usr/bin/env python3
"""Cross-edition audit of the volume roster extraction.

For every data/volume/col<year>/ produced by volume_link.py, reports:
  - records, roster blocks, records-per-block, bios, link rate
  - colonies detected; suspicious headers (not seen in >=3 other editions and
    not in the old manual_parsed chapter inventory)
  - rules-tier residue: roster blocks that yielded zero records (the Qwen
    worklist), overall and for the worst editions
  - expected-chapter check against ~/textasdatacolonialofficelist/{year}_manual_parsed

Usage: python3 volume_audit.py [--out data/volume/AUDIT.md]
"""
import json, os, re, argparse
from collections import Counter, defaultdict
from pathlib import Path

TAD = Path.home() / "textasdatacolonialofficelist"
ROOT = Path(__file__).parent / "data" / "volume"

def norm(h):
    h = h.upper().strip().rstrip(".")
    h = re.sub(r"^THE ", "", h)
    h = re.sub(r"[^A-Z& ]", " ", h)
    return re.sub(r"\s+", " ", h).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "AUDIT.md"))
    args = ap.parse_args()

    editions = sorted(int(p.name[3:]) for p in ROOT.glob("col[0-9]*") if p.name[3:].isdigit())
    colony_seen = Counter()          # normalized colony -> #editions
    per, residue_blocks = {}, {}
    for y in editions:
        d = ROOT / f"col{y}"
        summ = json.load(open(d / "summary.json")) if (d / "summary.json").exists() else {}
        recs = [json.loads(l) for l in open(d / "records.jsonl")] if (d / "records.jsonl").exists() else []
        blocks = [json.loads(l) for l in open(d / "roster_blocks.jsonl")] if (d / "roster_blocks.jsonl").exists() else []
        cols = Counter(r["colony"] for r in recs)
        for c in set(map(norm, cols)):
            colony_seen[c] += 1
        rec_blocks = {(r["provenance"]["page"], r["provenance"]["block"]) for r in recs}
        res = [b for b in blocks
               if (b["provenance"]["page"], b["provenance"]["block"]) not in rec_blocks
               and len(b.get("text", "")) > 60]
        per[y] = dict(records=len(recs), blocks=len(blocks), colonies=cols,
                      residue=len(res), summ=summ)
        residue_blocks[y] = res

    # old-corpus expected chapters per year
    expected = {}
    for y in editions:
        d = TAD / f"{y}_manual_parsed"
        if d.is_dir():
            expected[y] = {norm(f.stem.replace("_", " ")) for f in d.glob("*.txt")
                           if not f.name.endswith("Zone.Identifier")}

    out = ["# Volume roster extraction — cross-edition audit\n"]
    out.append("| year | pages | bios | records | roster blocks | residue blocks | link rate | colonies | missing vs old corpus |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    tot_rec = tot_res = tot_blk = 0
    for y in editions:
        p = per[y]; s = p["summ"]
        pages = s.get("pages", "")
        bios = s.get("bios", {}).get("n_bios", "")
        lr = s.get("bio_link_rate", 0)
        found = {norm(c) for c in p["colonies"]}
        miss = sorted(expected.get(y, set()) - found) if y in expected else []
        tot_rec += p["records"]; tot_res += p["residue"]; tot_blk += p["blocks"]
        out.append(f"| {y} | {pages} | {bios} | {p['records']:,} | {p['blocks']:,} | "
                   f"{p['residue']:,} | {lr:.0%} | {len(p['colonies'])} | "
                   f"{len(miss)}{': ' + ', '.join(miss[:4]) if miss else ''} |")
    out.append(f"\n**Totals:** {tot_rec:,} records; {tot_blk:,} roster blocks; "
               f"{tot_res:,} residue blocks (rules-tier zero-yield, the Qwen worklist).\n")

    # suspicious colony headers: in 1-2 editions only and never in old corpus
    all_expected = set().union(*expected.values()) if expected else set()
    susp = [(c, n) for c, n in colony_seen.items() if n <= 2 and c not in all_expected]
    out.append(f"## Suspicious colony headers (seen in <=2 editions, not in old corpus): {len(susp)}\n")
    for c, n in sorted(susp):
        out.append(f"- {c} ({n})")

    # residue sample from the worst editions
    worst = sorted(editions, key=lambda y: -per[y]["residue"])[:5]
    out.append("\n## Residue samples (worst editions)\n")
    for y in worst:
        out.append(f"### col{y} — {per[y]['residue']} residue blocks")
        for b in residue_blocks[y][:3]:
            out.append(f"- [{b['colony']} / {b.get('department')}] p{b['provenance']['page']}: "
                       f"{b['text'][:180].replace(chr(10),' ')}…")

    Path(args.out).write_text("\n".join(out) + "\n")
    print(f"wrote {args.out}")
    print(f"editions {len(editions)}  records {tot_rec:,}  residue blocks {tot_res:,} "
          f"({100*tot_res/max(tot_blk,1):.0f}% of roster blocks)")

if __name__ == "__main__":
    main()
