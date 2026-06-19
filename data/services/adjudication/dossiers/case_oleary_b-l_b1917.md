<!-- {"case_id": "case_oleary_b-l_b1917", "bio_ids": ["oleary_b-l_b1917"], "stint_ids": ["O'Leary, B. L___High Commission Territories___1959"]} -->
# Dossier case_oleary_b-l_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `oleary_b-l_b1917`

- Printed name: **OLEARY, B. L**
- Birth year: 1917 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B.E (1960), O.B.E (1965)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L26086.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> OLEARY, B. L., O.B.E. (1965), M.B.E. (1960).—b. 1917; ed. S.A. Coll. Sch., Cape Town; mil. serv., 1940-45, capt.; dept. of justice, S.A., 1935-52; legal sec., Basuto., 1953; asst. atty-gen., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935–1952 | dept. of justice, S.A | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | legal sec. | Basutoland | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1960 | asst. atty-gen | Basutoland *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `O'Leary, B. L___High Commission Territories___1959`

- Staff-list name: **O'Leary, B. L** | colony: **High Commission Territories** | listed 1959–1963 | editions [1959, 1960, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | B. L. O'Leary | Legal Secretary | BASUTOLAND | — | — |
| 1960 | B. L. O'Leary | Legal Secretary | BASUTOLAND | M.B.E. | — |
| 1963 | B. L. O'Leary | Assistant Attorney-General | Law Officers | M.B.E. | — |

### Deterministic checks: `oleary_b-l_b1917` vs `O'Leary, B. L___High Commission Territories___1959`

- [PASS] surname_gate: bio 'OLEARY' vs stint 'O'Leary, B. L' (exact)
- [PASS] initials: bio ['B', 'L'] ~ stint ['B', 'L']
- [PASS] age_gate: stint starts 1959, birth 1917 (age 42)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1963
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
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

