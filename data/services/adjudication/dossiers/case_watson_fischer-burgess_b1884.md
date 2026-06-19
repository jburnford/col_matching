<!-- {"case_id": "case_watson_fischer-burgess_b1884", "bio_ids": ["watson_fischer-burgess_b1884"], "stint_ids": ["Watson, F. Burges___Gibraltar___1927"]} -->
# Dossier case_watson_fischer-burgess_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 119 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `watson_fischer-burgess_b1884`

- Printed name: **WATSON, FISCHER BURGESS**
- Birth year: 1884 (attested in editions [1933, 1934])
- Honours: D.S.O (1917)
- Appears in editions: [1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1933-L64291.v` — printed in editions [1933, 1934]:**

> WATSON, COMMODORE FISCHER BURGESS, D.S.O. (1917), R.N.—B. 1884; ed. Ashdown House pte. schl. and H.M.S. "Britannia"; midshipman, 1900; sub-lieut., 1903; lieut., 1905; commdr., 1914; capt., 1921; naval asst. to 2nd sea lord, 1928-30; flag capt., H.M.S. "Nelson," 1930-31; commodore commdr., N.Z. station and naval adviser to N.Z. govt., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | midshipman | — | [1933, 1934] |
| 1 | 1903 | sub-lieut | — | [1933, 1934] |
| 2 | 1905 | lieut | — | [1933, 1934] |
| 3 | 1914 | commdr | — | [1933, 1934] |
| 4 | 1921 | capt | — | [1933, 1934] |
| 5 | 1928–1930 | naval asst. to 2nd sea lord | — | [1933, 1934] |
| 6 | 1930–1931 | flag capt., H.M.S. "Nelson," | — | [1933, 1934] |
| 7 | 1932 | commodore commdr., N.Z. station and naval adviser to N.Z. govt | New Zealand | [1933, 1934] |

## Candidate stint `Watson, F. Burges___Gibraltar___1927`

- Staff-list name: **Watson, F. Burges** | colony: **Gibraltar** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. Burges Watson | Chief Staff Officer | Chief Military and Naval Officers | D.S.O. | Captain |
| 1928 | F. Burges Watson | Chief Staff Officer | Chief Military and Naval Officers | D.S.O. | Captain |

### Deterministic checks: `watson_fischer-burgess_b1884` vs `Watson, F. Burges___Gibraltar___1927`

- [PASS] surname_gate: bio 'WATSON' vs stint 'Watson, F. Burges' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1927, birth 1884 (age 43)
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1928
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: D.S.O
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

