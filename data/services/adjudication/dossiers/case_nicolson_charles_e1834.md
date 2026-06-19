<!-- {"case_id": "case_nicolson_charles_e1834", "bio_ids": ["nicolson_charles_e1834"], "stint_ids": ["Nicolson, C. H___Victoria___1890"]} -->
# Dossier case_nicolson_charles_e1834

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['nicolson_charles_e1834'] carry a single initial only — the namesake trap applies.

## Biography `nicolson_charles_e1834`

- Printed name: **NICOLSON, CHARLES**
- Birth year: not printed
- Honours: 1st BART (1859), D.C.L., KNT. BACH. (1852)
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L36462.v` — printed in editions [1900]:**

> NICOLSON, SIR CHARLES, 1st BART (creat. 1859), KNT. BACH. (1852), D.C.L.—Emigrated to Australia in 1834, and practised there as a physician; was elected a mem. of the 1st legis. coun. of N. S. Wales in 1843, and was three times chosen for the office of speaker (1845 to 1856); is provost of the Univ. of Sydney.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1834 | physician | Australia | [1900] |
| 1 | 1843 | mem. of the 1st legis. coun. | New South Wales | [1900] |
| 2 | 1845–1856 | speaker | — | [1900] |

## Candidate stint `Nicolson, C. H___Victoria___1890`

- Staff-list name: **Nicolson, C. H** | colony: **Victoria** | listed 1890–1898 | editions [1890, 1894, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | C. H. Nicolson | Police Magistrate | Police Magistrates, Coroners, and Wardens of the Goldfields of Victoria | — | — |
| 1894 | C. H. Nicolson | Police Magistrate, Coroner, or Warden of the Goldfields of Victoria | Police Magistrates, Coroners, and Wardens of the Goldfields of Victoria | — | — |
| 1897 | C. H. Nicolson | Police Magistrate | Police Magistrates, Coroners, and Wardens of the Goldfields of Victoria | — | — |
| 1898 | C. H. Nicolson | Police Magistrate, Coroner, or Warden | Police Magistrates, Coroners, and Wardens of the Goldfields of Victoria | — | — |

### Deterministic checks: `nicolson_charles_e1834` vs `Nicolson, C. H___Victoria___1890`

- [PASS] surname_gate: bio 'NICOLSON' vs stint 'Nicolson, C. H' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1898
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

