<!-- {"case_id": "case_adamson_e_b1921", "bio_ids": ["adamson_e_b1921"], "stint_ids": ["Adamson, E___Singapore___1959"]} -->
# Dossier case_adamson_e_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['adamson_e_b1921'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Adamson, E___Singapore___1959` is also gate-compatible with biography(ies) outside this case: ['adamson_alfred-edward_b1871', 'adamson_st-john-ernest_b1867'] (already linked elsewhere or filtered).

## Biography `adamson_e_b1921`

- Printed name: **ADAMSON, E**
- Birth year: 1921 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L20491.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> ADAMSON, E.—b. 1921; ed. Bootle Gram. Sch. and L'pool Univ.; mil. serv., 1943-46; junr. scienc. offr., min. of aircraft prod., 1942; asst. engrn., P.W.D., Mal., 1946; senr. exec. engrn., P.W.D., S'pore, 1955; chief engrn., 1957; D.D.P.W., 1958-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | junr. scienc. offr., min. of aircraft prod | — | [1957, 1958, 1959, 1960, 1961] |
| 1 | 1946 | asst. engrn., P.W.D. | Malaya | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1955 | senr. exec. engrn., P.W.D., S'pore | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 3 | 1957 | chief engrn | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 4 | 1958–1960 | D.D.P.W | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Adamson, E___Singapore___1959`

- Staff-list name: **Adamson, E** | colony: **Singapore** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | E. Adamson | Deputy Director of Public Works | Civil Establishment | — | — |
| 1960 | E. Adamson | Deputy Director of Public Works | Ministry of National Development | — | — |

### Deterministic checks: `adamson_e_b1921` vs `Adamson, E___Singapore___1959`

- [PASS] surname_gate: bio 'ADAMSON' vs stint 'Adamson, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1959, birth 1921 (age 38)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1960
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

