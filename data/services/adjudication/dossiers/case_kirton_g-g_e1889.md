<!-- {"case_id": "case_kirton_g-g_e1889", "bio_ids": ["kirton_g-g_e1889", "kirton_g-g_e1889-2"], "stint_ids": ["Kirton, G___St Christopher and Nevis___1894"]} -->
# Dossier case_kirton_g-g_e1889

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Kirton, G___St Christopher and Nevis___1894'] have more than one claimant biography in this case.

## Biography `kirton_g-g_e1889`

- Printed name: **KIRTON, G. G**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L32470.v` — printed in editions [1894]:**

> KIRTON, G. G.—Ag. elk., P.O., St. Kitts, 1889; 2nd elk., reg'rs. off., 1892; ag. mag. elk., 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | Ag. elk., P.O. | St. Kitts | [1894] |
| 1 | 1892 | 2nd elk., reg'rs. off | St. Kitts *(inherited from previous clause)* | [1894] |

## Biography `kirton_g-g_e1889-2`

- Printed name: **KIRTON, G. G.**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L39818.v` — printed in editions [1896, 1897, 1898, 1899, 1900]:**

> KIRTON, G. G.—Ag. clk., P.O., St. Kitts, 1889; 2nd clk., registr.'s office, 1892; ag. mag.'s clk., Aug., 1891, to Feb., 1892, and Apr. to Oct., 1893; 1st clk. registr.'s office, May, 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889–1889 | Ag. clk., P.O. | St. Kitts | [1896, 1897, 1898, 1899, 1900] |
| 1 | 1891–1893 | ag. mag.'s clk. | — | [1896, 1897, 1898, 1899, 1900] |
| 2 | 1892–1892 | 2nd clk., registr.'s office | — | [1896, 1897, 1898, 1899, 1900] |
| 3 | 1895–1895 | 1st clk. registr.'s office | — | [1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Kirton, G___St Christopher and Nevis___1894`

- Staff-list name: **Kirton, G** | colony: **St Christopher and Nevis** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | G. Kirton | Clerk | Civil Establishment | — | — |
| 1896 | G. Kirton | 1st Clerk | Judicial Department | — | — |

### Deterministic checks: `kirton_g-g_e1889` vs `Kirton, G___St Christopher and Nevis___1894`

- [PASS] surname_gate: bio 'KIRTON' vs stint 'Kirton, G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'St Christopher and Nevis'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1896
- [FAIL] position_sim: best 31 vs bar 60: '2nd elk., reg'rs. off' ~ '1st Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `kirton_g-g_e1889-2` vs `Kirton, G___St Christopher and Nevis___1894`

- [PASS] surname_gate: bio 'KIRTON' vs stint 'Kirton, G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Christopher and Nevis'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
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

