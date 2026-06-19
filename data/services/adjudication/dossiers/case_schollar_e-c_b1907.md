<!-- {"case_id": "case_schollar_e-c_b1907", "bio_ids": ["schollar_e-c_b1907"], "stint_ids": ["Scholar, E___Leeward Islands___1949"]} -->
# Dossier case_schollar_e-c_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schollar_e-c_b1907`

- Printed name: **SCHOLLAR, E. C**
- Birth year: 1907 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1959-L27643.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964]:**

> SCHOLLAR, E. C.—b. 1907; ed. Eastbourne Gram. Sch.; mil. serv., 1939-45, sqdn. ldr.; traffic inspnr., G.C. rlyw. and harbours, 1947; asst. traffic supt., 1948; senr. traffic supt., 1953; commercial supt., 1956 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | traffic inspnr., G.C. rlyw. and harbours | Gold Coast | [1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | asst. traffic supt | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1953 | senr. traffic supt | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1956 | commercial supt | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Scholar, E___Leeward Islands___1949`

- Staff-list name: **Scholar, E** | colony: **Leeward Islands** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. Scholar | Assistant Superintendent, Printing Office | Printing | — | — |
| 1950 | E. Scholar | Assistant Superintendent, Printing Office | Printing | — | — |

### Deterministic checks: `schollar_e-c_b1907` vs `Scholar, E___Leeward Islands___1949`

- [PASS] surname_gate: bio 'SCHOLLAR' vs stint 'Scholar, E' (fuzzy:1)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

