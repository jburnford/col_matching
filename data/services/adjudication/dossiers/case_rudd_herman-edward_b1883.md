<!-- {"case_id": "case_rudd_herman-edward_b1883", "bio_ids": ["rudd_herman-edward_b1883"], "stint_ids": ["Rudd, H. E___Cape of Good Hope___1905"]} -->
# Dossier case_rudd_herman-edward_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rudd_herman-edward_b1883`

- Printed name: **RUDD, HERMAN EDWARD**
- Birth year: 1883 (attested in editions [1937, 1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L64400.v` — printed in editions [1937, 1939, 1940]:**

> RUDD, HERMAN EDWARD.—B. 1883; joined Cape civ. surv., Nov., 1900; clk., P.M.G.'s dept., 1901; clk., office of registr. sup. ct., Cape Town, 1903; clk., atty.-gen.'s office, 1903; clk., audit office, Cape Town, 1906; clk., office of contr. and audr.-gen., 1910; 1st cls. clk., do., 1912; senr. clk., do., 1921; prin. clk., do., 1928; ch. clk., do., 1930; ch. inspr. (rev.), do., 1932; ch. inspr. (expend.), do., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | joined Cape civ. surv | — | [1937, 1939, 1940] |
| 1 | 1901 | clk., P.M.G.'s dept | — | [1937, 1939, 1940] |
| 2 | 1903 | clk., office of registr. sup. ct., Cape Town | Cape of Good Hope | [1937, 1939, 1940] |
| 3 | 1906 | clk., audit office, Cape Town | Cape of Good Hope | [1937, 1939, 1940] |
| 4 | 1910 | clk., office of contr. and audr.-gen | Cape of Good Hope *(inherited from previous clause)* | [1937, 1939, 1940] |
| 5 | 1912 | 1st cls. clk. | Dominions Office | [1937, 1939, 1940] |
| 6 | 1921 | senr. clk. | Dominions Office | [1937, 1939, 1940] |
| 7 | 1928 | prin. clk. | Dominions Office | [1937, 1939, 1940] |
| 8 | 1930 | ch. clk. | Dominions Office | [1937, 1939, 1940] |
| 9 | 1932 | ch. inspr. (rev.) | Dominions Office | [1937, 1939, 1940] |
| 10 | 1935 | ch. inspr. (expend.) | Dominions Office | [1937, 1939, 1940] |

## Candidate stint `Rudd, H. E___Cape of Good Hope___1905`

- Staff-list name: **Rudd, H. E** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. E. Rudd | Examiners of Accounts | Accounting Branch | — | — |
| 1906 | H. E. Rudd | Examiners of Accounts | Accounting Branch | — | — |
| 1907 | H. E. Rudd | Examiner | Control and Audit Office | — | — |
| 1909 | H. E. Rudd | Examiners | Control and Audit Office | — | — |

### Deterministic checks: `rudd_herman-edward_b1883` vs `Rudd, H. E___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'RUDD' vs stint 'Rudd, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1905, birth 1883 (age 22)
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1905-1909
- [FAIL] position_sim: best 46 vs bar 60: 'clk., office of contr. and audr.-gen' ~ 'Examiners of Accounts'
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

