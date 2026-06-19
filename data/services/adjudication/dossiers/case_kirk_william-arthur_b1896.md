<!-- {"case_id": "case_kirk_william-arthur_b1896", "bio_ids": ["kirk_william-arthur_b1896"], "stint_ids": ["Kirk, A___Hong Kong___1922"]} -->
# Dossier case_kirk_william-arthur_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kirk_william-arthur_b1896`

- Printed name: **KIRK, WILLIAM ARTHUR**
- Birth year: 1896 (attested in editions [1939, 1940])
- Honours: A.M.I.C.E
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68236.v` — printed in editions [1939, 1940]:**

> KIRK, WILLIAM ARTHUR, A.M.I.C.E., Chtd. Civ. Engrnr.—B. 1896; ed. Sleaford Gram. Sch., Leeds Modern Sch., Leeds Univ.; ast. engrnr., P.W.D., Malaya, May, 1923; ex. engrnr., May, 1932; ag. sr. ex. engrnr., Apr., 1936; snr. ex. engrnr., Feb., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | ast. engrnr., P.W.D. | Malaya | [1939, 1940] |
| 1 | 1932 | ex. engrnr | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1936 | ag. sr. ex. engrnr | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1938 | snr. ex. engrnr | Malaya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Kirk, A___Hong Kong___1922`

- Staff-list name: **Kirk, A** | colony: **Hong Kong** | listed 1922–1928 | editions [1922, 1923, 1924, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. Kirk | Engineer | General Staff | — | — |
| 1923 | A. Kirk | Engineers | General Staff | — | — |
| 1924 | A. Kirk | Engineers | General Staff | — | — |
| 1925 | A. Kirk | Engineer | Resumptions | — | — |
| 1927 | A. Kirk | Engineers | Resumptions | — | — |
| 1928 | A. Kirk | Engineer-in-Charge | Resumptions | — | — |

### Deterministic checks: `kirk_william-arthur_b1896` vs `Kirk, A___Hong Kong___1922`

- [PASS] surname_gate: bio 'KIRK' vs stint 'Kirk, A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1928
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

