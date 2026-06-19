<!-- {"case_id": "case_dupavillon_h-a_b1908", "bio_ids": ["dupavillon_h-a_b1908"], "stint_ids": ["Dupavillon, H. A___Mauritius___1949"]} -->
# Dossier case_dupavillon_h-a_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dupavillon_h-a_b1908`

- Printed name: **DUPAVILLON, H. A**
- Birth year: 1908 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: C.P.M
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L22191.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> DUPAVILLON, H. A., C.P.M.—b. 1908; ed. Royal Coll., Maur.; police constable, Maur., 1926; police cadet, 1927; 1st cl. sgt., 1931; staff sgt., 1939; asst. supt., police, 1940; supt., 1947; senr. supt., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | police constable | Mauritius | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1927 | police cadet | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1931 | 1st cl. sgt | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1939 | staff sgt | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1940 | asst. supt., police | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 5 | 1947 | supt | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 6 | 1959 | senr. supt | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Dupavillon, H. A___Mauritius___1949`

- Staff-list name: **Dupavillon, H. A** | colony: **Mauritius** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. A. Dupavillon | Superintendent | Police | — | — |
| 1950 | H. A. Dupavillon | Superintendent | Police | — | — |

### Deterministic checks: `dupavillon_h-a_b1908` vs `Dupavillon, H. A___Mauritius___1949`

- [PASS] surname_gate: bio 'DUPAVILLON' vs stint 'Dupavillon, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1949, birth 1908 (age 41)
- [PASS] colony: 7 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 44 vs bar 60: 'supt' ~ 'Superintendent'
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

