<!-- {"case_id": "case_laschinger_edmund-herbert_b1874", "bio_ids": ["laschinger_edmund-herbert_b1874"], "stint_ids": ["Laschinger, Edmund Herbert___Canada___1905"]} -->
# Dossier case_laschinger_edmund-herbert_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `laschinger_edmund-herbert_b1874`

- Printed name: **LASCHINGER, EDMUND HERBERT**
- Birth year: 1874 (attested in editions [1910, 1911])
- Appears in editions: [1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1910-L47046.v` — printed in editions [1910, 1911]:**

> LASCHINGER, EDMUND HERBERT.—B. 1874; ent. civ. ser., Canada, 1896; asst. sec., P.O. dept., 1904; asst. dep. postmstr.-gen., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | ent. civ. ser. | Canada | [1910, 1911] |
| 1 | 1904 | asst. sec., P.O. dept | Canada *(inherited from previous clause)* | [1910, 1911] |
| 2 | 1907 | asst. dep. postmstr.-gen | Canada *(inherited from previous clause)* | [1910, 1911] |

## Candidate stint `Laschinger, Edmund Herbert___Canada___1905`

- Staff-list name: **Laschinger, Edmund Herbert** | colony: **Canada** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Edmund Herbert Laschinger | Chief Clerk, Assistant Secretary | Post Office Department | — | — |
| 1906 | Edmund Herbert Laschinger | Chief Clerk, Assistant Secretary | Post Office Department | — | — |
| 1907 | Edmund Herbert Laschinger | Chief Clerk, Assistant Secretary | Post Office Department | — | — |
| 1908 | Edmund Herbert Laschinger | Assistant Deputy Postmaster-General | Post Office Department | — | — |

### Deterministic checks: `laschinger_edmund-herbert_b1874` vs `Laschinger, Edmund Herbert___Canada___1905`

- [PASS] surname_gate: bio 'LASCHINGER' vs stint 'Laschinger, Edmund Herbert' (exact)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1905, birth 1874 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1905-1908
- [PASS] position_sim: best 74 vs bar 60: 'asst. dep. postmstr.-gen' ~ 'Assistant Deputy Postmaster-General'
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

