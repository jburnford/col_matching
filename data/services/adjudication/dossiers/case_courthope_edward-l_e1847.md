<!-- {"case_id": "case_courthope_edward-l_e1847", "bio_ids": ["courthope_edward-l_e1847"], "stint_ids": ["Courthope, E. L___Western Australia___1877", "Courthope, E. L___Western Australia___1889"]} -->
# Dossier case_courthope_edward-l_e1847

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `courthope_edward-l_e1847`

- Printed name: **COURTHOPE, EDWARD L**
- Birth year: not printed
- Appears in editions: [1883, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L26973.v` — printed in editions [1883, 1888, 1889, 1890]:**

> COURTHOPE, EDWARD L.—Clerk in audit office, Western Australia, 1847; secretary to board of education, 1854; acting auditor-general, 1863; resumed duties as clerk in audit office, 1865; registrar-general, 1871; auditor-general, 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1847 | Clerk in audit office | Western Australia | [1883, 1888, 1889, 1890] |
| 1 | 1854 | secretary to board of education | Western Australia *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 2 | 1863 | acting auditor-general | Western Australia *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 3 | 1865 | resumed duties as clerk in audit office | Western Australia *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 4 | 1871 | registrar-general | Western Australia *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 5 | 1872 | auditor-general | Western Australia *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |

## Candidate stint `Courthope, E. L___Western Australia___1877`

- Staff-list name: **Courthope, E. L** | colony: **Western Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. L. Courthope | Auditor General | Civil Establishment | — | — |
| 1878 | E. L. Courthope | Auditor-General | Civil Establishment | — | — |
| 1879 | E. L. Courthope | Auditor General | Audit Office | — | — |
| 1880 | E. L. Courthope | Auditor-General | Audit Department | — | — |

### Deterministic checks: `courthope_edward-l_e1847` vs `Courthope, E. L___Western Australia___1877`

- [PASS] surname_gate: bio 'COURTHOPE' vs stint 'Courthope, E. L' (exact)
- [PASS] initials: bio ['E', 'L'] ~ stint ['E', 'L']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Western Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 100 vs bar 60: 'auditor-general' ~ 'Auditor-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Courthope, E. L___Western Australia___1889`

- Staff-list name: **Courthope, E. L** | colony: **Western Australia** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | E. L. Courthope | Auditor-General | Audit Department | — | — |
| 1890 | E. L. Courthope | Auditor-General | Audit Department | — | — |

### Deterministic checks: `courthope_edward-l_e1847` vs `Courthope, E. L___Western Australia___1889`

- [PASS] surname_gate: bio 'COURTHOPE' vs stint 'Courthope, E. L' (exact)
- [PASS] initials: bio ['E', 'L'] ~ stint ['E', 'L']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

