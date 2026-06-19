<!-- {"case_id": "case_guise_christopher-probyn_b1899", "bio_ids": ["guise_christopher-probyn_b1899"], "stint_ids": ["Guise, C. P___Nyasaland___1928"]} -->
# Dossier case_guise_christopher-probyn_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `guise_christopher-probyn_b1899`

- Printed name: **GUISE, Christopher Probyn**
- Birth year: 1899 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33045.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GUISE, Christopher Probyn.—b. 1899; ed. Christ's Hosp. and Cheltenham; on mil. serv. 1917-19, capt.; police cadet, Nyasa., 1925; asst. supt., 1927; supt., 1944; senr. supt., T.T., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | police cadet | Nyasaland | [1948, 1949, 1950, 1951] |
| 1 | 1927 | asst. supt | Nyasaland *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1944 | supt | Nyasaland *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Guise, C. P___Nyasaland___1928`

- Staff-list name: **Guise, C. P** | colony: **Nyasaland** | listed 1928–1940 | editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | C. P. Guise | Cadets | Police, Prisons and Lunatic Asylum | — | — |
| 1929 | C. P. Guise | Assistant Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1930 | C. P. Guise | Assistant Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1931 | C. P. Guise | Assistant Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1932 | C. P. Guise | Assistant Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1933 | C. P. Guise | Assistant Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1934 | C. P. Guise | Assistant Superintendents | Police, Prisons and Lunatic Asylums | — | — |
| 1936 | C. P. Guise | Assistant Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1937 | C. P. Guise | Assistant Superintendent | Police, Prisons and Lunatic Asylum | — | — |
| 1939 | C. P. Guise | Assistants Superintendents | Police, Prisons and Lunatic Asylum | — | — |
| 1940 | C. P. Guise | Assistant Superintendent | Police, Prisons and Lunatic Asylum | — | — |

### Deterministic checks: `guise_christopher-probyn_b1899` vs `Guise, C. P___Nyasaland___1928`

- [PASS] surname_gate: bio 'GUISE' vs stint 'Guise, C. P' (exact)
- [PASS] initials: bio ['C', 'P'] ~ stint ['C', 'P']
- [PASS] age_gate: stint starts 1928, birth 1899 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1928-1940
- [FAIL] position_sim: best 56 vs bar 60: 'police cadet' ~ 'Cadets'
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

