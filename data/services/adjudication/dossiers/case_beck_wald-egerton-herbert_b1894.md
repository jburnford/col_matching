<!-- {"case_id": "case_beck_wald-egerton-herbert_b1894", "bio_ids": ["beck_wald-egerton-herbert_b1894"], "stint_ids": ["Beck, W___Australia___1918"]} -->
# Dossier case_beck_wald-egerton-herbert_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beck_wald-egerton-herbert_b1894`

- Printed name: **BECK, WALD EGERTON HERBERT**
- Birth year: 1894 (attested in editions [1934])
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L56475.v` — printed in editions [1934]:**

> BECK, WALD EGERTON HERBERT.—B. 1894; ed. Weymouth Coll., Dorset; pol. prolbnt., F.M.S., Oct., 1914; 1st. asst. commr. pol., Selangor, Feb., 1923; aspt., convict estabt., Taiping and imp., prisons, F.M.S., Sept., 1923; offr. l/c, pol. dist., Kuantan, Aug., 1927; comdt. pol., depot, K. Lumpur, Mar., 1929; aspt., pol. S.S., Oct., 1931; ch. pol. offr., N. Sembilan, Feb., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | pol. prolbnt. | Federated Malay States | [1934] |
| 1 | 1923 | 1st. asst. commr. pol., Selangor | Federated Malay States | [1934] |
| 2 | 1927 | offr. l/c, pol. dist., Kuantan | Federated Malay States *(inherited from previous clause)* | [1934] |
| 3 | 1929 | comdt. pol., depot, K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1934] |
| 4 | 1931 | aspt., pol. S.S | Federated Malay States *(inherited from previous clause)* | [1934] |
| 5 | 1932 | ch. pol. offr., N. Sembilan | Federated Malay States *(inherited from previous clause)* | [1934] |

## Candidate stint `Beck, W___Australia___1918`

- Staff-list name: **Beck, W** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | W. Beck | Accountant | Industries Department and Agricultural Bank | — | — |
| 1927 | W. Beck | Accountant | Agricultural Bank, Industries Assistance Board and Soldiers Settlement Scheme | — | — |

### Deterministic checks: `beck_wald-egerton-herbert_b1894` vs `Beck, W___Australia___1918`

- [PASS] surname_gate: bio 'BECK' vs stint 'Beck, W' (exact)
- [PASS] initials: bio ['W', 'E', 'H'] ~ stint ['W']
- [PASS] age_gate: stint starts 1918, birth 1894 (age 24)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

