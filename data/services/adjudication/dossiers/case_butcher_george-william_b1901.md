<!-- {"case_id": "case_butcher_george-william_b1901", "bio_ids": ["butcher_george-william_b1901"], "stint_ids": ["Butcher, G. W___Falkland Islands___1930"]} -->
# Dossier case_butcher_george-william_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `butcher_george-william_b1901`

- Printed name: **BUTCHER, George William**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31552.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BUTCHER, George William.—b. 1901; on naval serv. 1917–28; wireless offr., Falk. Is., 1929; linesman, 1930; elec.-in-chge., 1935; bcast. offr., G.C., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1928 | on naval serv | — | [1948, 1949, 1950, 1951] |
| 1 | 1929 | wireless offr. | Falkland Islands | [1948, 1949, 1950, 1951] |
| 2 | 1930 | linesman | Falkland Islands *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1935 | elec.-in-chge | Falkland Islands *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1936 | bcast. offr. | Gold Coast | [1948, 1949, 1950, 1951] |

## Candidate stint `Butcher, G. W___Falkland Islands___1930`

- Staff-list name: **Butcher, G. W** | colony: **Falkland Islands** | listed 1930–1936 | editions [1930, 1931, 1932, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | G. W. Butcher | Operator | Wireless Service | — | — |
| 1931 | G. W. Butcher | Linemen | Telephones and Electrical Services | — | — |
| 1932 | G. W. Butcher | Linemen | Telephones and Electrical Services | — | — |
| 1933 | G. W. Butcher | Linesman | Telephones and Electrical Services | — | — |
| 1934 | G. W. Butcher | Linesman | Telephones and Electrical Services | — | — |
| 1936 | G. W. Butcher | Chief Electrician | Telephones and Electrical Services | — | — |

### Deterministic checks: `butcher_george-william_b1901` vs `Butcher, G. W___Falkland Islands___1930`

- [PASS] surname_gate: bio 'BUTCHER' vs stint 'Butcher, G. W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1930, birth 1901 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Falkland Islands'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1930-1936
- [PASS] position_sim: best 100 vs bar 60: 'linesman' ~ 'Linesman'
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

