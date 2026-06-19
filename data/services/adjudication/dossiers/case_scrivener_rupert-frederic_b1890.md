<!-- {"case_id": "case_scrivener_rupert-frederic_b1890", "bio_ids": ["scrivener_rupert-frederic_b1890"], "stint_ids": ["Scrivener, R. F___Palestine___1921"]} -->
# Dossier case_scrivener_rupert-frederic_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Scrivener, R. F___Palestine___1921` is also gate-compatible with biography(ies) outside this case: ['scrivener_rupert-frederick_b1890'] (already linked elsewhere or filtered).

## Biography `scrivener_rupert-frederic_b1890`

- Printed name: **SCRIVENER, Rupert Frederic**
- Birth year: 1890 (attested in editions [1948])
- Honours: A.I.M.M, A.R.S.M, D.I.C
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L35770.v` — printed in editions [1948]:**

> SCRIVENER, Rupert Frederic, A.R.S.M., D.I.C., A.I.M.M.—b. 1890; ed. Prep. Sch., London, Heidelberg Coll., Germany and London Univ. Student of Inst. of Mining and Metallurgy; on mil. serv., 1914-20, maj.; asst. ch. engr., rlyws., Pal., 1920; engr., ways and wks., 1924; ch. engr., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | asst. ch. engr., rlyws. | Palestine | [1948] |
| 1 | 1924 | engr., ways and wks | Palestine *(inherited from previous clause)* | [1948] |
| 2 | 1931 | ch. engr | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Scrivener, R. F___Palestine___1921`

- Staff-list name: **Scrivener, R. F** | colony: **Palestine** | listed 1921–1940 | editions [1921, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | R. F. Scrivener | Assistant Chief Engineer | Palestine Railways | — | Major |
| 1923 | R. F. Scrivener | Assistant Chief Engineer | Palestine Railways | — | — |
| 1925 | R. F. Scrivener | Engineer, Ways and Works | Palestine Railways | — | — |
| 1927 | R. F. Scrivener | Engineer, Ways and Works | Palestine Railways | — | — |
| 1928 | R. F. Scrivener | Engineer, Ways and Works | Palestine Railways | — | — |
| 1929 | R. F. Scrivener | Engineer, Ways and Works | Palestine Railways | — | — |
| 1930 | R. F. Scrivener | Engineer, Ways and Works | Palestine Railways | — | — |
| 1931 | R. F. Scrivener | Engineer, Ways and Works | Palestine Railways | — | — |
| 1932 | R. F. Scrivener | Chief Engineer, Ways and Works | Palestine Railways | — | — |
| 1940 | R. F. Scrivener | Chief Engineer | Palestine Railways | — | — |

### Deterministic checks: `scrivener_rupert-frederic_b1890` vs `Scrivener, R. F___Palestine___1921`

- [PASS] surname_gate: bio 'SCRIVENER' vs stint 'Scrivener, R. F' (exact)
- [PASS] initials: bio ['R', 'F'] ~ stint ['R', 'F']
- [PASS] age_gate: stint starts 1921, birth 1890 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1921-1940
- [PASS] position_sim: best 85 vs bar 60: 'engr., ways and wks' ~ 'Engineer, Ways and Works'
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

