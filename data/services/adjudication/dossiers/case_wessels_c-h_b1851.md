<!-- {"case_id": "case_wessels_c-h_b1851", "bio_ids": ["wessels_c-h_b1851"], "stint_ids": ["Wessels, Cornelis Hermanus___Orange River Colony___1908"]} -->
# Dossier case_wessels_c-h_b1851

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wessels_c-h_b1851`

- Printed name: **WESSELS, C. H**
- Birth year: 1851 (attested in editions [1917, 1918, 1919, 1920, 1921, 1922, 1924])
- Honours: Kt. Bach (1920)
- Appears in editions: [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1917-L54032.v` — printed in editions [1917, 1918, 1919, 1920, 1921, 1922, 1924]:**

> WESSELS, Hon. Sir C. H., Kt. Bach. (1920).—B. 1851; ed. privately; was a J.P., O.F.S., for many years; mem. of the Volksraad, O.F.S., 1885-1899; member of legis. assem., and comsnr. of pub. wks., lands and mines, O.R.C., 1907; is now admstr. of the O.F.S. Prov., Union of S. Africa.

**Version `col1923-L58981.v` — printed in editions [1923]:**

> WESSELS, HON. SIR C. H., KT. BACH. (1920).—B. 1851; ed. privately; was a J.P., O.F.S., for many years; mem. of the Volksraad, O.F.S., 1886-1899; member of legis. assem., and COMMR. OF PUB. WKS., LANDS AND MINES, O.R.C., 1907; IS NOW ADMSTR. OF THE O.F.S. PROV., UNION OF S. AFRICA.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885–1899 | mem. of the Volksraad | Orange Free State | [1917, 1918, 1919, 1920, 1921, 1922, 1924] |
| 1 | 1886–1899 | mem. of the Volksraad | Orange Free State | [1923] |
| 2 | 1907 | member of legis. assem., and comsnr. of pub. wks., lands and mines, O.R.C | Orange Free State *(inherited from previous clause)* | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Wessels, Cornelis Hermanus___Orange River Colony___1908`

- Staff-list name: **Wessels, Cornelis Hermanus** | colony: **Orange River Colony** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | C. H. Wessels | Commissioner of Public Works, Lands, and Mines | Executive Council | — | — |
| 1908 | Hon. C. H. Wessels | Commissioner | Public Works Department | — | — |
| 1908 | Cornelius Hermanus Wessels | Member | Electoral Division | — | — |
| 1909 | Hon. C. H. Wessels | Commissioner | Public Works Department | — | — |
| 1909 | C. H. Wessels | Commissioner of Public Works, Lands and Mines | Executive Council | — | — |
| 1909 | Cornelis Hermanus Wessels | Member | Electoral Division | — | — |

### Deterministic checks: `wessels_c-h_b1851` vs `Wessels, Cornelis Hermanus___Orange River Colony___1908`

- [PASS] surname_gate: bio 'WESSELS' vs stint 'Wessels, Cornelis Hermanus' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1908, birth 1851 (age 57)
- [PASS] colony: 3 placed event(s) resolve to 'Orange River Colony'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1908-1909
- [PASS] position_sim: best 100 vs bar 60: 'member of legis. assem., and comsnr. of pub. wks., lands and mines, O.R.C' ~ 'Member'
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

