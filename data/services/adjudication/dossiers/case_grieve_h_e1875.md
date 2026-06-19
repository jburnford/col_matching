<!-- {"case_id": "case_grieve_h_e1875", "bio_ids": ["grieve_h_e1875"], "stint_ids": ["Grieve, M. H___Kenya___1932"]} -->
# Dossier case_grieve_h_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['grieve_h_e1875'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Grieve, M. H___Kenya___1932` is also gate-compatible with biography(ies) outside this case: ['grieve_michael-hope_b1904'] (already linked elsewhere or filtered).

## Biography `grieve_h_e1875`

- Printed name: **GRIEVE, H**
- Birth year: not printed
- Honours: C.M.G (1894), M.D
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L35236.v` — printed in editions [1900]:**

> GRIEVE, H., M.D., C.M.G. (1894).—Med. supt., lun. asyl., Berbice, Br. Guiana, Sept., 1875; ag. med. offir., immigr. dept., Aug., 1885; surg.-gen. of col., Oct., 1885; ret. 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Med. supt., lun. asyl., Berbice | British Guiana | [1900] |
| 1 | 1885 | ag. med. offir., immigr. dept | British Guiana *(inherited from previous clause)* | [1900] |
| 2 | 1894 | ret | British Guiana *(inherited from previous clause)* | [1900] |

## Candidate stint `Grieve, M. H___Kenya___1932`

- Staff-list name: **Grieve, M. H** | colony: **Kenya** | listed 1932–1940 | editions [1932, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | M. H. Grieve | Agricultural Officer | Sub-Division of Native Agriculture | — | — |
| 1934 | M. H. Grieve | Agricultural Officers | Sub-Division of Native Agriculture | — | — |
| 1937 | M. H. Grieve | Agricultural Officers | Sub-Division of Native Agriculture | — | — |
| 1939 | M. H. Grieve | Agricultural Officer | Agricultural Department | — | — |
| 1940 | M. H. Grieve | Agricultural Officers | Agricultural Department | — | — |

### Deterministic checks: `grieve_h_e1875` vs `Grieve, M. H___Kenya___1932`

- [PASS] surname_gate: bio 'GRIEVE' vs stint 'Grieve, M. H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['M', 'H']
- [PASS] age_gate: stint starts 1932; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1940
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

