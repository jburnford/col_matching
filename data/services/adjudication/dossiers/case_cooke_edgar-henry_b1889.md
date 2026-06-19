<!-- {"case_id": "case_cooke_edgar-henry_b1889", "bio_ids": ["cooke_edgar-henry_b1889"], "stint_ids": ["Cooke, E. H___Northern Rhodesia___1936"]} -->
# Dossier case_cooke_edgar-henry_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 25 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cooke_edgar-henry_b1889`

- Printed name: **COOKE, Edgar Henry**
- Birth year: 1889 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L65831.v` — printed in editions [1939, 1940]:**

> COOKE, Edgar Henry.—B. 1889; war serv., 1916-17; probr., N. Rhodesia, 1918; asst. nat. commr., 1919; nat. commr., 1924; asst. mag., 1928; dist. commr., 1933; ag. prov. commr., 1936 and 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916–1917 | war serv. | — | [1939, 1940] |
| 1 | 1918–1918 | probr. | Northern Rhodesia | [1939, 1940] |
| 2 | 1919–1919 | asst. nat. commr. | — | [1939, 1940] |
| 3 | 1924–1924 | nat. commr. | — | [1939, 1940] |
| 4 | 1928–1928 | asst. mag. | — | [1939, 1940] |
| 5 | 1933–1933 | dist. commr. | — | [1939, 1940] |
| 6 | 1936–1938 | ag. prov. commr. | — | [1939, 1940] |

## Candidate stint `Cooke, E. H___Northern Rhodesia___1936`

- Staff-list name: **Cooke, E. H** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. H. Cooke | District Officers | District Administration | — | — |
| 1939 | E. H. Cooke | District Officer | District Administration | — | — |
| 1940 | E. H. Cooke | Provincial Commissioner | District Administration | — | — |

### Deterministic checks: `cooke_edgar-henry_b1889` vs `Cooke, E. H___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'COOKE' vs stint 'Cooke, E. H' (exact)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1936, birth 1889 (age 47)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

