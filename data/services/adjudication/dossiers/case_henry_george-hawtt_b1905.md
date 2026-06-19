<!-- {"case_id": "case_henry_george-hawtt_b1905", "bio_ids": ["henry_george-hawtt_b1905", "henry_george-hewitt_b1906"], "stint_ids": ["Henry, G. H___Hong Kong___1936"]} -->
# Dossier case_henry_george-hawtt_b1905

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 42 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Henry, G. H___Hong Kong___1936'] have more than one claimant biography in this case.
- NOTE: stint `Henry, G. H___Hong Kong___1936` is also gate-compatible with biography(ies) outside this case: ['henry_george-hewitt_b1905'] (already linked elsewhere or filtered).
- NOTE: stint `Henry, G. H___Hong Kong___1936` is also gate-compatible with biography(ies) outside this case: ['henry_george-hewitt_b1905'] (already linked elsewhere or filtered).

## Biography `henry_george-hawtt_b1905`

- Printed name: **HENRY, GEORGE HAWTT**
- Birth year: 1905 (attested in editions [1939, 1940])
- Honours: L.M
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L67458.v` — printed in editions [1939, 1940]:**

> HENRY, GEORGE HAWTT, L.M., L.Ch., L.A.O. (Dub. Univ.).—B. 1905; med. offr., Nigeria, Aug., 1920; med. offr., med. dept., Hong Kong; med. offr. in ch., Lai Chi Kok prison, Kowloon mortuary, asst. M.O., Kowloon hosp., M.O. in ch., families, Kowloon, do., pol., Kowloon and do., K.C.R., 1935; med. offr., Nigeria, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | med. offr. | Nigeria | [1939, 1940] |
| 1 | 1935 | med. offr. in ch., Lai Chi Kok prison, Kowloon mortuary, asst. M.O., Kowloon hosp., M.O. in ch., families, Kowloon, do., pol., Kowloon and do., K.C.R | Nigeria *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1939 | med. offr. | Nigeria | [1939, 1940] |

## Biography `henry_george-hewitt_b1906`

- Printed name: **HENRY, GEORGE HEWITT**
- Birth year: 1906 (attested in editions [1936])
- Honours: L.C.H, L.M
- Appears in editions: [1936]

### Verbatim printed entry text (OCR)

**Version `col1936-L61515.v` — printed in editions [1936]:**

> HENRY, GEORGE HEWITT, L.M., L.C.H., L.A.O. (Dub. Univ.).—B. 1906; med. offr., Nigeria, Aug., 1929; med. offr., med. dept., Hong Kong; med. offr. in ch., Lai Chi Kok prison, Kowloon mortuary and astt. M.O., Kowloon hosp., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | med. offr. | Nigeria | [1936] |
| 1 | 1935 | med. offr. in ch., Lai Chi Kok prison, Kowloon mortuary and astt. M.O., Kowloon hosp | Nigeria *(inherited from previous clause)* | [1936] |

## Candidate stint `Henry, G. H___Hong Kong___1936`

- Staff-list name: **Henry, G. H** | colony: **Hong Kong** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. H. Henry | Medical Officers | Medical Department | — | — |
| 1937 | G. H. Henry | Medical Officer | Medical Department | — | — |
| 1939 | G. H. Henry | Medical Officer | Medical Department | — | — |

### Deterministic checks: `henry_george-hawtt_b1905` vs `Henry, G. H___Hong Kong___1936`

- [PASS] surname_gate: bio 'HENRY' vs stint 'Henry, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `henry_george-hewitt_b1906` vs `Henry, G. H___Hong Kong___1936`

- [PASS] surname_gate: bio 'HENRY' vs stint 'Henry, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1936, birth 1906 (age 30)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

