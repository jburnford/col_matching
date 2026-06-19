<!-- {"case_id": "case_tull_john-cadman_e1884", "bio_ids": ["tull_john-cadman_e1884"], "stint_ids": ["Tull, J. C___Straits Settlements___1922"]} -->
# Dossier case_tull_john-cadman_e1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tull_john-cadman_e1884`

- Printed name: **TULL, JOHN CADMAN**
- Birth year: not printed
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1932-L64602.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937, 1939]:**

> TULL, JOHN CADMAN.—M.D. (McGill), F.R.C.P. (Lond.).—B.1884; capt., Canadian Army Med. Corps (meutd. in desps.), France, 1915-19; pathologist, Rangoon gen. hosp., 1919; med. offr., gen. hosp., Penang, Jan., 1921; pathologist, Penang, July, 1921; lect., pathology, S'pore, June, 1926; govt. pathologist, S'pore, Aug., 1926; deleg. from King Edward VII Med. Coll. to Intern. cong. on cancer, London, May, 1928; deleg., leprosy confce., Manila, Dec., 1930; pathologist, Cyprus, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | M.D. (McGill), F.R.C.P. (Lond.).—B | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 1 | 1915–1919 | capt., Canadian Army Med. Corps (meutd. in desps.), France | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 2 | 1919 | pathologist, Rangoon gen. hosp | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 3 | 1921 | med. offr., gen. hosp., Penang | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 4 | 1921 | pathologist, Penang | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 5 | 1926 | lect., pathology, S'pore | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 6 | 1928 | deleg. from King Edward VII Med. Coll. to Intern. cong. on cancer, London | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 7 | 1930 | deleg., leprosy confce., Manila | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 8 | 1936 | pathologist | Cyprus | [1932, 1933, 1934, 1935, 1936, 1937, 1939] |

## Candidate stint `Tull, J. C___Straits Settlements___1922`

- Staff-list name: **Tull, J. C** | colony: **Straits Settlements** | listed 1922–1936 | editions [1922, 1923, 1925, 1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | J. C. Tull | Pathologist | Medical | — | — |
| 1923 | J. C. Tull | Pathologist | Medical | — | — |
| 1925 | J. C. Tull | Government Pathologist | PENANG | — | — |
| 1931 | J. C. Tull | Government Pathologist | Medical | — | — |
| 1933 | J. C. Tull | Government Pathologist | Medical | — | — |
| 1934 | J. C. Tull | Government Pathologist | Singapore | — | — |
| 1936 | J. C. Tull | Government Pathologist and Professor of Pathology | Medical | — | — |

### Deterministic checks: `tull_john-cadman_e1884` vs `Tull, J. C___Straits Settlements___1922`

- [PASS] surname_gate: bio 'TULL' vs stint 'Tull, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1936
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

