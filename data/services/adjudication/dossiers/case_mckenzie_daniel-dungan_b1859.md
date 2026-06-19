<!-- {"case_id": "case_mckenzie_daniel-dungan_b1859", "bio_ids": ["mckenzie_daniel-dungan_b1859"], "stint_ids": ["McKenzie, North & Victoria D. D___Canada___1918"]} -->
# Dossier case_mckenzie_daniel-dungan_b1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mckenzie_daniel-dungan_b1859`

- Printed name: **MCKENZIE, DANIEL DUNGAN**
- Birth year: 1859 (attested in editions [1922, 1924, 1925, 1927])
- Appears in editions: [1922, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1922-L54415.v` — printed in editions [1922, 1924, 1925, 1927]:**

> MCKENZIE, HON. DANIEL DUNGAN.—B. 1859; ed. pub. schl. and Sydney acad.; barrister; mayor of N. Sydney, N.S., for five consecutive years; judge, county ct. dist. No. 7, N.S., 1906-8; el. to leg. ass., N.S., 1900 and 1901; el. to H.C., 1904; re-el., g.e., 1908, 1911, 1917 and 1921; leader of opposition in H.C. after the death of Sir Wilfred Laurier until end of 2nd sess., 1919; solr.-gen. in King admtn., 29th Dec., 1921; judge, sup. ct., Nova Scotia, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1901 | el. to leg. ass. | Nova Scotia | [1922, 1924, 1925, 1927] |
| 1 | 1904–1904 | el. to H.C. | — | [1922, 1924, 1925, 1927] |
| 2 | 1906–1908 | judge, county ct. dist. No. 7 | Nova Scotia | [1922, 1924, 1925, 1927] |
| 3 | 1908–1921 | re-el., g.e. | — | [1922, 1924, 1925, 1927] |
| 4 | 1921–1921 | solr.-gen. in King admtn. | — | [1922, 1924, 1925, 1927] |
| 5 | 1923–1923 | judge, sup. ct. | Nova Scotia | [1922, 1924, 1925, 1927] |
| 6 | ?–1919 | leader of opposition in H.C. after the death of Sir Wilfred Laurier | — | [1922, 1924, 1925, 1927] |

## Candidate stint `McKenzie, North & Victoria D. D___Canada___1918`

- Staff-list name: **McKenzie, North & Victoria D. D** | colony: **Canada** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | North & Victoria D. D. McKenzie | Member of Parliament | House of Commons | — | — |
| 1919 | North & Victoria D. D. McKenzie | Calgary | House of Commons | — | — |

### Deterministic checks: `mckenzie_daniel-dungan_b1859` vs `McKenzie, North & Victoria D. D___Canada___1918`

- [PASS] surname_gate: bio 'MCKENZIE' vs stint 'McKenzie, North & Victoria D. D' (exact)
- [PASS] initials: bio ['D', 'D'] ~ stint ['N', 'V', 'D', 'D']
- [PASS] age_gate: stint starts 1918, birth 1859 (age 59)
- [PASS] colony: 3 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
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

