<!-- {"case_id": "case_le-pelley_richard-henry_b1903", "bio_ids": ["le-pelley_richard-henry_b1903"], "stint_ids": ["Le Pelley, R. H___Kenya___1931", "Le Pelley, R. H___Kenya___1950"]} -->
# Dossier case_le-pelley_richard-henry_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `le-pelley_richard-henry_b1903`

- Printed name: **LE PELLEY, Richard Henry**
- Birth year: 1903 (attested in editions [1957, 1958, 1959])
- Honours: A.R.C.S, D.I.C
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1957-L24957.v` — printed in editions [1957, 1958, 1959]:**

> LE PELLEY, R. H.—b. 1903; ed. Elizabeth Coll., Guernsey, and Royal Coll. of Science, London; asst. entom., Ken., 1929; senr., and hd. of section, 1946; senr. research offr., 1953; mem., E.A. anti-locust directorate, 1943-48.

**Version `col1960-L25189.v` — printed in editions [1960]:**

> LE PELEY, R. H.—b. 1903; ed. Elizabeth Coll., Guernsey, and Royal Coll. of Science, London; asst. entom., Ken., 1929; senr., and hd. of section, 1946; senr. research offr., 1953-59; mem., E.A. antilocus directorate, 1943-48.

**Version `col1948-L34002.v` — printed in editions [1948, 1949, 1950, 1951]:**

> LE PELLEY, Richard Henry, A.R.C.S., D.I.C., B.Sc., Ph.D. (Lond.)—b. 1903; ed. Elizabeth Coll., Guernsey, Imperial Coll. of Sci. and Tech., London; asst. entomologist, Ken., 1929; senr. entomologist, 1946; mem. of E. A. anti-locust directorate.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | asst. entom. | Kenya | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960] |
| 1 | 1943–1948 | mem., E.A. anti-locust directorate | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960] |
| 2 | 1946 | senr., and hd. of section | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960] |
| 3 | 1953 | senr. research offr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960] |

## Candidate stint `Le Pelley, R. H___Kenya___1931`

- Staff-list name: **Le Pelley, R. H** | colony: **Kenya** | listed 1931–1940 | editions [1931, 1932, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. H. Le Pelley | Entomologist | Scott Agricultural Laboratories | — | — |
| 1932 | R. H. Le Pelley | Entomologist | Scott Agricultural Laboratories | — | — |
| 1934 | R. H. Le Pelley | Entomologists | Scott Agricultural Laboratories | — | — |
| 1937 | R. H. Le Pelley | Entomologist | Scott Agricultural Laboratories | — | — |
| 1939 | R. H. Le Pelley | Entomologist | Agricultural Department | — | — |
| 1940 | R. H. Le Pelley | Entomologists | Agricultural Department | — | — |

### Deterministic checks: `le-pelley_richard-henry_b1903` vs `Le Pelley, R. H___Kenya___1931`

- [PASS] surname_gate: bio 'LE PELLEY' vs stint 'Le Pelley, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1931, birth 1903 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1940
- [FAIL] position_sim: best 45 vs bar 60: 'asst. entom.' ~ 'Entomologist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Le Pelley, R. H___Kenya___1950`

- Staff-list name: **Le Pelley, R. H** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. H. Le Pelley | Senior Entomologist | AGRICULTURE | — | — |
| 1951 | R. H. Le Pelley | Senior Entomologist | Agriculture | — | — |

### Deterministic checks: `le-pelley_richard-henry_b1903` vs `Le Pelley, R. H___Kenya___1950`

- [PASS] surname_gate: bio 'LE PELLEY' vs stint 'Le Pelley, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1950, birth 1903 (age 47)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 44 vs bar 60: 'senr., and hd. of section' ~ 'Senior Entomologist'
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

