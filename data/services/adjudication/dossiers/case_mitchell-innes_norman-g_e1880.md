<!-- {"case_id": "case_mitchell-innes_norman-g_e1880", "bio_ids": ["mitchell-innes_norman-g_e1880"], "stint_ids": ["Mitchell-Innes, N. G___Hong Kong___1886"]} -->
# Dossier case_mitchell-innes_norman-g_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mitchell-innes_norman-g_e1880`

- Printed name: **MITCHELL-INNES, NORMAN G**
- Birth year: not printed
- Terminal: resigned 1897 — “resigned, 1897.”
- Appears in editions: [1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1898-L34865.v` — printed in editions [1898, 1899]:**

> MITCHELL-INNES, NORMAN G.—Ed. Edin. Acad. and Repton; Hong Kong cadet, 1880; attached to the C.O. for one year, 1881; passed cadet, 1884; ag. astl. col. sec.; astl. registr.-gen., 1884; ag. pol. mag. and coroner, 1886; ag. superint., 1887; called to bar (Mid. Temp.), 1889; ag. registr.-gen., 1889-90; treas., and mem. exec. and legis. couns., 1891; resigned, 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Hong Kong cadet | Hong Kong | [1898, 1899] |
| 1 | 1881 | attached to the C.O. for one year | Colonial Office | [1898, 1899] |
| 2 | 1884 | passed cadet | Colonial Office *(inherited from previous clause)* | [1898, 1899] |
| 3 | 1886 | ag. pol. mag. and coroner | Colonial Office *(inherited from previous clause)* | [1898, 1899] |
| 4 | 1887 | ag. superint | Colonial Office *(inherited from previous clause)* | [1898, 1899] |
| 5 | 1889 | called to bar (Mid. Temp.) | Colonial Office *(inherited from previous clause)* | [1898, 1899] |
| 6 | 1891 | treas., and mem. exec. and legis. couns | Colonial Office *(inherited from previous clause)* | [1898, 1899] |

## Candidate stint `Mitchell-Innes, N. G___Hong Kong___1886`

- Staff-list name: **Mitchell-Innes, N. G** | colony: **Hong Kong** | listed 1886–1897 | editions [1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | N. G. Mitchell-Innes | Assistant Registrar-General | Registrar-General's Department | — | — |
| 1888 | N. G. Mitchell-Innes | Assistant Registrar-General | Registrar-General's Department | — | — |
| 1889 | N. G. Mitchell-Innes | Assistant Registrar-General | Registrar-General's Department | — | — |
| 1890 | N. G. Mitchell-Innes | Assistant Colonial Secretary | Colonial Secretary's Office | — | — |
| 1894 | N. G. Mitchell-Innes | Collector | Stamp Department | — | — |
| 1894 | N. G. Mitchell-Innes | Treasurer | Treasurer's Department | — | — |
| 1896 | N. G. Mitchell-Innes | Treasurer | Treasurer's Department | — | — |
| 1897 | N. G. Mitchell-Innes | Treasurer | Treasurer's Department | — | — |

### Deterministic checks: `mitchell-innes_norman-g_e1880` vs `Mitchell-Innes, N. G___Hong Kong___1886`

- [PASS] surname_gate: bio 'MITCHELL-INNES' vs stint 'Mitchell-Innes, N. G' (exact)
- [PASS] initials: bio ['N', 'G'] ~ stint ['N', 'G']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1897
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

