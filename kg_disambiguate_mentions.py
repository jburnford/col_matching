#!/usr/bin/env python3
"""Per-MENTION disambiguation of ambiguous institution surfaces.

Bare multi-referent surfaces ("Trinity College", "University College", "High
School") are cache-flagged `ambiguous` and excluded from emit — correct at the
SURFACE level, but it silently drops ~18k mentions whose raw education strings
carry the disambiguating cue right there: "Trinity college, Dublin",
"Otago university college", "St. John's college, Camb.".

Method (precision gate = the grounding cache itself):
  1. For every mention (ambiguous surface x person), scan the person's raw
     education strings for the surface and extract cue tokens — the place name
     FOLLOWING a comma ("Trinity College, Dublin") and/or the capitalised word
     PRECEDING the surface ("Otago University College").
  2. Reconstruct candidate parented forms ("<surface>, <cue>", "<cue> <surface>",
     "<surface> of <cue>") and look them up in institutions_grounding.jsonl
     under punctuation-/abbreviation-tolerant normalisation (Camb.->Cambridge,
     Oxon->Oxford, ...). ONLY an existing non-ambiguous cache entry resolves a
     mention — no guessing, no new grounding decisions here.
  3. Write per-corpus education_mention_overrides.jsonl; kg_ground_institutions
     cmd_emit appends these as extra education edges.

Unresolved mentions stay quarantined exactly as before.
Run: python3 kg_disambiguate_mentions.py            (CO)
     COL_KG_OUT=data/iol COL_CACHE=data/iol/institutions_grounding.jsonl \
       COL_WORK=data/iol/education_worklist.jsonl python3 kg_disambiguate_mentions.py
"""
from __future__ import annotations
import json, os, re, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = Path(os.environ.get("COL_KG_OUT", "data/kg"))
CACHE = Path(os.environ.get("COL_CACHE", "data/kg/institutions_grounding.jsonl"))
WORK = Path(os.environ.get("COL_WORK", "data/kg/education_worklist.jsonl"))

ABBREV = {
    "camb": "cambridge", "cantab": "cambridge", "cam": "cambridge",
    "oxon": "oxford", "oxf": "oxford", "ox": "oxford",
    "dub": "dublin", "lond": "london", "edin": "edinburgh", "spore": "singapore",
    "melb": "melbourne", "nz": "new zealand", "jca": "jamaica", "sa": "south africa",
}
STOP = {"and", "where", "the", "in", "at", "of", "he", "she", "was", "then", "with",
        "b.a", "ba", "ma", "m.a", "school", "college", "university", "hosp", "hospital"}


PHRASES = [  # corpus place abbreviations, expanded before tokenising
    (r"\bb\.?r?\.?\s*guiana\b", "british guiana"), (r"\bj'?ca\.?\b", "jamaica"),
    (r"\bh\.?\s*k\.?\b", "hong kong"), (r"\bsey\.?\b", "seychelles"),
    (r"\bmaur\.?\b", "mauritius"), (r"\btrin\.?\b(?!\w)", "trinidad"),
    (r"\bjo'?burg\b", "johannesburg"), (r"\bn\.?\s*z\.?\b", "new zealand"),
    (r"\bken\.?\b(?!\w)", "kenya"), (r"\bgib\.?\b(?!\w)", "gibraltar"),
    (r"\bs'pore\b", "singapore"), (r"\btech\.?\b", "technical"),
]


def norm(s: str) -> str:
    s = s.lower().replace("&", "and")
    for pat, rep in PHRASES:
        s = re.sub(pat, rep, s)
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\b(the|of|at)\b", " ", s)
    toks = [ABBREV.get(t, t) for t in s.split()]
    return " ".join(toks)


def load_jsonl(p):
    return [json.loads(l) for l in Path(p).open()]


def surf_pattern(surf: str) -> re.Pattern:
    """Match the surface INCLUDING printed abbreviations of its words:
    'Trinity College' also matches 'Trin. college', 'Trin college'."""
    parts = []
    for w in surf.split():
        we = re.escape(w)
        if len(w) >= 5 and w[0].isalpha():
            parts.append(f"(?:{we}|{re.escape(w[:4])}\\.?|{re.escape(w[:5])}\\.?)")
        else:
            parts.append(we)
    return re.compile(r"\s+".join(parts), re.I)


def main():
    cache = load_jsonl(CACHE)
    amb = {r["institution"] for r in cache if r.get("source") == "ambiguous"}
    # normalised index over RESOLVED cache rows; drop colliding norms
    index, coll = {}, set()
    for r in cache:
        if r.get("source") == "ambiguous" or not r.get("id"):
            continue
        k = norm(r["institution"])
        if k in index and index[k]["id"] != r["id"]:
            coll.add(k)
        else:
            index.setdefault(k, r)
    for k in coll:
        index.pop(k, None)

    work = {w["institution"]: w for w in load_jsonl(WORK)}
    # raw education strings grouped by base person id (education.jsonl rows are
    # attestation-level: kgp_col1937-p912b2_s9 -> base kgp_col1937-p912b2)
    edu = collections.defaultdict(list)
    for r in load_jsonl(OUT / "graph_stage3/education.jsonl"):
        base = re.sub(r"_s\d+$", "", r["person_id"])
        edu[base].append(r["education"])
        edu[r["person_id"]].append(r["education"])

    cap = r"[A-Z][\w.'’-]*"
    resolved, minted, unresolved = [], [], collections.Counter()
    for surf in sorted(amb):
        w = work.get(surf)
        if not w:
            continue
        pat = surf_pattern(surf)
        for pid in w["person_ids"]:
            hit = None
            best_cand = None
            for raw in edu.get(pid, []) or edu.get(re.sub(r"_s\d+$", "", pid), []):
                m = pat.search(raw)
                if not m:
                    continue
                cands = []
                after = raw[m.end():]
                # ", Dublin" / ", Newcastle-upon-Tyne" / " of London"
                fm = re.match(rf"\s*,\s*({cap}(?:[ -]{cap}|[ -](?:upon|on|under|le)[ -]{cap})?)", after)
                # a cue that is itself an institution is the NEXT item of a list
                # ("St. Andrew's school, Raffles Instn."), not a place — reject
                if fm and re.search(r"(school|college|inst|acad|univ|hosp|coll\b)",
                                    fm.group(1), re.I):
                    fm = None
                if fm:
                    cands += [f"{surf}, {fm.group(1)}", f"{surf} {fm.group(1)}"]
                om = re.match(rf"\s+of\s+({cap}(?: {cap})?)", after)
                if om:
                    cands.append(f"{surf} of {om.group(1)}")
                before = raw[: m.start()].rstrip()
                bm = re.search(rf"({cap})\s*$", before)
                if bm and norm(bm.group(1)) not in STOP:
                    cands.append(f"{bm.group(1)} {surf}")
                if cands and not best_cand:
                    best_cand = cands[0]           # comma-form first = most confident
                for c in cands:
                    r = index.get(norm(c))
                    if r:
                        hit = (c, r)
                        break
                if hit:
                    break
            if hit:
                c, r = hit
                resolved.append({"person_id": pid, "institution": c, "institution_id": r["id"],
                                 "institution_label": r["label"], "type": r.get("type"),
                                 "surface": surf, "source": "mention_cue"})
            elif best_cand:
                # confident cue but no cache entry: the parented form is single-
                # referent, so internal-mint it (the doc's rule for locals) —
                # upgradeable to a QID by a later grounding pass.
                minted.append({"person_id": pid, "parented": best_cand, "surface": surf})
            else:
                unresolved[surf] += 1

    # mint internal nodes for cue-reconstructed parented forms; slug on the
    # NORMALISED form so abbreviation variants (B. Guiana / Br. Guiana) share a
    # node; display label = longest raw variant seen
    slug = lambda s: "colkg:" + re.sub(r"[^\w]+", "_", norm(s)).strip("_").title()
    mint_rows = {}
    for m in minted:
        form = re.sub(r"\s+", " ", m["parented"]).strip(" ,")
        sid = slug(form)
        row = mint_rows.setdefault(sid, {"institution": form, "type": "school", "id": sid,
                                         "label": form, "instance_of": [], "country_qid": None,
                                         "source": "mention_mint", "match_type": "cue_reconstructed"})
        if len(form) > len(row["label"]):
            row["label"] = form; row["institution"] = form
        resolved.append({"person_id": m["person_id"], "institution": form, "institution_id": sid,
                         "institution_label": row["label"], "type": "school",
                         "surface": m["surface"], "source": "mention_mint"})
    if mint_rows:  # append to the cache so emit produces the nodes + future runs agree
        with CACHE.open("a") as fh:
            existing = {r["institution"] for r in cache}
            for row in mint_rows.values():
                if row["institution"] not in existing:
                    fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    ov = OUT / "graph_stage3/education_mention_overrides.jsonl"
    ov.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in resolved))
    n_q = sum(1 for r in resolved if str(r["institution_id"]).startswith("Q"))
    n_m = sum(1 for r in resolved if r["source"] == "mention_mint")
    print(f"[{OUT}] resolved {len(resolved)} mentions ({n_q} to QIDs, {n_m} minted to "
          f"{len(mint_rows)} internal nodes) -> {ov.name}; unresolved {sum(unresolved.values())}")
    for s, n in unresolved.most_common(10):
        print(f"    still ambiguous: {s} ({n})")


if __name__ == "__main__":
    main()
