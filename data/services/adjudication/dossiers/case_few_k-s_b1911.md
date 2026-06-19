<!-- {"case_id": "case_few_k-s_b1911", "bio_ids": ["few_k-s_b1911"], "stint_ids": ["Few, K. S___Fiji___1965"]} -->
# Dossier case_few_k-s_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `few_k-s_b1911`

- Printed name: **FEW, K. S**
- Birth year: 1911 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Terminal: retired 1964 — “retd. apptd. registr.-gen. and registr. titles, Fiji, 1964.”
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L21030.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> FEW, K. S., T.D.—b. 1911; ed. Mill Hill Sch., and King’s Coll., Camb.; solr., notary publ.; mil. serv., 1939-46; cr. coun., Ken., 1950; resdt. mag., 1953; senr. dep. registr., 1960; registr. sup. ct., 1963; retd. apptd. registr.-gen. and registr. titles, Fiji, 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | cr. coun. | Kenya | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | resdt. mag | Kenya *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1960 | senr. dep. registr | Kenya *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1963 | registr. sup. ct | Kenya *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Few, K. S___Fiji___1965`

- Staff-list name: **Few, K. S** | colony: **Fiji** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | K. S. Few | Registrar-General and Registrar of Titles | Civil Establishment | — | — |
| 1966 | K. S. Few | Registrar-General and Registrar of Titles | Civil Establishment | — | — |

### Deterministic checks: `few_k-s_b1911` vs `Few, K. S___Fiji___1965`

- [PASS] surname_gate: bio 'FEW' vs stint 'Few, K. S' (exact)
- [PASS] initials: bio ['K', 'S'] ~ stint ['K', 'S']
- [PASS] age_gate: stint starts 1965, birth 1911 (age 54)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

