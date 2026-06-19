<!-- {"case_id": "case_sykes_edwin-leonard_b1914", "bio_ids": ["sykes_edwin-leonard_b1914", "sykes_l_b1913"], "stint_ids": ["Sykes, L___Hong Kong___1949"]} -->
# Dossier case_sykes_edwin-leonard_b1914

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sykes_l_b1913'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Sykes, L___Hong Kong___1949'] have more than one claimant biography in this case.

## Biography `sykes_edwin-leonard_b1914`

- Printed name: **SYKES, EDWIN LEONARD**
- Birth year: 1914 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71048.v` — printed in editions [1939, 1940]:**

> SYKES, EDWIN LEONARD.—B. 1914; ed. Leys Schol. and Trinity Coll., Cambridge (senr. schol., 1936); 1st ols. history tripes., pt. I, 1935 and pt. II, 1936; B.A., 1936; appt. after compet. exam., asst. prin., D.O., Oct., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935–1936 | — | — | [1939, 1940] |
| 1 | 1936–1936 | — | — | [1939, 1940] |
| 2 | 1937 | asst. prin. | Dominions Office | [1939, 1940] |

## Biography `sykes_l_b1913`

- Printed name: **SYKES, L**
- Birth year: 1913 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L24461.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> SYKES, L.—b. 1913; senr. traffic supt., rlwy., H.K., 1938; stores offr., 1946; traffic asst., 1947; traffic supt., S.L., 1951. (S.L. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | senr. traffic supt., rlwy. | Hong Kong | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1946 | stores offr | Hong Kong *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1947 | traffic asst | Hong Kong *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1951 | traffic supt. | Sierra Leone | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Sykes, L___Hong Kong___1949`

- Staff-list name: **Sykes, L** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. Sykes | Stores Officer | Kowloon-Canton Railway | — | — |
| 1950 | L. Sykes | Traffic Manager | KOWLOON CANTON RAILWAY | — | — |

### Deterministic checks: `sykes_edwin-leonard_b1914` vs `Sykes, L___Hong Kong___1949`

- [PASS] surname_gate: bio 'SYKES' vs stint 'Sykes, L' (exact)
- [PASS] initials: bio ['E', 'L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `sykes_l_b1913` vs `Sykes, L___Hong Kong___1949`

- [PASS] surname_gate: bio 'SYKES' vs stint 'Sykes, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [PASS] position_sim: best 74 vs bar 60: 'traffic asst' ~ 'Traffic Manager'
- [FAIL] honour: no shared honour
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

