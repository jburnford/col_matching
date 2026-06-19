<!-- {"case_id": "case_merrill_reuben-saxon_b1897", "bio_ids": ["merrill_reuben-saxon_b1897"], "stint_ids": ["Merrill, R. S___Leeward Islands___1918", "Merrill, R. S___Leeward Islands___1932"]} -->
# Dossier case_merrill_reuben-saxon_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `merrill_reuben-saxon_b1897`

- Printed name: **MERRILL, Reuben Saxon**
- Birth year: 1897 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L34290.v` — printed in editions [1949, 1950, 1951]:**

> MERRILL, Reuben Saxon.—b. 1897; ed. Dominica Gram. Sch.; junr. audit clk., Dominica, 1918; cl. posts, various depts., 1918; postmr., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | junr. audit clk. | Dominica | [1949, 1950, 1951] |
| 1 | 1933 | postmr | Dominica *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Merrill, R. S___Leeward Islands___1918`

- Staff-list name: **Merrill, R. S** | colony: **Leeward Islands** | listed 1918–1927 | editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | R. S. Merrill | Acting for Grell | Post Office | — | — |
| 1919 | R. S. Merrill | Clerks to Auditor-General | Audit | — | — |
| 1920 | R. S. Merrill | Clerks to Auditor-General | Audit | — | — |
| 1921 | R. S. Merrill | Clerk to Auditor-General | Audit | — | — |
| 1922 | R. S. Merrill | 2nd Clerk | Audit | — | — |
| 1923 | R. S. Merrill | 2nd Clerk | Audit | — | — |
| 1924 | R. S. Merrill | 2nd Clerk | Audit | — | — |
| 1925 | R. S. Merrill | 2nd Clerk | Post Office | — | — |
| 1927 | R. S. Merrill | 1st Clerk | Post Office | — | — |

### Deterministic checks: `merrill_reuben-saxon_b1897` vs `Merrill, R. S___Leeward Islands___1918`

- [PASS] surname_gate: bio 'MERRILL' vs stint 'Merrill, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1918, birth 1897 (age 21)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Merrill, R. S___Leeward Islands___1932`

- Staff-list name: **Merrill, R. S** | colony: **Leeward Islands** | listed 1932–1939 | editions [1932, 1933, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | R. S. Merrill | Senior Clerk | Public Works Department | — | — |
| 1933 | R. S. Merrill | Senior Clerk | Public Works Department | — | — |
| 1936 | R. S. Merrill | Postmaster | Post Office | — | — |
| 1939 | R. S. Merrill | Postmaster | Post Office | — | — |

### Deterministic checks: `merrill_reuben-saxon_b1897` vs `Merrill, R. S___Leeward Islands___1932`

- [PASS] surname_gate: bio 'MERRILL' vs stint 'Merrill, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1932, birth 1897 (age 35)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1939
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

