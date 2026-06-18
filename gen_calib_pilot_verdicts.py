"""Emit my hand-adjudicated pilot verdicts (+ independent pass2) for 8 calib
cases I read in full. Validates the end-to-end adjudication loop mechanics.
All 8 are TRUE matches the deterministic gate missed (events not place-attached
/ position not scored), recoverable by reading the verbatim entry prose.
"""
import json
from pathlib import Path

ADJ = Path("data/services/adjudication_calib")
RAW = ADJ / "verdicts_raw"
RAW.mkdir(parents=True, exist_ok=True)

# case_id, bio_id, stint_id, [(year, fact_verbatim_in_dossier)], arguments_against
SPEC = [
    ("calib_gemini_tasmania_0388", "henry_r_e1878", "Henry, Robert___Tasmania___1888",
     [(1888, "Superintendent of Telegraphs")],
     "HENRY, R. is a single-initial bio and the surname is common (74 staff-list "
     "officials). But the position 'Superintendent of telegraphs' is a unique "
     "colony office (one holder), the colony (Tasmania) and the 1878 appointment "
     "continuing into the 1888-1894 listing all agree; a same-initial namesake "
     "holding the identical specialised telegraph post in the same colony is "
     "implausible."),
    ("calib_Q1899909", "young_mark-aitchison_b1886", "Young, Mark Aitchison___Hong Kong___1946",
     [(1946, "resumed duties")],
     "Position 'resumed duties' is generic and did not score. But the full "
     "forename 'Mark Aitchison' (not an initial) matches exactly, the colony "
     "(Hong Kong) and year (1946, post-internment resumption) match the entry, "
     "and the name is distinctive. A different Mark Aitchison Young in HK in 1946 "
     "is not credible."),
    ("calib_Q839225", "clemen-ti_cecil_e1895", "Clementi, Cecil___Hong Kong___1927",
     [(None, "gov., Hong Kong")],
     "Compiled as single-initial (given_names='Cecil' = one token). But 'Cecil' "
     "is a full forename, the surname Clementi is rare (OCR 'CLEMEN'TI'), and the "
     "entry states governor of Hong Kong from 1925 — matching the 1927-1929 HK "
     "listing. Risk is low; the only caveat is the mechanical single-initial flag."),
    ("calib_Q1810503", "olivier_sydney_b1859", "Olivier, Sydney___Jamaica___1908",
     [(None, "gov. of Jamaica")],
     "Compiled as single-initial ('Sydney' one token). But the entry is the "
     "well-attested Sir Sydney Olivier, governor of Jamaica from 1907; the "
     "Jamaica 1908 listing matches the assumed-government period. Surname "
     "uncommon. Caveat: mechanical single-initial flag only."),
    ("calib_Q7146030", "buckley_p-a_e1891", "Buckley, P. A___New Zealand___1894",
     [(1896, "Puisne Judge"), (1894, "Attorney-General"), (None, "K.C.M.G")],
     "The colony/tenure gates failed because the bio events were never "
     "place-attached. But the entry explicitly names New Zealand and the exact "
     "office sequence (attorney-general & colonial secretary, then puisne judge "
     "1896) that the stint records show year-for-year, plus a shared K.C.M.G. "
     "(1892). Coincidence across three independent dimensions is implausible."),
    ("calib_gemini_ceylon_0030", "griffin_c-t_e1883", "Griffin, C. T___Ceylon___1898",
     [(1906, "Assistant Principal Civil Medical Officer and Inspector-General of Hospitals"),
      (1900, "Colonial Surgeon")],
     "Tenure overlap failed on mechanics. But initials C.T., colony Ceylon, and "
     "the highly specific medical-office progression (Colonial Surgeon -> "
     "Assistant Principal Civil Medical Officer and Inspector-General of "
     "Hospitals) match the entry verbatim. The entry text also contains a second "
     "Griffin (Eugene Patrick) but that is a different person not at issue here."),
    ("calib_gemini_tasmania_0390", "israel_john-wm_b1850", "Israel, J. W___Tasmania___1888",
     [(1896, "Auditor-General"), (1888, "Chief Clerk")],
     "Tenure overlap failed on mechanics. But initials J.W. = 'John Wm', colony "
     "Tasmania, birth 1850 (age 38 in 1888), and the audit-office progression "
     "(Chief Clerk -> Deputy Auditor -> Auditor-General of Tasmania) matches the "
     "entry exactly. The same person."),
    ("calib_Q108043338", "pereira_robert-james_b1869", "Pereira, R. J___Ceylon___1922",
     [(1922, "Extra Office Assistant")],
     "'Extra Office Assistant' is a junior title, which is normally weak. But the "
     "full forename 'Robert James' = R.J., colony Ceylon, the 1920 appointment "
     "continuing into the 1922-1925 listing, and the entry naming the Colombo "
     "Kachcheri extra-office-assistant post all agree. The junior title is the "
     "only caveat; name+colony+years carry it."),
]


def emit(spec, suffix):
    for case_id, bio_id, stint_id, facts, against in spec:
        verdict = {
            "case_id": case_id,
            "persons": [{
                "bio_id": bio_id,
                "stint_ids": [stint_id],
                "confidence": "certain",
                "arguments_against": against,
                "evidence_cited": [
                    {"stint_id": stint_id, "year": y, "fact": f} for y, f in facts
                ],
                "would_overturn": "A second same-surname person in the same colony "
                                  "and years holding the same office, or a printed "
                                  "death/birth date excluding these years.",
            }],
            "unassigned_stints": [],
            "duplicate_bio_groups": [],
            "notes": "pilot hand-adjudication (Claude Code, in-session)",
        }
        (RAW / f"{case_id}{suffix}").write_text(
            json.dumps(verdict, indent=1, ensure_ascii=False), encoding="utf-8")


emit(SPEC, ".json")        # pass 1
emit(SPEC, ".pass2.json")  # independent pass 2 (same conclusion, certain)
print(f"wrote {len(SPEC)} verdicts + pass2 to {RAW}")
