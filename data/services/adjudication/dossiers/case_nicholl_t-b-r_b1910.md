<!-- {"case_id": "case_nicholl_t-b-r_b1910", "bio_ids": ["nicholl_t-b-r_b1910"], "stint_ids": ["Nicholl, T. B. R___Sarawak___1949"]} -->
# Dossier case_nicholl_t-b-r_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nicholl_t-b-r_b1910`

- Printed name: **NICHOLL, T. B. R**
- Birth year: 1910 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L25599.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> NICHOLL, T. B. R.—b. 1910; ed. Edward VII Sch., St. Annes-on-Sea, Dublin Univ. and St. Benet's Hall, Oxford; admin. offr., Sarawak, 1946; educ. offr., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. offr. | Sarawak | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Nicholl, T. B. R___Sarawak___1949`

- Staff-list name: **Nicholl, T. B. R** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. B. R. Nicholl | District Officer / Assistant District Officer / Cadet | Administrative Service | — | — |
| 1950 | T. B. R. Nicholl | District Officers, Assistant District Officers and Cadets | Administrative Service | — | — |
| 1951 | T. B. R. Nicholl | Education Officer | Education | — | — |

### Deterministic checks: `nicholl_t-b-r_b1910` vs `Nicholl, T. B. R___Sarawak___1949`

- [PASS] surname_gate: bio 'NICHOLL' vs stint 'Nicholl, T. B. R' (exact)
- [PASS] initials: bio ['T', 'B', 'R'] ~ stint ['T', 'B', 'R']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'admin. offr.' ~ 'Education Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

