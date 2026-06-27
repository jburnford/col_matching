#!/usr/bin/env python3
"""Layer 2 matching: match our senior officials to WD colony-position holders, zero-FP.

A target person matches a WD holder iff the holder held a senior position for one of the
person's colonies AND:
  - surnames are equal (normalised), AND
  - given names are compatible (first initial equal, no full-word conflict), AND
  - birth years agree within +/-2 if both are present (HARD veto on contradiction), AND
  - the match is UNAMBIGUOUS: exactly one WD holder (across the person's colonies) passes
    the above, and that holder is not claimed by another target person with a conflicting
    name (collision guard).
Birth is not required (many COL entries lack it) -- colony+position+surname is already a
very tight anchor -- but when present it must not contradict.
"""
import json, os, re, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
KG = os.path.join(ROOT, "data/kg")
GD = os.path.join(KG, "graph_stage3")

def norm_sur(s):
    if not s: return ""
    s = s.upper().replace("'", "").replace("’", "").replace("-", " ")
    return re.sub(r"[^A-Z ]", "", s).strip()

def gtok(g):
    return [t.upper() for t in re.findall(r"[A-Za-z]+", g)] if g else []

def wd_split(label):
    # strip trailing peerage/ordinal cruft ("Frederick Lugard, 1st Baron Lugard")
    base = label.split(",")[0]
    toks = re.findall(r"[A-Za-z'’-]+", base)
    if not toks: return "", []
    return norm_sur(toks[-1]), [t.upper() for t in toks[:-1]]

def name_relation(kg_tokens, wd_tokens):
    """(compatible, conflict, n_full_aligned) -- same logic as Layer 1."""
    if not kg_tokens or not wd_tokens: return False, False, 0
    if kg_tokens[0][0] != wd_tokens[0][0]: return False, False, 0
    n_full = 0
    for a, b in zip(kg_tokens, wd_tokens):
        af, bf = len(a) > 1, len(b) > 1
        if af and bf:
            if a != b: return False, True, 0
            n_full += 1
        else:
            if a[0] != b[0]: return False, True, 0
    return True, False, n_full

def main():
    targets = [json.loads(l) for l in open(os.path.join(KG, "l2_targets.jsonl"))]
    # toponym -> holders
    holders_by_top = {}
    for l in open(os.path.join(KG, "l2_wd_holders.jsonl")):
        d = json.loads(l)
        holders_by_top[d["toponym"]] = d["holders"]
    # exclude QIDs already grounded in Layer 1 (avoid double-claim / re-check)
    l1_qids = {json.loads(l)["qid"] for l in open(os.path.join(GD, "person_grounding.verified.jsonl"))}

    proposals = []  # (pid, qid, ...) candidate accepts before collision guard
    for p in targets:
        sur = norm_sur(p["surname"]); kg_g = gtok(p["given"])
        if not sur: continue
        # gather candidate holders across this person's colonies
        cand = {}
        for top in p["toponyms"]:
            for h in holders_by_top.get(top, []):
                wsur, wg = wd_split(h["label"])
                if wsur != sur: continue
                compat, conflict, n_full = name_relation(kg_g, wg)
                if not compat: continue
                # birth veto
                if p["birth"] and h["birth"] and abs(p["birth"] - h["birth"]) > 2:
                    continue
                birth_ok = bool(p["birth"] and h["birth"] and abs(p["birth"] - h["birth"]) <= 2)
                c = cand.setdefault(h["qid"], {
                    "qid": h["qid"], "label": h["label"], "wd_birth": h["birth"],
                    "n_full": n_full, "birth_ok": birth_ok, "positions": set(), "toponyms": set()})
                c["positions"].update(h["positions"]); c["toponyms"].add(top)
                c["n_full"] = max(c["n_full"], n_full); c["birth_ok"] = c["birth_ok"] or birth_ok
        if not cand:
            continue
        cands = list(cand.values())
        # zero-FP: a single holder, OR a single holder confirmed by birth among several
        if len(cands) == 1:
            chosen = cands[0]
        else:
            birth_confirmed = [c for c in cands if c["birth_ok"]]
            chosen = birth_confirmed[0] if len(birth_confirmed) == 1 else None
        if chosen is None:
            continue
        proposals.append({
            "person_id": p["pid"], "qid": chosen["qid"], "wd_name": chosen["label"],
            "kg_surname": p["surname"], "kg_given": p["given"], "kg_birth": p["birth"],
            "wd_birth": chosen["wd_birth"], "birth_ok": chosen["birth_ok"],
            "n_full": chosen["n_full"], "positions": sorted(chosen["positions"]),
            "toponyms": sorted(chosen["toponyms"]),
            "already_l1": chosen["qid"] in l1_qids,
        })

    # collision guard: if one QID is claimed by >1 target with conflicting names, drop all
    byq = collections.defaultdict(list)
    for pr in proposals:
        byq[pr["qid"]].append(pr)
    accepted, dropped = [], []
    for qid, prs in byq.items():
        if len(prs) == 1:
            accepted.append(prs[0]); continue
        toks = [gtok(pr["kg_given"]) for pr in prs]
        conflict = any(name_relation(toks[i], toks[j])[1]
                       for i in range(len(toks)) for j in range(i + 1, len(toks)))
        if conflict:
            for pr in prs: dropped.append({**pr, "drop": "qid_collision"})
        else:
            accepted.extend(prs)  # OCR-variant fragments of same person

    with open(os.path.join(GD, "person_grounding_l2.jsonl"), "w") as f:
        for a in accepted:
            f.write(json.dumps(a) + "\n")
    with open(os.path.join(KG, "person_grounding_l2_dropped.jsonl"), "w") as f:
        for d in dropped:
            f.write(json.dumps(d) + "\n")
    new = [a for a in accepted if not a["already_l1"]]
    print(f"proposals: {len(proposals)}  accepted: {len(accepted)}  collision-dropped: {len(dropped)}")
    print(f"NEW groundings (not already in Layer 1): {len(new)}")
    print(f"  with birth confirmation: {sum(1 for a in new if a['birth_ok'])}")
    print(f"  name-only (no/unknown birth, single colony-position holder): {sum(1 for a in new if not a['birth_ok'])}")

if __name__ == "__main__":
    main()
