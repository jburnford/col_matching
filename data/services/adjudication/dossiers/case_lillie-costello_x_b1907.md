<!-- {"case_id": "case_lillie-costello_x_b1907", "bio_ids": ["lillie-costello_x_b1907"], "stint_ids": ["Lillie-Costello, V. J. A___Gold Coast___1950"]} -->
# Dossier case_lillie-costello_x_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lillie-costello_x_b1907'] carry a single initial only — the namesake trap applies.

## Biography `lillie-costello_x_b1907`

- Printed name: **LILLIE-COSTELLO, (no given names printed)**
- Birth year: 1907 (attested in editions [1950, 1951, 1953, 1954])
- Honours: O.B.E, V. J. A
- Appears in editions: [1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1950-L37310.v` — printed in editions [1950, 1951, 1953, 1954]:**

> LILLIE-COSTELLO, Maj., V. J. A., O.B.E., M.C.—b. 1907; ed. Malvern Coll.; mil. serv., 1939-45; reg. inf. offr., B.W.A., 1946; P.R.O., G.C., 1948; dir., inf. servs., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | reg. inf. offr., B.W.A | — | [1950, 1951, 1953, 1954] |
| 1 | 1948 | P.R.O. | Gold Coast | [1950, 1951, 1953, 1954] |
| 2 | 1952 | dir., inf. servs | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |

## Candidate stint `Lillie-Costello, V. J. A___Gold Coast___1950`

- Staff-list name: **Lillie-Costello, V. J. A** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | V. J. A. Lillie-Costello | Public Relations Officer | Public Relations | — | — |
| 1951 | V. J. A. Lillie-Costello | Public Relations Officer | Public Relations Department | — | — |

### Deterministic checks: `lillie-costello_x_b1907` vs `Lillie-Costello, V. J. A___Gold Coast___1950`

- [PASS] surname_gate: bio 'LILLIE-COSTELLO' vs stint 'Lillie-Costello, V. J. A' (exact)
- [PASS] initials: bio ['?'] ~ stint ['V', 'J', 'A']
- [PASS] age_gate: stint starts 1950, birth 1907 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 38 vs bar 60: 'dir., inf. servs' ~ 'Public Relations Officer'
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

