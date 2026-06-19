<!-- {"case_id": "case_walwyn_algernon-edward-vere_b1888", "bio_ids": ["walwyn_algernon-edward-vere_b1888", "walwyn_algernon-edward-vero_b1888"], "stint_ids": ["Walwyn, A. E. V___Nigeria___1934"]} -->
# Dossier case_walwyn_algernon-edward-vere_b1888

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Walwyn, A. E. V___Nigeria___1934'] have more than one claimant biography in this case.

## Biography `walwyn_algernon-edward-vere_b1888`

- Printed name: **WALWYN, ALGERNON EDWARD VERE**
- Birth year: 1888 (attested in editions [1937, 1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L65586.v` — printed in editions [1937, 1939, 1940]:**

> WALWYN, ALGERNON EDWARD VERE.—B. 1888; ed. Bath Coll. and Peterhouse, Camb.; asst. dist. offr., N. Provs., Nigeria, Apr., 1915; rea., Sept., 1932; sec., N. Provs., 1933; staff grade, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | asst. dist. offr., N. Provs. | Nigeria | [1937, 1939, 1940] |
| 1 | 1932 | rea | Nigeria *(inherited from previous clause)* | [1937, 1939, 1940] |
| 2 | 1933 | sec., N. Provs | Nigeria *(inherited from previous clause)* | [1937, 1939, 1940] |
| 3 | 1937 | staff grade | Nigeria *(inherited from previous clause)* | [1937, 1939, 1940] |

## Biography `walwyn_algernon-edward-vero_b1888`

- Printed name: **WALWYN, ALGERNON EDWARD VERO**
- Birth year: 1888 (attested in editions [1934, 1935, 1936])
- Appears in editions: [1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1934-L63848.v` — printed in editions [1934, 1935, 1936]:**

> WALWYN, ALGERNON EDWARD VERO.—B. 1888; ed. Bath Coll. and Peterhouse, Camb.; asst. dist. offr., N. Prova., Nigeria, Apr., 1915; res., Sept., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | asst. dist. offr., N. Prova. | Nigeria | [1934, 1935, 1936] |
| 1 | 1932 | res | Nigeria *(inherited from previous clause)* | [1934, 1935, 1936] |

## Candidate stint `Walwyn, A. E. V___Nigeria___1934`

- Staff-list name: **Walwyn, A. E. V** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | A. E. V. Walwyn | — | Administrative Service | — | — |
| 1939 | A. E. V. Walwyn | Secretary | Secretariat, Northern Provinces | — | — |

### Deterministic checks: `walwyn_algernon-edward-vere_b1888` vs `Walwyn, A. E. V___Nigeria___1934`

- [PASS] surname_gate: bio 'WALWYN' vs stint 'Walwyn, A. E. V' (exact)
- [PASS] initials: bio ['A', 'E', 'V'] ~ stint ['A', 'E', 'V']
- [PASS] age_gate: stint starts 1934, birth 1888 (age 46)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 50 vs bar 60: 'rea' ~ 'Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `walwyn_algernon-edward-vero_b1888` vs `Walwyn, A. E. V___Nigeria___1934`

- [PASS] surname_gate: bio 'WALWYN' vs stint 'Walwyn, A. E. V' (exact)
- [PASS] initials: bio ['A', 'E', 'V'] ~ stint ['A', 'E', 'V']
- [PASS] age_gate: stint starts 1934, birth 1888 (age 46)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 33 vs bar 60: 'res' ~ 'Secretary'
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

