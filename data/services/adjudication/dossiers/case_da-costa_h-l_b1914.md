<!-- {"case_id": "case_da-costa_h-l_b1914", "bio_ids": ["da-costa_h-l_b1914"], "stint_ids": ["Da Costa, H. L___West Indies Federation___1961"]} -->
# Dossier case_da-costa_h-l_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `da-costa_h-l_b1914`

- Printed name: **Da COSTA, H. L**
- Birth year: 1914 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Honours: C.M.G (1962)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L22352.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> Da COSTA, H. L., C.M.G. (1962).—b. 1914; ed. Calabar High Sch., J'ca, and St. Edmund Hall, Oxford; barrister-at-law, Gray's Inn; crown coun., J'ca, 1952; senr., 1955; asst. atty.-gen., 1955; fed. atty.-gen., T.W.I., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | crown coun. | Jamaica | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1955 | senr | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1959 | fed. atty.-gen., T.W.I | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Da Costa, H. L___West Indies Federation___1961`

- Staff-list name: **Da Costa, H. L** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | H. L. Da Costa | Attorney-General | Law Officers | Q.C. | — |
| 1962 | H. L. Da Costa | Attorney-General | Law Officers | C.M.G. | — |

### Deterministic checks: `da-costa_h-l_b1914` vs `Da Costa, H. L___West Indies Federation___1961`

- [PASS] surname_gate: bio 'Da COSTA' vs stint 'Da Costa, H. L' (exact)
- [PASS] initials: bio ['H', 'L'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1961, birth 1914 (age 47)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
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

