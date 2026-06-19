<!-- {"case_id": "case_harkness_j_b1896", "bio_ids": ["harkness_j_b1896"], "stint_ids": ["Harkness, J. W. P___Palestine___1921"]} -->
# Dossier case_harkness_j_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['harkness_j_b1896'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Harkness, J. W. P___Palestine___1921` is also gate-compatible with biography(ies) outside this case: ['harkness_joseph-welsh-park_b1890'] (already linked elsewhere or filtered).

## Biography `harkness_j_b1896`

- Printed name: **HARKNESS, J**
- Birth year: 1896 (attested in editions [1933, 1935, 1937, 1940])
- Honours: D.T.M, F.R.C.S
- Appears in editions: [1933, 1934, 1935, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L60461.v` — printed in editions [1933, 1935, 1937, 1940]:**

> HARKNESS, J., F.R.C.S., L.R.C.P. & L.R.C.S. & L.R.F.P.S. (Edin. & Glas.), L.D.S. (Ed.), D.T.M., D.T.H. (Liv.).—B. 1896; mily. serv., 1914-19; med. offr., Tanganyika Territory, Sept., 1927.

**Version `col1934-L59939.v` — printed in editions [1934]:**

> ARKNESS, J., L.R.C.P. & L.R.C.S. & F.P.S. (Edn.& Glas.), L.D.S. (Ed.), D.T.M., H. (Liv.).—B. 1896; mily. serv., 1914-19; offr., Tanganyika Territory, Sept., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | mily. serv | — | [1933, 1934, 1935, 1937, 1940] |
| 1 | 1927 | med. offr., Tanganyika Territory | Tanganyika | [1933, 1934, 1935, 1937, 1940] |

## Candidate stint `Harkness, J. W. P___Palestine___1921`

- Staff-list name: **Harkness, J. W. P** | colony: **Palestine** | listed 1921–1940 | editions [1921, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. W. P. Harkness | Director of Quarantine and Relief | Public Health | — | — |
| 1923 | J. W. P. Harkness | Deputy Assistant Director | DEPARTMENT OF HEALTH | — | — |
| 1925 | J. W. P. Harkness | Deputy Assistant Director | Department of Health | — | — |
| 1927 | J. W. P. Harkness | Senior Medical Officer | Department of Health | — | — |
| 1928 | J. W. P. Harkness | Senior Medical Officer | Department of Health | — | — |
| 1929 | J. W. P. Harkness | Senior Medical Officers | Department of Health | — | — |
| 1930 | J. W. P. Harkness | Senior Medical Officers | Department of Health | — | — |
| 1931 | J. W. P. Harkness | Deputy Director | Department of Health | — | — |
| 1932 | J. W. P. Harkness | Deputy Director | Department of Health | — | — |
| 1940 | J. W. P. Harkness | Deputy Director | Department of Health | O.B.E. | — |

### Deterministic checks: `harkness_j_b1896` vs `Harkness, J. W. P___Palestine___1921`

- [PASS] surname_gate: bio 'HARKNESS' vs stint 'Harkness, J. W. P' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'W', 'P']
- [PASS] age_gate: stint starts 1921, birth 1896 (age 25)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1940
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

