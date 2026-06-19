<!-- {"case_id": "case_hotton_m-r-a_b1926", "bio_ids": ["hotton_m-r-a_b1926"], "stint_ids": ["Hooton, A___Hong Kong___1950"]} -->
# Dossier case_hotton_m-r-a_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hooton, A___Hong Kong___1950` is also gate-compatible with biography(ies) outside this case: ['hooton_arthur_b1912'] (already linked elsewhere or filtered).

## Biography `hotton_m-r-a_b1926`

- Printed name: **HOTTON, M. R. A**
- Birth year: 1926 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L15553.v` — printed in editions [1966]:**

> HOTTON, M. R. A.—b. 1926; ed. Ladysmith Senr. Boys Sch., Exeter and Exeter Tech. Sch.; mil. serv., 1946-48; Br. P.O., 1942-48; techn., gr. I, E.A.P. & T. admin., 1954; asst. engrn., gr. II, 1955; gr. I (old style), 1959; gr. I (new style), 1961; senr. asst. engrn., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942–1948 | Br. P.O | — | [1966] |
| 1 | 1954 | techn., gr. I, E.A.P. & T. admin | East Africa Protectorate | [1966] |
| 2 | 1955 | asst. engrn., gr. II | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 3 | 1959 | gr. I (old style) | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 4 | 1961 | gr. I (new style) | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 5 | 1965 | senr. asst. engrn | East Africa Protectorate *(inherited from previous clause)* | [1966] |

## Candidate stint `Hooton, A___Hong Kong___1950`

- Staff-list name: **Hooton, A** | colony: **Hong Kong** | listed 1950–1961 | editions [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. Hooton | Legal Officer | Legal | — | — |
| 1951 | A. Hooton | Legal Officer | Legal | — | — |
| 1953 | A. Hooton | Solicitor-General | Civil Establishment | — | — |
| 1954 | A. Hooton | Solicitor-General | Civil Establishment | — | — |
| 1955 | A. Hooton | Solicitor-General | Civil Establishment | Q.C. | — |
| 1956 | A. Hooton | Solicitor-General | Civil Establishment | — | — |
| 1957 | A. Hooton | Solicitor-General | Civil Establishment | — | — |
| 1958 | A. Hooton | Solicitor-General | Civil Establishment | C.B. | — |
| 1959 | A. Hooton | Solicitor-General | Civil Establishment | — | — |
| 1960 | A. Hooton | Solicitor-General | Civil Establishment | — | — |
| 1961 | A. Hooton | Solicitor-General | Civil Establishment | — | — |

### Deterministic checks: `hotton_m-r-a_b1926` vs `Hooton, A___Hong Kong___1950`

- [PASS] surname_gate: bio 'HOTTON' vs stint 'Hooton, A' (fuzzy:1)
- [PASS] initials: bio ['M', 'R', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1950, birth 1926 (age 24)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1961
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

