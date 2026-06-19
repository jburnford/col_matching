<!-- {"case_id": "case_stephens_william-wilberforce_e1852", "bio_ids": ["stephens_william-wilberforce_e1852"], "stint_ids": ["Stephens, W___South Australia___1877", "Stephens, W___South Australia___1888"]} -->
# Dossier case_stephens_william-wilberforce_e1852

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 40 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stephens_william-wilberforce_e1852`

- Printed name: **STEPHENS, WILLIAM WILBERFORCE**
- Birth year: not printed
- Appears in editions: [1907]

### Verbatim printed entry text (OCR)

**Version `col1907-L47082.v` — printed in editions [1907]:**

> STEPHENS, WILLIAM WILBERFORCE.—Clk., col. secretariat, N. S. Wales, 1852; priv. sec. to various premiers, 1856-58; clk., land dept., 1858; undersec. for lands, 1870; sec., atty.-gen.'s dept., 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | Clk., col. secretariat, N. S. Wales | Nova Scotia | [1907] |
| 1 | 1856–1858 | priv. sec. to various premiers | Nova Scotia *(inherited from previous clause)* | [1907] |
| 2 | 1858 | clk., land dept | Nova Scotia *(inherited from previous clause)* | [1907] |
| 3 | 1870 | undersec. for lands | Nova Scotia *(inherited from previous clause)* | [1907] |
| 4 | 1880 | sec., atty.-gen.'s dept | Nova Scotia *(inherited from previous clause)* | [1907] |

## Candidate stint `Stephens, W___South Australia___1877`

- Staff-list name: **Stephens, W** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Stephens | Draftsman | Engineer-in-Chief's Department | — | — |
| 1878 | W. Stephens | — | Engineer-in-Chief's Department | — | — |
| 1879 | W. Stephens | Draftsmen | Engineer-in-Chief's Department | — | — |
| 1880 | W. Stephens | Draughtsman | Engineer-in-Chief's Department | — | — |

### Deterministic checks: `stephens_william-wilberforce_e1852` vs `Stephens, W___South Australia___1877`

- [PASS] surname_gate: bio 'STEPHENS' vs stint 'Stephens, W' (exact)
- [PASS] initials: bio ['W', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stephens, W___South Australia___1888`

- Staff-list name: **Stephens, W** | colony: **South Australia** | listed 1888–1896 | editions [1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | W. Stephens | — | Engineer-in-Chief's Department | — | — |
| 1889 | W. Stephens | Draughtsmen | Engineer-in-Chief's Department | — | — |
| 1890 | W. Stephens | — | Engineer-in-Chief's Department | — | — |
| 1894 | W. Stephens | Draughtsmen | Engineer-in-Chief's Department | — | — |
| 1896 | W. Stephens | Draughtsmen | Engineer-in-Chief's Department | — | — |

### Deterministic checks: `stephens_william-wilberforce_e1852` vs `Stephens, W___South Australia___1888`

- [PASS] surname_gate: bio 'STEPHENS' vs stint 'Stephens, W' (exact)
- [PASS] initials: bio ['W', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1896
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

