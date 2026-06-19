<!-- {"case_id": "case_gilbert_william-thomas-moran_b1900", "bio_ids": ["gilbert_william-thomas-moran_b1900"], "stint_ids": ["Gilbert, W. T. M___St Helena___1958"]} -->
# Dossier case_gilbert_william-thomas-moran_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gilbert_william-thomas-moran_b1900`

- Printed name: **GILBERT, William Thomas Moran**
- Birth year: 1900 (attested in editions [1953, 1954, 1955])
- Honours: L.R.C.S
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1953-L17432.v` — printed in editions [1953, 1954, 1955]:**

> GILBERT, W. T. M.—b. 1900; ed. Rathmines Sch., Dublin; med. offr., Nig., 1930; S.M.O., 1949; asst. D.M.S., G.C., 1951; prin. M.O., 1953.

**Version `col1948-L32827.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GILBERT, William Thomas Moran, L.R.C.S., L.R.C.P. (Dub.)—b. 1900; ed. Rathmines Sch., Dublin; med. offr., Nig., 1930; S.M.O., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | med. offr. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1949 | S.M.O | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955] |
| 2 | 1950 | S.M.O | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1951 | asst. D.M.S. | Gold Coast | [1953, 1954, 1955] |
| 4 | 1953 | prin. M.O | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955] |

## Candidate stint `Gilbert, W. T. M___St Helena___1958`

- Staff-list name: **Gilbert, W. T. M** | colony: **St Helena** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | W. T. M. Gilbert | Senior Medical Officer | Civil Establishment | — | — |
| 1960 | W. T. M. Gilbert | Senior Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `gilbert_william-thomas-moran_b1900` vs `Gilbert, W. T. M___St Helena___1958`

- [PASS] surname_gate: bio 'GILBERT' vs stint 'Gilbert, W. T. M' (exact)
- [PASS] initials: bio ['W', 'T', 'M'] ~ stint ['W', 'T', 'M']
- [PASS] age_gate: stint starts 1958, birth 1900 (age 58)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
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

