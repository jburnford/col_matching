<!-- {"case_id": "case_rowe_charles-frederick_e1896", "bio_ids": ["rowe_charles-frederick_e1896"], "stint_ids": ["Rowe, C. F___Nigeria___1915"]} -->
# Dossier case_rowe_charles-frederick_e1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rowe_charles-frederick_e1896`

- Printed name: **ROWE, CHARLES FREDERICK**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1912-L47335.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> ROWE, CHARLES FREDERICK.—Lieut. 1st V.B. Royal War. regt., 1896-98; Natal pol., 1898-99; served throughout S. Africa war, in Imp. Light Horse, 1899-1900, and in S. African constab., 1900-1903; capt., Oct., 1903; asst. res., N. Nigeria, 14th May, 1904; 3rd cls. res., Apl., 1905; 2nd cls. res., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896–1898 | Lieut. 1st V.B. Royal War. regt | — | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1898–1899 | Natal pol | Natal | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1899–1900 | served throughout S. Africa war, in Imp. Light Horse | Natal *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 3 | 1900–1903 | in S. African constab | Natal *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 4 | 1903 | capt | Natal *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 5 | 1904 | asst. res., N. Nigeria | Natal *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 6 | 1905 | 3rd cls. res | Natal *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 7 | 1911 | 2nd cls. res | Natal *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Rowe, C. F___Nigeria___1915`

- Staff-list name: **Rowe, C. F** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | C. F. Rowe | Fifteen Second Class Residents or Commissioners | NORTHERN PROVINCES | — | — |
| 1917 | C. F. Rowe | Second Class Resident | Northern Provinces | — | — |
| 1918 | C. F. Rowe | Second Class Resident | Northern Provinces | — | — |
| 1919 | C. F. Rowe | Fifteen Second Class Residents | NORTHERN PROVINCES | — | — |

### Deterministic checks: `rowe_charles-frederick_e1896` vs `Rowe, C. F___Nigeria___1915`

- [PASS] surname_gate: bio 'ROWE' vs stint 'Rowe, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1919
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

