<!-- {"case_id": "case_saunders_godfrey-estridge_b1884", "bio_ids": ["saunders_godfrey-estridge_b1884"], "stint_ids": ["Saunders, G___Hong Kong___1929"]} -->
# Dossier case_saunders_godfrey-estridge_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Saunders, G___Hong Kong___1929` is also gate-compatible with biography(ies) outside this case: ['saunders_a-r-g_b1908', 'saunders_george-francis-thomas_b1896', 'saunders_reginald-g_e1898'] (already linked elsewhere or filtered).

## Biography `saunders_godfrey-estridge_b1884`

- Printed name: **SAUNDERS, GODFREY ESTRIDGE**
- Birth year: 1884 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70416.v` — printed in editions [1939, 1940]:**

> SAUNDERS, GODFREY ESTRIDGE.—B. 1884; offr. of cust., Cape Town, 1901; 1st grade examnt., Mossel Bay, 1915; prin. clk., Pretoria, 1923; senr. inspir., Johannesburg, 1931; surv., cust., Port Elizabeth, 1933; investigation offr., London, 1933; ch. inspir., Pretoria, 1936; asst. dep. commr., Pretoria, 1937; dep. commr., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | offr. of cust., Cape Town | Cape of Good Hope | [1939, 1940] |
| 1 | 1915 | 1st grade examnt., Mossel Bay | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1923 | prin. clk., Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1931 | senr. inspir., Johannesburg | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1933 | surv., cust., Port Elizabeth | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1936 | ch. inspir., Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |
| 6 | 1937 | asst. dep. commr., Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |
| 7 | 1938 | dep. commr | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Saunders, G___Hong Kong___1929`

- Staff-list name: **Saunders, G** | colony: **Hong Kong** | listed 1929–1936 | editions [1929, 1930, 1931, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | G. Saunders | Station Officer | Fire Brigade | — | — |
| 1930 | G. Saunders | Station Officer | Fire Brigade | — | — |
| 1931 | G. Saunders | Station Officer | Fire Brigade | — | — |
| 1932 | G. Saunders | Station Officer | Fire Brigade | — | — |
| 1934 | G. Saunders | Station Officer | Fire Brigade | — | — |
| 1936 | G. Saunders | Station Officer | Fire Brigade | — | — |

### Deterministic checks: `saunders_godfrey-estridge_b1884` vs `Saunders, G___Hong Kong___1929`

- [PASS] surname_gate: bio 'SAUNDERS' vs stint 'Saunders, G' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G']
- [PASS] age_gate: stint starts 1929, birth 1884 (age 45)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1936
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

