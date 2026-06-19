<!-- {"case_id": "case_humphreson_leslie-herrert_b1883", "bio_ids": ["humphreson_leslie-herrert_b1883"], "stint_ids": ["Humpherson, L. H___Sierra Leone___1925"]} -->
# Dossier case_humphreson_leslie-herrert_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `humphreson_leslie-herrert_b1883` ↔ `Humpherson, L. H___Sierra Leone___1925` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Humpherson, L. H___Sierra Leone___1925` is also gate-compatible with biography(ies) outside this case: ['humpherson_leslie-herbert_b1902'] (already linked elsewhere or filtered).

## Biography `humphreson_leslie-herrert_b1883`

- Printed name: **HUMPHRESON, LESLIE HERRERT**
- Birth year: 1883 (attested in editions [1927])
- Appears in editions: [1927]

### Verbatim printed entry text (OCR)

**Version `col1927-L59935.v` — printed in editions [1927]:**

> HUMPHRESON, LESLIE HERRERT.—B. 1883; ed. King Edward's Sch., Birmingham and Worcester Coll., Oxford; asst. dist. commr., Sierra Leone, 7th Jan., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. dist. commr. | Sierra Leone | [1927] |

## Candidate stint `Humpherson, L. H___Sierra Leone___1925`

- Staff-list name: **Humpherson, L. H** | colony: **Sierra Leone** | listed 1925–1937 | editions [1925, 1927, 1928, 1929, 1930, 1931, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | L. H. Humpherson | Civil Establishment | Civil Establishment | — | — |
| 1927 | L. H. Humpherson | Assistant District Commissioner | Provincial Administration | — | — |
| 1928 | L. H. Humpherson | Assistant District Commissioner | Civil Establishment | — | — |
| 1929 | L. H. Humpherson | Assistant District Commissioner | Provincial Administration | — | — |
| 1930 | L. H. Humpherson | Assistant District Commissioners | Provincial Administration | — | — |
| 1931 | L. H. Humpherson | Assistant District Commissioner | Provincial Administration | — | — |
| 1933 | L. H. Humpherson | District Commissioner | Provincial Administration | — | — |
| 1934 | L. H. Humpherson | District Commissioner | Civil Establishment | — | — |
| 1936 | L. H. Humpherson | District Commissioner | Civil Establishment | — | — |
| 1937 | L. H. Humpherson | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `humphreson_leslie-herrert_b1883` vs `Humpherson, L. H___Sierra Leone___1925`

- [PASS] surname_gate: bio 'HUMPHRESON' vs stint 'Humpherson, L. H' (fuzzy:2)
- [PASS] initials: bio ['L', 'H'] ~ stint ['L', 'H']
- [PASS] age_gate: stint starts 1925, birth 1883 (age 42)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1925-1937
- [PASS] position_sim: best 65 vs bar 60: 'asst. dist. commr.' ~ 'Assistant District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1927] pos~65 (bar: >=2)
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

