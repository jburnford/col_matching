<!-- {"case_id": "case_green_d_b1927", "bio_ids": ["green_d_b1927"], "stint_ids": ["Green, T. D___Leeward Islands___1949"]} -->
# Dossier case_green_d_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 91 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['green_d_b1927'] carry a single initial only — the namesake trap applies.

## Biography `green_d_b1927`

- Printed name: **GREEN, D.**
- Birth year: 1927 (attested in editions [1961])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L22686.v` — printed in editions [1961]:**

> GREEN, D.—b. 1927; ed. The Gram. Sch., Gateshead, and Downing Coll., Camb.; geologist, Bech. Prot., 1949; publ. Coal in the Bech. Prot. (Col. Geol. & Min. Res., vol. 3, no. 4); An outline of the Geology of the Bech. Prot. (XIXth Inter. Geol. Cong., Algiers, 1952) etc.

**Version `col1962-L21725.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> GREEN, D.—b. 1927; ed. The Gram. Sch., Gateshead, and Downing Coll., Camb.; geologist, Bech. Prot., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | geologist | Bechuanaland Protectorate | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Green, T. D___Leeward Islands___1949`

- Staff-list name: **Green, T. D** | colony: **Leeward Islands** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. D. Green | Supervisor of Education; Headmaster of the Senior School | EDUCATION | — | — |
| 1950 | T. D. Green | Supervisor of Education; Headmaster of the Senior School | EDUCATION | — | — |

### Deterministic checks: `green_d_b1927` vs `Green, T. D___Leeward Islands___1949`

- [PASS] surname_gate: bio 'GREEN' vs stint 'Green, T. D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['T', 'D']
- [PASS] age_gate: stint starts 1949, birth 1927 (age 22)
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

