<!-- {"case_id": "case_tait_william-gladstone_b1901", "bio_ids": ["tait_william-gladstone_b1901"], "stint_ids": ["Tait, G___Nigeria___1927", "Tait, W. G___Sarawak___1940"]} -->
# Dossier case_tait_william-gladstone_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tait_william-gladstone_b1901`

- Printed name: **TAIT, William Gladstone**
- Birth year: 1901 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L36068.v` — printed in editions [1949, 1950, 1951]:**

> TAIT, William Gladstone.—b. 1901 ; ed. Walbotte County Council Sch., Northumberland and Marconi Wireless Sch., Newcastle-on-Tyne ; asstl. tels. and telephones dept., Sarawak, 1926 ; P.M.G., 1939 ; civ. intern., 1941-45.

**Version `col1948-L36281.v` — printed in editions [1948]:**

> TAIT, William Gladstone.—b. 1901; ed. Walbottle County Council Sch., Northumberland, Marconi Wireless Sch., Newcastle-on-Tyne and London (cert. of prof. in radiotel.); asst., tels. and telephones dept., Sarawak, 1926; P.M.G., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asstl. tels. and telephones dept. | Sarawak | [1948, 1949, 1950, 1951] |
| 1 | 1939 | P.M.G | Sarawak *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1941–1945 | civ. intern | Sarawak *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Tait, G___Nigeria___1927`

- Staff-list name: **Tait, G** | colony: **Nigeria** | listed 1927–1934 | editions [1927, 1929, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | G. Tait | Senior Marine Officer | Marine | R.N.R. | Lieutenant |
| 1929 | Lieut. G. Tait | Marine Officers, Grade I | Marine | — | — |
| 1933 | G. Tait | Marine Officer Grade I | Marine | — | — |
| 1934 | G. Tait | Marine Officers, Grade I | Marine | — | — |

### Deterministic checks: `tait_william-gladstone_b1901` vs `Tait, G___Nigeria___1927`

- [PASS] surname_gate: bio 'TAIT' vs stint 'Tait, G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1927, birth 1901 (age 26)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Tait, W. G___Sarawak___1940`

- Staff-list name: **Tait, W. G** | colony: **Sarawak** | listed 1940–1951 | editions [1940, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | W. G. Tait | Postmaster General | Civil Establishment | — | — |
| 1949 | W. G. Tait | Postmaster-General | Posts and Telegraphs | — | — |
| 1950 | W. G. Tait | Postmaster-General | POSTS AND TELEGRAPHS | — | — |
| 1951 | W. G. Tait | Postmaster-General | Posts and Telegraphs | — | — |

### Deterministic checks: `tait_william-gladstone_b1901` vs `Tait, W. G___Sarawak___1940`

- [PASS] surname_gate: bio 'TAIT' vs stint 'Tait, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1940, birth 1901 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1940-1951
- [FAIL] position_sim: best 38 vs bar 60: 'asstl. tels. and telephones dept.' ~ 'Postmaster General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

