<!-- {"case_id": "case_tissik_johann-friedrich-bernhard_e1907", "bio_ids": ["tissik_johann-friedrich-bernhard_e1907"], "stint_ids": ["Rissik, J. F. B___South Africa___1912"]} -->
# Dossier case_tissik_johann-friedrich-bernhard_e1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tissik_johann-friedrich-bernhard_e1907`

- Printed name: **TISSIK, JOHANN FRIEDRICH BERNHARD**
- Birth year: not printed
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L58959.v` — printed in editions [1925]:**

> TISSIK, HON. JOHANN FRIEDRICH BERNHARD, I.L.A., Transvaal, for the electoral division Pretoria North Cent., 1907; mem. exec. nc. as min. for lands and native affairs, 1907; astr. of the Transvaal, 1911; mem. rlws. harb. board, 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | for the electoral division Pretoria North Cent. | Transvaal | [1925] |
| 1 | 1907 | mem. exec. nc. as min. for lands and native affairs | — | [1925] |
| 2 | 1911 | astr. | Transvaal | [1925] |
| 3 | 1917 | mem. rlws. harb. board | — | [1925] |

## Candidate stint `Rissik, J. F. B___South Africa___1912`

- Staff-list name: **Rissik, J. F. B** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Hon. J. Rissik | Administrator | Provincial Administration | — | — |
| 1914 | J. Rissik | Administrator | Provincial Administration | — | — |
| 1918 | J. F. B. Rissik | — | RAILWAYS AND HARBOURS BOARDS | — | — |

### Deterministic checks: `tissik_johann-friedrich-bernhard_e1907` vs `Rissik, J. F. B___South Africa___1912`

- [PASS] surname_gate: bio 'TISSIK' vs stint 'Rissik, J. F. B' (fuzzy:1)
- [PASS] initials: bio ['J', 'F', 'B'] ~ stint ['J', 'F', 'B']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

