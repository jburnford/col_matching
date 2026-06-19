<!-- {"case_id": "case_jackson_h-w_b1906", "bio_ids": ["jackson_h-w_b1906"], "stint_ids": ["Jackson, H. W___Singapore___1952"]} -->
# Dossier case_jackson_h-w_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 144 official(s) with this surname in the graph's staff lists; 60 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jackson_h-w_b1906`

- Printed name: **JACKSON, H. W**
- Birth year: 1906 (attested in editions [1954, 1955, 1956, 1957, 1958, 1959])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1954-L21000.v` — printed in editions [1954, 1955, 1956, 1957, 1958, 1959]:**

> JACKSON, H. W.—b. 1906; ed. Shawlands Acad., Cusack's Coll., and New York Univ.: M. of I., 1940-45; hd., dipl. sect., control off. (Germany and Austria), 1946; dep. dir., b'casting, Mal., 1946; dir., 1951-58.

**Version `col1953-L17912.v` — printed in editions [1953]:**

> JACKSON, H. W.—b. 1906; ed. Shawlands Acad., Cusacks Coll., and New York Univ.; dep. dir., b'casting, Mal., 1946; dir., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | hd., dipl. sect., control off. (Germany and Austria) | — | [1954, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1946 | dep. dir., b'casting | Malaya | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 2 | 1951–1958 | dir | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |

## Candidate stint `Jackson, H. W___Singapore___1952`

- Staff-list name: **Jackson, H. W** | colony: **Singapore** | listed 1952–1958 | editions [1952, 1953, 1954, 1955, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | H. W. Jackson | Director of Broadcasting, Malaya (Acting) | Civil Establishment | — | — |
| 1953 | H. W. Jackson | Director of Broadcasting | Civil Establishment | — | — |
| 1954 | H. W. Jackson | Director of Broadcasting, Malaya | Civil Establishment | — | — |
| 1955 | H. W. Jackson | Director of Broadcasting, Malaya | Civil Establishment | — | — |
| 1957 | H. W. Jackson | Director of Broadcasting, Malaya | Civil Establishment | — | — |
| 1958 | H. W. Jackson | Director of Broadcasting, Malaya | Civil Establishment | — | — |

### Deterministic checks: `jackson_h-w_b1906` vs `Jackson, H. W___Singapore___1952`

- [PASS] surname_gate: bio 'JACKSON' vs stint 'Jackson, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1952, birth 1906 (age 46)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1958
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

