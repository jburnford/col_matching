<!-- {"case_id": "case_mccracken_albert-victor-neilson_b1886", "bio_ids": ["mccracken_albert-victor-neilson_b1886"], "stint_ids": ["McCracken, A. V. N___Trinidad and Tobago___1928"]} -->
# Dossier case_mccracken_albert-victor-neilson_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mccracken_albert-victor-neilson_b1886`

- Printed name: **McCRACKEN, ALBERT VICTOR NEILSON**
- Birth year: 1886 (attested in editions [1940])
- Appears in editions: [1928, 1931, 1932, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66304.v` — printed in editions [1940]:**

> McCRACKEN, ALBERT VICTOR NEILSON.—B. 1886; dep. regir. and solr., Trinidad; serv. with Lond. Regt., 1915-19; marshal, sup. ct., Trinidad, Jan., 1926; ast. crown solr., May, 1931; regir. and marshal and regir.-gen., 1932; regir. and marshal, 1936.

**Version `col1936-L62654.v` — printed in editions [1936]:**

> McCRACKEN, ALBERT VICTOR NEILSON.—B. 1886; dep. regist. and asst. marshal, sup. ct., Trinidad, Jan., 1925; asst. crown solr., May, 1931; regist. and marshal and regist.-gen., 1932.

**Version `col1931-L66317.v` — printed in editions [1931, 1932]:**

> MOCRACKEN, ALBERT VICTOR NEILSON.—B. 1886; dep. registr. and asst. marshal, sup. ct., Trinidad, Jan., 1925; asst. crown solr., May, 1931.

**Version `col1928-L68042.v` — printed in editions [1928]:**

> McCRACKEN, ALBERT VICTOR NEILSON.—B. 1886; dep. regisr. and asst. marshal, sup. ct., Trinidad, Jan., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | serv. with Lond. Regt | — | [1940] |
| 1 | 1925 | dep. regist. and asst. marshal, sup. ct. | Trinidad | [1928, 1931, 1932, 1936] |
| 2 | 1926 | marshal, sup. ct. | Trinidad | [1940] |
| 3 | 1931 | ast. crown solr | Trinidad *(inherited from previous clause)* | [1931, 1932, 1936, 1940] |
| 4 | 1932 | regir. and marshal and regir.-gen | Trinidad *(inherited from previous clause)* | [1936, 1940] |
| 5 | 1936 | regir. and marshal | Trinidad *(inherited from previous clause)* | [1940] |

## Candidate stint `McCracken, A. V. N___Trinidad and Tobago___1928`

- Staff-list name: **McCracken, A. V. N** | colony: **Trinidad and Tobago** | listed 1928–1939 | editions [1928, 1931, 1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | A.V.N. McCracken | Deputy Registrar and Assistant Marshal | Judicial Department | — | — |
| 1931 | A. V. N. McCracken | Deputy Registrar-General | Registrar-General's Department | — | — |
| 1933 | A. V. N. McCracken | Registrar General, and Registrar and Marshal | Judicial Department | — | — |
| 1933 | A. V. N. McCracken | Registrar-General, Registrar and Marshal | Registrar-General's Department | — | — |
| 1934 | A. V. N. McCracken | Registrar General, Registrar and Marshal | Judicial Department | — | — |
| 1937 | A. V. N. McCracken | Registrar and Marshal | Judiciary | — | — |
| 1939 | A. V. N. McCracken | Registrar and Marshal | JUDICIARY | — | — |

### Deterministic checks: `mccracken_albert-victor-neilson_b1886` vs `McCracken, A. V. N___Trinidad and Tobago___1928`

- [PASS] surname_gate: bio 'McCRACKEN' vs stint 'McCracken, A. V. N' (exact)
- [PASS] initials: bio ['A', 'V', 'N'] ~ stint ['A', 'V', 'N']
- [PASS] age_gate: stint starts 1928, birth 1886 (age 42)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1939
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

