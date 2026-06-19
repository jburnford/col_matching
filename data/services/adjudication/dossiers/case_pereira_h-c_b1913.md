<!-- {"case_id": "case_pereira_h-c_b1913", "bio_ids": ["pereira_h-c_b1913"], "stint_ids": ["Pereira, H. C___Kenya___1950"]} -->
# Dossier case_pereira_h-c_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pereira_h-c_b1913`

- Printed name: **PEREIRA, H. C**
- Birth year: 1913 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L23471.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> PEREIRA, H. C.—b. 1913; ed. Prince Albert Coll., Saskatchewan, St. Albans Sch. and London Univ.; mil. serv., 1939-46, major; research offr., Ken. coffee team, 1947; soil physicist, E.A.A.F.R.O., 1952; dep. dir., E.A.A.F.R.O., 1955-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | research offr., Ken. coffee team | Kenya | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1952 | soil physicist, E.A.A.F.R.O | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1955–1961 | dep. dir., E.A.A.F.R.O | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Pereira, H. C___Kenya___1950`

- Staff-list name: **Pereira, H. C** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | H. C. Pereira | Agricultural Chemist | AGRICULTURE | — | — |
| 1951 | H. C. Pereira | Agricultural Chemist | Agriculture | — | — |

### Deterministic checks: `pereira_h-c_b1913` vs `Pereira, H. C___Kenya___1950`

- [PASS] surname_gate: bio 'PEREIRA' vs stint 'Pereira, H. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1950, birth 1913 (age 37)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 34 vs bar 60: 'soil physicist, E.A.A.F.R.O' ~ 'Agricultural Chemist'
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

