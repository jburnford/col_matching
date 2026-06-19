<!-- {"case_id": "case_marchand_felix-gabriel_b1832", "bio_ids": ["marchand_felix-gabriel_b1832"], "stint_ids": ["Marchand, F. G___Canada___1898"]} -->
# Dossier case_marchand_felix-gabriel_b1832

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `marchand_felix-gabriel_b1832`

- Printed name: **MARCHAND, FELIX GABRIEL**
- Birth year: 1832 (attested in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900])
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1889-L34512.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]:**

> MARCHAND, THE HON. FELIX GABRIEL.—Speaker, Leg. Ass. of Quebec; born 1832; elected member of the legislative assembly for the county of St. John's in 1867, re-elected in 1871, 1875, 1878, 1881, and in 1886; entered the cabinet as provincial secretary in 1878, and minister of crown lands in 1879; chosen speaker of the assembly in 1885; in Jan., 1882, organized the 21st bat. of infantry, and was apptd. lieut.-col., Canadian militia, 1866; during the Fenian invasions of 1866 and 1870, took active service with his batn., and commanded a brigade on the frontier; is an author of works in prose and verse; has received the decoration of officer of public instruction of France, and is F.R.S. of Canada, and of many other literary institutions.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | lieut.-col. | Canada | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1866–1870 | commanded a brigade | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 2 | 1867 | member of the legislative assembly | St. John's | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 3 | 1871–1886 | member of the legislative assembly | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 4 | 1878 | provincial secretary | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 5 | 1879 | minister of crown lands | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 6 | 1882 | — | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 7 | 1885 | speaker of the assembly | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Marchand, F. G___Canada___1898`

- Staff-list name: **Marchand, F. G** | colony: **Canada** | listed 1898–1900 | editions [1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Hon. F. G. Marchand | Prime Minister and Provincial Treasurer | Executive Council | — | — |
| 1899 | Hon. F. G. Marchand | Prime Minister and Provincial Treasurer | Executive Council | — | — |
| 1900 | Hon. F. G. Marchand | Prime Minister and Provincial Treasurer | Executive Council | — | — |

### Deterministic checks: `marchand_felix-gabriel_b1832` vs `Marchand, F. G___Canada___1898`

- [PASS] surname_gate: bio 'MARCHAND' vs stint 'Marchand, F. G' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1898, birth 1832 (age 66)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
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

