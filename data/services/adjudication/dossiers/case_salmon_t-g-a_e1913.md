<!-- {"case_id": "case_salmon_t-g-a_e1913", "bio_ids": ["salmon_t-g-a_e1913"], "stint_ids": ["Salmon, G___British Guiana___1883", "Salmon, T. G___Ceylon___1917"]} -->
# Dossier case_salmon_t-g-a_e1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `salmon_t-g-a_e1913`

- Printed name: **SALMON, T. G. A**
- Birth year: not printed
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1915-L50216.v` — printed in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]:**

> SALMON, T. G. A.—Asst. dist. comantr., E.A.P., Dec., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Asst. dist. comantr. | East Africa Protectorate | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |

## Candidate stint `Salmon, G___British Guiana___1883`

- Staff-list name: **Salmon, G** | colony: **British Guiana** | listed 1883–1889 | editions [1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | G. Salmon | Curate | Ecclesiastical Establishments | — | — |
| 1886 | G. Salmon | Curate | Ecclesiastical Establishments (Church of England) | — | — |
| 1888 | G. Salmon | Curate | Ecclesiastical Establishments (Church of England) | — | — |
| 1889 | Rev. G. Salmon | Curate | Ecclesiastical Establishments | — | — |

### Deterministic checks: `salmon_t-g-a_e1913` vs `Salmon, G___British Guiana___1883`

- [PASS] surname_gate: bio 'SALMON' vs stint 'Salmon, G' (exact)
- [PASS] initials: bio ['T', 'G', 'A'] ~ stint ['G']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Salmon, T. G___Ceylon___1917`

- Staff-list name: **Salmon, T. G** | colony: **Ceylon** | listed 1917–1920 | editions [1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | T. G. Salmon | Assistant Superintendent | Police Department | — | Captain |
| 1918 | T. G. Salmon | Assistant Superintendent | Police Department | — | Captain |
| 1919 | Captain T. G. Salmon | Assistant Superintendent | Police Department | — | Captain |
| 1920 | Captain T. G. Salmon | Assistant Superintendent | Police Department | — | Captain |

### Deterministic checks: `salmon_t-g-a_e1913` vs `Salmon, T. G___Ceylon___1917`

- [PASS] surname_gate: bio 'SALMON' vs stint 'Salmon, T. G' (exact)
- [PASS] initials: bio ['T', 'G', 'A'] ~ stint ['T', 'G']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1920
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

