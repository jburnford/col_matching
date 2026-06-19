<!-- {"case_id": "case_mccaithy_robt-henry_e1875", "bio_ids": ["mccaithy_robt-henry_e1875"], "stint_ids": ["McCarthy, R. H___Trinidad and Tobago___1899", "McCarthy, R. H___Trinidad___1897"]} -->
# Dossier case_mccaithy_robt-henry_e1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `McCarthy, R. H___Trinidad and Tobago___1899` is also gate-compatible with biography(ies) outside this case: ['mccarthy_robt-henry_e1875'] (already linked elsewhere or filtered).
- Phase 1 found `mccaithy_robt-henry_e1875` ↔ `McCarthy, R. H___Trinidad___1897` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `McCarthy, R. H___Trinidad___1897` is also gate-compatible with biography(ies) outside this case: ['mccarthy_robt-henry_e1875'] (already linked elsewhere or filtered).

## Biography `mccaithy_robt-henry_e1875`

- Printed name: **MCCAITHY, ROBT. HENRY**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L36033.v` — printed in editions [1900]:**

> MCCAITHY, ROBT. HENRY.—2nd-class clk., impl. customs, Belfast, Feb., 1875; served at Cork and Plymouth; selected for special service with survrs.-gen., and in connection with reorganization of customs statistical dept., 1895; 2nd offr., Folkestone, 1894; collr. of customs, Trinidad, Dec., 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | 2nd-class clk., impl. customs, Belfast | — | [1900] |
| 1 | 1894 | 2nd offr., Folkestone | — | [1900] |
| 2 | 1895 | selected for special service with survrs.-gen., and in connection with reorganization of customs statistical dept | Trinidad | [1900] |

## Candidate stint `McCarthy, R. H___Trinidad and Tobago___1899`

- Staff-list name: **McCarthy, R. H** | colony: **Trinidad and Tobago** | listed 1899–1907 | editions [1899, 1900, 1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | R. H. McCarthy | Collector of Customs | Customs Department | — | — |
| 1900 | R. H. McCarthy | Collector of Customs | Customs Department | — | — |
| 1905 | R. H. McCarthy | Collector of Customs | Customs Department | — | — |
| 1906 | R. H. McCarthy | Collector of Customs | Customs Department | — | — |
| 1907 | R. H. McCarthy | Collector of Customs | Customs Department | C.M.G. | — |

### Deterministic checks: `mccaithy_robt-henry_e1875` vs `McCarthy, R. H___Trinidad and Tobago___1899`

- [PASS] surname_gate: bio 'MCCAITHY' vs stint 'McCarthy, R. H' (fuzzy:1)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McCarthy, R. H___Trinidad___1897`

- Staff-list name: **McCarthy, R. H** | colony: **Trinidad** | listed 1897–1898 | editions [1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | R. H. McCarthy | Collector of Customs | Customs Department | — | — |
| 1898 | R. H. McCarthy | Collector of Customs | Customs Department | — | — |

### Deterministic checks: `mccaithy_robt-henry_e1875` vs `McCarthy, R. H___Trinidad___1897`

- [PASS] surname_gate: bio 'MCCAITHY' vs stint 'McCarthy, R. H' (fuzzy:1)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1897-1898
- [PASS] position_sim: best 67 vs bar 60: 'selected for special service with survrs.-gen., and in connection with reorganization of customs statistical dept' ~ 'Collector of Customs'
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

