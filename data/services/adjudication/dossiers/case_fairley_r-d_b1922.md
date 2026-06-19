<!-- {"case_id": "case_fairley_r-d_b1922", "bio_ids": ["fairley_r-d_b1922"], "stint_ids": ["Fairley, D___St Helena___1949", "Fairley, R. D___Western Pacific___1954"]} -->
# Dossier case_fairley_r-d_b1922

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fairley_r-d_b1922`

- Printed name: **FAIRLEY, R. D**
- Birth year: 1922 (attested in editions [1959, 1960])
- Appears in editions: [1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1959-L22834.v` — printed in editions [1959, 1960]:**

> FAIRLEY, R. D.—b. 1922; ed. Cheltenham Coll.; mil. serv., 1940-46, R.A.F. (desps.); admin. offr., N. Heb., 1947; asst. sec., W. Pac. H.C., 1949; secon., spec. asst. to sec.-gen., S. Pac. Comsn., New Caledonia, 1951-52; dist. comsnr., B. Sol. Is. Prot., 1955; admin. offr., Nyasa., 1957-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | admin. offr., N. Heb | — | [1959, 1960] |
| 1 | 1949 | asst. sec., W. Pac. H.C | Western Pacific | [1959, 1960] |
| 2 | 1951–1952 | secon., spec. asst. to sec.-gen., S. Pac. Comsn., New Caledonia | Western Pacific *(inherited from previous clause)* | [1959, 1960] |
| 3 | 1955 | dist. comsnr., B. Sol. Is. Prot | Western Pacific *(inherited from previous clause)* | [1959, 1960] |
| 4 | 1957–1959 | admin. offr. | Nyasaland | [1959, 1960] |

## Candidate stint `Fairley, D___St Helena___1949`

- Staff-list name: **Fairley, D** | colony: **St Helena** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. Fairley | Senior Medical Officer | Public Health | — | — |
| 1950 | D. Fairley | Senior Medical Officer | PUBLIC HEALTH | — | — |
| 1951 | D. Fairley | Senior Medical Officer | PUBLIC HEALTH | — | — |

### Deterministic checks: `fairley_r-d_b1922` vs `Fairley, D___St Helena___1949`

- [PASS] surname_gate: bio 'FAIRLEY' vs stint 'Fairley, D' (exact)
- [PASS] initials: bio ['R', 'D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fairley, R. D___Western Pacific___1954`

- Staff-list name: **Fairley, R. D** | colony: **Western Pacific** | listed 1954–1955 | editions [1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | R. D. Fairley | Assistant Secretary | Civil Establishment | — | — |
| 1955 | R. D. Fairley | Assistant Secretary | Civil Establishment | — | — |

### Deterministic checks: `fairley_r-d_b1922` vs `Fairley, R. D___Western Pacific___1954`

- [PASS] surname_gate: bio 'FAIRLEY' vs stint 'Fairley, R. D' (exact)
- [PASS] initials: bio ['R', 'D'] ~ stint ['R', 'D']
- [PASS] age_gate: stint starts 1954, birth 1922 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Western Pacific'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1954-1955
- [FAIL] position_sim: best 36 vs bar 60: 'dist. comsnr., B. Sol. Is. Prot' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

