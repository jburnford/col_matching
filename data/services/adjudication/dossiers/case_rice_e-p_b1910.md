<!-- {"case_id": "case_rice_e-p_b1910", "bio_ids": ["rice_e-p_b1910"], "stint_ids": ["Rice, E. P___Kenya___1949"]} -->
# Dossier case_rice_e-p_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rice_e-p_b1910`

- Printed name: **RICE, E. P**
- Birth year: 1910 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L26362.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> RICE, E. P.—b. 1910; ed. Abingdon Sch., and Royal Vet. Coll.; mil. serv., 1941-45; vet. offr., S. Rhod., 1934; Ken., 1946; asst. D.V.S., 1952; D.D.V.S., 1955-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | vet. offr. | Southern Rhodesia | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1946 | vet. offr. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1952 | asst. D.V.S | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1955–1962 | D.D.V.S | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Rice, E. P___Kenya___1949`

- Staff-list name: **Rice, E. P** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. P. Rice | Senior Veterinary Officers | Veterinary | — | — |
| 1950 | E. P. Rice | Senior Veterinary Officer | Veterinary | — | — |
| 1951 | E. P. Rice | Senior Veterinary Officers | VETERINARY | — | — |

### Deterministic checks: `rice_e-p_b1910` vs `Rice, E. P___Kenya___1949`

- [PASS] surname_gate: bio 'RICE' vs stint 'Rice, E. P' (exact)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E', 'P']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 48 vs bar 60: 'vet. offr.' ~ 'Senior Veterinary Officer'
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

