<!-- {"case_id": "case_oliphant_george-mitchell_b1905", "bio_ids": ["oliphant_george-mitchell_b1905", "oliphant_grey_e1925"], "stint_ids": ["Oliphant, G. M___Northern Rhodesia___1936"]} -->
# Dossier case_oliphant_george-mitchell_b1905

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['oliphant_grey_e1925'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Oliphant, G. M___Northern Rhodesia___1936'] have more than one claimant biography in this case.

## Biography `oliphant_george-mitchell_b1905`

- Printed name: **OLIPHANT, GEORGE MITCHELL**
- Birth year: 1905 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69531.v` — printed in editions [1939, 1940]:**

> OLIPHANT, GEORGE MITCHELL.—B. 1905; ed. Morgan Acad., Dundee and Glasgow Univ.; admitted solr., Jan., 1926; ast. land offr., Tanganyika Territory, 1930; ast. admr.-gen. and offr. recr., N. Rhodesia, 1935; regtr., high ct., sheriff, regtr., companies, patents, trade marks and designs, regtr.-gen., births, deaths and marriages, 1936; admstv. gen. and offr. recr., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | admitted solr | — | [1939, 1940] |
| 1 | 1930 | ast. land offr., Tanganyika Territory | Tanganyika | [1939, 1940] |
| 2 | 1935 | ast. admr.-gen. and offr. recr., N. Rhodesia | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1936 | regtr., high ct., sheriff, regtr., companies, patents, trade marks and designs, regtr.-gen., births, deaths and marriages | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1937 | admstv. gen. and offr. recr | Tanganyika *(inherited from previous clause)* | [1939, 1940] |

## Biography `oliphant_grey_e1925`

- Printed name: **OLIPHANT, GREY**
- Birth year: not printed
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L63712.v` — printed in editions [1937]:**

> OLIPHANT, GREY, 1925; gov., Gambia, 1930; ed. Morgan Acad., ch., Cyprus, 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925–1925 | — | — | [1937] |
| 1 | 1930–1930 | gov. | Gambia | [1937] |
| 2 | 1933–1933 | ch. | Cyprus | [1937] |

## Candidate stint `Oliphant, G. M___Northern Rhodesia___1936`

- Staff-list name: **Oliphant, G. M** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. M. Oliphant | Registrar of the High Court | Judicial | — | — |
| 1937 | G. M. Oliphant | Registrar of the High Court | Judicial | — | — |
| 1939 | G. M. Oliphant | Administrator-General and Official Receiver | Administrator-General | — | — |
| 1940 | G. M. Oliphant | Administrator-General and Official Receiver | Administrator-General | — | — |

### Deterministic checks: `oliphant_george-mitchell_b1905` vs `Oliphant, G. M___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'OLIPHANT' vs stint 'Oliphant, G. M' (exact)
- [PASS] initials: bio ['G', 'M'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `oliphant_grey_e1925` vs `Oliphant, G. M___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'OLIPHANT' vs stint 'Oliphant, G. M' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

