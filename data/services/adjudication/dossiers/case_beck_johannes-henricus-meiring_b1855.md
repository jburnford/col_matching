<!-- {"case_id": "case_beck_johannes-henricus-meiring_b1855", "bio_ids": ["beck_johannes-henricus-meiring_b1855"], "stint_ids": ["Beck, John___South Australia___1889"]} -->
# Dossier case_beck_johannes-henricus-meiring_b1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beck_johannes-henricus-meiring_b1855`

- Printed name: **BECK, JOHANNES HENRICUS MEIRING**
- Birth year: 1855 (attested in editions [1917, 1918, 1919])
- Honours: KT. BACH. (1911)
- Appears in editions: [1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1917-L47568.v` — printed in editions [1917, 1918, 1919]:**

> BECK, HON. SIR JOHANNES HENRICUS MEIRING, KT. BACH. (1911), M.D., F.R.S.E., J.P.—B. 1855; ed. Worcester Pub. Schl., Cape of Good Hope, S. African Coll., Univ. of Edinburgh, Berlin and Vienna; graduated in medicine, Edin. Univ., 1879; M.L.A., Worcester (Cape), 1898-1910; Cape of Good Hope deleg. to S. African national convention; mem. of coun., Cape Univ., 1888-1912; ex-pres., Cape medical coun.; senator, Union of S. Africa, since 1910, and chrmn. of comtees. of senate; min. of posts and telegraphs, Union of S. Africa, 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1879 | graduated in medicine | — | [1917, 1918, 1919] |
| 1 | 1888–1912 | mem. of coun. | Cape of Good Hope | [1917, 1918, 1919] |
| 2 | 1898–1910 | M.L.A. | Cape of Good Hope | [1917, 1918, 1919] |
| 3 | 1910 | senator | South Africa | [1917, 1918, 1919] |
| 4 | 1916–1916 | min. of posts and telegraphs | South Africa | [1917, 1918, 1919] |

## Candidate stint `Beck, John___South Australia___1889`

- Staff-list name: **Beck, John** | colony: **South Australia** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | John Beck | Vice-Consul | Foreign Consuls | — | — |
| 1890 | John Beck | Vice-Consul | Foreign Consuls | — | — |

### Deterministic checks: `beck_johannes-henricus-meiring_b1855` vs `Beck, John___South Australia___1889`

- [PASS] surname_gate: bio 'BECK' vs stint 'Beck, John' (exact)
- [PASS] initials: bio ['J', 'H', 'M'] ~ stint ['J']
- [PASS] age_gate: stint starts 1889, birth 1855 (age 34)
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

