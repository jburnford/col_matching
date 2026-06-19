<!-- {"case_id": "case_dignum_andrew-b_e1861", "bio_ids": ["dignum_andrew-b_e1861"], "stint_ids": ["Dignum, A. B___Jamaica___1877"]} -->
# Dossier case_dignum_andrew-b_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dignum_andrew-b_e1861`

- Printed name: **DIGNUM, ANDREW B**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L33100.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1898]:**

> DIGNUM, ANDREW B.—Deputy clerk to magistrates, Trelawny, Jamaica, 1861; clerk, Falmouth district court, Jan., 1867; ditto, St. Ann's Bay, 1870; ditto, northern district, Jan., 1880; notary public, May, 1868; is a solicitor of supreme court.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Deputy clerk to magistrates, Trelawny | Jamaica | [1888, 1889, 1890, 1894, 1896, 1898] |
| 1 | 1867 | clerk, Falmouth district court | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |
| 2 | 1868 | notary public | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |
| 3 | 1870 | ditto, St. Ann's Bay | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |
| 4 | 1880 | ditto, northern district | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |

## Candidate stint `Dignum, A. B___Jamaica___1877`

- Staff-list name: **Dignum, A. B** | colony: **Jamaica** | listed 1877–1897 | editions [1877, 1878, 1879, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. B. Dignum | Clerk | District Courts | — | — |
| 1878 | A. B. Dignum | Clerk | District Courts | — | — |
| 1879 | A. B. Dignum | Clerk | District Courts | — | — |
| 1883 | A. B. Dignum | Clerk | District Courts | — | — |
| 1886 | A. B. Dignum | Clerk of District Courts | District Courts | — | — |
| 1888 | A. B. Dignum | Clerk of District Court | Judicial Establishment | — | — |
| 1889 | A. B. Dignum | Resident Magistrate | Resident Magistrates | — | — |
| 1890 | A. B. Dignum | Resident Magistrate | Judicial Establishment | — | — |
| 1894 | A. B. Dignum | Resident Magistrate | Resident Magistrates | — | — |
| 1896 | A. B. Dignum | Resident Magistrate | Judicial Establishment | — | — |
| 1897 | A. B. Dignum | Resident Magistrate | Resident Magistrates | — | — |

### Deterministic checks: `dignum_andrew-b_e1861` vs `Dignum, A. B___Jamaica___1877`

- [PASS] surname_gate: bio 'DIGNUM' vs stint 'Dignum, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1897
- [FAIL] position_sim: best 57 vs bar 60: 'ditto, northern district' ~ 'Clerk of District Court'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1888] pos~57 (bar: >=2)
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

