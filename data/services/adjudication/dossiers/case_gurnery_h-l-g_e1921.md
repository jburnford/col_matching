<!-- {"case_id": "case_gurnery_h-l-g_e1921", "bio_ids": ["gurnery_h-l-g_e1921", "gurney_h-l-g_e1921"], "stint_ids": ["Gurney, H. L. G___Kenya___1931"]} -->
# Dossier case_gurnery_h-l-g_e1921

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Gurney, H. L. G___Kenya___1931'] have more than one claimant biography in this case.
- NOTE: stint `Gurney, H. L. G___Kenya___1931` is also gate-compatible with biography(ies) outside this case: ['gurney_henry-lovell-goldsworthy_b1898'] (already linked elsewhere or filtered).
- NOTE: stint `Gurney, H. L. G___Kenya___1931` is also gate-compatible with biography(ies) outside this case: ['gurney_henry-lovell-goldsworthy_b1898'] (already linked elsewhere or filtered).

## Biography `gurnery_h-l-g_e1921`

- Printed name: **GURNERY, H. L. G**
- Birth year: not printed
- Appears in editions: [1927]

### Verbatim printed entry text (OCR)

**Version `col1927-L59480.v` — printed in editions [1927]:**

> GURNERY, H. L. G.—Asst. dist. commr., Kenya, June 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Asst. dist. commr. | Kenya | [1927] |

## Biography `gurney_h-l-g_e1921`

- Printed name: **GURNEY, H. L. G**
- Birth year: not printed
- Appears in editions: [1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1924-L54823.v` — printed in editions [1924, 1925]:**

> GURNEY, H. L. G.—Aast. dist. comntr., Kenya, June 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Aast. dist. comntr. | Kenya | [1924, 1925] |

## Candidate stint `Gurney, H. L. G___Kenya___1931`

- Staff-list name: **Gurney, H. L. G** | colony: **Kenya** | listed 1931–1940 | editions [1931, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. L. G. Gurney | Secretaries | Local Government, Lands and Settlement | — | — |
| 1934 | H. L. G. Gurney | Secretaries | Local Government, Lands, Settlement and Mines | — | — |
| 1937 | H. L. G. Gurney | Assistant Secretaries (seconded from Provincial Administration) | Secretariat | — | — |
| 1939 | H. L. G. Gurney | Assistant Secretary | Secretariat | — | — |
| 1940 | H. L. G. Gurney | Secretary | Executive Council | — | — |

### Deterministic checks: `gurnery_h-l-g_e1921` vs `Gurney, H. L. G___Kenya___1931`

- [PASS] surname_gate: bio 'GURNERY' vs stint 'Gurney, H. L. G' (fuzzy:1)
- [PASS] initials: bio ['H', 'L', 'G'] ~ stint ['H', 'L', 'G']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1940
- [FAIL] position_sim: best 47 vs bar 60: 'Asst. dist. commr.' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `gurney_h-l-g_e1921` vs `Gurney, H. L. G___Kenya___1931`

- [PASS] surname_gate: bio 'GURNEY' vs stint 'Gurney, H. L. G' (exact)
- [PASS] initials: bio ['H', 'L', 'G'] ~ stint ['H', 'L', 'G']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1940
- [FAIL] position_sim: best 46 vs bar 60: 'Aast. dist. comntr.' ~ 'Assistant Secretary'
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

