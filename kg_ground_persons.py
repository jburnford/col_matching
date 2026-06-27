#!/usr/bin/env python3
"""Ground KG persons (officials) to Wikidata QIDs.

Layer 1: deterministic, zero-FP match against the pre-harvested colonial-officials
set (textasdatacolonialofficelist/wikidata_harvest/merged_all_people.json, 34.6k
Wikidata persons with positions/colonies/dates).

Acceptance tiers (all require name compatibility = exact normalised surname +
matching first given-initial):
  A  unique name candidate AND |KG.birth - WD.birth| <= 1   (needs WD DOB)
  B  unique name candidate AND shared colony (QID or label)
  C  ambiguous name disambiguated to exactly one WD person by colony AND/OR birth

Stage 1 (this run, --stage candidates): emit candidate pairs + the WD QID list
needing DOB.  Stage 2 (--stage finalize): apply fetched DOB, emit accepted matches.
"""
import json, re, collections, argparse, os

ROOT = os.path.dirname(os.path.abspath(__file__))
KG = os.path.join(ROOT, "data/kg/graph_stage3")
HARVEST = "/home/jic823/textasdatacolonialofficelist/wikidata_harvest/merged_all_people.json"
OUT = os.path.join(ROOT, "data/kg")

# ---------- normalisation ----------
def norm_surname(s):
    if not s: return ""
    s = s.upper().replace("'", "").replace("’", "").replace("-", " ")
    return re.sub(r"[^A-Z ]", "", s).strip()

def initials(given):
    if not given: return []
    return [t[0] for t in re.findall(r"[A-Za-z]+", given.upper())]

def norm_label(s):
    if not s: return ""
    return re.sub(r"[^a-z]", "", s.lower())

def given_tokens(given):
    """Full given-name tokens, upper-cased. Initials become single letters."""
    if not given: return []
    return [t.upper() for t in re.findall(r"[A-Za-z]+", given)]

def wd_parse(name):
    toks = re.findall(r"[A-Za-z'’-]+", name)
    if not toks: return "", []
    return norm_surname(toks[-1]), [t.upper() for t in toks[:-1]]

def name_relation(kg_tokens, wd_tokens):
    """Position-wise compare given-name tokens.
    Returns (compatible, conflict, n_full_aligned).
      conflict  -> two full words at the same position disagree (e.g. CAMPBELL vs WILLIAM,
                   or JAMES vs JOHN) -> reject outright.
      compatible-> first initials match and no conflict anywhere.
      n_full_aligned -> count of positions where both are full words and equal (match strength).
    """
    if not kg_tokens or not wd_tokens:
        return False, False, 0
    if kg_tokens[0][0] != wd_tokens[0][0]:
        return False, False, 0
    n_full = 0
    for a, b in zip(kg_tokens, wd_tokens):
        a_full, b_full = len(a) > 1, len(b) > 1
        if a_full and b_full:
            if a != b:
                return False, True, 0       # hard conflict
            n_full += 1
        else:  # at least one is an initial -> compare first letters
            if a[0] != b[0]:
                return False, True, 0       # initial vs full/initial mismatch = conflict
    return True, False, n_full

# ---------- load KG ----------
def load_kg():
    facts = collections.defaultdict(lambda: {"cols": set(), "labels": set()})
    for l in open(os.path.join(KG, "career_facts.jsonl")):
        d = json.loads(l)
        f = facts[d["person_id"]]
        for q in (d.get("place_qid"), d.get("colony_qid")):
            if q: f["cols"].add(q)
        for lab in (d.get("place_label"), d.get("colony_label")):
            if lab: f["labels"].add(norm_label(lab))
    persons = []
    for l in open(os.path.join(KG, "persons.jsonl")):
        d = json.loads(l)
        sur = norm_surname(d.get("surname"))
        if not sur or len(sur) < 2: continue
        f = facts.get(d["person_id"], {"cols": set(), "labels": set()})
        persons.append({
            "pid": d["person_id"], "surname": sur,
            "gtok": given_tokens(d.get("given_names")),
            "birth": d.get("birth_year"),
            "cols": f["cols"], "labels": f["labels"],
            "raw_surname": d.get("surname"), "raw_given": d.get("given_names"),
        })
    return persons

# ---------- load WD harvest ----------
def load_wd():
    wd = json.load(open(HARVEST))
    index = collections.defaultdict(list)
    for p in wd:
        sur, ini = wd_parse(p["name"])
        if not sur: continue
        cols = {pos.get("colony_qid") for pos in p.get("positions", []) if pos.get("colony_qid")}
        labs = {norm_label(pos.get("colony_name")) for pos in p.get("positions", []) if pos.get("colony_name")}
        index[sur].append({
            "qid": p["qid"], "name": p["name"], "gtok": ini,
            "cols": cols, "labels": labs,
            "npos": len(p.get("positions", [])),
        })
    return index

def colony_overlap(kg, wd):
    return bool((kg["cols"] & wd["cols"]) or (kg["labels"] & wd["labels"]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["candidates", "finalize"], default="candidates")
    ap.add_argument("--dob", default=os.path.join(OUT, "wd_person_dob.jsonl"))
    args = ap.parse_args()

    persons = load_kg()
    wd_index = load_wd()
    print(f"KG persons (named): {len(persons)}   WD surnames: {len(wd_index)}")

    candidates = []  # each: dict with pid, qid, tier_signals
    for p in persons:
        cands = []
        for c in wd_index.get(p["surname"], []):
            compat, conflict, n_full = name_relation(p["gtok"], c["gtok"])
            if compat:
                cands.append((c, n_full))
        if not cands:
            continue
        for c, n_full in cands:
            candidates.append({
                "pid": p["pid"], "qid": c["qid"], "wd_name": c["name"],
                "kg_surname": p["raw_surname"], "kg_given": p["raw_given"],
                "kg_birth": p["birth"],
                "colony_match": colony_overlap(p, c),
                "n_full_aligned": n_full,
                "n_name_cands": len(cands),
            })

    if args.stage == "candidates":
        with open(os.path.join(OUT, "person_grounding_candidates.jsonl"), "w") as fo:
            for c in candidates:
                fo.write(json.dumps(c) + "\n")
        qids = sorted({c["qid"] for c in candidates})
        with open(os.path.join(OUT, "wd_person_qids_to_fetch.txt"), "w") as fo:
            fo.write("\n".join(qids) + "\n")
        print(f"candidates: {len(candidates)}  distinct WD QIDs: {len(qids)}")
        print(f"  unique-name candidates: {sum(1 for c in candidates if c['n_name_cands']==1)}")
        print(f"  with colony corroboration: {sum(1 for c in candidates if c['colony_match'])}")
        return

    # finalize: load DOB, apply tiers
    dob = {}
    for l in open(args.dob):
        d = json.loads(l)
        if d.get("year"): dob[d["qid"]] = d["year"]
    accepted = []
    vetoed = 0
    by_pid = collections.defaultdict(list)
    for c in candidates:
        by_pid[c["pid"]].append(c)
    for pid, cs0 in by_pid.items():
        # birth corroboration + contradiction veto per candidate
        cs = []
        for c in cs0:
            wd_y = dob.get(c["qid"])
            c["wd_birth"] = wd_y
            if c["kg_birth"] and wd_y and abs(c["kg_birth"] - wd_y) > 2:
                vetoed += 1            # birth years actively contradict -> drop
                continue
            c["birth_match"] = bool(c["kg_birth"] and wd_y and abs(c["kg_birth"] - wd_y) <= 1)
            cs.append(c)
        if not cs:
            continue
        unique = len(cs) == 1
        # Tier A: unique name + birth match
        a = [c for c in cs if unique and c["birth_match"]]
        # Tier B: unique name + colony
        b = [c for c in cs if unique and c["colony_match"]]
        # Tier C: ambiguous, exactly one disambiguated by birth, OR by colony backed
        # by at least one full given-name agreement (not initials alone).
        disc = [c for c in cs if c["birth_match"]
                or (c["colony_match"] and c.get("n_full_aligned", 0) >= 1)]
        if a:
            a[0]["tier"] = "A"; accepted.append(a[0])
        elif b:
            b[0]["tier"] = "B"; accepted.append(b[0])
        elif not unique and len(disc) == 1:
            disc[0]["tier"] = "C"; accepted.append(disc[0])
    with open(os.path.join(KG, "person_grounding.jsonl"), "w") as fo:
        for c in accepted:
            fo.write(json.dumps({
                "person_id": c["pid"], "qid": c["qid"], "wd_name": c["wd_name"],
                "tier": c["tier"], "kg_surname": c["kg_surname"], "kg_given": c["kg_given"],
                "kg_birth": c["kg_birth"], "wd_birth": c.get("wd_birth"),
                "colony_match": c["colony_match"], "birth_match": c["birth_match"],
            }) + "\n")
    tier_counts = collections.Counter(c["tier"] for c in accepted)
    print(f"ACCEPTED: {len(accepted)}  tiers={dict(tier_counts)}  (birth-contradiction vetoes: {vetoed})")

if __name__ == "__main__":
    main()
