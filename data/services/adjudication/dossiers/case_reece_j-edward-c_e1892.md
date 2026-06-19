<!-- {"case_id": "case_reece_j-edward-c_e1892", "bio_ids": ["reece_j-edward-c_e1892"], "stint_ids": ["Reece, J. E___Barbados___1888"]} -->
# Dossier case_reece_j-edward-c_e1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reece_j-edward-c_e1892`

- Printed name: **REECE, J. EDWARD C**
- Birth year: not printed
- Appears in editions: [1907]

### Verbatim printed entry text (OCR)

**Version `col1907-L46459.v` — printed in editions [1907]:**

> REECE, J. EDWARD C.—Ed. Merchant Venturers Coll., Bristol; art. pupil to Messrs. Foster & Co., Bristol, 1892; asst. to borough engnr., Islington, 1897; ch. asst. borough engnr., Margate, 1900; prin. land survr., P.W.D., Hong Kong, 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | art. pupil to Messrs. Foster & Co., Bristol | — | [1907] |
| 1 | 1897 | asst. to borough engnr., Islington | — | [1907] |
| 2 | 1900 | ch. asst. borough engnr | — | [1907] |
| 3 | 1902 | prin. land survr., P.W.D. | Hong Kong | [1907] |

## Candidate stint `Reece, J. E___Barbados___1888`

- Staff-list name: **Reece, J. E** | colony: **Barbados** | listed 1888–1912 | editions [1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1889 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1890 | J. E. Reece | Inspector of Schools | Educational | — | — |
| 1894 | J. E. Reece | Inspector of Schools | Educational | — | — |
| 1896 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1898 | J. E. Reece | Inspector of Schools | Educational | — | — |
| 1899 | J. E. Reece | Inspector of Schools | Educational | — | — |
| 1900 | J. E. Reece | Inspector of Schools | Educational | — | — |
| 1905 | J. E. Reece | Inspector of Schools | Educational | — | — |
| 1906 | J. E. Reece | Inspector of Schools | Educational | — | — |
| 1907 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1908 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1909 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1910 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1911 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |
| 1912 | Rev. J. E. Reece | Inspector of Schools | Educational | — | — |

### Deterministic checks: `reece_j-edward-c_e1892` vs `Reece, J. E___Barbados___1888`

- [PASS] surname_gate: bio 'REECE' vs stint 'Reece, J. E' (exact)
- [PASS] initials: bio ['J', 'E', 'C'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1912
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

