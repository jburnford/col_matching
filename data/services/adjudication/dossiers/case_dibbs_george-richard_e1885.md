<!-- {"case_id": "case_dibbs_george-richard_e1885", "bio_ids": ["dibbs_george-richard_e1885", "dibbs_grobeo-richard_e1883"], "stint_ids": ["Dibbs, G. R___New South Wales___1899"]} -->
# Dossier case_dibbs_george-richard_e1885

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Dibbs, G. R___New South Wales___1899'] have more than one claimant biography in this case.

## Biography `dibbs_george-richard_e1885`

- Printed name: **DIBBS, GEORGE RICHARD**
- Birth year: not printed
- Honours: K.C.M.G. (1892)
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1894-L31226.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1900]:**

> DIBBS, THE HON. SIR GEORGE RICHARD, K.C.M.G., (1892).—Colonial treas., New South Wales, Jan., 1888, to Oct., 1885; premier and colonial secy., Oct., 1885; treas. and premier, Oct. to Dec., 1886; colonial secy. and premier, Feb., 1886, to Feb., 1887, and Jan. and Feb., 1889, again premier and colonial secy. 1891-4; one of the representatives of N.S.W. at federation convention, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885–1885 | premier and colonial secy. | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1886–1886 | treas. and premier | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 2 | 1888–1885 | Colonial treas. | New South Wales | [1894, 1896, 1897, 1898, 1899, 1900] |
| 3 | 1891–1891 | one of the representatives at federation convention | New South Wales | [1894, 1896, 1897, 1898, 1899, 1900] |

## Biography `dibbs_grobeo-richard_e1883`

- Printed name: **DIBBS, GROBEO RICHARD**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33078.v` — printed in editions [1888, 1889, 1890]:**

> DIBBS, GROBEO RICHARD.—Colonial treasurer, New South Wales, Jan., 1883, to Oct., 1885; premier and colonial secretary, Oct., 1885; treasurer and premier, Oct. to Dec., 1885; colonial secretary, Feb., 1886, to Feb., 1887, and Jan. and Feb., 1889.

**Version `col1886-L33061.v` — printed in editions [1886]:**

> DIBBS, Hon. G. R.—Colonial treasurer and secretary for finance and trade, New South Wales, Jan., 1883; premier and treasurer, Oct., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883–1885 | Colonial treasurer | New South Wales | [1886, 1888, 1889, 1890] |
| 1 | 1885–1885 | premier and colonial secretary | — | [1888, 1889, 1890] |
| 2 | 1885–1885 | treasurer and premier | New South Wales *(inherited from previous clause)* | [1886, 1888, 1889, 1890] |
| 3 | 1886–1889 | colonial secretary | — | [1888, 1889, 1890] |

## Candidate stint `Dibbs, G. R___New South Wales___1899`

- Staff-list name: **Dibbs, G. R** | colony: **New South Wales** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | G. R. Dibbs | Commanding | National Guard | K.C.M.G. | Captain |
| 1900 | G. R. Dibbs | Commanding | National Guard | K.C.M.G. | Capt. |

### Deterministic checks: `dibbs_george-richard_e1885` vs `Dibbs, G. R___New South Wales___1899`

- [PASS] surname_gate: bio 'DIBBS' vs stint 'Dibbs, G. R' (exact)
- [PASS] initials: bio ['G', 'R'] ~ stint ['G', 'R']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.M.G.
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `dibbs_grobeo-richard_e1883` vs `Dibbs, G. R___New South Wales___1899`

- [PASS] surname_gate: bio 'DIBBS' vs stint 'Dibbs, G. R' (exact)
- [PASS] initials: bio ['G', 'R'] ~ stint ['G', 'R']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
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

