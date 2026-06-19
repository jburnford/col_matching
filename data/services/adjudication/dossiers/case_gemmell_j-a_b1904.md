<!-- {"case_id": "case_gemmell_j-a_b1904", "bio_ids": ["gemmell_j-a_b1904"], "stint_ids": ["Gemmell, J___Uganda___1933"]} -->
# Dossier case_gemmell_j-a_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gemmell_j-a_b1904`

- Printed name: **GEMMELL, J. A**
- Birth year: 1904 (attested in editions [1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1961-L22373.v` — printed in editions [1961, 1962, 1963, 1964, 1965]:**

> GEMMELL, J. A.—b. 1904; ed. Mary Erskine Sch., Edin., and Edin. Univ.; med. supt., with W.M.S. for India, 1936-1948; M.O., Aden, 1949; med. supt., maternity clinic, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936–1948 | med. supt., with W.M.S. for India | — | [1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | M.O. | Aden | [1961, 1962, 1963, 1964, 1965] |
| 2 | 1952 | med. supt., maternity clinic | Aden *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Gemmell, J___Uganda___1933`

- Staff-list name: **Gemmell, J** | colony: **Uganda** | listed 1933–1940 | editions [1933, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. Gemmell | Head Gaoler | Police and Prisons | — | — |
| 1937 | J. Gemmell | Head Gaolers | Traffic Branch | — | — |
| 1939 | J. Gemmell | Head Gaolers | Prisons | — | — |
| 1940 | J. Gemmell | Head Gaolers | Prisons | — | — |

### Deterministic checks: `gemmell_j-a_b1904` vs `Gemmell, J___Uganda___1933`

- [PASS] surname_gate: bio 'GEMMELL' vs stint 'Gemmell, J' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J']
- [PASS] age_gate: stint starts 1933, birth 1904 (age 29)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

