<!-- {"case_id": "case_target_b-a-g_b1921", "bio_ids": ["target_b-a-g_b1921"], "stint_ids": ["Target, B. A. G___Zanzibar___1961"]} -->
# Dossier case_target_b-a-g_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `target_b-a-g_b1921`

- Printed name: **TARGET, B. A. G**
- Birth year: 1921 (attested in editions [1962])
- Appears in editions: [1962]

### Verbatim printed entry text (OCR)

**Version `col1962-L27040.v` — printed in editions [1962]:**

> TARGET, B. A. G.—b. 1921; ed. Christ's Hosp., Queens' Coll. Camb.; mil. serv. 1941–46; cr. coun. Tang., 1951; secon., Zanz. 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | cr. coun. Tang | — | [1962] |
| 1 | 1957 | secon. | Zanzibar | [1962] |

## Candidate stint `Target, B. A. G___Zanzibar___1961`

- Staff-list name: **Target, B. A. G** | colony: **Zanzibar** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | B. A. G. Target | Crown Counsel | Civil Establishment | — | — |
| 1962 | B. A. G. Target | Crown Counsels | Law Officers | — | — |

### Deterministic checks: `target_b-a-g_b1921` vs `Target, B. A. G___Zanzibar___1961`

- [PASS] surname_gate: bio 'TARGET' vs stint 'Target, B. A. G' (exact)
- [PASS] initials: bio ['B', 'A', 'G'] ~ stint ['B', 'A', 'G']
- [PASS] age_gate: stint starts 1961, birth 1921 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1961-1962
- [FAIL] position_sim: best 56 vs bar 60: 'secon.' ~ 'Crown Counsel'
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

