<!-- {"case_id": "case_murray_robert-hosworth_e1923", "bio_ids": ["murray_robert-hosworth_e1923", "murray_robert-howson_e1923"], "stint_ids": ["Murray, R. H___Nyasaland___1911"]} -->
# Dossier case_murray_robert-hosworth_e1923

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 123 official(s) with this surname in the graph's staff lists; 63 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Murray, R. H___Nyasaland___1911'] have more than one claimant biography in this case.
- Phase 1 found `murray_robert-hosworth_e1923` ↔ `Murray, R. H___Nyasaland___1911` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `murray_robert-howson_e1923` ↔ `Murray, R. H___Nyasaland___1911` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `murray_robert-hosworth_e1923`

- Printed name: **MURRAY, ROBERT HOSWORTH**
- Birth year: not printed
- Appears in editions: [1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1924-L56795.v` — printed in editions [1924, 1925]:**

> MURRAY, ROBERT HOSWORTH.—Admstrn. offr., 1st grade, Nyasaland, 28th Feb., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | Admstrn. offr., 1st grade | Nyasaland | [1924, 1925] |

## Biography `murray_robert-howson_e1923`

- Printed name: **MURRAY, ROBERT HOWSON**
- Birth year: not printed
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1927-L61593.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934]:**

> MURRAY, ROBERT HOWSON.—Admstrn. offr., 1st grade, Nyasaland, Feb., 1923; ag. prov. comsnr., July, 1925 to July, 1926; prov. comsnr., Jan., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | Admstrn. offr., 1st grade | Nyasaland | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 1 | 1925–1926 | ag. prov. comsnr | Nyasaland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 2 | 1928 | prov. comsnr | Nyasaland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |

## Candidate stint `Murray, R. H___Nyasaland___1911`

- Staff-list name: **Murray, R. H** | colony: **Nyasaland** | listed 1911–1925 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | R. H. Murray | Eighteen 3rd Grade | Residents | — | — |
| 1912 | R. H. Murray | Nineteen 3rd Grade | Residents | — | — |
| 1913 | R. H. Murray | Twenty-one 3rd Grade | Residents | — | — |
| 1914 | R. H. Murray | Twenty-one Assistant | Residents | — | — |
| 1915 | R. H. Murray | Assistant | District Residents | — | — |
| 1917 | R. H. Murray | Assistant | District Residents | — | — |
| 1918 | R. H. Murray | Twenty-four Assistants | District Residents | — | — |
| 1919 | R. H. Murray | Twenty-four Assistants | District Residents | — | — |
| 1920 | R. H. Murray | Assistant | District Residents | — | — |
| 1921 | R. H. Murray | Residents | District Residents | — | — |
| 1922 | R. H. Murray | Assistant | District Staff | — | — |
| 1923 | R. H. Murray | Administrative Officer (2nd Grade) | District Staff | — | — |
| 1924 | R. H. Murray | Administrative Officer, 1st Grade | District Staff | — | — |
| 1925 | R. H. Murray | Administrative Officers, 1st Grade | District Staff | — | — |

### Deterministic checks: `murray_robert-hosworth_e1923` vs `Murray, R. H___Nyasaland___1911`

- [PASS] surname_gate: bio 'MURRAY' vs stint 'Murray, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1925
- [PASS] position_sim: best 78 vs bar 60: 'Admstrn. offr., 1st grade' ~ 'Administrative Officer, 1st Grade'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1924, 1925] pos~77 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `murray_robert-howson_e1923` vs `Murray, R. H___Nyasaland___1911`

- [PASS] surname_gate: bio 'MURRAY' vs stint 'Murray, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1911-1925
- [PASS] position_sim: best 78 vs bar 60: 'Admstrn. offr., 1st grade' ~ 'Administrative Officer, 1st Grade'
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

