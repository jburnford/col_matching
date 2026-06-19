<!-- {"case_id": "case_turbet_charles-rupert_b1897", "bio_ids": ["turbet_charles-rupert_b1897"], "stint_ids": ["Turbet, C. R___Fiji___1927"]} -->
# Dossier case_turbet_charles-rupert_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `turbet_charles-rupert_b1897`

- Printed name: **TURBET, CHARLES RUPERT**
- Birth year: 1897 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71315.v` — printed in editions [1939, 1940]:**

> TURBET, CHARLES RUPERT, B.V.Sc., M.R.C.V.S.—B. 1897; served, A.I.F., 1915-19, Egypt and France; vety. offr., Fiji, 1923; senr. vety. offr., 1930; ag. dir., agr., Fiji, 1937 and provisional offr. M.L.C.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | served, A.I.F. | Egypt and France | [1939, 1940] |
| 1 | 1923 | vety. offr. | Fiji | [1939, 1940] |
| 2 | 1930 | senr. vety. offr. | — | [1939, 1940] |
| 3 | 1937 | ag. dir., agr. and provisional offr. M.L.C. | Fiji | [1939, 1940] |

## Candidate stint `Turbet, C. R___Fiji___1927`

- Staff-list name: **Turbet, C. R** | colony: **Fiji** | listed 1927–1940 | editions [1927, 1929, 1930, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | C. R. Turbet | Veterinary Surgeons | Department of Agriculture | — | — |
| 1929 | C. R. Turbet | Veterinary Surgeon | Department of Agriculture | — | — |
| 1930 | C. R. Turbet | Senior Veterinary Officer | Department of Agriculture | — | — |
| 1932 | C. R. Turbet | Senior Veterinary Officer | Department of Agriculture | — | — |
| 1933 | C. R. Turbet | Senior Veterinary Officer | Department of Agriculture | — | — |
| 1934 | C. R. Turbet | Senior Veterinary Officer | Department of Agriculture | — | — |
| 1936 | C. R. Turbet | Senior Veterinary Officer | Department of Agriculture | — | — |
| 1937 | C. R. Turbet | Senior Veterinary Officer | Department of Agriculture | — | — |
| 1939 | C. R. Turbet | Senior Veterinary Officer | Agricultural Department | — | — |
| 1940 | C. R. Turbet | Senior Veterinary Officer | Agricultural Department | — | — |

### Deterministic checks: `turbet_charles-rupert_b1897` vs `Turbet, C. R___Fiji___1927`

- [PASS] surname_gate: bio 'TURBET' vs stint 'Turbet, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1927, birth 1897 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1940
- [FAIL] position_sim: best 53 vs bar 60: 'vety. offr.' ~ 'Senior Veterinary Officer'
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

