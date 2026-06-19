<!-- {"case_id": "case_lloyd_j-r_b1912", "bio_ids": ["lloyd_j-r_b1912"], "stint_ids": ["Lloyd, J. R___Sierra Leone___1958"]} -->
# Dossier case_lloyd_j-r_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lloyd_j-r_b1912`

- Printed name: **LLOYD, J. R**
- Birth year: 1912 (attested in editions [1959, 1961, 1962, 1964])
- Appears in editions: [1959, 1961, 1962, 1964]

### Verbatim printed entry text (OCR)

**Version `col1959-L25342.v` — printed in editions [1959, 1961, 1962, 1964]:**

> LLOYD, J. R.—b. 1912; ed. Birkenhead Inst., Runcorn Central Sch., and privately; mil. serv., 1940–47, major; asst. supt., prisons, Nig., 1948; prin. approved sch., 1950–55; supt., prisons, 1955; dir., prisons, S. Leone, 1957; warder, prisons, Berm., 1962–63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | asst. supt., prisons | Nigeria | [1959, 1961, 1962, 1964] |
| 1 | 1950–1955 | prin. approved sch | Nigeria *(inherited from previous clause)* | [1959, 1961, 1962, 1964] |
| 2 | 1955 | supt., prisons | Nigeria *(inherited from previous clause)* | [1959, 1961, 1962, 1964] |
| 3 | 1957 | dir., prisons, S. Leone | Nigeria *(inherited from previous clause)* | [1959, 1961, 1962, 1964] |
| 4 | 1962–1963 | warder, prisons | Bermuda | [1959, 1961, 1962, 1964] |

## Candidate stint `Lloyd, J. R___Sierra Leone___1958`

- Staff-list name: **Lloyd, J. R** | colony: **Sierra Leone** | listed 1958–1960 | editions [1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | J. R. Lloyd | Director of Prisons | Civil Establishment | — | — |
| 1959 | J. R. Lloyd | Director of Prisons | Civil Establishment | — | — |
| 1960 | J. R. Lloyd | Director of Prisons | Civil Establishment | — | — |

### Deterministic checks: `lloyd_j-r_b1912` vs `Lloyd, J. R___Sierra Leone___1958`

- [PASS] surname_gate: bio 'LLOYD' vs stint 'Lloyd, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1958, birth 1912 (age 46)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
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

