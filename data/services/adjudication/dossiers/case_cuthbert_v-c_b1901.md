<!-- {"case_id": "case_cuthbert_v-c_b1901", "bio_ids": ["cuthbert_v-c_b1901"], "stint_ids": ["Cuthbert, C___Trinidad and Tobago___1922"]} -->
# Dossier case_cuthbert_v-c_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cuthbert_v-c_b1901`

- Printed name: **CUTHBERT, V. C**
- Birth year: 1901 (attested in editions [1957, 1958, 1959, 1960])
- Appears in editions: [1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1957-L22344.v` — printed in editions [1957, 1958, 1959, 1960]:**

> CUTHBERT, V. C.—b. 1901; ed. Wolmer's Sch., J'ca, and London Univ.; inspr., schs., J'ca, 1939; educ. offr., 1950; senr. educ. offr., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | inspr., schs. | Jamaica | [1957, 1958, 1959, 1960] |
| 1 | 1955 | senr. educ. offr | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960] |

## Candidate stint `Cuthbert, C___Trinidad and Tobago___1922`

- Staff-list name: **Cuthbert, C** | colony: **Trinidad and Tobago** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Miss C. Cuthbert | 17th Clerk | Post Office Department | — | — |
| 1923 | Miss C. Cuthbert | 17th Clerk | Post Office Department | — | — |

### Deterministic checks: `cuthbert_v-c_b1901` vs `Cuthbert, C___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'CUTHBERT' vs stint 'Cuthbert, C' (exact)
- [PASS] initials: bio ['V', 'C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1922, birth 1901 (age 21)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

