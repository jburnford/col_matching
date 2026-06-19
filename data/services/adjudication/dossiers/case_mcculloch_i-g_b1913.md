<!-- {"case_id": "case_mcculloch_i-g_b1913", "bio_ids": ["mcculloch_i-g_b1913"], "stint_ids": ["McCulloch, I. G___Nyasaland___1963", "McCulloch, I. G___Uganda___1949"]} -->
# Dossier case_mcculloch_i-g_b1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcculloch_i-g_b1913`

- Printed name: **McCULLOCH, I. G**
- Birth year: 1913 (attested in editions [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L25258.v` — printed in editions [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966]:**

> McCULLOCH, I. G.—b. 1913; ed. John Neilson Sch., Paisley; mil. serv., 1940–46, t. maj.; asst. civil reabsorption offr., Uga., 1945; labr. offr., 1948; senr. labr. offr., 1953; dep. comsnr., labr. and welfare, Aden, 1958; dep. comsnr., labr., Nyasa, 1960; comsnr., 1962; under sec., 1962; perm. sec., min. of labr., 1962. (Malawi Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | asst. civil reabsorption offr. | Uganda | [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966] |
| 1 | 1948 | labr. offr | Uganda *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966] |
| 2 | 1953 | senr. labr. offr | Uganda *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966] |
| 3 | 1958 | dep. comsnr., labr. and welfare | Aden | [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966] |
| 4 | 1960 | dep. comsnr., labr. | Nyasaland | [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966] |
| 5 | 1962 | comsnr | Nyasaland *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1963, 1964, 1965, 1966] |

## Candidate stint `McCulloch, I. G___Nyasaland___1963`

- Staff-list name: **McCulloch, I. G** | colony: **Nyasaland** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | I. G. McCulloch | Permanent Secretary | Ministry of Labour | — | — |
| 1964 | I. G. McCulloch | Permanent Secretary | Ministry of Labour | — | — |

### Deterministic checks: `mcculloch_i-g_b1913` vs `McCulloch, I. G___Nyasaland___1963`

- [PASS] surname_gate: bio 'McCULLOCH' vs stint 'McCulloch, I. G' (exact)
- [PASS] initials: bio ['I', 'G'] ~ stint ['I', 'G']
- [PASS] age_gate: stint starts 1963, birth 1913 (age 50)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1963-1964
- [FAIL] position_sim: best 35 vs bar 60: 'dep. comsnr., labr.' ~ 'Permanent Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `McCulloch, I. G___Uganda___1949`

- Staff-list name: **McCulloch, I. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | I. G. McCulloch | Labour Officer | Labour | — | — |
| 1951 | I. G. McCulloch | Labour Officer | Labour | — | — |

### Deterministic checks: `mcculloch_i-g_b1913` vs `McCulloch, I. G___Uganda___1949`

- [PASS] surname_gate: bio 'McCULLOCH' vs stint 'McCulloch, I. G' (exact)
- [PASS] initials: bio ['I', 'G'] ~ stint ['I', 'G']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 78 vs bar 60: 'labr. offr' ~ 'Labour Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

