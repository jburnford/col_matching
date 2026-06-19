<!-- {"case_id": "case_mcnaughtan_f_b1905", "bio_ids": ["mcnaughtan_f_b1905"], "stint_ids": ["McNaughtan, F___Kenya___1939"]} -->
# Dossier case_mcnaughtan_f_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcnaughtan_f_b1905'] carry a single initial only — the namesake trap applies.

## Biography `mcnaughtan_f_b1905`

- Printed name: **McNAUGHTAN, F**
- Birth year: 1905 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L25399.v` — printed in editions [1957]:**

> McNAUGHTAN, F.—b. 1905; ed. Edin. Univ.; junr. lab. asst., agric. dept., Ken., 1929; asst. govt. chmst., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | junr. lab. asst., agric. dept. | Kenya | [1957] |
| 1 | 1946 | asst. govt. chmst | Kenya *(inherited from previous clause)* | [1957] |

## Candidate stint `McNaughtan, F___Kenya___1939`

- Staff-list name: **McNaughtan, F** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | F. McNaughtan | Agricultural Chemist (Pyrethrum) | Agricultural Department | — | — |
| 1940 | F. McNaughtan | Agricultural Chemist (Pyrethrum) | Agricultural Department | — | — |

### Deterministic checks: `mcnaughtan_f_b1905` vs `McNaughtan, F___Kenya___1939`

- [PASS] surname_gate: bio 'McNAUGHTAN' vs stint 'McNaughtan, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1939, birth 1905 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 44 vs bar 60: 'junr. lab. asst., agric. dept.' ~ 'Agricultural Chemist (Pyrethrum)'
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

