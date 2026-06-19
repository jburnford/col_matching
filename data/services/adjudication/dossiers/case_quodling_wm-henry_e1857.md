<!-- {"case_id": "case_quodling_wm-henry_e1857", "bio_ids": ["quodling_wm-henry_e1857"], "stint_ids": ["Quodling, William H___New South Wales___1877"]} -->
# Dossier case_quodling_wm-henry_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `quodling_wm-henry_e1857`

- Printed name: **QUODLING, WM. HENRY**
- Birth year: not printed
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L35233.v` — printed in editions [1889, 1890]:**

> QUODLING, WM. HENRY.—Sec. and acctnt. rly. constrn. dept., N.S. Wales, June, 1888; was apptd. clerk to engineer-in-chief for rlys., Oct., 1857.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857 | was apptd. clerk to engineer-in-chief for rlys | Nova Scotia *(inherited from previous clause)* | [1889, 1890] |
| 1 | 1888 | Sec. and acctnt. rly. constrn. dept., N.S. Wales | Nova Scotia | [1889, 1890] |

## Candidate stint `Quodling, William H___New South Wales___1877`

- Staff-list name: **Quodling, William H** | colony: **New South Wales** | listed 1877–1894 | editions [1877, 1879, 1880, 1886, 1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | William H. Quodling | Chief Clerk | Extensions | — | — |
| 1879 | William H. Quodling | Chief Clerk | Extensions | — | — |
| 1880 | William H. Quodling | Chief Clerk | Extensions | — | — |
| 1886 | William H. Quodling | Chief Clerk | Extensions | — | — |
| 1888 | William H. Quodling | Chief Clerk | Extensions | — | — |
| 1889 | William H. Quodling | Chief Clerk | Extensions | — | — |
| 1894 | W. H. Quodling | Chief Accountant | Department of Works and Subordinate Departments | — | — |

### Deterministic checks: `quodling_wm-henry_e1857` vs `Quodling, William H___New South Wales___1877`

- [PASS] surname_gate: bio 'QUODLING' vs stint 'Quodling, William H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1894
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

