<!-- {"case_id": "case_churchill_j-f_e1859", "bio_ids": ["churchill_j-f_e1859"], "stint_ids": ["Churchill, J. F___Ceylon___1877"]} -->
# Dossier case_churchill_j-f_e1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `churchill_j-f_e1859`

- Printed name: **CHURCHILL, J. F.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26837.v` — printed in editions [1883]:**

> CHURCHILL, J. F.—Assistant civil engineer and commissioner of roads, Ceylon, 1866; acted as civil engineer, &c., of the island, 1859 to 1861; proceeded to England, July, 1861, where he was employed, under the direction of the secretary of state, on duty connected with the proposed Ceylon railway; provincial assistant, southern province, March, 1866; acting provincial assistant, central province, north, July, 1866; resumed duties in the southern province, March, 1868; appointed to central province, 1874; acting director public works, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859–1861 | acted as civil engineer, &c. | — | [1883] |
| 1 | 1861 | — | England | [1883] |
| 2 | 1866 | Assistant civil engineer and commissioner of roads | Ceylon | [1883] |
| 3 | 1866 | provincial assistant | — | [1883] |
| 4 | 1868 | — | — | [1883] |
| 5 | 1874 | — | — | [1883] |
| 6 | 1876 | acting director public works | — | [1883] |

## Candidate stint `Churchill, J. F___Ceylon___1877`

- Staff-list name: **Churchill, J. F** | colony: **Ceylon** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. F. Churchill | Provl. Assistant | Public Works Department | — | — |
| 1878 | J. F. Churchill | Director of Public Works | Public Works Department | — | — |
| 1879 | J. F. Churchill | Director of Public Works (acting) | Public Works Department | — | — |
| 1880 | J. F. Churchill | Director of Public Works (acting) | Public Works Department | — | — |
| 1883 | J. F. Churchill | Director of Public Works | Public Works Department | — | — |

### Deterministic checks: `churchill_j-f_e1859` vs `Churchill, J. F___Ceylon___1877`

- [PASS] surname_gate: bio 'CHURCHILL' vs stint 'Churchill, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

