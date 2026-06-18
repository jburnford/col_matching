"""IN-SESSION LLM dedup review harness (read-only; emits decision-ready dossiers).

Surfaces candidate same-person CLUSTERS for human/LLM adjudication: bios are
linked when they share a spelled forename token AND a surname suffix (the
OCR-truncation-tolerant key from compile pass E), so garbled/truncated surname
variants of one person land in the same cluster. Connected components of size
>=2 that compile did NOT already merge are the review units.

The adjudicator reads each cluster and writes verdicts to
  data/services/dedup/llm_merges.jsonl   (one JSON object per MERGE group)
keyed on stable version_ids; compile unions those versions on the next run.
Clusters whose bios are already covered by the ledger are skipped, so the loop
resumes where it left off.

Usage:
  python3 dedup_review.py --limit 15            # next 15 unreviewed clusters
  python3 dedup_review.py --limit 15 --min 2 --max 6   # bound cluster size
  python3 dedup_review.py --stats               # coverage / how many remain
Run with COL_USE_AUGMENTED=1.
"""
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from pathlib import Path

from col_match.config import Config
from col_match.services.schema import Biography, ParsedEntry
from col_match.services.match import _norm
from col_match.services.compile import _canon_token

cfg = Config.from_env(); DD = Path(cfg.data_dir)
LEDGER = DD / "dedup" / "llm_merges.jsonl"

ap = argparse.ArgumentParser()
ap.add_argument("--limit", type=int, default=15)
ap.add_argument("--min", type=int, default=2, help="min cluster size to show")
ap.add_argument("--max", type=int, default=8, help="max cluster size to show")
ap.add_argument("--stats", action="store_true")
ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--ignore-ledger", action="store_true",
                help="re-emit clusters even if already in the ledger (replay Opus's dossiers "
                     "for a DeepSeek A/B); deterministic order is unchanged")
args = ap.parse_args()

bios = [Biography.model_validate_json(l)
        for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
edu = {}
for name in ("llm.jsonl", "rules.jsonl"):
    p = DD / "parsed" / name
    if p.exists():
        for l in p.open(encoding="utf-8"):
            r = ParsedEntry.model_validate_json(l)
            edu[r.version_id] = r.education or ""

matched = set()
for fn in ("stint_matches.jsonl", "record_attachments.jsonl"):
    p = DD / "matches" / fn
    if p.exists():
        for l in p.open(encoding="utf-8"):
            matched.add(json.loads(l)["bio_id"])

# ledger: versions already adjudicated (in any merge group)
reviewed_versions = set()
n_groups = 0
if LEDGER.exists():
    for l in LEDGER.open(encoding="utf-8"):
        g = json.loads(l)
        reviewed_versions.update(g.get("versions", []))
        n_groups += 1

def spelled(b):
    return {_canon_token(t) for t in re.split(r"[ .]+", b.given_names or "") if len(_canon_token(t)) > 2}

# union-find over bios linked by (shared spelled forename token AND shared surname suffix-4)
idx = {b.bio_id: i for i, b in enumerate(bios)}
parent = list(range(len(bios)))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[ra] = rb

buckets = defaultdict(list)
for b in bios:
    sur = _norm(b.surname)
    if len(sur) < 5:
        continue
    suf = sur[-4:]
    for tok in spelled(b):
        buckets[(tok, suf)].append(b.bio_id)
for members in buckets.values():
    for k in range(1, len(members)):
        union(idx[members[0]], idx[members[k]])

comps = defaultdict(list)
for b in bios:
    comps[find(idx[b.bio_id])].append(b)

clusters = [c for c in comps.values() if len(c) >= 2]
# unreviewed = no bio in the cluster has a version already in the ledger
def cluster_versions(c): return {v for b in c for v in b.version_ids}
unreviewed = clusters if args.ignore_ledger else \
    [c for c in clusters if not (cluster_versions(c) & reviewed_versions)]

if args.stats:
    total_bios_in_clusters = sum(len(c) for c in clusters)
    print(f"ledger: {n_groups} merge groups, {len(reviewed_versions)} versions adjudicated")
    print(f"candidate clusters (>=2 bios, shared forename+surname-suffix): {len(clusters)}  "
          f"covering {total_bios_in_clusters} bios")
    print(f"UNREVIEWED clusters remaining: {len(unreviewed)}  "
          f"covering {sum(len(c) for c in unreviewed)} bios")
    from collections import Counter
    sz = Counter(min(len(c), 10) for c in unreviewed)
    print("  size distribution (unreviewed):", dict(sorted(sz.items())))
    raise SystemExit

# show smallest, highest-signal clusters first (easier, higher-precision), bounded by --max
shown = [c for c in unreviewed if args.min <= len(c) <= args.max]
shown.sort(key=lambda c: (len(c), min(b.bio_id for b in c)))

def line(b):
    tag = "MATCHED " if b.bio_id in matched else "unmatch."
    e = max((edu.get(v, "") for v in b.version_ids), key=len, default="")
    ev = [x for x in b.events if x.year_start]
    career = " | ".join(f"{x.year_start} {x.place or '-'} {(x.position or '')[:34]}" for x in ev[:14])
    hon = ";".join(f"{h.award}{('/'+str(h.year)) if h.year else ''}" for h in b.honours[:6])
    by = f"b.{b.birth_year.value}" if b.birth_year else "b.?"
    term = f" {b.terminal.kind}.{b.terminal.year}" if (b.terminal and b.terminal.year) else ""
    parts = [f"{b.surname}, {b.given_names or '?'}", by]
    if e: parts.append("ed. " + e[:90])
    if hon: parts.append("hon: " + hon)
    parts.append("career: " + (career or "(none)"))
    return (f"  [{tag}] bio={b.bio_id}\n"
            f"      versions={b.version_ids}\n"
            f"      {'; '.join(parts)}{term}")

print(f"# {len(shown)} clusters shown (of {len(unreviewed)} unreviewed); "
      f"ledger has {n_groups} groups\n")
for n, c in enumerate(shown[:args.limit], 1):
    c = sorted(c, key=lambda b: (b.surname, b.given_names or ""))
    print(f"### CLUSTER {n}  ({len(c)} bios, surnames: {sorted({b.surname for b in c})})")
    for b in c:
        print(line(b))
    print()
