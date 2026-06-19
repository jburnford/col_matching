<!-- {"case_id": "case_poyser_kenneth-elton-barbados_b1882", "bio_ids": ["poyser_kenneth-elton-barbados_b1882"], "stint_ids": ["Poyser, K. E___Ceylon___1934", "Poyser, Kenneth E___Leeward Islands___1921"]} -->
# Dossier case_poyser_kenneth-elton-barbados_b1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Poyser, K. E___Ceylon___1934` is also gate-compatible with biography(ies) outside this case: ['poyser_kenneth-elliston_b1882'] (already linked elsewhere or filtered).
- NOTE: stint `Poyser, Kenneth E___Leeward Islands___1921` is also gate-compatible with biography(ies) outside this case: ['poyser_kenneth-elliston_b1882'] (already linked elsewhere or filtered).

## Biography `poyser_kenneth-elton-barbados_b1882`

- Printed name: **POYSER, KENNETH ELTON (Barbados)**
- Birth year: 1882 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L64016.v` — printed in editions [1937]:**

> POYSER, KENNETH ELTON (Barbados).—B. 1882; Merton Coll., Oxford; Temple, 1906; served, Eu. L.I., and Loyal N. Lana. Regt. (depts. D.S.O., 1917); puisne judge, Leeward, Sept., 1920; atty.-gen., Barbados, June, atty.-gen., Uganda, 1928; puisne just., n., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | Temple | — | [1937] |
| 1 | 1917 | served, Eu. L.I., and Loyal N. Lana. Regt. (depts. D.S.O | — | [1937] |
| 2 | 1920 | puisne judge, Leeward | — | [1937] |
| 3 | 1928 | atty.-gen., Barbados, June, atty.-gen. | Uganda | [1937] |
| 4 | 1933 | puisne just., n | Uganda *(inherited from previous clause)* | [1937] |

## Candidate stint `Poyser, K. E___Ceylon___1934`

- Staff-list name: **Poyser, K. E** | colony: **Ceylon** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | K. E. Poyser | Puise Justice | Supreme Court | D.S.O. | — |
| 1936 | K. E. Poyser | Puine Justice | Supreme Court | — | — |

### Deterministic checks: `poyser_kenneth-elton-barbados_b1882` vs `Poyser, K. E___Ceylon___1934`

- [PASS] surname_gate: bio 'POYSER' vs stint 'Poyser, K. E' (exact)
- [PASS] initials: bio ['K', 'E'] ~ stint ['K', 'E']
- [PASS] age_gate: stint starts 1934, birth 1882 (age 52)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Poyser, Kenneth E___Leeward Islands___1921`

- Staff-list name: **Poyser, Kenneth E** | colony: **Leeward Islands** | listed 1921–1925 | editions [1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | K. E. Poyser | 2nd Puisne Judge | Judicial Establishment | D.S.O. | Major |
| 1922 | K. E. Poyser | 2nd Puise Judge | Judicial Establishment | D.S.O. | Major |
| 1922 | Kenneth E. Poyser | 2nd Puise Judge | Judicial | D.S.O. | — |
| 1923 | K. E. Poyser | 2nd Puisne Judge | Judicial Establishment | D.S.O. | Major |
| 1923 | Kenneth E. Poyser | 2nd Puisme Judge | Judicial | D.S.O. | — |
| 1924 | Kenneth E. Poyser | 2nd Puime Judge | Judicial and Legal | D.S.O. | — |
| 1924 | K. E. Poyser | 2nd Puisne Judge | Judicial Establishment | D.S.O. | Major |
| 1925 | Kenneth E. Poyser | 2nd Puise Judge | Judicial and Legal | D.S.O. | — |
| 1925 | K. E. Poyser | 2nd Puisne Judge | Judicial Establishment | D.S.O. | Major |

### Deterministic checks: `poyser_kenneth-elton-barbados_b1882` vs `Poyser, Kenneth E___Leeward Islands___1921`

- [PASS] surname_gate: bio 'POYSER' vs stint 'Poyser, Kenneth E' (exact)
- [PASS] initials: bio ['K', 'E'] ~ stint ['K', 'E']
- [PASS] age_gate: stint starts 1921, birth 1882 (age 39)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

