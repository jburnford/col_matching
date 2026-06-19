<!-- {"case_id": "case_kennan_thomas-bhereton_b1891", "bio_ids": ["kennan_thomas-bhereton_b1891"], "stint_ids": ["Kennan, Thomas Brereton___Basutoland___1920"]} -->
# Dossier case_kennan_thomas-bhereton_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Kennan, Thomas Brereton___Basutoland___1920` is also gate-compatible with biography(ies) outside this case: ['kennan_thomas-brereton_b1891'] (already linked elsewhere or filtered).

## Biography `kennan_thomas-bhereton_b1891`

- Printed name: **KENNAN, THOMAS BHERETON**
- Birth year: 1891 (attested in editions [1933, 1935, 1936, 1940])
- Appears in editions: [1933, 1935, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L61237.v` — printed in editions [1933, 1935, 1936, 1940]:**

> KENNAN, THOMAS BHERETON, M.C.—B. 1891; ed. Collet Court, Lond. and Worcester Cathedral Schl.; cler. asst., Basutoland, 1910; sub-inspr., pol., 1913; inspr., 1919; served in European War; asst. comsnr., 1929; title changed to dist. comsnr., 1936; ag. govt. sec., 1938; 1st asst. sec., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | cler. asst. | Basutoland | [1933, 1935, 1936, 1940] |
| 1 | 1913 | sub-inspr., pol | Basutoland *(inherited from previous clause)* | [1933, 1935, 1936, 1940] |
| 2 | 1919 | inspr | Basutoland *(inherited from previous clause)* | [1933, 1935, 1936, 1940] |
| 3 | 1929 | asst. comsnr | Basutoland *(inherited from previous clause)* | [1933, 1935, 1936, 1940] |
| 4 | 1936 | title changed to dist. comsnr | Basutoland *(inherited from previous clause)* | [1933, 1935, 1936, 1940] |
| 5 | 1938 | ag. govt. sec | Basutoland *(inherited from previous clause)* | [1933, 1935, 1936, 1940] |

## Candidate stint `Kennan, Thomas Brereton___Basutoland___1920`

- Staff-list name: **Kennan, Thomas Brereton** | colony: **Basutoland** | listed 1920–1925 | editions [1920, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Thomas Brereton Kennan | Inspector of Police | Civil Establishment | — | — |
| 1921 | Thomas Brereton Kennan | Inspector of Police | Establishment | — | — |
| 1922 | Thomas Brereton Kennan | Inspector of Police | Establishment | — | — |
| 1924 | Thomas Brereton Kennan | Inspector | Police | — | Captain |
| 1925 | Thomas Brereton Kennan | Inspector | Police | — | Captain |

### Deterministic checks: `kennan_thomas-bhereton_b1891` vs `Kennan, Thomas Brereton___Basutoland___1920`

- [PASS] surname_gate: bio 'KENNAN' vs stint 'Kennan, Thomas Brereton' (exact)
- [PASS] initials: bio ['T', 'B'] ~ stint ['T', 'B']
- [PASS] age_gate: stint starts 1920, birth 1891 (age 29)
- [PASS] colony: 6 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1920-1925
- [PASS] position_sim: best 71 vs bar 60: 'inspr' ~ 'Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

