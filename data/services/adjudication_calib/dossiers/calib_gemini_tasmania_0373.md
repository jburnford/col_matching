<!-- {"case_id": "calib_gemini_tasmania_0373", "bio_ids": ["douglas_a-c_e1869"], "stint_ids": ["Douglas, Adye___Tasmania___1877"]} -->
# Dossier calib_gemini_tasmania_0373

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 135 official(s) with this surname in the graph's staff lists; 27 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `douglas_a-c_e1869`

- Printed name: **DOUGLAS, A. C**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33114.v` — printed in editions [1886]:**

> DOUGLAS, A. C.—Postmaster and secretary to Post Office, Tasmania, 1 April, 1869.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Postmaster and secretary to Post Office | Tasmania | [1886] |

## Candidate stint `Douglas, Adye___Tasmania___1877`

- Staff-list name: **Douglas, Adye** | colony: **Tasmania** | listed 1877–1900 | editions [1877, 1878, 1879, 1880, 1888, 1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. C. Douglas | Secretary | Post Office | — | — |
| 1878 | A. C. Douglas | Secretary | Post Office | — | — |
| 1879 | A. C. Douglas | Secretary | Post Office | — | — |
| 1880 | A. C. Douglas | Secretary | Post Office | — | — |
| 1888 | A. C. Douglas | Postmaster and Secretary to Post Office | Post Office | — | — |
| 1894 | A. Douglas | Member | Legislative Council | — | — |
| 1894 | A. Douglas | Chief Secretary | Chief Secretary's Department | — | — |
| 1894 | A. Douglas | Chief Secretary | Cabinet | — | — |
| 1896 | A. Douglas | — | Legislative Council | — | — |
| 1896 | Adye Douglas | President | Legislative Council | — | — |
| 1897 | Adye Douglas | President | Legislative Council | — | — |
| 1897 | A. Douglas | — | Legislative Council | — | — |
| 1898 | A. Douglas | Member | Legislative Council | — | — |
| 1898 | Adye Douglas | President | Legislative Council | — | — |
| 1899 | A. Douglas | Member | Legislative Council | — | — |
| 1899 | Adye Douglas | President | Legislative Council | — | — |
| 1900 | Hon. Adye Douglas | President | Legislative Council | — | — |

### Deterministic checks: `douglas_a-c_e1869` vs `Douglas, Adye___Tasmania___1877`

- [PASS] surname_gate: bio 'DOUGLAS' vs stint 'Douglas, Adye' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1900
- [PASS] position_sim: best 100 vs bar 60: 'Postmaster and secretary to Post Office' ~ 'Postmaster and Secretary to Post Office'
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

