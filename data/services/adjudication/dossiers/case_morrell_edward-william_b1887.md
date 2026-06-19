<!-- {"case_id": "case_morrell_edward-william_b1887", "bio_ids": ["morrell_edward-william_b1887"], "stint_ids": ["Morrell, E. W___North Borneo___1920", "Morrell, E. W___North Borneo___1933"]} -->
# Dossier case_morrell_edward-william_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morrell_edward-william_b1887`

- Printed name: **MORRELL, EDWARD WILLIAM**
- Birth year: 1887 (attested in editions [1936])
- Appears in editions: [1936]

### Verbatim printed entry text (OCR)

**Version `col1936-L63193.v` — printed in editions [1936]:**

> MORRELL, EDWARD WILLIAM.—B. 1887; N. Borneo serv., Sept., 1909; mag., 1st cls., Oct., 1914; dist. offr., June, 1915; res., May, 1922; asst. govt. sec., Mar., 1924; ag. judge, high ct., Sept., 1932; O.A.G., Mar.-Sept., 1934; res., Sept., 1934; judge, high ct., Jan., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | N. Borneo serv | North Borneo | [1936] |
| 1 | 1914 | mag., 1st cls | North Borneo *(inherited from previous clause)* | [1936] |
| 2 | 1915 | dist. offr | North Borneo *(inherited from previous clause)* | [1936] |
| 3 | 1922 | res | North Borneo *(inherited from previous clause)* | [1936] |
| 4 | 1924 | asst. govt. sec | North Borneo *(inherited from previous clause)* | [1936] |
| 5 | 1932 | ag. judge, high ct | North Borneo *(inherited from previous clause)* | [1936] |
| 6 | 1934 | O.A.G., Mar.- | North Borneo *(inherited from previous clause)* | [1936] |
| 7 | 1935 | judge, high ct | North Borneo *(inherited from previous clause)* | [1936] |

## Candidate stint `Morrell, E. W___North Borneo___1920`

- Staff-list name: **Morrell, E. W** | colony: **North Borneo** | listed 1920–1929 | editions [1920, 1921, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | E. W. Morrell | District Officer | District Officers | — | — |
| 1921 | E. W. Morrell | — | District Officers | — | — |
| 1929 | E. W. Morrell | Resident, Kudat | Staff | — | — |

### Deterministic checks: `morrell_edward-william_b1887` vs `Morrell, E. W___North Borneo___1920`

- [PASS] surname_gate: bio 'MORRELL' vs stint 'Morrell, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1920, birth 1887 (age 33)
- [PASS] colony: 8 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1920-1929
- [PASS] position_sim: best 72 vs bar 60: 'dist. offr' ~ 'District Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Morrell, E. W___North Borneo___1933`

- Staff-list name: **Morrell, E. W** | colony: **North Borneo** | listed 1933–1936 | editions [1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. W. Morrell | Resident, Tawau | Staff | — | — |
| 1936 | E. W. Morrell | Resident, Sandakan | Civil Service | — | — |

### Deterministic checks: `morrell_edward-william_b1887` vs `Morrell, E. W___North Borneo___1933`

- [PASS] surname_gate: bio 'MORRELL' vs stint 'Morrell, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1933, birth 1887 (age 46)
- [PASS] colony: 8 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1933-1936
- [FAIL] position_sim: best 30 vs bar 60: 'asst. govt. sec' ~ 'Resident, Tawau'
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

