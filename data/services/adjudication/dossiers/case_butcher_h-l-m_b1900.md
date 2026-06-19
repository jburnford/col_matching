<!-- {"case_id": "case_butcher_h-l-m_b1900", "bio_ids": ["butcher_h-l-m_b1900"], "stint_ids": ["Butcher, H. L. M___Nigeria___1934"]} -->
# Dossier case_butcher_h-l-m_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `butcher_h-l-m_b1900`

- Printed name: **BUTCHER, H. L. M**
- Birth year: 1900 (attested in editions [1953, 1954, 1955, 1956])
- Appears in editions: [1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1953-L16766.v` — printed in editions [1953, 1954, 1955, 1956]:**

> BUTCHER, H. L. M.—b. 1900 ; ed. Bedford Gram. Sch., Dean Close Sch., Cheltenham, and Camb. Univ. ; mil. serv., 1940-41, capt. ; cadet, Nig., 1925 ; admin. offr., cl. II, 1944 ; cl. I, 1948 ; sole comsnr., Ibadan, into allegation against Chief Salami Agbaje and Native Auth.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | cadet | Nigeria | [1953, 1954, 1955, 1956] |
| 1 | 1944 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 2 | 1948 | cl. I | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |

## Candidate stint `Butcher, H. L. M___Nigeria___1934`

- Staff-list name: **Butcher, H. L. M** | colony: **Nigeria** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | H. L. M. Butcher | — | Administrative Service | — | — |
| 1936 | H. L. M. Butcher | Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `butcher_h-l-m_b1900` vs `Butcher, H. L. M___Nigeria___1934`

- [PASS] surname_gate: bio 'BUTCHER' vs stint 'Butcher, H. L. M' (exact)
- [PASS] initials: bio ['H', 'L', 'M'] ~ stint ['H', 'L', 'M']
- [PASS] age_gate: stint starts 1934, birth 1900 (age 34)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 25 vs bar 60: 'cadet' ~ 'Assistant Secretary'
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

