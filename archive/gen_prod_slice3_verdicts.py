"""Hand-adjudicated production verdicts batch 3 (+ independent pass2)."""
import json
from pathlib import Path

RAW = Path("data/services/adjudication/verdicts_raw")
OVT = ("A second same-surname person serving the same colony in the same years "
       "and offices, or a printed birth/death date excluding these years.")

SPEC = [
    # NATHAN — Col. Sir Matthew Nathan, gov. Gold Coast(1900)/HK(1903)/Natal/Qld.
    ("case_nathan_sr-matthew_b1862", "nathan_sr-matthew_b1862",
     ["Nathan, Matthew___Hong Kong___1905", "Nathan, Matthew___Gold Coast___1922",
      "Nathan, Matthew___Gold Coast___1946"],
     [("Nathan, Matthew___Hong Kong___1905", 1905, "Governor"),
      ("Nathan, Matthew___Gold Coast___1946", 1946, "Governor"),
      ("Nathan, Matthew___Hong Kong___1905", 1905, "K.C.M.G")],
     "Sir Matthew Nathan is a singular figure. The Hong Kong 1905 stint is his "
     "contemporaneous governorship (the entry states gov. Hong Kong from 1903), "
     "colony and tenure agreeing. The two Gold Coast 'Governors' records "
     "(1922, 1946) are retrospective rosters of past Gold Coast governors — he "
     "governed the Gold Coast from 1900 per the entry — naming 'Sir Matthew "
     "Nathan, K.C.M.G.' His distinctive name and the shared K.C.M.G. make a "
     "different person implausible; the only caveat is that the Gold Coast "
     "records are historical-roster years, not his 1900-04 tenure years.", []),
    # CHAMPION — Sir Reginald Stuart Champion, Palestine then Aden (gov. 1944).
    ("case_champion_reginald-stuart_b1895", "champion_reginald-stuart_b1895",
     ["Champion, R. S___Palestine___1923", "Champion, Reginald Stuart___Aden___1929",
      "Champion, Reginald Stuart___Aden___1946"],
     [("Champion, R. S___Palestine___1923", 1923, "District Officer"),
      ("Champion, Reginald Stuart___Aden___1929", 1933, "Protectorate Secretary and District Magistrate"),
      ("Champion, Reginald Stuart___Aden___1946", 1948, "Governor")],
     "One continuous career, initials R.S. throughout. The entry traces "
     "Palestine civil administration (district officer) from 1920, secondment "
     "to Aden as political/protectorate secretary 1928-34, then governor and "
     "commander-in-chief of Aden 1944 — matched exactly by the Palestine 1923, "
     "Aden 1929, and Aden 1946 stints, the last carrying the K.C.M.G.(1946) and "
     "O.B.E.(1934). No competing R. S. Champion exists.", []),
    # LOGAN — Sir William Marston Logan (W.M., administrator). REJECT the
    # W.E.M. Logan forestry stints (a different man).
    ("case_logan_william-marston_b1889", "logan_william-marston_b1889",
     ["Logan, W. M___Kenya___1924", "Logan, W. M___Northern Rhodesia___1939"],
     [("Logan, W. M___Kenya___1924", 1924, "Senior Assistant Secretary"),
      ("Logan, W. M___Northern Rhodesia___1939", 1939, "Chief Secretary"),
      ("Logan, W. M___Northern Rhodesia___1939", 1939, "C.M.G.")],
     "Two distinct Logans share this surname. Sir William Marston Logan (W.M., "
     "b.1889) is an ADMINISTRATOR: the entry gives senior assistant secretary "
     "Kenya from 1924 (O.B.E.) and chief secretary Northern Rhodesia 1937 "
     "(C.M.G.) — matched by the two W. M. Logan stints assigned here. The three "
     "'W. E. M. Logan' stints (Kenya/Tanganyika/Uganda, 1949-62) are a "
     "FORESTER (Conservator of Forests) with a different middle initial and an "
     "entirely different career — a different person, left unassigned.",
     [("Logan, W. E. M___Kenya___1949", "W. E. M. Logan, Assistant Conservator "
       "of Forests — a forester, different middle initial; not this administrator."),
      ("Logan, W. E. M___Tanganyika___1956", "W. E. M. Logan, Deputy Chief "
       "Conservator of Forests — the forester, not this man."),
      ("Logan, W. E. M___Uganda___1959", "W. E. M. Logan, Chief Conservator of "
       "Forests — the forester, not this man.")]),
]


def emit(suffix):
    for case_id, bio_id, stints, facts, against, unassigned in SPEC:
        v = {"case_id": case_id,
             "persons": [{"bio_id": bio_id, "stint_ids": stints,
                          "confidence": "certain", "arguments_against": against,
                          "evidence_cited": [{"stint_id": s, "year": y, "fact": f}
                                             for s, y, f in facts],
                          "would_overturn": OVT}],
             "unassigned_stints": [{"stint_id": s, "reason": r} for s, r in unassigned],
             "duplicate_bio_groups": [],
             "notes": "production high-value slice batch 3, hand-adjudicated (Claude Code, in-session)"}
        (RAW / f"{case_id}{suffix}").write_text(
            json.dumps(v, indent=1, ensure_ascii=False), encoding="utf-8")


emit(".json"); emit(".pass2.json")
print(f"wrote {len(SPEC)} verdicts + pass2")
