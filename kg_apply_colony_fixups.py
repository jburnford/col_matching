#!/usr/bin/env python3
"""Post-emit colony fixups — the YEAR- and PERSON-aware corrections that the
place->colony crosswalk cannot express (it is keyed by place alone).

Every emit recomputes colonies from resolve_colony + the crosswalk, which is
year-blind and person-blind; the corrections below would otherwise silently
revert on each re-emit (they did once, 2026-07-03). reemit_dedup.sh runs this
as its final step; it is idempotent and safe to run repeatedly.

Rules (provenance: modern-colony-QID audit + re-grounding sweep, 2026-07-02/03):
  1. Q252 Dutch East Indies pool: bare "Borneo"/"New Guinea"/"Australasia"
     surfaces belong to British territories — per-person dispositions from
     career-context review (consuls-general -> Labuan, Brooke era -> Sarawak,
     BNB constabulary -> British North Borneo; New Guinea by era; Federal
     Council of Australasia -> Australia). Java/Batavia/Sumatra stay.
  2. Ionian Islands: British protectorate ended 1864 — Ionian-place facts
     after 1864 (WWI Salonika-era Corfu) are foreign service in Greece.
  3. Chinde concession: <=1907 belongs to British Central Africa, after to
     Nyasaland (the crosswalk override is year-blind -> Nyasaland).
  4. South-West Africa towns: pre-1919 facts are the German era / the 1914-16
     campaign, not mandate administration -> colony null.
  5. Pakistan province splits by period: NWFP created 1901 (before: Punjab),
     Sind separated from Bombay 1936, Baluchistan agency from 1877.
  6. Jubaland was British East Africa/Kenya until the 1925 cession to Italy.
  7. Bare "Somalia" before 1941 -> British Somaliland (the BMA of ex-Italian
     Somalia only exists 1941+).
  8. Aden: Mukalla/Hadhramaut = Aden Protectorate (not Colony); Aden-side
     facts before 1937 = Aden Province (under Bombay).
  9. Tai Po (New Territories) -> Hong Kong, not China.
 10. Final pass: colony_label normalised to colony_label_lock everywhere.
"""
from __future__ import annotations
import json, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOCK = json.loads((ROOT / "data/kg/colony_label_lock.json").read_text())
CANON = json.loads((ROOT / "data/kg/colony_canon.json").read_text())

# 1. Q252 per-person dispositions (CO corpus; career-context review 2026-07-03)
Q252_PERSON = {
    "kgp_col1910-p784b6": "Q1147441", "kgp_col1914-p739b7": "Q1147441",
    "kgp_col1954-p265b5": "Q1147441", "kgp_col1919-p846b19": "Q1147441",
    "kgp_col1948-p418b12": "Q1658411", "kgp_col1867-p242b9": "Q1658411",
    "kgp_col1877-p405b10": "Q1658411", "kgp_col1877-p366b20": "Q1658411",
    "kgp_col1867-p214b13": "Q6420545", "kgp_col1910-p719b15": "Q6420545",
    "kgp_col1914-p825b8": "Q6420545", "kgp_col1918-p685b16": "Q6420545",
    "kgp_col1877-p423b7": "Q6420545",
}
IONIAN_PLACES = {"Corfu", "Paxos", "Kythira", "Zakynthos", "Cephalonia", "Ithaca", "Lefkada"}
SWA_TOWNS = {"Q3935", "Q597491", "Q159325"}
PK_KPK = {"Q4412467"}


def fix(r):
    """Mutate one row; return True if changed."""
    q = r.get("colony_qid")
    pid = r.get("person_id") or ""
    pq = r.get("place_qid") or r.get("qid")
    pl = (r.get("place_label") or r.get("place") or "")
    y = r.get("year_start") or r.get("year_end") or 0

    def set_colony(nq):
        if r.get("colony_qid") == nq:
            return False
        r["colony_qid"] = nq
        r["colony_label"] = LOCK.get(nq) if nq else None
        return True

    if q in CANON and CANON[q] != q:                   # 0. canon folds on existing rows
        return set_colony(CANON[q])
    if q == "Q252":
        if pl.startswith("Borneo") and pid in Q252_PERSON:
            return set_colony(Q252_PERSON[pid])
        if pl.startswith("New Guinea"):
            return set_colony("Q1443945" if y >= 1920 else "Q2645837")
        if pl.startswith("Australasia"):
            return set_colony("Q56850459" if pid == "kgp_col1922-p768b13" else "Q408")
        return False
    if q == "Q1063498" and y > 1864:
        return set_colony("Q41")                       # post-protectorate Greece
    if q == "Q41" and pl in IONIAN_PLACES and 0 < y <= 1864:
        return set_colony("Q1063498")
    if pq == "Q2261361" and 0 < y <= 1907:             # Chinde, BCA era
        return set_colony("Q2642989")
    if pq in SWA_TOWNS and 0 < y < 1919:               # German era / campaign
        return set_colony(None)
    if q in PK_KPK and 0 < y < 1901:                   # NWFP not yet created
        return set_colony("Q2629708")
    if q == "Q891827" and y >= 1936 and (r.get("colony_label") or "").startswith("Bombay") \
            and "sind" in ((r.get("place_label") or "").lower()):
        return set_colony("Q7522091")                  # Sind Province from 1936
    if q == "Q3303188" and 0 < y < 1877:
        return set_colony("Q129286")                   # pre-agency Baluchistan
    if "jubaland" in pl.lower():
        return set_colony("Q2538511")                  # Kenya until 1925 cession
    if q == "Q1045" and 0 < y < 1941:
        return set_colony("Q662653")                   # no BMA before 1941
    if q in ("Q49910", "Q17509767"):
        low = pl.lower()
        if any(k in low for k in ("mukalla", "hadhramaut", "yemen")):
            return set_colony("Q1865132")              # Protectorate, not Colony
        if q == "Q49910" and 0 < y < 1937:
            return set_colony("Q17509767")             # Aden Province era
    if pl == "Tai Po" or (q == "Q148" and "tai po" in pl.lower()):
        return set_colony("Q1054923")                  # New Territories = Hong Kong
    # 10. label normalisation (covers e.g. Q148 rows still saying "Weihaiwei")
    if q and q in LOCK and r.get("colony_label") != LOCK[q]:
        r["colony_label"] = LOCK[q]
        return True
    return False


def main():
    tot = collections.Counter()
    for corpus in ("data/kg", "data/iol"):
        for name in ("career_events", "career_facts", "places", "employment_edges"):
            p = ROOT / corpus / "graph_stage3" / f"{name}.jsonl"
            if not p.exists():
                continue
            out, n = [], 0
            for line in p.open():
                r = json.loads(line)
                if fix(r):
                    n += 1
                out.append(json.dumps(r, ensure_ascii=False))
            if n:
                p.write_text("\n".join(out) + "\n")
            tot[f"{corpus}/{name}"] = n
    for k, n in tot.items():
        if n:
            print(f"  fixups {k}: {n}")
    if not any(tot.values()):
        print("  fixups: nothing to do (already applied)")


if __name__ == "__main__":
    main()
