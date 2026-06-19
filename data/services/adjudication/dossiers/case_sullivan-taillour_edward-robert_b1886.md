<!-- {"case_id": "case_sullivan-taillour_edward-robert_b1886", "bio_ids": ["sullivan-taillour_edward-robert_b1886", "sullivan-tailyour_edward-robert_b1886"], "stint_ids": ["Sullivan-Tailyour, E. R___Kenya___1922"]} -->
# Dossier case_sullivan-taillour_edward-robert_b1886

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Sullivan-Tailyour, E. R___Kenya___1922'] have more than one claimant biography in this case.
- NOTE: stint `Sullivan-Tailyour, E. R___Kenya___1922` is also gate-compatible with biography(ies) outside this case: ['sullivan-tailour_edward-robert_b1886'] (already linked elsewhere or filtered).
- NOTE: stint `Sullivan-Tailyour, E. R___Kenya___1922` is also gate-compatible with biography(ies) outside this case: ['sullivan-tailour_edward-robert_b1886'] (already linked elsewhere or filtered).

## Biography `sullivan-taillour_edward-robert_b1886`

- Printed name: **SULLIVAN-TAILLOUR, EDWARD ROBERT**
- Birth year: 1886 (attested in editions [1930])
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L68700.v` — printed in editions [1930]:**

> SULLIVAN-TAILLOUR, EDWARD ROBERT.—B. 1886; supt., pol., Kenya, June, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | supt., pol. | Kenya | [1930] |

## Biography `sullivan-tailyour_edward-robert_b1886`

- Printed name: **SULLIVAN-TAILYOUR, EDWARD ROBERT**
- Birth year: 1886 (attested in editions [1928, 1929, 1931, 1932, 1933, 1935])
- Appears in editions: [1928, 1929, 1931, 1932, 1933, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1928-L70366.v` — printed in editions [1928, 1929, 1931, 1932, 1933, 1935]:**

> SULLIVAN-TAILYOUR, EDWARD ROBERT.—B. 1886; supt., pol., Kenya, June, 1923.

**Version `col1936-L64973.v` — printed in editions [1936]:**

> SULLIVAN-TAILYOUR, EDWARD ROBERT.—B. 1886; SUPT., POL., KENYA, JUNE, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | supt., pol. | Kenya | [1928, 1929, 1931, 1932, 1933, 1935, 1936] |

## Candidate stint `Sullivan-Tailyour, E. R___Kenya___1922`

- Staff-list name: **Sullivan-Tailyour, E. R** | colony: **Kenya** | listed 1922–1927 | editions [1922, 1923, 1924, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | E. R. Sullivan-Tailyour | Assistant Superintendent | Police | — | — |
| 1923 | E. R. Sullivan-Tailyour | Assistant Superintendent | Police | — | — |
| 1924 | E. R. Sullivan-Tailyour | Superintendent | Police | — | — |
| 1927 | E. R. Sullivan-Tailyour | Superintendent | Police Department | — | — |

### Deterministic checks: `sullivan-taillour_edward-robert_b1886` vs `Sullivan-Tailyour, E. R___Kenya___1922`

- [PASS] surname_gate: bio 'SULLIVAN-TAILLOUR' vs stint 'Sullivan-Tailyour, E. R' (fuzzy:1)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1922, birth 1886 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1927
- [FAIL] position_sim: best 36 vs bar 60: 'supt., pol.' ~ 'Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `sullivan-tailyour_edward-robert_b1886` vs `Sullivan-Tailyour, E. R___Kenya___1922`

- [PASS] surname_gate: bio 'SULLIVAN-TAILYOUR' vs stint 'Sullivan-Tailyour, E. R' (exact)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1922, birth 1886 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1927
- [FAIL] position_sim: best 36 vs bar 60: 'supt., pol.' ~ 'Superintendent'
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

