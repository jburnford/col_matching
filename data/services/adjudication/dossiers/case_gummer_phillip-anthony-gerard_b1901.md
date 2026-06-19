<!-- {"case_id": "case_gummer_phillip-anthony-gerard_b1901", "bio_ids": ["gummer_phillip-anthony-gerard_b1901"], "stint_ids": ["Gummer, P. A. G___Northern Rhodesia___1933"]} -->
# Dossier case_gummer_phillip-anthony-gerard_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gummer_phillip-anthony-gerard_b1901`

- Printed name: **GUMMER, Phillip Anthony Gerard**
- Birth year: 1901 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33053.v` — printed in editions [1948, 1949]:**

> GUMMER, Phillip Anthony Gerard.—b. 1901; dept. of customs and excise, U.K., 1920; acctnt., customs dept., N., Rhod., 1931; dep. comptlr. of customs, 1940; do., G.C., 1945; ag. comptlr, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | dept. of customs and excise, U.K | — | [1948, 1949] |
| 1 | 1931 | acctnt., customs dept., N., Rhod | — | [1948, 1949] |
| 2 | 1940 | dep. comptlr. of customs | — | [1948, 1949] |
| 3 | 1945 | dep. comptlr. of customs | Gold Coast | [1948, 1949] |
| 4 | 1946 | ag. comptlr | Gold Coast *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Gummer, P. A. G___Northern Rhodesia___1933`

- Staff-list name: **Gummer, P. A. G** | colony: **Northern Rhodesia** | listed 1933–1940 | editions [1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | P. A. G. Gummer | Accountant | Customs | — | — |
| 1934 | P. A. G. Gummer | Accountant | Customs | — | — |
| 1936 | P. A. G. Gummer | Accountant | Customs | — | — |
| 1937 | P. A. G. Gummer | Accountant | Customs | — | — |
| 1939 | P. A. G. Gummer | Accountant | Customs | — | — |
| 1940 | P. A. G. Gummer | Deputy Controller | Customs | — | — |

### Deterministic checks: `gummer_phillip-anthony-gerard_b1901` vs `Gummer, P. A. G___Northern Rhodesia___1933`

- [PASS] surname_gate: bio 'GUMMER' vs stint 'Gummer, P. A. G' (exact)
- [PASS] initials: bio ['P', 'A', 'G'] ~ stint ['P', 'A', 'G']
- [PASS] age_gate: stint starts 1933, birth 1901 (age 32)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

