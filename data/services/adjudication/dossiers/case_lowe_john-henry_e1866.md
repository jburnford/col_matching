<!-- {"case_id": "case_lowe_john-henry_e1866", "bio_ids": ["lowe_john-henry_e1866"], "stint_ids": ["Lowe, J. Henry___New Zealand___1890", "Lowe, John___Canada___1877"]} -->
# Dossier case_lowe_john-henry_e1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lowe_john-henry_e1866`

- Printed name: **LOWE, JOHN HENRY**
- Birth year: not printed
- Honours: M.I.C.E
- Appears in editions: [1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L40064.v` — printed in editions [1896, 1897, 1898, 1899, 1900]:**

> LOWE, JOHN HENRY, M.I.C.E.—Entered service of Nelson provinsl. govt., N.Z., as dist. engrnr. and survr. for goldfields, 1866; apptd. warden of Nelson goldfields; entered service of col. govt., N.Z., as asst. engrnr., 1872; res. engrnr.-in-charge of rlys. under construction, Otago, 1873; engrnr.-in-charge of rlys. open for traffic, Middle Island, 1877; ch. engrnr., N.Z. rlys. dept., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Entered service of Nelson provinsl. govt., N.Z., as dist. engrnr. and survr. for goldfields | — | [1896, 1897, 1898, 1899, 1900] |
| 1 | 1872 | entered service of col. govt., N.Z., as asst. engrnr | — | [1896, 1897, 1898, 1899, 1900] |
| 2 | 1873 | res. engrnr.-in-charge of rlys. under construction, Otago | — | [1896, 1897, 1898, 1899, 1900] |
| 3 | 1877 | engrnr.-in-charge of rlys. open for traffic, Middle Island | — | [1896, 1897, 1898, 1899, 1900] |
| 4 | 1887 | ch. engrnr., N.Z. rlys. dept | New Zealand | [1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Lowe, J. Henry___New Zealand___1890`

- Staff-list name: **Lowe, J. Henry** | colony: **New Zealand** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | J. Henry Lowe | Engineer | Working Railways Department | — | — |
| 1894 | J. Henry Lowe | Engineer | Working Railways Department | — | — |

### Deterministic checks: `lowe_john-henry_e1866` vs `Lowe, J. Henry___New Zealand___1890`

- [PASS] surname_gate: bio 'LOWE' vs stint 'Lowe, J. Henry' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1894
- [FAIL] position_sim: best 33 vs bar 60: 'ch. engrnr., N.Z. rlys. dept' ~ 'Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Lowe, John___Canada___1877`

- Staff-list name: **Lowe, John** | colony: **Canada** | listed 1877–1894 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John Lowe | Secretary | Bureau of Agriculture and Statistics | — | — |
| 1878 | John Lowe | Secretary | Bureau of Agriculture and Statistics | — | — |
| 1879 | John Lowe | Secretary | Bureau of Agriculture and Statistics | — | — |
| 1880 | John Lowe | Secretary | Bureau of Agriculture and Statistics | — | — |
| 1883 | John Lowe | Secretary | Bureau of Agriculture and Statistics | — | — |
| 1886 | John Lowe | Secretary | Bureau of Agriculture and Statistics | — | — |
| 1888 | John Lowe | Secretary | Bureau of Agriculture and Statistics | — | — |
| 1889 | John Lowe | Deputy | Bureau of Agriculture and Statistics | — | — |
| 1890 | John Lowe | Deputy | Bureau of Agriculture and Statistics | — | — |
| 1894 | John Lowe | Deputy | Department of Agriculture and Statistics | — | — |

### Deterministic checks: `lowe_john-henry_e1866` vs `Lowe, John___Canada___1877`

- [PASS] surname_gate: bio 'LOWE' vs stint 'Lowe, John' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1894
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

