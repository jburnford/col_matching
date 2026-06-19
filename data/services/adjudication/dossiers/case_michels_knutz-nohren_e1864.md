<!-- {"case_id": "case_michels_knutz-nohren_e1864", "bio_ids": ["michels_knutz-nohren_e1864", "michiels_knutz-nohren_e1864"], "stint_ids": ["Michels, K. N___Heligoland___1883"]} -->
# Dossier case_michels_knutz-nohren_e1864

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Michels, K. N___Heligoland___1883'] have more than one claimant biography in this case.

## Biography `michels_knutz-nohren_e1864`

- Printed name: **MICHELS, KNUTZ NOHREN**
- Birth year: not printed
- Appears in editions: [1888, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34906.v` — printed in editions [1888, 1890]:**

> MICHELS, KNUTZ NOHREN.—Town clerk, Heligoland, 1864 to 1865; bathing director, 1875; treasurer, 1882; reappointed town clerk and ex officio member of executive council of Heligoland, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864–1865 | Town clerk | Heligoland | [1888, 1890] |
| 1 | 1875 | bathing director | Heligoland *(inherited from previous clause)* | [1888, 1890] |
| 2 | 1882 | treasurer | Heligoland *(inherited from previous clause)* | [1888, 1890] |
| 3 | 1884 | reappointed town clerk and ex officio member of executive council of Heligoland | Heligoland *(inherited from previous clause)* | [1888, 1890] |

## Biography `michiels_knutz-nohren_e1864`

- Printed name: **MICHIELS, KNUTZ NOHREN**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L34634.v` — printed in editions [1889]:**

> MICHIELS, KNUTZ NOHREN.—Town clerk, Heligoland, 1864 to 1865; bathing director, 1875; treasurer, 1882; reappointed town clerk and ex officio member of executive council of Heligoland, 1864.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864–1865 | Town clerk | Heligoland | [1889] |
| 1 | 1875 | bathing director | Heligoland *(inherited from previous clause)* | [1889] |
| 2 | 1882 | treasurer | Heligoland *(inherited from previous clause)* | [1889] |

## Candidate stint `Michels, K. N___Heligoland___1883`

- Staff-list name: **Michels, K. N** | colony: **Heligoland** | listed 1883–1890 | editions [1883, 1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | K. N. Michels | Treasurer and Director of the Bathing Establishment | — | — | — |
| 1888 | K. N. Michels | Town Clerk, Treasurer and Director of Bathing Establishment | — | — | — |
| 1890 | K. N. Michels | Town Clerk, Treasurer and Director of Bathing Establishment | Civil Establishment | — | — |

### Deterministic checks: `michels_knutz-nohren_e1864` vs `Michels, K. N___Heligoland___1883`

- [PASS] surname_gate: bio 'MICHELS' vs stint 'Michels, K. N' (exact)
- [PASS] initials: bio ['K', 'N'] ~ stint ['K', 'N']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Heligoland'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1883-1890
- [PASS] position_sim: best 100 vs bar 60: 'bathing director' ~ 'Treasurer and Director of the Bathing Establishment'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `michiels_knutz-nohren_e1864` vs `Michels, K. N___Heligoland___1883`

- [PASS] surname_gate: bio 'MICHIELS' vs stint 'Michels, K. N' (fuzzy:1)
- [PASS] initials: bio ['K', 'N'] ~ stint ['K', 'N']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Heligoland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1883-1890
- [PASS] position_sim: best 100 vs bar 60: 'bathing director' ~ 'Treasurer and Director of the Bathing Establishment'
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

