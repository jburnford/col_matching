<!-- {"case_id": "case_marsh_sydney-george_b1903", "bio_ids": ["marsh_sydney-george_b1903"], "stint_ids": ["Marsh, S. G___Uganda___1939"]} -->
# Dossier case_marsh_sydney-george_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `marsh_sydney-george_b1903`

- Printed name: **MARSH, Sydney George**
- Birth year: 1903 (attested in editions [1949, 1950])
- Appears in editions: [1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1949-L34177.v` — printed in editions [1949, 1950]:**

> MARSH, Sydney George.—b. 1903; ed. St. John's Sch., Hampton Wick; on mil. serv. 1939-42, Q.M.S.; clk., educ. dept., Uga., 1937; assessor, jt. inc. tax dept., Ken., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | clk., educ. dept. | Uganda | [1949, 1950] |
| 1 | 1942 | assessor, jt. inc. tax dept. | Kenya | [1949, 1950] |

## Candidate stint `Marsh, S. G___Uganda___1939`

- Staff-list name: **Marsh, S. G** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | S. G. Marsh | Clerk | Education | — | — |
| 1940 | S. G. Marsh | Clerks | Education | — | — |

### Deterministic checks: `marsh_sydney-george_b1903` vs `Marsh, S. G___Uganda___1939`

- [PASS] surname_gate: bio 'MARSH' vs stint 'Marsh, S. G' (exact)
- [PASS] initials: bio ['S', 'G'] ~ stint ['S', 'G']
- [PASS] age_gate: stint starts 1939, birth 1903 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 33 vs bar 60: 'clk., educ. dept.' ~ 'Clerk'
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

