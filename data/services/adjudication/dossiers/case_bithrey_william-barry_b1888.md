<!-- {"case_id": "case_bithrey_william-barry_b1888", "bio_ids": ["bithrey_william-barry_b1888"], "stint_ids": ["Bithrey, W. B___Nyasaland___1922"]} -->
# Dossier case_bithrey_william-barry_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bithrey_william-barry_b1888`

- Printed name: **BITHREY, William Barry**
- Birth year: 1888 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L31212.v` — printed in editions [1948]:**

> BITHREY, William Barry.—b. 1888; ed. Perins Sch., Alfredest; trpr. B.S.A. police, S. Rhod., 1913; supt., Nyasa., 1920; comsnr., Nyasa., 1938; comsnr. of police, T.T., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | trpr. B.S.A. police | Southern Rhodesia | [1948] |
| 1 | 1920 | supt. | Nyasaland | [1948] |
| 2 | 1938 | comsnr. | Nyasaland | [1948] |
| 3 | 1942 | comsnr. of police, T.T | Nyasaland *(inherited from previous clause)* | [1948] |

## Candidate stint `Bithrey, W. B___Nyasaland___1922`

- Staff-list name: **Bithrey, W. B** | colony: **Nyasaland** | listed 1922–1940 | editions [1922, 1923, 1924, 1925, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. B. Bithrey | Depot Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1923 | W. B. Bithrey | Depot Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1924 | W. B. Bithrey | Depot Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1925 | W. B. Bithrey | Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1929 | W. B. Bithrey | Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1930 | W. B. Bithrey | Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1931 | W. B. Bithrey | Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1932 | W. B. Bithrey | Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1933 | W. B. Bithrey | Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1934 | W. B. Bithrey | Superintendents | Police, Prisons and Lunatic Asylums | — | — |
| 1936 | W. B. Bithrey | Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1937 | W. B. Bithrey | Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1940 | W. B. Bithrey | Chief Commissioner of Police and Chief Inspector of Prisons, Principal Immigration Officer and Registrar of Motor Vehicles | Police, Prisons and Lunatic Asylum | — | — |

### Deterministic checks: `bithrey_william-barry_b1888` vs `Bithrey, W. B___Nyasaland___1922`

- [PASS] surname_gate: bio 'BITHREY' vs stint 'Bithrey, W. B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1922, birth 1888 (age 34)
- [PASS] colony: 3 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1922-1940
- [FAIL] position_sim: best 44 vs bar 60: 'supt.' ~ 'Superintendent'
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

