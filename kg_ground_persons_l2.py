#!/usr/bin/env python3
"""Layer 2: ground senior colonial officials (governors / colonial secretaries / chief
justices) to Wikidata by anchoring on COLONY + POSITION -- the structured discriminator.

For each colony in our target set we ask Wikidata (QLever) for every human who held a
"Governor / Colonial Secretary / Administrator / Chief Justice ... of <colony>" position.
Position+colony is extremely specific, so a surname match inside that holder set is
near-unique and zero-FP.  We then gate hard on birth-year agreement / given-name conflict.

  stage targets   -> data/kg/l2_targets.jsonl       (our senior officials + colonies)
  stage fetch     -> data/kg/l2_wd_holders.jsonl    (WD position holders per toponym)
  stage match     -> data/kg/graph_stage3/person_grounding_l2.jsonl
"""
import json, re, os, collections, argparse, urllib.request, time, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
KG = os.path.join(ROOT, "data/kg")
GD = os.path.join(KG, "graph_stage3")
QLEVER = "https://qlever.dev/api/wikidata"
PFX = ("PREFIX wd: <http://www.wikidata.org/entity/> "
       "PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
       "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> ")

SENIOR = re.compile(r"governor|colonial administrator|administrator of the government|"
                    r"colonial secretary|chief secretary|chief justice", re.I)
EXCLUDE = re.compile(r"private secretary|ps and adc|adc and ps|administrator general|"
                     r"administrator-general|administrator of native law", re.I)

def is_senior(role):
    return bool(role) and SENIOR.search(role) and not EXCLUDE.search(role)

# strip colony qualifiers -> core toponym for matching WD position labels
def toponym(label):
    if not isinstance(label, str) or not label.strip(): return None
    s = label
    s = re.sub(r"\b(Colony and Protectorate of|Protectorate of|Dominion of|"
               r"Commonwealth of|Colony of|Province of)\b", "", s, flags=re.I)
    s = re.sub(r"\b(British|Colony|Protectorate|Dominion|Crown)\b", "", s, flags=re.I)
    s = re.sub(r"\s+", " ", s).strip(" ,")
    return s or None

def norm_sur(s):
    if not s: return ""
    s = s.upper().replace("'", "").replace("’", "").replace("-", " ")
    return re.sub(r"[^A-Z ]", "", s).strip()

def gtok(g):
    return [t.upper() for t in re.findall(r"[A-Za-z]+", g)] if g else []

def qlever(q):
    req = urllib.request.Request(QLEVER, data=(PFX + q).encode(),
        headers={"Accept": "application/sparql-results+json",
                 "Content-type": "application/sparql-query"})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=120))["results"]["bindings"]
        except Exception as e:
            print(f"    retry {attempt}: {e}", file=sys.stderr); time.sleep(4 * (attempt + 1))
    return []

# ---------------------------------------------------------------- targets
def build_targets():
    import ladybug
    db = ladybug.Database(os.path.join(KG, "ladybug_db")); conn = ladybug.Connection(db)
    df = conn.execute("""
    MATCH (p:Person)-[:HAS_EVENT]->(e:CareerEvent)-[:EVENT_ROLE]->(r:Role)
    WHERE p.wikidata_qid='' AND (r.label CONTAINS 'overnor' OR r.label CONTAINS 'dministrator'
       OR r.label CONTAINS 'olonial Secretary' OR r.label CONTAINS 'hief Justice')
    OPTIONAL MATCH (e)-[:EVENT_PLACE]->(pl:Place)
    OPTIONAL MATCH (e)-[:EVENT_COLONY]->(cl:Place)
    RETURN p.person_id AS pid, p.surname AS sur, p.given_names AS giv, p.birth_year AS birth,
           r.label AS role, e.year_start AS ys, e.year_end AS ye,
           pl.label AS place_label, cl.label AS colony_label
    """).get_as_df()
    persons = {}
    for _, r in df.iterrows():
        if not is_senior(r.role):
            continue
        p = persons.setdefault(r.pid, {
            "pid": r.pid,
            "surname": r.sur if isinstance(r.sur, str) else None,
            "given": r.giv if isinstance(r.giv, str) else None,
            "birth": int(r.birth) if r.birth == r.birth else None,
            "roles": set(), "toponyms": set(), "years": set()})
        p["roles"].add(r.role)
        for lab in (r.colony_label, r.place_label):
            t = toponym(lab)
            if t and len(t) > 2:
                p["toponyms"].add(t)
        for y in (r.ys, r.ye):
            if y == y and y: p["years"].add(int(y))
    out = []
    for p in persons.values():
        if not p["surname"] or not p["toponyms"]:
            continue
        p["roles"] = sorted(p["roles"]); p["toponyms"] = sorted(p["toponyms"])
        p["years"] = sorted(p["years"])
        out.append(p)
    with open(os.path.join(KG, "l2_targets.jsonl"), "w") as f:
        for p in out:
            f.write(json.dumps(p) + "\n")
    tops = collections.Counter(t for p in out for t in p["toponyms"])
    print(f"senior targets: {len(out)} persons, {len(tops)} distinct toponyms")
    print("top toponyms:", tops.most_common(12))

# ---------------------------------------------------------------- fetch holders
def fetch_holders():
    targets = [json.loads(l) for l in open(os.path.join(KG, "l2_targets.jsonl"))]
    tops = sorted({t for p in targets for t in p["toponyms"]})
    out = os.path.join(KG, "l2_wd_holders.jsonl")
    done = set()
    if os.path.exists(out):
        for l in open(out):
            done.add(json.loads(l)["toponym"])
    todo = [t for t in tops if t not in done]
    print(f"{len(tops)} toponyms, {len(done)} cached, {len(todo)} to fetch")
    fo = open(out, "a")
    for i, top in enumerate(todo):
        esc = top.replace('"', '').replace("\\", "")
        q = (f'SELECT ?person ?personLabel ?dob ?posLabel WHERE {{ '
             f'?pos rdfs:label ?posLabel . FILTER(LANG(?posLabel)="en") '
             f'FILTER(CONTAINS(?posLabel,"{esc}")) '
             f'FILTER(CONTAINS(?posLabel,"Governor") || CONTAINS(?posLabel,"Secretary") || '
             f'CONTAINS(?posLabel,"Administrator") || CONTAINS(?posLabel,"Chief Justice")) '
             f'?person wdt:P39 ?pos ; wdt:P31 wd:Q5 ; rdfs:label ?personLabel . '
             f'FILTER(LANG(?personLabel)="en") OPTIONAL {{ ?person wdt:P569 ?dob }} }} LIMIT 500')
        rows = qlever(q)
        holders = {}
        for b in rows:
            qid = b["person"]["value"].rsplit("/", 1)[-1]
            dobv = b.get("dob", {}).get("value", "")
            yr = None
            if dobv:
                neg = dobv.startswith("-")
                try: yr = (-1 if neg else 1) * int(dobv.lstrip("-").split("-")[0])
                except ValueError: pass
            h = holders.setdefault(qid, {"qid": qid, "label": b["personLabel"]["value"],
                                          "birth": yr, "positions": set()})
            h["positions"].add(b["posLabel"]["value"])
        for h in holders.values():
            h["positions"] = sorted(h["positions"])
        fo.write(json.dumps({"toponym": top, "holders": list(holders.values())}) + "\n")
        fo.flush()
        print(f"  [{i+1}/{len(todo)}] {top:28} -> {len(holders)} holders")
        time.sleep(0.5)
    fo.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["targets", "fetch", "match"])
    args = ap.parse_args()
    if args.stage == "targets": build_targets()
    elif args.stage == "fetch": fetch_holders()
    elif args.stage == "match": import kg_ground_persons_l2_match  # noqa
