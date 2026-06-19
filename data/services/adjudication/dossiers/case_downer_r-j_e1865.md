<!-- {"case_id": "case_downer_r-j_e1865", "bio_ids": ["downer_r-j_e1865"], "stint_ids": ["Downer, R. J___British Honduras___1877"]} -->
# Dossier case_downer_r-j_e1865

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `downer_r-j_e1865`

- Printed name: **DOWNER, R. J**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27242.v` — printed in editions [1883]:**

> DOWNER, R. J.—Paid magistrate, Southern District, British Honduras, 1865; commissioner superior court, 1866; paid magistrate and sub-agent of immigration of North Western Frontier, 1866; paid magistrate, Southern District, 1874; health officer of Southern District, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | Paid magistrate, Southern District | British Honduras | [1883] |
| 1 | 1866 | commissioner superior court | British Honduras *(inherited from previous clause)* | [1883] |
| 2 | 1874 | paid magistrate, Southern District | British Honduras *(inherited from previous clause)* | [1883] |
| 3 | 1877 | health officer of Southern District | British Honduras *(inherited from previous clause)* | [1883] |

## Candidate stint `Downer, R. J___British Honduras___1877`

- Staff-list name: **Downer, R. J** | colony: **British Honduras** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. J. Downer | Magistrate, Southern District | Judicial Establishment | — | — |
| 1878 | R. J. Downer | Magistrate | Judicial Establishment | — | — |
| 1879 | R. J. Downer | Magistrate, Southern District | Judicial Establishment | — | — |
| 1880 | R. J. Downer | Magistrate | Judicial Establishment | — | — |
| 1883 | R. J. Downer | Magistrate | Judicial Establishment | — | — |

### Deterministic checks: `downer_r-j_e1865` vs `Downer, R. J___British Honduras___1877`

- [PASS] surname_gate: bio 'DOWNER' vs stint 'Downer, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'paid magistrate, Southern District' ~ 'Magistrate, Southern District'
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

