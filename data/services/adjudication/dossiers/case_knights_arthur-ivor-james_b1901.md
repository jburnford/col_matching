<!-- {"case_id": "case_knights_arthur-ivor-james_b1901", "bio_ids": ["knights_arthur-ivor-james_b1901"], "stint_ids": ["Knights, A. I. J___Trinidad and Tobago___1922"]} -->
# Dossier case_knights_arthur-ivor-james_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `knights_arthur-ivor-james_b1901`

- Printed name: **KNIGHTS, Arthur Ivor James**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33871.v` — printed in editions [1948, 1949, 1950, 1951]:**

> KNIGHTS, Arthur Ivor James.—b. 1901; ed. Storrington Coll., Sussex; asst. supt., police, Trin., 1921; supt., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | asst. supt., police | Trinidad | [1948, 1949, 1950, 1951] |
| 1 | 1928 | supt | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Knights, A. I. J___Trinidad and Tobago___1922`

- Staff-list name: **Knights, A. I. J** | colony: **Trinidad and Tobago** | listed 1922–1940 | editions [1922, 1923, 1925, 1927, 1928, 1929, 1931, 1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. I. J. Knights | Sub-Inspector | Constabulary and Gaols | — | — |
| 1923 | A. I. J. Knights | Sub-Inspector | Constabulary and Gaols | — | — |
| 1925 | A. I. J. Knights | Sub-Inspector | Constabulary and Gaols | — | — |
| 1927 | A. I. J. Knights | Sub-Inspector | Constabulary and Gaols | — | — |
| 1928 | A. I. J. Knights | Sub-Inspectors | Constabulary and Gaols | — | — |
| 1929 | A. I. J. Knights | Inspectors | Constabulary and Gaols | — | — |
| 1931 | A. I. J. Knights | Inspector | Constabulary and Gaols | — | — |
| 1933 | A. I. J. Knights | Inspector | Constabulary and Gaols | — | Captain |
| 1934 | A. I. J. Knights | Inspector | Constabulary and Gaols | — | Captain |
| 1937 | Capt. A. I. J. Knights | Inspectors | Constabulary | — | Captain |
| 1939 | A. I. J. Knights | Superintendent | Police | — | Captain |
| 1940 | A. I. J. Knights | Superintendent | Police | — | Major |

### Deterministic checks: `knights_arthur-ivor-james_b1901` vs `Knights, A. I. J___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'KNIGHTS' vs stint 'Knights, A. I. J' (exact)
- [PASS] initials: bio ['A', 'I', 'J'] ~ stint ['A', 'I', 'J']
- [PASS] age_gate: stint starts 1922, birth 1901 (age 21)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1940
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

