<!-- {"case_id": "case_ames_cecil-geraint_b1897", "bio_ids": ["ames_cecil-geraint_b1897"], "stint_ids": ["Ames, C. G___Gambia___1964"]} -->
# Dossier case_ames_cecil-geraint_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ames_cecil-geraint_b1897`

- Printed name: **AMES, Cecil Geraint**
- Birth year: 1897 (attested in editions [1935, 1936, 1937, 1939])
- Honours: Kt (1965)
- Appears in editions: [1935, 1936, 1937, 1939, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `dol1935-L56559.v` — printed in editions [1935, 1936, 1937, 1939]:**

> AMES, Cecil Geraint.—B. 1897; ed. Elstree Prep. Schl. and Dover Coll.; (schol.); 5th Somerset Light Infv., 1915-19; Law Soc.'s final exam. (hons.), 1921; Nigerian admnstr. serv., 1922; ag. ch. registr., sup. ct., Nov. 1932-July, 1933; admitted, solr., Nov., 1933; attd. judl. dept., Jan.—Mar., 1934; astt. judge, high ct., Apr., 1934.

**Version `col1963-L16873.v` — printed in editions [1963, 1964, 1965, 1966]:**

> AMES, Sir Cecil, Kt. (1965).—b. 1897; ed. Dover Coll.; admin. offr., 1922; asst. judge, Nig. Prot., 1934; judge, 1945; ret. 1950; re-apptd. temp. judge, Gamb.; just. of appeal, W. Afr. ct. of appeal; comsnr. rev. of laws; pres. S.L. and Gamb., ct. of appeal, 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | 5th Somerset Light Infv | — | [1935, 1936, 1937, 1939] |
| 1 | 1921 | Law Soc.'s final exam. (hons.) | — | [1935, 1936, 1937, 1939] |
| 2 | 1922 | Nigerian admnstr. serv | — | [1935, 1936, 1937, 1939] |
| 3 | 1922 | admin. offr | — | [1963, 1964, 1965, 1966] |
| 4 | 1932–1933 | ag. ch. registr., sup. ct | — | [1935, 1936, 1937, 1939] |
| 5 | 1933 | admitted, solr | — | [1935, 1936, 1937, 1939] |
| 6 | 1934 | attd. judl. dept., Jan.— | — | [1935, 1936, 1937, 1939] |
| 7 | 1934 | astt. judge, high ct | — | [1935, 1936, 1937, 1939] |
| 8 | 1934 | asst. judge | Nigeria | [1963, 1964, 1965, 1966] |
| 9 | 1945 | judge | Nigeria *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 10 | 1950 | ret | Nigeria *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 11 | 1962 | pres. S.L. and Gamb., ct. of appeal | Nigeria *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Ames, C. G___Gambia___1964`

- Staff-list name: **Ames, C. G** | colony: **Gambia** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | C. G. Ames | President, Gambia Court of Appeal | Judiciary | — | — |
| 1965 | C. G. Ames | President, Gambia Court of Appeal | JUDICIARY | — | — |

### Deterministic checks: `ames_cecil-geraint_b1897` vs `Ames, C. G___Gambia___1964`

- [PASS] surname_gate: bio 'AMES' vs stint 'Ames, C. G' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1964, birth 1897 (age 67)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1965
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

