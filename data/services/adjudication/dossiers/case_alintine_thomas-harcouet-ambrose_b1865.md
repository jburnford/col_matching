<!-- {"case_id": "case_alintine_thomas-harcouet-ambrose_b1865", "bio_ids": ["alintine_thomas-harcouet-ambrose_b1865"], "stint_ids": ["Valentine, T. H. A___New Zealand___1912", "Valintine, T. H. A___New Zealand___1920"]} -->
# Dossier case_alintine_thomas-harcouet-ambrose_b1865

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Valintine, T. H. A___New Zealand___1920` is also gate-compatible with biography(ies) outside this case: ['valintine_thomas-harcourt-ambrose_b1865'] (already linked elsewhere or filtered).

## Biography `alintine_thomas-harcouet-ambrose_b1865`

- Printed name: **ALINTINE, THOMAS HARCOUET AMBROSE**
- Birth year: 1865 (attested in editions [1925])
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L60014.v` — printed in editions [1925]:**

> ALINTINE, THOMAS HARCOUET AMBROSE, E. (1919). M.R.C.S. (Eng.), L.R.C.P. (Lond.), H. (R.C.S. and R.C.P., Lond.)—B. 1865; Marlborough Coll. and St. Bartholomew's; dist. health offr., N.Z., 1901; astt. ch. th offr., 1902; inspr. gen. of hosps., 1907; health offr., 1909; dir., mily. hosps., 1915-19; gen. of pub. health, 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | dist. health offr. | New Zealand | [1925] |
| 1 | 1902 | astt. ch. th offr | New Zealand *(inherited from previous clause)* | [1925] |
| 2 | 1907 | inspr. gen. of hosps | New Zealand *(inherited from previous clause)* | [1925] |
| 3 | 1909 | health offr | New Zealand *(inherited from previous clause)* | [1925] |
| 4 | 1915–1919 | dir., mily. hosps | New Zealand *(inherited from previous clause)* | [1925] |
| 5 | 1921 | gen. of pub. health | New Zealand *(inherited from previous clause)* | [1925] |

## Candidate stint `Valentine, T. H. A___New Zealand___1912`

- Staff-list name: **Valentine, T. H. A** | colony: **New Zealand** | listed 1912–1917 | editions [1912, 1913, 1914, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | T. H. A. Valentine | Chief Health Officer | Public Health | — | — |
| 1913 | T. H. A. Valentine | Chief Health Officer | PUBLIC HEALTH | — | — |
| 1914 | T. H. A. Valentine | Inspector-General of Hospitals and Chief Health Officer | Hospitals and Charitable Aid and Public Health. | — | — |
| 1917 | T. H. A. Valentine | Inspector-General of Hospitals and Chief Health Officer | Hospitals and Charitable Aid and Public Health | — | — |

### Deterministic checks: `alintine_thomas-harcouet-ambrose_b1865` vs `Valentine, T. H. A___New Zealand___1912`

- [PASS] surname_gate: bio 'ALINTINE' vs stint 'Valentine, T. H. A' (fuzzy:2)
- [PASS] initials: bio ['T', 'H', 'A'] ~ stint ['T', 'H', 'A']
- [PASS] age_gate: stint starts 1912, birth 1865 (age 47)
- [PASS] colony: 6 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1912-1917
- [PASS] position_sim: best 71 vs bar 60: 'health offr' ~ 'Chief Health Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Valintine, T. H. A___New Zealand___1920`

- Staff-list name: **Valintine, T. H. A** | colony: **New Zealand** | listed 1920–1922 | editions [1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | T. H. A. Valintine | Inspector-General of Hospitals and Chief Health Officer, Director of Military Hospitals, and Registrar of Nurses and Midwives | Hospitals and Charitable Aid and Public Health | — | — |
| 1922 | T. H. A. Valintine | Director-General of Health and Registrar of Nurses and Midwives | Department of Health | — | — |

### Deterministic checks: `alintine_thomas-harcouet-ambrose_b1865` vs `Valintine, T. H. A___New Zealand___1920`

- [PASS] surname_gate: bio 'ALINTINE' vs stint 'Valintine, T. H. A' (fuzzy:1)
- [PASS] initials: bio ['T', 'H', 'A'] ~ stint ['T', 'H', 'A']
- [PASS] age_gate: stint starts 1920, birth 1865 (age 55)
- [PASS] colony: 6 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1920-1922
- [PASS] position_sim: best 69 vs bar 60: 'gen. of pub. health' ~ 'Inspector-General of Hospitals and Chief Health Officer, Director of Military Hospitals, and Registrar of Nurses and Midwives'
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

