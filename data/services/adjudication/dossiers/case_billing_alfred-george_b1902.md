<!-- {"case_id": "case_billing_alfred-george_b1902", "bio_ids": ["billing_alfred-george_b1902"], "stint_ids": ["Billing, A. G___Federation of Malaya___1950"]} -->
# Dossier case_billing_alfred-george_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `billing_alfred-george_b1902`

- Printed name: **BILLING, ALFRED GEORGE**
- Birth year: 1902 (attested in editions [1940])
- Honours: M.Q.I.S
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L62404.v` — printed in editions [1940]:**

> BILLING, ALFRED GEORGE, M.Q.I.S.—B. 1902; ed. Gram. Sch., Queensland, Australia; survey dept., Queensland, 1918-23; surv.-on-agr., F.M.S., Mar., 1924; asst. supt., Mar., 1928; title changed to senr. surv., Sept., 1938; ag. dep. ch. surv., S'pore., Sept., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1923 | survey dept. | Queensland | [1940] |
| 1 | 1924 | surv.-on-agr. | Federated Malay States | [1940] |
| 2 | 1928 | asst. supt | Federated Malay States *(inherited from previous clause)* | [1940] |
| 3 | 1938 | title changed to senr. surv | Federated Malay States *(inherited from previous clause)* | [1940] |

## Candidate stint `Billing, A. G___Federation of Malaya___1950`

- Staff-list name: **Billing, A. G** | colony: **Federation of Malaya** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. G. Billing | Surveyor-General | Civil Establishment | — | — |
| 1952 | A. G. Billing | Surveyor-General, Malaya* | Civil Establishment | — | — |

### Deterministic checks: `billing_alfred-george_b1902` vs `Billing, A. G___Federation of Malaya___1950`

- [PASS] surname_gate: bio 'BILLING' vs stint 'Billing, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1950, birth 1902 (age 48)
- [FAIL] colony: no placed event resolves to 'Federation of Malaya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

