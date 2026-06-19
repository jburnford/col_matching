<!-- {"case_id": "case_adams_r-p_e1867", "bio_ids": ["adams_r-p_e1867", "adams_robert-patton_e1867"], "stint_ids": ["Adams, R. P___Tasmania___1878"]} -->
# Dossier case_adams_r-p_e1867

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 96 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Adams, R. P___Tasmania___1878'] have more than one claimant biography in this case.
- Phase 1 found `adams_r-p_e1867` ↔ `Adams, R. P___Tasmania___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `adams_robert-patton_e1867` ↔ `Adams, R. P___Tasmania___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `adams_r-p_e1867`

- Printed name: **ADAMS, R. P**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L31832.v` — printed in editions [1886]:**

> ADAMS, R. P.—Solicitor-general, Tasmania, 20 Dec., 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | Solicitor-general | Tasmania | [1886] |

## Biography `adams_robert-patton_e1867`

- Printed name: **ADAMS, ROBERT PATTON**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1888-L31740.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]:**

> ADAMS, ROBERT PATTON—Solicitor-general, Tasmania, 20 Dec., 1867; puisne judge 1889, formerly chairman of quarter sessions and commr., court of requests.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | Solicitor-general | Tasmania | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1889 | puisne judge | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Adams, R. P___Tasmania___1878`

- Staff-list name: **Adams, R. P** | colony: **Tasmania** | listed 1878–1898 | editions [1878, 1879, 1880, 1888, 1889, 1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | R. P. Adams | Solicitor-General | Judicial and Legal Departments | — | — |
| 1879 | R. P. Adams | Solicitor-General | Judicial and Legal Departments | — | — |
| 1880 | R. P. Adams | Solicitor-General | Judicial and Legal Departments | — | — |
| 1888 | R. P. Adams | Solicitor-General and Clerk of the Peace | Law Officers | — | — |
| 1889 | R. P. Adams | Puisne Judges | Judicial and Legal Departments | — | — |
| 1894 | R. P. Adams | Puisne Judge | Judicial and Legal Departments | — | — |
| 1896 | R. P. Adams | Puisne Judge | Judicial and Legal Departments | — | — |
| 1897 | R. P. Adams | Puisne Judge | Judicial and Legal Departments | — | — |
| 1898 | R. P. Adams | Puisne Judge | Judicial and Legal Departments | — | — |

### Deterministic checks: `adams_r-p_e1867` vs `Adams, R. P___Tasmania___1878`

- [PASS] surname_gate: bio 'ADAMS' vs stint 'Adams, R. P' (exact)
- [PASS] initials: bio ['R', 'P'] ~ stint ['R', 'P']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1898
- [PASS] position_sim: best 100 vs bar 60: 'Solicitor-general' ~ 'Solicitor-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `adams_robert-patton_e1867` vs `Adams, R. P___Tasmania___1878`

- [PASS] surname_gate: bio 'ADAMS' vs stint 'Adams, R. P' (exact)
- [PASS] initials: bio ['R', 'P'] ~ stint ['R', 'P']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1898
- [PASS] position_sim: best 100 vs bar 60: 'Solicitor-general' ~ 'Solicitor-General'
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

