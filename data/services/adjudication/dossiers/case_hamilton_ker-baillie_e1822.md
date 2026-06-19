<!-- {"case_id": "case_hamilton_ker-baillie_e1822", "bio_ids": ["hamilton_ker-baillie_e1822"], "stint_ids": ["Hamilton, K.B___Leeward Islands___1886", "Hamilton, K___Nigeria___1918"]} -->
# Dossier case_hamilton_ker-baillie_e1822

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 105 official(s) with this surname in the graph's staff lists; 44 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hamilton, K___Nigeria___1918` is also gate-compatible with biography(ies) outside this case: ['hamilton_kyrie-claude_b1894'] (already linked elsewhere or filtered).

## Biography `hamilton_ker-baillie_e1822`

- Printed name: **HAMILTON, Ker Baillie**
- Birth year: not printed
- Honours: C.B.
- Terminal: retired 1867 — “retired on pension, 1867.”
- Appears in editions: [1883, 1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1883-L27843.v` — printed in editions [1883, 1886, 1888, 1889]:**

> HAMILTON, Ker Baillie, C.B.—Educated for the army at the Royal Military Academy at Woolwich; entered the Indian military service in 1822; appointed a writer in the civil service of the Mauritius in 1826, and assistant private secretary to governor Sir Lowry Cole; clerk of the council, at the Cape of Good Hope, in 1829; afterwards acted there as colonial secretary; appointed lieutenant-governor of Grenada, in 1846; administrator of the government of Barbados and the Windward Islands in 1851; governor of Newfoundland, in 1852; governor-in-chief of Antigua and the Leeward Islands, in 1855, to Jan. 1868; retired on pension, 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1822 | Indian military service | — | [1883, 1886, 1888, 1889] |
| 1 | 1826 | writer in the civil service and assistant private secretary to governor | Mauritius | [1883, 1886, 1888, 1889] |
| 2 | 1829 | clerk of the council | Cape of Good Hope | [1883, 1886, 1888, 1889] |
| 3 | 1846 | lieutenant-governor | Grenada | [1883, 1886, 1888, 1889] |
| 4 | 1851 | administrator of the government | Barbados and the Windward Islands | [1883, 1886, 1888, 1889] |
| 5 | 1852 | governor | Newfoundland | [1883, 1886, 1888, 1889] |
| 6 | 1855–1868 | governor-in-chief | Antigua and the Leeward Islands | [1883, 1886, 1888, 1889] |
| 7 | ? | acting colonial secretary | Cape of Good Hope | [1883, 1886, 1888, 1889] |

## Candidate stint `Hamilton, K.B___Leeward Islands___1886`

- Staff-list name: **Hamilton, K.B** | colony: **Leeward Islands** | listed 1886–1889 | editions [1886, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | K. B. Hamilton | — | Governors | C.B. | — |

### Deterministic checks: `hamilton_ker-baillie_e1822` vs `Hamilton, K.B___Leeward Islands___1886`

- [PASS] surname_gate: bio 'HAMILTON' vs stint 'Hamilton, K.B' (exact)
- [PASS] initials: bio ['K', 'B'] ~ stint ['K', 'B']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.B.
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hamilton, K___Nigeria___1918`

- Staff-list name: **Hamilton, K** | colony: **Nigeria** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | K. Hamilton | Sixty‑four Assistant District Officer | Northern Provinces | — | — |
| 1919 | K. Hamilton | Sixty-four Assistant District Officers | NORTHERN PROVINCES | — | — |

### Deterministic checks: `hamilton_ker-baillie_e1822` vs `Hamilton, K___Nigeria___1918`

- [PASS] surname_gate: bio 'HAMILTON' vs stint 'Hamilton, K' (exact)
- [PASS] initials: bio ['K', 'B'] ~ stint ['K']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
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

