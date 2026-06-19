<!-- {"case_id": "case_watt_george_b1905", "bio_ids": ["watt_george_b1905"], "stint_ids": ["Watt, W. G___Togoland___1920"]} -->
# Dossier case_watt_george_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['watt_george_b1905'] carry a single initial only — the namesake trap applies.

## Biography `watt_george_b1905`

- Printed name: **WATT, George**
- Birth year: 1905 (attested in editions [1953, 1954, 1955])
- Honours: M.B
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1953-L19469.v` — printed in editions [1953, 1954, 1955]:**

> WATT, G., M.B.E. (mil.).—b. 1905; ed. S. African Coll., Cape Town, and Edin. Univ.; mil. serv., 1939-45 (desps.); med. offr., G.C., 1934; asst. D.M.S., 1948; prin. M.O., 1953; dep. ch., 1954.

**Version `col1948-L36716.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WATT, George, M.B.E. (mil.), M.B., Ch.B. (Edin.), D.T.M. & H. (Edin.).—b. 1905 ; ed. S. African Coll., Cape Town and Edin. Univ. ; on mil. serv., 1939-45 (desps.) ; med. offr., G.C., 1934 ; asst. D.M.S., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | med. offr. | Gold Coast | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1948 | asst. D.M.S | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955] |
| 2 | 1949 | asst. D.M.S | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1953 | prin. M.O | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955] |
| 4 | 1954 | dep. ch | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955] |

## Candidate stint `Watt, W. G___Togoland___1920`

- Staff-list name: **Watt, W. G** | colony: **Togoland** | listed 1920–1925 | editions [1920, 1921, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | W. G. Watt | Medical Officer of Health | Sanitary Branch | — | — |
| 1921 | W. G. Watt | Medical Officer of Health | Sanitary Branch | — | — |
| 1925 | W. G. Watt | Senior Sanitary Officer | Sanitation Branch | — | — |

### Deterministic checks: `watt_george_b1905` vs `Watt, W. G___Togoland___1920`

- [PASS] surname_gate: bio 'WATT' vs stint 'Watt, W. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1920, birth 1905 (age 15)
- [FAIL] colony: no placed event resolves to 'Togoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1925
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

