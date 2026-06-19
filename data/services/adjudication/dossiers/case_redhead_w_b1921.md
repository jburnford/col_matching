<!-- {"case_id": "case_redhead_w_b1921", "bio_ids": ["redhead_w_b1921"], "stint_ids": ["Redhead, W. A___Barbados___1955", "Redhead, W. A___Grenada___1963"]} -->
# Dossier case_redhead_w_b1921

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['redhead_w_b1921'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Redhead, W. A___Barbados___1955` is also gate-compatible with biography(ies) outside this case: ['redhead_w-a_b1909'] (already linked elsewhere or filtered).
- NOTE: stint `Redhead, W. A___Grenada___1963` is also gate-compatible with biography(ies) outside this case: ['redhead_w-a_b1909'] (already linked elsewhere or filtered).

## Biography `redhead_w_b1921`

- Printed name: **REDHEAD, W**
- Birth year: 1921 (attested in editions [1961])
- Appears in editions: [1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1961-L26547.v` — printed in editions [1961]:**

> REDHEAD, W.—b. 1921; ed. Chigwell Sch.; mil. serv., 1941–47, major; admin. cadet, G.C., 1949; asst. dist. comsnr., 1950; govt. agent, 1952; admin. offr., cl. II, 1955; cl. I, 1958–60 (Ghana civil service).

**Version `col1960-L27255.v` — printed in editions [1960]:**

> REDEHEAD, W.—b. 1921; ed. Chigwell Sch.; mil. serv., 1941–47, major; admin. cadet, G.C., 1949; asst. dist. comsnr., 1950; govt. agent, 1952; admin. offr., cl. II, 1955; cl. I, 1958–60 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | admin. cadet | Gold Coast | [1960, 1961] |
| 1 | 1950 | asst. dist. comsnr | Gold Coast *(inherited from previous clause)* | [1960, 1961] |
| 2 | 1952 | govt. agent | Gold Coast *(inherited from previous clause)* | [1960, 1961] |
| 3 | 1955 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1960, 1961] |
| 4 | 1958–1960 | cl. I | Gold Coast *(inherited from previous clause)* | [1960, 1961] |

## Candidate stint `Redhead, W. A___Barbados___1955`

- Staff-list name: **Redhead, W. A** | colony: **Barbados** | listed 1955–1962 | editions [1955, 1956, 1957, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | W. A. Redhead | Superintendent of Prison | Civil Establishment | — | — |
| 1956 | W. A. Redhead | Superintendent of Prisons | Civil Establishment | — | — |
| 1957 | W. A. Redhead | Superintendent of Prisons | Civil Establishment | — | — |
| 1962 | W. A. Redhead | District Officer, Carriacou | Civil Establishment | — | — |

### Deterministic checks: `redhead_w_b1921` vs `Redhead, W. A___Barbados___1955`

- [PASS] surname_gate: bio 'REDHEAD' vs stint 'Redhead, W. A' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1955, birth 1921 (age 34)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Redhead, W. A___Grenada___1963`

- Staff-list name: **Redhead, W. A** | colony: **Grenada** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | W. A. Redhead | District Officer | Civil Establishment | — | — |
| 1964 | W. A. Redhead | District Officer, Carriacou | Civil Establishment | — | — |
| 1965 | W. A. Redhead | District Officer | Civil Establishment | — | — |
| 1966 | W. A. Redhead | District Officer, Carriacou | Civil Establishment | — | — |

### Deterministic checks: `redhead_w_b1921` vs `Redhead, W. A___Grenada___1963`

- [PASS] surname_gate: bio 'REDHEAD' vs stint 'Redhead, W. A' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1963, birth 1921 (age 42)
- [FAIL] colony: no placed event resolves to 'Grenada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1966
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

