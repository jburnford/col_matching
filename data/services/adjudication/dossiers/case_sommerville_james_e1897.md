<!-- {"case_id": "case_sommerville_james_e1897", "bio_ids": ["sommerville_james_e1897"], "stint_ids": ["Sommerville, J___Transvaal___1906"]} -->
# Dossier case_sommerville_james_e1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sommerville_james_e1897'] carry a single initial only — the namesake trap applies.

## Biography `sommerville_james_e1897`

- Printed name: **SOMMERVILLE, JAMES**
- Birth year: not printed
- Honours: O.B.E
- Appears in editions: [1924, 1925, 1928, 1929, 1930, 1932]

### Verbatim printed entry text (OCR)

**Version `col1924-L58048.v` — printed in editions [1924, 1925, 1928, 1929, 1930, 1932]:**

> SOMMERVILLE, JAMES, O.B.E.—Ck., traffic dept., Cape, 20th Mar., 1897; clk., C. T. M. offices, Cape, 1st Oct., 1898; ch. clk., admstr.'s office, Transvaal, 1st Dec., 1900; sec., refugees aid dept., 1st Nov., 1901; sec., Transvaal immigrn. office, 1st Aug., 1903; ch. clk., lands dept., 1st May, 1904; under sec. for lands, Union of Africa, 1st June, 1917; sec. for lands, 1st Apr., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | Ck., traffic dept. | Cape of Good Hope | [1924, 1925, 1928, 1929, 1930, 1932] |
| 1 | 1898 | clk., C. T. M. offices | Cape of Good Hope | [1924, 1925, 1928, 1929, 1930, 1932] |
| 2 | 1900 | ch. clk., admstr.'s office | Transvaal | [1924, 1925, 1928, 1929, 1930, 1932] |
| 3 | 1901 | sec., refugees aid dept | Transvaal *(inherited from previous clause)* | [1924, 1925, 1928, 1929, 1930, 1932] |
| 4 | 1903 | sec., Transvaal immigrn. office | Transvaal | [1924, 1925, 1928, 1929, 1930, 1932] |
| 5 | 1904 | ch. clk., lands dept | Transvaal *(inherited from previous clause)* | [1924, 1925, 1928, 1929, 1930, 1932] |
| 6 | 1917 | under sec. for lands, Union of Africa | Transvaal *(inherited from previous clause)* | [1924, 1925, 1928, 1929, 1930, 1932] |
| 7 | 1921 | sec. for lands | Transvaal *(inherited from previous clause)* | [1924, 1925, 1928, 1929, 1930, 1932] |

## Candidate stint `Sommerville, J___Transvaal___1906`

- Staff-list name: **Sommerville, J** | colony: **Transvaal** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | J. Sommerville | Chief Clerk | Land Department | — | — |
| 1907 | J. Sommerville | Chief Clerk | Land Department | — | — |
| 1908 | J. Sommerville | Chief Clerk and Accountant | Land Department | — | — |

### Deterministic checks: `sommerville_james_e1897` vs `Sommerville, J___Transvaal___1906`

- [PASS] surname_gate: bio 'SOMMERVILLE' vs stint 'Sommerville, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Transvaal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1908
- [FAIL] position_sim: best 43 vs bar 60: 'ch. clk., lands dept' ~ 'Chief Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

