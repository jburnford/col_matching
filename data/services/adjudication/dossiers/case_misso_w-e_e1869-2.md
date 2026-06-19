<!-- {"case_id": "case_misso_w-e_e1869-2", "bio_ids": ["misso_w-e_e1869-2"], "stint_ids": ["Misso, William E___Ceylon___1877", "Misso, William E___Ceylon___1894"]} -->
# Dossier case_misso_w-e_e1869-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `misso_w-e_e1869-2` ↔ `Misso, William E___Ceylon___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Misso, William E___Ceylon___1877` is also gate-compatible with biography(ies) outside this case: ['misso_w-e_e1869'] (already linked elsewhere or filtered).
- NOTE: stint `Misso, William E___Ceylon___1894` is also gate-compatible with biography(ies) outside this case: ['misso_w-e_e1869'] (already linked elsewhere or filtered).

## Biography `misso_w-e_e1869-2`

- Printed name: **MISSO, W. E.**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1894-L33041.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1900]:**

> MISSO, W. E., M.R.C.S.—Asst. col. surg., Ceylon, 1869; dist. med. offr., Badulla, Jan., 1883; sen. med. offr., 1886; asst. col. surg., Galle, 1889. 1889; apptd. gov. Oct., 1889; gov. S. S., Oct., 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Asst. col. surg. | Ceylon | [1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1883 | dist. med. offr. | Badulla | [1894, 1896, 1897, 1898, 1899, 1900] |
| 2 | 1886 | sen. med. offr. | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 3 | 1889 | asst. col. surg. | Galle | [1894, 1896, 1897, 1898, 1899, 1900] |
| 4 | 1889 | gov. | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 5 | 1893 | gov. | Straits Settlements | [1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Misso, William E___Ceylon___1877`

- Staff-list name: **Misso, William E** | colony: **Ceylon** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. E. Misso | Assistant Colonial Surgeons | Medical Department | — | — |
| 1878 | W. E. Misso | Assistant Colonial Surgeons | Medical Department | — | — |
| 1879 | W. E. Misso | Assistant Colonial Surgeons | Medical Department | — | — |
| 1880 | W. E. Misso | Assistant Colonial Surgeons | Medical Department | — | — |
| 1883 | W. E. Misso | Assistant Colonial Surgeon | Medical Department | — | — |
| 1886 | W. E. Misso | Assistant Colonial Surgeon | Medical Department | — | — |
| 1888 | W. E. Misso | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `misso_w-e_e1869-2` vs `Misso, William E___Ceylon___1877`

- [PASS] surname_gate: bio 'MISSO' vs stint 'Misso, William E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1888
- [PASS] position_sim: best 67 vs bar 60: 'Asst. col. surg.' ~ 'Assistant Colonial Surgeon'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Misso, William E___Ceylon___1894`

- Staff-list name: **Misso, William E** | colony: **Ceylon** | listed 1894–1898 | editions [1894, 1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | William E. Misso | Assistant Colonial Surgeon | Medical Department | — | — |
| 1896 | W. E. Misso | Assistant Colonial Surgeon | Medical Department | — | — |
| 1898 | W. E. Misso | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `misso_w-e_e1869-2` vs `Misso, William E___Ceylon___1894`

- [PASS] surname_gate: bio 'MISSO' vs stint 'Misso, William E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1898
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

