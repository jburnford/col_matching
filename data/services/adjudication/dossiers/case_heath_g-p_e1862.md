<!-- {"case_id": "case_heath_g-p_e1862", "bio_ids": ["heath_g-p_e1862", "heath_george-poynter_e1845"], "stint_ids": ["Heath, G. P___Queensland___1878", "Heath, G___Jamaica___1883"]} -->
# Dossier case_heath_g-p_e1862

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Heath, G. P___Queensland___1878', 'Heath, G___Jamaica___1883'] have more than one claimant biography in this case.
- NOTE: stint `Heath, G___Jamaica___1883` is also gate-compatible with biography(ies) outside this case: ['heath_w-g_e1897'] (already linked elsewhere or filtered).
- NOTE: stint `Heath, G___Jamaica___1883` is also gate-compatible with biography(ies) outside this case: ['heath_w-g_e1897'] (already linked elsewhere or filtered).

## Biography `heath_g-p_e1862`

- Printed name: **HEATH, G. P**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33986.v` — printed in editions [1886]:**

> HEATH, COMMANDER G. P., R.N.—Portmaster, Queensland, 13th Jan., 1862.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Portmaster | Queensland | [1886] |

## Biography `heath_george-poynter_e1845`

- Printed name: **HEATH, GEORGE POYNTER**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33959.v` — printed in editions [1888, 1889, 1890]:**

> HEATH, GEORGE POYNTER, Commander, R.N.—Educated at Cheltenham College; entered the navy as a cadet in 1845, and served in the Channel Squadron, on the south-east coast of South America; and employed in the survey of Torres Straits, N. Guinea, and of the coasts of Australia and New Zealand, marine surveyor of Queensland in 1860, and in 1862 postmaster of the colony, and member of the marine board, of which he became chairman in 1869.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1845 | cadet | — | [1888, 1889, 1890] |
| 1 | 1860 | marine surveyor | Queensland | [1888, 1889, 1890] |
| 2 | 1862 | postmaster and member of the marine board | Queensland | [1888, 1889, 1890] |
| 3 | 1869 | chairman | Queensland | [1888, 1889, 1890] |

## Candidate stint `Heath, G. P___Queensland___1878`

- Staff-list name: **Heath, G. P** | colony: **Queensland** | listed 1878–1890 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | G. P. Heath | Portmaster | Colonial Treasurer's Department | — | — |
| 1879 | Commander G. P. Heath, R.N. | Postmaster | Colonial Treasurer's Department | — | — |
| 1880 | Commander G. P. Heath | Postmaster | Colonial Treasurer's Department | — | — |
| 1883 | G. P. Heath | Postmaster | Colonial Treasurer's Department | — | — |
| 1886 | G. P. Heath | Portmaster | Colonial Treasurer's Department | — | — |
| 1888 | G. P. Heath | Postmaster | Colonial Treasurer's Department | — | — |
| 1889 | Commander G. P. Heath, R.N. | Portmaster | Colonial Treasurer's Department | — | — |
| 1890 | G. P. Heath | Portmaster, Commander | Colonial Treasurer's Department | — | — |

### Deterministic checks: `heath_g-p_e1862` vs `Heath, G. P___Queensland___1878`

- [PASS] surname_gate: bio 'HEATH' vs stint 'Heath, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `heath_george-poynter_e1845` vs `Heath, G. P___Queensland___1878`

- [PASS] surname_gate: bio 'HEATH' vs stint 'Heath, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1890
- [FAIL] position_sim: best 36 vs bar 60: 'chairman' ~ 'Portmaster, Commander'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Heath, G___Jamaica___1883`

- Staff-list name: **Heath, G** | colony: **Jamaica** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | G. Heath | 3rd Class Clerks | Department of the Director of Roads and Surveyor-General | — | — |
| 1886 | G. Heath | 3rd Class Clerks | Public Works | — | — |

### Deterministic checks: `heath_g-p_e1862` vs `Heath, G___Jamaica___1883`

- [PASS] surname_gate: bio 'HEATH' vs stint 'Heath, G' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `heath_george-poynter_e1845` vs `Heath, G___Jamaica___1883`

- [PASS] surname_gate: bio 'HEATH' vs stint 'Heath, G' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
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

