<!-- {"case_id": "case_hadley_c-v-d_b1900", "bio_ids": ["hadley_c-v-d_b1900"], "stint_ids": ["Hadley, C. V. D___Windward Islands___1950", "Hadley, Digby___Windward Islands___1922"]} -->
# Dossier case_hadley_c-v-d_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hadley_c-v-d_b1900`

- Printed name: **HADLEY, C. V. D**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961])
- Honours: M.B.E (1961)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1948-L33072.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]:**

> HADLEY, C. V. D., M.B.E. (1961).—b. 1900; ed. St. Vincent Gram. Sch., Bristol Univ. and Trinity Coll., Camb.; mil. serv. in first world war; asst. mstr., Grenada boys' sec. sch., 1937; res. sec-tutor, second soc. welf. course, J'ca, 1944; soc. welf. offr., St. V., 1945; educ. offr., and chief inspr., schs., 1950-60; Wind. Is. educ. surv., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | asst. mstr., Grenada boys' sec. sch | Grenada | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1944 | res. sec-tutor, second soc. welf. course | Jamaica | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1945 | soc. welf. offr. | St. Vincent | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 3 | 1953 | Wind. Is. educ. surv | St. Vincent *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Hadley, C. V. D___Windward Islands___1950`

- Staff-list name: **Hadley, C. V. D** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | C. V. D. Hadley | Social Welfare Officer | Social Welfare | — | — |
| 1952 | C. V. D. Hadley | Education Officer | Civil Establishment | — | — |

### Deterministic checks: `hadley_c-v-d_b1900` vs `Hadley, C. V. D___Windward Islands___1950`

- [PASS] surname_gate: bio 'HADLEY' vs stint 'Hadley, C. V. D' (exact)
- [PASS] initials: bio ['C', 'V', 'D'] ~ stint ['C', 'V', 'D']
- [PASS] age_gate: stint starts 1950, birth 1900 (age 50)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hadley, Digby___Windward Islands___1922`

- Staff-list name: **Hadley, Digby** | colony: **Windward Islands** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Digby Hadley | Executive Council Member | Executive Council | — | — |
| 1923 | Digby Hadley | Executive Council Member | Executive Council | — | — |
| 1924 | Digby Hadley | Executive Council Member | Executive Council | — | — |
| 1925 | Digby Hadley | Member, Executive Council | Executive Council | — | — |
| 1925 | Digby Hadley | Member, Legislative Council | Legislative Council | — | — |

### Deterministic checks: `hadley_c-v-d_b1900` vs `Hadley, Digby___Windward Islands___1922`

- [PASS] surname_gate: bio 'HADLEY' vs stint 'Hadley, Digby' (exact)
- [PASS] initials: bio ['C', 'V', 'D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1922, birth 1900 (age 22)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
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

