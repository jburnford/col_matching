<!-- {"case_id": "case_tilley_w-e_b1921", "bio_ids": ["tilley_w-e_b1921"], "stint_ids": ["Tilley, W. E___British Somaliland___1950"]} -->
# Dossier case_tilley_w-e_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tilley_w-e_b1921`

- Printed name: **TILLEY, W. E**
- Birth year: 1921 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L25674.v` — printed in editions [1963, 1964, 1965, 1966]:**

> TILLEY, W. E.—b. 1921; ed. Lawrence R.M.S., Sanamar, and Loughborough Coll.; mil. serv., 1941–46; asst. engrn., Somali Prot., 1949; exec. engrn., Fiji, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | asst. engrn., Somali Prot | — | [1963, 1964, 1965, 1966] |
| 1 | 1952 | exec. engrn. | Fiji | [1963, 1964, 1965, 1966] |

## Candidate stint `Tilley, W. E___British Somaliland___1950`

- Staff-list name: **Tilley, W. E** | colony: **British Somaliland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. E. Tilley | Engineers, Grade I and II | Public Works | — | — |
| 1951 | W. E. Tilley | Engineers, Grade I and II | PUBLIC WORKS | — | — |

### Deterministic checks: `tilley_w-e_b1921` vs `Tilley, W. E___British Somaliland___1950`

- [PASS] surname_gate: bio 'TILLEY' vs stint 'Tilley, W. E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1950, birth 1921 (age 29)
- [FAIL] colony: no placed event resolves to 'British Somaliland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

