<!-- {"case_id": "case_flores_j_b1907", "bio_ids": ["flores_j_b1907"], "stint_ids": ["Flores, C. J___Malta___1934", "Flores, J___Malta___1960"]} -->
# Dossier case_flores_j_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['flores_j_b1907'] carry a single initial only — the namesake trap applies.

## Biography `flores_j_b1907`

- Printed name: **FLORES, J**
- Birth year: 1907 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L23050.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> FLORES, J.—b. 1907; ed. Flores Coll., and Royal Univ. of Malta; vice-pres., chamber of advocates, 1953; speaker, Malta leg. assembly, 1955; lectr., canon law, Royal Univ. of Malta, 1955; judge, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | vice-pres., chamber of advocates | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1955 | speaker, Malta leg. assembly | Malta | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Flores, C. J___Malta___1934`

- Staff-list name: **Flores, C. J** | colony: **Malta** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | C. J. Flores | Masters | Lyceum | — | — |
| 1936 | C. J. Flores | Masters | Education Department | — | — |

### Deterministic checks: `flores_j_b1907` vs `Flores, C. J___Malta___1934`

- [PASS] surname_gate: bio 'FLORES' vs stint 'Flores, C. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1934, birth 1907 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Flores, J___Malta___1960`

- Staff-list name: **Flores, J** | colony: **Malta** | listed 1960–1964 | editions [1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | J. Flores | Judge | Judiciary | — | — |
| 1961 | J. Flores | Judge | Judiciary | — | — |
| 1962 | J. Flores | Judge | Judiciary | — | — |
| 1963 | J. Flores | Judge | Judiciary | — | — |
| 1964 | J. Flores | Judge | Judiciary | — | — |

### Deterministic checks: `flores_j_b1907` vs `Flores, J___Malta___1960`

- [PASS] surname_gate: bio 'FLORES' vs stint 'Flores, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1960, birth 1907 (age 53)
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1960-1964
- [FAIL] position_sim: best 13 vs bar 60: 'speaker, Malta leg. assembly' ~ 'Judge'
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

