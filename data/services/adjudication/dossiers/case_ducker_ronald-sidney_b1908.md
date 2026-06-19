<!-- {"case_id": "case_ducker_ronald-sidney_b1908", "bio_ids": ["ducker_ronald-sidney_b1908"], "stint_ids": ["Decker, R. S. S___Gambia___1924"]} -->
# Dossier case_ducker_ronald-sidney_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ducker_ronald-sidney_b1908`

- Printed name: **DUCKER, RONALD SIDNEY**
- Birth year: 1908 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L60455.v` — printed in editions [1937, 1940]:**

> DUCKER, RONALD SIDNEY.—B. 1908; ed. Pembroke Coll., Oxford; B.A. (1929); M.A. (1935); spec. course in educn. at London Univ. for C.O. probationers, 1929; inspr., schls., Gold Coast, 1930; 2nd inspr., schls., Br. Guiana, 1932; supt., educn., Nigeria, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | B.A. ( | — | [1937, 1940] |
| 1 | 1929 | spec. course in educn. at London Univ. for C.O. probationers | Colonial Office | [1937, 1940] |
| 2 | 1930 | inspr., schls. | Gold Coast | [1937, 1940] |
| 3 | 1932 | 2nd inspr., schls. | British Guiana | [1937, 1940] |
| 4 | 1935 | M.A. ( | — | [1937, 1940] |
| 5 | 1936 | supt., educn. | Nigeria | [1937, 1940] |

## Candidate stint `Decker, R. S. S___Gambia___1924`

- Staff-list name: **Decker, R. S. S** | colony: **Gambia** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | R. S. S. Decker | Telephone Operator | Posts and Telegraphs | — | — |
| 1925 | R. S. S. Decker | Telephone Operator | Posts and Telegraphs | — | — |

### Deterministic checks: `ducker_ronald-sidney_b1908` vs `Decker, R. S. S___Gambia___1924`

- [PASS] surname_gate: bio 'DUCKER' vs stint 'Decker, R. S. S' (fuzzy:1)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S', 'S']
- [PASS] age_gate: stint starts 1924, birth 1908 (age 16)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
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

