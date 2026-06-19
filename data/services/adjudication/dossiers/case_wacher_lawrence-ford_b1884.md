<!-- {"case_id": "case_wacher_lawrence-ford_b1884", "bio_ids": ["wacher_lawrence-ford_b1884"], "stint_ids": ["Wacher, Lawrence Ford___Basutoland___1920"]} -->
# Dossier case_wacher_lawrence-ford_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wacher_lawrence-ford_b1884`

- Printed name: **WACHER, LAWRENCE FORD**
- Birth year: 1884 (attested in editions [1939, 1940])
- Honours: M.B.E (1937)
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71465.v` — printed in editions [1939, 1940]:**

> WACHER, LAWRENCE FORD, M.B.E. (1937).—B. 1884; ed. Waldon House Schl., Herne Bay, Kent Coast Coll. and Agrl. Coll., Wye; mem. staff, Wye Coll., 1910; agrl. offr., Basutoland, 1911; war serv., 1915-19; 2nd lieut., H.C.H.B., 1915; lieut., 1916; ag. capt. and adjt. 2nd D.A.C., 1918; returned to Basutoland, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | mem. staff, Wye Coll | — | [1939, 1940] |
| 1 | 1911 | agrl. offr. | Basutoland | [1939, 1940] |
| 2 | 1915 | 2nd lieut., H.C.H.B | Basutoland *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1916 | lieut | Basutoland *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1918 | ag. capt. and adjt. 2nd D.A.C | Basutoland *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1920 | returned to Basutoland | Basutoland *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Wacher, Lawrence Ford___Basutoland___1920`

- Staff-list name: **Wacher, Lawrence Ford** | colony: **Basutoland** | listed 1920–1925 | editions [1920, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Lawrence Ford Wacher | Agricultural Officer | Civil Establishment | — | — |
| 1920 | Lawrence Ford Wacher | Agricultural Officer | Establishment | — | — |
| 1921 | Lawrence Ford Wacher | Agricultural Officer | Establishment | — | — |
| 1922 | Lawrence Ford Wacher | Agricultural Officer | Establishment | — | — |
| 1924 | Lawrence Ford Wacher | Agricultural Officer | Veterinary and Agriculture | — | — |
| 1925 | Lawrence Ford Wacher | Agricultural Officer | Veterinary and Agriculture | — | — |

### Deterministic checks: `wacher_lawrence-ford_b1884` vs `Wacher, Lawrence Ford___Basutoland___1920`

- [PASS] surname_gate: bio 'WACHER' vs stint 'Wacher, Lawrence Ford' (exact)
- [PASS] initials: bio ['L', 'F'] ~ stint ['L', 'F']
- [PASS] age_gate: stint starts 1920, birth 1884 (age 36)
- [PASS] colony: 5 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1920-1925
- [FAIL] position_sim: best 38 vs bar 60: 'returned to Basutoland' ~ 'Agricultural Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

