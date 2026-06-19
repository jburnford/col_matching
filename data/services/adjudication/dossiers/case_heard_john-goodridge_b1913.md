<!-- {"case_id": "case_heard_john-goodridge_b1913", "bio_ids": ["heard_john-goodridge_b1913"], "stint_ids": ["Heard, J___Nigeria___1930"]} -->
# Dossier case_heard_john-goodridge_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heard_john-goodridge_b1913`

- Printed name: **HEARD, John Goodridge**
- Birth year: 1913 (attested in editions [1960, 1961])
- Honours: C.P.M (1952)
- Appears in editions: [1948, 1949, 1950, 1951, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1960-L23958.v` — printed in editions [1960, 1961]:**

> HEARD, J. G., C.P.M. (1952).—b. 1913; ed. St. Edward's, Oxford; police constable, Pal., 1933; asst. supt., Nig., 1939; supt., 1948; sen. supt., 1951; asst. comsnr., 1956-60.

**Version `col1948-L33263.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HEARD, John Goodridge.—b. 1913; ed. Probus Sch., Cornwall and St. Edward's Sch., Oxford; police const., Pal., 1933; sgt., 1938; asst. supt., police, Nig., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | police constable | Palestine | [1948, 1949, 1950, 1951, 1960, 1961] |
| 1 | 1938 | sgt | Palestine *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1939 | asst. supt. | Nigeria | [1948, 1949, 1950, 1951, 1960, 1961] |
| 3 | 1948 | supt | Nigeria *(inherited from previous clause)* | [1960, 1961] |
| 4 | 1951 | sen. supt | Nigeria *(inherited from previous clause)* | [1960, 1961] |
| 5 | 1956–1960 | asst. comsnr | Nigeria *(inherited from previous clause)* | [1960, 1961] |

## Candidate stint `Heard, J___Nigeria___1930`

- Staff-list name: **Heard, J** | colony: **Nigeria** | listed 1930–1939 | editions [1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | J. Heard | Veterinary Officer | Veterinary Department | — | — |
| 1933 | J. Heard | Veterinary Officer | Veterinary Department | — | — |
| 1934 | J. Heard | Veterinary Officer | Veterinary Department | — | — |
| 1936 | J. Heard | Veterinary Officer | Veterinary Department | — | — |
| 1939 | J. Heard | Veterinary Officer | Veterinary Department | — | — |

### Deterministic checks: `heard_john-goodridge_b1913` vs `Heard, J___Nigeria___1930`

- [PASS] surname_gate: bio 'HEARD' vs stint 'Heard, J' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J']
- [PASS] age_gate: stint starts 1930, birth 1913 (age 17)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1939
- [FAIL] position_sim: best 15 vs bar 60: 'asst. supt.' ~ 'Veterinary Officer'
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

