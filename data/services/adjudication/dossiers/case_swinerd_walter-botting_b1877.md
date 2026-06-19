<!-- {"case_id": "case_swinerd_walter-botting_b1877", "bio_ids": ["swinerd_walter-botting_b1877"], "stint_ids": ["Swinerd, William B___Zanzibar___1911"]} -->
# Dossier case_swinerd_walter-botting_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `swinerd_walter-botting_b1877`

- Printed name: **SWINERD, Walter Botting**
- Birth year: 1877 (attested in editions [1917, 1918])
- Appears in editions: [1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1917-L53504.v` — printed in editions [1917, 1918]:**

> SWINERD, Walter Botting.—B. 1877; ed. Cranleigh, Surrey; asst. collr. of cust., Zanzibar 8th Feb., 1901; ag. collr. on several occasions ag. collr., Pemba, Jan. to Nov., 1903; ag. treas., Mar. and Apl., 1906; chief of ctn., May, 1906; ag. financial mem. of coun. and treas., Sep., 1908 to Feb., 1909; Dec., 1910 to May, 1911; and from Jan. to Sep., 1913; ag. treas. from May, 1916, to Feb., 1917; marshal of H.B.M. Court for Zanzibar (in Prize).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1901 | asst. collr. of cust. | Zanzibar | [1917, 1918] |
| 1 | 1903–1903 | ag. collr. | Pemba | [1917, 1918] |
| 2 | 1906–1906 | ag. treas. | — | [1917, 1918] |
| 3 | 1906–1906 | chief of ctn. | — | [1917, 1918] |
| 4 | 1908–1909 | ag. financial mem. of coun. and treas. | — | [1917, 1918] |
| 5 | 1910–1911 | ag. financial mem. of coun. and treas. | — | [1917, 1918] |
| 6 | 1913–1913 | ag. financial mem. of coun. and treas. | — | [1917, 1918] |
| 7 | 1916–1917 | ag. treas. | — | [1917, 1918] |

## Candidate stint `Swinerd, William B___Zanzibar___1911`

- Staff-list name: **Swinerd, William B** | colony: **Zanzibar** | listed 1911–1917 | editions [1911, 1912, 1913, 1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | W. B. Swinerd | Collector of Customs | — | — | — |
| 1912 | W. B. Swinerd | Collector of Customs | — | — | — |
| 1913 | W. B. Swinerd | Collector of Customs | — | — | — |
| 1914 | W. B. Swinerd | Collector of Customs | — | — | — |
| 1915 | W. B. Swinerd | Chief of Customs | Customs | — | — |
| 1917 | William B. Swinerd | Chief of Customs | Customs | — | — |

### Deterministic checks: `swinerd_walter-botting_b1877` vs `Swinerd, William B___Zanzibar___1911`

- [PASS] surname_gate: bio 'SWINERD' vs stint 'Swinerd, William B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1911, birth 1877 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1917
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

