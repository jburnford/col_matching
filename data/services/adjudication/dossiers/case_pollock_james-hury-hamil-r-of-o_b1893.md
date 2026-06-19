<!-- {"case_id": "case_pollock_james-hury-hamil-r-of-o_b1893", "bio_ids": ["pollock_james-hury-hamil-r-of-o_b1893"], "stint_ids": ["Pollock, J. H. H___Palestine___1931"]} -->
# Dossier case_pollock_james-hury-hamil-r-of-o_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Pollock, J. H. H___Palestine___1931` is also gate-compatible with biography(ies) outside this case: ['pollock_james-huey-hamill_b1893'] (already linked elsewhere or filtered).

## Biography `pollock_james-hury-hamil-r-of-o_b1893`

- Printed name: **POLLOCK, JAMES HURY HAMIL (R. of O.)**
- Birth year: 1893 (attested in editions [1936, 1937, 1939])
- Honours: O.B.E (1939)
- Appears in editions: [1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1936-L63769.v` — printed in editions [1936, 1937, 1939]:**

> POLLOCK, CAPT. JAMES HURY HAMIL (R. of O.), O.B.E. (1939).—B. 1893; ed. Royal Schl., Armagh; war serv., 1914-20; Gallipoli, Macedonia, Egypt and Palestine; men. in despatch; staff capt., O.E.T.A.; inspr., grade 3, Palestine, July, 1920; dep. gov., grade 3, Ramallah, Oct., 1920; admstv. offr., Nigeria, Sept., 1923; asst. sec., secr., Lagos, Dec., 1927; admstv. offr., Palestine, Jan., 1930; asst. dist. commr., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | inspr., grade 3 | Palestine | [1936, 1937, 1939] |
| 1 | 1923 | admstv. offr. | Nigeria | [1936, 1937, 1939] |
| 2 | 1927 | asst. sec., secr. | Lagos | [1936, 1937, 1939] |
| 3 | 1930 | admstv. offr. | Palestine | [1936, 1937, 1939] |
| 4 | 1932 | asst. dist. commr | Palestine *(inherited from previous clause)* | [1936, 1937, 1939] |

## Candidate stint `Pollock, J. H. H___Palestine___1931`

- Staff-list name: **Pollock, J. H. H** | colony: **Palestine** | listed 1931–1946 | editions [1931, 1932, 1940, 1946]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. H. H. Pollock | District Officer | District Staff | — | — |
| 1932 | J. H. H. Pollock | District Officer | District Staff | — | — |
| 1940 | J. H. H. Pollock | Assistant District Commissioner | District Staff | — | — |
| 1946 | Captain J. H. H. Pollock | Member (personal capacity) | Advisory Council | C.M.G. | Captain |
| 1946 | Captain J. H. H. Pollock | District Commissioner (Jerusalem District) | Executive Council | C.M.G. | Captain |

### Deterministic checks: `pollock_james-hury-hamil-r-of-o_b1893` vs `Pollock, J. H. H___Palestine___1931`

- [PASS] surname_gate: bio 'POLLOCK' vs stint 'Pollock, J. H. H' (exact)
- [PASS] initials: bio ['J', 'H', 'H', 'O', 'O'] ~ stint ['J', 'H', 'H']
- [PASS] age_gate: stint starts 1931, birth 1893 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1946
- [PASS] position_sim: best 65 vs bar 60: 'asst. dist. commr' ~ 'Assistant District Commissioner'
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

