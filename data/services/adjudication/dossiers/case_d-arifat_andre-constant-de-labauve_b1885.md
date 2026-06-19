<!-- {"case_id": "case_d-arifat_andre-constant-de-labauve_b1885", "bio_ids": ["d-arifat_andre-constant-de-labauve_b1885"], "stint_ids": ["d'Arifat, C.L___Mauritius___1925"]} -->
# Dossier case_d-arifat_andre-constant-de-labauve_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `d-arifat_andre-constant-de-labauve_b1885`

- Printed name: **D'ARIFAT, Andre Constant de Labauve**
- Birth year: 1885 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63588.v` — printed in editions [1940]:**

> D'ARIFAT, Andre Constant de Labauve.—B. 1885; sany. warden, Mauritius, Jan., 1924; med. offr., hookworm br., May, 1927; dep. dir., med. services, Dec., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | sany. warden | Mauritius | [1940] |
| 1 | 1927 | med. offr., hookworm br | Mauritius *(inherited from previous clause)* | [1940] |
| 2 | 1932 | dep. dir., med. services | Mauritius *(inherited from previous clause)* | [1940] |

## Candidate stint `d'Arifat, C.L___Mauritius___1925`

- Staff-list name: **d'Arifat, C.L** | colony: **Mauritius** | listed 1925–1929 | editions [1925, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | C. L. d'Arifat | Medical Officers | Medical and Health Department | — | — |
| 1927 | Dr. C. L. d'Arifat | Medical Officer | Medical and Health Department | — | — |
| 1928 | C. L. d'Arifat | Medical Officer | Medical and Health Department | — | — |
| 1929 | C.L. d'Arifat | Medical Officer | Medical and Health Department | — | — |

### Deterministic checks: `d-arifat_andre-constant-de-labauve_b1885` vs `d'Arifat, C.L___Mauritius___1925`

- [PASS] surname_gate: bio 'D'ARIFAT' vs stint 'd'Arifat, C.L' (exact)
- [PASS] initials: bio ['A', 'C', 'D', 'L'] ~ stint ['C', 'L']
- [PASS] age_gate: stint starts 1925, birth 1885 (age 40)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1925-1929
- [FAIL] position_sim: best 46 vs bar 60: 'med. offr., hookworm br' ~ 'Medical Officer'
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

