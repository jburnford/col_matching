<!-- {"case_id": "case_figg_frederick-george_e1872", "bio_ids": ["figg_frederick-george_e1872"], "stint_ids": ["Figg, F. G___Hong Kong___1894"]} -->
# Dossier case_figg_frederick-george_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `figg_frederick-george_e1872`

- Printed name: **FIGG, FREDERICK GEORGE**
- Birth year: not printed
- Appears in editions: [1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1909-L45207.v` — printed in editions [1909, 1910, 1911, 1912]:**

> FIGG, FREDERICK GEORGE.—Asst., Kew Observatory, 1872; magnetic observer, 1876; 1st asst., Hong Kong Observatory, 1883; ag. director, 1897, 1900, 1902 and 1903; director, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Asst. | — | [1909, 1910, 1911, 1912] |
| 1 | 1876 | magnetic observer | — | [1909, 1910, 1911, 1912] |
| 2 | 1883 | 1st asst. | Hong Kong | [1909, 1910, 1911, 1912] |
| 3 | 1897–1903 | ag. director | — | [1909, 1910, 1911, 1912] |
| 4 | 1907 | director | — | [1909, 1910, 1911, 1912] |

## Candidate stint `Figg, F. G___Hong Kong___1894`

- Staff-list name: **Figg, F. G** | colony: **Hong Kong** | listed 1894–1912 | editions [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | F. G. Figg | First Assistant | Hong Kong Observatory | — | — |
| 1896 | F. G. Figg | First Assistant | Hong Kong Observatory | — | — |
| 1897 | F. G. Figg | First Assistant | Hong Kong Observatory | — | — |
| 1898 | F. G. Figg | First Assistant | Hong Kong Observatory | — | — |
| 1899 | F. G. Figg | First Assistant | Hong Kong Observatory | — | — |
| 1900 | F. G. Figg | First Assistant | Hong Kong Observatory | — | — |
| 1905 | F. G. Figg | First Assistant | Observatory Department | — | — |
| 1906 | F. G. Figg | First Assistant | Observatory | — | — |
| 1907 | F. G. Figg | First Assistant | Observatory | — | — |
| 1908 | F. G. Figg | Director of the Observatory | Observatory | — | — |
| 1909 | F. G. Figg | Director of the Observatory | Observatory | — | — |
| 1910 | F. G. Figg | Director of the Observatory | Observatory | — | — |
| 1911 | F. G. Figg | Director of the Observatory | Observatory | — | — |
| 1912 | F. G. Figg | Director of the Observatory | Observatory | — | — |

### Deterministic checks: `figg_frederick-george_e1872` vs `Figg, F. G___Hong Kong___1894`

- [PASS] surname_gate: bio 'FIGG' vs stint 'Figg, F. G' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1912
- [FAIL] position_sim: best 43 vs bar 60: '1st asst.' ~ 'First Assistant'
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

