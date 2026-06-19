<!-- {"case_id": "case_knight_norman-spencer_b1914", "bio_ids": ["knight_norman-spencer_b1914"], "stint_ids": ["Knight, N. S___Northern Rhodesia___1939"]} -->
# Dossier case_knight_norman-spencer_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 72 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `knight_norman-spencer_b1914`

- Printed name: **KNIGHT, Norman Spencer**
- Birth year: 1914 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L24771.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> KNIGHT, N. S.—b. 1914; ed. Uppingham Sch. and Oxford Univ.; mil. serv., 1939-44, lieut.; cadet, N. Rhod., 1937; D.O., 1939; asst. senr., 1953; secon., fedl. govt., 1955.

**Version `col1948-L33870.v` — printed in editions [1948, 1949, 1950, 1951]:**

> KNIGHT, Norman Spencer.—b. 1914; ed. Uppingham and Oxford, B.A.; on mil. serv., 1939-44, lieut.; cadet, N. Rhod., 1937; dist. offr., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1939 | cadet | Dominions Office | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1939 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1953 | asst. senr | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1955 | secon., fedl. govt | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Knight, N. S___Northern Rhodesia___1939`

- Staff-list name: **Knight, N. S** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | N. S. Knight | District Officer | District Administration | — | — |
| 1940 | N. S. Knight | District Officer | District Administration | — | — |

### Deterministic checks: `knight_norman-spencer_b1914` vs `Knight, N. S___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'KNIGHT' vs stint 'Knight, N. S' (exact)
- [PASS] initials: bio ['N', 'S'] ~ stint ['N', 'S']
- [PASS] age_gate: stint starts 1939, birth 1914 (age 25)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 72 vs bar 60: 'dist. offr' ~ 'District Officer'
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

