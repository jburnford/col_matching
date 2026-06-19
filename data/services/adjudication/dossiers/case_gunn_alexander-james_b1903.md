<!-- {"case_id": "case_gunn_alexander-james_b1903", "bio_ids": ["gunn_alexander-james_b1903"], "stint_ids": ["Gunn, A. J___Northern Rhodesia___1930", "Gunn, A. J___Northern Rhodesia___1936", "Gunn, A. J___Northern Rhodesia___1949"]} -->
# Dossier case_gunn_alexander-james_b1903

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gunn_alexander-james_b1903`

- Printed name: **GUNN, Alexander James**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33057.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GUNN, Alexander James.—b. 1903; ed. Durness Sch. and Aberdeen Univ., M.A., teacher's cert.; on mil. serv. 1940-44, lieut.; asst. mstr., Scottish Educ. Dept., 1924; mstr., N. Rhod. European Educ. Dept., 1929; prin., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | asst. mstr., Scottish Educ. Dept | — | [1948, 1949, 1950, 1951] |
| 1 | 1929 | mstr., N. Rhod. European Educ. Dept | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 2 | 1931 | prin | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Gunn, A. J___Northern Rhodesia___1930`

- Staff-list name: **Gunn, A. J** | colony: **Northern Rhodesia** | listed 1930–1931 | editions [1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | A. J. Gunn | Master | European Education | — | — |
| 1931 | A. J. Gunn | Masters | European Education | — | — |

### Deterministic checks: `gunn_alexander-james_b1903` vs `Gunn, A. J___Northern Rhodesia___1930`

- [PASS] surname_gate: bio 'GUNN' vs stint 'Gunn, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1930, birth 1903 (age 27)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1930-1931
- [FAIL] position_sim: best 22 vs bar 60: 'mstr., N. Rhod. European Educ. Dept' ~ 'Master'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Gunn, A. J___Northern Rhodesia___1936`

- Staff-list name: **Gunn, A. J** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | A. J. Gunn | Headmasters | European Education | — | — |
| 1937 | A. J. Gunn | Headmasters | European Education | — | — |
| 1939 | A. J. Gunn | Head Master | European Education | — | — |
| 1940 | A. J. Gunn | Head Master | European Education | — | — |

### Deterministic checks: `gunn_alexander-james_b1903` vs `Gunn, A. J___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'GUNN' vs stint 'Gunn, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1936, birth 1903 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 13 vs bar 60: 'prin' ~ 'Headmasters'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Gunn, A. J___Northern Rhodesia___1949`

- Staff-list name: **Gunn, A. J** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. J. Gunn | Principal | Education | — | — |
| 1951 | A. J. Gunn | Principal | Education | — | — |

### Deterministic checks: `gunn_alexander-james_b1903` vs `Gunn, A. J___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'GUNN' vs stint 'Gunn, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1949, birth 1903 (age 46)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

