<!-- {"case_id": "case_peat_a-a_b1904", "bio_ids": ["peat_a-a_b1904"], "stint_ids": ["Peat, A. A___Trinidad and Tobago___1949"]} -->
# Dossier case_peat_a-a_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peat_a-a_b1904`

- Printed name: **PEAT, A. A**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: C.B.E (1963)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1948-L35171.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> PEAT, A. A., C.B.E. (1963).—b. 1904; ed. Beckford and Smith's Sch., Spanish Town, J'ca, J'ca Coll., and Aberdeen and Harvard Univs.; M.O. (H), J'ca, 1935; asst. D.M.S. (hosp. and personnel), 1945; D.M.S., Trin., 1948; chief M.O., J'ca, 1956. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | M.O. (H) | Jamaica | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1945 | asst. D.M.S. (hosp. and personnel) | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1948 | D.M.S. | Trinidad | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1956 | chief M.O. | Jamaica | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Peat, A. A___Trinidad and Tobago___1949`

- Staff-list name: **Peat, A. A** | colony: **Trinidad and Tobago** | listed 1949–1954 | editions [1949, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. A. Peat | Director of Medical Services | Health | — | — |
| 1952 | Dr. A. A. Peat | Director of Medical Services | Civil Establishment | — | — |
| 1953 | A. A. Peat | Director of Medical Services | Civil Establishment | — | — |
| 1954 | A. A. Peat | Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `peat_a-a_b1904` vs `Peat, A. A___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'PEAT' vs stint 'Peat, A. A' (exact)
- [PASS] initials: bio ['A', 'A'] ~ stint ['A', 'A']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

