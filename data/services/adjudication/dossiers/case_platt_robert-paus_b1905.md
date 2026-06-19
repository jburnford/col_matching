<!-- {"case_id": "case_platt_robert-paus_b1905", "bio_ids": ["platt_robert-paus_b1905"], "stint_ids": ["Platt, R. P___Kenya___1936"]} -->
# Dossier case_platt_robert-paus_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `platt_robert-paus_b1905`

- Printed name: **PLATT, ROBERT PAUS**
- Birth year: 1905 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67626.v` — printed in editions [1940]:**

> PLATT, ROBERT PAUS, B.A. (Cantab.).—B. 1905; ed. Shrewsbury and Queens' Coll., Cambridge; cadet, Kenya, 1927; dist. offr., 1929; ag. ast. sec., 1935; seconded to C.O., Jan., 1938 to May, 1939; ast. civ. sec., Aden, June, 1939; ag. civ. sec., July to Sept., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet | Kenya | [1940] |
| 1 | 1929 | dist. offr | Kenya *(inherited from previous clause)* | [1940] |
| 2 | 1935 | ag. ast. sec | Kenya *(inherited from previous clause)* | [1940] |
| 3 | 1938–1939 | seconded to C.O | Kenya *(inherited from previous clause)* | [1940] |
| 4 | 1939 | ast. civ. sec. | Aden | [1940] |

## Candidate stint `Platt, R. P___Kenya___1936`

- Staff-list name: **Platt, R. P** | colony: **Kenya** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | R. P. Platt | Assistant Secretaries (seconded from Provincial Administration) | Secretariat | — | — |
| 1937 | R. P. Platt | Assistant Secretaries (seconded from Provincial Administration) | Secretariat | — | — |

### Deterministic checks: `platt_robert-paus_b1905` vs `Platt, R. P___Kenya___1936`

- [PASS] surname_gate: bio 'PLATT' vs stint 'Platt, R. P' (exact)
- [PASS] initials: bio ['R', 'P'] ~ stint ['R', 'P']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1936-1937
- [PASS] position_sim: best 73 vs bar 60: 'seconded to C.O' ~ 'Assistant Secretaries (seconded from Provincial Administration)'
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

