<!-- {"case_id": "case_parboosingh_ivan-samuel_b1905", "bio_ids": ["parboosingh_ivan-samuel_b1905"], "stint_ids": ["Parboosingh, I. S___Jamaica___1949"]} -->
# Dossier case_parboosingh_ivan-samuel_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `parboosingh_ivan-samuel_b1905`

- Printed name: **PARBOOSINGH, Ivan Samuel**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35105.v` — printed in editions [1948, 1949, 1950, 1951]:**

> PARBOOSINGH, Ivan Samuel, B.A. (hons.), M.D. (Penn.), D.T.M. (Liv.).—b. 1905; ed. Univ. of Pennsylvania and Liverpool Univ.; supernumerary, Spanish Twm. and Hordley Hosp., J'ca., 1935; D.M.O., Spanish Twm., 1936; senr. anaesthetist and emergency surgn., 1937; S.M.O., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | supernumerary, Spanish Twm. and Hordley Hosp. | Jamaica | [1948, 1949, 1950, 1951] |
| 1 | 1936 | D.M.O., Spanish Twm | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1937 | senr. anaesthetist and emergency surgn | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1943 | S.M.O | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Parboosingh, I. S___Jamaica___1949`

- Staff-list name: **Parboosingh, I. S** | colony: **Jamaica** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | I. S. Parboosingh | Senior Medical Officer | Medical | — | — |
| 1950 | I. S. Parboosingh | Senior Medical Officers | MEDICAL | — | — |

### Deterministic checks: `parboosingh_ivan-samuel_b1905` vs `Parboosingh, I. S___Jamaica___1949`

- [PASS] surname_gate: bio 'PARBOOSINGH' vs stint 'Parboosingh, I. S' (exact)
- [PASS] initials: bio ['I', 'S'] ~ stint ['I', 'S']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 4 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 16 vs bar 60: 'S.M.O' ~ 'Senior Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

