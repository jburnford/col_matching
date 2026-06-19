<!-- {"case_id": "case_kitching_j_b1900", "bio_ids": ["kitching_j_b1900"], "stint_ids": ["Kitching, J___Ceylon___1931"]} -->
# Dossier case_kitching_j_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['kitching_j_b1900'] carry a single initial only — the namesake trap applies.

## Biography `kitching_j_b1900`

- Printed name: **KITCHING, J**
- Birth year: 1900 (attested in editions [1957, 1958])
- Honours: M.B.E (1942)
- Appears in editions: [1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1957-L24755.v` — printed in editions [1957, 1958]:**

> KITCHING, J., M.B.E. (1942)—b. 1900; ed. Shrewsbury Sch. and Edin. Univ.; irrig. dept., Ceylon, 1929-48; agric. dept., Nig., 1949; prin. irrig. engrnr., 1951 (N. Nig.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929–1948 | irrig. dept. | Ceylon | [1957, 1958] |
| 1 | 1949 | agric. dept. | Nigeria | [1957, 1958] |
| 2 | 1951 | prin. irrig. engrnr | Nigeria *(inherited from previous clause)* | [1957, 1958] |

## Candidate stint `Kitching, J___Ceylon___1931`

- Staff-list name: **Kitching, J** | colony: **Ceylon** | listed 1931–1940 | editions [1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. Kitching | Temporary Irrigation Engineer | Irrigation Department | — | — |
| 1934 | J. Kitching | Irrigation Engineer | Irrigation Department | — | — |
| 1936 | J. Kitching | Irrigation Engineer | Irrigation Department | — | — |
| 1937 | J. Kitching | Irrigation Engineer | Irrigation Department | — | — |
| 1940 | J. Kitching | Irrigation Engineer | Irrigation Department | — | — |

### Deterministic checks: `kitching_j_b1900` vs `Kitching, J___Ceylon___1931`

- [PASS] surname_gate: bio 'KITCHING' vs stint 'Kitching, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1931, birth 1900 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1940
- [FAIL] position_sim: best 48 vs bar 60: 'irrig. dept.' ~ 'Irrigation Engineer'
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

