#!/usr/bin/env python3
"""Apply live-Wikidata verification to the person grounding -> zero-FP final set.

Two cleanups, both driven by data pulled fresh from WDQS (person_qid_verification.jsonl):

1. OFFICE GATE: drop matches that rest only on a colony string-match (birth_match
   False) AND have no office corroboration (NO_OFFICE flag) -> the cricketer/actor
   namesakes that slipped into the ambiguous colony tier.

2. COLLISION RESOLUTION: when 2+ distinct KG persons map to one QID, cluster them by
   OCR/abbrev-tolerant name identity.  Keep a cluster only if it UNIQUELY contains a
   member whose KG birth == live wd_birth (authoritative).  Otherwise drop the whole
   QID group (genuinely different people we cannot safely separate).
"""
import json, os, collections
from kg_ground_persons import given_tokens, wd_parse, name_relation

ROOT = os.path.dirname(os.path.abspath(__file__))
KG = os.path.join(ROOT, "data/kg/graph_stage3")
GROUNDING = os.path.join(KG, "person_grounding.jsonl")
VERIFY = os.path.join(ROOT, "data/kg/person_qid_verification.jsonl")
CANDS = os.path.join(ROOT, "data/kg/person_grounding_candidates.jsonl")
OUT = os.path.join(KG, "person_grounding.verified.jsonl")
LOG = os.path.join(ROOT, "data/kg/person_grounding_dropped.jsonl")

def name_strength(kg_given, wd_name):
    """(n_name_cands handled separately) -> count of full given tokens that align with WD."""
    _, _, n_full = name_relation(given_tokens(kg_given), wd_parse(wd_name)[1])
    return n_full

def lev(a, b):
    if a == b: return 0
    if not a or not b: return max(len(a), len(b))
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + (ca != cb)))
        prev = cur
    return prev[-1]

def tokens_same_person(ta, tb):
    """True if two given-token lists are the same person allowing OCR / abbreviation
    differences (no GENUINE conflict). Genuine conflict = differing initials, or full
    words that are neither edit-close nor prefix-compatible."""
    if not ta or not tb: return True
    if ta[0][0] != tb[0][0]: return False
    for a, b in zip(ta, tb):
        if a == b: continue
        a_full, b_full = len(a) > 1, len(b) > 1
        if a_full and b_full:
            short, lng = sorted((a, b), key=len)
            if lng.startswith(short): continue            # abbrev / truncation
            if lev(a, b) <= 2: continue                   # OCR spelling
            return False                                  # genuinely different word
        else:  # at least one initial; first letters already known equal here
            if a[0] != b[0]:
                return False                              # differing initials
    return True

def cluster(members):
    """Union-find members into same-person clusters."""
    n = len(members)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    toks = [given_tokens(m["kg_given"]) for m in members]
    for i in range(n):
        for j in range(i+1, n):
            if tokens_same_person(toks[i], toks[j]):
                parent[find(i)] = find(j)
    groups = collections.defaultdict(list)
    for i in range(n):
        groups[find(i)].append(members[i])
    return list(groups.values())

def main():
    rows = [json.loads(l) for l in open(GROUNDING)]
    vmap = {json.loads(l)["qid"]: json.loads(l) for l in open(VERIFY)}
    # n_name_cands per (pid, qid): how many WD persons shared surname+initial (namesake pool)
    ncand = {(c["pid"], c["qid"]): c["n_name_cands"] for c in (json.loads(l) for l in open(CANDS))}
    dropped = []

    # --- gate 1: namesake guard for weakly-anchored, office-less matches ---
    # A match needs a strong anchor (>=2 full given tokens) to survive without office
    # corroboration.  A unique surname can substitute for that anchor -- UNLESS the only
    # Wikidata identity is athlete/entertainer (then a unique surname is no defence: it is
    # just the one cricketer/skater in the pool, not our official).  This trio = birth/
    # colony coincidence with a namesake (Robertson Davies, Alexis Smith, Arthur Nash...).
    SPORT_ENT = ("cricketer", "footballer", "football player", "rugby", "ice hockey",
                 "hockey player", "figure skat", "ice dancer", "actor", "actress", "singer",
                 "musician", "novelist", "athlete", "tennis", "golfer", "olympic",
                 "sportsperson", "comedian", "rules football", "association football")
    kept = []
    for r in rows:
        v = vmap.get(r["qid"], {})
        flags = v.get("flags", [])
        occ = (v.get("occs") or "").lower()
        no_office = "NO_OFFICE" in flags
        has_sport = any(s in occ for s in SPORT_ENT)
        unique_surname = ncand.get((r["person_id"], r["qid"]), 99) == 1
        n_full = name_strength(r["kg_given"], r["wd_name"])
        if no_office and n_full < 2 and (not unique_surname or has_sport):
            dropped.append({**r, "drop_reason": "namesake_no_office",
                            "n_full": n_full, "uniq": unique_surname, "sport": has_sport})
        else:
            kept.append(r)

    # --- gate 2: collision resolution per QID ---
    byq = collections.defaultdict(list)
    for r in kept:
        byq[r["qid"]].append(r)
    final = []
    for qid, members in byq.items():
        if len(members) == 1:
            final.append(members[0]); continue
        clusters = cluster(members)
        if len(clusters) == 1:
            final.extend(members); continue              # all same person (OCR variants)
        wd_birth = vmap.get(qid, {}).get("live_birth")
        # which clusters contain an EXACT wd_birth match?
        def has_exact(cl):
            return wd_birth is not None and any(m["kg_birth"] == wd_birth for m in cl)
        exact_clusters = [cl for cl in clusters if has_exact(cl)]
        if len(exact_clusters) == 1:
            for cl in clusters:
                if cl is exact_clusters[0]:
                    final.extend(cl)
                else:
                    for m in cl:
                        dropped.append({**m, "drop_reason": "collision_loser",
                                        "wd_birth": wd_birth})
        else:
            for m in members:
                dropped.append({**m, "drop_reason": "collision_ambiguous",
                                "wd_birth": wd_birth})

    with open(OUT, "w") as fo:
        for r in final:
            fo.write(json.dumps(r) + "\n")
    with open(LOG, "w") as fo:
        for r in dropped:
            fo.write(json.dumps(r) + "\n")

    dr = collections.Counter(d["drop_reason"] for d in dropped)
    tiers = collections.Counter(r["tier"] for r in final)
    print(f"input matches: {len(rows)}")
    print(f"dropped: {len(dropped)}  {dict(dr)}")
    print(f"FINAL verified matches: {len(final)}  tiers={dict(tiers)}")
    print(f"distinct QIDs: {len({r['qid'] for r in final})}")

if __name__ == "__main__":
    main()
