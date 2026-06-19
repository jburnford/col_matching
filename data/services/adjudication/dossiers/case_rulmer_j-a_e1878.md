<!-- {"case_id": "case_rulmer_j-a_e1878", "bio_ids": ["rulmer_j-a_e1878"], "stint_ids": ["Bulmer, J. A___Trinidad and Tobago___1899", "Bulmer, J. A___Trinidad___1886"]} -->
# Dossier case_rulmer_j-a_e1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bulmer, J. A___Trinidad and Tobago___1899` is also gate-compatible with biography(ies) outside this case: ['bulmer_j-a_e1878'] (already linked elsewhere or filtered).
- Phase 1 found `rulmer_j-a_e1878` ↔ `Bulmer, J. A___Trinidad___1886` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Bulmer, J. A___Trinidad___1886` is also gate-compatible with biography(ies) outside this case: ['bulmer_j-a_e1878'] (already linked elsewhere or filtered).

## Biography `rulmer_j-a_e1878`

- Printed name: **RULMER, J. A**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L34061.v` — printed in editions [1900]:**

> RULMER, J. A.—Postmr., Cyprus, 27 July, 1878; Postmr.-gen., Trinidad, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Postmr. | Cyprus | [1900] |
| 1 | 1883 | Postmr.-gen. | Trinidad | [1900] |

## Candidate stint `Bulmer, J. A___Trinidad and Tobago___1899`

- Staff-list name: **Bulmer, J. A** | colony: **Trinidad and Tobago** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1900 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |

### Deterministic checks: `rulmer_j-a_e1878` vs `Bulmer, J. A___Trinidad and Tobago___1899`

- [PASS] surname_gate: bio 'RULMER' vs stint 'Bulmer, J. A' (fuzzy:1)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bulmer, J. A___Trinidad___1886`

- Staff-list name: **Bulmer, J. A** | colony: **Trinidad** | listed 1886–1898 | editions [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1888 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1889 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1890 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1894 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1896 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1897 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |
| 1898 | J. A. Bulmer | Postmaster-General | Post Office Department | — | — |

### Deterministic checks: `rulmer_j-a_e1878` vs `Bulmer, J. A___Trinidad___1886`

- [PASS] surname_gate: bio 'RULMER' vs stint 'Bulmer, J. A' (fuzzy:1)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1898
- [PASS] position_sim: best 69 vs bar 60: 'Postmr.-gen.' ~ 'Postmaster-General'
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

