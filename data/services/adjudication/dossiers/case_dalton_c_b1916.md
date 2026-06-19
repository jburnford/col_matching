<!-- {"case_id": "case_dalton_c_b1916", "bio_ids": ["dalton_c_b1916"], "stint_ids": ["Dalton, L. C___Ceylon___1934"]} -->
# Dossier case_dalton_c_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dalton_c_b1916'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Dalton, L. C___Ceylon___1934` is also gate-compatible with biography(ies) outside this case: ['dalton_llewelyn-chisholm_e1901'] (already linked elsewhere or filtered).

## Biography `dalton_c_b1916`

- Printed name: **DALTON, C**
- Birth year: 1916 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L18812.v` — printed in editions [1963, 1964, 1965, 1966]:**

> DALTON, C.—b. 1916; ed. trg. ship "Mercury"; mil. serv., 1938-46; dist. asst., N. Rhod., 1952; senr. dist. asst., 1957; comm. devel. offr., 1960. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | dist. asst. | Northern Rhodesia | [1963, 1964, 1965, 1966] |
| 1 | 1957 | senr. dist. asst | Northern Rhodesia *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1960 | comm. devel. offr | Northern Rhodesia *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Dalton, L. C___Ceylon___1934`

- Staff-list name: **Dalton, L. C** | colony: **Ceylon** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | L. C. Dalton | Puise Justice | Supreme Court | — | — |
| 1936 | L. C. Dalton | Senior Puine Justice | Supreme Court | — | — |

### Deterministic checks: `dalton_c_b1916` vs `Dalton, L. C___Ceylon___1934`

- [PASS] surname_gate: bio 'DALTON' vs stint 'Dalton, L. C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['L', 'C']
- [PASS] age_gate: stint starts 1934, birth 1916 (age 18)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1936
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

