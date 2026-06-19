<!-- {"case_id": "case_parsons_thomas-reginald_b1898", "bio_ids": ["parsons_thomas-reginald_b1898"], "stint_ids": ["Parsons, R___North Borneo___1950"]} -->
# Dossier case_parsons_thomas-reginald_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `parsons_thomas-reginald_b1898`

- Printed name: **PARSONS, THOMAS REGINALD**
- Birth year: 1898 (attested in editions [1956, 1957, 1958])
- Honours: I.S.O (1956), M.B.E
- Appears in editions: [1939, 1940, 1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1956-L23420.v` — printed in editions [1956, 1957, 1958]:**

> PARSONS, T. R., I.S.O. (1956), M.B.E.—b. 1898; mil. serv., 1916-19; boy clk., G.P.O., 1914; asst. clk. (clerical offr.), 1916; trans. to C.O., 1923; higher clerical offr., 1938; higher exec. offr., 1944; senr. exec. offr., 1948; chief exec. offr., 1954.

**Version `col1939-L69638.v` — printed in editions [1939, 1940]:**

> PARSONS, THOMAS REGINALD.—B. 1898; entd. savings bank dept., G.P.O., June, 1914; apprd. after compet. exam., asst. clk., Apr., 1916; served in R.N., Apr., 1917-Apr., 1919; trans. to C.O. as cler.-offr., Sept., 1922; higher grade cler.-offr., Jan., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | boy clk., G.P.O | — | [1956, 1957, 1958] |
| 1 | 1914 | entd. savings bank dept., G.P.O | — | [1939, 1940] |
| 2 | 1916 | asst. clk. (clerical offr.) | — | [1956, 1957, 1958] |
| 3 | 1916 | apprd. after compet. exam., asst. clk | — | [1939, 1940] |
| 4 | 1917–1919 | served in R.N | — | [1939, 1940] |
| 5 | 1922 | trans. to C.O. as cler.-offr | Colonial Office | [1939, 1940] |
| 6 | 1923 | trans. to C.O | — | [1956, 1957, 1958] |
| 7 | 1938 | higher clerical offr | — | [1956, 1957, 1958] |
| 8 | 1938 | higher grade cler.-offr | Colonial Office *(inherited from previous clause)* | [1939, 1940] |
| 9 | 1944 | higher exec. offr | — | [1956, 1957, 1958] |
| 10 | 1948 | senr. exec. offr | — | [1956, 1957, 1958] |
| 11 | 1954 | chief exec. offr | — | [1956, 1957, 1958] |

## Candidate stint `Parsons, R___North Borneo___1950`

- Staff-list name: **Parsons, R** | colony: **North Borneo** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. Parsons | Cadet | District Administration | — | — |
| 1951 | R. Parsons | Cadet | District Administration | — | — |

### Deterministic checks: `parsons_thomas-reginald_b1898` vs `Parsons, R___North Borneo___1950`

- [PASS] surname_gate: bio 'PARSONS' vs stint 'Parsons, R' (exact)
- [PASS] initials: bio ['T', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1950, birth 1898 (age 52)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

