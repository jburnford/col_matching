<!-- {"case_id": "case_mountain_george-alphonse_b1860", "bio_ids": ["mountain_george-alphonse_b1860"], "stint_ids": ["Mountain, G. A___Canada___1912"]} -->
# Dossier case_mountain_george-alphonse_b1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mountain_george-alphonse_b1860`

- Printed name: **MOUNTAIN, GEORGE ALPHONSE**
- Birth year: 1860 (attested in editions [1921, 1922, 1923, 1924, 1927])
- Appears in editions: [1921, 1922, 1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1921-L58699.v` — printed in editions [1921, 1922, 1923, 1924, 1927]:**

> MOUNTAIN, GEORGE ALPHONSE.—B. 1860; ed. Quebec; civ. engrnr. and Dom. land surr.; on surv. of Queb. and Lake St. John Rly., 1879; Newfoundland Rly., 1880; Can. Atlantic Rly., 1881 to 1904; ch. engrnr., 1888 to 1904; ch. engrnr., bd. of rly. comsrs., Can., 1st July, 1904; past pres. and mem. of Engng. Inst. of Can.; mem. Amer. Rly. Engrng. Assoc., and Assoc. of Rly. Supts. of Bldgs. and Bridges.

**Version `col1925-L58080.v` — printed in editions [1925]:**

> MOUNTAIN, GEORGE ALPHONSE.—B. ed. Quebec; civ. engnr. and Dom. land surveyor, Que., 1880; Can. Atlantic Rly., 1904; ch. engnr., 1888 to 1904; ch. engrg. rly. comsnrs., Can., 1st July, 1904; past mem. of Engng. Inst. of Can.; mem. Can. Rly. Engng. Assoc., and Assoc. of Rly. Bldgs. and Bridges.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | on surv. of Queb. and Lake St. John Rly | — | [1921, 1922, 1923, 1924, 1927] |
| 1 | 1880 | Newfoundland Rly | Newfoundland | [1921, 1922, 1923, 1924, 1927] |
| 2 | 1880 | civ. engnr. and Dom. land surveyor, Que | — | [1925] |
| 3 | 1881–1904 | Can. Atlantic Rly | Newfoundland *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1927] |
| 4 | 1888–1904 | ch. engrnr | Newfoundland *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1925, 1927] |
| 5 | 1904 | ch. engrnr., bd. of rly. comsrs., Can | Newfoundland *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1925, 1927] |
| 6 | 1904 | Can. Atlantic Rly | — | [1925] |

## Candidate stint `Mountain, G. A___Canada___1912`

- Staff-list name: **Mountain, G. A** | colony: **Canada** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1913 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1914 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1915 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1917 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1918 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1919 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1920 | G. A. Mountain | Chief Engineer | Permanent Railway Commission | — | — |
| 1922 | G. A. Mountain | Chief Engineer | Railway Commission | — | — |

### Deterministic checks: `mountain_george-alphonse_b1860` vs `Mountain, G. A___Canada___1912`

- [PASS] surname_gate: bio 'MOUNTAIN' vs stint 'Mountain, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1912, birth 1860 (age 52)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1922
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

