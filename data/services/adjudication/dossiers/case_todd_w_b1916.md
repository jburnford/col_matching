<!-- {"case_id": "case_todd_w_b1916", "bio_ids": ["todd_w_b1916"], "stint_ids": ["Todd, W. M___Uganda___1936"]} -->
# Dossier case_todd_w_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 56 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['todd_w_b1916'] carry a single initial only — the namesake trap applies.

## Biography `todd_w_b1916`

- Printed name: **TODD, W**
- Birth year: 1916 (attested in editions [1962, 1963, 1964, 1965])
- Honours: C.P.M (1964), King's Police Med (1947)
- Appears in editions: [1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1962-L27279.v` — printed in editions [1962, 1963, 1964, 1965]:**

> TODD, W., King's Police Med. (1947), C.P.M. (1964).—b. 1916; ed. Morgan Acad.; H.K. police, 1939; interned 1941–45; sub. inspr., 1946; asst. supt., 1950; supt. 1953; snr. supt., 1960–64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | H.K. police | Hong Kong | [1962, 1963, 1964, 1965] |
| 1 | 1941–1945 | interned | Hong Kong *(inherited from previous clause)* | [1962, 1963, 1964, 1965] |
| 2 | 1946 | sub. inspr | Hong Kong *(inherited from previous clause)* | [1962, 1963, 1964, 1965] |
| 3 | 1950 | asst. supt | Hong Kong *(inherited from previous clause)* | [1962, 1963, 1964, 1965] |
| 4 | 1953 | supt | Hong Kong *(inherited from previous clause)* | [1962, 1963, 1964, 1965] |
| 5 | 1960–1964 | snr. supt | Hong Kong *(inherited from previous clause)* | [1962, 1963, 1964, 1965] |

## Candidate stint `Todd, W. M___Uganda___1936`

- Staff-list name: **Todd, W. M** | colony: **Uganda** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. M. Todd | Driller | Drilling Section | — | — |
| 1939 | W. M. Todd | Driller | Geological Survey | — | — |
| 1940 | W. M. Todd | Driller | Geological Survey | — | — |

### Deterministic checks: `todd_w_b1916` vs `Todd, W. M___Uganda___1936`

- [PASS] surname_gate: bio 'TODD' vs stint 'Todd, W. M' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'M']
- [PASS] age_gate: stint starts 1936, birth 1916 (age 20)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

