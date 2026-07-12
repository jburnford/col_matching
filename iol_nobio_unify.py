#!/usr/bin/env python3
"""No-bio within-population unification (NOBIO_DEDUP_KICKOFF step 1).

The 19,849 civil chains and 14,984 unlinked gradation identities
describe overlapping people three ways; this pass finds the edges,
deterministic keys first, and renders the residue for the Nibi judge:

  chain<->gradation   the census' 512 name-key overlap is a floor;
                      corroborate on covenant/commission year (gold:
                      entry precedes every listed office), Bengal/
                      Madras/Bombay establishment vs government side,
                      edition-era overlap
  chain<->chain       same (surname, initials) in different governments
                      = transfers or dual listing; forename agreement
                      or corpus-unique adjacency is deterministic
  gradation<->exit    unlinked 1861-85 casualties onto the gradation
                      spine: the identity stops being printed at the
                      exit year (disappearance window)
  chain<->exit        unlinked exits closing a civil chain

Outputs (data/iol/identity/):
  nobio_unify_edges.jsonl     accepted edges, tier det_strong/det_std
  nobio_unify_residue.jsonl   candidate pairs for LLM adjudication
                              (both-side context rendered in-row)
  NOBIO_UNIFY.md              report

Gotchas honoured: full paths everywhere (no CWD-relative writes);
deterministic fingerprints outrank single judged verdicts downstream;
unlinked = not claimed by iol_link_exits/_gradation on the CURRENT
audited table — rerun this after any table rebuild.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from glob import glob
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"

CAREER_MAX = 50          # years, entry -> last attestation
ERA_SLACK = 8            # chain years vs gradation editions
DET_ERA = 5              # tighter window earns the det bonus

_STYLES = {"sir", "hon", "honble", "rev", "revd", "dr", "lord", "bart",
           "bt", "mr", "major", "col", "capt", "lieut", "lt", "gen"}

# Which governments a Bengal/Madras/Bombay covenant could serve under.
# GoI, the India Office and the secretariats draw from all three.
_ANY_GOV = {"GOVERNMENT OF INDIA", "INDIA OFFICE (LONDON)",
            "OFFICE OF THE HIGH COMMISSIONER FOR INDIA"}
_SIDE = {
    "BENGAL": {"BENGAL", "PUNJAB", "NORTH-WESTERN PROVINCES AND OUDH",
               "UNITED PROVINCES OF AGRA AND OUDH", "CENTRAL PROVINCES",
               "ASSAM", "BURMA", "BIHAR AND ORISSA", "BIHAR", "ORISSA",
               "DELHI", "NORTH-WEST FRONTIER PROVINCE",
               "EASTERN BENGAL AND ASSAM"},
    "MADRAS": {"MADRAS", "COORG"},
    "BOMBAY": {"BOMBAY", "SIND", "BALUCHISTAN", "ADEN"},
}
_CORPS_PRES = [("BO", "BOMBAY"), ("B", "BENGAL"), ("M", "MADRAS")]


def sk(s: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def given_tokens(given: str | None) -> list[str]:
    toks = [t.strip(".") for t in re.split(r"[ .]+", given or "")
            if t.strip(".")]
    return [t for t in toks
            if re.sub(r"[^a-z]", "", t.lower()) not in _STYLES]


def initials_of(tokens: list[str]) -> str:
    return "".join(t[0].upper() for t in tokens if t and t[0].isalpha())


def given_part(full_name: str | None) -> str:
    """Drop the trailing surname token so initials-only names ("J.
    Smith") can never forename-match on the surname."""
    toks = [t for t in (full_name or "").split()
            if any(c.isalpha() for c in t)]
    return " ".join(toks[:-1]) if len(toks) >= 2 else ""


def forename_agree(a_given: str | None, b_given: str | None) -> bool:
    """Both sides carry a full given word and the first ones match.
    Pass GIVEN-name parts only (use given_part on full names)."""
    aw = [t.upper() for t in given_tokens(a_given) if len(t) > 2]
    bw = [t.upper() for t in given_tokens(b_given) if len(t) > 2]
    return bool(aw and bw and aw[0] == bw[0])


def forename_conflict(a_given: str | None, b_given: str | None) -> bool:
    aw = [t.upper() for t in given_tokens(a_given) if len(t) > 2]
    bw = [t.upper() for t in given_tokens(b_given) if len(t) > 2]
    return bool(aw and bw and aw[0] != bw[0])


# most-specific first: GENERAL is a substring of LIEUT.-GENERALS
_RANK_ORDER = [("LIEUTGENERAL", 7), ("LTGENERAL", 7),
               ("MAJORGENERAL", 6), ("MAJGENERAL", 6),
               ("LIEUTCOLONEL", 4), ("LTCOLONEL", 4),
               ("LIEUTCOL", 4), ("LTCOL", 4),
               ("GENERAL", 8), ("COLONEL", 5), ("COL", 5),
               ("MAJOR", 3), ("MAJ", 3), ("CAPTAIN", 2), ("CAPT", 2),
               ("LIEUTENANT", 1), ("LIEUT", 1), ("LT", 1),
               ("ENSIGN", 0), ("CORNET", 0)]


def name_rank(nm: str | None) -> int | None:
    """Rank carried in a casualty-name prefix ('Lt.Col. R. G. ...')."""
    head = sk("".join((nm or "").split()[:2]))
    for key, r in _RANK_ORDER:
        if head.startswith(key):
            return r
    return None


def section_ranks(sections: list[str]) -> set[int]:
    out = set()
    for s in sections or []:
        k = sk(s)
        for key, r in _RANK_ORDER:
            if key in k:
                out.add(r)
                break
    return out


def gov_side(gov: str | None) -> str | None:
    for pres, govs in _SIDE.items():
        if gov in govs:
            return pres
    return None            # _ANY_GOV and unknowns: unconstrained


def corps_pres(corps: list[str]) -> set[str]:
    out = set()
    for c in corps:
        head = re.sub(r"[^A-Z]", "", (c or "").upper().split(".")[0])
        for pre, pres in _CORPS_PRES:
            if head == pre:
                out.add(pres)
                break
    return out


def grad_pres(g: dict) -> set[str]:
    if g["list_type"] == "civil":
        return set(g.get("establishments") or [])
    return corps_pres(g.get("corps") or [])


def pres_compatible(pres: set[str], gov: str | None) -> bool | None:
    """True corroborates, False blocks det tier, None = unknown."""
    if not pres or gov in _ANY_GOV or gov is None:
        return None
    side = gov_side(gov)
    if side is None:
        return None
    return side in pres


def load_chains() -> list[dict]:
    return [json.loads(l) for l in
            open(IDD / "nobio_civil_chains.jsonl", encoding="utf-8")]


def load_gradation() -> list[dict]:
    gid = [json.loads(l) for l in
           open(ROOT / "gradation/gradation_identities.jsonl",
                encoding="utf-8")]
    linked = {json.loads(l)["gradation_id"] for l in
              open(ROOT / "gradation/gradation_person_links.jsonl",
                   encoding="utf-8")}
    return [g for g in gid if g["gradation_id"] not in linked]


def load_exits() -> list[dict]:
    linked = {json.loads(l)["event_id"] for l in
              open(IDD / "exit_links.jsonl", encoding="utf-8")}
    evs = []
    for f in sorted(glob(str(ROOT / "casualties/casualties_1*.jsonl"))):
        for i, l in enumerate(open(f, encoding="utf-8")):
            e = json.loads(l)
            e["event_id"] = f"{e['edition_tag']}:{i}"
            if e["event_id"] in linked:
                continue
            nm = e.get("name") or ""
            toks = [t for t in nm.split() if any(c.isalpha() for c in t)]
            if len(toks) < 2 or len(toks[-1]) < 3 or not e.get("year"):
                continue
            e["surname_key"] = sk(toks[-1])
            e["given"] = " ".join(toks[:-1])
            e["initials"] = initials_of(given_tokens(e["given"]))
            evs.append(e)
    return evs


def main() -> None:
    chains = load_chains()
    grads = load_gradation()
    exits = load_exits()

    ch_by_key = defaultdict(list)
    for c in chains:
        ch_by_key[(c["surname_key"], c["initials"])].append(c)
    gr_by_key = defaultdict(list)
    for g in grads:
        gr_by_key[(sk(g["surname"]),
                   initials_of(given_tokens(g.get("given"))))].append(g)

    edges, residue = [], []
    stats = Counter()

    def emit(edge_type, a, b, tier, score, ev):
        row = {"edge_type": edge_type, "a": a, "b": b, "tier": tier,
               "score": score, "evidence": ev}
        (edges if tier.startswith("det") else residue).append(row)
        stats[f"{edge_type}:{tier}"] += 1

    # ---- chain <-> gradation -------------------------------------
    for key, gs in gr_by_key.items():
        cs = ch_by_key.get(key)
        if not cs:
            continue
        for g in gs:
            eds = g.get("editions") or []
            ey = g.get("entry_year")
            for c in cs:
                y0, y1 = c["years"]
                straddle = bool(ey and y0 < ey <= y1 + 1)
                if ey and (ey > y1 + 1 or y1 - ey > CAREER_MAX):
                    continue            # covenant after the chain ends
                if eds and not (min(eds) - ERA_SLACK <= y1
                                and max(eds) + ERA_SLACK >= y0):
                    continue
                if forename_conflict(given_part(c["name"]),
                                     g.get("given")):
                    continue
                comp = pres_compatible(grad_pres(g), c["government"])
                if comp is False:
                    continue
                score = 20
                fn = forename_agree(given_part(c["name"]), g.get("given"))
                score += 15 if fn else 0
                score += 15 if comp else 0
                score += 10 if (eds and min(eds) - DET_ERA <= y1
                                and max(eds) + DET_ERA >= y0) else 0
                unique = len(gs) == 1 and len(cs) == 1
                score += 20 if unique else 0
                ev = {"key": list(key), "entry_year": ey,
                      "grad_eds": [min(eds), max(eds)] if eds else None,
                      "chain_years": c["years"], "forename": fn,
                      "pres": sorted(grad_pres(g)),
                      "government": c["government"], "unique": unique,
                      "chain_name": c["name"], "grad_given": g.get("given"),
                      "list_type": g["list_type"],
                      "entry_straddle": straddle}
                if straddle:            # office before covenant year:
                    emit("chain_grad", c["chain_id"], g["gradation_id"],
                         "llm", score, ev)  # real (uncovenanted start)
                elif unique and score >= 60:
                    emit("chain_grad", c["chain_id"], g["gradation_id"],
                         "det_strong", score, ev)
                elif unique and score >= 45:
                    emit("chain_grad", c["chain_id"], g["gradation_id"],
                         "det_std", score, ev)
                else:
                    emit("chain_grad", c["chain_id"], g["gradation_id"],
                         "llm", score, ev)

    # ---- chain <-> chain (cross-government) ----------------------
    for key, cs in ch_by_key.items():
        if len(cs) < 2:
            continue
        if len(cs) > 4:                 # surname-frequency runaway
            stats["chain_chain:skipped_bigkey"] += len(cs)
            continue
        cs = sorted(cs, key=lambda c: c["years"][0])
        for i, a in enumerate(cs):
            for b in cs[i + 1:]:
                if a["government"] == b["government"]:
                    continue            # gap-split namesakes by design
                gap = b["years"][0] - a["years"][1]
                span = b["years"][1] - a["years"][0]
                if gap > 3 or span > CAREER_MAX:
                    continue
                if forename_conflict(given_part(a["name"]),
                                     given_part(b["name"])):
                    continue
                fn = forename_agree(given_part(a["name"]),
                                    given_part(b["name"]))
                adjacent = -1 <= gap <= 2
                score = 20 + (25 if fn else 0) + (10 if adjacent else 0) \
                    + (15 if len(cs) == 2 else 0)
                ev = {"key": list(key), "a_gov": a["government"],
                      "b_gov": b["government"], "a_years": a["years"],
                      "b_years": b["years"], "forename": fn,
                      "a_name": a["name"], "b_name": b["name"],
                      "gap": gap, "n_key_chains": len(cs)}
                if fn and len(cs) == 2:
                    emit("chain_chain", a["chain_id"], b["chain_id"],
                         "det_strong", score, ev)
                elif len(cs) == 2 and adjacent:
                    emit("chain_chain", a["chain_id"], b["chain_id"],
                         "det_std", score, ev)
                else:
                    emit("chain_chain", a["chain_id"], b["chain_id"],
                         "llm", score, ev)

    # ---- gradation <-> exit --------------------------------------
    ex_grad = [e for e in exits if (e.get("establishment") or "")
               .startswith(("MILITARY", "CIVIL")) or
               e.get("establishment") is None]
    for e in ex_grad:
        gs = gr_by_key.get((e["surname_key"], e["initials"]))
        if not gs:
            continue
        est = e.get("establishment") or ""
        want = ("army" if est.startswith("MILITARY")
                else "civil" if est.startswith("CIVIL") else None)
        cands = []
        for g in gs:
            if want and g["list_type"] != want:
                continue
            ey, eds = g.get("entry_year"), g.get("editions") or []
            if ey and not (ey < e["year"] <= ey + CAREER_MAX + 10):
                continue
            if not eds:
                continue
            dis = e["year"] <= max(eds) + 2 and max(eds) <= e["year"] + 2
            if not (min(eds) - 1 <= e["year"] <= max(eds) + ERA_SLACK):
                continue
            pres = grad_pres(g)
            comp = (None if not e.get("presidency") or not pres
                    else e["presidency"] in pres)
            if comp is False:
                continue
            cands.append((g, dis, comp))
        for g, dis, comp in cands:
            fn = forename_agree(e["given"], g.get("given"))
            # rank gate (silver audit: a COLONELS-list man cannot die
            # a Capt. — namesake): >1 grade off demotes to the judge
            er = name_rank(e.get("name"))
            gr = section_ranks(g.get("sections"))
            rank_ok = (er is None or not gr
                       or min(gr) - 1 <= er <= max(gr) + 1)
            score = 20 + (15 if fn else 0) + (20 if dis else 0) \
                + (10 if comp else 0) + (15 if len(cands) == 1 else 0)
            ev = {"event": e["event"], "year": e["year"],
                  "name": e["name"], "grad_given": g.get("given"),
                  "entry_year": g.get("entry_year"),
                  "last_ed": max(g["editions"]),
                  "presidency": e.get("presidency"),
                  "establishment": e.get("establishment"),
                  "disappearance": dis, "n_cands": len(cands),
                  "rank_conflict": not rank_ok}
            if not rank_ok:
                emit("grad_exit", g["gradation_id"], e["event_id"],
                     "llm", score, ev)
            elif len(cands) == 1 and dis and score >= 60:
                emit("grad_exit", g["gradation_id"], e["event_id"],
                     "det_strong" if e["event"] == "death" else "det_std",
                     score, ev)
            elif len(cands) == 1 and score >= 50:
                emit("grad_exit", g["gradation_id"], e["event_id"],
                     "det_std", score, ev)
            else:
                emit("grad_exit", g["gradation_id"], e["event_id"],
                     "llm", score, ev)

    # ---- chain <-> exit ------------------------------------------
    for e in exits:
        cs = ch_by_key.get((e["surname_key"], e["initials"]))
        if not cs:
            continue
        cands = []
        for c in cs:
            if not (c["years"][0] <= e["year"] + 1
                    and c["years"][1] - 1 <= e["year"] <= c["years"][1] + 3):
                continue                # exit closes the chain
            comp = pres_compatible({e["presidency"]}
                                   if e.get("presidency") else set(),
                                   c["government"])
            if comp is False:
                continue
            cands.append((c, comp))
        for c, comp in cands:
            fn = forename_agree(e["given"], given_part(c["name"]))
            if forename_conflict(e["given"], given_part(c["name"])):
                continue
            score = 20 + (20 if fn else 0) + (10 if comp else 0) \
                + (15 if len(cands) == 1 else 0)
            ev = {"event": e["event"], "year": e["year"],
                  "name": e["name"], "chain_name": c["name"],
                  "chain_years": c["years"],
                  "government": c["government"],
                  "presidency": e.get("presidency"), "n_cands": len(cands)}
            if len(cands) == 1 and fn:
                emit("chain_exit", c["chain_id"], e["event_id"],
                     "det_strong", score, ev)
            elif len(cands) == 1 and score >= 45:
                emit("chain_exit", c["chain_id"], e["event_id"],
                     "det_std", score, ev)
            else:
                emit("chain_exit", c["chain_id"], e["event_id"], "llm",
                     score, ev)

    with open(IDD / "nobio_unify_edges.jsonl", "w",
              encoding="utf-8") as fh:
        for r in edges:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(IDD / "nobio_unify_residue.jsonl", "w",
              encoding="utf-8") as fh:
        for r in residue:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Union effect on the census: distinct no-bio ids merged by det edges
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    ids = set()
    for r in edges:
        if r["edge_type"] in ("chain_grad", "chain_chain"):
            ids.update((r["a"], r["b"]))
            ra, rb = find(r["a"]), find(r["b"])
            if ra != rb:
                parent[ra] = rb
    merged = len(ids) - len({find(x) for x in ids})

    by_type = defaultdict(Counter)
    for k, v in stats.items():
        t, tier = k.split(":", 1)
        by_type[t][tier] = v
    lines = ["# No-bio within-population unification", ""]
    for t in ("chain_grad", "chain_chain", "grad_exit", "chain_exit"):
        c = by_type[t]
        lines.append(
            f"- **{t}**: det_strong {c['det_strong']:,}, det_std "
            f"{c['det_std']:,}, llm residue {c['llm']:,}"
            + (f" (big-key skipped {c['skipped_bigkey']:,})"
               if c.get("skipped_bigkey") else ""))
    union = json.load(open(IDD / "nobio_census.json"))["nobio_union"]
    lines += [
        "",
        f"Deterministic identity edges collapse **{merged:,}** ids out "
        f"of the {union:,} census union (chain_grad + chain_chain only; "
        "exit edges attach events, they do not merge identities).",
        "",
        "Residue pairs carry both-side context in-row -> render with "
        "iol_build_adjudication_batch.py-style worklist for the Nibi "
        "judge (`nobio_unify_residue.jsonl`).",
    ]
    (IDD / "NOBIO_UNIFY.md").write_text("\n".join(lines) + "\n",
                                        encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
