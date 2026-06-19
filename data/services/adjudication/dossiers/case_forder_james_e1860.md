<!-- {"case_id": "case_forder_james_e1860", "bio_ids": ["forder_james_e1860"], "stint_ids": ["Forder, J___Natal___1877"]} -->
# Dossier case_forder_james_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['forder_james_e1860'] carry a single initial only — the namesake trap applies.

## Biography `forder_james_e1860`

- Printed name: **FORDER, JAMES**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1889, 1890, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1883-L27494.v` — printed in editions [1883, 1886, 1889, 1890, 1896, 1897]:**

> FORDER, JAMES, graduated at the University of Cambridge, as B.A., in 1860; head-master of High School, Pietermaritzburg, July, 1868; acting master and registrar, supreme court, March, 1878; acting chief clerk, colonial office, Aug., 1878; resident magistrate for the colony, 18th Mar., 1880; justice of the peace for the Colony 13th Oct., 1880; now R.M. of Umgeni division, Pietermaritzburg.

**Version `col1898-L33387.v` — printed in editions [1898, 1899]:**

> FORDER, JAMES.—B.A., Camb., 1860; headmstr. High Schl., Pietermaritzburg, July, 1868; ag. master and registr., sup. ct., Mar., 1878; ag. ch. clk., C.O., 1878; res. mag., 1880; J.P., 1880; now R.M. of Umgani div., Pietermaritzburg.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860–1860 | — | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 1 | 1860 | B.A., Camb | — | [1898, 1899] |
| 2 | 1868–1868 | head-master of High School | Pietermaritzburg | [1883, 1886, 1889, 1890, 1896, 1897] |
| 3 | 1868 | headmstr. High Schl., Pietermaritzburg | — | [1898, 1899] |
| 4 | 1878–1878 | acting master and registrar, supreme court | — | [1883, 1886, 1889, 1890, 1896, 1897, 1898, 1899] |
| 5 | 1878–1878 | acting chief clerk, colonial office | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 6 | 1878 | ag. ch. clk. | Colonial Office | [1898, 1899] |
| 7 | 1880–1880 | resident magistrate | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 8 | 1880–1880 | justice of the peace | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 9 | 1880 | res. mag | Colonial Office *(inherited from previous clause)* | [1898, 1899] |
| 10 | ? | R.M. of Umgeni division | Pietermaritzburg | [1883, 1886, 1889, 1890, 1896, 1897] |

## Candidate stint `Forder, J___Natal___1877`

- Staff-list name: **Forder, J** | colony: **Natal** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Forder | Head Master, High School | Education | — | — |
| 1879 | J. Forder | Chief Clerk | Colonial Secretary's Department | — | — |
| 1880 | J. Forder | Chief Clerk | Colonial Secretary's Department | — | — |

### Deterministic checks: `forder_james_e1860` vs `Forder, J___Natal___1877`

- [PASS] surname_gate: bio 'FORDER' vs stint 'Forder, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

