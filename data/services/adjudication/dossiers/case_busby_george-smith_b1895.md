<!-- {"case_id": "case_busby_george-smith_b1895", "bio_ids": ["busby_george-smith_b1895"], "stint_ids": ["Busby, G. S___British Honduras___1924"]} -->
# Dossier case_busby_george-smith_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `busby_george-smith_b1895`

- Printed name: **BUSBY, George Smith**
- Birth year: 1895 (attested in editions [1948, 1949, 1950, 1951])
- Honours: F.S.I
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31540.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BUSBY, George Smith, F.S.I.—b. 1895; on mil. serv. 1914-18, lieut.; R.A.R.O., 1922-37; ord. survey dept., 1912; land survr., Br. Hond., 1922; dep. dir. surv. and dep. sub-intendant cr. lands., Trin., 1943; dir. and sub-intendant, 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | ord. survey dept | — | [1948, 1949, 1950, 1951] |
| 1 | 1922–1937 | R.A.R.O | — | [1948, 1949, 1950, 1951] |
| 2 | 1922 | land survr., Br. Hond | — | [1948, 1949, 1950, 1951] |
| 3 | 1943 | dep. dir. surv. and dep. sub-intendant cr. lands. | Trinidad | [1948, 1949, 1950, 1951] |
| 4 | 1945 | dir. and sub-intendant | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Busby, G. S___British Honduras___1924`

- Staff-list name: **Busby, G. S** | colony: **British Honduras** | listed 1924–1940 | editions [1924, 1927, 1928, 1929, 1930, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | G. S. Busby | Surveyor | Lands | — | — |
| 1927 | G. S. Busby | Surveyor | Lands | — | — |
| 1928 | G. S. Busby | Surveyor | Lands | — | — |
| 1929 | G. S. Busby | Surveyors | Lands | — | — |
| 1930 | G. S. Busby | Surveyor | Lands | — | — |
| 1932 | G. S. Busby | Surveyors | Lands | — | — |
| 1933 | G. S. Busby | Surveyors | Lands | — | — |
| 1934 | G. S. Busby | Surveyors | Lands | — | — |
| 1936 | G. S. Busby | Surveyors | Lands | — | — |
| 1937 | G. S. Busby | Surveyors | Lands | — | — |
| 1939 | G. S. Busby | Surveyors | Survey Department | — | — |
| 1940 | G. S. Busby | Surveys | Survey Department | — | — |

### Deterministic checks: `busby_george-smith_b1895` vs `Busby, G. S___British Honduras___1924`

- [PASS] surname_gate: bio 'BUSBY' vs stint 'Busby, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1924, birth 1895 (age 29)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1940
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

