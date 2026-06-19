<!-- {"case_id": "case_shaylor_denis-freke_b1906", "bio_ids": ["shaylor_denis-freke_b1906"], "stint_ids": ["Shaylor, D. F___Kenya___1949", "Shaylor, D. F___Uganda___1939"]} -->
# Dossier case_shaylor_denis-freke_b1906

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shaylor_denis-freke_b1906`

- Printed name: **SHAYLOR, Denis Freke**
- Birth year: 1906 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951, 1953]

### Verbatim printed entry text (OCR)

**Version `col1950-L39462.v` — printed in editions [1950, 1951]:**

> SHAYLOR, Denis Freke.—b. 1906; ed. Reading Sch., solr., sup. ct., Eng., 1929; on mil. serv., 1940–43 (K.A.R., O.E.T.A., Som., town mag., asst. leg. advr., cust. of enemy propy.); asst. registr., titles, Uga., 1938; registr., sup. ct. of Ken. and ct. of appeal for E.A., 1947.

**Version `col1953-L18967.v` — printed in editions [1953]:**

> SHAYLOR, D. F.—b. 1906; ed. Reading Sch.; solr.; barrister-at-law, Middle Temple; mil. serv., 1940–43; town mag., asst. leg. advr., cust. of enemy propy., O.E.T.A., Som.; asst. registr., titles, Uga., 1938; registr., sup. ct. of Ken. and ct. of appeal for E.A., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | asst. registr., titles | Uganda | [1950, 1951, 1953] |
| 1 | 1947 | registr., sup. ct. of Ken. and ct. of appeal for E.A | Uganda *(inherited from previous clause)* | [1950, 1951, 1953] |

## Candidate stint `Shaylor, D. F___Kenya___1949`

- Staff-list name: **Shaylor, D. F** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. F. Shaylor | Registrar of Supreme Court and Court of Appeal for Eastern Africa | Judicial | — | — |
| 1950 | D. F. Shaylor | Registrar of Supreme Court and Court of Appeal for Eastern Africa | JUDICIAL | — | — |
| 1951 | D. F. Shaylor | Registrar of Supreme Court and Court of Appeal for Eastern Africa | Inland Revenue Department | — | — |

### Deterministic checks: `shaylor_denis-freke_b1906` vs `Shaylor, D. F___Kenya___1949`

- [PASS] surname_gate: bio 'SHAYLOR' vs stint 'Shaylor, D. F' (exact)
- [PASS] initials: bio ['D', 'F'] ~ stint ['D', 'F']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Shaylor, D. F___Uganda___1939`

- Staff-list name: **Shaylor, D. F** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | D. F. Shaylor | Assistant Registrars of Titles and Conveyancers | Land and Survey Department | — | — |
| 1940 | D. F. Shaylor | Assistant Registrars of Titles and Conveyancers | Land and Survey Department | — | — |

### Deterministic checks: `shaylor_denis-freke_b1906` vs `Shaylor, D. F___Uganda___1939`

- [PASS] surname_gate: bio 'SHAYLOR' vs stint 'Shaylor, D. F' (exact)
- [PASS] initials: bio ['D', 'F'] ~ stint ['D', 'F']
- [PASS] age_gate: stint starts 1939, birth 1906 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 58 vs bar 60: 'asst. registr., titles' ~ 'Assistant Registrars of Titles and Conveyancers'
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

