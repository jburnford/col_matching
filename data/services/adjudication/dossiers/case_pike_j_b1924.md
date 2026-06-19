<!-- {"case_id": "case_pike_j_b1924", "bio_ids": ["pike_j_b1924"], "stint_ids": ["Pike, J___Sarawak___1950"]} -->
# Dossier case_pike_j_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pike_j_b1924'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Pike, J___Sarawak___1950` is also gate-compatible with biography(ies) outside this case: ['pike_x_e1869'] (already linked elsewhere or filtered).

## Biography `pike_j_b1924`

- Printed name: **PIKE, J**
- Birth year: 1924 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L26261.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> PIKE, J.—b. 1924; ed. Dauntsey's Sch. and St. Edmund Hall, Oxford; mil. serv., 1943-46, capt.; admin. cadet, Sarawak, 1949; dist. offr., 1954; prin. asst. sec., 1956; under sec., 1962; state fin. sec., 1964.

**Version `col1960-L26977.v` — printed in editions [1960]:**

> PIKE, J.—b. 1924; ed. Oxford Univ.; admin. cadet, Sarawak, 1949; dist. offr., 1954; prin. asst. sec., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | admin. cadet | Sarawak | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1954 | dist. offr | Sarawak *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | prin. asst. sec | Sarawak *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1962 | under sec | Sarawak *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1964 | state fin. sec | Sarawak *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Pike, J___Sarawak___1950`

- Staff-list name: **Pike, J** | colony: **Sarawak** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. Pike | District Officers, Assistant District Officers and Cadets | Administrative Service | — | — |
| 1951 | J. Pike | District Officers, Assistant District Officers and Cadets | Administrative Service | — | — |

### Deterministic checks: `pike_j_b1924` vs `Pike, J___Sarawak___1950`

- [PASS] surname_gate: bio 'PIKE' vs stint 'Pike, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1950, birth 1924 (age 26)
- [PASS] colony: 5 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 41 vs bar 60: 'admin. cadet' ~ 'District Officers, Assistant District Officers and Cadets'
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

