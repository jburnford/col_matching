<!-- {"case_id": "case_george_s-p_b1899", "bio_ids": ["george_s-p_b1899"], "stint_ids": ["George, P___British Honduras___1915", "George, S. P___Nigeria___1933"]} -->
# Dossier case_george_s-p_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `george_s-p_b1899`

- Printed name: **GEORGE, S. P**
- Birth year: 1899 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Honours: K.P.M
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L32788.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> GEORGE, S. P., K.P.M.—b. 1899; ed. St. Peter's Sch., York, passed for R.M.C., Sandhurst (1917); mil. serv., 1917–23, ag. capt., 1923–30, R.A.F., flt.-lieut.; apptd. to police, Nig., 1931; senr. asst. supt., 1939; supt., 1946; senr., 1949; comsnr., E. regn., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | apptd. to police | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1939 | senr. asst. supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1946 | supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 3 | 1949 | senr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 4 | 1951 | comsnr., E. regn | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `George, P___British Honduras___1915`

- Staff-list name: **George, P** | colony: **British Honduras** | listed 1915–1918 | editions [1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | P. George | 2nd Class Clerk | Judicial Department | — | — |
| 1917 | P. George | Clerk | Judicial Department | — | — |
| 1918 | P. George | Clerk | Judicial Department | — | — |

### Deterministic checks: `george_s-p_b1899` vs `George, P___British Honduras___1915`

- [PASS] surname_gate: bio 'GEORGE' vs stint 'George, P' (exact)
- [PASS] initials: bio ['S', 'P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1915, birth 1899 (age 16)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `George, S. P___Nigeria___1933`

- Staff-list name: **George, S. P** | colony: **Nigeria** | listed 1933–1939 | editions [1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | S. P. George | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | S. P. George | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | S. P. George | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | S. P. George | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `george_s-p_b1899` vs `George, S. P___Nigeria___1933`

- [PASS] surname_gate: bio 'GEORGE' vs stint 'George, S. P' (exact)
- [PASS] initials: bio ['S', 'P'] ~ stint ['S', 'P']
- [PASS] age_gate: stint starts 1933, birth 1899 (age 34)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1939
- [PASS] position_sim: best 62 vs bar 60: 'senr. asst. supt' ~ 'Senior Assistant Superintendent'
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

