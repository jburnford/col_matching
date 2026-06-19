<!-- {"case_id": "case_jansen_francois-johannes_b1869", "bio_ids": ["jansen_francois-johannes_b1869"], "stint_ids": ["Jansen, F. J___Cape of Good Hope___1905"]} -->
# Dossier case_jansen_francois-johannes_b1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jansen_francois-johannes_b1869`

- Printed name: **JANSEN, FRANCOIS JOHANNES**
- Birth year: 1869 (attested in editions [1925, 1927, 1928, 1929])
- Appears in editions: [1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1925-L56843.v` — printed in editions [1925, 1927, 1928, 1929]:**

> JANSEN, FRANCOIS JOHANNES.—B. 1869; ed. Graaff Reinet Coll.; mag.'s clk., Fraserburg, Feb., 1889; Beaconsfield, Jan., 1890; examr. of accts., C.O., Oct., 1892; civ. comntr.'s clk. and asst. mag., Barkly West, Dec., 1894; Aliwal North, May, 1895; Dordrecht, July, 1895; clk. and paymr., Cape pol., Kimberley, Nov., 1897; acct., plague admnstr., Apr., 1901; acct., guardians fund, Mar., 1902; sub-comntr., war losses compensation comntr., Aug., 1902; regisr., sup. ct., Eastern dists., Apr., 1904; civ. comntr., and res. mag., Murray'sburg, Oct., 1907; Victoria West, Dec., 1910; ch. clk., dept. of just., Sept., 1917; civ. comntr., and mag., Uitenhage, Feb., 1923; East London, Feb., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | mag.'s clk., Fraserburg | — | [1925, 1927, 1928, 1929] |
| 1 | 1890 | Beaconsfield | — | [1925, 1927, 1928, 1929] |
| 2 | 1892 | examr. of accts. | Colonial Office | [1925, 1927, 1928, 1929] |
| 3 | 1894 | civ. comntr.'s clk. and asst. mag., Barkly West | Colonial Office *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 4 | 1895 | Aliwal North | Colonial Office *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 5 | 1897 | clk. and paymr., Cape pol., Kimberley | Colonial Office *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 6 | 1901 | acct., plague admnstr | Colonial Office *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 7 | 1902 | acct., guardians fund | Colonial Office *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 8 | 1904 | regisr., sup. ct., Eastern dists | Colonial Office *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 9 | 1907 | civ. comntr., and res. mag., Murray'sburg | Colonial Office *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 10 | 1910 | Victoria West | Victoria | [1925, 1927, 1928, 1929] |
| 11 | 1917 | ch. clk., dept. of just | Victoria *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 12 | 1923 | civ. comntr., and mag., Uitenhage | Victoria *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |
| 13 | 1924 | East London | Victoria *(inherited from previous clause)* | [1925, 1927, 1928, 1929] |

## Candidate stint `Jansen, F. J___Cape of Good Hope___1905`

- Staff-list name: **Jansen, F. J** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | F. J. Jansen | Registrar | Eastern Districts Court | — | — |
| 1906 | F. J. Jansen | Registrar | Eastern Districts Court, Grahamstown | — | — |
| 1907 | F. J. Jansen | Registrar | Eastern Districts Court, Grahamstown | — | — |
| 1909 | F. J. Jansen | C.C. and R.M. | Division Of Murraysburg. | — | — |

### Deterministic checks: `jansen_francois-johannes_b1869` vs `Jansen, F. J___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'JANSEN' vs stint 'Jansen, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1905, birth 1869 (age 36)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

