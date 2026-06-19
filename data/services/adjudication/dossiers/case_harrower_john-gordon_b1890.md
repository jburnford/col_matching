<!-- {"case_id": "case_harrower_john-gordon_b1890", "bio_ids": ["harrower_john-gordon_b1890"], "stint_ids": ["Harrower, J. G___Straits Settlements___1923"]} -->
# Dossier case_harrower_john-gordon_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harrower_john-gordon_b1890`

- Printed name: **HARROWER, JOHN GORDON**
- Birth year: 1890 (attested in editions [1932, 1933, 1934, 1935, 1936])
- Honours: F.R.C.S.E, F.R.S.E, M.B
- Appears in editions: [1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1932-L60933.v` — printed in editions [1932, 1933, 1934, 1935, 1936]:**

> HARROWER, JOHN GORDON, M.B., Ch.B. (Hons.), D.Sc. (Edin.), Ch.M. (Glas.), F.R.C.S.E., F.R.S.E.—B. 1890; prof. of anatomy, King Edward VII Med. Coll., Singapore, Mar., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | prof. of anatomy, King Edward VII Med. Coll. | Singapore | [1932, 1933, 1934, 1935, 1936] |

## Candidate stint `Harrower, J. G___Straits Settlements___1923`

- Staff-list name: **Harrower, J. G** | colony: **Straits Settlements** | listed 1923–1936 | editions [1923, 1925, 1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | J. G. Harrower | Professor of Anatomy | King Edward VII College of Medicine | — | — |
| 1925 | J. G. Harrower | Professor of Anatomy | King Edward VII College of Medicine | — | — |
| 1931 | J. G. Harrower | Professor of Anatomy | King Edward VII College of Medicine | — | — |
| 1933 | J. G. Harrower | Professor of Anatomy | King Edward VII College of Medicine | — | — |
| 1934 | J. G. Harrower | Professor of Anatomy | King Edward VII College of Medicine, Singapore | — | — |
| 1936 | J. G. Harrower | Professor of Anatomy | King Edward VII College of Medicine | — | — |

### Deterministic checks: `harrower_john-gordon_b1890` vs `Harrower, J. G___Straits Settlements___1923`

- [PASS] surname_gate: bio 'HARROWER' vs stint 'Harrower, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
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

