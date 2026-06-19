<!-- {"case_id": "case_croal_george-henry_b1893", "bio_ids": ["croal_george-henry_b1893"], "stint_ids": ["Croal, G. H___British Guiana___1912"]} -->
# Dossier case_croal_george-henry_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `croal_george-henry_b1893`

- Printed name: **CROAL, George Henry**
- Birth year: 1893 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32033.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CROAL, George Henry.—b. 1893; ed. Middle Sch.; cl. asst. med. dept., Br. Guiana, 1911; 5th cl. offr., customs, 1915; asst. comptlr. of customs, 1944; comptlr. of customs, 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | cl. asst. med. dept. | British Guiana | [1948, 1949, 1950, 1951] |
| 1 | 1915 | 5th cl. offr., customs | British Guiana *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1944 | asst. comptlr. of customs | British Guiana *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1945 | comptlr. of customs | British Guiana *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Croal, G. H___British Guiana___1912`

- Staff-list name: **Croal, G. H** | colony: **British Guiana** | listed 1912–1939 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1930, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | G. H. Croal | — | General Register Office | — | — |
| 1913 | G. H. Croal | Clerical Assistant | Medical Department | — | — |
| 1914 | G. H. Croal | 6th Class Clerk | Prisons | — | — |
| 1915 | G. H. Croal | 6th Class Clerk | Prisons | — | — |
| 1917 | G. H. Croal | 5th | Customs | — | — |
| 1918 | G. H. Croal | 5th | Customs | — | — |
| 1919 | G. H. Croal | 5th Class | Customs | — | — |
| 1920 | G. H. Croal | 5th Class | Customs | — | — |
| 1921 | G. H. Croal | 5th Class | Customs | — | — |
| 1922 | G. H. Croal | 5th | Customs | — | — |
| 1923 | G. H. Croal | 5th Class Clerk | Harbours | — | — |
| 1925 | G. H. Croal | 4th | Customs | — | — |
| 1927 | G. H. Croal | Deputy Harbour Master | Harbour Dept.—Harbour Board | — | — |
| 1927 | G. H. Croal | Sub-Comptroller | Customs | — | — |
| 1928 | G. H. Croal | Sub-Comptroller | Customs | — | — |
| 1928 | G. H. Croal | Deputy Harbour Master | Harbour Dept.—Harbour Board | — | — |
| 1929 | G. H. Croal | Deputy Harbour Master | Harbour Department—Harbour Board | — | — |
| 1929 | G. H. Croal | Sub-Controller | Customs | — | — |
| 1930 | G. H. Croal | Deputy Harbour Master | Harbour Department | — | — |
| 1930 | G. H. Croal | Sub-Controller | Customs | — | — |
| 1939 | G. H. Croal | Class II Clerk | Customs | — | — |

### Deterministic checks: `croal_george-henry_b1893` vs `Croal, G. H___British Guiana___1912`

- [PASS] surname_gate: bio 'CROAL' vs stint 'Croal, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1912, birth 1893 (age 19)
- [PASS] colony: 4 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1912-1939
- [PASS] position_sim: best 100 vs bar 60: '5th cl. offr., customs' ~ '5th'
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

