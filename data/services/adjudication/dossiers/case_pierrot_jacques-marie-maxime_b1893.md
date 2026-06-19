<!-- {"case_id": "case_pierrot_jacques-marie-maxime_b1893", "bio_ids": ["pierrot_jacques-marie-maxime_b1893"], "stint_ids": ["Pierrot, M___Mauritius___1922", "Pierrot, M___Mauritius___1937"]} -->
# Dossier case_pierrot_jacques-marie-maxime_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pierrot_jacques-marie-maxime_b1893`

- Printed name: **PIERROT, Jacques Marie Maxime**
- Birth year: 1893 (attested in editions [1949])
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L34943.v` — printed in editions [1949]:**

> PIERROT, Jacques Marie Maxime.—b. 1893; ed. Royal Coll., Maur. and the Sorbonne, Paris; assoc. coll. of preceptors; asst. mstr., Royal Coll., Maur., 1919; educ. offr., gr. I, 1933; co-ed. Dict. of Mauritius Biography.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | asst. mstr., Royal Coll. | Mauritius | [1949] |

## Candidate stint `Pierrot, M___Mauritius___1922`

- Staff-list name: **Pierrot, M** | colony: **Mauritius** | listed 1922–1931 | editions [1922, 1923, 1927, 1928, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | M. Pierrot | Assistant Masters | Education | — | — |
| 1923 | M. Pierrot | Assistant Masters | Education | — | — |
| 1927 | M. Pierrot | Assistant Masters | Education | — | — |
| 1928 | M. Pierrot | Assistant Masters | Education | — | — |
| 1931 | M. Pierrot | Assistant Masters | Education | — | — |

### Deterministic checks: `pierrot_jacques-marie-maxime_b1893` vs `Pierrot, M___Mauritius___1922`

- [PASS] surname_gate: bio 'PIERROT' vs stint 'Pierrot, M' (exact)
- [PASS] initials: bio ['J', 'M', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1922, birth 1893 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1931
- [FAIL] position_sim: best 49 vs bar 60: 'asst. mstr., Royal Coll.' ~ 'Assistant Masters'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Pierrot, M___Mauritius___1937`

- Staff-list name: **Pierrot, M** | colony: **Mauritius** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | M. Pierrot | Masters | Education | — | — |
| 1939 | M. Pierrot | Masters | Education | — | — |

### Deterministic checks: `pierrot_jacques-marie-maxime_b1893` vs `Pierrot, M___Mauritius___1937`

- [PASS] surname_gate: bio 'PIERROT' vs stint 'Pierrot, M' (exact)
- [PASS] initials: bio ['J', 'M', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1937, birth 1893 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1939
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

