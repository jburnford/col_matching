<!-- {"case_id": "case_bell_leslie-livingstone_e1906", "bio_ids": ["bell_leslie-livingstone_e1906"], "stint_ids": ["Bell, L. L___Australia___1912", "Bell, L. L___Papua___1909"]} -->
# Dossier case_bell_leslie-livingstone_e1906

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 123 official(s) with this surname in the graph's staff lists; 69 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bell_leslie-livingstone_e1906`

- Printed name: **BELL, LESLIE LIVINGSTONE**
- Birth year: not printed
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1910-L44228.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]:**

> BELL, LESLIE LIVINGSTONE.—2nd cls. gov.-in-ch. sec.'s dept., Papua, 20th Jan., 1906; chief instr. dept. of native affairs and control, 20th Feb., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | 2nd cls. gov.-in-ch. sec.'s dept. | Papua | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |

## Candidate stint `Bell, L. L___Australia___1912`

- Staff-list name: **Bell, L. L** | colony: **Australia** | listed 1912–1918 | editions [1912, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | L. L. Bell | Chief Inspector | Department of Native Affairs | — | — |
| 1918 | L. L. Bell | Chief Inspector | Department of Native Affairs | — | — |

### Deterministic checks: `bell_leslie-livingstone_e1906` vs `Bell, L. L___Australia___1912`

- [PASS] surname_gate: bio 'BELL' vs stint 'Bell, L. L' (exact)
- [PASS] initials: bio ['L', 'L'] ~ stint ['L', 'L']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bell, L. L___Papua___1909`

- Staff-list name: **Bell, L. L** | colony: **Papua** | listed 1909–1917 | editions [1909, 1911, 1913, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | L. L. Bell | Resident Magistrate, Gulf Division | Establishment | — | — |
| 1911 | L. L. Bell | Chief Inspector | Department of Native Affairs | — | — |
| 1913 | L. L. Bell | Chief Inspector | Department of Native Affairs | — | — |
| 1917 | L. L. Bell | Chief Inspector | Department of Native Affairs | — | — |

### Deterministic checks: `bell_leslie-livingstone_e1906` vs `Bell, L. L___Papua___1909`

- [PASS] surname_gate: bio 'BELL' vs stint 'Bell, L. L' (exact)
- [PASS] initials: bio ['L', 'L'] ~ stint ['L', 'L']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Papua'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1917
- [FAIL] position_sim: best 40 vs bar 60: '2nd cls. gov.-in-ch. sec.'s dept.' ~ 'Chief Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

