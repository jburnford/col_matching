<!-- {"case_id": "case_prouse_arthur-duncan_b1863", "bio_ids": ["prouse_arthur-duncan_b1863"], "stint_ids": ["Prouse, A. D___Ceylon___1914"]} -->
# Dossier case_prouse_arthur-duncan_b1863

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `prouse_arthur-duncan_b1863`

- Printed name: **PROUSE, ARTHUR DUNCAN**
- Birth year: 1863 (attested in editions [1920, 1921, 1922, 1923, 1924])
- Appears in editions: [1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1920-L56584.v` — printed in editions [1920, 1921, 1922, 1923, 1924]:**

> PROUSE, ARTHUR DUNCAN.—B. 1863; M.I.C.E.; asst. engrnr., harbour wks., Colombo, Ceylon, Feb., 1896; on spec. duty, Zanzibar, May to Aug., 1909; res. engrnr., Colombo harbour wks., Feb., 1913; harbour engrnr., Feb., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | asst. engrnr., harbour wks., Colombo | Ceylon | [1920, 1921, 1922, 1923, 1924] |
| 1 | 1909 | on spec. duty | Zanzibar | [1920, 1921, 1922, 1923, 1924] |
| 2 | 1913 | res. engrnr., Colombo harbour wks | Zanzibar *(inherited from previous clause)* | [1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Prouse, A. D___Ceylon___1914`

- Staff-list name: **Prouse, A. D** | colony: **Ceylon** | listed 1914–1923 | editions [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1915 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1917 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1918 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1919 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1920 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1921 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1922 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |
| 1923 | A. D. Prouse | Harbour Engineer | Colombo Port Commission | — | — |

### Deterministic checks: `prouse_arthur-duncan_b1863` vs `Prouse, A. D___Ceylon___1914`

- [PASS] surname_gate: bio 'PROUSE' vs stint 'Prouse, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1914, birth 1863 (age 51)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1923
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

