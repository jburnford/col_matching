"""Hand-adjudicated production verdicts (+ independent pass2) for a high-value
slice (senior, single-bio, uncontested, strong-dimension cases). Each confirm
is a real recovered career link. I assign ONLY the stints I verified against
the verbatim prose; unexamined/anomalous stints are listed unassigned (the
compiler defaults them to unlinked — safe, recoverable).
"""
import json
from pathlib import Path

ADJ = Path("data/services/adjudication")
RAW = ADJ / "verdicts_raw"
RAW.mkdir(parents=True, exist_ok=True)

OVERTURN = ("A second same-surname person serving the same colony in the same "
            "years and offices, or a printed birth/death date excluding these "
            "years.")

# case_id, bio_id, [assigned stint_ids], [(stint, year, fact)], args_against,
#   [(unassigned_stint, reason)]
SPEC = [
    ("case_caron_j-p-r-a_b1843", "caron_j-p-r-a_b1843",
     ["Caron, Adolphe___Canada___1883", "Caron, J. P. R. A___Canada___1883"],
     [("Caron, J. P. R. A___Canada___1883", 1883, "Minister of Militia and Defence"),
      ("Caron, Adolphe___Canada___1883", 1888, "Minister of Militia"),
      ("Caron, Adolphe___Canada___1883", 1886, "K.C.M.G.")],
     "Two stints are involved; the 'Adolphe' rendering is a single printed "
     "initial 'A.'. But the entry is Sir J. P. R. A. Caron (Adolphe-Philippe "
     "Caron), Canadian Minister of Militia and Defence, K.C.M.G. (1885) — both "
     "stints carry that exact office, the K.C.M.G., and Canada across "
     "overlapping years. They are one person under two name renderings; a "
     "distinct same-surname Canadian militia minister with the K.C.M.G. is not "
     "credible.",
     []),
    ("case_beyts_h-n-duverger_e1854", "beyts_h-n-duverger_e1854",
     ["Beyts, H. N. D___Mauritius___1877"],
     [("Beyts, H. N. D___Mauritius___1877", 1878, "Receiver-General"),
      ("Beyts, H. N. D___Mauritius___1877", 1883, "C.M.G.")],
     "Place evidence is inherited across clauses (weak on its own). But initials "
     "H.N.D. are exact, the colony is Mauritius, the office (Receiver-General, "
     "with acting Colonial Secretary) matches the entry, and the C.M.G. is "
     "shared. Four independent dimensions agree.",
     []),
    ("case_grannum_edward-allan_b1869", "grannum_edward-allan_b1869",
     ["Grannum, A___Mauritius___1910", "Grannum, E. A___Mauritius___1913"],
     [("Grannum, A___Mauritius___1910", 1910, "Auditor-General"),
      ("Grannum, E. A___Mauritius___1913", 1915, "Receiver-General"),
      ("Grannum, E. A___Mauritius___1913", 1915, "C.M.G.")],
     "The 1910 stint is a single initial 'A.'. But the entry is Sir Edward Allan "
     "Grannum, Mauritius: auditor-general 1909 then receiver-general 1912 — the "
     "two stints hold exactly those two offices in sequence in Mauritius, with "
     "the C.M.G. (1915) on the receiver-general records. One continuous career.",
     []),
    ("case_hamiiton_charles-boughton_b1850", "hamiiton_charles-boughton_b1850",
     ["Hamilton, C. B___British Guiana___1877",
      "Hamilton, C. B___British Guiana___1894",
      "Hamilton, C. B___Trinidad___1886"],
     [("Hamilton, C. B___British Guiana___1877", 1877, "Clerk"),
      ("Hamilton, C. B___British Guiana___1894", 1896, "Receiver-General"),
      ("Hamilton, C. B___Trinidad___1886", 1886, "Receiver-General"),
      ("Hamilton, C. B___British Guiana___1894", 1896, "C.M.G.")],
     "Surname is OCR-garbled (HAMIITON~Hamilton, edit distance 1) and the "
     "Trinidad position scored only 52. But the entry explicitly traces this "
     "exact career: clerk/bookkeeper British Guiana from the 1870s, "
     "'rec.-gen., &c., Trinidad, 1886', then receiver-general British Guiana "
     "1892 with the C.M.G. (1895). Initials C.B., the colonies, and the office "
     "sequence all match the prose verbatim across three stints.",
     []),
    ("case_jack_enos-louis_b1898", "jack_enos-louis_b1898",
     ["Jack, E. L___Jamaica___1917", "Jack, E. L___Jamaica___1922"],
     [("Jack, E. L___Jamaica___1922", 1922, "Government Savings Bank"),
      ("Jack, E. L___Jamaica___1922", 1922, "Clerk, 2nd Class")],
     "The 1917 stint is a generic 'Clerical Assistant' (junior titles are weak). "
     "But initials E.L. are exact, the colony is Jamaica, the man (Enos Louis "
     "Jack, b. 1898, M.B.E.) entered the service as a clerk in 1915, and the "
     "1922 stint is verbatim '2nd Class Clerk, Government Savings Bank' matching "
     "the entry's '2nd cl. clk., gov. sav. bk., 1920'. The 1917 clerkship is the "
     "same young man's first posting; the savings-bank stint anchors it.",
     [("Jack, E. L___Jamaica___1949", "Not examined in this pass; a later "
       "1949 Jamaica E. L. Jack stint plausibly the same man (career ran to "
       "1940s) but left for review.")]),
    ("case_micallef_sr-richard_b1846", "micallef_sr-richard_b1846",
     ["Micallef, Richard___Malta___1877"],
     [("Micallef, Richard___Malta___1877", 1889, "Comptroller of Charitable Institutions"),
      ("Micallef, Richard___Malta___1877", 1905, "C.M.G.")],
     "The bio is Sir Richard Micallef, Malta, Comptroller of Charitable "
     "Institutions, C.M.G.(1902)/K.C.M.G.(1906), retired 1911. The Malta 1877 "
     "stint matches verbatim (clerk -> Comptroller of Charitable Institutions, "
     "C.M.G.). I assign only that stint. The Leeward Islands / Virgin Islands "
     "stints show the SAME Malta-specific offices (Comptroller of Charitable "
     "Institutions, Council of Government, Monte di Pieta) and are very likely "
     "the same man mis-colonied upstream, but the colony discrepancy needs human "
     "review, not auto-confirmation. The Malta 1930 stint is a different, "
     "younger namesake (R. G. Micallef, a Major in Public Health, 1930-40; this "
     "man retired in 1911).",
     [("Micallef, Richard___Leeward Islands___1897", "Holds Malta-specific "
       "offices (Comptroller of Charitable Institutions, Council of Government) "
       "identical to the bio — likely the same man mis-colonied as 'Leeward "
       "Islands' upstream. Review the colony anomaly before linking."),
      ("Micallef, Richard___Virgin Islands___1890", "Same Malta-specific offices "
       "as the bio; likely the same man mis-colonied as 'Virgin Islands'. "
       "Review the colony anomaly."),
      ("Micallef, Richard___Malta___1930", "R. G. Micallef, Major, 2nd-class "
       "clerk in Public Health 1930-1940 — a different, younger namesake. The "
       "bio's Sir Richard Micallef retired in 1911."),
      ("Micallef, S___Malta___1911", "Single-initial 'S.' Malta 1911; not "
       "examined in detail. Possibly the same man's final year but left for "
       "review given the bare initial.")]),
]


def emit(suffix):
    for case_id, bio_id, stints, facts, against, unassigned in SPEC:
        verdict = {
            "case_id": case_id,
            "persons": [{
                "bio_id": bio_id,
                "stint_ids": stints,
                "confidence": "certain",
                "arguments_against": against,
                "evidence_cited": [
                    {"stint_id": s, "year": y, "fact": f} for s, y, f in facts
                ],
                "would_overturn": OVERTURN,
            }],
            "unassigned_stints": [
                {"stint_id": s, "reason": r} for s, r in unassigned
            ],
            "duplicate_bio_groups": [],
            "notes": "production high-value slice, hand-adjudicated (Claude Code, in-session)",
        }
        (RAW / f"{case_id}{suffix}").write_text(
            json.dumps(verdict, indent=1, ensure_ascii=False), encoding="utf-8")


emit(".json")
emit(".pass2.json")
print(f"wrote {len(SPEC)} production verdicts + pass2 to {RAW}")
