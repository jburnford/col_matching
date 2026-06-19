<!-- {"case_id": "case_wickham_dennis-henry_b1896", "bio_ids": ["wickham_dennis-henry_b1896"], "stint_ids": ["Wickham, D. H___British Somaliland___1930"]} -->
# Dossier case_wickham_dennis-henry_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wickham_dennis-henry_b1896`

- Printed name: **WICKHAM, Dennis Henry**
- Birth year: 1896 (attested in editions [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940])
- Appears in editions: [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1930-L69363.v` — printed in editions [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940]:**

> WICKHAM, Capt. Dennis Henry.—B. 1896; ed. Winchester Coll. and New Coll., Oxford; Connaught Rangers, Sept., 1914; served B.E.F., France, 1915-18; mentd. in despatches; transfd. to Queen's Royal Regt., 1922; served with 5th K.A.R., Kenya, 1922-25; admive. offr., Kenya col.; seconded to Somaliland, Apr., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Connaught Rangers | — | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940] |
| 1 | 1915–1918 | served B.E.F., France | — | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940] |
| 2 | 1922 | transfd. to Queen's Royal Regt | — | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940] |
| 3 | 1922–1925 | served with 5th K.A.R. | Kenya | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940] |
| 4 | 1929 | seconded to Somaliland | Kenya *(inherited from previous clause)* | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940] |

## Candidate stint `Wickham, D. H___British Somaliland___1930`

- Staff-list name: **Wickham, D. H** | colony: **British Somaliland** | listed 1930–1933 | editions [1930, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | D. H. Wickham | Commissioner | Administration | — | Captain |
| 1932 | D. H. Wickham | Commissioner | Administration | — | Captain |
| 1933 | D. H. Wickham | Assistant District Officer | Administration | — | Captain |

### Deterministic checks: `wickham_dennis-henry_b1896` vs `Wickham, D. H___British Somaliland___1930`

- [PASS] surname_gate: bio 'WICKHAM' vs stint 'Wickham, D. H' (exact)
- [PASS] initials: bio ['D', 'H'] ~ stint ['D', 'H']
- [PASS] age_gate: stint starts 1930, birth 1896 (age 34)
- [FAIL] colony: no placed event resolves to 'British Somaliland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1933
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

