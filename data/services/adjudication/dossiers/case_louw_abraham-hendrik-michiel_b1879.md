<!-- {"case_id": "case_louw_abraham-hendrik-michiel_b1879", "bio_ids": ["louw_abraham-hendrik-michiel_b1879"], "stint_ids": ["Louw, A. H. M___Cape of Good Hope___1906"]} -->
# Dossier case_louw_abraham-hendrik-michiel_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `louw_abraham-hendrik-michiel_b1879`

- Printed name: **LOUW, ABRAHAM HENDRIK MICHIEL**
- Birth year: 1879 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L68744.v` — printed in editions [1939]:**

> LOUW, ABRAHAM HENDRIK MICHIEL.—B. 1879; ed. Normal Coll., Cape Town, and pvt. tuition; Cape agrl. dept., 1896; sur.-gen's. office, 1905; Union lands dept., 1912; oh. clk., dept. of interior, 1928; asst. sec., S.W. Africa, 1935; under sec., dept. of int., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | Cape agrl. dept | Cape of Good Hope | [1939] |
| 1 | 1905 | sur.-gen's. office | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 2 | 1912 | Union lands dept | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 3 | 1928 | oh. clk., dept. of interior | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 4 | 1935 | asst. sec., S.W. Africa | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 5 | 1937 | under sec., dept. of int | Cape of Good Hope *(inherited from previous clause)* | [1939] |

## Candidate stint `Louw, A. H. M___Cape of Good Hope___1906`

- Staff-list name: **Louw, A. H. M** | colony: **Cape of Good Hope** | listed 1906–1909 | editions [1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | A. H. M. Louw | Clerk | Surveyor-General's Office | — | — |
| 1907 | A. H. M. Louw | Clerk | Surveyor-General's Office | — | — |
| 1908 | A. H. M. Louw | Clerk | Surveyor-General's Office | — | — |
| 1909 | A. H. M. Louw | Clerk | Surveyor-General's Office | — | — |

### Deterministic checks: `louw_abraham-hendrik-michiel_b1879` vs `Louw, A. H. M___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'LOUW' vs stint 'Louw, A. H. M' (exact)
- [PASS] initials: bio ['A', 'H', 'M'] ~ stint ['A', 'H', 'M']
- [PASS] age_gate: stint starts 1906, birth 1879 (age 27)
- [PASS] colony: 6 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1906-1909
- [FAIL] position_sim: best 32 vs bar 60: 'sur.-gen's. office' ~ 'Clerk'
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

