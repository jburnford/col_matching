<!-- {"case_id": "case_wade_t-g-rochfort_b1901", "bio_ids": ["wade_t-g-rochfort_b1901"], "stint_ids": ["Wade, T. G. Rochfort___Windward Islands___1933"]} -->
# Dossier case_wade_t-g-rochfort_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wade, T. G. Rochfort___Windward Islands___1933` is also gate-compatible with biography(ies) outside this case: ['wade_robert_e1882'] (already linked elsewhere or filtered).

## Biography `wade_t-g-rochfort_b1901`

- Printed name: **WADE, T. G. Rochfort**
- Birth year: 1901 (attested in editions [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: F.R.G.S, M.A
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L64754.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> WADE, Capt. T. G. Rochfort, M.A., F.R.G.S.—B. 1901; ed. King William's Coll., Isle of Man, and St. Columba's Coll., Dublin; B.A., Trinity Coll., Dublin, 1926; M.A., 1930; inspr., schls., St. Lucia, May, 1931; C.O., St. Lucia Volunteer Forces; headmast., Grammar Schl., St. Vincent, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | B.A., Trinity Coll., Dublin | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1930 | M.A | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1931 | inspr., schls. | St. Lucia | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1938 | headmast., Grammar Schl. | St. Vincent | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Wade, T. G. Rochfort___Windward Islands___1933`

- Staff-list name: **Wade, T. G. Rochfort** | colony: **Windward Islands** | listed 1933–1937 | editions [1933, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | Capt. The Rev. T. G. Wade | Inspector of Schools | Education Department | — | Captain |
| 1936 | T. G. Wade | Inspector of Schools | Education Department | — | Captain |
| 1936 | Captain T. G. Rochfort Wade | Inspector of Schools | Legislative Council | — | Captain |
| 1937 | T. G. Rochfort Wade | Officer Commanding | St. Lucia Volunteers | — | Captain |
| 1937 | Capt. The Rev. T. G. Roohfort Wade | Inspector of Schools | Education Department | — | Captain |

### Deterministic checks: `wade_t-g-rochfort_b1901` vs `Wade, T. G. Rochfort___Windward Islands___1933`

- [PASS] surname_gate: bio 'WADE' vs stint 'Wade, T. G. Rochfort' (exact)
- [PASS] initials: bio ['T', 'G', 'R'] ~ stint ['T', 'G', 'R']
- [PASS] age_gate: stint starts 1933, birth 1901 (age 32)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1937
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

