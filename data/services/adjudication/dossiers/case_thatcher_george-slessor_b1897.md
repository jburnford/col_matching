<!-- {"case_id": "case_thatcher_george-slessor_b1897", "bio_ids": ["thatcher_george-slessor_b1897"], "stint_ids": ["Thatcher, G. S___Straits Settlements___1925"]} -->
# Dossier case_thatcher_george-slessor_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `thatcher_george-slessor_b1897`

- Printed name: **THATCHER, GEORGE SLESSOR**
- Birth year: 1897 (attested in editions [1939, 1940])
- Honours: A.M.I.C.E, A.M.I.W.E
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71128.v` — printed in editions [1939, 1940]:**

> THATCHER, GEORGE SLESSOR, A.M.I.C.E., A.M.I.W.E., Chtd. Civ. Engrnr.—B.1897; ed. Ven. Bede Colleg. Schl.; astt. engrnr., P.W.D., Malaya, June, 1924; ex. engrnr., June, 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | astt. engrnr., P.W.D. | Malaya | [1939, 1940] |
| 1 | 1933 | ex. engrnr | Malaya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Thatcher, G. S___Straits Settlements___1925`

- Staff-list name: **Thatcher, G. S** | colony: **Straits Settlements** | listed 1925–1939 | editions [1925, 1931, 1933, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | G. S. Thatcher | Assistant Engineer | Public Works | — | — |
| 1931 | G. S. Thatcher | Assistant Engineer | Public Works | — | — |
| 1933 | G. S. Thatcher | Assistant Engineers | Public Works | — | — |
| 1934 | G. S. Thatcher | Executive Engineer | Public Works | — | — |
| 1939 | G. S. Thatcher | Executive Engineers | Public Works | — | — |

### Deterministic checks: `thatcher_george-slessor_b1897` vs `Thatcher, G. S___Straits Settlements___1925`

- [PASS] surname_gate: bio 'THATCHER' vs stint 'Thatcher, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1925, birth 1897 (age 28)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1939
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

