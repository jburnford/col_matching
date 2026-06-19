<!-- {"case_id": "case_russouw_j-w-h_e1882", "bio_ids": ["russouw_j-w-h_e1882"], "stint_ids": ["Russouw, J. W. H___Cape of Good Hope___1877", "Russouw, J. W. H___Cape of Good Hope___1890"]} -->
# Dossier case_russouw_j-w-h_e1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Russouw, J. W. H___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['russoow_w-h_e1882'] (already linked elsewhere or filtered).
- NOTE: stint `Russouw, J. W. H___Cape of Good Hope___1890` is also gate-compatible with biography(ies) outside this case: ['russoow_w-h_e1882'] (already linked elsewhere or filtered).

## Biography `russouw_j-w-h_e1882`

- Printed name: **RUSSOUW, J. W. H**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L35581.v` — printed in editions [1886]:**

> RUSSOUW, J. W. H.—Civil commissioner and resident magistrate, Piquetberg division, Cape of Good Hope, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Civil commissioner and resident magistrate, Piquetberg division | Cape of Good Hope | [1886] |

## Candidate stint `Russouw, J. W. H___Cape of Good Hope___1877`

- Staff-list name: **Russouw, J. W. H** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. W. H. Russouw | Clerk | Cape Town | — | — |
| 1878 | J. W. H. Russouw | Clerk | Civil and Judicial Establishments | — | — |
| 1879 | J. W. H. Russouw | Clerk | Divisional Courts and Offices | — | — |
| 1880 | J. W. H. Russouw | Clerk | CAPE TOWN | — | — |

### Deterministic checks: `russouw_j-w-h_e1882` vs `Russouw, J. W. H___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'RUSSOUW' vs stint 'Russouw, J. W. H' (exact)
- [PASS] initials: bio ['J', 'W', 'H'] ~ stint ['J', 'W', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Russouw, J. W. H___Cape of Good Hope___1890`

- Staff-list name: **Russouw, J. W. H** | colony: **Cape of Good Hope** | listed 1890–1896 | editions [1890, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | J. W. H. Russouw | C.C. and R.M. | Division of Piagetberg | — | — |
| 1896 | J. W. H. Russouw | R.M. | DIVISION OF MALMESBURY | — | — |

### Deterministic checks: `russouw_j-w-h_e1882` vs `Russouw, J. W. H___Cape of Good Hope___1890`

- [PASS] surname_gate: bio 'RUSSOUW' vs stint 'Russouw, J. W. H' (exact)
- [PASS] initials: bio ['J', 'W', 'H'] ~ stint ['J', 'W', 'H']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1896
- [FAIL] position_sim: best 50 vs bar 60: 'Civil commissioner and resident magistrate, Piquetberg division' ~ 'C.C. and R.M.'
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

