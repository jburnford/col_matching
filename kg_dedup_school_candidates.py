#!/usr/bin/env python3
"""School-blocked person-dedup CANDIDATE GENERATOR (review-only, no mutation).

The education atlas surfaced dupes that role+colony+year blocking
([[kg-roleyear-peerage-dedup]]) split apart, because they never shared a job at
a place in a year: peerage-title surname swaps (STANLEY/DERBY), OCR (ST./SR.
JOHN BRODRICK), and cross-edition supplement splits (WALPOLE Horace G.×2).
Shared SCHOOL co-locates them — but a school spans generations, so this blocker
is NOT self-protecting like role+colony+year. Fathers and sons attend the same
school (Eton holds the whole Derby dynasty), so every candidate is scored for
father/son risk and the script ONLY writes a review file — it never touches the
merge map. Apply (after hand review) is a separate step.

Reuses the matching contract of kg_dedup_roleyear.py (rank/honorific-stripped,
OCR-tolerant token-subset; birth-year conflict >2 vetoes). Env COL_KG_OUT.
"""
import json, re, unicodedata
from collections import defaultdict
from rapidfuzz.distance import Levenshtein
from col_match.kg.paths import KG_OUT
lev = Levenshtein.distance

_LIG = {"œ": "oe", "Œ": "oe", "æ": "ae", "Æ": "ae", "ø": "o", "Ø": "o", "ß": "ss"}
def _fold(s):
    for k, v in _LIG.items():
        s = s.replace(k, v)
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))

RANK = {"earl","marquess","marquis","viscount","viscountess","baron","baroness","baronet",
 "bart","lord","lady","duke","duchess","count","countess","of","the","sir","dame","rt",
 "right","hon","honorary","honourable","formerly","first","second","third",
 "rai","bahadur","sahib","sahibzada","nawabzada","kunwar","pandit","babu","mirza",
 "maulvi","munshi","khan","nawab","begum","diwan","dewan","qanungo","kanungo","raja",
 "rajah","sri","srijat","brod","mst","mr","mrs","miss","esq","kt","cie","csi","maung"}

def toks(p):
    s = _fold(((p.get("surname") or "") + " " + (p.get("given_names") or ""))).lower()
    return [t for t in re.split(r"[^a-z0-9]+", s) if t and t not in RANK and len(t) > 1]
def tin(t, S): return any(t == u or (len(t) >= 4 and len(u) >= 4 and lev(t, u) <= 1) for u in S)
def match(A, B):
    TA, TB = set(toks(A)), set(toks(B))
    if len(TA) < 2 or len(TB) < 2: return False
    small, big = (TA, TB) if len(TA) <= len(TB) else (TB, TA)
    shared = [t for t in small if tin(t, big)]
    return len(shared) >= 2 and len(shared) / len(small) >= 0.75 and any(len(t) >= 4 for t in shared)
def bconf(A, B):
    a, b = A.get("birth_year"), B.get("birth_year"); return bool(a and b and abs(a - b) > 2)
def bmatch(A, B):
    a, b = A.get("birth_year"), B.get("birth_year"); return bool(a and b and abs(a - b) <= 2)


def load_resolver(root):
    m = {}
    for f in root.glob("dedup_stage3_merge_map*.jsonl"):
        if "bak" in f.name or "_v2" in f.name: continue
        for l in f.open():
            d = json.loads(l)
            if d["person_id"] != d["canonical_person_id"]:
                m[d["person_id"]] = d["canonical_person_id"]
    def res(pid):
        seen = set()
        while pid in m and pid not in seen:
            seen.add(pid); pid = m[pid]
        return pid
    return res


def main():
    persons = {p["person_id"]: p for p in (json.loads(l) for l in open(KG_OUT / "graph_stage3/persons.jsonl"))}
    resolve = load_resolver(KG_OUT)

    # person -> grounded schools (resolved to canonical)
    school_alumni = defaultdict(set)
    for l in open(KG_OUT / "graph_stage3/education_edges.jsonl"):
        d = json.loads(l); iid = d.get("institution_id") or ""
        if not iid.startswith("Q"): continue
        pid = resolve(d["person_id"])
        if pid in persons:
            school_alumni[iid].add(pid)

    # appointment keys per person (a shared year-anchored posting = strong
    # same-person signal). Tolerant of edition wording/place drift: index BOTH
    # (role-stem, year) and (place, year) so "outbreak of plague @ — 1897" and
    # "epidemics of plague @ Ceylon 1897" still coincide (the Fernando case).
    def rstem(r): return re.sub(r"[^a-z]", "", (r or "").lower())[:10]
    appt = defaultdict(set)
    cf = KG_OUT / "graph_stage3/career_facts.jsonl"
    ce = KG_OUT / "graph_stage3/career_events.jsonl"
    src = cf if cf.exists() else ce
    for l in open(src):
        d = json.loads(l)
        role = d.get("role_label") or d.get("position_norm")
        place = d.get("colony_qid") or d.get("place_qid")
        y = d.get("year_start")
        if not y: continue
        if role: appt[d["person_id"]].add(("r", rstem(role), y))
        if place: appt[d["person_id"]].add(("p", place, y))

    # candidate pairs within each school block
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    pair_ev = {}
    for iid, pids in school_alumni.items():
        pl = sorted(pids)
        if len(pl) < 2: continue
        for i in range(len(pl)):
            for j in range(i + 1, len(pl)):
                a, b = pl[i], pl[j]
                A, B = persons[a], persons[b]
                if bconf(A, B) or not match(A, B): continue
                key = (a, b)
                if key not in pair_ev:
                    shared_appt = bool(appt[a] & appt[b])
                    ea, eb = A.get("editions") or [], B.get("editions") or []
                    overlap = bool(ea and eb and not (max(ea) < min(eb) - 3 or max(eb) < min(ea) - 3))
                    pair_ev[key] = {"birth_match": bmatch(A, B), "shared_appt": shared_appt,
                                    "edition_overlap": overlap, "school": iid}
                if find(a) != find(b): parent[find(a)] = find(b)

    clusters = defaultdict(list)
    for p in list(parent): clusters[find(p)].append(p)
    clusters = [sorted(m) for m in clusters.values() if len(m) > 1]

    # classify each cluster by father/son risk
    def cluster_disposition(members):
        # cluster-level birth conflict: union-find can chain members through a
        # missing-birth intermediary into an over-merge (Chalmers b1859+b1869).
        births = [persons[p].get("birth_year") for p in members if persons[p].get("birth_year")]
        if births and max(births) - min(births) > 2:
            return "conflict"                    # over-merge / father-son — likely SPLIT
        bm = sa = ov = False
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                ev = pair_ev.get((members[i], members[j]))
                if not ev: continue
                bm |= ev["birth_match"]; sa |= ev["shared_appt"]; ov |= ev["edition_overlap"]
        if bm or sa: return "confident"          # matched birth year or shared a posting
        if ov: return "likely"                   # overlapping/adjacent edition runs
        return "review"                          # possible father/son or distinct — needs eyes

    out, counts = [], defaultdict(int)
    for m in clusters:
        disp = cluster_disposition(m)
        counts[disp] += 1
        schools = set()
        for i in range(len(m)):
            for j in range(i + 1, len(m)):
                ev = pair_ev.get((m[i], m[j]))
                if ev: schools.add(ev["school"])
        out.append({
            "disposition": disp,
            "members": [{
                "id": p, "surname": persons[p].get("surname"),
                "given": persons[p].get("given_names"), "birth": persons[p].get("birth_year"),
                "editions": [min(persons[p]["editions"]), max(persons[p]["editions"])] if persons[p].get("editions") else None,
                "n": persons[p].get("n_attestations"),
            } for p in m],
            "schools": sorted(schools),
        })
    order = {"conflict": 0, "review": 1, "confident": 2, "likely": 3}
    out.sort(key=lambda c: (order[c["disposition"]], -len(c["members"])))

    fn = KG_OUT / "dedup_school_candidates.jsonl"
    with open(fn, "w") as fh:
        for c in out: fh.write(json.dumps(c) + "\n")
    print(f"{KG_OUT}: school-blocked candidate clusters = {len(out)}  "
          f"(conflict {counts['conflict']} / review {counts['review']} / "
          f"confident {counts['confident']} / likely {counts['likely']})")
    print(f"  records involved: {sum(len(c['members']) for c in out)}  ->  {fn.name}")
    for bucket in ("conflict", "review"):
        ex = [c for c in out if c["disposition"] == bucket]
        if ex:
            print(f"  {bucket} clusters (need eyes):")
            for c in ex[:10]:
                nm = " | ".join(f"{x['surname']},{(x['given'] or '')[:16]}(b{x['birth'] or '?'},{x['editions']})" for x in c["members"])
                print(f"    {nm}")


if __name__ == "__main__":
    main()
