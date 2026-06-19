<!-- {"case_id": "case_rajendra_murugeswar_b1911", "bio_ids": ["rajendra_murugeswar_b1911"], "stint_ids": ["Rajendra, M___Ceylon___1936"]} -->
# Dossier case_rajendra_murugeswar_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rajendra_murugeswar_b1911'] carry a single initial only — the namesake trap applies.

## Biography `rajendra_murugeswar_b1911`

- Printed name: **RAJENDRA, MURUGESWAR**
- Birth year: 1911 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70009.v` — printed in editions [1939, 1940]:**

> RAJENDRA, MURUGESWAR, B.A. (hons.), Lond.—B. 1911; cadet, Ceylon civ. serv. Dec., 1934; office asst., Hambantota kach., Apr., 1935; att. office of dir., med. and sany. services, and ast. sec. to min. for health, June, 1936; do. and sec. to do., June, 1937; addnl. ast. govt. agt., Mebara and Hambantota, Oct., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | cadet, Ceylon civ. serv | Ceylon | [1939, 1940] |
| 1 | 1935 | office asst., Hambantota kach | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1936 | att. office of dir., med. and sany. services, and ast. sec. to min. for health | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1937 | do. and sec. to do | Dominions Office | [1939, 1940] |
| 4 | 1938 | addnl. ast. govt. agt., Mebara and Hambantota | Dominions Office *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Rajendra, M___Ceylon___1936`

- Staff-list name: **Rajendra, M** | colony: **Ceylon** | listed 1936–1940 | editions [1936, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | M. Rajendra | Office Assistant | Southern Province | — | — |
| 1940 | M. Rajendra | Additional Assistant Government Agent (Land) | Government Agencies | — | — |

### Deterministic checks: `rajendra_murugeswar_b1911` vs `Rajendra, M___Ceylon___1936`

- [PASS] surname_gate: bio 'RAJENDRA' vs stint 'Rajendra, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1936, birth 1911 (age 25)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 65 vs bar 60: 'office asst., Hambantota kach' ~ 'Office Assistant'
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

