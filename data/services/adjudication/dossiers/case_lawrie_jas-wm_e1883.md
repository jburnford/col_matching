<!-- {"case_id": "case_lawrie_jas-wm_e1883", "bio_ids": ["lawrie_jas-wm_e1883"], "stint_ids": ["Lawrie, J. W___Straits Settlements___1888"]} -->
# Dossier case_lawrie_jas-wm_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lawrie_jas-wm_e1883`

- Printed name: **LAWRIE, JAS. WM**
- Birth year: not printed
- Appears in editions: [1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1905-L44441.v` — printed in editions [1905, 1906]:**

> LAWRIE, JAS. WM.—Asst. govt. engrnr. survr., Singapore, 12th June, 1883; resigned, 10th Oct., 1884; re-appointed asst. govt. marine survr., 26th Sept., 1887; govt. marine survr., Penang, 9th Mar., 1901.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Asst. govt. engrnr. survr. | Singapore | [1905, 1906] |
| 1 | 1884 | resigned | Singapore *(inherited from previous clause)* | [1905, 1906] |
| 2 | 1887 | re-appointed asst. govt. marine survr | Singapore *(inherited from previous clause)* | [1905, 1906] |
| 3 | 1901 | govt. marine survr., Penang | Singapore *(inherited from previous clause)* | [1905, 1906] |

## Candidate stint `Lawrie, J. W___Straits Settlements___1888`

- Staff-list name: **Lawrie, J. W** | colony: **Straits Settlements** | listed 1888–1905 | editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. W. Lawrie | Assistant Government Engineer Surveyor | Marine Department | — | — |
| 1889 | J. W. Lawrie | Assistant Government Engineer Surveyor | Marine Department | — | — |
| 1890 | J. W. Lawrie | Assistant Government Engineer Surveyor | Marine Department | — | — |
| 1894 | J. W. Lawrie | Assistant Government Marine Surveyor | Marine Department | — | — |
| 1896 | J. W. Lawrie | Assistant Government Marine Surveyor | Marine Department | — | — |
| 1897 | J. W. Lawrie | Assistant Government Marine Surveyor | Marine Department | — | — |
| 1898 | J. W. Lawrie | Assistant Government Marine Surveyor | Marine Department | — | — |
| 1899 | J. W. Lawrie | Assistant Government Marine Surveyor | Marine Department | — | — |
| 1905 | J. W. Lawrie | Government Marine Surveyor | Penang | — | — |

### Deterministic checks: `lawrie_jas-wm_e1883` vs `Lawrie, J. W___Straits Settlements___1888`

- [PASS] surname_gate: bio 'LAWRIE' vs stint 'Lawrie, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1905
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

