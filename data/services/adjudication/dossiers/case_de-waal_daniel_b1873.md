<!-- {"case_id": "case_de-waal_daniel_b1873", "bio_ids": ["de-waal_daniel_b1873"], "stint_ids": ["de Waal, David___Cape of Good Hope___1888"]} -->
# Dossier case_de-waal_daniel_b1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['de-waal_daniel_b1873'] carry a single initial only — the namesake trap applies.

## Biography `de-waal_daniel_b1873`

- Printed name: **DE WAAL, Daniel**
- Birth year: 1873 (attested in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937])
- Honours: D.S.O
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1924-L53763.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937]:**

> DE WAAL, Hon. Daniel, D.S.O., K.C.—B. 1873; ed. Victoria Coll., Stellenbosch and Trinity Hall, Cambridge; B.A., LL. B. (Cantab. and Cape); admitted, advoo., Cape and Transvaal, 1897; practised, Pretoria; German S. W. Africa campaign, 1915; K.C., 1919; ag. judge, Griqualand West Local Divn., Oct., 1919; judge, sup. ct., T.P.D., Aug., 1920; judge pres., T.P.D., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | admitted, advoo., Cape and Transvaal | Cape of Good Hope | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 1 | 1915 | German S. W. Africa campaign | Cape of Good Hope *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 2 | 1919 | K.C | Cape of Good Hope *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 3 | 1919 | ag. judge, Griqualand West Local Divn | Griqualand West | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 4 | 1920 | judge, sup. ct., T.P.D | Griqualand West *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 5 | 1927 | judge pres., T.P.D | Griqualand West *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |

## Candidate stint `de Waal, David___Cape of Good Hope___1888`

- Staff-list name: **de Waal, David** | colony: **Cape of Good Hope** | listed 1888–1897 | editions [1888, 1889, 1890, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | David de Waal | Member | Constituency Members | — | — |
| 1889 | David de Waal | — | Constituency | — | — |
| 1890 | David de Waal | Member | House of Assembly | — | — |
| 1896 | David de Waal | — | House of Assembly | — | — |
| 1897 | David de Waal | — | Members | — | — |

### Deterministic checks: `de-waal_daniel_b1873` vs `de Waal, David___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'DE WAAL' vs stint 'de Waal, David' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1888, birth 1873 (age 15)
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1897
- [FAIL] position_sim: best 21 vs bar 60: 'admitted, advoo., Cape and Transvaal' ~ 'Member'
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

