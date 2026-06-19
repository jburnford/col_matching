<!-- {"case_id": "case_tave_x_e1855", "bio_ids": ["tave_x_e1855"], "stint_ids": ["Tave, G. A___Gold Coast___1908"]} -->
# Dossier case_tave_x_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['tave_x_e1855'] carry a single initial only — the namesake trap applies.

## Biography `tave_x_e1855`

- Printed name: **TAVE, (no given names printed)**
- Birth year: not printed
- Honours: K.C.M.G. (1895)
- Appears in editions: [1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L35698.v` — printed in editions [1899]:**

> TAVE, K.C.M.G. (1895).—Ed. in Paris, and called to the bar of Quebec in 1855; elected to parltm. of old Canada for Lotbiniere in 1861, and continued to represent the county till 1867, when he was returned both to the parltm. of the Dominion and to the legislature of Quebec; in 1874 he ret. from parltm. to devote his attention to provincial affairs: in 1878, on the dismissal of the De Boucherville cabinet, he was called on to form a ministry, which he did, holding power for one session by virtue of the vote of the speaker; resig. 1879, after defeat in the house of assen.; later he ret. from the leadership of the party; and in 1886, as a protest against the Itel agitation carried on by the provincial liberal party, ret. from public life; in 1877 was offered the portfolio of agricul. in the Mackenziegovt., with a seat in the senate; controller of inland rev., without a seat in the cabinet, in Sir W. Laurier's govt., June, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855–1855 | called to the bar | Quebec | [1899] |
| 1 | 1861–1867 | represent the county | Canada | [1899] |
| 2 | 1867 | returned both to the parltm. of the Dominion and to the legislature of Quebec | Quebec | [1899] |
| 3 | 1874–1874 | — | — | [1899] |
| 4 | 1877–1877 | portfolio of agricul. | — | [1899] |
| 5 | 1878 | form a ministry | — | [1899] |
| 6 | 1879–1879 | — | — | [1899] |
| 7 | 1886–1886 | — | — | [1899] |
| 8 | 1896 | controller of inland rev. | — | [1899] |

## Candidate stint `Tave, G. A___Gold Coast___1908`

- Staff-list name: **Tave, G. A** | colony: **Gold Coast** | listed 1908–1910 | editions [1908, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | G. A. Tave | Second Class Officers | Customs | — | — |
| 1910 | G. A. Tave | Second Class Officer | Customs | — | — |

### Deterministic checks: `tave_x_e1855` vs `Tave, G. A___Gold Coast___1908`

- [PASS] surname_gate: bio 'TAVE' vs stint 'Tave, G. A' (exact)
- [PASS] initials: bio ['?'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1910
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

