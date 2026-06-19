<!-- {"case_id": "case_brazier_john-alfred_b1900", "bio_ids": ["brazier_john-alfred_b1900"], "stint_ids": ["Brazier, J. A___Federation of Malaya___1950"]} -->
# Dossier case_brazier_john-alfred_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brazier_john-alfred_b1900`

- Printed name: **BRAZIER, John Alfred**
- Birth year: 1900 (attested in editions [1951, 1953, 1954, 1955, 1956])
- Honours: M.B.E
- Appears in editions: [1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1951-L36407.v` — printed in editions [1951, 1953, 1954, 1955, 1956]:**

> BRAZIER, John Alfred, M.B.E.—b. 1900; ed. L.C.C. Tech. Coll., Nat. Coun. of Labour Coll. and Ruskin Coll.; mag. and J.P.; labour and welf. offr., rlwys., Mal., 1945; trade union advr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | labour and welf. offr., rlwys. | Malaya | [1951, 1953, 1954, 1955, 1956] |
| 1 | 1946 | trade union advr | Malaya *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956] |

## Candidate stint `Brazier, J. A___Federation of Malaya___1950`

- Staff-list name: **Brazier, J. A** | colony: **Federation of Malaya** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. A. Brazier | Trade Union Adviser | Civil Establishment | M.B.E. | — |
| 1952 | J. A. Brazier | Trade Union Adviser* | Civil Establishment | — | — |

### Deterministic checks: `brazier_john-alfred_b1900` vs `Brazier, J. A___Federation of Malaya___1950`

- [PASS] surname_gate: bio 'BRAZIER' vs stint 'Brazier, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1950, birth 1900 (age 50)
- [PASS] colony: 2 placed event(s) resolve to 'Federation of Malaya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1952
- [PASS] position_sim: best 91 vs bar 60: 'trade union advr' ~ 'Trade Union Adviser'
- [PASS] honour: shared: M.B.E
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

