<!-- {"case_id": "case_coutts_p-g_b1924", "bio_ids": ["coutts_p-g_b1924"], "stint_ids": ["Coutts, P. G___Uganda___1949"]} -->
# Dossier case_coutts_p-g_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coutts_p-g_b1924`

- Printed name: **COUTTS, P. G**
- Birth year: 1924 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: M.B.E (1955)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L22195.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> COUTTS, P. G., M.B.E. (1955).—b. 1924; ed. Fettes Coll., Edin., and St. Andrews Univ.; mil. serv., 1943-46, f/o; cadet, Uga., 1948; D.O., 1950; prin. Nsamizi training centre, 1955; dep. estab. sec., 1957; estab. sec., 1962-63. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | cadet | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1950 | cadet | Dominions Office | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1955 | prin. Nsamizi training centre | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1957 | dep. estab. sec | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1962–1963 | estab. sec | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Coutts, P. G___Uganda___1949`

- Staff-list name: **Coutts, P. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. G. Coutts | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | P. G. Coutts | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `coutts_p-g_b1924` vs `Coutts, P. G___Uganda___1949`

- [PASS] surname_gate: bio 'COUTTS' vs stint 'Coutts, P. G' (exact)
- [PASS] initials: bio ['P', 'G'] ~ stint ['P', 'G']
- [PASS] age_gate: stint starts 1949, birth 1924 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 17 vs bar 60: 'cadet' ~ 'District Officers and Assistant District Officers'
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

