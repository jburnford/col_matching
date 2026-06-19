<!-- {"case_id": "case_leathes_francis-pallent_b1888", "bio_ids": ["leathes_francis-pallent_b1888"], "stint_ids": ["Leathes, F. P___Tanganyika___1921", "Leathes, F. P___Tanganyika___1933"]} -->
# Dossier case_leathes_francis-pallent_b1888

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `leathes_francis-pallent_b1888`

- Printed name: **LEATHES, FRANCIS PALLENT**
- Birth year: 1888 (attested in editions [1939, 1940])
- Honours: O.B.E (1939)
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68565.v` — printed in editions [1939, 1940]:**

> LEATHES, FRANCIS PALLENT, O.B.E. (1939).—B. 1888; S. African M. Pol., 1907-16; E.A. campaign, 1914-18; Tanganyika Territory pol., 1916; ast. supt., 1926; ag. dep. comntr., several occasions; dep. comntr., June, 1936; ag. comntr., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907–1916 | S. African M. Pol | — | [1939, 1940] |
| 1 | 1914–1918 | E.A. campaign | — | [1939, 1940] |
| 2 | 1916 | Tanganyika Territory pol | Tanganyika | [1939, 1940] |
| 3 | 1926 | ast. supt | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1936 | dep. comntr | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1938 | ag. comntr | Tanganyika *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Leathes, F. P___Tanganyika___1921`

- Staff-list name: **Leathes, F. P** | colony: **Tanganyika** | listed 1921–1925 | editions [1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | F. P. Leathes | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1922 | F. P. Leathes | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1923 | F. P. Leathes | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1924 | F. P. Leathes | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1925 | F. P. Leathes | Assistant District Superintendent | Police and Prisons Department | — | — |

### Deterministic checks: `leathes_francis-pallent_b1888` vs `Leathes, F. P___Tanganyika___1921`

- [PASS] surname_gate: bio 'LEATHES' vs stint 'Leathes, F. P' (exact)
- [PASS] initials: bio ['F', 'P'] ~ stint ['F', 'P']
- [PASS] age_gate: stint starts 1921, birth 1888 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1921-1925
- [FAIL] position_sim: best 39 vs bar 60: 'ast. supt' ~ 'Assistant District Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Leathes, F. P___Tanganyika___1933`

- Staff-list name: **Leathes, F. P** | colony: **Tanganyika** | listed 1933–1940 | editions [1933, 1934, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | F. P. Leathes | Superintendent | Police | — | — |
| 1934 | F. P. Leathes | Superintendents | Police | — | — |
| 1940 | F. P. Leathes | Deputy Commissioners | Police Department | — | — |

### Deterministic checks: `leathes_francis-pallent_b1888` vs `Leathes, F. P___Tanganyika___1933`

- [PASS] surname_gate: bio 'LEATHES' vs stint 'Leathes, F. P' (exact)
- [PASS] initials: bio ['F', 'P'] ~ stint ['F', 'P']
- [PASS] age_gate: stint starts 1933, birth 1888 (age 45)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1933-1940
- [PASS] position_sim: best 60 vs bar 60: 'dep. comntr' ~ 'Deputy Commissioners'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

