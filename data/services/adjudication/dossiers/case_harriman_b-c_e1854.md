<!-- {"case_id": "case_harriman_b-c_e1854", "bio_ids": ["harriman_b-c_e1854", "harriman_b-c_e1872"], "stint_ids": ["Harriman, B. C___Victoria___1877"]} -->
# Dossier case_harriman_b-c_e1854

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Harriman, B. C___Victoria___1877'] have more than one claimant biography in this case.
- Phase 1 found `harriman_b-c_e1854` ↔ `Harriman, B. C___Victoria___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `harriman_b-c_e1872` ↔ `Harriman, B. C___Victoria___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `harriman_b-c_e1854`

- Printed name: **HARRIMAN, B. C.**
- Birth year: not printed
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L33893.v` — printed in editions [1888, 1889]:**

> HARRIMAN, B. C.—Secretary to the Law Department, Victoria, 1st July, 1872, having acted as such under the designation of chief clerk from July, 1870; joined the civil service as clerk in police department, Sept., 1854; and promoted to law department 1st Aug., 1860.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854 | clerk | — | [1888, 1889] |
| 1 | 1860 | — | — | [1888, 1889] |
| 2 | 1870–1872 | chief clerk | — | [1888, 1889] |
| 3 | 1872 | Secretary to the Law Department | Victoria | [1888, 1889] |

## Biography `harriman_b-c_e1872`

- Printed name: **HARRIMAN, B. C**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33928.v` — printed in editions [1886]:**

> HARRIMAN, B. C.—Secretary to the Law Department, Victoria, 5 Aug., 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Secretary to the Law Department | Victoria | [1886] |

## Candidate stint `Harriman, B. C___Victoria___1877`

- Staff-list name: **Harriman, B. C** | colony: **Victoria** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | B. C. Harriman | Secretary to the Law Department | Crown Law Offices | — | — |
| 1879 | B. C. Harriman | Secretary to the Law Department | Crown Law Offices | — | — |
| 1880 | B. C. Harriman | Secretary to the Law Department | At Courts of Assize | — | — |
| 1883 | B. C. Harriman | Secretary to the Law Department | Crown Law Offices | — | — |

### Deterministic checks: `harriman_b-c_e1854` vs `Harriman, B. C___Victoria___1877`

- [PASS] surname_gate: bio 'HARRIMAN' vs stint 'Harriman, B. C' (exact)
- [PASS] initials: bio ['B', 'C'] ~ stint ['B', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'Secretary to the Law Department' ~ 'Secretary to the Law Department'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `harriman_b-c_e1872` vs `Harriman, B. C___Victoria___1877`

- [PASS] surname_gate: bio 'HARRIMAN' vs stint 'Harriman, B. C' (exact)
- [PASS] initials: bio ['B', 'C'] ~ stint ['B', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'Secretary to the Law Department' ~ 'Secretary to the Law Department'
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

