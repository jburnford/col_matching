<!-- {"case_id": "case_seager_meeting-bloomfield_e1861", "bio_ids": ["seager_meeting-bloomfield_e1861"], "stint_ids": ["Seager, M. B___Cyprus___1888"]} -->
# Dossier case_seager_meeting-bloomfield_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `seager_meeting-bloomfield_e1861`

- Printed name: **SEAGER, MEETING BLOOMFIELD**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1889-L35559.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899]:**

> SEAGER, MEETING BLOOMFIELD.—Entered Wellington Coll.; 2nd lieut., R.M.L.I., 1861; 1st lieut., 1867; called to the bar, Middle Temp., 1874; asst. commr., Nicosia, Cyprus, 1878; ass. commr., Kyrenia, 1879; deputy judicial commr. and first delegate of Evkaf, 1880; capt. R.M.L.I.; presdt. dist. ct., Nicosia, 1883; major, R.M.L.I., 1887; retired from R.M.L.I.; presdt. dist. ct., Larnaca, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | 2nd lieut., R.M.L.I | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 1 | 1867 | 1st lieut | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 2 | 1874 | called to the bar, Middle Temp | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 3 | 1878 | asst. commr., Nicosia | Cyprus | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 4 | 1879 | ass. commr., Kyrenia | Cyprus *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 5 | 1880 | deputy judicial commr. and first delegate of Evkaf | Cyprus *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 6 | 1883 | presdt. dist. ct., Nicosia | Cyprus *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 7 | 1887 | major, R.M.L.I | Cyprus *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 8 | 1896 | presdt. dist. ct., Larnaca | Cyprus *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |

## Candidate stint `Seager, M. B___Cyprus___1888`

- Staff-list name: **Seager, M. B** | colony: **Cyprus** | listed 1888–1898 | editions [1888, 1890, 1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | M. B. Seager | President | Courts of Justice | — | — |
| 1890 | M. B. Seager | President | District Courts | — | — |
| 1894 | M. B Seager | President | District Courts | — | — |
| 1896 | M. B. Seager | President | Courts of Justice | — | — |
| 1897 | M. B. Seager | President | District Court - Larnaca | — | — |
| 1898 | M. B. Seager | President | District Courts - Larnaca | — | — |

### Deterministic checks: `seager_meeting-bloomfield_e1861` vs `Seager, M. B___Cyprus___1888`

- [PASS] surname_gate: bio 'SEAGER' vs stint 'Seager, M. B' (exact)
- [PASS] initials: bio ['M', 'B'] ~ stint ['M', 'B']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1888-1898
- [FAIL] position_sim: best 39 vs bar 60: 'presdt. dist. ct., Nicosia' ~ 'President'
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

