<!-- {"case_id": "case_woods_g_b1906", "bio_ids": ["woods_g_b1906"], "stint_ids": ["Woods, William G___Sierra Leone___1949"]} -->
# Dossier case_woods_g_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['woods_g_b1906'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Woods, William G___Sierra Leone___1949` is also gate-compatible with biography(ies) outside this case: ['woods_wilfred-george_b1899'] (already linked elsewhere or filtered).

## Biography `woods_g_b1906`

- Printed name: **WOODS, G**
- Birth year: 1906 (attested in editions [1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1954-L22970.v` — printed in editions [1954, 1955, 1956, 1957]:**

> WOODS, G.—b. 1906; ed. Gram. Sch., Sligo, Mountjoy Sch. and Trinity Coll., Dublin; mil. serv., 1940-45; asst. mstr., F.M.S., 1930; headmstr., gov't. English sch., Muar, 1946; supt., educ., Johore, 1949; senr. inspr., schs., Selangor, 1951; dep. dir., educ., 1952.

**Version `col1953-L19653.v` — printed in editions [1953]:**

> WOODS, G.—b. 1906; ed. Gram. Sch., Sligo, Mountjoy Sch. and Trinity Coll., Dublin; mil. serv., 1940–45; asst. mstr., F.M.S., 1930; headmstr., 1946; ag. dep. dir., educ., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | asst. mstr. | Federated Malay States | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1946 | headmstr., gov't. English sch., Muar | Federated Malay States *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1949 | supt., educ. | Johore | [1954, 1955, 1956, 1957] |
| 3 | 1951 | senr. inspr., schs., Selangor | Johore *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 4 | 1952 | dep. dir., educ | Johore *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Woods, William G___Sierra Leone___1949`

- Staff-list name: **Woods, William G** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | William G. Woods | Works Manager | Railway | — | — |
| 1950 | W. G. Woods | Works Manager | Locomotive | — | — |
| 1951 | W. G. Woods | Works Manager | Locomotive | — | — |

### Deterministic checks: `woods_g_b1906` vs `Woods, William G___Sierra Leone___1949`

- [PASS] surname_gate: bio 'WOODS' vs stint 'Woods, William G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

