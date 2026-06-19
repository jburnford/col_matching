<!-- {"case_id": "case_morgan_james-conwy_b1910", "bio_ids": ["morgan_james-conwy_b1910"], "stint_ids": ["Morgan, J___Bermuda___1931"]} -->
# Dossier case_morgan_james-conwy_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 85 official(s) with this surname in the graph's staff lists; 36 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Morgan, J___Bermuda___1931` is also gate-compatible with biography(ies) outside this case: ['morgan_mervyn-james-eversfield_b1907'] (already linked elsewhere or filtered).

## Biography `morgan_james-conwy_b1910`

- Printed name: **MORGAN, James Conwy**
- Birth year: 1910 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L23135.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> MORGAN, J. C.—b. 1910; ed. Malvern Coll. and Brasenose Coll., Oxford; mil. serv., 1939-47, K.A.R.; B.M.A. Somalia, lt.-col. (senr. civ. affrs. offr.) (desps.); cadet, Tang., 1934; asst. dist. offr., 1936; dist. offr. (in absentia), 1946; prin., C.O., 1947; asst. sec., 1955; attd. Monckton comsn., 1960.

**Version `col1948-L34770.v` — printed in editions [1948, 1949, 1950, 1951]:**

> MORGAN, James Conwy.—b. 1910; ed. Malvern Coll. (schol.), Brasenose Coll., Oxford (schol.), Heath Harrison exhibr. and Kitchener schol., 2nd cl. hon. mods., 1st cl. lit. humaniors, London Univ., inter B.Sc. (econ.) (extra-mural); war serv., 1939-47, K.A.R. (capt.), polit. offr., Intern. Somaliland (maj.), G.S.O. II, 1942-44, lt.-col., senr. civ. aff. offr., i/c Benadin Prov., 1945 (desps.): cadet, T.T., 1934; asst. dist. offr., 1936; dist. offr., 1946; prin. C.O., 3rd Mar. 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | cadet | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1936 | asst. dist. offr | Tanganyika *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1946 | dist. offr. (in absentia) | Tanganyika *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1947 | prin. | Colonial Office | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1955 | asst. sec | Colonial Office *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 5 | 1960 | attd. Monckton comsn | Colonial Office *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Morgan, J___Bermuda___1931`

- Staff-list name: **Morgan, J** | colony: **Bermuda** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | Mrs J. Morgan | Junior Clerk | Public Works Department | — | — |
| 1932 | Mrs J. Morgan | Junior Clerk | Public Works Department | — | — |

### Deterministic checks: `morgan_james-conwy_b1910` vs `Morgan, J___Bermuda___1931`

- [PASS] surname_gate: bio 'MORGAN' vs stint 'Morgan, J' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J']
- [PASS] age_gate: stint starts 1931, birth 1910 (age 21)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

