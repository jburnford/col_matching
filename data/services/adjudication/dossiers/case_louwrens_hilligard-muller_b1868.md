<!-- {"case_id": "case_louwrens_hilligard-muller_b1868", "bio_ids": ["louwrens_hilligard-muller_b1868"], "stint_ids": ["Lourensz, H___Ceylon___1934"]} -->
# Dossier case_louwrens_hilligard-muller_b1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `louwrens_hilligard-muller_b1868`

- Printed name: **LOUWRENS, HILLIGARD MULLER**
- Birth year: 1868 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1927-L60822.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935]:**

> LOUWRENS, HILLIGARD MULLER.—B. 1868; ed. Normal Coll., Cape Town, Victoria Coll., Stellenbosch and law classes, S.A. Coll., Cape Town; admitted as atty. and notary, sup. ct., Cape Town, 1892; practised as atty., 1892-1903; ca. led to bar, Middle Temple, 1906; practised at sup. ct. bar, Cape Town, 1906-23; K.C., 1922; ag. water ct. judge, 1923; judge, sup. ct., Cape of Good Hope local divn., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | admitted as atty. and notary, sup. ct., Cape Town | Cape of Good Hope | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 1 | 1906 | ca. led to bar, Middle Temple | Cape of Good Hope | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 2 | 1922 | K.C | Cape of Good Hope *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 3 | 1923 | ag. water ct. judge | Cape of Good Hope *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 4 | 1924 | judge, sup. ct., Cape of Good Hope local divn | Cape of Good Hope | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |

## Candidate stint `Lourensz, H___Ceylon___1934`

- Staff-list name: **Lourensz, H** | colony: **Ceylon** | listed 1934–1940 | editions [1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | H. Lourensz | Probationer | Income Tax Department | — | — |
| 1937 | H. Lourensz | Assistant Assessor | Department of Income Tax, Estate Duty and Stamps | — | — |
| 1940 | H. Lourensz | Assistant Assessor | Department of Income Tax, Estate Duty and Stamps. | — | — |

### Deterministic checks: `louwrens_hilligard-muller_b1868` vs `Lourensz, H___Ceylon___1934`

- [PASS] surname_gate: bio 'LOUWRENS' vs stint 'Lourensz, H' (fuzzy:2)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H']
- [PASS] age_gate: stint starts 1934, birth 1868 (age 66)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1940
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

