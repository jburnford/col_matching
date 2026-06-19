<!-- {"case_id": "case_gunter_p-c_b1906", "bio_ids": ["gunter_p-c_b1906"], "stint_ids": ["Gunter, P. C___Jamaica___1954"]} -->
# Dossier case_gunter_p-c_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gunter_p-c_b1906`

- Printed name: **GUNTER, P. C**
- Birth year: 1906 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L23674.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> GUNTER, P. C.—b. 1906; ed. Wolmer's Sch., J'ca; solicitor; dep. clk., courts, J'ca, 1933; clk., courts, 1939; registr., titles, 1954. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | dep. clk., courts | Jamaica | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1939 | clk., courts | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1954 | registr., titles | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Gunter, P. C___Jamaica___1954`

- Staff-list name: **Gunter, P. C** | colony: **Jamaica** | listed 1954–1956 | editions [1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | P. C. Gunter | Registrar of Titles | Civil Establishment | — | — |
| 1955 | P. C. Gunter | Registrar of Titles | Civil Establishment | — | — |
| 1956 | P. C. Gunter | Registrar of Titles | Civil Establishment | — | — |

### Deterministic checks: `gunter_p-c_b1906` vs `Gunter, P. C___Jamaica___1954`

- [PASS] surname_gate: bio 'GUNTER' vs stint 'Gunter, P. C' (exact)
- [PASS] initials: bio ['P', 'C'] ~ stint ['P', 'C']
- [PASS] age_gate: stint starts 1954, birth 1906 (age 48)
- [PASS] colony: 3 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1954-1956
- [PASS] position_sim: best 85 vs bar 60: 'registr., titles' ~ 'Registrar of Titles'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

