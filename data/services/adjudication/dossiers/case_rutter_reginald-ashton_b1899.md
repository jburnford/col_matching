<!-- {"case_id": "case_rutter_reginald-ashton_b1899", "bio_ids": ["rutter_reginald-ashton_b1899"], "stint_ids": ["Rutter, R. A___North Borneo___1933"]} -->
# Dossier case_rutter_reginald-ashton_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rutter_reginald-ashton_b1899`

- Printed name: **RUTTER, REGINALD ASHTON**
- Birth year: 1899 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70365.v` — printed in editions [1939, 1940]:**

> RUTTER, REGINALD ASHTON.—B. 1899; cadet, N. Borneo, Oct., 1920; asst. dist. offr., July, 1923; dist. offr., Oct., 1926; mag., lat. cls., Oct., 1930; addl. sess. judge, July, 1936; ag. res., offl. mem., leg. coun. and ag. judge, high ct., Oct., 1937; judge, high ct., July, 1938; res., Aug., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | cadet | North Borneo | [1939, 1940] |
| 1 | 1923 | asst. dist. offr | North Borneo *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1926 | dist. offr | North Borneo *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1930 | mag., lat. cls | North Borneo *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1936 | addl. sess. judge | North Borneo *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1937 | ag. res., offl. mem., leg. coun. and ag. judge, high ct | North Borneo *(inherited from previous clause)* | [1939, 1940] |
| 6 | 1938 | judge, high ct | North Borneo *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Rutter, R. A___North Borneo___1933`

- Staff-list name: **Rutter, R. A** | colony: **North Borneo** | listed 1933–1940 | editions [1933, 1936, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. A. Rutter | District Officer | District Officers | — | — |
| 1936 | R. A. Rutter | Deputy Protector and Assistant Secretary for Chinese Affairs | Other Officers | — | — |
| 1936 | R. A. Rutter | District Officer | District Officers | — | — |
| 1940 | R. A. Rutter | Resident, East Coast | Civil Service | — | — |

### Deterministic checks: `rutter_reginald-ashton_b1899` vs `Rutter, R. A___North Borneo___1933`

- [PASS] surname_gate: bio 'RUTTER' vs stint 'Rutter, R. A' (exact)
- [PASS] initials: bio ['R', 'A'] ~ stint ['R', 'A']
- [PASS] age_gate: stint starts 1933, birth 1899 (age 34)
- [PASS] colony: 7 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1933-1940
- [FAIL] position_sim: best 41 vs bar 60: 'ag. res., offl. mem., leg. coun. and ag. judge, high ct' ~ 'Deputy Protector and Assistant Secretary for Chinese Affairs'
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

