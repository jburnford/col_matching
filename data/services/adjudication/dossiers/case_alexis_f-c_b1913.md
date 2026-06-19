<!-- {"case_id": "case_alexis_f-c_b1913", "bio_ids": ["alexis_f-c_b1913"], "stint_ids": ["Alexis, F. C___Grenada___1963", "Alexis, F___Windward Islands___1939"]} -->
# Dossier case_alexis_f-c_b1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `alexis_f-c_b1913`

- Printed name: **ALEXIS, F. C**
- Birth year: 1913 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1953-L16328.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> ALEXIS, F. C.—b. 1913; ed. Grenada Boys' Secondary Sch. and Royal Coll. of Surgeons, Edin.; dist. med. offr., St. V., 1935; supt. physician, col. hosp., Grenada, 1952; S.M.O., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | dist. med. offr. | St. Vincent | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1952 | supt. physician, col. hosp. | Grenada | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1955 | S.M.O | Grenada *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Alexis, F. C___Grenada___1963`

- Staff-list name: **Alexis, F. C** | colony: **Grenada** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | F. C. Alexis | Senior Medical Officer | Civil Establishment | — | — |
| 1964 | F. C. Alexis | Senior Medical Officer | Civil Establishment | — | — |
| 1965 | F. C. Alexis | Senior Medical Officer | Civil Establishment | — | — |
| 1966 | F. C. Alexis | Senior Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `alexis_f-c_b1913` vs `Alexis, F. C___Grenada___1963`

- [PASS] surname_gate: bio 'ALEXIS' vs stint 'Alexis, F. C' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F', 'C']
- [PASS] age_gate: stint starts 1963, birth 1913 (age 50)
- [PASS] colony: 2 placed event(s) resolve to 'Grenada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1966
- [FAIL] position_sim: best 16 vs bar 60: 'S.M.O' ~ 'Senior Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Alexis, F___Windward Islands___1939`

- Staff-list name: **Alexis, F** | colony: **Windward Islands** | listed 1939–1950 | editions [1939, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | F. Alexis | District Medical Officer | Medical | — | — |
| 1950 | F. Alexis | Medical Officer | Medical | — | — |

### Deterministic checks: `alexis_f-c_b1913` vs `Alexis, F___Windward Islands___1939`

- [PASS] surname_gate: bio 'ALEXIS' vs stint 'Alexis, F' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F']
- [PASS] age_gate: stint starts 1939, birth 1913 (age 26)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1950
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

