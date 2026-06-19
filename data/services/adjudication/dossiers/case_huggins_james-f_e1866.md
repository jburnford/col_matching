<!-- {"case_id": "case_huggins_james-f_e1866", "bio_ids": ["huggins_james-f_e1866"], "stint_ids": ["Huggins, J. F___St Lucia___1894"]} -->
# Dossier case_huggins_james-f_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `huggins_james-f_e1866`

- Printed name: **HUGGINS, JAMES F.**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L35568.v` — printed in editions [1900]:**

> HUGGINS, JAMES F.—CLK., P.O., ST. VINCENT, JUNE, 1886; CLK., TREAS., AND AUDIT OFFICE, 1888; 4TH CLK., TREAS., ST. LUCIA, 1890; REV. OFFR., NOV., 1890; AG. 2ND CLK., TREAS., 1891; AG. COL. POSTMSTR., NOV., 1891, TO FEB., 1892; CLK., 2ND DIST. CT. AND SUB-COLL. OF TAXES, POSTMSTR., AND WARDEN, SOUFIERIE, 1892, AND ON OTHER OCCASIONS DURING 1894-5-7; AG. COL. POSTMSTR., AUG. TO OCT., 1897.

**Version `col1894-L32209.v` — printed in editions [1894, 1896, 1897, 1898, 1899]:**

> HUGGINS, JAMES F.—Ck., P.O., St. Vincent, June, 1866; clk., treasy., and audit office, 1888; 4th clk., treasy., St. Lucia, 1890; rev. offr., Nov., 1890; ag. 2nd clk., treasy., 1891; ag. col. postmr., Nov., 1891, to Feb., 1892; ag. clk., 2nd dist. ct. and sub-collr. of taxco, postmr., and warden, Soufriere, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Ck., P.O. | St. Vincent | [1894, 1896, 1897, 1898, 1899] |
| 1 | 1886–1886 | CLK., P.O. | St. Vincent | [1900] |
| 2 | 1888–1888 | CLK., TREAS., AND AUDIT OFFICE | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 3 | 1890–1890 | 4TH CLK., TREAS. | St. Lucia | [1894, 1896, 1897, 1898, 1899, 1900] |
| 4 | 1890–1890 | REV. OFFR. | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 5 | 1891–1891 | AG. 2ND CLK., TREAS. | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 6 | 1891–1892 | AG. COL. POSTMSTR. | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 7 | 1892–1897 | CLK., 2ND DIST. CT. AND SUB-COLL. OF TAXES, POSTMSTR., AND WARDEN | Soufriere | [1894, 1896, 1897, 1898, 1899, 1900] |
| 8 | 1897–1897 | AG. COL. POSTMSTR. | — | [1900] |

## Candidate stint `Huggins, J. F___St Lucia___1894`

- Staff-list name: **Huggins, J. F** | colony: **St Lucia** | listed 1894–1899 | editions [1894, 1896, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. F. Huggins | Landing Waiters and Revenue Officers | Treasury, Customs, and Inland Revenue Department | — | — |
| 1896 | J. F. Huggins | Landing Waiters and Revenue Officers | Treasury, Customs, and Inland Revenue Department | — | — |
| 1898 | J. F. Huggins | Landing Writers and Revenue Officers | Treasury, Customs, and Inland Revenue Department | — | — |
| 1899 | J. F. Huggins | Landing Waiters and Revenue Officers | Treasury, Customs, and Inland Revenue Department | — | — |

### Deterministic checks: `huggins_james-f_e1866` vs `Huggins, J. F___St Lucia___1894`

- [PASS] surname_gate: bio 'HUGGINS' vs stint 'Huggins, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Lucia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1899
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

