<!-- {"case_id": "case_corbett_d-m_b1911", "bio_ids": ["corbett_d-m_b1911"], "stint_ids": ["Corbett, D. M___Bermuda___1929"]} -->
# Dossier case_corbett_d-m_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `corbett_d-m_b1911`

- Printed name: **CORBETT, D. M**
- Birth year: 1911 (attested in editions [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L21615.v` — printed in editions [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> CORBETT, D. M.—b. 1911; ed. Gordon's Coll., Aberdeen, and Royal (Dick) Vet. Coll., Edin.; vet. offr., min. of agric., N. Ireland, 1937; dept. of agric., N.Z., 1944; Tang., 1949; asst. D.V.S., 1957; senr. vet. offr., H.K., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | vet. offr., min. of agric., N. Ireland | — | [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1944 | dept. of agric. | New Zealand | [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1949 | dept. of agric. | Tanganyika | [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1957 | asst. D.V.S | Tanganyika *(inherited from previous clause)* | [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1957 | senr. vet. offr. | Hong Kong | [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Corbett, D. M___Bermuda___1929`

- Staff-list name: **Corbett, D. M** | colony: **Bermuda** | listed 1929–1932 | editions [1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | D. M. Corbett | Senior Medical Officer | Chief Military Officers | — | Major |
| 1930 | Major D. M. Corbett | Senior Medical Officer | Chief Military Officers | — | Major |
| 1931 | Major D. M. Corbett | Senior Medical Officer | Chief Military Officers | — | Major |
| 1932 | Major D. M. Corbett | Senior Medical Officer | Chief Military Officers. | — | Major |

### Deterministic checks: `corbett_d-m_b1911` vs `Corbett, D. M___Bermuda___1929`

- [PASS] surname_gate: bio 'CORBETT' vs stint 'Corbett, D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1929, birth 1911 (age 18)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1932
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

