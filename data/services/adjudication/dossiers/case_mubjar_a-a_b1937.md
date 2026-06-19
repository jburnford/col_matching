<!-- {"case_id": "case_mubjar_a-a_b1937", "bio_ids": ["mubjar_a-a_b1937"], "stint_ids": ["Mubgar, Awadh bin Awadh___Aden___1964"]} -->
# Dossier case_mubjar_a-a_b1937

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mubjar_a-a_b1937`

- Printed name: **MUBJAR, A. A**
- Birth year: 1937 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L16819.v` — printed in editions [1966]:**

> MUBJAR, A. A.—b. 1937; ed. Bayoomi Coll., Aden, and Lib., London Univ.; barrister-at-law, Middle Temple; cr. coun., Aden, 1960; dep. advoc. gen. and dep. leg. sec., Fed. of S. Arabia, 1963; asst. atty-gen., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1960 | cr. coun. | Aden | [1966] |
| 1 | 1963 | dep. advoc. gen. and dep. leg. sec., Fed. of S. Arabia | Aden *(inherited from previous clause)* | [1966] |
| 2 | 1965 | asst. atty-gen | Aden *(inherited from previous clause)* | [1966] |

## Candidate stint `Mubgar, Awadh bin Awadh___Aden___1964`

- Staff-list name: **Mubgar, Awadh bin Awadh** | colony: **Aden** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | Awadh bin Awadh Mubgar | Deputy Advocate General and Deputy Legal Secretary | Civil Establishment | — | — |
| 1965 | Awadh bin Awadh Mubgar | Deputy Advocate General and Deputy Legal Secretary | Civil Establishment | — | — |

### Deterministic checks: `mubjar_a-a_b1937` vs `Mubgar, Awadh bin Awadh___Aden___1964`

- [PASS] surname_gate: bio 'MUBJAR' vs stint 'Mubgar, Awadh bin Awadh' (fuzzy:1)
- [PASS] initials: bio ['A', 'A'] ~ stint ['A', 'B', 'A']
- [PASS] age_gate: stint starts 1964, birth 1937 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1964-1965
- [PASS] position_sim: best 62 vs bar 60: 'dep. advoc. gen. and dep. leg. sec., Fed. of S. Arabia' ~ 'Deputy Advocate General and Deputy Legal Secretary'
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

