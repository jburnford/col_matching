<!-- {"case_id": "case_foran_william-robert_e1899", "bio_ids": ["foran_william-robert_e1899"], "stint_ids": ["Foran, William___Canada___1899"]} -->
# Dossier case_foran_william-robert_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Foran, William___Canada___1899` is also gate-compatible with biography(ies) outside this case: ['foran_william_b1871'] (already linked elsewhere or filtered).

## Biography `foran_william-robert_e1899`

- Printed name: **FORAN, William Robert**
- Birth year: not printed
- Appears in editions: [1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1908-L44466.v` — printed in editions [1908, 1909]:**

> FORAN, William Robert.—Ed. at Prior Park, Bath, and St. Edmund's Coll., Ware, Herts.; served in Somerset L.I., I.Y., and on transport staff during S. African war, 1899 to 1902; resig., June, 1903; Transvaal civ. ser., 1903 to 1904; inspr. of pol., E. Africa Prot., 16th May, 1904; asst. dist. supt. of pol., E. Africa Prot., 15th Oct., 1904; S. African medals, Queen's and King's, 5 bars.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899–1902 | served in Somerset L.I., I.Y., and on transport staff during S. African war | — | [1908, 1909] |
| 1 | 1903 | resig | — | [1908, 1909] |
| 2 | 1903–1904 | Transvaal civ. ser | Transvaal | [1908, 1909] |
| 3 | 1904 | inspr. of pol., E. Africa Prot | Transvaal *(inherited from previous clause)* | [1908, 1909] |

## Candidate stint `Foran, William___Canada___1899`

- Staff-list name: **Foran, William** | colony: **Canada** | listed 1899–1922 | editions [1899, 1900, 1905, 1906, 1907, 1908, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | William Foran | Secretary | Secretary of State | — | — |
| 1900 | William Foran | Secretary | Departments of State | — | — |
| 1905 | William Foran | Secretary | Secretary of State | — | — |
| 1906 | William Foran | Secretary | Secretary of State | — | — |
| 1907 | William Foran | Secretary | DEPARTMENTS OF STATE | — | — |
| 1908 | William Foran | Secretary | Secretary of State | — | — |
| 1912 | William Foran | Secretary | Civil Service Commission | — | — |
| 1913 | William Foran | Secretary | Civil Service Commission | — | — |
| 1914 | William Foran | Secretary | Civil Service Commission | — | — |
| 1915 | William Foran | Secretary | Civil Service Commission | — | — |
| 1917 | William Foran | Secretary | Civil Service Commission | — | — |
| 1918 | William Foran | Secretary | Civil Service Commission | — | — |
| 1919 | William Foran | Secretary | Civil Service Commission | — | — |
| 1920 | William Foran | Secretary | Civil Service Commission | — | — |
| 1922 | William Foran | Secretary | Civil Service Commission | — | — |

### Deterministic checks: `foran_william-robert_e1899` vs `Foran, William___Canada___1899`

- [PASS] surname_gate: bio 'FORAN' vs stint 'Foran, William' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1922
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

