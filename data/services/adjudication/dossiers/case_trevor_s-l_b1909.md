<!-- {"case_id": "case_trevor_s-l_b1909", "bio_ids": ["trevor_s-l_b1909"], "stint_ids": ["Trevor, S. L___Northern Rhodesia___1949"]} -->
# Dossier case_trevor_s-l_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `trevor_s-l_b1909`

- Printed name: **TREVOR, S. L**
- Birth year: 1909 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Terminal: retired 1964 — “retd., apptd. vet. offr., Bech., 1964.”
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L28177.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> TREVOR, S. L.—b. 1909; ed. Pretoria Boys’ High Sch., Bootham Sch., York, and Vet. Coll., Dublin; mil. serv., 1940-46, lt.-col.; vet. offr., N. Rhod., 1946; ch. vet. offr., 1962-64; retd., apptd. vet. offr., Bech., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | vet. offr. | Northern Rhodesia | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1962–1964 | ch. vet. offr | Northern Rhodesia *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Trevor, S. L___Northern Rhodesia___1949`

- Staff-list name: **Trevor, S. L** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. L. Trevor | Veterinary Officers | Veterinary | — | — |
| 1951 | S. L. Trevor | Veterinary Officers | VETERINARY | — | — |

### Deterministic checks: `trevor_s-l_b1909` vs `Trevor, S. L___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'TREVOR' vs stint 'Trevor, S. L' (exact)
- [PASS] initials: bio ['S', 'L'] ~ stint ['S', 'L']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'vet. offr.' ~ 'Veterinary Officers'
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

