<!-- {"case_id": "case_apthorpe_mabmaduke-gwin_b1875", "bio_ids": ["apthorpe_mabmaduke-gwin_b1875"], "stint_ids": ["Athorp, M. G___Cape of Good Hope___1906"]} -->
# Dossier case_apthorpe_mabmaduke-gwin_b1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `apthorpe_mabmaduke-gwin_b1875`

- Printed name: **APTHORPE, MABMADUKE GWIN**
- Birth year: 1875 (attested in editions [1932, 1935])
- Appears in editions: [1932, 1935]

### Verbatim printed entry text (OCR)

**Version `col1932-L58027.v` — printed in editions [1932, 1935]:**

> APTHORPE, MABMADUKE GWIN, B.A.—B. 1875; ed. Malvern and Queen's Coll., Cambridge; clk., atty-gen.'s office, Cape Town, Sept., 1900; clk., survr.-gen.'s office, Feb., 1905; clk., treas. and pvtc. sec. to prime min., Apr., 1909; ag. prin. clk., P.W.D., May, 1910; prin. clk., native affrs. dept., June, 1910; on active serv. with E. African expd., forces, 1916-17; ag. ch. clk. and ag. undersec. for native affrs., 1917; mag., Lady Frere, May, 1918; do., Kentani, June, 1923; ch. clk., ch. mag.'s office, Umtata, and sec. and treas., Transkeian Territories and Pondoland gen. couns., Dec., 1925; ch. native comsnr., Ciakel, Oct., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | clk., atty-gen.'s office, Cape Town | Cape of Good Hope | [1932, 1935] |
| 1 | 1905 | clk., survr.-gen.'s office | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |
| 2 | 1909 | clk., treas. and pvtc. sec. to prime min | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |
| 3 | 1910 | ag. prin. clk., P.W.D | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |
| 4 | 1917 | ag. ch. clk. and ag. undersec. for native affrs | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |
| 5 | 1918 | mag., Lady Frere | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |
| 6 | 1923 | do., Kentani | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |
| 7 | 1925 | ch. clk., ch. mag.'s office, Umtata, and sec. and treas., Transkeian Territories and Pondoland gen. couns | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |
| 8 | 1928 | ch. native comsnr., Ciakel | Cape of Good Hope *(inherited from previous clause)* | [1932, 1935] |

## Candidate stint `Athorp, M. G___Cape of Good Hope___1906`

- Staff-list name: **Athorp, M. G** | colony: **Cape of Good Hope** | listed 1906–1908 | editions [1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | M. G. Athorp | Clerk | Surveyor-General's Office | — | — |
| 1908 | M. G. Athorp | Clerk | Surveyor-General's Office | — | — |

### Deterministic checks: `apthorpe_mabmaduke-gwin_b1875` vs `Athorp, M. G___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'APTHORPE' vs stint 'Athorp, M. G' (fuzzy:2)
- [PASS] initials: bio ['M', 'G'] ~ stint ['M', 'G']
- [PASS] age_gate: stint starts 1906, birth 1875 (age 31)
- [PASS] colony: 9 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1906-1908
- [FAIL] position_sim: best 32 vs bar 60: 'clk., survr.-gen.'s office' ~ 'Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

