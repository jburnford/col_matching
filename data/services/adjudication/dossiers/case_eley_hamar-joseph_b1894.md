<!-- {"case_id": "case_eley_hamar-joseph_b1894", "bio_ids": ["eley_hamar-joseph_b1894"], "stint_ids": ["Eley, H. J___Straits Settlements___1921"]} -->
# Dossier case_eley_hamar-joseph_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `eley_hamar-joseph_b1894`

- Printed name: **ELEY, HAMAR JOSEPH**
- Birth year: 1894 (attested in editions [1923, 1924, 1925, 1927, 1928, 1929])
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1923-L54183.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1929]:**

> ELEY, HAMAR JOSEPH.—B. 1894; ed. Burton-on-Trent and Queen's Coll., Camb. (math. tripos, pt. I); O.T.C., Camb.; 2nd lieut., 13th Bn. Sherwood Foresters, Feb., 1915; served, Suvala Bay, Egypt and France; wounded, Sept., 1916; discharged, Apr., 1918; cadet, Malayan civil service (S.S.), Mar., 1920; collr. of income tax, Singapore, May, 1920; ag. res., Labuan, 5th Oct., 1921; passed cadet, 14th Mar., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | 2nd lieut., 13th Bn. Sherwood Foresters | — | [1923, 1924, 1925, 1927, 1928, 1929] |
| 1 | 1916 | wounded | — | [1923, 1924, 1925, 1927, 1928, 1929] |
| 2 | 1918 | discharged | — | [1923, 1924, 1925, 1927, 1928, 1929] |
| 3 | 1920 | cadet, Malayan civil service (S.S.) | — | [1923, 1924, 1925, 1927, 1928, 1929] |
| 4 | 1920 | collr. of income tax | Singapore | [1923, 1924, 1925, 1927, 1928, 1929] |
| 5 | 1921 | ag. res. | Labuan | [1923, 1924, 1925, 1927, 1928, 1929] |
| 6 | 1922 | passed cadet | Labuan *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1929] |

## Candidate stint `Eley, H. J___Straits Settlements___1921`

- Staff-list name: **Eley, H. J** | colony: **Straits Settlements** | listed 1921–1922 | editions [1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | H. J. Eley | Cadet | Civil Establishment | — | — |
| 1922 | H. J. Eley | Resident and District Judge | Establishment | — | — |

### Deterministic checks: `eley_hamar-joseph_b1894` vs `Eley, H. J___Straits Settlements___1921`

- [PASS] surname_gate: bio 'ELEY' vs stint 'Eley, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1921, birth 1894 (age 27)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1922
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

