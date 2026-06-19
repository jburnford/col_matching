<!-- {"case_id": "case_powell_george-maurice-caler_b1892", "bio_ids": ["powell_george-maurice-caler_b1892"], "stint_ids": ["Powell, G. M. C___Northern Rhodesia___1925"]} -->
# Dossier case_powell_george-maurice-caler_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Powell, G. M. C___Northern Rhodesia___1925` is also gate-compatible with biography(ies) outside this case: ['powell_george-maurice-caleb_b1892', 'powell_grant_b1819'] (already linked elsewhere or filtered).

## Biography `powell_george-maurice-caler_b1892`

- Printed name: **POWELL, GEORGE MAURICE CALER**
- Birth year: 1892 (attested in editions [1940])
- Honours: D.P.H, F.R.C.S.I, R.C.P.S.I
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67682.v` — printed in editions [1940]:**

> POWELL, GEORGE MAURICE CALER, L.R.C.P.I. & L.M., L.R.C.S.I. & L.M., D.P.H., R.C.P.S.I., D.T.M. & H. (Eng.), F.R.C.S.I.—B. 1892; mily. serv., 1914-18; N. Rhodesia, med. offr., 1920; senr. med. offr., Tanganyika Territory, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1918 | mily. serv | — | [1940] |
| 1 | 1920 | N. Rhodesia, med. offr | — | [1940] |
| 2 | 1938 | senr. med. offr., Tanganyika Territory | Tanganyika | [1940] |

## Candidate stint `Powell, G. M. C___Northern Rhodesia___1925`

- Staff-list name: **Powell, G. M. C** | colony: **Northern Rhodesia** | listed 1925–1937 | editions [1925, 1927, 1928, 1929, 1930, 1931, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | G. M. C. Powell | Medical Officer | Medical | — | — |
| 1927 | G. M. C. Powell | Medical Officer | Medical | — | — |
| 1928 | G. M. C. Powell | Medical Officer | Medical | — | — |
| 1929 | G. M. C. Powell | Medical Officers | Health | — | — |
| 1930 | G. M. C. Powell | Medical Officers | Health | — | — |
| 1931 | G. M. C. Powell | Medical Officer | Health | — | — |
| 1933 | G. M. C. Powell | Medical Officers | Health | — | — |
| 1934 | G. M. C. Powell | Medical Officers | Health | — | — |
| 1936 | G. M. C. Powell | Medical and Health Officer | Medical | — | — |
| 1937 | G. M. C. Powell | Medical Officer | Medical | — | — |

### Deterministic checks: `powell_george-maurice-caler_b1892` vs `Powell, G. M. C___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'POWELL' vs stint 'Powell, G. M. C' (exact)
- [PASS] initials: bio ['G', 'M', 'C'] ~ stint ['G', 'M', 'C']
- [PASS] age_gate: stint starts 1925, birth 1892 (age 33)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1937
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

