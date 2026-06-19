<!-- {"case_id": "case_hake_walter-conway_e1902", "bio_ids": ["hake_walter-conway_e1902"], "stint_ids": ["Hake, W. C___Hong Kong___1921"]} -->
# Dossier case_hake_walter-conway_e1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hake_walter-conway_e1902`

- Printed name: **HAKE, WALTER CONWAY**
- Birth year: not printed
- Appears in editions: [1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1924-L54845.v` — printed in editions [1924, 1925]:**

> HAKE, WALTER CONWAY.—H.M.S. "Conway," 1902-1904; midshipman, R.N.R.; served in H.M.S. "Essex," 1908; H.M.S. "Roxburgh," 1910; H.M.S. "Leander," 1912; in command, West Indian Mail Steamers, 1913-14; navigating lieut., H.M.S. "Edinburgh Castle," 1914-1917; navigating lieut., H.M.S. "Tyne," 1918; elected a younger brother of Trinity House; in commd., H.M.S. "Fame" (China Station), 1918-1920; elected F.R.G.S., 1923; awarded the R.D., promoted to lieut. commdr. and placed on the retired list; ag. ast. harbmr., and apptd. ast. harbmr., 1920; ag. harbmr., 1921, 1923 and 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1904 | — | — | [1924, 1925] |
| 1 | 1908–1908 | served | — | [1924, 1925] |
| 2 | 1910–1910 | — | — | [1924, 1925] |
| 3 | 1912–1912 | — | — | [1924, 1925] |
| 4 | 1913–1914 | in command | West Indies | [1924, 1925] |
| 5 | 1914–1917 | navigating lieut. | — | [1924, 1925] |
| 6 | 1918–1918 | navigating lieut. | — | [1924, 1925] |
| 7 | 1918–1920 | in commd. | China | [1924, 1925] |
| 8 | 1920–1920 | ag. ast. harbmr., and apptd. ast. harbmr. | — | [1924, 1925] |
| 9 | 1921–1924 | ag. harbmr. | — | [1924, 1925] |
| 10 | 1923–1923 | — | — | [1924, 1925] |

## Candidate stint `Hake, W. C___Hong Kong___1921`

- Staff-list name: **Hake, W. C** | colony: **Hong Kong** | listed 1921–1925 | editions [1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | W. C. Hake | Assistant Harbour Master | Harbour Office | — | — |
| 1922 | W. C. Hake | Assistant Harbour Master, Lieut.-Commander | Harbour Office | — | — |
| 1923 | W. C. Hake | Assistant Harbour Master | Harbour Office | — | — |
| 1924 | W. C. Hake | Assistant Harbour Master, Lieut.-Commander | Harbour Office | — | — |
| 1925 | W. C. Hake | Assistant Harbour Master | Harbour Office | — | — |

### Deterministic checks: `hake_walter-conway_e1902` vs `Hake, W. C___Hong Kong___1921`

- [PASS] surname_gate: bio 'HAKE' vs stint 'Hake, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

