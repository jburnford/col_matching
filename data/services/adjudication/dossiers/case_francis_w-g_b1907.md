<!-- {"case_id": "case_francis_w-g_b1907", "bio_ids": ["francis_w-g_b1907"], "stint_ids": ["Francis, W___Palestine___1923"]} -->
# Dossier case_francis_w-g_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 55 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Francis, W___Palestine___1923` is also gate-compatible with biography(ies) outside this case: ['francis_william_e1890'] (already linked elsewhere or filtered).

## Biography `francis_w-g_b1907`

- Printed name: **FRANCIS, W. G**
- Birth year: 1907 (attested in editions [1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L15348.v` — printed in editions [1965, 1966]:**

> FRANCIS, W. G.—b. 1907; ed. Hurlford Academy and Neilston Sch.; police, Shanghai, 1930-42; police, Eritrea, 1946; asst. supt., prisons, Nig., 1947; supt., 1949; inspnr., 1952; asst. dir. prisons, 1954; dep. dir., 1960; dir., 1961-62; ret. appt. asst. supt. prisons, Zanz., 1962; supt., 1962-64; sen. supt. prisons, Zambia, 1964. (Zambia Govt. service.)

**Version `col1960-L23047.v` — printed in editions [1960, 1961, 1962, 1963, 1964]:**

> FRANCIS, W. G.—b. 1907; ed. Hurlford Academy and Neilston Sch.; police, Shanghai, 1930-42; police, Eritrea, 1946; asst. supt., prisons, Nig., 1947; supt., 1949; asst. supt. prisons, Zanz., 1952; supt., 1962. (Zanz. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1942 | police, Shanghai | — | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1946 | police, Eritrea | — | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1947 | asst. supt., prisons | Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1949 | supt | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1952 | inspnr | Nigeria *(inherited from previous clause)* | [1965, 1966] |
| 5 | 1952 | asst. supt. prisons | Zanzibar | [1960, 1961, 1962, 1963, 1964] |
| 6 | 1954 | asst. dir. prisons | Nigeria *(inherited from previous clause)* | [1965, 1966] |
| 7 | 1960 | dep. dir | Nigeria *(inherited from previous clause)* | [1965, 1966] |
| 8 | 1961–1962 | dir | Nigeria *(inherited from previous clause)* | [1965, 1966] |
| 9 | 1962 | ret. appt. asst. supt. prisons | Zanzibar | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 10 | 1964 | sen. supt. prisons, Zambia | Zanzibar *(inherited from previous clause)* | [1965, 1966] |

## Candidate stint `Francis, W___Palestine___1923`

- Staff-list name: **Francis, W** | colony: **Palestine** | listed 1923–1932 | editions [1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | W. Francis | Junior Assistant Treasurers and Inspectors of Revenue | TREASURY | — | — |
| 1924 | W. Francis | Assistant District Officer | Administrative Staff | — | — |
| 1927 | W. Francis | Assistant District Officers | District Staff | — | — |
| 1928 | W. Francis | Assistant District Officer | District Staff | — | — |
| 1929 | W. Francis | Assistant District Officer | Civil Establishment | — | — |
| 1930 | W. Francis | Assistant District Officer | District Staff | — | — |
| 1931 | W. Francis | Assistant District Officer | District Staff | — | — |
| 1932 | W. Francis | Assistant District Officer | District Staff | — | — |

### Deterministic checks: `francis_w-g_b1907` vs `Francis, W___Palestine___1923`

- [PASS] surname_gate: bio 'FRANCIS' vs stint 'Francis, W' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W']
- [PASS] age_gate: stint starts 1923, birth 1907 (age 16)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1932
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

