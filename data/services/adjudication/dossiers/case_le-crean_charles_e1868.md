<!-- {"case_id": "case_le-crean_charles_e1868", "bio_ids": ["le-crean_charles_e1868"], "stint_ids": ["Le Cren, C___Victoria___1877"]} -->
# Dossier case_le-crean_charles_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['le-crean_charles_e1868'] carry a single initial only — the namesake trap applies.
- Phase 1 found `le-crean_charles_e1868` ↔ `Le Cren, C___Victoria___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Le Cren, C___Victoria___1877` is also gate-compatible with biography(ies) outside this case: ['le-cren_charles_e1838'] (already linked elsewhere or filtered).

## Biography `le-crean_charles_e1868`

- Printed name: **LE CREAN, CHARLES**
- Birth year: not printed
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L34458.v` — printed in editions [1888, 1889]:**

> LE CREAN, CHARLES.—Secretary for public works, Victoria, Jan., 1878; also a member of the board of land and works; has held office under Victorian government since June, 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | has held office under Victorian government since | Victoria *(inherited from previous clause)* | [1888, 1889] |
| 1 | 1878 | Secretary for public works | Victoria | [1888, 1889] |

## Candidate stint `Le Cren, C___Victoria___1877`

- Staff-list name: **Le Cren, C** | colony: **Victoria** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. Le Cren | Secretary and Treasurer | Melbourne Sewers and Water Supply Branch | — | — |
| 1878 | C. Le Cren | Secretary and Treasurer | Melbourne Water Supply Branch | — | — |
| 1879 | C. Le Cren | Secretary | Department of Public Works | — | — |
| 1879 | C. Le Cren | Secretary and Treasurer | Melbourne Water Supply Branch | — | — |
| 1880 | C. Le Cren | Secretary | Department of Public Works | — | — |
| 1880 | C. Le Cren | Secretary and Treasurer | Melbourne Water Supply Branch | — | — |
| 1883 | C. Le Cren | Secretary | Department of Public Works | — | — |
| 1883 | C. Le Cren | Secretary and Treasurer | Melbourne Water Supply Branch | — | — |

### Deterministic checks: `le-crean_charles_e1868` vs `Le Cren, C___Victoria___1877`

- [PASS] surname_gate: bio 'LE CREAN' vs stint 'Le Cren, C' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'Secretary for public works' ~ 'Secretary'
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

