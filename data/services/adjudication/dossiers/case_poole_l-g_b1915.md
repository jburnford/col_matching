<!-- {"case_id": "case_poole_l-g_b1915", "bio_ids": ["poole_l-g_b1915"], "stint_ids": ["Poole, L. G___Fiji___1950"]} -->
# Dossier case_poole_l-g_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `poole_l-g_b1915`

- Printed name: **POOLE, L. G**
- Birth year: 1915 (attested in editions [1956, 1957, 1958, 1959, 1960])
- Appears in editions: [1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1956-L23569.v` — printed in editions [1956, 1957, 1958, 1959, 1960]:**

> POOLE, L. G.—b. 1915; ed. Liverpool Univ.; M.O., Fiji, 1943; S.M.O., 1952; specialist, 1956–59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | M.O. | Fiji | [1956, 1957, 1958, 1959, 1960] |
| 1 | 1952 | S.M.O | Fiji *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |
| 2 | 1956–1959 | specialist | Fiji *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Poole, L. G___Fiji___1950`

- Staff-list name: **Poole, L. G** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | L. G. Poole | Medical Officer | Medical | — | — |
| 1951 | L. G. Poole | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `poole_l-g_b1915` vs `Poole, L. G___Fiji___1950`

- [PASS] surname_gate: bio 'POOLE' vs stint 'Poole, L. G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1950, birth 1915 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

