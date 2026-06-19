<!-- {"case_id": "case_gibb_a_e1911", "bio_ids": ["gibb_a_e1911", "gibb_a_e1911-2"], "stint_ids": ["Gibb, A___British Somaliland___1912"]} -->
# Dossier case_gibb_a_e1911

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gibb_a_e1911', 'gibb_a_e1911-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Gibb, A___British Somaliland___1912'] have more than one claimant biography in this case.
- Phase 1 found `gibb_a_e1911` ↔ `Gibb, A___British Somaliland___1912` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `gibb_a_e1911-2` ↔ `Gibb, A___British Somaliland___1912` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `gibb_a_e1911`

- Printed name: **GIBB, A**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1912-L44375.v` — printed in editions [1912, 1913, 1914]:**

> GIBB, A.—Astt. dist. offr., Somaliland, Aug., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | Astt. dist. offr. | Somaliland | [1912, 1913, 1914] |

## Biography `gibb_a_e1911-2`

- Printed name: **GIBB, A**
- Birth year: not printed
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1915-L47204.v` — printed in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]:**

> GIBB, A.—Asst. dist. offr., Somaliland, Aug., 1911; apptd. for serv. with camel constaby., Aug., 1912; company comdr., Dec., 1913; ag. comdt., Sept. to Nov., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | Asst. dist. offr. | Somaliland | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 1 | 1912 | apptd. for serv. with camel constaby | Somaliland *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 2 | 1913 | company comdr | Somaliland *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Gibb, A___British Somaliland___1912`

- Staff-list name: **Gibb, A** | colony: **British Somaliland** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. Gibb | Assistant District Officer | Civil Establishment | — | — |
| 1913 | A. Gibb | Constabulary Officer | Camel Constabulary | — | — |
| 1914 | A. Gibb | Company Commander | Camel Constabulary | — | — |
| 1915 | A. Gibb | Company Commanders (4) | Military Department | — | — |
| 1917 | A. Gibb | Company Commander | Military Department | — | Capt. |
| 1918 | A. Gibb | Company Commanders | Military Department | — | Capt. |
| 1919 | A. Gibb | District Commissioner | Administration | — | Captain |
| 1920 | A. Gibb | District Commissioner | Administration | — | Captain |
| 1922 | A. Gibb | District Commissioner | Administration | D.S.O. | Captain |

### Deterministic checks: `gibb_a_e1911` vs `Gibb, A___British Somaliland___1912`

- [PASS] surname_gate: bio 'GIBB' vs stint 'Gibb, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1922
- [PASS] position_sim: best 70 vs bar 60: 'Astt. dist. offr.' ~ 'Assistant District Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1912] pos~70 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `gibb_a_e1911-2` vs `Gibb, A___British Somaliland___1912`

- [PASS] surname_gate: bio 'GIBB' vs stint 'Gibb, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1912-1922
- [PASS] position_sim: best 87 vs bar 60: 'company comdr' ~ 'Company Commander'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1915, 1917, 1918] pos~83 (bar: >=2)
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

