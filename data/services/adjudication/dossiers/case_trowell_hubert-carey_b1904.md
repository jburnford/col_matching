<!-- {"case_id": "case_trowell_hubert-carey_b1904", "bio_ids": ["trowell_hubert-carey_b1904"], "stint_ids": ["Trowell, H. C___Uganda___1939"]} -->
# Dossier case_trowell_hubert-carey_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `trowell_hubert-carey_b1904`

- Printed name: **TROWELL, Hubert Carey**
- Birth year: 1904 (attested in editions [1957])
- Honours: F.R.C.P, O.B.E
- Appears in editions: [1948, 1949, 1950, 1951, 1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L27919.v` — printed in editions [1957]:**

> TROWELL, H. C., O.B.E.—b. 1904; educ. Reigate Gram. Sch., St. Thos. Hosp. and Med. Sch.; M.O., Ken., 1929; Uga., 1935; specialist physcn., 1945; senr. specialist, 1954; African efficiency survey, K.U.R. and H., 1946; author Handbook for Dressers and Nurses in the Tropics; Diagnosis and Treatment in the Tropics; and articles in med. journals.

**Version `col1948-L36495.v` — printed in editions [1948, 1949, 1950, 1951]:**

> TROWELL, Hubert Carey, M.D. (Lond.), F.R.C.P.—b. 1904; ed. Reigate Gram. Sch. and St. Thomas' Hosp., London; med. offr., Ken., 1929; Uga., 1935; speclst. physcn., 1946; employed on African efficiency survey, Ken. and Uga. rlyws., 1946; author of Handbook for Dressers and Nurses in the Tropics, Diagnosis and Treatment in the Tropics, also of articles in medical journals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | M.O. | Kenya | [1948, 1949, 1950, 1951, 1957] |
| 1 | 1935 | M.O. | Uganda | [1948, 1949, 1950, 1951, 1957] |
| 2 | 1945 | specialist physcn | Uganda *(inherited from previous clause)* | [1957] |
| 3 | 1946 | African efficiency survey, K.U.R. and H | Kenya | [1948, 1949, 1950, 1951, 1957] |
| 4 | 1954 | senr. specialist | Uganda *(inherited from previous clause)* | [1957] |

## Candidate stint `Trowell, H. C___Uganda___1939`

- Staff-list name: **Trowell, H. C** | colony: **Uganda** | listed 1939–1951 | editions [1939, 1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. C. Trowell | Medical Officer | Medical | — | — |
| 1940 | H. C. Trowell | Medical Officer | Medical | — | — |
| 1949 | H. C. Trowell | Physicians | Medical | — | — |
| 1951 | H. C. Trowell | Physicians | MEDICAL | — | — |

### Deterministic checks: `trowell_hubert-carey_b1904` vs `Trowell, H. C___Uganda___1939`

- [PASS] surname_gate: bio 'TROWELL' vs stint 'Trowell, H. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1939, birth 1904 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1951
- [FAIL] position_sim: best 59 vs bar 60: 'specialist physcn' ~ 'Physicians'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Adjudication constraints (binding)

- The prime directive is NO FALSE MERGES. A missed link is recoverable; a
  wrong one silently corrupts the historical record. When in doubt, leave
  the stint unassigned.
- Surname identity is NOT evidence: every candidate here already shares the
  surname (it is the blocking key). Only position, place, dates, honours,
  initials/forenames, and edition co-occurrence count.
- Single-initial biographies (e.g. "J. Lewis") must never be merged on
  shared-stint or tenure-overlap evidence alone; they need a strong
  independent dimension (specific position match, shared honour, or
  multi-edition co-occurrence).
- A stint belongs to AT MOST one biography. If two biographies in this case
  could plausibly hold the same stint, assign it to neither.
- Respect hard chronology: nobody serves before age ~15 or after death.
- Generic junior titles (clerk, cadet, assistant) recur constantly; a title
  match alone on a common office is weak evidence.

