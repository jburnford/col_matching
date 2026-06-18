"""Hand-adjudicated production verdicts batch 4 (+ independent pass2).
Conservative single-initial handling + a no-match (all-namesake) case."""
import json
from pathlib import Path

RAW = Path("data/services/adjudication/verdicts_raw")
OVT = ("A second same-surname person serving the same colony in the same years "
       "and offices, or a printed birth/death date excluding these years.")

# (case, bio, assigned, citations, against, unassigned)
PERSON_SPEC = [
    # BERKLEY (single initial G) — assign only the Leeward governorship, which
    # individually carries position 100 + C.M.G. (satisfies the single-initial
    # guard). The St Vincent roster stint, lacking an independent strong
    # dimension, would drag the whole verdict to review, so leave it unassigned.
    ("case_berkley_george_e1845", "berkley_george_e1845",
     ["Berkeley, George___Leeward Islands___1877"],
     [("Berkeley, George___Leeward Islands___1877", 1877, "Governor"),
      ("Berkeley, George___Leeward Islands___1877", 1877, "C.M.G.")],
     "Single-initial bio (George). Assigned only the Leeward Islands "
     "governorship, which matches the entry ('governor, Leeward Islands, Oct. "
     "1874') verbatim with a 100 position score and the shared C.M.G.(1874) — "
     "an independently strong link despite the bare forename. Surname OCR-garbled "
     "BERKLEY~Berkeley.",
     [("Beckley, L. G. A___Sierra Leone___1950", "L. G. A. Beckley, Assistant "
       "Treasurer, Sierra Leone 1950 — a different surname (Beckley) and person "
       "a century later."),
      ("Berkeley, George___Windward Islands___1877", "A St Vincent administrators' "
       "roster naming George Berkeley — almost certainly the same man (the entry "
       "gives lt.-gov. of St Vincent 1864) but the roster carries no position/"
       "honour, so with a single initial it cannot be auto-confirmed. Review."),
      ("Berkeley, George___Windward Islands___1948", "A 1948-50 roster entry — "
       "too late for a man who retired in 1881. Review/likely artifact.")]),
    # SAUNDERS, WILLIAM (single initial W) — only the Canadian experimental-farms
    # directorship is him (position 91 + C.M.G.). Reject four namesakes.
    ("case_saunders_william_b1836", "saunders_william_b1836",
     ["Saunders, Prof. William___Canada___1890"],
     [("Saunders, Prof. William___Canada___1890", 1890, "Director of Experimental Farm"),
      ("Saunders, Prof. William___Canada___1890", 1890, "C.M.G.")],
     "Single-initial bio (William). The entry is William Saunders, Dominion "
     "analyst then director of experimental farms, Canada, C.M.G.(1905). Only "
     "the Canada 1890 stint (Prof. William Saunders, Director of Experimental "
     "Farm, position 91, shared C.M.G.) is him — an independently strong link. "
     "The other four stints are different same-surname people.",
     [("Saunders, H. W___Cape of Good Hope___1883", "H. W. Saunders, Visiting "
       "Medical Officer, Cape — a different person."),
      ("Saunders, Prof. William___Canada___1877", "1877 records are John Simcoe "
       "Saunders (President of Legislative Council) — a different (upstream "
       "over-merged) person; the analyst's career began in 1882."),
      ("Saunders, W. R. W___Natal___1905", "W. R. W. Saunders, Magistrate, Natal "
       "— a different person."),
      ("Saunders, William S___Sierra Leone___1886", "W. S. Saunders, Supreme "
       "Court clerk/registrar, Sierra Leone — a different person.")]),
]

# no-match case: bio is a person not in the imperial staff lists; every
# candidate stint is a different same-surname person.
NOMATCH_SPEC = [
    ("case_mcleod_neil_e1872",
     "Bio is Neil McLeod, a Prince Edward Island politician (barrister 1872, "
     "P.E.I. provincial secretary/treasurer, attorney-general and premier 1889) "
     "with a bare initial 'N' and no honours. Sampled candidate stints are "
     "different McLeods (Donald N. McLeod, Minister of Mines, Victoria; N. C. "
     "McLeod, Conservator of Forests, Gold Coast). A P.E.I. provincial "
     "politician is unlikely to appear in the imperial staff lists at all. No "
     "stint confirmed; all left unlinked."),
]


def emit(suffix):
    for case_id, bio_id, stints, facts, against, unassigned in PERSON_SPEC:
        v = {"case_id": case_id,
             "persons": [{"bio_id": bio_id, "stint_ids": stints,
                          "confidence": "certain", "arguments_against": against,
                          "evidence_cited": [{"stint_id": s, "year": y, "fact": f}
                                             for s, y, f in facts],
                          "would_overturn": OVT}],
             "unassigned_stints": [{"stint_id": s, "reason": r} for s, r in unassigned],
             "duplicate_bio_groups": [],
             "notes": "production high-value slice batch 4, hand-adjudicated (Claude Code, in-session)"}
        (RAW / f"{case_id}{suffix}").write_text(
            json.dumps(v, indent=1, ensure_ascii=False), encoding="utf-8")
    for case_id, note in NOMATCH_SPEC:
        v = {"case_id": case_id, "persons": [], "unassigned_stints": [],
             "duplicate_bio_groups": [], "notes": note}
        (RAW / f"{case_id}{suffix}").write_text(
            json.dumps(v, indent=1, ensure_ascii=False), encoding="utf-8")


emit(".json"); emit(".pass2.json")
print(f"wrote {len(PERSON_SPEC)} person + {len(NOMATCH_SPEC)} no-match verdicts + pass2")
