<!-- {"case_id": "case_coghill_i-g_b1926", "bio_ids": ["coghill_i-g_b1926"], "stint_ids": ["Coghill, I. G___Gambia___1964"]} -->
# Dossier case_coghill_i-g_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coghill_i-g_b1926`

- Printed name: **COGHILL, I. G**
- Birth year: 1926 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L15854.v` — printed in editions [1964, 1965, 1966]:**

> COGHILL, I. G.—b. 1926; ed. Paisley Gram. Sch., William Barbour Acad. and Glasgow Univ.; mil. serv., 1944-48, capt.; cadet admin., Som., 1953; admin. offr., 1955; Gam., 1959. (Gambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | cadet admin. | Somaliland | [1964, 1965, 1966] |
| 1 | 1955 | admin. offr | Somaliland *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1959 | Gam | Somaliland *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Coghill, I. G___Gambia___1964`

- Staff-list name: **Coghill, I. G** | colony: **Gambia** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | I. G. Coghill | Secretary | Ministry of Works and Communications | — | — |
| 1965 | I. G. Coghill | Secretary | Ministry of Works and Communications | — | — |

### Deterministic checks: `coghill_i-g_b1926` vs `Coghill, I. G___Gambia___1964`

- [PASS] surname_gate: bio 'COGHILL' vs stint 'Coghill, I. G' (exact)
- [PASS] initials: bio ['I', 'G'] ~ stint ['I', 'G']
- [PASS] age_gate: stint starts 1964, birth 1926 (age 38)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1965
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

