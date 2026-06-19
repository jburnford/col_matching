<!-- {"case_id": "case_jarrette_bertel-oliver_b1891", "bio_ids": ["jarrette_bertel-oliver_b1891"], "stint_ids": ["Jarrette, B. O___Trinidad and Tobago___1927"]} -->
# Dossier case_jarrette_bertel-oliver_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jarrette_bertel-oliver_b1891`

- Printed name: **JARRETTE, Bertel Oliver**
- Birth year: 1891 (attested in editions [1948, 1949, 1950, 1951])
- Honours: D.M, M.B
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33624.v` — printed in editions [1948, 1949, 1950, 1951]:**

> JARRETTE, Bertel Oliver, M.B., Ch.B. (Edin.), D.M., R.E. (Liverpool).—b. 1891; ed. Queen's Royal Coll., Trinidad, Edinburgh Univ., Liverpool Univ.; med. offr., Trin., 1919; radiologist, 1939; senr. (gr. A), 1941.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | med. offr. | Trinidad | [1948, 1949, 1950, 1951] |
| 1 | 1939 | radiologist | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1941 | senr. (gr. A) | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Jarrette, B. O___Trinidad and Tobago___1927`

- Staff-list name: **Jarrette, B. O** | colony: **Trinidad and Tobago** | listed 1927–1934 | editions [1927, 1928, 1929, 1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | B. O. Jarrette | Medical Officer | Government Medical Officers | — | — |
| 1928 | B. O. Jarrette | — | Government Medical Officers | — | — |
| 1929 | B. O. Jarrette | — | Government Medical Officers | — | — |
| 1931 | B. O. Jarrette | — | Government Medical Officers | — | — |
| 1933 | B. O. Jarrette | Medical Officer | Medical Establishment | — | — |
| 1934 | B. O. Jarrette | Medical Officer | Government Medical Officers | — | — |

### Deterministic checks: `jarrette_bertel-oliver_b1891` vs `Jarrette, B. O___Trinidad and Tobago___1927`

- [PASS] surname_gate: bio 'JARRETTE' vs stint 'Jarrette, B. O' (exact)
- [PASS] initials: bio ['B', 'O'] ~ stint ['B', 'O']
- [PASS] age_gate: stint starts 1927, birth 1891 (age 36)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1934
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

