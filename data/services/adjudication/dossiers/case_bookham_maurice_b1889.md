<!-- {"case_id": "case_bookham_maurice_b1889", "bio_ids": ["bookham_maurice_b1889"], "stint_ids": ["Bookham, M___British Honduras___1934", "Bookham, M___Trinidad and Tobago___1929"]} -->
# Dossier case_bookham_maurice_b1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bookham_maurice_b1889'] carry a single initial only — the namesake trap applies.

## Biography `bookham_maurice_b1889`

- Printed name: **BOOKHAM, MAURICE**
- Birth year: 1889 (attested in editions [1940])
- Honours: M.B.E
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L62531.v` — printed in editions [1940]:**

> BOOKHAM, MAURICE, M.B.E.—B. 1889; imp. prison serv., 1913-27; war serv., 1914-19; dep. ast. supt., prisons, Trinidad, 1927-33; ast. supt., pol., Br. Honduras, 1933-38; supt., prisons, 1938; do., Br. Guiana, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1927 | imp. prison serv | — | [1940] |
| 1 | 1927–1933 | dep. ast. supt., prisons | Trinidad | [1940] |
| 2 | 1933–1938 | ast. supt., pol., Br. Honduras | Trinidad *(inherited from previous clause)* | [1940] |
| 3 | 1938 | supt., prisons | British Guiana | [1940] |

## Candidate stint `Bookham, M___British Honduras___1934`

- Staff-list name: **Bookham, M** | colony: **British Honduras** | listed 1934–1939 | editions [1934, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | M. Bookham | Asst. Superintendent of Police of Prisons | Prisons | — | — |
| 1936 | M. Bookham | Asst. Superintendent of Police i/c of Prisons | Prisons | — | — |
| 1937 | M. Bookham | Asst. Superintendent of Police i/c of Prisons | Prisons | — | — |
| 1939 | M. Bookham | Superintendent of Prisons | Prisons | — | — |

### Deterministic checks: `bookham_maurice_b1889` vs `Bookham, M___British Honduras___1934`

- [PASS] surname_gate: bio 'BOOKHAM' vs stint 'Bookham, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1934, birth 1889 (age 45)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bookham, M___Trinidad and Tobago___1929`

- Staff-list name: **Bookham, M** | colony: **Trinidad and Tobago** | listed 1929–1933 | editions [1929, 1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | M. Bookham | Deputy Assistant Superintendent | Constabulary and Gaols | — | — |
| 1931 | M. Bookham | Deputy Assistant Superintendent | Constabulary and Gaols | — | — |
| 1933 | M. Bookham | Deputy Assistant Superintendent | Constabulary and Gaols | — | — |

### Deterministic checks: `bookham_maurice_b1889` vs `Bookham, M___Trinidad and Tobago___1929`

- [PASS] surname_gate: bio 'BOOKHAM' vs stint 'Bookham, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1929, birth 1889 (age 40)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1933
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

