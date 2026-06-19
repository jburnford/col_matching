<!-- {"case_id": "case_briscoe_henry-villiers_b1896", "bio_ids": ["briscoe_henry-villiers_b1896"], "stint_ids": ["Briscoe, H. V___Gold Coast___1949"]} -->
# Dossier case_briscoe_henry-villiers_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `briscoe_henry-villiers_b1896`

- Printed name: **BRISCOE, Henry Villiers**
- Birth year: 1896 (attested in editions [1950])
- Honours: C.I.E (1945), O.B.E
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L33888.v` — printed in editions [1950]:**

> BRISCOE, Capt. Henry Villiers, C.I.E. (1945), O.B.E., N.R. (retd.).—b. 1896; ed. R.N.C., Osborne, and Dartmouth and R.N.; war serv., 1941-45, R.N.; marine offr., T.T., 1931; port capt., Maur., 1939; harb. mstr., Trin., 1945; marine supt., Takoradi Harbour, G.C., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | marine offr., T.T | — | [1950] |
| 1 | 1939 | port capt. | Mauritius | [1950] |
| 2 | 1945 | harb. mstr. | Trinidad | [1950] |
| 3 | 1947 | marine supt., Takoradi Harbour | Gold Coast | [1950] |

## Candidate stint `Briscoe, H. V___Gold Coast___1949`

- Staff-list name: **Briscoe, H. V** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. V. Briscoe | Marine Superintendent | Railway and Takoradi Harbour | — | — |
| 1951 | Capt. H. V. Briscoe | Marine Superintendent | Marine Branch | — | Captain |

### Deterministic checks: `briscoe_henry-villiers_b1896` vs `Briscoe, H. V___Gold Coast___1949`

- [PASS] surname_gate: bio 'BRISCOE' vs stint 'Briscoe, H. V' (exact)
- [PASS] initials: bio ['H', 'V'] ~ stint ['H', 'V']
- [PASS] age_gate: stint starts 1949, birth 1896 (age 53)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 49 vs bar 60: 'marine supt., Takoradi Harbour' ~ 'Marine Superintendent'
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

