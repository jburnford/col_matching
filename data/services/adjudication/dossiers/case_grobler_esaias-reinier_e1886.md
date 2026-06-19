<!-- {"case_id": "case_grobler_esaias-reinier_e1886", "bio_ids": ["grobler_esaias-reinier_e1886"], "stint_ids": ["Grobler, E. R___South Africa___1914", "Grobler, Esaias Renier___Orange River Colony___1908"]} -->
# Dossier case_grobler_esaias-reinier_e1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `grobler_esaias-reinier_e1886`

- Printed name: **GROBLER, ESAIAS REINIER**
- Birth year: not printed
- Appears in editions: [1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1928-L66730.v` — printed in editions [1928, 1929, 1930, 1931]:**

> GROBLER, HON. ESAIAS REINIER.—Ed. in O.F.S.; mem., O.F.S. Volksraad, 1886-1899; el. vice-chmn. three times and acted as chmn. last two sessions; mem., coun. of dels. between O.F.S. and Transvaal from inception of coun.; ch. commdt., S. divn. Federal Forces, Anglo-Boer War, 1899-1901; mem., inter col. irrigan. comm., 1903; pres., leg. coun., O.R.C., 1907-10; shmn., comm., on native affrs., 1909; senator, Union of S. Africa, 1910-24; mem., influenza epidemic comm., 1919; admstr., O.F.S., 1924-29.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886–1899 | mem., O.F.S. Volksraad | Orange Free State | [1928, 1929, 1930, 1931] |
| 1 | 1899–1901 | ch. commdt., S. divn. Federal Forces, Anglo-Boer War | Orange Free State *(inherited from previous clause)* | [1928, 1929, 1930, 1931] |
| 2 | 1903 | mem., inter col. irrigan. comm | Orange Free State *(inherited from previous clause)* | [1928, 1929, 1930, 1931] |
| 3 | 1907–1910 | pres., leg. coun., O.R.C | Orange Free State *(inherited from previous clause)* | [1928, 1929, 1930, 1931] |
| 4 | 1909 | shmn., comm., on native affrs | Orange Free State *(inherited from previous clause)* | [1928, 1929, 1930, 1931] |
| 5 | 1910–1924 | senator, Union of S. Africa | Orange Free State *(inherited from previous clause)* | [1928, 1929, 1930, 1931] |
| 6 | 1919 | mem., influenza epidemic comm | Orange Free State *(inherited from previous clause)* | [1928, 1929, 1930, 1931] |
| 7 | 1924–1929 | admstr. | Orange Free State | [1928, 1929, 1930, 1931] |

## Candidate stint `Grobler, E. R___South Africa___1914`

- Staff-list name: **Grobler, E. R** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | E. R. Grobler | Senator | Senate | — | — |
| 1918 | E. R. Grobler | Senator | Senate | — | — |

### Deterministic checks: `grobler_esaias-reinier_e1886` vs `Grobler, E. R___South Africa___1914`

- [PASS] surname_gate: bio 'GROBLER' vs stint 'Grobler, E. R' (exact)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Grobler, Esaias Renier___Orange River Colony___1908`

- Staff-list name: **Grobler, Esaias Renier** | colony: **Orange River Colony** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | E. R. Grobler | President | Legislative Council | — | — |
| 1908 | Esaias Renier Grobler | Member | Legislative Council | — | — |
| 1909 | Esaias Renier Grobler | — | Legislative Council | — | — |
| 1909 | E. R. Grobler | President | Legislative Council | — | — |

### Deterministic checks: `grobler_esaias-reinier_e1886` vs `Grobler, Esaias Renier___Orange River Colony___1908`

- [PASS] surname_gate: bio 'GROBLER' vs stint 'Grobler, Esaias Renier' (exact)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 8 placed event(s) resolve to 'Orange River Colony'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1908-1909
- [FAIL] position_sim: best 31 vs bar 60: 'pres., leg. coun., O.R.C' ~ 'President'
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

