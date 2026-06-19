<!-- {"case_id": "case_stutterfield_abbrey-g_e1862", "bio_ids": ["stutterfield_abbrey-g_e1862"], "stint_ids": ["Butterfield, A. G___Bermuda___1877"]} -->
# Dossier case_stutterfield_abbrey-g_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `stutterfield_abbrey-g_e1862` ↔ `Butterfield, A. G___Bermuda___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Butterfield, A. G___Bermuda___1877` is also gate-compatible with biography(ies) outside this case: ['butterfield_aubrey-g_e1862'] (already linked elsewhere or filtered).

## Biography `stutterfield_abbrey-g_e1862`

- Printed name: **STUTTERFIELD, ABBREY G.**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L31126.v` — printed in editions [1897]:**

> STUTTERFIELD, ABBREY G.—Clerk in British Consul's office, New York, April, 1862; paid vice-consul, Key West, Florida, October, 1862 to 1868 as unpaid vice-consul to 1871; treasury clerk, Bermuda, 1871; colonial postmaster, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Clerk | New York | [1897] |
| 1 | 1862–1868 | paid vice-consul | Florida | [1897] |
| 2 | 1871 | treasury clerk | Bermuda | [1897] |
| 3 | 1880 | colonial postmaster | — | [1897] |
| 4 | ?–1871 | unpaid vice-consul | — | [1897] |

## Candidate stint `Butterfield, A. G___Bermuda___1877`

- Staff-list name: **Butterfield, A. G** | colony: **Bermuda** | listed 1877–1896 | editions [1877, 1878, 1879, 1880, 1883, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. G. Butterfield | Clerk, Treasury | Revenue Department | — | — |
| 1878 | A. G. Butterfield | Clerk, Treasury | Revenue Department | — | — |
| 1879 | A. G. Butterfield | Clerk, Treasury | Revenue Department | — | — |
| 1880 | A. G. Butterfield | Postmaster | General Post Office | — | — |
| 1883 | A. G. Butterfield | Colonial Postmaster | General Post Office | — | — |
| 1888 | A. G. Butterfield | Colonial Postmaster | General Post Office | — | — |
| 1889 | A. G. Butterfield | Colonial Postmaster | General Post Office | — | — |
| 1890 | A. G. Butterfield | Colonial Postmaster | General Post Office | — | — |
| 1894 | A. G. Butterfield | Colonial Postmaster | General Post Office | — | — |
| 1896 | A. G. Butterfield | Colonial Postmaster | General Post Office | — | — |

### Deterministic checks: `stutterfield_abbrey-g_e1862` vs `Butterfield, A. G___Bermuda___1877`

- [PASS] surname_gate: bio 'STUTTERFIELD' vs stint 'Butterfield, A. G' (fuzzy:2)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bermuda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1896
- [PASS] position_sim: best 100 vs bar 60: 'treasury clerk' ~ 'Clerk, Treasury'
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

