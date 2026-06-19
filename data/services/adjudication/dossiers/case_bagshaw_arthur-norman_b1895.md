<!-- {"case_id": "case_bagshaw_arthur-norman_b1895", "bio_ids": ["bagshaw_arthur-norman_b1895"], "stint_ids": ["Bagshaw, A. N___Northern Rhodesia___1925"]} -->
# Dossier case_bagshaw_arthur-norman_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bagshaw_arthur-norman_b1895`

- Printed name: **BAGSHAW, Arthur Norman**
- Birth year: 1895 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.B.E
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L30919.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BAGSHAW, Arthur Norman, M.B.E.—b. 1895; ed. Kettering Gram. Sch. and Elstow Sch.; on mil. serv., 1939-42, maj., lieut.-col.; apptd. mil. branch police, N. Rhod., 1920; lt.-col. dir. of war evacuees and camps, 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | apptd. mil. branch police | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1944 | lt.-col. dir. of war evacuees and camps | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Bagshaw, A. N___Northern Rhodesia___1925`

- Staff-list name: **Bagshaw, A. N** | colony: **Northern Rhodesia** | listed 1925–1939 | editions [1925, 1927, 1929, 1931, 1933, 1934, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | A. N. Bagshaw | Lieutenant | Military Branch | — | — |
| 1927 | A. N. Bagshaw | Lieutenants | Military Branch | — | — |
| 1929 | A. N. Bagshaw | Adjutant | Northern Rhodesia Police - Headquarters Staff | — | — |
| 1931 | A. N. Bagshaw | Lieutenant | Military Branch | — | Lieutenant |
| 1933 | A. N. Bagshaw | Captain | Northern Rhodesia Police (Military) | — | Captain |
| 1934 | A. N. Bagshaw | Captain | Northern Rhodesia Police (Military) | — | — |
| 1936 | A. N. Bagshaw | Captain | Northern Rhodesia Regiment | — | — |
| 1937 | A. N. Bagshaw | Captain | Northern Rhodesia Regiment | — | Captain |
| 1939 | A. N. Bagshaw | Captain | Northern Rhodesia Regiment | — | Captain |

### Deterministic checks: `bagshaw_arthur-norman_b1895` vs `Bagshaw, A. N___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'BAGSHAW' vs stint 'Bagshaw, A. N' (exact)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1925, birth 1895 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1925-1939
- [FAIL] position_sim: best 33 vs bar 60: 'apptd. mil. branch police' ~ 'Captain'
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

