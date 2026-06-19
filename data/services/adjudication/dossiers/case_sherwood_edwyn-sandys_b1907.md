<!-- {"case_id": "case_sherwood_edwyn-sandys_b1907", "bio_ids": ["sherwood_edwyn-sandys_b1907"], "stint_ids": ["Sherwood, E. S___Nigeria___1933"]} -->
# Dossier case_sherwood_edwyn-sandys_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sherwood_edwyn-sandys_b1907`

- Printed name: **SHERWOOD, Edwyn Sandys**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951])
- Honours: C.P.M (1950)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35856.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SHERWOOD, Edwyn Sandys, C.P.M. (1950).—b. 1907; ed. Orley Farm Prep. Sch., Harrow, and Kings Sch., Worcester; on mil. serv., 1940-43; capt.; apptd. police, Nig., 1929; senr. supt., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | apptd. police | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1949 | senr. supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Sherwood, E. S___Nigeria___1933`

- Staff-list name: **Sherwood, E. S** | colony: **Nigeria** | listed 1933–1939 | editions [1933, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. S. Sherwood | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | E. S. Sherwood | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | E. S. Sherwood | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `sherwood_edwyn-sandys_b1907` vs `Sherwood, E. S___Nigeria___1933`

- [PASS] surname_gate: bio 'SHERWOOD' vs stint 'Sherwood, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1933, birth 1907 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1939
- [FAIL] position_sim: best 31 vs bar 60: 'apptd. police' ~ 'Commissioners and Assistant Commissioners'
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

