<!-- {"case_id": "case_bemore_earlor-somerset-richard-lowry-corry_e1856", "bio_ids": ["bemore_earlor-somerset-richard-lowry-corry_e1856"], "stint_ids": ["Belmore, E___Bermuda___1905"]} -->
# Dossier case_bemore_earlor-somerset-richard-lowry-corry_e1856

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bemore_earlor-somerset-richard-lowry-corry_e1856`

- Printed name: **BEMORE, EARLOR, Somerset Richard Lowry Corry**
- Birth year: not printed
- Honours: G.C.M.G. (1890), K.C.M.G. (1872)
- Appears in editions: [1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L33623.v` — printed in editions [1899]:**

> BEMORE, EARLOR, G.C.M.G.(1890), K.C.M.G. (1872), Somerset Richard Lowry Corry, fourth Earl and Viscount Belmore of the co. Fermanagh, Belmore, Viscount and Baron Belmore, of Castle Coole, co. Fermanagh, in the peerage of Ireland, of which he is a representative peer. Graduated M.A. (hon.) at Cambridge 1856; elected a representative peer for Ireland, Jan., 1857; was Under Sec. of State for Home Dept. in Lord Derby's 3rd adminstr., July, 1866; Priv. Counlr. (Ireland), 1867; gov. of N. S. Wales, Aug., 1867; resig. 1872; served as one of the Lords Justices of Ireland, 1885; again 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856–1856 | — | — | [1899] |
| 1 | 1857–1857 | representative peer | Ireland | [1899] |
| 2 | 1866–1866 | Under Sec. of State for Home Dept. | — | [1899] |
| 3 | 1867–1867 | Priv. Counlr. | Ireland | [1899] |
| 4 | 1867–1867 | gov. | New South Wales | [1899] |
| 5 | 1872–1872 | — | — | [1899] |
| 6 | 1885–1885 | one of the Lords Justices | Ireland | [1899] |
| 7 | 1886–1886 | one of the Lords Justices | Ireland | [1899] |

## Candidate stint `Belmore, E___Bermuda___1905`

- Staff-list name: **Belmore, E** | colony: **Bermuda** | listed 1905–1914 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1906 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1907 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1908 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1909 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1910 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1911 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1912 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1913 | E. Belmore | Inspector of Police | Police and Gaols | — | — |
| 1914 | E. Belmore | Inspector of Police | Police and Gaols | — | — |

### Deterministic checks: `bemore_earlor-somerset-richard-lowry-corry_e1856` vs `Belmore, E___Bermuda___1905`

- [PASS] surname_gate: bio 'BEMORE' vs stint 'Belmore, E' (fuzzy:1)
- [PASS] initials: bio ['E', 'S', 'R', 'L', 'C'] ~ stint ['E']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1914
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

