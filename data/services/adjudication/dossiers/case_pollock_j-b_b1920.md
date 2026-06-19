<!-- {"case_id": "case_pollock_j-b_b1920", "bio_ids": ["pollock_j-b_b1920"], "stint_ids": ["Pollock, J. B___Uganda___1949"]} -->
# Dossier case_pollock_j-b_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pollock_j-b_b1920`

- Printed name: **POLLOCK, J. B**
- Birth year: 1920 (attested in editions [1958, 1959, 1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L26067.v` — printed in editions [1958, 1959, 1960, 1961]:**

> POLLOCK, J. B.—b. 1920; ed. Bedford Sch., and Royal Sch. of Mines; metallur- gist, geol. survey, Uga., 1946; redesig. senr. chemist, 1957; author An absorptiometric method for the Determination of Beryllium in Beryl (Analyst, Jan. 1956); A Photometric method for the determination of Tungsten in low grade mine ore, and mineral dressing products (Analyst, Sept. 1959).

**Version `col1962-L25452.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> POLLOCK, J. B.—b. 1920; ed. Bedford Sch., and Royal Sch. of Mines; metallurgist, geol. survey, Uga., 1946; redesign. senr. chemist, 1957. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | metallur- gist, geol. survey | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1956 | author An absorptiometric method for the Determination of Beryllium in Beryl (Analyst | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 2 | 1957 | redesig. senr. chemist | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1959 | A Photometric method for the determination of Tungsten in low grade mine ore, and mineral dressing products (Analyst | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |

## Candidate stint `Pollock, J. B___Uganda___1949`

- Staff-list name: **Pollock, J. B** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. B. Pollock | Metallurgist | GEOLOGICAL SURVEY | — | — |
| 1951 | J. B. Pollock | Metallurgist | Geological Survey | — | — |

### Deterministic checks: `pollock_j-b_b1920` vs `Pollock, J. B___Uganda___1949`

- [PASS] surname_gate: bio 'POLLOCK' vs stint 'Pollock, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1949, birth 1920 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 49 vs bar 60: 'metallur- gist, geol. survey' ~ 'Metallurgist'
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

