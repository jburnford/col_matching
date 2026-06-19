<!-- {"case_id": "case_lawes_w-e_b1916", "bio_ids": ["lawes_w-e_b1916"], "stint_ids": ["Lawes, W. E___Kenya___1949"]} -->
# Dossier case_lawes_w-e_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lawes_w-e_b1916`

- Printed name: **LAWES, W. E**
- Birth year: 1916 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L24884.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> LAWES, W. E.—b. 1916; ed. Gram. Sch., Burnley, and Medical Sch., Edin. Univ.; M.O., Ken., 1942; specialist anaesthetist, 1950; pubn. *Intermittent Positive Pressure Respiration in Polio-myelitis (B.M.J.)* (Jointly with J. R. Harries).

**Version `col1962-L23425.v` — printed in editions [1962, 1963, 1964]:**

> LAWES, W. E.—b. 1916; ed. Gram. Sch., Burnley, and Medical Sch., Edin. Univ.; M.O., Ken., 1942; specialist anaesthetist, 1950-63. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1950 | specialist anaesthetist | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Lawes, W. E___Kenya___1949`

- Staff-list name: **Lawes, W. E** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. E. Lawes | Medical Officer | Medical | — | — |
| 1950 | W. E. Lawes | Medical Officer | Medical | — | — |
| 1951 | W. E. Lawes | Medical Officer | Medical | — | — |

### Deterministic checks: `lawes_w-e_b1916` vs `Lawes, W. E___Kenya___1949`

- [PASS] surname_gate: bio 'LAWES' vs stint 'Lawes, W. E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 32 vs bar 60: 'specialist anaesthetist' ~ 'Medical Officer'
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

