<!-- {"case_id": "case_townsend_w-h-m_e1903", "bio_ids": ["townsend_w-h-m_e1903"], "stint_ids": ["Townsend, W. H. M___Kenya___1909", "Townsend, William___South Australia___1878"]} -->
# Dossier case_townsend_w-h-m_e1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Townsend, William___South Australia___1878` is also gate-compatible with biography(ies) outside this case: ['townsend_wm-richard_e1894', 'townssend_wm-richard_e1894'] (already linked elsewhere or filtered).

## Biography `townsend_w-h-m_e1903`

- Printed name: **TOWNSEND, W. H. M**
- Birth year: not printed
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1910-L49157.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> TOWNSEND, W. H. M.—Ch. offr., Uganda river lake steamers, June, 1903; comdr., July, 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Ch. offr., Uganda river lake steamers | Uganda | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1905 | comdr | Uganda *(inherited from previous clause)* | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Townsend, W. H. M___Kenya___1909`

- Staff-list name: **Townsend, W. H. M** | colony: **Kenya** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | W. H. M. Townsend | Commanders | Lake Steamers | — | — |
| 1910 | W. H. M. Townsend | Commanders | Lake Steamers | — | — |

### Deterministic checks: `townsend_w-h-m_e1903` vs `Townsend, W. H. M___Kenya___1909`

- [PASS] surname_gate: bio 'TOWNSEND' vs stint 'Townsend, W. H. M' (exact)
- [PASS] initials: bio ['W', 'H', 'M'] ~ stint ['W', 'H', 'M']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Townsend, William___South Australia___1878`

- Staff-list name: **Townsend, William** | colony: **South Australia** | listed 1878–1879 | editions [1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | William Townsend | Chairman of Committees | House of Assembly | — | — |
| 1879 | William Townsend | Chairman of Committees | House of Assembly | — | — |

### Deterministic checks: `townsend_w-h-m_e1903` vs `Townsend, William___South Australia___1878`

- [PASS] surname_gate: bio 'TOWNSEND' vs stint 'Townsend, William' (exact)
- [PASS] initials: bio ['W', 'H', 'M'] ~ stint ['W']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1879
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

