<!-- {"case_id": "case_emberton_john-james_b1893", "bio_ids": ["emberton_john-james_b1893"], "stint_ids": ["Pemberton, Jane___Dominica___1909"]} -->
# Dossier case_emberton_john-james_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `emberton_john-james_b1893`

- Printed name: **EMBERTON, JOHN JAMES**
- Birth year: 1893 (attested in editions [1939, 1940])
- Honours: M.C.
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L66545.v` — printed in editions [1939, 1940]:**

> EMBERTON, JOHN JAMES, M.C.—B. 1893; ed. Newcastle-under-Lyme, Staffs.; mily. serv. 1914-19, England, Egypt, Belgium, France and Germany; admnstr. offr., cls. IV., Nigeria, 1920; do., cls. III., 1929; do., cls. I., 1936; comsnr. of col., Lagos, 1937; prin. asst. sec., secret., and ag. dir., transport, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | mily. serv. | — | [1939, 1940] |
| 1 | 1920 | admnstr. offr., cls. IV. | Nigeria | [1939, 1940] |
| 2 | 1929 | admnstr. offr., cls. III. | — | [1939, 1940] |
| 3 | 1936 | admnstr. offr., cls. I. | — | [1939, 1940] |
| 4 | 1937 | comsnr. of col. | Lagos | [1939, 1940] |
| 5 | 1939 | prin. asst. sec., secret., and ag. dir., transport | — | [1939, 1940] |

## Candidate stint `Pemberton, Jane___Dominica___1909`

- Staff-list name: **Pemberton, Jane** | colony: **Dominica** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | Miss Jane Pemberton | Educational Officer, Roseau | Educational Establishment | — | — |
| 1910 | Jane Pemberton | Educational Officer, Roseau | Educational Establishment | — | — |

### Deterministic checks: `emberton_john-james_b1893` vs `Pemberton, Jane___Dominica___1909`

- [PASS] surname_gate: bio 'EMBERTON' vs stint 'Pemberton, Jane' (fuzzy:1)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1909, birth 1893 (age 16)
- [FAIL] colony: no placed event resolves to 'Dominica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1910
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

