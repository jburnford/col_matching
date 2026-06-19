<!-- {"case_id": "case_wiltshire_h-g_e1914", "bio_ids": ["wiltshire_h-g_e1914"], "stint_ids": ["Wiltshire, H. G___Nyasaland___1928", "Wiltshire, H. G___Zanzibar___1932"]} -->
# Dossier case_wiltshire_h-g_e1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wiltshire_h-g_e1914`

- Printed name: **WILTSHIRE, H. G.**
- Birth year: not printed
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L64589.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> WILTSHIRE, H. G., M.A., M.B., B.Chir. (Cantab.), M.R.C.S., L.R.C.P., D.P.H., D.T.M. & H.—Ed. Cheltenham Coll.; exhibr. Emmanuel Coll., Cambridge (coll. prize); L.S.T.M. certif. with distinc. (2nd place); war serv., 1914-19; France, Gallipoli, Egypt, Palestine (1914 Star with clasp); bacteriological specialist, R.A.M.C., 1916-19; med. offr., Nyasaland, 1924; do., Zanzibar, 1930; pathologist, 1932; senr. do., Uganda, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | war serv. | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1916–1919 | bacteriological specialist | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1924–1924 | med. offr. | Nyasaland | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1930–1930 | med. offr. | Zanzibar | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1932–1932 | pathologist | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1937–1937 | senr. pathologist | Uganda | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Wiltshire, H. G___Nyasaland___1928`

- Staff-list name: **Wiltshire, H. G** | colony: **Nyasaland** | listed 1928–1930 | editions [1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | H. G. Wiltshire | Medical Officers | Medical | — | — |
| 1929 | H. G. Wiltshire | Medical Officer | Medical | — | — |
| 1930 | H. G. Wiltshire | Medical Officer | Medical | — | — |

### Deterministic checks: `wiltshire_h-g_e1914` vs `Wiltshire, H. G___Nyasaland___1928`

- [PASS] surname_gate: bio 'WILTSHIRE' vs stint 'Wiltshire, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1928; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Wiltshire, H. G___Zanzibar___1932`

- Staff-list name: **Wiltshire, H. G** | colony: **Zanzibar** | listed 1932–1937 | editions [1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | H. G. Wiltshire | Medical Officer | Medical Department | — | — |
| 1933 | H. G. Wiltshire | Pathologist | Medical Department | — | — |
| 1934 | H. G. Wiltshire | Pathologist | Medical Department | — | — |
| 1936 | H. G. Wiltshire | Pathologist | Medical Department | — | — |
| 1937 | H. G. Wiltshire | Pathologist | Medical Department | — | — |

### Deterministic checks: `wiltshire_h-g_e1914` vs `Wiltshire, H. G___Zanzibar___1932`

- [PASS] surname_gate: bio 'WILTSHIRE' vs stint 'Wiltshire, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1932; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1937
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

