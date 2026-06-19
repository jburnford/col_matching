<!-- {"case_id": "case_harley_p-j_b1909", "bio_ids": ["harley_p-j_b1909"], "stint_ids": ["Harley, P. J___Leeward Islands___1939"]} -->
# Dossier case_harley_p-j_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harley_p-j_b1909`

- Printed name: **HARLEY, P. J**
- Birth year: 1909 (attested in editions [1960, 1961, 1962])
- Honours: C.P.M (1949), O.B.E (1958), Q.P.M (1962)
- Appears in editions: [1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1960-L23823.v` — printed in editions [1960, 1961, 1962]:**

> HARLEY, P. J., O.B.E. (1958), Q.P.M. (1962), C.P.M. (1949).—b. 1909; ed. Wellington Coll.; police constable, Pal., 1934; asst. supt., Leeward Is., 1938; supt., Dominica, St. L., St. V., 1941-46; Maur., 1946; senr. asst. supt., Nig., 1950; senr. supt., 1951; dep. comsnr., 1957; comsnr., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | police constable | Palestine | [1960, 1961, 1962] |
| 1 | 1938 | asst. supt., Leeward Is | Palestine *(inherited from previous clause)* | [1960, 1961, 1962] |
| 2 | 1941–1946 | supt., Dominica, St. L. | St. Vincent | [1960, 1961, 1962] |
| 3 | 1946 | supt., Dominica, St. L. | Mauritius | [1960, 1961, 1962] |
| 4 | 1950 | senr. asst. supt. | Nigeria | [1960, 1961, 1962] |
| 5 | 1951 | senr. supt | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962] |
| 6 | 1957 | dep. comsnr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962] |
| 7 | 1958 | comsnr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962] |

## Candidate stint `Harley, P. J___Leeward Islands___1939`

- Staff-list name: **Harley, P. J** | colony: **Leeward Islands** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | P. J. Harley | Sub-Inspector | Police | — | — |
| 1940 | P. J. Harley | Assistant Superintendent | Police | — | — |

### Deterministic checks: `harley_p-j_b1909` vs `Harley, P. J___Leeward Islands___1939`

- [PASS] surname_gate: bio 'HARLEY' vs stint 'Harley, P. J' (exact)
- [PASS] initials: bio ['P', 'J'] ~ stint ['P', 'J']
- [PASS] age_gate: stint starts 1939, birth 1909 (age 30)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

