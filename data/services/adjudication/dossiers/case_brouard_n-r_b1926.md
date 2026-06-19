<!-- {"case_id": "case_brouard_n-r_b1926", "bio_ids": ["brouard_n-r_b1926"], "stint_ids": ["Brouard, R___Mauritius___1949"]} -->
# Dossier case_brouard_n-r_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `brouard_n-r_b1926` ↔ `Brouard, R___Mauritius___1949` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Brouard, R___Mauritius___1949` is also gate-compatible with biography(ies) outside this case: ['brouard_raoul_b1901'] (already linked elsewhere or filtered).

## Biography `brouard_n-r_b1926`

- Printed name: **BROUARD, N. R**
- Birth year: 1926 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L20887.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> BROUARD, N. R.—b. 1926; ed. Royal Coll., Maur. and Univ. of Wales, Bangor; temp. clk., Maur., 1945; forester, gr. I, 1948; dep. ranger, 1949; forest ranger, 1955; asst. conserv., forests, 1955; dep. conserv. forests, 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | temp. clk. | Mauritius | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | forester, gr. I | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1949 | dep. ranger | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1955 | forest ranger | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1960 | dep. conserv. forests | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Brouard, R___Mauritius___1949`

- Staff-list name: **Brouard, R** | colony: **Mauritius** | listed 1949–1961 | editions [1949, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. Brouard | Master and Registrar | JUDICIAL | — | — |
| 1952 | R. Brouard | Registrar General | Civil Establishment | — | — |
| 1953 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1954 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1955 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1956 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1957 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1958 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1959 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1960 | R. Brouard | Registrar-General | Civil Establishment | — | — |
| 1961 | R. Brouard | Registrar-General | Civil Establishment | — | — |

### Deterministic checks: `brouard_n-r_b1926` vs `Brouard, R___Mauritius___1949`

- [PASS] surname_gate: bio 'BROUARD' vs stint 'Brouard, R' (exact)
- [PASS] initials: bio ['N', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1949, birth 1926 (age 23)
- [PASS] colony: 5 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1949-1961
- [PASS] position_sim: best 62 vs bar 60: 'forest ranger' ~ 'Registrar-General'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1958, 1959] pos~62 (bar: >=2)
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

