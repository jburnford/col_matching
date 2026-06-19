<!-- {"case_id": "case_evans_richard-francis_b1901", "bio_ids": ["evans_richard-francis_b1901"], "stint_ids": ["Evans, R. F___North Borneo___1933"]} -->
# Dossier case_evans_richard-francis_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 143 official(s) with this surname in the graph's staff lists; 63 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Evans, R. F___North Borneo___1933` is also gate-compatible with biography(ies) outside this case: ['evans_frederick_b1849'] (already linked elsewhere or filtered).

## Biography `evans_richard-francis_b1901`

- Printed name: **EVANS, RICHARD FRANCIS**
- Birth year: 1901 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64100.v` — printed in editions [1940]:**

> EVANS, RICHARD FRANCIS.—B. 1901; cadet, N. Borneo, Jan., 1921; ast. dist. offr., Jan., 1923; dist. offr., Sept., 1925; mag., 1st cls., Mar., 1931; ag. res., Feb., 1935; addl. sess. judge, Jan., 1936; offr., mem., leg. coun., Jan., 1937; res., July, 1937; judge, high ct., May, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cadet | North Borneo | [1940] |
| 1 | 1923 | ast. dist. offr | North Borneo *(inherited from previous clause)* | [1940] |
| 2 | 1925 | dist. offr | North Borneo *(inherited from previous clause)* | [1940] |
| 3 | 1931 | mag., 1st cls | North Borneo *(inherited from previous clause)* | [1940] |
| 4 | 1935 | ag. res | North Borneo *(inherited from previous clause)* | [1940] |
| 5 | 1936 | addl. sess. judge | North Borneo *(inherited from previous clause)* | [1940] |
| 6 | 1937 | offr., mem., leg. coun | North Borneo *(inherited from previous clause)* | [1940] |
| 7 | 1938 | judge, high ct | North Borneo *(inherited from previous clause)* | [1940] |

## Candidate stint `Evans, R. F___North Borneo___1933`

- Staff-list name: **Evans, R. F** | colony: **North Borneo** | listed 1933–1940 | editions [1933, 1936, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. F. Evans | District Officer | District Officers | — | — |
| 1936 | R. F. Evans | Resident, Interior (acting) | Civil Service | — | — |
| 1936 | R. F. Evans | District Officer | District Officers | — | — |
| 1940 | R. F. Evans | Resident, West Coast | Civil Service | — | — |

### Deterministic checks: `evans_richard-francis_b1901` vs `Evans, R. F___North Borneo___1933`

- [PASS] surname_gate: bio 'EVANS' vs stint 'Evans, R. F' (exact)
- [PASS] initials: bio ['R', 'F'] ~ stint ['R', 'F']
- [PASS] age_gate: stint starts 1933, birth 1901 (age 32)
- [PASS] colony: 8 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1933-1940
- [FAIL] position_sim: best 41 vs bar 60: 'addl. sess. judge' ~ 'Resident, West Coast'
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

