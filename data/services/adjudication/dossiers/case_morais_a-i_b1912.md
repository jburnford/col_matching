<!-- {"case_id": "case_morais_a-i_b1912", "bio_ids": ["morais_a-i_b1912"], "stint_ids": ["Morais, A. I___Jamaica___1955"]} -->
# Dossier case_morais_a-i_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morais_a-i_b1912`

- Printed name: **MORAIS, A. I**
- Birth year: 1912 (attested in editions [1963])
- Appears in editions: [1963]

### Verbatim printed entry text (OCR)

**Version `col1963-L23001.v` — printed in editions [1963]:**

> MORAIS, A. I.—b. 1912; ed. Kingston Coll., J'ca, and Lond. Univ.; asst. stats. offr., J'ca., 1940; stats. offr., 1943; asst. island statistn., 1945; asst. ch. elect. offr., 1948; dep. dir. stats., 1954; secon. ch. statistn., Carib. commsn., 1950-55; secon. T.W.I. govt. asst. trade commsn. in U.K., 1956; prim. asst. sec., J'ca., 1959; asst. U.S., off. of Prem., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | asst. stats. offr. | Jamaica | [1963] |
| 1 | 1943 | stats. offr | Jamaica *(inherited from previous clause)* | [1963] |
| 2 | 1945 | asst. island statistn | Jamaica *(inherited from previous clause)* | [1963] |
| 3 | 1948 | asst. ch. elect. offr | Jamaica *(inherited from previous clause)* | [1963] |
| 4 | 1950–1955 | secon. ch. statistn., Carib. commsn | Jamaica *(inherited from previous clause)* | [1963] |
| 5 | 1954 | dep. dir. stats | Jamaica *(inherited from previous clause)* | [1963] |
| 6 | 1956 | secon. T.W.I. govt. asst. trade commsn. in U.K | Jamaica *(inherited from previous clause)* | [1963] |
| 7 | 1959 | prim. asst. sec. | Jamaica | [1963] |
| 8 | 1961 | asst. U.S., off. of Prem | Jamaica *(inherited from previous clause)* | [1963] |

## Candidate stint `Morais, A. I___Jamaica___1955`

- Staff-list name: **Morais, A. I** | colony: **Jamaica** | listed 1955–1956 | editions [1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | A. I. Morais | Deputy Director of Statistical Services | Civil Establishment | — | — |
| 1956 | A. I. Morais | Deputy Director of Statistical Services | Civil Establishment | — | — |

### Deterministic checks: `morais_a-i_b1912` vs `Morais, A. I___Jamaica___1955`

- [PASS] surname_gate: bio 'MORAIS' vs stint 'Morais, A. I' (exact)
- [PASS] initials: bio ['A', 'I'] ~ stint ['A', 'I']
- [PASS] age_gate: stint starts 1955, birth 1912 (age 43)
- [PASS] colony: 9 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1955-1956
- [FAIL] position_sim: best 50 vs bar 60: 'dep. dir. stats' ~ 'Deputy Director of Statistical Services'
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

