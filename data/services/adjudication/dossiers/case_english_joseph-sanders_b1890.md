<!-- {"case_id": "case_english_joseph-sanders_b1890", "bio_ids": ["english_joseph-sanders_b1890"], "stint_ids": ["English, J. S___Straits Settlements___1923"]} -->
# Dossier case_english_joseph-sanders_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `english_joseph-sanders_b1890`

- Printed name: **ENGLISH, JOSEPH SANDERS**
- Birth year: 1890 (attested in editions [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: B.A, F.C.O.G, M.D
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L60005.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> ENGLISH, JOSEPH SANDERS, B.A., M.D., B.Ch., B.A.O. (Dub.), L.M. (Rotunda Hosp., Dub.), F.C.O.G.—B. 1890; prof. of midwifery and gynaecology, King Edward VII. Coll. of Medicine, Singapore, Jan., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | prof. of midwifery and gynaecology, King Edward VII. Coll. of Medicine | Singapore | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `English, J. S___Straits Settlements___1923`

- Staff-list name: **English, J. S** | colony: **Straits Settlements** | listed 1923–1936 | editions [1923, 1925, 1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | J. S. English | Professor of Midwifery and Gynaecology | King Edward VII College of Medicine | — | — |
| 1925 | J. S. English | Professor of Midwifery and Gynaecology | King Edward VII College of Medicine | — | — |
| 1931 | J. S. English | Professor of Midwifery and Gynaecology | King Edward VII College of Medicine | — | — |
| 1933 | J. S. English | Professor of Midwifery and Gynaecology | King Edward VII College of Medicine | — | — |
| 1934 | J. S. English | Professor of Midwifery and Gynaecology | King Edward VII College of Medicine, Singapore | — | — |
| 1936 | J. S. English | Professor of Midwifery and Gynaecology | King Edward VII College of Medicine | — | — |

### Deterministic checks: `english_joseph-sanders_b1890` vs `English, J. S___Straits Settlements___1923`

- [PASS] surname_gate: bio 'ENGLISH' vs stint 'English, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1923, birth 1890 (age 33)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1936
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

