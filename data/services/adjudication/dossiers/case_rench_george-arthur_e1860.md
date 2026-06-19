<!-- {"case_id": "case_rench_george-arthur_e1860", "bio_ids": ["rench_george-arthur_e1860"], "stint_ids": ["French, G. A___Queensland___1886"]} -->
# Dossier case_rench_george-arthur_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `rench_george-arthur_e1860` ↔ `French, G. A___Queensland___1886` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `French, G. A___Queensland___1886` is also gate-compatible with biography(ies) outside this case: ['french_george-arthur_e1860'] (already linked elsewhere or filtered).

## Biography `rench_george-arthur_e1860`

- Printed name: **RENCH, GEORGE ARTHUR**
- Birth year: not printed
- Honours: C.G. (1877)
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L32060.v` — printed in editions [1897]:**

> RENCH, MAJ.-GEN. GEORGE ARTHUR, R.A., C.G. (1877).—Educated at Sandhurst and Woolwich; joined R.A. as licit., 1860; proceeded to North America in Dec., 1861, with expeditionary force sent out in consequence of the "Trent Affair"; served at R.A., Kingston, from 1862 to 1866; qualified as 1st-class gunnery instructor in 1867; 1st-class inspector of warlike stores in 1868; appointed W.O. at Quebec in 1869 on the withdrawal of Imperial troops; inspector of artillery, with rank of lieut.-col., in 1870; organized the permanent batteries of artillery in 1871; commissioner for West Mounted Police, and stipendiary magistrate for the territories, in Dec., 1873; raised, organized, and equipped the force; commanded expedition sent from the Red River to the base of the Rocky Mountains in 1874; inspector of store stores, Devonport, 1878 to 1883; commandant Queensland forces, with rank of col., 1883; commandant N.S.W. Wales forces, 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | licit. | — | [1897] |
| 1 | 1861 | — | North America | [1897] |
| 2 | 1862–1866 | served at R.A. | Kingston | [1897] |
| 3 | 1867 | 1st-class gunnery instructor | — | [1897] |
| 4 | 1868 | 1st-class inspector of warlike stores | — | [1897] |
| 5 | 1869 | W.O. | Quebec | [1897] |
| 6 | 1870 | inspector of artillery | — | [1897] |
| 7 | 1871 | — | — | [1897] |
| 8 | 1873 | commissioner for West Mounted Police, and stipendiary magistrate for the territories | — | [1897] |
| 9 | 1874 | — | — | [1897] |
| 10 | 1878–1883 | inspector of store stores | Devonport | [1897] |
| 11 | 1883 | commandant Queensland forces | Queensland | [1897] |
| 12 | 1895 | commandant N.S.W. Wales forces | New South Wales | [1897] |

## Candidate stint `French, G. A___Queensland___1886`

- Staff-list name: **French, G. A** | colony: **Queensland** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | G. A. French | Commandant Defence Force | Colonial Secretary's Department | C.M.G. | Colonel |
| 1888 | G. A. French | Commandant, Defence Force | Colonial Secretary's Department | C.M.G. | Colonel |
| 1889 | G. A. French | Commandant, Defence Force | Colonial Secretary's Department | C.M.G. | Colonel |
| 1890 | G. A. French | Commandant, Defence Force | Colonial Secretary's Department | — | Colonel |

### Deterministic checks: `rench_george-arthur_e1860` vs `French, G. A___Queensland___1886`

- [PASS] surname_gate: bio 'RENCH' vs stint 'French, G. A' (fuzzy:1)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1890
- [PASS] position_sim: best 62 vs bar 60: 'commandant Queensland forces' ~ 'Commandant Defence Force'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

