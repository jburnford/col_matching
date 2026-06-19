<!-- {"case_id": "case_oakes_alfred-charles-george_b1878", "bio_ids": ["oakes_alfred-charles-george_b1878"], "stint_ids": ["Oakes, A. C. G___Cape of Good Hope___1899"]} -->
# Dossier case_oakes_alfred-charles-george_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `oakes_alfred-charles-george_b1878`

- Printed name: **OAKES, ALFRED CHARLES GEORGE**
- Birth year: 1878 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L69486.v` — printed in editions [1939]:**

> OAKES, ALFRED CHARLES GEORGE.—B. 1878; ed. privately; clk., surv.-gen'l. office, Cape Town, 1897; native affrs. dept., 1908; on active serv., 1917-18; mag., Taunye, Bechuanaland 1919; Sutherland, 1923; Willowmore, 1927; Craddock, 1929; Bethal, 1932; senr. addl. mag., Durban, 1932; mag., Potchefstroom, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | clk., surv.-gen'l. office, Cape Town | Cape of Good Hope | [1939] |
| 1 | 1908 | native affrs. dept | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 2 | 1919 | mag., Taunye | Bechuanaland | [1939] |
| 3 | 1923 | Sutherland | Bechuanaland *(inherited from previous clause)* | [1939] |
| 4 | 1927 | Willowmore | Bechuanaland *(inherited from previous clause)* | [1939] |
| 5 | 1929 | Craddock | Bechuanaland *(inherited from previous clause)* | [1939] |
| 6 | 1932 | Bethal | Bechuanaland *(inherited from previous clause)* | [1939] |
| 7 | 1936 | mag., Potchefstroom | Bechuanaland *(inherited from previous clause)* | [1939] |

## Candidate stint `Oakes, A. C. G___Cape of Good Hope___1899`

- Staff-list name: **Oakes, A. C. G** | colony: **Cape of Good Hope** | listed 1899–1909 | editions [1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | A. C. G. Oakes | Clerk | Surveyor-General's Office | — | — |
| 1900 | A. C. Oakes | Clerk | Surveyor-General's Office | — | — |
| 1905 | A. C. Oakes | Clerk | Surveyor-General's Office | — | — |
| 1906 | A. C. Oakes | Clerk | Surveyor-General's Office | — | — |
| 1907 | A. C. Oakes | Clerk | Surveyor-General's Office | — | — |
| 1908 | A. C. Oakes | Clerk | Surveyor-General's Office | — | — |
| 1909 | A. C. G. Oakes | Clerks | Native Affairs Branch | — | — |

### Deterministic checks: `oakes_alfred-charles-george_b1878` vs `Oakes, A. C. G___Cape of Good Hope___1899`

- [PASS] surname_gate: bio 'OAKES' vs stint 'Oakes, A. C. G' (exact)
- [PASS] initials: bio ['A', 'C', 'G'] ~ stint ['A', 'C', 'G']
- [PASS] age_gate: stint starts 1899, birth 1878 (age 21)
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1899-1909
- [FAIL] position_sim: best 24 vs bar 60: 'clk., surv.-gen'l. office, Cape Town' ~ 'Clerk'
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

