<!-- {"case_id": "case_benatar_david-j_b1872", "bio_ids": ["benatar_david-j_b1872"], "stint_ids": ["Benatar, D___Gambia___1914", "Benatar, D___Gibraltar___1909"]} -->
# Dossier case_benatar_david-j_b1872

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `benatar_david-j_b1872`

- Printed name: **BENATAR, DAVID J.**
- Birth year: 1872 (attested in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919])
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1910-L44238.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> BENATAR, DAVID J., B.Sc., B. Eng.—B. 1872; ed. Walker Engineering Laboratories, Univ. Coll., Liverpool; 1st class engineering certif.; B.Sc., Victoria Univ. (engineering subjects), 1st class, 1st div., 1894; B.Eng., Liverpool Univ., 1904; mem. of Convocation of both univs.; mem. of engineering exec. staff, Admiralty docks and harbour wks., Gibraltar, 1895-1906; entd. pub. wks. dep. as asst. engr., Jan., 1907; surveyor, govt. engrn.'s dept., June, 1908; ag. govt. engrn., July to Oct., 1911 and 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895–1906 | mem. of engineering exec. staff, Admiralty docks and harbour wks. | Gibraltar | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1907–1907 | asst. engr. | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1908–1908 | surveyor | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 3 | 1911–1913 | ag. govt. engrn. | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Benatar, D___Gambia___1914`

- Staff-list name: **Benatar, D** | colony: **Gambia** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | D. Benatar | Surveyor | Public Works | — | — |
| 1915 | D. Benatar | Surveyor | Public Works | — | — |

### Deterministic checks: `benatar_david-j_b1872` vs `Benatar, D___Gambia___1914`

- [PASS] surname_gate: bio 'BENATAR' vs stint 'Benatar, D' (exact)
- [PASS] initials: bio ['D', 'J'] ~ stint ['D']
- [PASS] age_gate: stint starts 1914, birth 1872 (age 42)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Benatar, D___Gibraltar___1909`

- Staff-list name: **Benatar, D** | colony: **Gibraltar** | listed 1909–1919 | editions [1909, 1910, 1911, 1912, 1913, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | D. Benatar | Surveyor | Public Works | — | — |
| 1910 | D. Benatar | Surveyor | Public Works | — | — |
| 1911 | D. Benatar | Surveyor | Public Works | — | — |
| 1912 | D. Benatar | Surveyor | Public Works | — | — |
| 1913 | D. Benatar | Surveyor | Public Works | — | — |
| 1917 | D. Benatar | Surveyor | Public Works | — | — |
| 1918 | D. Benatar | Surveyor | Public Works | — | — |
| 1919 | D. Benatar | Surgeon | Public Works | — | — |

### Deterministic checks: `benatar_david-j_b1872` vs `Benatar, D___Gibraltar___1909`

- [PASS] surname_gate: bio 'BENATAR' vs stint 'Benatar, D' (exact)
- [PASS] initials: bio ['D', 'J'] ~ stint ['D']
- [PASS] age_gate: stint starts 1909, birth 1872 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1919
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

