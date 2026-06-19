<!-- {"case_id": "case_walters_a-w_b1900", "bio_ids": ["walters_a-w_b1900", "walters_arthur-willoughby_b1900"], "stint_ids": ["Walters, A. W___Swaziland___1925"]} -->
# Dossier case_walters_a-w_b1900

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Walters, A. W___Swaziland___1925'] have more than one claimant biography in this case.

## Biography `walters_a-w_b1900`

- Printed name: **WALTERS, A. W**
- Birth year: 1900 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958])
- Honours: C.B.E (1954), O.B.E
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1953-L19434.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958]:**

> WALTERS, A. W., C.B.E. (1954), O.B.E.—b. 1900; acctnt., Basuto., 1934; fin. sec., Bech. Prot., 1940; asst. ch. sec. (fin.) to high comsnr., 1950; sec. for fin., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | acctnt. | Basutoland | [1953, 1954, 1955, 1956, 1957, 1958] |
| 1 | 1940 | fin. sec. | Bechuanaland | [1953, 1954, 1955, 1956, 1957, 1958] |
| 2 | 1950 | asst. ch. sec. (fin.) to high comsnr | Bechuanaland *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958] |
| 3 | 1953 | sec. for fin | Bechuanaland *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958] |

## Biography `walters_arthur-willoughby_b1900`

- Printed name: **WALTERS, ARTHUR WILLOUGHBY**
- Birth year: 1900 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71553.v` — printed in editions [1939, 1940]:**

> WALTERS, ARTHUR WILLOUGHBY.—B. 1900; ed. Cordwallis Prep. Schol., Michaelhouse; secret. elk., Swaziland, 1919; dist. adminstr., Swaziland, 1920; treasy. elk., Swaziland, 1922; transf. as treasy. elk., grade I, to Basutoland, 1928; ag. finan. sec. in 1933, 1936 and 1937; ast., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919–1919 | secret. elk. | Swaziland | [1939, 1940] |
| 1 | 1920–1920 | dist. adminstr. | Swaziland | [1939, 1940] |
| 2 | 1922–1922 | treasy. elk. | Swaziland | [1939, 1940] |
| 3 | 1928–1928 | transf. as treasy. elk., grade I | Basutoland | [1939, 1940] |
| 4 | 1933–1937 | ag. finan. sec. | — | [1939, 1940] |
| 5 | 1934–1934 | ast. | — | [1939, 1940] |

## Candidate stint `Walters, A. W___Swaziland___1925`

- Staff-list name: **Walters, A. W** | colony: **Swaziland** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | A. W. Walters | Clerk | Administration Establishment | — | — |
| 1927 | A. W. Walters | Clerk | Administration Establishment | — | — |

### Deterministic checks: `walters_a-w_b1900` vs `Walters, A. W___Swaziland___1925`

- [PASS] surname_gate: bio 'WALTERS' vs stint 'Walters, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1925, birth 1900 (age 25)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `walters_arthur-willoughby_b1900` vs `Walters, A. W___Swaziland___1925`

- [PASS] surname_gate: bio 'WALTERS' vs stint 'Walters, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1925, birth 1900 (age 25)
- [PASS] colony: 3 placed event(s) resolve to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

