#!/usr/bin/env python3
"""IOL <-> COL cross-corpus person join (docs/IOL_VS_COL.md §7's floor of
211 exact-name matches, done properly): link India Office List canonical
persons (19,513) to Colonial Office List bio-persons (27,511) on tiered
evidence, then quantify the 1947-exodus cohort — ICS/Indian-service
officers reappearing in the Colonial Service after Partition.

Tiers (strongest first; a person links once, at its best tier):
  T1_honour   shared (award, year) honour + compatible names — award+year
              is near-unique empire-wide
  T2_birth    birth year agrees (+-1) + same surname key + given names
              compatible with >=1 shared full token
  T3_name     exact surname + >=2-token exact given names + plausible
              chronology (COL career not entirely before the IOL one)

Outputs:
  data/iol/identity/iol_col_links.jsonl
  docs/IOL_COL_JOIN.md   tier counts + the exodus cohort
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

IOL = Path("data/iol/llm_struct_corpus.stage3.deduped.jsonl")
COL = Path("data/volume/bio_persons/bio_persons.jsonl")
OUT = Path("data/iol/identity/iol_col_links.jsonl")
DOC = Path("docs/IOL_COL_JOIN.md")


def sk(s):
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def awk(a):
    return re.sub(r"[^A-Z]", "", (a or "").upper())


def toks(g):
    return [t for t in re.split(r"[ .]+", g or "") if t]


def initials(ts):
    return "".join(t[0].upper() for t in ts if t and t[0].isalpha())


def compat(ga, gb):
    """None=contradiction, 'weak'=initials-level, 'full'=shared full token."""
    ta, tb = toks(ga), toks(gb)
    if not ta or not tb:
        return "weak"
    ia, ib = initials(ta), initials(tb)
    if not (ia == ib or ia.startswith(ib) or ib.startswith(ia)):
        return None
    wa = {t.upper() for t in ta if len(t) > 2}
    wb = {t.upper() for t in tb if len(t) > 2}
    if wa and wb:
        if not (wa & wb) and initials(sorted(wa)) != initials(sorted(wb)):
            # differing full-form sets with no overlap: contradiction only
            # if the FIRST full tokens disagree
            fa = [t.upper() for t in ta if len(t) > 2][0]
            fb = [t.upper() for t in tb if len(t) > 2][0]
            if fa != fb:
                return None
        return "full" if wa & wb else "weak"
    return "weak"


def honour_set(p):
    return {(awk(h.get("award")), h["year"]) for h in (p.get("honours") or [])
            if h.get("year") and awk(h.get("award"))}


def main() -> None:
    iol = [json.loads(l) for l in open(IOL, encoding="utf-8")]
    col = [json.loads(l) for l in open(COL, encoding="utf-8")]

    col_by_sk = defaultdict(list)
    for c in col:
        col_by_sk[sk(c.get("surname"))].append(c)
        # Indian names: IOL surname may be the FULL name; COL sometimes
        # splits it — index COL by given+surname full key too
        full = sk((c.get("given_names") or "") + (c.get("surname") or ""))
        if full and full != sk(c.get("surname")):
            col_by_sk[full].append(c)

    links = []
    stats = Counter()
    for p in iol:
        hs = honour_set(p)
        keys = {sk(p.get("surname")),
                sk((p.get("given_names") or "") + (p.get("surname") or ""))}
        pool, seen = [], set()
        for k in keys:
            for c in col_by_sk.get(k, []):
                if id(c) not in seen:
                    seen.add(id(c))
                    pool.append(c)
        best = None
        for c in pool:
            nc = compat(p.get("given_names"), c.get("given_names"))
            if nc is None:
                continue
            tier = None
            shared_h = hs & honour_set(c)
            ba, bb = p.get("birth_year"), c.get("birth_year")
            birth_ok = ba and bb and abs(ba - bb) <= 1
            birth_conflict = ba and bb and abs(ba - bb) > 3
            if shared_h and not birth_conflict:
                tier = "T1_honour"
            elif birth_ok and nc == "full":
                tier = "T2_birth"
            elif ba and bb and ba == bb and nc == "weak":
                # exact birth year + initials-compatible names (one side
                # prints initials only) — the COL-side norm before 1930s
                tier = "T2_birth_initials"
            elif nc == "full" and not birth_conflict \
                    and len(toks(p.get("given_names"))) >= 2 \
                    and sk(p.get("given_names")) == sk(c.get("given_names")):
                # chronology: COL career must not sit entirely before IOL's
                pe = p.get("editions") or []
                ce = c.get("editions") or []
                if pe and ce and max(ce) >= min(pe):
                    tier = "T3_name"
            if tier is None:
                continue
            rank = {"T1_honour": 0, "T2_birth": 1,
                    "T2_birth_initials": 2, "T3_name": 3}[tier]
            cand = (rank, -len(shared_h), c, tier, sorted(shared_h))
            if best is None or cand[:2] < best[:2]:
                best = cand
        if best is None:
            continue
        _, _, c, tier, shared_h = best
        pe, ce = p.get("editions") or [], c.get("editions") or []
        row = {"iol_person_id": p["person_id"],
               "col_person_id": c["person_id"],
               "tier": tier,
               "surname": p.get("surname"),
               "iol_given": p.get("given_names"),
               "col_given": c.get("given_names"),
               "iol_birth": p.get("birth_year"),
               "col_birth": c.get("birth_year"),
               "shared_honours": [f"{a} {y}" for a, y in shared_h],
               "iol_editions": [min(pe), max(pe)] if pe else None,
               "col_editions": [min(ce), max(ce)] if ce else None}
        row["exodus_1947"] = bool(pe and ce and max(pe) >= 1945
                                  and min(ce) >= 1946)
        links.append(row)
        stats[tier] += 1
        if row["exodus_1947"]:
            stats[f"exodus_{tier}"] += 1

    with open(OUT, "w", encoding="utf-8") as fh:
        for r in links:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    exodus = [r for r in links if r["exodus_1947"]]
    exodus.sort(key=lambda r: (r["tier"], r["surname"] or ""))
    lines = [
        "# IOL <-> COL cross-corpus person links",
        "",
        f"{len(iol):,} IOL canonical persons x {len(col):,} COL "
        f"bio-persons -> **{len(links):,} links** "
        f"(T1 honour {stats['T1_honour']:,} / T2 birth "
        f"{stats['T2_birth']:,}+{stats['T2_birth_initials']:,} initials-level "
        f"/ T3 name {stats['T3_name']:,}).",
        "",
        "## The 1947 exodus (IOL attested 1945+, COL first attested 1946+)",
        "",
        f"**{len(exodus):,} officers** cross from the India Office List's "
        "final editions into post-war Colonial Office Lists "
        f"(T1 {stats['exodus_T1_honour']:,} / T2 "
        f"{stats['exodus_T2_birth']:,}+{stats['exodus_T2_birth_initials']:,} "
        f"/ T3 {stats['exodus_T3_name']:,}).",
        "",
        "| tier | surname | given (IOL) | birth | IOL span | COL span | shared honours |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in exodus[:60]:
        lines.append(
            f"| {r['tier'][:2]} | {r['surname']} | {r['iol_given'] or ''} "
            f"| {r['iol_birth'] or r['col_birth'] or ''} "
            f"| {r['iol_editions'][0]}-{r['iol_editions'][1]} "
            f"| {r['col_editions'][0]}-{r['col_editions'][1]} "
            f"| {', '.join(r['shared_honours'][:3])} |")
    if len(exodus) > 60:
        lines.append(f"| … | +{len(exodus) - 60} more | | | | | |")
    lines += [
        "",
        "Full links: `data/iol/identity/iol_col_links.jsonl` "
        "(`exodus_1947` flag). T1 = shared dated honour (near-unique "
        "empire-wide) + compatible names; T2 = birth ±1 + shared full "
        "given token; T3 = exact full-name match with sane chronology "
        "(weakest — audit before quantitative use).",
    ]
    DOC.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:12]))
    print("stats:", dict(stats))


if __name__ == "__main__":
    main()
