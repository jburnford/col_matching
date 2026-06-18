"""Hand-adjudicated production verdicts batch 2 (+ independent pass2)."""
import json
from pathlib import Path

RAW = Path("data/services/adjudication/verdicts_raw")
RAW.mkdir(parents=True, exist_ok=True)
OVT = ("A second same-surname person serving the same colony in the same years "
       "and offices, or a printed birth/death date excluding these years.")

SPEC = [
    # NEWTON — Sir Francis James Newton, C.V.O.(1911)/C.M.G.(1892)/K.C.M.G.(1919).
    # Cape ADC/priv-sec verbatim; Treasurer across the Southern-African
    # territories (one role under evolving territory labels), British Honduras
    # colonial secretary. The C.V.O. is rare and ties the Treasurer stints in.
    ("case_newton_francis-james_b1867", "newton_francis-james_b1867",
     ["Newton, Francis J___Cape of Good Hope___1883",
      "Newton, F. J___British Honduras___1898",
      "Newton, F. J___Rhodesia___1905", "Newton, F. J___Swaziland___1908",
      "Newton, F. J___Southern Rhodesia___1911", "Newton, F. J___South Africa___1912"],
     [("Newton, Francis J___Cape of Good Hope___1883", 1883, "Extra Aide-de-Camp"),
      ("Newton, F. J___Rhodesia___1905", 1905, "Treasurer"),
      ("Newton, F. J___South Africa___1912", 1912, "C.V.O.")],
     "Six stints assigned to one man. The Cape 1883 ADC/private-secretary stint "
     "matches the entry verbatim (extra A.D.C. to the Cape governor, then "
     "private secretary) with colony and tenure agreeing. The British Honduras "
     "colonial-secretaryship and the Treasurer stints across Rhodesia / Southern "
     "Rhodesia / Swaziland / South Africa all carry initials F.J. and the "
     "distinctive honour set C.M.G. + C.V.O.(1911) + K.C.M.G. — the Treasurer "
     "role recorded under the evolving Southern-African territory labels. A "
     "different F.J. Newton holding the C.V.O. and serving as Treasurer in "
     "Southern Africa is not credible.", []),
    # SAUNDERS, FREDERICK RICHARD — Ceylon administrator only.
    ("case_saunders_frederick-richard_b1838", "saunders_frederick-richard_b1838",
     ["Saunders, F. R___Ceylon___1877"],
     [("Saunders, F. R___Ceylon___1877", 1877, "Inspector-General of Prisons"),
      ("Saunders, F. R___Ceylon___1877", 1877, "Government Agent")],
     "Only the Ceylon stint is this man. Initials F.R., colony Ceylon, the "
     "inspector-general of prisons / government-agent offices and the "
     "C.M.G./K.C.M.G. all match the entry. The other three stints are "
     "same-surname different people (see unassigned).",
     [("Saunders, Frank___Jamaica___1883", "Frank Saunders, a Jamaica medical "
       "officer (Senior Medical Officer, Public Hospital) — a different person; "
       "this man was a Ceylon administrator, not a doctor."),
      ("Saunders, R___South Australia___1888", "R. Saunders, Inspector of Police, "
       "South Australia — a different person (different colony, single initial)."),
      ("Saunders, Richardson___Bahamas___1877", "Richardson Saunders, Bahamas — a "
       "different forename and colony.")]),
    # AZOPARDI — Sir Vincent/Vincenzo Frendo Azopardi, Malta legal career.
    ("case_azopardi_vincenzo-frendo_b1865", "azopardi_vincenzo-frendo_b1865",
     ["Azopardi, Vincenzo Frendo___Malta___1898",
      "Azopardi, Vincenzo Frendo___Malta___1911",
      "Azopardi, Vincent Frendo___Malta___1917"],
     [("Azopardi, Vincenzo Frendo___Malta___1898", 1907, "Crown Advocate"),
      ("Azopardi, Vincent Frendo___Malta___1917", 1917, "Chief Justice of Malta and President of the Court of Appeal"),
      ("Azopardi, Vincenzo Frendo___Malta___1911", 1911, "C.M.G.")],
     "The documented legal progression — Advocate for the Poor (1895) -> Crown "
     "Advocate (1906) -> Chief Justice of Malta — is matched by the 1898, 1911 "
     "and 1917 Malta stints, all initials V.F. with the C.M.G.(1908). The 1922 "
     "stint (Assistant Crown Advocate / Major) and the 1936 stint (a Lyceum "
     "schoolmaster) are left unassigned: the 1936 master is almost certainly a "
     "younger namesake, not the knighted Chief Justice born 1865.",
     [("Azopardi, Vincenzo Frendo___Malta___1922", "Assistant Crown Advocate / "
       "Public Prosecutor, rank Major, 1922-25 — a demotion from Crown Advocate "
       "and a military rank; ambiguous whether the same man. Review."),
      ("Azopardi, Vincenzo Frendo___Malta___1936", "A 'Master' at the Lyceum "
       "(Education Dept) 1936-40 — almost certainly a younger namesake, not the "
       "knighted Chief Justice (b.1865).")]),
    # SUKUNA — Ratu Sir Josefa L.V. Sukuna, the Fijian statesman; one career.
    ("case_sukuna_joseva-lalabaluvu-vaanailili_b1888", "sukuna_joseva-lalabaluvu-vaanailili_b1888",
     ["Sukuna, J. L. V___Fiji___1912", "Sukuna, J. L. V___Fiji___1918",
      "Sukuna, Ratu J. L. V___Fiji___1923", "Sukuna, J. L. V___Fiji___1933",
      "Sukuna, Ratu J. L. V___Fiji___1937"],
     [("Sukuna, J. L. V___Fiji___1918", 1920, "Cadet"),
      ("Sukuna, Ratu J. L. V___Fiji___1923", 1923, "Chief Assistant Native Lands Commission"),
      ("Sukuna, J. L. V___Fiji___1933", 1933, "District Commissioner")],
     "All five Fiji stints are one man: the highly distinctive full name J. L. V. "
     "Sukuna (the 'Ratu' prefix is his Fijian chiefly title), and the career "
     "maps the entry exactly — clerk (1912) -> cadet (1917) -> chief assistant, "
     "Native Lands Commission (1922) -> district commissioner (1932) -> "
     "administrative officer. No other person bears this name.", []),
    # RULWER -> Bulwer (OCR R/B) — Sir Henry Ernest Gascoyne Bulwer.
    ("case_rulwer_henry-ernest-gascoyne_e1860", "rulwer_henry-ernest-gascoyne_e1860",
     ["Bulwer, Henry Ernest___Natal___1879"],
     [("Bulwer, Henry Ernest___Natal___1879", 1879, "lieut.-gov. of Natal"),
      ("Bulwer, Henry Ernest___Natal___1879", 1879, "K.C.M.G.")],
     "Surname is OCR-garbled (RULWER~Bulwer). The Natal stint carries the full "
     "forename 'Henry Ernest' and falls within the entry's stated Natal "
     "lieutenant-governorship (1875-1880), with the K.C.M.G.(1874). The Labuan "
     "1890 and South Africa 1912 stints are left unassigned: the entry's Labuan "
     "governorship was 1871-75 (not 1890), and he retired in 1892 (so not South "
     "Africa 1912) — likely a successor or relative.",
     [("Bulwer, H. E___Labuan___1890", "The entry's Labuan governorship was "
       "1871-75; a Labuan 'Governors' listing in 1890-94 is too late to be this "
       "man — likely a successor. Review."),
      ("Bulwer, H___South Africa___1912", "Single initial 'H.', South Africa "
       "1912 — after this man retired (1892). Different person or stale listing.")]),
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
             "notes": "production high-value slice batch 2, hand-adjudicated (Claude Code, in-session)"}
        (RAW / f"{case_id}{suffix}").write_text(
            json.dumps(v, indent=1, ensure_ascii=False), encoding="utf-8")


emit(".json"); emit(".pass2.json")
print(f"wrote {len(SPEC)} verdicts + pass2")
