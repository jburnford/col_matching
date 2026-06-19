<!-- {"case_id": "case_strachan_c-r-p_b1917", "bio_ids": ["strachan_c-r-p_b1917"], "stint_ids": ["Strachan, R___British Honduras___1932"]} -->
# Dossier case_strachan_c-r-p_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `strachan_c-r-p_b1917`

- Printed name: **STRACHAN, C. R. P.**
- Birth year: 1917 (attested in editions [1965])
- Appears in editions: [1965]

### Verbatim printed entry text (OCR)

**Version `col1965-L19460.v` — printed in editions [1965]:**

> STRACHAN, C. R. P.—b. 1917; ed. Skerrys Coll., Newcastle-on-Tyne, and Sunderland Tech. Coll.; U.K. hospital, 1939; mil. serv., 1943-46; supt. pharmacist, Malaya, 1950, ch. pharmacist, 1957-61; retd., apptd. ch. pharmacist, E. Nig., 1962. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939–1939 | hospital | United Kingdom | [1965] |
| 1 | 1943–1946 | mil. serv. | — | [1965] |
| 2 | 1950–1950 | supt. pharmacist | Malaya | [1965] |
| 3 | 1957–1961 | ch. pharmacist | — | [1965] |
| 4 | 1962–1962 | ch. pharmacist | Eastern Nigeria | [1965] |

## Candidate stint `Strachan, R___British Honduras___1932`

- Staff-list name: **Strachan, R** | colony: **British Honduras** | listed 1932–1937 | editions [1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | Mrs. R. Strachan | Matron | Industrial School, Pomona, Stann Creek | — | — |
| 1933 | R. Strachan | Matron | Industrial School, Pomona, Stann Creek | — | — |
| 1934 | R. Strachan | Matron | Industrial School, Pomona, Stann Creek | — | — |
| 1936 | Mrs. R. Strachan | Matron | Industrial School, Pomona, Stann Creek | — | — |
| 1937 | R. Strachan | Matron | Industrial School | — | — |

### Deterministic checks: `strachan_c-r-p_b1917` vs `Strachan, R___British Honduras___1932`

- [PASS] surname_gate: bio 'STRACHAN' vs stint 'Strachan, R' (exact)
- [PASS] initials: bio ['C', 'R', 'P'] ~ stint ['R']
- [PASS] age_gate: stint starts 1932, birth 1917 (age 15)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1937
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

