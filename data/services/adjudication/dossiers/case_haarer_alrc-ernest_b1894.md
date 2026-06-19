<!-- {"case_id": "case_haarer_alrc-ernest_b1894", "bio_ids": ["haarer_alrc-ernest_b1894", "haarker_alec-ernest_b1896"], "stint_ids": ["Haarer, A. E___Tanganyika___1922"]} -->
# Dossier case_haarer_alrc-ernest_b1894

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Haarer, A. E___Tanganyika___1922'] have more than one claimant biography in this case.

## Biography `haarer_alrc-ernest_b1894`

- Printed name: **HAARER, ALRC ERNEST**
- Birth year: 1894 (attested in editions [1934, 1935, 1937])
- Honours: F.L.S
- Appears in editions: [1934, 1935, 1937]

### Verbatim printed entry text (OCR)

**Version `col1934-L59862.v` — printed in editions [1934, 1935, 1937]:**

> HAARER, ALRC ERNEST, F.L.S.—B. 1894; ed. Birkenhead Inst., Battersea Gram. Schol. and Royal Horticultural Coll. (dipl. hort.); dist. agrl. offr., Tanganyika Territory, 1921; agrl. lect., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | dist. agrl. offr., Tanganyika Territory | Tanganyika | [1934, 1935, 1937] |
| 1 | 1930 | agrl. lect | Tanganyika *(inherited from previous clause)* | [1934, 1935, 1937] |

## Biography `haarker_alec-ernest_b1896`

- Printed name: **HAARKER, Alec Ernest**
- Birth year: 1896 (attested in editions [1936])
- Honours: F.L.S
- Appears in editions: [1936]

### Verbatim printed entry text (OCR)

**Version `col1936-L61285.v` — printed in editions [1936]:**

> HAARKER, Alec Ernest, F.L.S.—B. 1896; ed. Birkenhead Inst., Battersea Gram. Schl. and Royal Horticultural Coll. (dipl. hort.); dist. agril. offr., Tanganyika Territory, 1921; agril. lect., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | dist. agril. offr., Tanganyika Territory | Tanganyika | [1936] |
| 1 | 1930 | agril. lect | Tanganyika *(inherited from previous clause)* | [1936] |

## Candidate stint `Haarer, A. E___Tanganyika___1922`

- Staff-list name: **Haarer, A. E** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. E. Haarer | District Agricultural Officers | Agriculture | — | — |
| 1923 | A. E. Haarer | District Agricultural Officers | Agriculture | — | — |
| 1924 | A. E. Haarer | District Agricultural Officers | Agriculture | — | — |
| 1925 | A. E. Haarer | District Agricultural Officers | Agriculture | — | — |

### Deterministic checks: `haarer_alrc-ernest_b1894` vs `Haarer, A. E___Tanganyika___1922`

- [PASS] surname_gate: bio 'HAARER' vs stint 'Haarer, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1922, birth 1894 (age 28)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 49 vs bar 60: 'dist. agrl. offr., Tanganyika Territory' ~ 'District Agricultural Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `haarker_alec-ernest_b1896` vs `Haarer, A. E___Tanganyika___1922`

- [PASS] surname_gate: bio 'HAARKER' vs stint 'Haarer, A. E' (fuzzy:1)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 52 vs bar 60: 'dist. agril. offr., Tanganyika Territory' ~ 'District Agricultural Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

