<!-- {"case_id": "case_bale_edgar-george_b1891", "bio_ids": ["bale_edgar-george_b1891"], "stint_ids": ["Bale, E. G___Kenya___1922"]} -->
# Dossier case_bale_edgar-george_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bale_edgar-george_b1891`

- Printed name: **BALE, EDGAR GEORGE**
- Birth year: 1891 (attested in editions [1930, 1931, 1932, 1933, 1935, 1936])
- Appears in editions: [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1930-L62357.v` — printed in editions [1930, 1931, 1932, 1933, 1935, 1936]:**

> BALE, EDGAR GEORGE.—B. 1891; ed. King Edward's Schol.; Imp. cust. and excise serv., 1912-21; asst. to comsnr. of cust., Kenya and Uganda, Mar., 1921; dep. comsnr., cust., April, 1923; ag. comsnr., cust., for various periods, 1924-29.

**Version `col1937-L58597.v` — printed in editions [1937]:**

> BALE, EDGAR GEORGE.—B. 1891; ed. King Edward's Schl.; Imp. cust. and excise serv., 1912-21; ast. to comanr. of cust., Kenya and Uganda, Mar., 1921; dep. comanr., cust., April, 1923; comanr., cust., May, 1936; chmn., harbr. advr. bd.; chmn., K.R.N.V.R. advr. comtee.

**Version `col1934-L56348.v` — printed in editions [1934]:**

> BALE, EDGAR GEORGE.—B. 1891; ed. King Edward's Schl.; Imp. cust. and excise serv., 1912-21; astl. to comanr. of cust., Kenya and

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912–1921 | Imp. cust. and excise serv | — | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1921 | asst. to comsnr. of cust., Kenya and Uganda | Kenya | [1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 2 | 1923 | dep. comsnr., cust | Kenya *(inherited from previous clause)* | [1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 3 | 1924–1929 | ag. comsnr., cust., for various periods | Kenya *(inherited from previous clause)* | [1930, 1931, 1932, 1933, 1935, 1936] |
| 4 | 1936 | comanr., cust | Kenya *(inherited from previous clause)* | [1937] |

## Candidate stint `Bale, E. G___Kenya___1922`

- Staff-list name: **Bale, E. G** | colony: **Kenya** | listed 1922–1932 | editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | E. G. Bale | Assistants | Customs | — | — |
| 1923 | E. G. Bale | Assistants | Customs | — | — |
| 1924 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |
| 1925 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |
| 1927 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |
| 1928 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |
| 1929 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |
| 1930 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |
| 1931 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |
| 1932 | E. G. Bale | Deputy Commissioner of Customs | Customs | — | — |

### Deterministic checks: `bale_edgar-george_b1891` vs `Bale, E. G___Kenya___1922`

- [PASS] surname_gate: bio 'BALE' vs stint 'Bale, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1922, birth 1891 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1922-1932
- [PASS] position_sim: best 67 vs bar 60: 'dep. comsnr., cust' ~ 'Deputy Commissioner of Customs'
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

