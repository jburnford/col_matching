<!-- {"case_id": "case_eddey_leslie-george_b1903", "bio_ids": ["eddey_leslie-george_b1903"], "stint_ids": ["Eddey, L. G___British Guiana___1949"]} -->
# Dossier case_eddey_leslie-george_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `eddey_leslie-george_b1903`

- Printed name: **EDDEY, Leslie George**
- Birth year: 1903 (attested in editions [1953, 1954, 1955, 1956])
- Honours: M.B
- Appears in editions: [1948, 1949, 1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1953-L17211.v` — printed in editions [1953, 1954, 1955, 1956]:**

> EDDEY, L. G.—b. 1903; ed. Aberdeen Univ.; sany. inspr., G.C., 1928-34; M.O.H., 1939; D.D.M.S. and registr.-gen., B. Guiana, 1946; D.D.M.S., 1948; D.D.M.S., G.C., 1951; ch. med. offr., 1952; author of articles on mosquito destruction and disease control in medical journals.

**Version `col1948-L32386.v` — printed in editions [1948, 1949, 1951]:**

> EDDEY, Leslie George, M.B., Ch.B. (Aber.), D.T.M. & H. (Liv.), D.P.H. (Lond.).—b. 1903; ed. Aberdeen Univ.; Langley mem. prize (L.S.H. & T.M.); sani. inspr., G.C., 1928-34; M.O.H., 1939; D.D.M.S. and registr.-gen., B. Guiana, 1946; D.M.S., 1948; author of articles on mosquito destruction and disease control in medical journals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928–1934 | sany. inspr. | Gold Coast | [1948, 1949, 1951, 1953, 1954, 1955, 1956] |
| 1 | 1939 | M.O.H | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1951, 1953, 1954, 1955, 1956] |
| 2 | 1946 | D.D.M.S. and registr.-gen., B. Guiana | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1951, 1953, 1954, 1955, 1956] |
| 3 | 1948 | D.D.M.S | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1951, 1953, 1954, 1955, 1956] |
| 4 | 1951 | D.D.M.S. | Gold Coast | [1953, 1954, 1955, 1956] |
| 5 | 1952 | ch. med. offr | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |

## Candidate stint `Eddey, L. G___British Guiana___1949`

- Staff-list name: **Eddey, L. G** | colony: **British Guiana** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. G. Eddey | Director of Medical Services | Medical | — | — |
| 1950 | L. G. Eddey | Director of Medical Services | Medical | — | — |

### Deterministic checks: `eddey_leslie-george_b1903` vs `Eddey, L. G___British Guiana___1949`

- [PASS] surname_gate: bio 'EDDEY' vs stint 'Eddey, L. G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1949, birth 1903 (age 46)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

