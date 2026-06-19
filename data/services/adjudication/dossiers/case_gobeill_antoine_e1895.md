<!-- {"case_id": "case_gobeill_antoine_e1895", "bio_ids": ["gobeill_antoine_e1895"], "stint_ids": ["Gobeil, A___Canada___1886"]} -->
# Dossier case_gobeill_antoine_e1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gobeill_antoine_e1895'] carry a single initial only — the namesake trap applies.
- Phase 1 found `gobeill_antoine_e1895` ↔ `Gobeil, A___Canada___1886` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Gobeil, A___Canada___1886` is also gate-compatible with biography(ies) outside this case: ['gobeil_antoine_e1879'] (already linked elsewhere or filtered).

## Biography `gobeill_antoine_e1895`

- Printed name: **GOBEILL, ANTOINE**
- Birth year: not printed
- Appears in editions: [1896]

### Verbatim printed entry text (OCR)

**Version `col1896-L39084.v` — printed in editions [1896]:**

> GOBEILL, ANTOINE.—Secretary, department of public works, Canada, Jan., 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | Secretary, department of public works | Canada | [1896] |

## Candidate stint `Gobeil, A___Canada___1886`

- Staff-list name: **Gobeil, A** | colony: **Canada** | listed 1886–1908 | editions [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | A. Gobeil | Secretary | Public Works | — | — |
| 1888 | A. Gobeil | Secretary | Public Works | — | — |
| 1889 | A. Gobeil | Secretary | Department of Public Works | — | — |
| 1890 | A. Gobeil | Secretary | Department of Public Works | — | — |
| 1894 | A. Gobeil | Deputy 'do. | Public Works | — | — |
| 1896 | A. Gobeil | Deputy do. | DEPARTMENT OF PUBLIC WORKS | — | — |
| 1896 | A. Gobeil | Deputy | Public Works | — | — |
| 1897 | A. Gobeil | Deputy Minister | Public Works | — | — |
| 1898 | A. Gobeil | Deputy do. | Public Works | — | — |
| 1899 | A. Gobeil | Deputy do. | Department of Public Works | — | — |
| 1900 | A. Gobeil | Deputy do. | Public Works | — | — |
| 1905 | A. Gobeil | Deputy Minister of Public Works | Public Works | — | — |
| 1906 | A. Gobeil | Deputy Minister of Public Works | Public Works | — | — |
| 1907 | A. Gobeil | Deputy Minister of Public Works | Public Works | — | — |
| 1908 | A. Gobeil | Deputy Minister of Public Works | Public Works | — | — |

### Deterministic checks: `gobeill_antoine_e1895` vs `Gobeil, A___Canada___1886`

- [PASS] surname_gate: bio 'GOBEILL' vs stint 'Gobeil, A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1908
- [PASS] position_sim: best 100 vs bar 60: 'Secretary, department of public works' ~ 'Secretary'
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

