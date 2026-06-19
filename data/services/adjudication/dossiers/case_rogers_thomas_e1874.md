<!-- {"case_id": "case_rogers_thomas_e1874", "bio_ids": ["rogers_thomas_e1874"], "stint_ids": ["Rogers, Thomas___Bermuda___1888"]} -->
# Dossier case_rogers_thomas_e1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 27 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rogers_thomas_e1874'] carry a single initial only — the namesake trap applies.

## Biography `rogers_thomas_e1874`

- Printed name: **ROGERS, THOMAS**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1905-L45589.v` — printed in editions [1905, 1907, 1908, 1909]:**

> ROGERS, THOMAS.—Employed by Cape gov't., 1874 to 1889; by Main Reef G.M.C., Transvaal, 1889-90; in naval dockyard, Simonstown, 1890-91; re-appd. by Cape gov't., Feb., 1891, to Mar., 1897; instr. of drills and diamond setter, late O.F.S., Mar., 1897, to Oct., 1899; ditto, Imperial military gov't., 1st Oct., 1900; ditto, civil gov't., O.R.C., 1st July, 1902.

**Version `col1906-L47718.v` — printed in editions [1906]:**

> ROGERS, THOMAS.—EMPLOYED BY CAPE GOVT., 1874 TO 1889; BY MAIN REEF (G.M.C.), TRANSVAAL, 1889-90; IN NAVAL DOCKYARD, SIMONS TOWN, 1890-91; RE-APPTD. BY CAPE GOVT., FEB., 1891, TO MAR., 1897; INSPR. OF DRILLS AND DIAMOND SETTER, LATE O.F.S., MAR., 1897, TO OCT., 1899; DITTO, IMPERIAL MILITARY GOVT., 1ST OCT., 1900; DITTO, CIVIL GOVT., O.R.C., 1ST JULY, 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874–1889 | Employed | Cape Colony | [1905, 1906, 1907, 1908, 1909] |
| 1 | 1889–1890 | — | Transvaal | [1905, 1906, 1907, 1908, 1909] |
| 2 | 1890–1891 | — | Simonstown | [1905, 1907, 1908, 1909] |
| 3 | 1890–1891 | — | — | [1906] |
| 4 | 1891–1897 | re-appd. | Cape Colony | [1905, 1906, 1907, 1908, 1909] |
| 5 | 1897–1899 | instr. of drills and diamond setter | Orange Free State | [1905, 1906, 1907, 1908, 1909] |
| 6 | 1900 | ditto | — | [1905, 1907, 1908, 1909] |
| 7 | 1900 | INSPR. OF DRILLS AND DIAMOND SETTER | — | [1906] |
| 8 | 1902 | ditto | Orange River Colony | [1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Rogers, Thomas___Bermuda___1888`

- Staff-list name: **Rogers, Thomas** | colony: **Bermuda** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Thomas Rogers | Wesleyan Ministers | Ecclesiastical Establishment | — | — |
| 1889 | Thomas Rogers | Wesleyan Minister | Ecclesiastical Establishment | — | — |

### Deterministic checks: `rogers_thomas_e1874` vs `Rogers, Thomas___Bermuda___1888`

- [PASS] surname_gate: bio 'ROGERS' vs stint 'Rogers, Thomas' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

