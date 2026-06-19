<!-- {"case_id": "case_durnford_c-c_e1863", "bio_ids": ["durnford_c-c_e1863"], "stint_ids": ["Durnford, C. C___Ceylon___1877"]} -->
# Dossier case_durnford_c-c_e1863

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `durnford_c-c_e1863`

- Printed name: **DURNFORD, C. C**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27287.v` — printed in editions [1883]:**

> DURNFORD, CAPT. C. C.—Deputy assistant-commissary, Kandy, Ceylon, 1863; deputy post-master-general, Kandy, 1866.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863 | Deputy assistant-commissary, Kandy | Ceylon | [1883] |
| 1 | 1866 | deputy post-master-general, Kandy | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Durnford, C. C___Ceylon___1877`

- Staff-list name: **Durnford, C. C** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. C. Durnford | Deputy Postmaster-General, Central Province | Post-Office | — | — |
| 1878 | C. C. Durnford | Deputy Postmaster-General | Post-Office | — | — |
| 1879 | C. C. Durnford | Deputy Postmaster-General | Post-Office | — | — |
| 1880 | C. C. Durnford | Deputy Postmaster-General, Central Province | Post-Office | — | — |

### Deterministic checks: `durnford_c-c_e1863` vs `Durnford, C. C___Ceylon___1877`

- [PASS] surname_gate: bio 'DURNFORD' vs stint 'Durnford, C. C' (exact)
- [PASS] initials: bio ['C', 'C'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 100 vs bar 60: 'deputy post-master-general, Kandy' ~ 'Deputy Postmaster-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

