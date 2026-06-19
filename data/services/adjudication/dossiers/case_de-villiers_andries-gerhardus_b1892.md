<!-- {"case_id": "case_de-villiers_andries-gerhardus_b1892", "bio_ids": ["de-villiers_andries-gerhardus_b1892"], "stint_ids": ["de Villiers, A. G___Tanganyika___1922"]} -->
# Dossier case_de-villiers_andries-gerhardus_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-villiers_andries-gerhardus_b1892`

- Printed name: **DE VILLIERS, ANDRIES GERHARDUS**
- Birth year: 1892 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L66100.v` — printed in editions [1939, 1940]:**

> DE VILLIERS, ANDRIES GERHARDUS.—B. 1892; ed. Boys' High Schl., Paarl, S. Africa; army, S.A.M.R., 1913-19; Tanganyika Territory pol., 1919; astt. supl., 1926; supl., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1919 | army, S.A.M.R | — | [1939, 1940] |
| 1 | 1919 | Tanganyika Territory pol | Tanganyika | [1939, 1940] |
| 2 | 1926 | astt. supl | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1934 | supl | Tanganyika *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `de Villiers, A. G___Tanganyika___1922`

- Staff-list name: **de Villiers, A. G** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. G. de Villiers | Assistant Inspector | Police and Prisons Department | — | — |
| 1923 | A. G. de Villiers | Assistant Inspector | Police and Prisons Department | — | — |
| 1924 | A. G. de Villiers | Assistant Inspector | Police and Prisons Department | — | — |
| 1925 | A. G. de Villiers | Inspector | Police and Prisons Department | — | — |

### Deterministic checks: `de-villiers_andries-gerhardus_b1892` vs `de Villiers, A. G___Tanganyika___1922`

- [PASS] surname_gate: bio 'DE VILLIERS' vs stint 'de Villiers, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1922, birth 1892 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 50 vs bar 60: 'astt. supl' ~ 'Assistant Inspector'
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

