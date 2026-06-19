<!-- {"case_id": "case_wadeley_walter-joseph-durham_b1903", "bio_ids": ["wadeley_walter-joseph-durham_b1903"], "stint_ids": ["Wadley, W. J. D___Gold Coast___1927"]} -->
# Dossier case_wadeley_walter-joseph-durham_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `wadeley_walter-joseph-durham_b1903` ↔ `Wadley, W. J. D___Gold Coast___1927` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Wadley, W. J. D___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['wadley_walter-joseph-durham_b1903'] (already linked elsewhere or filtered).

## Biography `wadeley_walter-joseph-durham_b1903`

- Printed name: **WADELEY, Walter Joseph Durham**
- Birth year: 1903 (attested in editions [1955, 1957])
- Appears in editions: [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1955-L23170.v` — printed in editions [1955, 1957]:**

> WADELEY, W. J. D.—b. 1903; ed. Oxford Univ.; inspir., schs., G.C., 1926; dep. dir., educ., Ken., 1946; dir., 1930.

**Version `col1950-L40418.v` — printed in editions [1950, 1951, 1953, 1954, 1956, 1958, 1959]:**

> WADLEY, Walter Joseph Durham.—b. 1903; ed. Oxford Univ., M.A. (Oxon), inspr., schs., G.C., 1926; dep. dir., educ., Ken., 1946; dir., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | inspir., schs. | Gold Coast | [1955, 1957] |
| 1 | 1930 | dir | Kenya *(inherited from previous clause)* | [1955, 1957] |
| 2 | 1946 | dep. dir., educ. | Kenya | [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 3 | 1950 | dir | Kenya *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1956, 1958, 1959] |

## Candidate stint `Wadley, W. J. D___Gold Coast___1927`

- Staff-list name: **Wadley, W. J. D** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1929, 1930, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. J. D. Wadley | Inspector of Schools | Education Department | — | — |
| 1929 | W. J. D. Wadley | Inspector of Schools | Education Department | — | — |
| 1930 | W. J. D. Wadley | Inspector of Schools | Education Department | — | — |
| 1932 | W. J. D. Wadley | Inspectors of Schools | Education Department | — | — |
| 1936 | W. J. D. Wadley | Provincial Inspector and Inspector of Schools | Education Department | — | — |

### Deterministic checks: `wadeley_walter-joseph-durham_b1903` vs `Wadley, W. J. D___Gold Coast___1927`

- [PASS] surname_gate: bio 'WADELEY' vs stint 'Wadley, W. J. D' (fuzzy:1)
- [PASS] initials: bio ['W', 'J', 'D'] ~ stint ['W', 'J', 'D']
- [PASS] age_gate: stint starts 1927, birth 1903 (age 24)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1936
- [PASS] position_sim: best 65 vs bar 60: 'inspir., schs.' ~ 'Inspector of Schools'
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

