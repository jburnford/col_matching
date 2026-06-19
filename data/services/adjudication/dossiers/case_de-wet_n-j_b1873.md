<!-- {"case_id": "case_de-wet_n-j_b1873", "bio_ids": ["de-wet_n-j_b1873"], "stint_ids": ["de Wet, N. J___South Africa___1914", "de Wet, Nicolaas Jacobus___British Somaliland___1923"]} -->
# Dossier case_de-wet_n-j_b1873

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-wet_n-j_b1873`

- Printed name: **DE WET, N. J**
- Birth year: 1873 (attested in editions [1939, 1940])
- Appears in editions: [1933, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L66263.v` — printed in editions [1939, 1940]:**

> DE WET, THE HON. N.J., K.C.—B. 1873; Min. of just., Union of S. Africa, 1913-24; puisane judge, Transvaal prov. div., 1932; judge of appl., 1937.

**Version `col1933-L59195.v` — printed in editions [1933, 1935, 1936, 1937]:**

> DE WET, THE HON. N. J., K.C.—Min. of just., Union of S. Africa, 1913-24; puisne judge, Transvaal prov. divn., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1924 | Min. of just., Union of S. Africa | — | [1933, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1932 | puisane judge, Transvaal prov. div | Transvaal | [1933, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1937 | judge of appl | Transvaal *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `de Wet, N. J___South Africa___1914`

- Staff-list name: **de Wet, N. J** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | N. J. de Wet | Minister of Justice | Executive Council | K.C. | — |
| 1914 | N. J. de Wet | Minister of Justice | Department of Justice | — | — |
| 1918 | N. J. de Wet | Minister of Justice | Department of Justice | — | — |
| 1918 | The Hon. N. J. de Wet | Minister of Justice | Executive Council | — | — |

### Deterministic checks: `de-wet_n-j_b1873` vs `de Wet, N. J___South Africa___1914`

- [PASS] surname_gate: bio 'DE WET' vs stint 'de Wet, N. J' (exact)
- [PASS] initials: bio ['N', 'J'] ~ stint ['N', 'J']
- [PASS] age_gate: stint starts 1914, birth 1873 (age 41)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `de Wet, Nicolaas Jacobus___British Somaliland___1923`

- Staff-list name: **de Wet, Nicolaas Jacobus** | colony: **British Somaliland** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | Nicolaas Jacobus de Wet | — | Parliament | — | — |
| 1924 | N. J. de Wet | Minister of Justice | Department of Justice | K.C. | — |
| 1925 | Nicolaas Jacobus de Wet | Senator | Senate | — | — |

### Deterministic checks: `de-wet_n-j_b1873` vs `de Wet, Nicolaas Jacobus___British Somaliland___1923`

- [PASS] surname_gate: bio 'DE WET' vs stint 'de Wet, Nicolaas Jacobus' (exact)
- [PASS] initials: bio ['N', 'J'] ~ stint ['N', 'J']
- [PASS] age_gate: stint starts 1923, birth 1873 (age 50)
- [FAIL] colony: no placed event resolves to 'British Somaliland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
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

