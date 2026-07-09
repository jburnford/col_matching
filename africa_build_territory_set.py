#!/usr/bin/env python3
"""Curated 'British Africa' territory set for the Woldense-style mobility paper.

Hand-vetted from the 64 colony nodes whose coords/labels fall in/near Africa
(see africa_build_persons.py for provenance). Each INCLUDE territory gets a
region tag and a `canonical` id that folds pure sequential RENAMES of the same
administrative area (so a 1920 rename does not read as a career "transfer").

EXCLUDED as not-British-Africa: the Mediterranean fortress colonies (Malta,
Gibraltar, Cyprus), the Levant/Mandate territories (Palestine, Transjordan,
Iraq, Israel), the Arabian/Gulf protectorates (all Aden nodes, Bahrain, Kuwait,
Qatar, Trucial States), and Greece (Ionian residue).

DESIGN CALLS flagged for Jim + Josef (edit here, re-run downstream):
  - Egypt (Q127861) & Anglo-Egyptian Sudan (Q541455): INCLUDED but tagged
    region 'NE_condominium' so they can be toggled in a sensitivity run
    (occupation 1882 / veiled protectorate / condominium — not a normal colony).
  - Renames FOLDED (canonical): East Africa Protectorate->Kenya;
    British Central Africa->Nyasaland; bare modern 'South Africa' Q258->Union.
  - Renames NOT folded (kept as distinct branches, pending decision): the
    Nigeria sub-units (Lagos / Oil Rivers / S. Nigeria / N. Nigeria / amalgamated
    Nigeria), the Orange chain (Sovereignty/Free State/River Colony), the four
    pre-1910 South African colonies vs the 1910 Union, and BSAC vs the two
    Rhodesias. These were genuinely separate administrations for much of the
    period; folding them is a substantive choice, not a data-cleaning one.
"""
import json, os

# qid -> (label, region, canonical_qid_or_None_for_self)
TERRITORIES = {
    # --- West Africa ---
    "Q2046345": ("Colony and Protectorate of Nigeria", "West", None),
    "Q585408":  ("Northern Nigeria", "West", None),
    "Q2062030": ("Southern Nigeria Protectorate", "West", None),
    "Q472146":  ("Lagos Colony", "West", None),
    "Q2566427": ("Oil Rivers Protectorate", "West", None),
    "Q1806380": ("Royal Niger Company Territory", "West", None),
    "Q503623":  ("British Gold Coast", "West", None),
    "Q96372444":("Ashanti", "West", None),
    "Q1998749": ("Northern Territories of the Gold Coast", "West", None),
    "Q30059027":("Sierra Leone Colony and Protectorate", "West", None),
    "Q3557236": ("Gambia Colony and Protectorate", "West", None),
    "Q1028835": ("British Cameroons", "West", None),
    "Q797527":  ("British Togoland", "West", None),
    "Q205022":  ("Fernando Po (British)", "West", None),
    # --- East Africa ---
    "Q2538511": ("Kenya, Colony & Protectorate of", "East", None),
    "Q876185":  ("East Africa Protectorate", "East", "Q2538511"),   # -> Kenya (1920 rename)
    "Q1097943": ("Uganda", "East", None),
    "Q158725":  ("Tanganyika Territory", "East", None),
    "Q3574782": ("Zanzibar", "East", None),
    # --- Central Africa ---
    "Q953903":  ("Northern Rhodesia", "Central", None),
    "Q750583":  ("Southern Rhodesia", "Central", None),
    "Q5155572": ("British South Africa Company Territory", "Central", None),
    "Q1649306": ("Nyasaland", "Central", None),
    "Q2642989": ("British Central Africa Protectorate", "Central", "Q1649306"),  # -> Nyasaland (1907)
    "Q654342":  ("Federation of Rhodesia and Nyasaland", "Central", None),
    # --- Southern Africa ---
    "Q370736":  ("Cape Colony", "Southern", None),
    "Q1301901": ("Colony of Natal", "Southern", None),
    "Q1187978": ("Transvaal Colony (First British)", "Southern", None),
    "Q550374":  ("South African Republic (Restored)", "Southern", None),
    "Q193619":  ("Union of South Africa", "Southern", None),
    "Q258":     ("South Africa", "Southern", "Q193619"),           # modern-QID -> Union
    "Q1142179": ("Orange River Colony", "Southern", None),
    "Q218023":  ("Orange Free State", "Southern", None),
    "Q3048062": ("Orange River Sovereignty", "Southern", None),
    "Q2547918": ("Griqualand West", "Southern", None),
    "Q729768":  ("Zululand", "Southern", None),
    "Q2340665": ("Basutoland", "Southern", None),
    "Q1050":    ("Swaziland", "Southern", None),
    "Q747314":  ("Bechuanaland Protectorate", "Southern", None),
    "Q4530733": ("British Bechuanaland", "Southern", None),
    "Q953068":  ("South-West Africa", "Southern", None),
    # --- North-East / Horn (condominium/occupation — toggle-able) ---
    "Q127861":  ("Egypt", "NE_condominium", None),
    "Q541455":  ("Sudan, Anglo-Egyptian", "NE_condominium", None),
    "Q662653":  ("British Somaliland", "Horn", None),
    "Q1045":    ("Somalia (British Military Administration)", "Horn", None),
    # --- Indian Ocean islands (off Africa) ---
    "Q12053604":("Mauritius", "IndianOcean", None),
    "Q21821453":("Seychelles", "IndianOcean", None),
    # --- South Atlantic ---
    "Q34497":   ("St. Helena", "SAtlantic", None),
}

def main():
    out = {}
    for qid, (label, region, canon) in TERRITORIES.items():
        out[qid] = {"label": label, "region": region,
                    "canonical": canon or qid,
                    "canonical_label": TERRITORIES.get(canon, (label,))[0] if canon else label}
    os.makedirs("data/africa", exist_ok=True)
    with open("data/africa/africa_territories.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    import collections
    byr = collections.Counter(v["region"] for v in out.values())
    ncanon = len({v["canonical"] for v in out.values()})
    print(f"territories: {len(out)}  canonical (rename-folded): {ncanon}")
    print("by region:", dict(byr))
    print("folded renames:")
    for qid,(label,region,canon) in TERRITORIES.items():
        if canon: print(f"   {label}  ->  {TERRITORIES[canon][0]}")

if __name__ == "__main__":
    main()
