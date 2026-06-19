<!-- {"case_id": "case_gross_j_b1906", "bio_ids": ["gross_j_b1906"], "stint_ids": ["Gross, J___Palestine___1931"]} -->
# Dossier case_gross_j_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gross_j_b1906'] carry a single initial only — the namesake trap applies.

## Biography `gross_j_b1906`

- Printed name: **GROSS, J**
- Birth year: 1906 (attested in editions [1961, 1962])
- Appears in editions: [1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1961-L22785.v` — printed in editions [1961, 1962]:**

> GROSS, J.—b. 1906; ed. Oberreal Schule Nord, Leipzig, Leipzig and Dresden Univ.; mil. serv., 1943-46; met. dept., E.A.C.S.O., 1948; exec. engnr., E.A.P. & T. admin., 1955; senr. exec. engnr., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | met. dept., E.A.C.S.O | — | [1961, 1962] |
| 1 | 1955 | exec. engnr., E.A.P. & T. admin | East Africa Protectorate | [1961, 1962] |
| 2 | 1960 | senr. exec. engnr | East Africa Protectorate *(inherited from previous clause)* | [1961, 1962] |

## Candidate stint `Gross, J___Palestine___1931`

- Staff-list name: **Gross, J** | colony: **Palestine** | listed 1931–1940 | editions [1931, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. Gross | Senior Assistant Treasurer | Treasury | — | — |
| 1940 | J. Gross | Senior Assistant Treasurer | Treasury | — | — |

### Deterministic checks: `gross_j_b1906` vs `Gross, J___Palestine___1931`

- [PASS] surname_gate: bio 'GROSS' vs stint 'Gross, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1931, birth 1906 (age 25)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1940
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

