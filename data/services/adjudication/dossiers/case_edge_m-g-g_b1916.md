<!-- {"case_id": "case_edge_m-g-g_b1916", "bio_ids": ["edge_m-g-g_b1916"], "stint_ids": ["Edge, M. G___North Borneo___1940"]} -->
# Dossier case_edge_m-g-g_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `edge_m-g-g_b1916`

- Printed name: **EDGE, M. G. G**
- Birth year: 1916 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.P.M (1962)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L22745.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> EDGE, M. G., C.P.M. (1962).—b. 1916; ed. Chigwell Sch., and Queen Mary Coll., Lond. Univ.; interned, 1942-45; N.B.A.C., 1939; asst. supt., 1942; col. police serv., N. Borneo, 1946; dep. supt., 1949; supt., 1956.

**Version `col1956-L20960.v` — printed in editions [1956]:**

> EDGE, M. G. G.—b. 1916; ed. Chigwell Sch. and Univ. Coll., London; mil. serv., 1942-46, lieut., p.o.w., 1942-45; cadet (Chartered Co.'s. serv.) N. Borneo, 1937; dist. offr., and mag., 1941; dist. offr., col. admin. serv., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | cadet (Chartered Co.'s. serv.) N. Borneo | — | [1956] |
| 1 | 1939 | N.B.A.C | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1941 | dist. offr., and mag | — | [1956] |
| 3 | 1942–1945 | interned | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1942 | asst. supt | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1946 | col. police serv. | North Borneo | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1946 | dist. offr., col. admin. serv | — | [1956] |
| 7 | 1949 | dep. supt | North Borneo *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 8 | 1956 | supt | North Borneo *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Edge, M. G___North Borneo___1940`

- Staff-list name: **Edge, M. G** | colony: **North Borneo** | listed 1940–1951 | editions [1940, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | M. G. Edge | Chief Police Officer, Sandakan | Other Officers | — | — |
| 1940 | M. G. Edge | Cadet | Cadets | — | — |
| 1949 | M. G. Edge | Assistant Superintendents (m) | CONSTABULARY | — | — |
| 1950 | M. G. Edge | Assistant Superintendent | POLICE | — | — |
| 1951 | M. G. Edge | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `edge_m-g-g_b1916` vs `Edge, M. G___North Borneo___1940`

- [PASS] surname_gate: bio 'EDGE' vs stint 'Edge, M. G' (exact)
- [PASS] initials: bio ['M', 'G', 'G'] ~ stint ['M', 'G']
- [PASS] age_gate: stint starts 1940, birth 1916 (age 24)
- [PASS] colony: 3 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1940-1951
- [FAIL] position_sim: best 57 vs bar 60: 'col. police serv.' ~ 'Chief Police Officer, Sandakan'
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

