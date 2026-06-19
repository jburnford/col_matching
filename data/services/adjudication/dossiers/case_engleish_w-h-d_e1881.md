<!-- {"case_id": "case_engleish_w-h-d_e1881", "bio_ids": ["engleish_w-h-d_e1881", "english_w-h-d_e1881"], "stint_ids": ["English, W. H. D___Cape of Good Hope___1877"]} -->
# Dossier case_engleish_w-h-d_e1881

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['English, W. H. D___Cape of Good Hope___1877'] have more than one claimant biography in this case.

## Biography `engleish_w-h-d_e1881`

- Printed name: **ENGLEISH, W. H. D**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L31422.v` — printed in editions [1894]:**

> ENGLEISH, W. H. D.—C.C. and resident magistrate, Robertson division, Cape Colony, 1st April, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | C.C. and resident magistrate, Robertson division | Cape of Good Hope | [1894] |

## Biography `english_w-h-d_e1881`

- Printed name: **ENGLISH, W. H. D**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L33261.v` — printed in editions [1886, 1888, 1889, 1890]:**

> ENGLISH, W. H. D.—C.C. and resident magistrate, Robertson division, Cape Colony, 1st April, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | C.C. and resident magistrate, Robertson division | Cape of Good Hope | [1886, 1888, 1889, 1890] |

## Candidate stint `English, W. H. D___Cape of Good Hope___1877`

- Staff-list name: **English, W. H. D** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. H. English | Clerk | Police Branch | — | — |
| 1878 | W. H. D. English | Clerk | DIVISION OF HUMANSDORP | — | — |
| 1880 | W. H. D. English | Clerk | DIVISION OF HUMANSDORP | — | — |

### Deterministic checks: `engleish_w-h-d_e1881` vs `English, W. H. D___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'ENGLEISH' vs stint 'English, W. H. D' (fuzzy:1)
- [PASS] initials: bio ['W', 'H', 'D'] ~ stint ['W', 'H', 'D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 12 vs bar 60: 'C.C. and resident magistrate, Robertson division' ~ 'Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `english_w-h-d_e1881` vs `English, W. H. D___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'ENGLISH' vs stint 'English, W. H. D' (exact)
- [PASS] initials: bio ['W', 'H', 'D'] ~ stint ['W', 'H', 'D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 12 vs bar 60: 'C.C. and resident magistrate, Robertson division' ~ 'Clerk'
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

