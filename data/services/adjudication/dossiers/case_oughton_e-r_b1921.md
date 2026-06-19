<!-- {"case_id": "case_oughton_e-r_b1921", "bio_ids": ["oughton_e-r_b1921"], "stint_ids": ["Oughton, E. R___Gold Coast___1949"]} -->
# Dossier case_oughton_e-r_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `oughton_e-r_b1921`

- Printed name: **OUGHTON, E. R**
- Birth year: 1921 (attested in editions [1959, 1960, 1961])
- Appears in editions: [1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1959-L26589.v` — printed in editions [1959, 1960, 1961]:**

> OUGHTON, E. R.—b. 1921; ed. Repton Sch., Emmanuel Coll., Camb.; mil. serv., 1939-47; asst. supt., police, G.C., 1948; supt., 1954; senr. supt., 1957; asst. comsnr., police, 1958-60 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | asst. supt., police | Gold Coast | [1959, 1960, 1961] |
| 1 | 1954 | supt | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961] |
| 2 | 1957 | senr. supt | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961] |
| 3 | 1958–1960 | asst. comsnr., police | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961] |

## Candidate stint `Oughton, E. R___Gold Coast___1949`

- Staff-list name: **Oughton, E. R** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. R. Oughton | Senior Assistant Superintendents and Assistant Superintendents | Police | — | — |
| 1951 | E. R. Oughton | Senior Assistant Superintendent / Assistant Superintendent / Cadet | Police | — | — |

### Deterministic checks: `oughton_e-r_b1921` vs `Oughton, E. R___Gold Coast___1949`

- [PASS] surname_gate: bio 'OUGHTON' vs stint 'Oughton, E. R' (exact)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1949, birth 1921 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 45 vs bar 60: 'asst. supt., police' ~ 'Senior Assistant Superintendent / Assistant Superintendent / Cadet'
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

