<!-- {"case_id": "case_maynard_richard-william-henry_b1906", "bio_ids": ["maynard_richard-william-henry_b1906"], "stint_ids": ["Maynard, R. W. H___Hong Kong___1931", "Maynard, R. W. H___Hong Kong___1949"]} -->
# Dossier case_maynard_richard-william-henry_b1906

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maynard_richard-william-henry_b1906`

- Printed name: **MAYNARD, Richard William Henry**
- Birth year: 1906 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37942.v` — printed in editions [1950, 1951]:**

> MAYNARD, Richard William Henry.—b. 1906; clk. magistracy, H.K., 1924; senr. exec. offr., cl. II, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | clk. magistracy | Hong Kong | [1950, 1951] |
| 1 | 1947 | senr. exec. offr., cl. II | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Maynard, R. W. H___Hong Kong___1931`

- Staff-list name: **Maynard, R. W. H** | colony: **Hong Kong** | listed 1931–1934 | editions [1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. W. H. Maynard | Clerk to Chief Justice | Supreme Court | — | — |
| 1933 | R. W. H. Maynard | Clerk to Chief Justice | Supreme Court | — | — |
| 1934 | R. W. H. Maynard | Clerk to Chief Justice | Supreme Court | — | — |

### Deterministic checks: `maynard_richard-william-henry_b1906` vs `Maynard, R. W. H___Hong Kong___1931`

- [PASS] surname_gate: bio 'MAYNARD' vs stint 'Maynard, R. W. H' (exact)
- [PASS] initials: bio ['R', 'W', 'H'] ~ stint ['R', 'W', 'H']
- [PASS] age_gate: stint starts 1931, birth 1906 (age 25)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1934
- [FAIL] position_sim: best 39 vs bar 60: 'clk. magistracy' ~ 'Clerk to Chief Justice'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Maynard, R. W. H___Hong Kong___1949`

- Staff-list name: **Maynard, R. W. H** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. W. H. Maynard | Secretary, Urban Council | Sanitary | — | — |
| 1950 | R. W. H. Maynard | Chief Clerk (acting) | Secretariat | — | — |
| 1951 | R. W. H. Maynard | Chief Clerks | Administration | — | — |

### Deterministic checks: `maynard_richard-william-henry_b1906` vs `Maynard, R. W. H___Hong Kong___1949`

- [PASS] surname_gate: bio 'MAYNARD' vs stint 'Maynard, R. W. H' (exact)
- [PASS] initials: bio ['R', 'W', 'H'] ~ stint ['R', 'W', 'H']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 42 vs bar 60: 'senr. exec. offr., cl. II' ~ 'Chief Clerk (acting)'
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

