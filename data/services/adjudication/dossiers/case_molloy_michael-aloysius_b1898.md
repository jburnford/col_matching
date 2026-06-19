<!-- {"case_id": "case_molloy_michael-aloysius_b1898", "bio_ids": ["molloy_michael-aloysius_b1898"], "stint_ids": ["Molloy, M. A___Tanganyika___1930"]} -->
# Dossier case_molloy_michael-aloysius_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `molloy_michael-aloysius_b1898`

- Printed name: **MOLLOY, MICHAEL ALOYSIUS**
- Birth year: 1898 (attested in editions [1939, 1940])
- Honours: M.R.C.V.S
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69163.v` — printed in editions [1939, 1940]:**

> MOLLOY, MICHAEL ALOYSIUS, M.R.C.V.S.—B. 1898; ed. Dominican Coll. and Christian Bros. Day Schl., Dublin, Castletknock Coll., Dublin, Salesian Coll., Farnboro' and Royal Coll. Vety. Surgeons, Dublin; vety. offr., Tanganyika Territory, July, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | vety. offr., Tanganyika Territory | Tanganyika | [1939, 1940] |

## Candidate stint `Molloy, M. A___Tanganyika___1930`

- Staff-list name: **Molloy, M. A** | colony: **Tanganyika** | listed 1930–1940 | editions [1930, 1933, 1934, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | M. A. Molloy | Veterinary Officer | Veterinary | — | — |
| 1933 | M. A. Molloy | Veterinary Officers | Veterinary | — | — |
| 1934 | M. A. Molloy | Veterinary Officers | Veterinary | — | — |
| 1940 | M. A. Molloy | Veterinary Officer | Veterinary | — | — |

### Deterministic checks: `molloy_michael-aloysius_b1898` vs `Molloy, M. A___Tanganyika___1930`

- [PASS] surname_gate: bio 'MOLLOY' vs stint 'Molloy, M. A' (exact)
- [PASS] initials: bio ['M', 'A'] ~ stint ['M', 'A']
- [PASS] age_gate: stint starts 1930, birth 1898 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1940
- [FAIL] position_sim: best 46 vs bar 60: 'vety. offr., Tanganyika Territory' ~ 'Veterinary Officer'
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

