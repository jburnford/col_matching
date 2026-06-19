<!-- {"case_id": "case_clayton_george-edward_b1896", "bio_ids": ["clayton_george-edward_b1896"], "stint_ids": ["Clayton, G. E___Straits Settlements___1925"]} -->
# Dossier case_clayton_george-edward_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Clayton, G. E___Straits Settlements___1925` is also gate-compatible with biography(ies) outside this case: ['clayton_gilbert_b1875'] (already linked elsewhere or filtered).

## Biography `clayton_george-edward_b1896`

- Printed name: **CLAYTON, GEORGE EDWARD**
- Birth year: 1896 (attested in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931])
- Appears in editions: [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1922-L51410.v` — printed in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]:**

> CLAYTON, GEORGE EDWARD, M.C.—B. 1896; ed. King's Schi., Canterbury, 1910-15; 2nd lieut., R.F.A., 13th Dec., 1915; served in France, 55th (West Lancs.) divn., 1917-18; Mily. Cross, Apr., 1918; served in Germany, 1919; demob., 1st Nov., 1919; cadet, F.M.S., Aug., 1920; attached to secretariat, Singapore, 1920; trans. to Penang, Jan., 1921; dep. registr., sup. ct., Penang, 29th May, 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | 2nd lieut., R.F.A | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 1 | 1917–1918 | served in France, 55th (West Lancs.) divn | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 2 | 1918 | Mily. Cross | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 3 | 1919 | served in Germany | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 4 | 1919 | demob | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 5 | 1920 | cadet | Federated Malay States | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 6 | 1920 | attached to secretariat | Singapore | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 7 | 1921 | trans. to Penang | Singapore *(inherited from previous clause)* | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |

## Candidate stint `Clayton, G. E___Straits Settlements___1925`

- Staff-list name: **Clayton, G. E** | colony: **Straits Settlements** | listed 1925–1932 | editions [1925, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | G. E. Clayton | Assistant District Judge | Colonial Secretary's Office | — | — |
| 1932 | G. E. Clayton | Second Magistrate | District and Police Courts | — | — |

### Deterministic checks: `clayton_george-edward_b1896` vs `Clayton, G. E___Straits Settlements___1925`

- [PASS] surname_gate: bio 'CLAYTON' vs stint 'Clayton, G. E' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1925, birth 1896 (age 29)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1932
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

