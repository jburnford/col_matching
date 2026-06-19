<!-- {"case_id": "case_reed_john-ranken_b1864", "bio_ids": ["reed_john-ranken_b1864"], "stint_ids": ["Reed, James___Victoria___1900"]} -->
# Dossier case_reed_john-ranken_b1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 31 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reed_john-ranken_b1864`

- Printed name: **REED, JOHN RANKEN**
- Birth year: 1864 (attested in editions [1922, 1923, 1925, 1927, 1928, 1929, 1930, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: C.B.E (1919), Kt. Bach (1936)
- Appears in editions: [1922, 1923, 1925, 1927, 1928, 1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1922-L55612.v` — printed in editions [1922, 1923, 1925, 1927, 1928, 1929, 1930, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> REED, HON. SIR JOHN RANKEN, Kt. Bach. (1936), C.B.E. (1919).—B. 1864; ed. Gram. Schl., Auckland, N.Z.; Victoria Coll., Jersey, and Clare Coll., Cambridge; judge, N.Z. sup. ct., 1921-39; pres., prions bd., 1928; judge advoc.-gen., N.Z. Defence Forces, with rank of colonel, 1911-33.

**Version `col1932-L63409.v` — printed in editions [1932]:**

> REED, HON. HON. RANKEN, C.B.E. (1919).—B. 1864; ed. Gram. Schl., Auckland, N.Z., Victoria Coll., Jersey, and Clare Coll., Cambridge; judge, N.Z. sup. ct., 1921; pres., prisons bd., 1928; is judge advoc.-gen., N.Z. Defence Forces, with rank of colonel.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911–1933 | judge advoc.-gen., N.Z. Defence Forces, with rank of colonel | New Zealand *(inherited from previous clause)* | [1922, 1923, 1925, 1927, 1928, 1929, 1930, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1921–1939 | judge, N.Z. sup. ct | New Zealand | [1922, 1923, 1925, 1927, 1928, 1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1928 | pres., prions bd | New Zealand *(inherited from previous clause)* | [1922, 1923, 1925, 1927, 1928, 1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Reed, James___Victoria___1900`

- Staff-list name: **Reed, James** | colony: **Victoria** | listed 1900–1917 | editions [1900, 1906, 1907, 1908, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | J. M. Reed | Commissioner | Land Tax Commission | — | — |
| 1900 | J. M. Reed | Surrogate-General | Department of Lands and Survey | — | — |
| 1906 | J. M. Reed | Commissioner | Land Tax Commission | — | — |
| 1906 | J. M. Reed | Surveyor-General | Lands and Survey | — | — |
| 1907 | J. M. Reed | Commissioner | Land Tax Commission | — | — |
| 1907 | J. M. Reed | Surveyor-General | Department of Lands and Survey | — | — |
| 1908 | J. M. Reed | Commissioner | Land Tax Commission | — | — |
| 1908 | J. M. Reed | Surveyor-General | Department of Lands and Survey | — | — |
| 1917 | J. M. Reed | Secretary for Lands | Department of Lands and Survey | — | — |

### Deterministic checks: `reed_john-ranken_b1864` vs `Reed, James___Victoria___1900`

- [PASS] surname_gate: bio 'REED' vs stint 'Reed, James' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J']
- [PASS] age_gate: stint starts 1900, birth 1864 (age 36)
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1917
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

