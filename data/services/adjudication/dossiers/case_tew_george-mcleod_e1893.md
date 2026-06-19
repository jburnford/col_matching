<!-- {"case_id": "case_tew_george-mcleod_e1893", "bio_ids": ["tew_george-mcleod_e1893"], "stint_ids": ["Tew, G. McL___Kenya___1909"]} -->
# Dossier case_tew_george-mcleod_e1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tew_george-mcleod_e1893`

- Printed name: **TEW, GEORGE McLEOD**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1908-L47816.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]:**

> TEW, GEORGE McLEOD.—Indian pol., Harar, 1893-7; Uganda rly. pol., 1899-1903; asst. dist. supt. of pol., E. Africa Prot., 1st Apr., 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893–1897 | Indian pol., Harar | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1899–1903 | Uganda rly. pol | Uganda | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1903 | asst. dist. supt. of pol., E. Africa Prot | Uganda *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Tew, G. McL___Kenya___1909`

- Staff-list name: **Tew, G. McL** | colony: **Kenya** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | G. McL. Tew | Assistant District Superintendent | Police | — | — |
| 1910 | G. McL. Tew | Assistant District Superintendent | Police | — | — |

### Deterministic checks: `tew_george-mcleod_e1893` vs `Tew, G. McL___Kenya___1909`

- [PASS] surname_gate: bio 'TEW' vs stint 'Tew, G. McL' (exact)
- [PASS] initials: bio ['G', 'M'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1910
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

