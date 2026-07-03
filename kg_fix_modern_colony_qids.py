#!/usr/bin/env python3
"""Fix the modern-country-QID-as-colony class (audit 2026-07-02, follow-up to the
Q1020 Malawi/BCA fix): 21 colony_qids in the graph were modern sovereign states
wearing period labels via the label lock, having leaked in through the TTL
skos:relatedMatch -> _index route or the crosswalk's country_is_colony rule
(which trusts _COL_QIDS, seeded from the graph's own places.jsonl — so one leak
self-perpetuates and swallows every locality of that country).

Three treatments, decided per evidence card (scratchpad colony_audit_cards.json):

FOLD — the period polity node already exists and dominates; the modern QID is a
  pure duplicate (e.g. Q712 modern Fiji next to Q5148320 Fiji colony).

SPLIT — one modern QID pooled facts that belong to several period polities,
  resolved per place (geo admin chain) and/or year:
  * Q843 Pakistan ("North-West Frontier", seat Quetta!) -> Punjab / NWFP (1901+) /
    Sind (Bombay Pres. before 1936) / Baluchistan (1877+) / Raj residue
  * Q924 Tanzania -> Pemba=Zanzibar, mainland=Tanganyika
  * Q805 Yemen -> Mukalla+Hadhramaut=Aden Protectorate, Aden-side by year
    (Province <1937 / Colony >=1937)
  * Q1045 Somalia -> Jubaland=Kenya (ceded to Italy 1925; all facts <=1925),
    Berbera/Zeila + pre-1941=British Somaliland, 1941+ bare "Somalia"=BMA (kept)
  * Q41 Greece -> Ionian island places with year<=1864 = United States of the
    Ionian Islands; the rest (Salonika WWI, Piraeus 1854-57 occupation) stays
  * Q148 China -> Tai Po (New Territories) = Hong Kong; consular rest stays
  * Q954 Zimbabwe ("Rhodesia (UDI)" for 1889-1919 facts!) -> BSAC Territory

KEEP — genuine umbrella / foreign-service nodes, label-lock corrected only:
  Q258 "South Africa" (lock wrongly said "Griqualand West"), Q148 China,
  Q41 Greece, Q683 Samoa, Q252 Indonesia (flagged: bare Borneo/N. Guinea
  surfaces need re-grounding, not a colony fold).

Rewrites graph_stage3 layers in place for BOTH corpora; colony_canon.json and
colony_label_lock.json are updated separately so future re-emits agree.
"""
from __future__ import annotations
import json, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GEO = json.loads((ROOT / "data/kg/place_geo_chain.json").read_text())
LOCK = json.loads((ROOT / "data/kg/colony_label_lock.json").read_text())

FOLD = {  # modern colony_qid -> canonical period polity (unconditional)
    "Q712":  "Q5148320",    # Fiji -> Fiji colony
    "Q244":  "Q63973349",   # Barbados -> Barbados Colony
    "Q233":  "Q6744657",    # Malta -> Malta colony
    "Q1042": "Q21821453",   # Seychelles -> Seychelles colony
    "Q398":  "Q21816225",   # Bahrain -> Bahrain Protectorate
    "Q817":  "Q3480281",    # Kuwait -> Kuwait protectorate
    "Q678":  "Q17197946",   # Tonga -> Tonga Protectorate
    "Q763":  "Q1637975",    # St Kitts & Nevis -> Saint Kitts and Nevis Colony
    "Q781":  "Q130386222",  # Antigua & Barbuda -> Antigua Colony
    "Q836":  "Q2376315",    # Myanmar -> Burma
    "Q1049": "Q541455",     # Sudan -> Anglo-Egyptian Sudan
    "Q954":  "Q5155572",    # Zimbabwe, facts all 1889-1919 -> BSAC Territory
}

# Q843 Pakistan: modern admin-chain keyword -> region bucket
PK_REGION = {
    "kpk": ("khyber pakhtunkhwa", "peshawar", "bannu", "kohat", "dera ismail khan",
            "charsadda", "mardan", "nowshera", "thall", "wana", "hazara", "malakand",
            "waziristan", "swat", "abbottabad", "tank", "kurram", "khyber"),
    "punjab": ("punjab", "lahore", "multan", "rawalpindi", "attock", "mianwali",
               "jhelum", "sialkot", "gujranwala", "bahawalpur", "dera ghazi khan"),
    "sindh": ("sindh", "karachi", "hyderabad", "sukkur", "larkana", "shikarpur", "thatta"),
    "baluch": ("balochistan", "quetta", "zhob", "sibi", "rakhshan", "chagai",
               "pishin", "kalat", "loralai", "makran"),
}
IONIAN = {"Corfu", "Paxos", "Kythira", "Zakynthos", "Cephalonia", "Ithaca", "Lefkada"}

RELABEL = {  # keep the node, fix its display label (mirrors the lock update)
    "Q258": "South Africa",
    "Q1045": "Somalia (British Military Administration)",
    "Q2376315": "Burma",
}


def _admins(place_qid):
    e = GEO.get(place_qid) or {}
    return " | ".join((al or "").lower() for _, al in (e.get("admins") or []))


def remap(colony_qid, place_qid, place_label, year):
    """Return new colony_qid for a fact, or None to keep as-is."""
    y = year or 0
    if colony_qid in FOLD:
        return FOLD[colony_qid]
    if colony_qid == "Q843":
        astr = _admins(place_qid)
        for region, keys in PK_REGION.items():
            if any(k in astr for k in keys):
                if region == "kpk":
                    return "Q4412467" if (not y or y >= 1901) else "Q2629708"
                if region == "punjab":
                    return "Q2629708"
                if region == "sindh":
                    return "Q7522091" if y >= 1936 else "Q891827"
                if region == "baluch":
                    return "Q3303188" if (not y or y >= 1877) else "Q129286"
        return "Q129286"                          # bare Pakistan / Afghan frontier
    if colony_qid == "Q924":
        hay = (_admins(place_qid) + " " + (place_label or "")).lower()
        return "Q3574782" if ("pemba" in hay or "zanzibar" in hay) else "Q158725"
    if colony_qid == "Q41":
        if place_label in IONIAN and 0 < y <= 1864:
            return "Q1063498"
        return None
    if colony_qid == "Q805":
        hay = (place_label or "").lower()
        if any(k in hay for k in ("mukalla", "hadhramaut", "yemen")):
            return "Q1865132"
        return "Q49910" if (not y or y >= 1937) else "Q17509767"
    if colony_qid == "Q1045":
        hay = (place_label or "").lower()
        if "jubaland" in hay:
            return "Q2538511"                     # Kenya until the 1925 cession
        if any(k in hay for k in ("berbera", "zeila", "zeyla")):
            return "Q662653"
        return None if y >= 1941 else "Q662653"   # 1941+ bare Somalia = BMA, keep
    if colony_qid == "Q148":
        hay = (_admins(place_qid) + " " + (place_label or "")).lower()
        if "tai po" in hay or "hong kong" in hay or "new territories" in hay:
            return "Q1054923"
        return None
    return None


def main():
    touched = collections.Counter()
    for corpus in ("data/kg", "data/iol"):
        for name in ("career_events", "career_facts", "places", "employment_edges"):
            p = ROOT / corpus / "graph_stage3" / f"{name}.jsonl"
            if not p.exists():
                continue
            out, n = [], 0
            for line in p.open():
                r = json.loads(line)
                q = r.get("colony_qid")
                if q:
                    y = r.get("year_start") or r.get("year_end")
                    nq = remap(q, r.get("place_qid") or r.get("qid"),
                               r.get("place_label") or r.get("place"), y)
                    if nq and nq != q:
                        touched[(q, nq)] += 1
                        r["colony_qid"] = nq
                        r["colony_label"] = LOCK.get(nq, r.get("colony_label"))
                        n += 1
                    elif q in RELABEL and r.get("colony_label") != RELABEL[q]:
                        r["colony_label"] = RELABEL[q]
                        n += 1
                out.append(json.dumps(r, ensure_ascii=False))
            if n:
                p.write_text("\n".join(out) + "\n")
            print(f"{corpus}/{name}: {n} rows touched")
    print("\nremap totals:")
    for (a, b), n in sorted(touched.items(), key=lambda x: -x[1]):
        print(f"  {a:9s} -> {b:11s} {LOCK.get(b, '?')[:40]:40s} {n:5,}")


if __name__ == "__main__":
    main()
