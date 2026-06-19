<!-- {"case_id": "case_carr_george-thomas-whitmore_b1913", "bio_ids": ["carr_george-thomas-whitmore_b1913"], "stint_ids": ["Carr, G. T. W___Trinidad and Tobago___1937"]} -->
# Dossier case_carr_george-thomas-whitmore_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carr_george-thomas-whitmore_b1913`

- Printed name: **CARR, George Thomas Whitmore**
- Birth year: 1913 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.V.O. (1966), O.B.E. (1962), Q.P.M. (1959)
- Appears in editions: [1948, 1949, 1950, 1951, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L21210.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> CARR, G. T. W., C.V.O. (1966), O.B.E. (1962), Q.P.M. (1959).—b. 1913; ed. Queen's Royal Coll., Trin.; 4th cl. Clk., customs and excise, Trin., 1931, asst. supt., police, 1934; supt., 1944; asst. comsnr., police, 1955; dep. comsnr., 1956; comsnr., 1962. (T'dad. Govt. service.)

**Version `col1948-L31649.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CARR, George Thomas Whitmore.—b. 1913; ed. Queen's Royal Coll., Trin.; clk., Trin., 1931; asst. supt., police, 1931; senr. asst. supt., 1938; supt., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931–1931 | 4th cl. Clk., customs and excise | Trinidad | [1948, 1949, 1950, 1951, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1934–1934 | asst. supt., police | — | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1938 | senr. asst. supt | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1944–1944 | supt. | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1955–1955 | asst. comsnr., police | — | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1956–1956 | dep. comsnr. | — | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1962–1962 | comsnr. | — | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Carr, G. T. W___Trinidad and Tobago___1937`

- Staff-list name: **Carr, G. T. W** | colony: **Trinidad and Tobago** | listed 1937–1949 | editions [1937, 1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | G. T. W. Carr | Sub-Inspectors | Constabulary | — | — |
| 1939 | G. T. W. Carr | Assistant Superintendent | Police | — | — |
| 1940 | G. T. W. Carr | Assistant Superintendent | Police | — | Captain |
| 1949 | G. T. W. Carr | Superintendents | Police | — | — |

### Deterministic checks: `carr_george-thomas-whitmore_b1913` vs `Carr, G. T. W___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'CARR' vs stint 'Carr, G. T. W' (exact)
- [PASS] initials: bio ['G', 'T', 'W'] ~ stint ['G', 'T', 'W']
- [PASS] age_gate: stint starts 1937, birth 1913 (age 24)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1949
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

