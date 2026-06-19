<!-- {"case_id": "case_betuel_h-w-n_b1908", "bio_ids": ["betuel_h-w-n_b1908"], "stint_ids": ["Betuel, H. W. N___Nigeria___1958"]} -->
# Dossier case_betuel_h-w-n_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `betuel_h-w-n_b1908`

- Printed name: **BETUEL, H. W. N**
- Birth year: 1908 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L21123.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> BETUEL, H. W. N.—b. 1908; ed. Ecole Publique, St. Julien, Marseilles, Univ. of London, and Council of Legal Educ.; barrister-at-law, Gray's Inn; magistrate, Nig., 1939; chief mag., 1953; judge, E. Nig., 1958; chmn., arbit. tribunal, in re dispute between Elder Dempsters and their union.

**Version `col1962-L18848.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> BETUEL, H. W. N.—b. 1908; ed. Ecole Publique, St. Julien, Marseilles, Univ. of London, and Council of Legal Educ.; barrister-at-law, Gray's Inn; magistrate, Nig., 1939; chief mag., 1953; judge, E. Nig. 1958-65. (E. Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | magistrate | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | chief mag | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1958 | judge | Eastern Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Betuel, H. W. N___Nigeria___1958`

- Staff-list name: **Betuel, H. W. N** | colony: **Nigeria** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | H. W. N. Betuel | Chief Magistrate | Civil Establishment | — | — |
| 1960 | H. W. Betuel | Justice | Judiciary | — | — |

### Deterministic checks: `betuel_h-w-n_b1908` vs `Betuel, H. W. N___Nigeria___1958`

- [PASS] surname_gate: bio 'BETUEL' vs stint 'Betuel, H. W. N' (exact)
- [PASS] initials: bio ['H', 'W', 'N'] ~ stint ['H', 'W', 'N']
- [PASS] age_gate: stint starts 1958, birth 1908 (age 50)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1958-1960
- [PASS] position_sim: best 72 vs bar 60: 'chief mag' ~ 'Chief Magistrate'
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

