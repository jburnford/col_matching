<!-- {"case_id": "case_okeden_w-e-p_e1890", "bio_ids": ["okeden_w-e-p_e1890"], "stint_ids": ["Okeden, W. E. Parry___Queensland___1888", "Okeden, W. E. Parry___Queensland___1899"]} -->
# Dossier case_okeden_w-e-p_e1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `okeden_w-e-p_e1890`

- Printed name: **OKEDEN, W. E. P**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1899, 1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1894-L33278.v` — printed in editions [1894, 1896, 1897, 1899, 1900, 1905, 1906]:**

> OKEDEN, W. E. P.—Formerly immigration agent, Brisbane; under colonial secretary, Queen's land, 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | under colonial secretary | Queen's land | [1894, 1896, 1897, 1899, 1900, 1905, 1906] |

## Candidate stint `Okeden, W. E. Parry___Queensland___1888`

- Staff-list name: **Okeden, W. E. Parry** | colony: **Queensland** | listed 1888–1890 | editions [1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | W. E. P. Okeden | Immigration Agent | Colonial Secretary's Department | — | — |
| 1890 | W. E. P. Okeden | Immigration Agent | Colonial Secretary's Department | — | — |

### Deterministic checks: `okeden_w-e-p_e1890` vs `Okeden, W. E. Parry___Queensland___1888`

- [PASS] surname_gate: bio 'OKEDEN' vs stint 'Okeden, W. E. Parry' (exact)
- [PASS] initials: bio ['W', 'E', 'P'] ~ stint ['W', 'E', 'P']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1890
- [FAIL] position_sim: best 24 vs bar 60: 'under colonial secretary' ~ 'Immigration Agent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Okeden, W. E. Parry___Queensland___1899`

- Staff-list name: **Okeden, W. E. Parry** | colony: **Queensland** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | W. E. Parry Okeden | Commissioner of Police | Home Secretary's Department | — | — |
| 1900 | W. E. Parry Okeden | Commissioner of Police | Home Secretary's Department | — | — |

### Deterministic checks: `okeden_w-e-p_e1890` vs `Okeden, W. E. Parry___Queensland___1899`

- [PASS] surname_gate: bio 'OKEDEN' vs stint 'Okeden, W. E. Parry' (exact)
- [PASS] initials: bio ['W', 'E', 'P'] ~ stint ['W', 'E', 'P']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1899-1900
- [FAIL] position_sim: best 35 vs bar 60: 'under colonial secretary' ~ 'Commissioner of Police'
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

