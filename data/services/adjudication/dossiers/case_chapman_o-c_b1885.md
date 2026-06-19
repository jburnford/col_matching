<!-- {"case_id": "case_chapman_o-c_b1885", "bio_ids": ["chapman_o-c_b1885"], "stint_ids": ["Chapman, O___South Africa___1914"]} -->
# Dossier case_chapman_o-c_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chapman_o-c_b1885`

- Printed name: **CHAPMAN, O. C.**
- Birth year: 1885 (attested in editions [1925])
- Honours: O.B.E.
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L54739.v` — printed in editions [1925]:**

> CHAPMAN, O. C., O.B.E.—B. 1885; schol., Westminster Schol., 1890; Christ Ch., Oxford (exhbr.), 1903; B.A., 1906; apptd. after compet. exam.; asst. survr., G.P.O., 1910; transf. to R.O., Jan., 1911; lent to cust. and excise, 1914; lent to B. of T. and apptd. asst. sec. and later sec. of Comm. Internat. de Ravitaillement, 1915; sp. of Comm. on Allied Maritime Transport Comtee. and on Russian Transport Comtee.; awarded, Corona d’Italia (cavaliere), St. Anne of Russia (3rd cls.), Leopold of Belgium (chevalier); sent to Paris to assist in winding up Paris office of Miny. of Munitions, 1919; later in ch., Paris office; Br. sec. to raw materials sec., Sup. Econ. Council, 1920; asst. prin., C.O., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | asst. survr. | G.P.O. | [1925] |
| 1 | 1911 | transf. to R.O. | — | [1925] |
| 2 | 1914 | lent to cust. and excise | — | [1925] |
| 3 | 1915 | lent to B. of T. and apptd. asst. sec. and later sec. of Comm. Internat. de Ravitaillement | — | [1925] |
| 4 | 1919 | sent to Paris to assist in winding up Paris office of Miny. of Munitions | Paris | [1925] |
| 5 | 1920 | Br. sec. to raw materials sec., Sup. Econ. Council | — | [1925] |
| 6 | 1923 | asst. prin. | C.O. | [1925] |
| 7 | ? | apptd. | — | [1925] |
| 8 | ? | later in ch., Paris office | Paris | [1925] |

## Candidate stint `Chapman, O___South Africa___1914`

- Staff-list name: **Chapman, O** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | O. Chapman | Senior Clerk | Controller and Auditor-General's Department | — | — |
| 1918 | O. Chapman | Principal Clerks | Controller and Auditor-General's Department | — | — |

### Deterministic checks: `chapman_o-c_b1885` vs `Chapman, O___South Africa___1914`

- [PASS] surname_gate: bio 'CHAPMAN' vs stint 'Chapman, O' (exact)
- [PASS] initials: bio ['O', 'C'] ~ stint ['O']
- [PASS] age_gate: stint starts 1914, birth 1885 (age 29)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

