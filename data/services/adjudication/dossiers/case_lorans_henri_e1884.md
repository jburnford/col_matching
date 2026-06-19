<!-- {"case_id": "case_lorans_henri_e1884", "bio_ids": ["lorans_henri_e1884"], "stint_ids": ["Lorans, H___Mauritius___1888", "Lorans, H___Mauritius___1897"]} -->
# Dossier case_lorans_henri_e1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lorans_henri_e1884'] carry a single initial only — the namesake trap applies.

## Biography `lorans_henri_e1884`

- Printed name: **LORANS, HENRI**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1905-L44539.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910]:**

> LORANS, HENRI, M.B.C.M., and D.P.H., Edin.—Police and prison surg., Mauritius, 1884; poor law med. offr., Port Louis, 10th Jan., 1884; med. inspr., 15th Nov., 1895; ag. diretr., med. and health dept., 1900 and 1902; nom. mem. of coun. of govt.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884–1884 | Police and prison surg. | Mauritius | [1905, 1906, 1907, 1908, 1909, 1910] |
| 1 | 1884–1884 | poor law med. offr. | Port Louis | [1905, 1906, 1907, 1908, 1909, 1910] |
| 2 | 1895–1895 | med. inspr. | — | [1905, 1906, 1907, 1908, 1909, 1910] |
| 3 | 1900–1902 | ag. diretr., med. and health dept. | — | [1905, 1906, 1907, 1908, 1909, 1910] |

## Candidate stint `Lorans, H___Mauritius___1888`

- Staff-list name: **Lorans, H** | colony: **Mauritius** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | H. Lorans | Prison and Police Surgeon | Civil Medical Department | — | — |
| 1889 | Dr. H. Lorans | Prison and Police Surgeon | Civil Medical Department | — | — |
| 1890 | Dr. H. Lorans | Prison and Police Surgeon | Civil Medical Department | — | — |

### Deterministic checks: `lorans_henri_e1884` vs `Lorans, H___Mauritius___1888`

- [PASS] surname_gate: bio 'LORANS' vs stint 'Lorans, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Lorans, H___Mauritius___1897`

- Staff-list name: **Lorans, H** | colony: **Mauritius** | listed 1897–1910 | editions [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | Dr. H. Lorans | Medical Inspector | Medical and Health Department | — | — |
| 1898 | Dr. H. Lorans | Medical Inspector | Medical and Health Department | — | — |
| 1899 | H. Lorans | Medical Inspector | Medical and Health Department | — | — |
| 1900 | Dr. H. Lorans | Medical Inspector | Medical and Health Department | — | — |
| 1905 | H. Lorans | Director | MEDICAL AND HEALTH DEPARTMENT | — | — |
| 1906 | Dr. H. Lorans | Director | Medical and Health Department | — | — |
| 1907 | Dr. H. Lorans | Director | Medical and Health Department | — | — |
| 1908 | Dr. H. Lorans | Director | Medical and Health Department | — | — |
| 1909 | Dr. H. Lorans | Director | Medical and Health Department | — | — |
| 1910 | H. Lorans | Director | Medical and Health Department | — | — |

### Deterministic checks: `lorans_henri_e1884` vs `Lorans, H___Mauritius___1897`

- [PASS] surname_gate: bio 'LORANS' vs stint 'Lorans, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1910
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

