<!-- {"case_id": "case_suttie_r-s_b1915", "bio_ids": ["suttie_r-s_b1915"], "stint_ids": ["Suttie, R. S___Gold Coast___1950"]} -->
# Dossier case_suttie_r-s_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `suttie_r-s_b1915`

- Printed name: **SUTTIE, R. S.**
- Birth year: 1915 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L28381.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> SUTTIE, R. S.—b. 1915; ed. Stobswell Sch., Dundee, and Edin. Univ.; mil. serv., 1940-46, w/sgt.; Br. P.O., 1930-39, civil service, 1939-48; records offr., lands dept., G.C., 1948; asst. contrlr., posts, 1950; district contrlr., 1954; regional contrlr. (Ghana civil service), 1956; retd., re-apptd. asst. contrlr., posts, H.K., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1939 | — | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1939–1948 | civil service | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1940–1946 | mil. serv., w/sgt. | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1948 | records offr., lands dept. | Gold Coast | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1950 | asst. contrlr., posts | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1954 | district contrlr. | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1956 | regional contrlr. (Ghana civil service) | Ghana | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 7 | 1959 | asst. contrlr., posts | Hong Kong | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Suttie, R. S___Gold Coast___1950`

- Staff-list name: **Suttie, R. S** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. S. Suttie | Officers-in-Charge Records | LANDS | — | — |
| 1951 | R. S. Suttie | Assistant Controllers of Posts | Traffic Branch | — | — |

### Deterministic checks: `suttie_r-s_b1915` vs `Suttie, R. S___Gold Coast___1950`

- [PASS] surname_gate: bio 'SUTTIE' vs stint 'Suttie, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1950, birth 1915 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 51 vs bar 60: 'records offr., lands dept.' ~ 'Officers-in-Charge Records'
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

