<!-- {"case_id": "case_rabaut_arthur-edmund_b1885", "bio_ids": ["rabaut_arthur-edmund_b1885"], "stint_ids": ["Rabaud, A___Mauritius___1925"]} -->
# Dossier case_rabaut_arthur-edmund_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rabaut_arthur-edmund_b1885`

- Printed name: **RABAUT, ARTHUR EDMUND**
- Birth year: 1885 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L67567.v` — printed in editions [1931]:**

> RABAUT, ARTHUR EDMUND, B.A.—B.1885; ed. Magd. Coll. Schl. and B.N.C., Oxford; 2nd cls. math. mods., 1906; 4th cls. bot., 1908; dipl. forestry, 1909; asst. com., forests, F.M.S., Nov., 1909; on mil. duty; 2nd lieut. North. Fus. (T.F.), 1915; lieut., 1916; temp. capt. 1916; served in France; intel. corps., 1917 (France, Belgium, Germany); rtnd. to F.M.S., Aug., 1919; ag. dep. com., forests, Selangor, in 1920, 1921 and 1923; dep. com., forests, S.S. and F.M.S., Nov., 1926; ag. per. asst. to com., forests, Dec., 1927 and Aug., 1928; conserv., forests, Jan., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906–1906 | 2nd cls. math. mods. | — | [1931] |
| 1 | 1908–1908 | 4th cls. bot. | — | [1931] |
| 2 | 1909–1909 | dipl. forestry | — | [1931] |
| 3 | 1909–1909 | asst. com., forests | Federated Malay States | [1931] |
| 4 | 1915–1915 | 2nd lieut. North. Fus. (T.F.) | — | [1931] |
| 5 | 1916–1916 | lieut. | — | [1931] |
| 6 | 1916–1916 | temp. capt. | — | [1931] |
| 7 | 1917–1917 | intel. corps. | — | [1931] |
| 8 | 1919–1919 | rtnd. | Federated Malay States | [1931] |
| 9 | 1920–1923 | ag. dep. com., forests | Selangor | [1931] |
| 10 | 1926–1926 | dep. com., forests | Straits Settlements and Federated Malay States | [1931] |
| 11 | 1927–1928 | ag. per. asst. to com., forests | — | [1931] |
| 12 | 1930–1930 | conserv., forests | — | [1931] |

## Candidate stint `Rabaud, A___Mauritius___1925`

- Staff-list name: **Rabaud, A** | colony: **Mauritius** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | A. Rabaud | 1st Class Tidewater | Outdoor Branch | — | — |
| 1927 | A. Rabaud | 1st Class Tidewaiter | Outdoor Branch | — | — |

### Deterministic checks: `rabaut_arthur-edmund_b1885` vs `Rabaud, A___Mauritius___1925`

- [PASS] surname_gate: bio 'RABAUT' vs stint 'Rabaud, A' (fuzzy:1)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A']
- [PASS] age_gate: stint starts 1925, birth 1885 (age 40)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

