<!-- {"case_id": "case_bardo_frederic-stanley-cook_b1869", "bio_ids": ["bardo_frederic-stanley-cook_b1869"], "stint_ids": ["Bardo, F. S___Zanzibar___1909"]} -->
# Dossier case_bardo_frederic-stanley-cook_b1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bardo_frederic-stanley-cook_b1869`

- Printed name: **BARDO, FREDERIC STANLEY COOK**
- Birth year: 1869 (attested in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922])
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1915-L45043.v` — printed in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> BARDO, FREDERIC STANLEY COOK.—B. 1869; ed. City of London Schl. and Vickery's Naval Acad., Pts.; master mariner; asst. port offr., Zanzibar, 22nd June, 1904; port offr., 11th June, 1905; director of wireless telegraph, 1907 to 1914; 3rd cls. Aliyah and 3rd cls. Brilliant Star.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | asst. port offr. | Zanzibar | [1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 1 | 1905 | port offr | Zanzibar *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 2 | 1907–1914 | director of wireless telegraph | Zanzibar *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Bardo, F. S___Zanzibar___1909`

- Staff-list name: **Bardo, F. S** | colony: **Zanzibar** | listed 1909–1921 | editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | F. S. Bardo | Port Officer | — | — | Captain |
| 1910 | Captain F. S. Bardo | Port Officer | — | — | Captain |
| 1911 | Captain F. S. Bardo | Port Officer | — | — | — |
| 1912 | Captain F. S. Bardo | Port Officer | — | — | Captain |
| 1913 | F. S. Bardo | Port Officer | — | — | Captain |
| 1914 | F. S. Bardo | Port Officer | — | — | Captain |
| 1915 | F. S. Bardo | Port Officer | Port Service and Shipping Departments | — | Captain |
| 1917 | F. S. Bardo | Port Officer | Port Service and Shipping Departments | — | Captain |
| 1919 | Capt. F. S. Bardo | Port Officer | Port Service and Shipping Departments | — | Captain |
| 1920 | F. S. Bardo | Port Officer | Port Service and Shipping Departments | — | Captain |
| 1921 | F. S. Bardo | Port Officer | Port Service and Shipping Departments | — | Captain |

### Deterministic checks: `bardo_frederic-stanley-cook_b1869` vs `Bardo, F. S___Zanzibar___1909`

- [PASS] surname_gate: bio 'BARDO' vs stint 'Bardo, F. S' (exact)
- [PASS] initials: bio ['F', 'S', 'C'] ~ stint ['F', 'S']
- [PASS] age_gate: stint starts 1909, birth 1869 (age 40)
- [PASS] colony: 3 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1921
- [FAIL] position_sim: best 29 vs bar 60: 'director of wireless telegraph' ~ 'Port Officer'
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

