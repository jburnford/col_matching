<!-- {"case_id": "case_cardin_pierre-joseph-arthur_b1879", "bio_ids": ["cardin_pierre-joseph-arthur_b1879"], "stint_ids": ["Carden, John___Rhodesia___1908"]} -->
# Dossier case_cardin_pierre-joseph-arthur_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cardin_pierre-joseph-arthur_b1879`

- Printed name: **CARDIN, PIERRE JOSEPH ARTHUR**
- Birth year: 1879 (attested in editions [1936, 1937, 1940])
- Appears in editions: [1927, 1928, 1929, 1930, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L59550.v` — printed in editions [1936, 1937, 1940]:**

> CARDIN, HON. PIERRE JOSEPH ARTHUR (Richelieu)—B. 1879; ed. Sorel Comm'l. Coll. and pvtly. teachers; studied law, Laval Univ.; batonnier Richelieu bar sec.; first elec. to H. of C., Canada, at g.e., 1911; re-elec., g.e., 1917 and g.e., 1921; mem., privy coun. and min. of marine and fisheries, 1924; re-elec. by accl. after assuming office, 1924; re-elec. at g.e., 1925, 1926, 1930 and 1935; resigned portfolio with King Cabinet, 1926; re-apptd. min. of marine and fisheries, Sept., 1926; min. of pub. wks. in King cabinet, 1935.

**Version `col1927-L57735.v` — printed in editions [1927, 1928, 1929, 1930]:**

> CARDIN, PIERRE J. ARTHUR.—B. 1879; ed. Laval Univ.; rep. Richelieu in House of Commons, Canada, 1911-26; min. of marine and fisheries, 30th Jan., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911–1911 | first elec. to H. of C. | Canada | [1927, 1928, 1929, 1930, 1936, 1937, 1940] |
| 1 | 1917–1921 | re-elec., g.e. | — | [1936, 1937, 1940] |
| 2 | 1924–1924 | mem., privy coun. and min. of marine and fisheries | Canada *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1936, 1937, 1940] |
| 3 | 1924–1924 | re-elec. by accl. after assuming office | — | [1936, 1937, 1940] |
| 4 | 1925–1935 | re-elec. at g.e. | — | [1936, 1937, 1940] |
| 5 | 1926–1926 | resigned portfolio with King Cabinet | — | [1936, 1937, 1940] |
| 6 | 1926–1926 | re-apptd. min. of marine and fisheries | — | [1936, 1937, 1940] |
| 7 | 1935–1935 | min. of pub. wks. in King cabinet | — | [1936, 1937, 1940] |

## Candidate stint `Carden, John___Rhodesia___1908`

- Staff-list name: **Carden, John** | colony: **Rhodesia** | listed 1908–1910 | editions [1908, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | John Carden | Commandant, Barotse Native Police | NORTH-WESTERN RHODESIA | — | Lieut.-Colonel |
| 1910 | John Carden | Commandant, Barotse Native Police | NORTH-WESTERN RHODESIA | — | Lt.-Col. |

### Deterministic checks: `cardin_pierre-joseph-arthur_b1879` vs `Carden, John___Rhodesia___1908`

- [PASS] surname_gate: bio 'CARDIN' vs stint 'Carden, John' (fuzzy:1)
- [PASS] initials: bio ['P', 'J', 'A'] ~ stint ['J']
- [PASS] age_gate: stint starts 1908, birth 1879 (age 29)
- [FAIL] colony: no placed event resolves to 'Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1910
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

