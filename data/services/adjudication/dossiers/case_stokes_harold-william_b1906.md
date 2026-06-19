<!-- {"case_id": "case_stokes_harold-william_b1906", "bio_ids": ["stokes_harold-william_b1906"], "stint_ids": ["Stokes, H. W___Leeward Islands___1932"]} -->
# Dossier case_stokes_harold-william_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stokes_harold-william_b1906`

- Printed name: **STOKES, Harold William**
- Birth year: 1906 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1948-L36176.v` — printed in editions [1948, 1949]:**

> STOKES, Harold William.—b. 1906; ed. County Sch. for Boys', Dover and Selwyn Coll., Cambridge, M.A. (hons.) (Cantab.), Kitchener schol., Barwell schol.; hdmstr., Dominica Gram. Sch., B.W.I., 1929; junr. ed. comsnr., W.I., 1936; educ. offr., Ken., 1938; admin. sec., educ. dept., 1943; senr. educ. offr., 1945.

**Version `col1950-L39867.v` — printed in editions [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962]:**

> STOKES, Harold William.—b. 1906; ed. County Sch. for Boys’, Dover and Selwyn Coll., Camb., M.A. (Cantab.); headmtr., Trin., 1929; educ. offr., Ken., 1938; inspr., schs., 1945; senr. educ. offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | hdmstr., Dominica Gram. Sch., B.W.I | — | [1948, 1949] |
| 1 | 1929 | headmtr. | Trinidad | [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1936 | junr. ed. comsnr. | West Indies | [1948, 1949] |
| 3 | 1943 | admin. sec., educ. dept | West Indies *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1945 | senr. educ. offr | West Indies *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 5 | 1945 | inspr., schs | Trinidad *(inherited from previous clause)* | [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Stokes, H. W___Leeward Islands___1932`

- Staff-list name: **Stokes, H. W** | colony: **Leeward Islands** | listed 1932–1933 | editions [1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | H. W. Stokes | Head Master, Dominica Grammar School, Principal | Education | — | — |
| 1933 | H. W. Stokes | Head Master, Dominica Grammar School Principal | Education | — | — |

### Deterministic checks: `stokes_harold-william_b1906` vs `Stokes, H. W___Leeward Islands___1932`

- [PASS] surname_gate: bio 'STOKES' vs stint 'Stokes, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1932, birth 1906 (age 26)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1933
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

