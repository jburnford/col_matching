<!-- {"case_id": "case_mitchell_b-l_b1909", "bio_ids": ["mitchell_b-l_b1909"], "stint_ids": ["Mitchell, B. L___Nyasaland___1949"]} -->
# Dossier case_mitchell_b-l_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 118 official(s) with this surname in the graph's staff lists; 46 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mitchell_b-l_b1909`

- Printed name: **MITCHELL, B. L**
- Birth year: 1909 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L19945.v` — printed in editions [1964, 1965, 1966]:**

> MITCHELL, B. L.—b. 1909; ed. London Univ.; biologist, Nyas., 1946; N. Rhod., 1954. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | biologist, Nyas | — | [1964, 1965, 1966] |
| 1 | 1954 | biologist, Nyas | Northern Rhodesia | [1964, 1965, 1966] |

## Candidate stint `Mitchell, B. L___Nyasaland___1949`

- Staff-list name: **Mitchell, B. L** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. L. Mitchell | Entomologist | Game, Fish and Tsetse Control Branch | — | — |
| 1951 | B. L. Mitchell | Entomologist | Game, Fish and Tsetse Control | — | — |

### Deterministic checks: `mitchell_b-l_b1909` vs `Mitchell, B. L___Nyasaland___1949`

- [PASS] surname_gate: bio 'MITCHELL' vs stint 'Mitchell, B. L' (exact)
- [PASS] initials: bio ['B', 'L'] ~ stint ['B', 'L']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

