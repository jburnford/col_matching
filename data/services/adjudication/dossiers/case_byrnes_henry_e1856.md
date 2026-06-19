<!-- {"case_id": "case_byrnes_henry_e1856", "bio_ids": ["byrnes_henry_e1856"], "stint_ids": ["Byrnes, H___Mauritius___1877"]} -->
# Dossier case_byrnes_henry_e1856

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['byrnes_henry_e1856'] carry a single initial only — the namesake trap applies.

## Biography `byrnes_henry_e1856`

- Printed name: **BYRNES, HENRY**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L32974.v` — printed in editions [1890]:**

> BYRNES, HENRY.—Assistant clerk to the magistrate, Pamplemousses, Mauritius, July, 1856; district clerk, Riviere du Rempart, Feb., 1859; joint clerk, April, 1860; district clerk, Grand Port, 1869; census superintendent, Aug., 1880.

**Version `col1883-L26699.v` — printed in editions [1883, 1886, 1888]:**

> BYRNES, HENRY.—Assistant clerk to the magistrate, Pamphoumousses, Mauritius, July, 1856; joint clerk, April, 1860; district clerk, Grand Port, 1869.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856 | Assistant clerk to the magistrate, Pamplemousses | Mauritius | [1883, 1886, 1888, 1890] |
| 1 | 1859 | district clerk, Riviere du Rempart | Mauritius *(inherited from previous clause)* | [1890] |
| 2 | 1860 | joint clerk | Mauritius *(inherited from previous clause)* | [1883, 1886, 1888, 1890] |
| 3 | 1869 | district clerk, Grand Port | Mauritius *(inherited from previous clause)* | [1883, 1886, 1888, 1890] |
| 4 | 1880 | census superintendent | Mauritius *(inherited from previous clause)* | [1890] |

## Candidate stint `Byrnes, H___Mauritius___1877`

- Staff-list name: **Byrnes, H** | colony: **Mauritius** | listed 1877–1890 | editions [1877, 1879, 1880, 1883, 1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. Byrnes | District Clerk | District Magistracy | — | — |
| 1879 | H. Byrnes | District Clerk | District Magistracy | — | — |
| 1880 | H. Byrnes | District Clerk | District Magistracy | — | — |
| 1883 | H. Byrnes | District Clerk | District Magistracy | — | — |
| 1888 | H. Byrnes | District Clerk | District Magistracy | — | — |
| 1890 | H. Byrnes | District Clerk | District Magistracy | — | — |

### Deterministic checks: `byrnes_henry_e1856` vs `Byrnes, H___Mauritius___1877`

- [PASS] surname_gate: bio 'BYRNES' vs stint 'Byrnes, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1890
- [PASS] position_sim: best 100 vs bar 60: 'district clerk, Grand Port' ~ 'District Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

