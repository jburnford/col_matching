<!-- {"case_id": "case_mclowane_percy-alexander_b1884", "bio_ids": ["mclowane_percy-alexander_b1884"], "stint_ids": ["McCowan, A___Australia___1913", "McCowan, A___Victoria___1900"]} -->
# Dossier case_mclowane_percy-alexander_b1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mclowane_percy-alexander_b1884`

- Printed name: **MCLOWANE, PERCY ALEXANDER**
- Birth year: 1884 (attested in editions [1940])
- Honours: Kt. Bach (1939)
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66365.v` — printed in editions [1940]:**

> MCLOWANE, SIR PERCY ALEXANDER, Kt. Bach. (1939), B.A. (Hons.), LL.D.—B. 1884; ed. Campbell Coll., Belfast and Trinity Coll., Dublin; called to Irish bar (King's Inn), 1908; Alberta bar, 1913; temp. lieut., Royal Irish Rifles, B.E.F., 1916-19; stip. mag. and coroner, 2nd and 3rd dists., St. Lucia, 1920; crown counsel, Kenya, Apr., 1923; senr. crown coun., Jan., 1926; ag. solr.-gen., Kenya and M.C., Oct., 1925 to Mar., 1926; atty.-gen., Fiji, 1927; K.C., N. Ireland, Feb., 1929; dep. pub. pros., Singapore, 1930; atty.-gen., S.S., Sept., 1933; ch. just., S.S., 1936; prepared revd. edn., Laws of Straits Settlements, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | called to Irish bar (King's Inn) | — | [1940] |
| 1 | 1913 | Alberta bar | — | [1940] |
| 2 | 1916–1919 | temp. lieut., Royal Irish Rifles, B.E.F | — | [1940] |
| 3 | 1920 | stip. mag. and coroner, 2nd and 3rd dists. | St. Lucia | [1940] |
| 4 | 1923 | crown counsel | Kenya | [1940] |
| 5 | 1925–1926 | ag. solr.-gen., Kenya and M.C | Kenya | [1940] |
| 6 | 1926 | senr. crown coun | Kenya *(inherited from previous clause)* | [1940] |
| 7 | 1927 | atty.-gen. | Fiji | [1940] |
| 8 | 1929 | K.C., N. Ireland | Fiji *(inherited from previous clause)* | [1940] |
| 9 | 1930 | dep. pub. pros. | Singapore | [1940] |
| 10 | 1933 | atty.-gen. | Straits Settlements | [1940] |
| 11 | 1936 | ch. just. | Straits Settlements | [1940] |

## Candidate stint `McCowan, A___Australia___1913`

- Staff-list name: **McCowan, A** | colony: **Australia** | listed 1913–1918 | editions [1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | A. McCowan | Skilled Member | — | — | — |
| 1918 | A. McCowan | Skilled Member | Court of Marine Inquiry | — | — |

### Deterministic checks: `mclowane_percy-alexander_b1884` vs `McCowan, A___Australia___1913`

- [PASS] surname_gate: bio 'MCLOWANE' vs stint 'McCowan, A' (fuzzy:2)
- [PASS] initials: bio ['P', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1913, birth 1884 (age 29)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McCowan, A___Victoria___1900`

- Staff-list name: **McCowan, A** | colony: **Victoria** | listed 1900–1917 | editions [1900, 1905, 1906, 1907, 1908, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | A. McCowan | Skilled Member | Court of Marine Inquiry | — | — |
| 1905 | A. McCowan | Skilled Member | Court of Marine Inquiry | — | — |
| 1906 | A. McCowan | Skilled Member | Court of Marine Inquiry | — | — |
| 1907 | A. McCowan | Skilled Member | Court of Marine Inquiry | — | — |
| 1908 | A. McCowan | Skilled Member | Court of Marine Inquiry | — | — |
| 1917 | A. McCowan | Skilled Member | Court of Marine Inquiry | — | — |

### Deterministic checks: `mclowane_percy-alexander_b1884` vs `McCowan, A___Victoria___1900`

- [PASS] surname_gate: bio 'MCLOWANE' vs stint 'McCowan, A' (fuzzy:2)
- [PASS] initials: bio ['P', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1900, birth 1884 (age 16)
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1917
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

