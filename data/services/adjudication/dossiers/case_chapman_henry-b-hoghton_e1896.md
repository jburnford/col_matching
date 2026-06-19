<!-- {"case_id": "case_chapman_henry-b-hoghton_e1896", "bio_ids": ["chapman_henry-b-hoghton_e1896"], "stint_ids": ["Chapman, H. B. H___Lagos___1897", "Chapman, H___New South Wales___1877", "Chapman, H___New South Wales___1899"]} -->
# Dossier case_chapman_henry-b-hoghton_e1896

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Chapman, H___New South Wales___1877` is also gate-compatible with biography(ies) outside this case: ['chapman_george-h_e1865'] (already linked elsewhere or filtered).
- NOTE: stint `Chapman, H___New South Wales___1899` is also gate-compatible with biography(ies) outside this case: ['chapman_george-h_e1865', 'chapman_thos-howard_b1866'] (already linked elsewhere or filtered).

## Biography `chapman_henry-b-hoghton_e1896`

- Printed name: **CHAPMAN, HENRY B. HOGHTON**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L34228.v` — printed in editions [1900]:**

> CHAPMAN, HENRY B. HOGHTON.—Dir. of P.W., Lagos, Dec., 1896; sent on special service to report on water supply of Sierra Leone, Jan., 1898.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | Dir. of P.W. | Lagos | [1900] |
| 1 | 1898 | sent on special service to report on water supply of Sierra Leone | Lagos *(inherited from previous clause)* | [1900] |

## Candidate stint `Chapman, H. B. H___Lagos___1897`

- Staff-list name: **Chapman, H. B. H** | colony: **Lagos** | listed 1897–1899 | editions [1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | H. B. H. Chapman | Director | Public Works Department | — | — |
| 1898 | H. B. H. Chapman | Director | Public Works Department | — | — |
| 1899 | H. B. H. Chapman | Director | Public Works Department | — | — |

### Deterministic checks: `chapman_henry-b-hoghton_e1896` vs `Chapman, H. B. H___Lagos___1897`

- [PASS] surname_gate: bio 'CHAPMAN' vs stint 'Chapman, H. B. H' (exact)
- [PASS] initials: bio ['H', 'B', 'H'] ~ stint ['H', 'B', 'H']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Lagos'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1897-1899
- [FAIL] position_sim: best 47 vs bar 60: 'Dir. of P.W.' ~ 'Director'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Chapman, H___New South Wales___1877`

- Staff-list name: **Chapman, H** | colony: **New South Wales** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. Chapman | Chief Clerk | Colonial Architect's Department | — | — |
| 1878 | H. Chapman | Chief Clerk | Colonial Architect's Department | — | — |
| 1879 | H. Chapman | Chief Clerk | Colonial Architect's Department | — | — |

### Deterministic checks: `chapman_henry-b-hoghton_e1896` vs `Chapman, H___New South Wales___1877`

- [PASS] surname_gate: bio 'CHAPMAN' vs stint 'Chapman, H' (exact)
- [PASS] initials: bio ['H', 'B', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Chapman, H___New South Wales___1899`

- Staff-list name: **Chapman, H** | colony: **New South Wales** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | H. Chapman | Members of Board | Metropolitan Board of Water Supply and Sewerage | — | — |
| 1900 | H. Chapman | Members of Board | Metropolitan Board of Water Supply and Sewerage | — | — |

### Deterministic checks: `chapman_henry-b-hoghton_e1896` vs `Chapman, H___New South Wales___1899`

- [PASS] surname_gate: bio 'CHAPMAN' vs stint 'Chapman, H' (exact)
- [PASS] initials: bio ['H', 'B', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
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

