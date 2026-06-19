<!-- {"case_id": "case_buragiar_francisco_e1894", "bio_ids": ["buragiar_francisco_e1894"], "stint_ids": ["Buhagiar, F___Malta___1925", "Buhaqiar, F___Malta___1931"]} -->
# Dossier case_buragiar_francisco_e1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['buragiar_francisco_e1894'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Buhagiar, F___Malta___1925` is also gate-compatible with biography(ies) outside this case: ['buhagiar_francesco_e1894'] (already linked elsewhere or filtered).

## Biography `buragiar_francisco_e1894`

- Printed name: **BURAGIAR, FRANCISCO**
- Birth year: not printed
- Honours: LL.D (1901)
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L58341.v` — printed in editions [1933]:**

> BURAGIAR, HON. FRANCISCO, LL.D.(1901).—Ed., Malta Lyceum; matric., Malta Univ., 1894; called to bar, 1902; cl. to rep., 4th dist., first Maltese parl., Oct., 1921; min. of just., July, 1922; judge, Sept., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | matric., Malta Univ | Malta | [1933] |
| 1 | 1902 | called to bar | Malta *(inherited from previous clause)* | [1933] |
| 2 | 1921 | cl. to rep., 4th dist., first Maltese parl | Malta *(inherited from previous clause)* | [1933] |
| 3 | 1922 | min. of just | Malta *(inherited from previous clause)* | [1933] |
| 4 | 1924 | judge | Malta *(inherited from previous clause)* | [1933] |

## Candidate stint `Buhagiar, F___Malta___1925`

- Staff-list name: **Buhagiar, F** | colony: **Malta** | listed 1925–1930 | editions [1925, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | F. Buhagiar | Judge | Judicial Establishment | — | — |
| 1929 | F. Buhagiar | Judge | Judicial Establishment | — | — |
| 1930 | F. Buhagiar | Judge | Judicial Establishment | — | — |

### Deterministic checks: `buragiar_francisco_e1894` vs `Buhagiar, F___Malta___1925`

- [PASS] surname_gate: bio 'BURAGIAR' vs stint 'Buhagiar, F' (fuzzy:1)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1925; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1925-1930
- [PASS] position_sim: best 100 vs bar 60: 'judge' ~ 'Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Buhaqiar, F___Malta___1931`

- Staff-list name: **Buhaqiar, F** | colony: **Malta** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | F. Buhaqiar | Judge | Judicial Establishment | — | — |
| 1933 | F. Buhaqiar | Judge | Judicial Establishment | — | — |

### Deterministic checks: `buragiar_francisco_e1894` vs `Buhaqiar, F___Malta___1931`

- [PASS] surname_gate: bio 'BURAGIAR' vs stint 'Buhaqiar, F' (fuzzy:2)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1933
- [PASS] position_sim: best 100 vs bar 60: 'judge' ~ 'Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1933] pos~100 (bar: >=2)
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

