#!/usr/bin/env python3
"""Emit the EMPLOYER / ORGANISATION layer of the KG (v2.1).

Reads the career-event layer + the org grounding cache and writes:
  data/kg/graph_stage3/organisations.jsonl    org nodes (Wikidata QID or colkg:)
  data/kg/graph_stage3/employment_edges.jsonl  person -> org employment attestations

Disposition of each org mention (career event whose place_raw is an employer):
  1. surface is in the grounding cache  -> link to that node (railways, ministries,
     named police/regiments, qualified colonial depts already minted, EAP&T, ...)
  2. surface is a BARE GENERIC department (treasury / secretariat / customs / PWD /
     education dept / ...) with no colony in the string -> RESOLVE per Jim's rule:
       back-track to the person's career colony (nearest career event by sequence
       that carries a resolved colony) and mint a colony-qualified entity
       (colkg:<Colony>_<DeptType>, e.g. colkg:Nigeria_Treasury). When no colony can
       be determined (e.g. a metropolitan UK civil servant), keep it as a bare
       department TYPE on the edge with NO entity link (org_id=null).
  3. surface is uncached and NOT generic (qualified colonial dept, local/colonial org
     with no Wikidata entity, OCR fragment) -> internal-mint colkg:<Slug> and persist
     to the cache (upgradeable to a QID by a later MCP pass, cf. the education layer).

Run:  python3 kg_emit_org.py
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import defaultdict, Counter

GD = Path("data/kg/graph_stage3")
CACHE = Path("data/kg/org_grounding.jsonl")
WORK = Path("data/kg/org_worklist.jsonl")
EVENTS = GD / "career_events.jsonl"

# Same ORG detector used to build the worklist (a place_raw that is an employer).
ORG = re.compile(
    r"\b(railway|railways|R\. ?& ?H|harbour|harbours|posts|telegraph|telegraphs|tels|"
    r"telecom|telecoms|P\. ?& ?T|currency|administration|department|dept|board of|"
    r"regiment|battalion|infantry|artillery|fusiliers|hussars|lancers|"
    r"colonial office|customs|excise|police|constabulary|secretariat|treasury|"
    r"public works|P\.W\.D|survey|surveys|audit|judicial|legal|marine|forestry|"
    r"agriculture|education|medical|sanitary|inland revenue|income tax|inc\. tax|"
    r"war office|foreign office|home office|admiralty|crown agents)\b",
    re.I,
)

# A department-type keyword (the kinds of thing that exist once per colony).
DEPT_KW = re.compile(
    r"\b(treasury|exchequer|currency|secretariat|colonial sec|customs|excise|"
    r"inland rev|inc\. tax|income tax|public works|p\.w\.d|education|board of education|"
    r"medical|sanitary|audit|survey|agricultur|forest|judicial|legal|justice|mines|"
    r"marine|fisheries|finance|immigration|stores|labr|labour|irrign|irrigation|"
    r"district administration|native affairs|war department|general department|"
    r"shipping department|prime minister|external affairs|health department|"
    r"printing|stationery|migration|atty\.?-?gen|appts|passages)\b",
    re.I,
)
# A colony / territory / metropolitan place token -> the surface is QUALIFIED, not bare.
PLACE_TOK = re.compile(
    r"\b(Nigeria|Nigerian|Lagos|Jamaica|J'?ca|Zanzibar|Natal|Transvaal|Union|Colombo|"
    r"Ceylon|Berbice|Corentyne|Malta|Cape|Kenya|Uganda|Tanganyika|Gold Coast|G\.C|"
    r"Sudan|Palestine|Pal\b|Hong Kong|H\.K|Sarawak|Fiji|Trinidad|Mauritius|"
    r"Sierra Leone|Bechuanaland|Basutoland|Swaziland|Rhodesia|S\. ?provs|"
    r"Southern Provinces|N\. ?Nig|S\.A\b|S\. African|South African|N\.S\.W|N\.Z|"
    r"W\. ?Australian|E\. ?Africa|East Africa|British Guiana|B\. ?Guiana|Orange|O\.R\.C|"
    r"Kano|Poona|Pune|Singapore|S'?pore|Federated Malay|F\.M\.S|Mal\.|Malayan|Perak|"
    r"Commonwealth|Louis Trichardt|Westminster|Liverpool|Ontario|Scotch|Scotland|"
    r"Indian|India|Couva|Yilgarn|Weihaiwei|Amani|Guelph|L\. ?Islds|Nig\.|Tang\.|"
    r"S\. ?Leone|Windward|Leeward|Antigua|Dominica|St\.? ?Lucia|Grenada|Barbados|"
    r"Bahamas|Bermuda|Somaliland|Nyasaland|Aden|Cyprus|Egypt|Br\. ?Honduras)",
    # NB: no trailing \b -- many place tokens end in "." (Nig., Tang., F.M.S) where a
    # trailing word-boundary can never match.
    re.I,
)

def clean_colony(lbl: str) -> str:
    """Strip 'Colony'/'Protectorate' boilerplate so 'Colony and Protectorate of
    Nigeria' and 'Kenya Colony Protectorate of' both reduce to a single node name."""
    s = re.sub(r"\b(Colony and Protectorate of|Colony of|Protectorate of)\b", "", lbl, flags=re.I)
    s = re.sub(r"\b(Crown Colony|Colony|Protectorate)\b", "", s, flags=re.I)
    s = re.sub(r"[,&]+", " ", s)
    s = re.sub(r"\s+(and|of)\s*$", "", s, flags=re.I)
    s = re.sub(r"\s+", " ", s).strip(" ,&")
    return s or lbl

def slug(name: str) -> str:
    return "colkg:" + re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", name)).strip("_")

def nrm(s: str) -> str:
    """Match the worklist's surface normalisation (casefold, collapse whitespace,
    drop trailing period) so case/punctuation variants of an event string -- e.g.
    'E.A.R. & H.' -- resolve to the grounded cache row keyed 'E.A.R. & H'."""
    return re.sub(r"\s+", " ", (s or "")).strip().rstrip(".").strip().casefold()

def is_generic_dept(surface: str) -> bool:
    """Bare generic department: a department-type keyword and NO place qualifier."""
    return bool(DEPT_KW.search(surface)) and not PLACE_TOK.search(surface)

def dept_info(surface: str):
    """(type_slug, label_suffix) for a colony-qualified department node."""
    s = surface.lower()
    table = [
        (("audit",), ("audit", "Audit Department")),
        (("exchequer", "treasury", "currency"), ("treasury", "Treasury")),
        (("secretariat", "colonial sec"), ("secretariat", "Secretariat")),
        (("customs", "excise", "inland rev", "inc. tax", "income tax"), ("customs", "Customs")),
        (("public works", "p.w.d"), ("public_works", "Public Works Department")),
        (("education", "board of education"), ("education", "Education Department")),
        (("medical", "sanitary", "health"), ("medical", "Medical Department")),
        (("audit",), ("audit", "Audit Department")),
        (("survey",), ("survey", "Survey Department")),
        (("agricultur",), ("agriculture", "Agriculture Department")),
        (("forest",), ("forestry", "Forest Department")),
        (("judicial", "legal", "justice"), ("judicial", "Judicial Department")),
        (("mines",), ("mines", "Mines Department")),
        (("marine", "fisheries"), ("marine", "Marine Department")),
        (("immigration", "migration"), ("immigration", "Immigration Department")),
        (("police", "constab"), ("police", "Police")),
        (("district administration",), ("administration", "District Administration")),
        (("native affairs",), ("native_affairs", "Native Affairs Department")),
        (("finance",), ("finance", "Finance Department")),
        (("stores",), ("stores", "Stores Department")),
        (("printing", "stationery"), ("printing", "Printing and Stationery Department")),
    ]
    for keys, out in table:
        if any(k in s for k in keys):
            return out
    return ("department", "Department")

def load_jsonl(p):
    return [json.loads(l) for l in p.open()] if p.exists() else []

def main():
    cache = {r["institution"]: r for r in load_jsonl(CACHE)}
    work = {w["institution"]: w for w in load_jsonl(WORK)}
    events = load_jsonl(EVENTS)

    # normalized-surface index so case/punctuation variants of an event string hit
    # the grounded cache row (prefer a Wikidata QID row on collision)
    ncache = {}
    for r in cache.values():
        k = nrm(r["institution"])
        if k not in ncache or (str(r["id"]).startswith("Q") and not str(ncache[k]["id"]).startswith("Q")):
            ncache[k] = r
    # drop stale cache rows shadowed by a better row under the same normalized
    # surface (e.g. an old colkg:E_A_R_H minted before the period-variant fix,
    # now superseded by the grounded 'E.A.R. & H' -> Q1277719 row)
    kept = {inst: r for inst, r in cache.items() if ncache[nrm(inst)] is r}
    if len(kept) < len(cache):
        cache = kept
        with CACHE.open("w") as fh:
            for r in cache.values():
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ---- per-person colony track (seq -> colony) for back-tracking ---------------
    track = defaultdict(list)  # pid -> [(seq, colony_qid, colony_label)]
    for e in events:
        if e.get("colony_qid") and e.get("colony_label"):
            track[e["person_id"]].append((e.get("seq", 0), e["colony_qid"], e["colony_label"]))
    for pid in track:
        track[pid].sort()

    def backtrack_colony(pid, seq):
        """Conservative: trust a colony only when it is unambiguous for this person
        -- either they served in exactly one colony, or an immediately-adjacent
        career event (seq +/-1) carries one. Multi-colony careers with no adjacent
        cue resolve to None (typed-only) rather than risk a wrong colony."""
        cands = track.get(pid)
        if not cands:
            return None
        s = seq if isinstance(seq, int) else 0
        distinct = {c[1] for c in cands}
        if len(distinct) == 1:
            return cands[0][1], cands[0][2]
        adj = [c for c in cands if abs(c[0] - s) <= 1]
        if adj:
            best = min(adj, key=lambda c: (abs(c[0] - s), c[0]))
            return best[1], best[2]
        return None

    # ---- pass 1: internal-mint uncached, non-generic org surfaces ---------------
    # Key by normalized surface so punctuation/case variants mint ONE node and
    # don't shadow a grounded cache row.
    minted = 0
    uncached_norms = {}  # nrm -> representative raw surface
    for e in events:
        raw = e.get("place_raw")
        if not raw or e.get("place_qid") or not ORG.search(raw):
            continue
        k = nrm(raw)
        if k in ncache or is_generic_dept(raw):
            continue
        uncached_norms.setdefault(k, raw)
    for k, surface in uncached_norms.items():
        row = {
            "institution": surface, "type": work.get(surface, {}).get("type", "organisation"),
            "id": slug(surface), "label": surface.strip().rstrip("."),
            "instance_of": [], "country_qid": None,
            "source": "internal", "match_type": "internal_mint",
        }
        cache[surface] = row
        ncache[k] = row
        minted += 1
    if minted:
        with CACHE.open("w") as fh:
            for r in cache.values():
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ---- pass 2: emit edges + collect nodes ------------------------------------
    org_nodes = {}          # id -> node row
    n_people = Counter()    # id -> distinct persons (for n_people)
    seen_person_org = set()
    edges = []
    stat = Counter()

    def use_node(id, label, typ, source, country_qid=None):
        if id not in org_nodes:
            org_nodes[id] = {"id": id, "label": label, "type": typ,
                             "source": source, "country_qid": country_qid}

    for e in events:
        raw = e.get("place_raw")
        if not raw or e.get("place_qid") or not ORG.search(raw):
            continue
        pid, seq = e["person_id"], e.get("seq", 0)
        edge = {"person_id": pid, "seq": seq, "position": e.get("position"),
                "year_start": e.get("year_start"), "year_end": e.get("year_end"),
                "surface": raw}
        r = cache.get(raw) or ncache.get(nrm(raw))
        if r and r.get("source") != "ambiguous":
            # 1. directly grounded / internal-minted org
            use_node(r["id"], r["label"], r.get("type", "organisation"),
                     r["source"], r.get("country_qid"))
            edge.update(org_id=r["id"], org_label=r["label"], org_type=r.get("type"),
                        source=r["source"])
            stat["cached_qid" if str(r["id"]).startswith("Q") else "cached_internal"] += 1
        elif is_generic_dept(raw):
            # 2. bare generic department -> back-track to the person's colony
            dtype, suffix = dept_info(raw)
            col = backtrack_colony(pid, seq)
            if col:
                cq, clabel = col
                cname = clean_colony(clabel)
                label = f"{cname} {suffix}"
                oid = slug(label)
                use_node(oid, label, dtype, "resolved_colony", cq)
                edge.update(org_id=oid, org_label=label, org_type=dtype,
                            source="resolved_colony", colony_qid=cq, colony_label=cname,
                            dept_type=dtype)
                stat["resolved_colony"] += 1
            else:
                # no colony -> bare typed department, no entity
                edge.update(org_id=None, org_label=None, org_type=dtype,
                            source="department_typed", dept_type=dtype)
                stat["department_typed"] += 1
        else:
            # shouldn't happen (pass 1 minted these); guard anyway
            edge.update(org_id=None, org_label=None, org_type="organisation",
                        source="unresolved")
            stat["unresolved"] += 1
        if edge.get("org_id"):
            key = (pid, edge["org_id"])
            if key not in seen_person_org:
                n_people[edge["org_id"]] += 1
                seen_person_org.add(key)
        edges.append(edge)

    for oid, node in org_nodes.items():
        node["n_people"] = n_people[oid]

    with (GD / "organisations.jsonl").open("w") as fh:
        for node in sorted(org_nodes.values(), key=lambda n: -n["n_people"]):
            fh.write(json.dumps(node, ensure_ascii=False) + "\n")
    with (GD / "employment_edges.jsonl").open("w") as fh:
        for ed in edges:
            fh.write(json.dumps(ed, ensure_ascii=False) + "\n")

    # ---- report ----------------------------------------------------------------
    qn = sum(1 for n in org_nodes.values() if str(n["id"]).startswith("Q"))
    rn = sum(1 for n in org_nodes.values() if n["source"] == "resolved_colony")
    inn = sum(1 for n in org_nodes.values() if n["source"] == "internal")
    tot = len(edges)
    linked = sum(v for k, v in stat.items() if k != "department_typed" and k != "unresolved")
    print(f"internal-minted this run: {minted}")
    print(f"org nodes: {len(org_nodes):,}  (Wikidata {qn} / resolved-colony depts {rn} / internal {inn})")
    print(f"employment edges: {tot:,}")
    for k in ["cached_qid", "cached_internal", "resolved_colony", "department_typed", "unresolved"]:
        if stat[k]:
            print(f"  {k:18} {stat[k]:5}  ({100*stat[k]/tot:.1f}%)")
    print(f"edges linked to an entity: {linked:,} ({100*linked/tot:.1f}%); "
          f"typed-only (no colony): {stat['department_typed']:,}")

if __name__ == "__main__":
    main()
