#!/usr/bin/env python3
"""Apply the OLD pipeline's proven cross-edition TEXT-CHAINING dedup
(col_match/services/dedup.py) to the new-KG bios, to fix the under-merging that
left 79% of KG persons single-edition. Reuses the exact gates/blocking — only
the I/O is adapted (KG bio dicts instead of RawEntry).

Reports the true distinct-entry count (target ~30k from the old run) and how many
current persons.jsonl records collapse together.

  python3 kg_textchain_dedup.py [--write persons.deduped.jsonl] [--review merges.txt]
"""
from __future__ import annotations
import argparse, json, glob, re
from collections import defaultdict
from col_match.services.dedup import surname_key, first_initial, _same_version
from col_match.kg.paths import kg_out

ap = argparse.ArgumentParser()
ap.add_argument("--write", default="")
ap.add_argument("--review", default="")
args = ap.parse_args()

KG = str(kg_out())
# load all bios + current person mapping
bios = []
for f in glob.glob(f"{KG}/bios/*.jsonl"):
    if ".xref" in f:
        continue
    for l in open(f):
        bios.append(json.loads(l))
P = [json.loads(l) for l in open(f"{KG}/persons.jsonl")]
bio2pid = {bid: p["person_id"] for p in P for bid in p.get("attestation_bio_ids", [])}
pid_by = {p["person_id"]: p for p in P}

# chain within (surname_key, first_initial) blocks, chronologically
blocks = defaultdict(list)
for b in bios:
    t = b["raw_text"]
    blocks[f"{surname_key(t)}|{first_initial(t)}"].append(b)

chains_all = []
for key, members in blocks.items():
    members.sort(key=lambda b: (b["edition_year"], b["bio_id"]))
    chains = []
    for b in members:
        best = None
        for ch in chains:
            tail = ch[-1]
            if tail["edition_year"] == b["edition_year"]:
                continue
            if _same_version(tail["raw_text"], b["raw_text"]):
                best = ch; break
        if best is not None:
            best.append(b)
        else:
            chains.append([b])
    chains_all.extend(chains)

versions = len(chains_all)
sing4 = sum(1 for ch in chains_all if len(ch) == 1)
print(f"bios {len(bios):,} -> distinct entry-chains {versions:,}  ({len(bios)/versions:.2f}x collapse)")
print(f"  single-edition chains: {sing4:,} ({100*sing4/versions:.0f}%)  [was 79% under name+birth clustering]")

# how many CURRENT persons collapse together
person_collapse = []   # chains spanning >1 current person_id
covered = 0
for ch in chains_all:
    pids = {bio2pid.get(b["bio_id"]) for b in ch} - {None}
    if len(pids) >= 2:
        person_collapse.append((ch, pids))
excess = sum(len(p) - 1 for _, p in person_collapse)
print(f"  chains spanning >1 current person_id: {len(person_collapse):,}")
print(f"  -> {excess:,} excess person records collapse ({len(P):,} -> ~{len(P)-excess:,})")

if args.review:
    with open(args.review, "w") as fh:
        for ch, pids in sorted(person_collapse, key=lambda x: -len(x[1]))[:400]:
            head = ch[0]["raw_text"][:70].replace("\n", " ")
            fh.write(f"=== {len(pids)} persons, {len(ch)} bios | {head}\n")
            for b in sorted(ch, key=lambda b: b["edition_year"]):
                fh.write(f"    {b['edition_year']} {b['bio_id']:24s} {b['raw_text'][:90].strip()}\n")
            fh.write("\n")
    print(f"  wrote merge-review sample -> {args.review}")

if args.write:
    # emit one deduped person per chain: richest (most years*100+len) bio = canonical
    YEAR = re.compile(r"\b1[789]\d\d\b")
    def rich(b): return len(YEAR.findall(b["raw_text"])) * 100 + len(b["raw_text"])
    with open(args.write, "w") as fh:
        for ch in chains_all:
            canon = max(ch, key=rich)
            fh.write(json.dumps({
                "person_id": "kgp_" + canon["bio_id"],
                "surname": canon.get("surname") or canon["raw_text"].split(",", 1)[0],
                "given_names": canon.get("given_names"),
                "birth_year": next((b.get("birth_year") for b in ch if b.get("birth_year")), None),
                "editions": sorted({b["edition_year"] for b in ch}),
                "canonical_bio_id": canon["bio_id"],
                "canonical_edition": canon["edition_year"],
                "n_attestations": len(ch),
                "attestation_bio_ids": [b["bio_id"] for b in ch],
            }, ensure_ascii=False) + "\n")
    print(f"  wrote deduped persons -> {args.write}")
