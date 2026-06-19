<!-- {"case_id": "case_coulthard_robert_b1899", "bio_ids": ["coulthard_robert_b1899"], "stint_ids": ["Coulthard, R___Nigeria___1928"]} -->
# Dossier case_coulthard_robert_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['coulthard_robert_b1899'] carry a single initial only — the namesake trap applies.

## Biography `coulthard_robert_b1899`

- Printed name: **COULTHARD, Robert**
- Birth year: 1899 (attested in editions [1958, 1959, 1960])
- Honours: M.R.C.V.S
- Appears in editions: [1948, 1950, 1951, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1958-L21651.v` — printed in editions [1958, 1959, 1960]:**

> COULTHARD, R.—b. 1899; ed. Felsted Sch., and Royal Vet. Coll., London; mil. serv., 1917-19, flt. lt.; appd. Nig., 1927; senr. vet. offr., 1938; game warden, N. Nig., 1956.

**Version `col1961-L21005.v` — printed in editions [1961]:**

> COUTHARD, R.—b. 1899; ed. Felsted Sch., and Royal Vet. Coll., London; mil. serv., 1917-19, flt. lt.; appd. Nig., 1927; senr. vet. offr., 1938; game warden, N. Nig., 1956.

**Version `col1948-L31939.v` — printed in editions [1948, 1950, 1951]:**

> COULTHARD, Robert, M.R.C.V.S.—b. 1899; ed. Seascake Prep. Sch., Felsted Sch. and Royal Veterinary Coll., Lond.; on war serv., 1917-18, fly. offr.; apptd. col. vet. serv., Nig., 1927; senr. vet. offr., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | appd. Nig | — | [1958, 1959, 1960, 1961] |
| 1 | 1927 | apptd. col. vet. serv. | Nigeria | [1948, 1950, 1951] |
| 2 | 1938 | senr. vet. offr | Nigeria *(inherited from previous clause)* | [1948, 1950, 1951, 1958, 1959, 1960, 1961] |
| 3 | 1956 | game warden | Northern Nigeria | [1958, 1959, 1960, 1961] |

## Candidate stint `Coulthard, R___Nigeria___1928`

- Staff-list name: **Coulthard, R** | colony: **Nigeria** | listed 1928–1939 | editions [1928, 1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | R. Coulthard | Veterinary Officer | Veterinary Department | — | — |
| 1929 | R. Coulthard | Veterinary Officer | Veterinary Department | — | — |
| 1930 | R. Coulthard | Veterinary Officer | Veterinary Department | — | — |
| 1933 | R. Coulthard | Veterinary Officer | Veterinary Department | — | — |
| 1934 | R. Coulthard | Veterinary Officer | Veterinary Department | — | — |
| 1936 | R. Coulthard | Veterinary Officer | Veterinary Department | — | — |
| 1939 | R. Coulthard | Veterinary Officer | Veterinary Department | — | — |

### Deterministic checks: `coulthard_robert_b1899` vs `Coulthard, R___Nigeria___1928`

- [PASS] surname_gate: bio 'COULTHARD' vs stint 'Coulthard, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1928, birth 1899 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1928-1939
- [FAIL] position_sim: best 58 vs bar 60: 'senr. vet. offr' ~ 'Veterinary Officer'
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

