#!/usr/bin/env python3
"""Audit place groundings for OBVIOUS misgroundings by comparing the raw OCR
surface string to the grounded Wikidata label, and by flagging colony rollups
that are geographically inconsistent (a Caribbean place landing in Cyprus).

Two independent checks, tuned for PRECISION (errors are rare; minimise noise):

  A. surface vs place-label mismatch -- the grounded entity's name shares nothing
     with the surface, and it is not a known abbreviation, OCR variant, or modern
     rename (Calcutta->Kolkata). High-confidence place misgroundings.
  B. colony geo-outlier -- the place's modern country (P17) disagrees with the
     dominant country of every other place in the same colony (Saint Vincent,
     country Q757, sitting in the Cyprus colony whose places are all Q229).

Read-only; prints a review list. Run from repo root.
"""
from __future__ import annotations
import json, re, difflib, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GEO = json.loads((ROOT / "data/kg/place_geo_chain.json").read_text())

# modern rename / historical-name pairs that legitimately differ from the surface
RENAMES = [
    ("kolkata", "calcutta"), ("mumbai", "bombay"), ("chennai", "madras"),
    ("yangon", "rangoon"), ("prayagraj", "allahabad"), ("varanasi", "benares"),
    ("kanpur", "cawnpore"), ("pune", "poona"), ("kochi", "cochin"),
    ("thiruvananthapuram", "trivandrum"), ("kozhikode", "calicut"),
    ("awadh", "oudh"), ("gqeberha", "port elizabeth"), ("makhanda", "grahamstown"),
    ("polokwane", "pietersburg"), ("thoothukudi", "tuticorin"), ("vadodara", "baroda"),
    ("mangaluru", "mangalore"), ("shimla", "simla"), ("puducherry", "pondicherry"),
    ("yangon", "rangoon"), ("guangzhou", "canton"), ("ujungpandang", "makassar"),
    ("harare", "salisbury"), ("maputo", "lourenco marques"), ("kinshasa", "leopoldville"),
    ("dhaka", "dacca"), ("chattogram", "chittagong"), ("vijayawada", "bezwada"),
    ("prayagraj district", "allahabad"), ("kolkata district", "calcutta"),
    ("george town", "georgetown"), ("yangon region", "rangoon"),
]
_RENAME = {a: b for a, b in RENAMES}
_RENAME.update({b: a for a, b in RENAMES})

_DROP = {"district", "province", "provinces", "colony", "region", "settlement",
         "presidency", "state", "territory", "territories", "island", "islands",
         "the", "of", "and", "city", "town", "fort", "saint", "st", "san",
         "north", "south", "east", "west", "western", "eastern", "northern",
         "southern", "central", "upper", "lower", "new", "old", "british",
         "protectorate", "crown", "company", "dependency"}
_PUNCT = re.compile(r"[^a-z0-9 ]")


def norm(s):
    return _PUNCT.sub(" ", (s or "").lower()).split()


def core(s):
    """Significant tokens (drop generic qualifiers)."""
    return [t for t in norm(s) if t not in _DROP and len(t) > 1]


def plausible(surface, label):
    """True if surface and grounded label plausibly name the same place."""
    s_all, l_all = norm(surface), norm(label)
    if not s_all or not l_all:
        return True                                   # nothing to compare
    s_str, l_str = " ".join(s_all), " ".join(l_all)
    sc, lc = set(core(surface)), set(core(label))
    # 1. shared significant token
    if sc & lc:
        return True
    # 2. shared 4+ char token even if generic
    if {t for t in s_all if len(t) >= 4} & {t for t in l_all if len(t) >= 4}:
        return True
    # 3. abbreviation: a surface token is a prefix of a label token (Cyp.->Cyprus)
    for st in s_all:
        for lt in l_all:
            if len(st) >= 2 and (lt.startswith(st) or st.startswith(lt)):
                return True
    # 4. known rename
    for t in sc | {s_str}:
        if _RENAME.get(t) and _RENAME[t] in (lc | {l_str}):
            return True
    # 5. fuzzy (OCR): Limasol/Limassol, Nikosia/Nicosia
    if difflib.SequenceMatcher(None, s_str, l_str).ratio() >= 0.7:
        return True
    if sc and lc and max(difflib.SequenceMatcher(None, a, b).ratio()
                         for a in sc for b in lc) >= 0.82:
        return True
    # 6. initialism: surface letters == first letters of label words (B.G.->British
    #    Guiana, G.E.A.->German East Africa, T.T.->Tanganyika Territory)
    s_letters = re.sub(r"[^a-z]", "", surface.lower())
    l_initials = "".join(w[0] for w in l_all)
    if 2 <= len(s_letters) <= 5 and s_letters in (l_initials, l_initials.replace("the", "")):
        return True
    if len(s_letters) >= 2 and l_initials.startswith(s_letters):
        return True
    return False


def main():
    rows = []
    for corpus, path in (("CO", "data/kg/graph_stage3/places.jsonl"),
                         ("IOL", "data/iol/graph_stage3/places.jsonl")):
        for l in (ROOT / path).open():
            d = json.loads(l)
            d["_corpus"] = corpus
            rows.append(d)

    # ---- Check A: surface vs place label ------------------------------------
    print("=" * 70)
    print("CHECK A — surface string vs grounded Wikidata place label")
    print("=" * 70)
    flagged_a = []
    seen = set()
    for d in rows:
        surf, lab, qid = d["place"], d.get("label"), d.get("qid")
        if not qid or not lab:
            continue
        # the vetted qid_manifest groundings are trusted (curated colony abbrevs);
        # genuine misgroundings live in the MCP-grounded tail.
        if (d.get("match_type") or "").startswith("manifest"):
            continue
        key = (surf, qid)
        if key in seen:
            continue
        seen.add(key)
        if not plausible(surf, lab):
            flagged_a.append(d)
    for d in sorted(flagged_a, key=lambda x: -(x.get("count") or 0)):
        print(f"  [{d['_corpus']}] {d['place']!r:34} -> {d.get('label')!r:30} "
              f"{d.get('qid')}  (n={d.get('count')}, {d.get('match_type')})")
    print(f"  CHECK A flags: {len(flagged_a)}")

    # ---- Check B: colony geo-outlier ---------------------------------------
    print("\n" + "=" * 70)
    print("CHECK B — place country (P17) inconsistent with its colony")
    print("=" * 70)
    by_colony = collections.defaultdict(list)
    for d in rows:
        if d.get("qid") and d.get("colony_qid"):
            by_colony[d["colony_qid"]].append(d)
    flagged_b = []
    for cq, members in by_colony.items():
        ctry = collections.Counter()
        for d in members:
            c = (GEO.get(d["qid"]) or {}).get("country")
            if c:
                ctry[c] += d.get("count") or 1
        if not ctry:
            continue
        modal, modal_n = ctry.most_common(1)[0]
        total = sum(ctry.values())
        if modal_n / total < 0.6:
            continue                                  # genuinely multi-country colony
        for d in members:
            c = (GEO.get(d["qid"]) or {}).get("country")
            if c and c != modal:
                flagged_b.append((d, c, modal, members[0].get("colony_label")))
    for d, c, modal, clabel in sorted(flagged_b, key=lambda x: -(x[0].get("count") or 0)):
        print(f"  [{d['_corpus']}] {d['place']!r:26} ({d.get('label')}) country={c} "
              f"-> colony {clabel!r} (modal country {modal})  n={d.get('count')}")
    print(f"  CHECK B flags: {len(flagged_b)}")


if __name__ == "__main__":
    main()
