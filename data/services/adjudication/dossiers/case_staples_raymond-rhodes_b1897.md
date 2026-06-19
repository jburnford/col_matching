<!-- {"case_id": "case_staples_raymond-rhodes_b1897", "bio_ids": ["staples_raymond-rhodes_b1897"], "stint_ids": ["Staples, R. R___Tanganyika___1933"]} -->
# Dossier case_staples_raymond-rhodes_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `staples_raymond-rhodes_b1897`

- Printed name: **STAPLES, RAYMOND RHODES**
- Birth year: 1897 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70854.v` — printed in editions [1939, 1940]:**

> STAPLES, RAYMOND RHODES.—B. 1897; M.A.; dip. agr. (Cantab.); botanist, Union of S.A., 1922; agr. economist, Tanganyika Territory, 1929; ag. dep. dir., agr., 1930; res. offr. (pasture), vety. dept., 1931; botanist, 1935; ecological survey, Basutoland, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | botanist, Union of S.A | — | [1939, 1940] |
| 1 | 1929 | agr. economist, Tanganyika Territory | Tanganyika | [1939, 1940] |
| 2 | 1930 | ag. dep. dir., agr | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1931 | res. offr. (pasture), vety. dept | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1935 | botanist | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1937 | ecological survey | Basutoland | [1939, 1940] |

## Candidate stint `Staples, R. R___Tanganyika___1933`

- Staff-list name: **Staples, R. R** | colony: **Tanganyika** | listed 1933–1940 | editions [1933, 1934, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. R. Staples | Research Officer (Pastures) | Veterinary | — | — |
| 1934 | R. R. Staples | Research Officer (Pastures) | Veterinary | — | — |
| 1940 | R. R. Staples | Botanist | Veterinary | — | — |

### Deterministic checks: `staples_raymond-rhodes_b1897` vs `Staples, R. R___Tanganyika___1933`

- [PASS] surname_gate: bio 'STAPLES' vs stint 'Staples, R. R' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1933, birth 1897 (age 36)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1940
- [PASS] position_sim: best 100 vs bar 60: 'botanist' ~ 'Botanist'
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

