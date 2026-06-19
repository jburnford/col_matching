<!-- {"case_id": "case_tranchell_e-f_e1843", "bio_ids": ["tranchell_e-f_e1843"], "stint_ids": ["Tranchell, E. F___Ceylon___1886"]} -->
# Dossier case_tranchell_e-f_e1843

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tranchell_e-f_e1843`

- Printed name: **TRANCHELL, E. F.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L29781.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> TRANCHELL, Major E. F.—Royal Cadet Military College, Sandhurst entered the army in 1843; served 28 years in the Ceylon rifle regiment, during which time he served with a detachment of his regiment in China, 1859-61; held the appointment of staff officer of the Kandian district, 1859-61; commandant of Jaffna, 1864-66; commandant of Kandy, 1866-68; commanded the troops at Labuan 1868-69; commandant of Trincomalee, 1870-71; was selected by Major-General Lockyer for special service connected with recruiting for the Ceylon rifle regiment, 1858-59, and visited the Straits Settlements, Siam, Brunei, Sarawak, and other parts of Borneo; superintendent of police, Ceylon, March, 1871; acting inspector-general, 12th July, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1843–1843 | entered the army | — | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1858–1859 | special service connected with recruiting | Straits Settlements | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1859–1861 | served with a detachment of his regiment in China | China | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1859–1861 | staff officer of the Kandian district | — | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1864–1866 | commandant of Jaffna | — | [1883, 1886, 1888, 1889, 1890] |
| 5 | 1866–1868 | commandant of Kandy | — | [1883, 1886, 1888, 1889, 1890] |
| 6 | 1868–1869 | commanded the troops | Labuan | [1883, 1886, 1888, 1889, 1890] |
| 7 | 1870–1871 | commandant of Trincomalee | — | [1883, 1886, 1888, 1889, 1890] |
| 8 | 1871 | superintendent of police | Ceylon | [1883, 1886, 1888, 1889, 1890] |
| 9 | 1882 | acting inspector-general | — | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Tranchell, E. F___Ceylon___1886`

- Staff-list name: **Tranchell, E. F** | colony: **Ceylon** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | E. F. Tranchell | Provincial Superintendent | Police | — | Major |
| 1888 | E. F. Tranchell | Provincial Superintendent | Police | — | Major |
| 1889 | E. F. Tranchell | Provincial Superintendent | Police | — | Major |
| 1890 | E. F. Tranchell | Provincial Superintendent | Police | — | — |

### Deterministic checks: `tranchell_e-f_e1843` vs `Tranchell, E. F___Ceylon___1886`

- [PASS] surname_gate: bio 'TRANCHELL' vs stint 'Tranchell, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1890
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

