<!-- {"case_id": "case_owen_t-m_e1886", "bio_ids": ["owen_t-m_e1886"], "stint_ids": ["Owen, T. M___Natal___1888", "Owen, T. M___Natal___1905"]} -->
# Dossier case_owen_t-m_e1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 26 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `owen_t-m_e1886`

- Printed name: **OWEN, T. M**
- Birth year: not printed
- Appears in editions: [1913]

### Verbatim printed entry text (OCR)

**Version `col1913-L48509.v` — printed in editions [1913]:**

> OWEN, T. M.—Clerical asst., govt. house, Natal, 27th June, 1886; 3rd cls. elk., treas., th Jan., 1886; 2nd cls. elk., 1st July, 1890; 1st cls. elk., 1st July, 1896; ag. sec. to treas., 1890-1900; paymaster, volunteers, during S. African war; ch. elk., 1st Mch., 1901; acctnt., treas., 1st Mch., 1901; ch. acctnt., 1st July, 1903; comsnr. of stamps and sec. to Bond board; fixed estabnt.; ag. acctnt., dept. of finance, Union of S. Africa, 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886 | Clerical asst., govt. house | Natal | [1913] |
| 1 | 1890 | 2nd cls. elk | Natal *(inherited from previous clause)* | [1913] |
| 2 | 1896 | 1st cls. elk | Natal *(inherited from previous clause)* | [1913] |
| 3 | 1901 | ch. elk., 1st Mch | Natal *(inherited from previous clause)* | [1913] |
| 4 | 1903 | ch. acctnt | Natal *(inherited from previous clause)* | [1913] |
| 5 | 1911 | ag. acctnt., dept. of finance, Union of S. Africa | Natal *(inherited from previous clause)* | [1913] |

## Candidate stint `Owen, T. M___Natal___1888`

- Staff-list name: **Owen, T. M** | colony: **Natal** | listed 1888–1894 | editions [1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | T. M. Owen | Clerk | Treasury Office | — | — |
| 1889 | T. M. Owen | Clerk | Treasury Office | — | — |
| 1890 | T. M. Owen | Clerk | Treasury Office | — | — |
| 1894 | T. M. Owen | Clerk | Treasury Office | — | — |

### Deterministic checks: `owen_t-m_e1886` vs `Owen, T. M___Natal___1888`

- [PASS] surname_gate: bio 'OWEN' vs stint 'Owen, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1894
- [FAIL] position_sim: best 50 vs bar 60: '2nd cls. elk' ~ 'Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Owen, T. M___Natal___1905`

- Staff-list name: **Owen, T. M** | colony: **Natal** | listed 1905–1910 | editions [1905, 1906, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | T. M. Owen | Chief Accountant | Treasury | — | — |
| 1906 | T. M. Owen | Chief Accountant | Treasury | — | — |
| 1907 | T. M. Owen | Chief Accountant | Treasury | — | — |
| 1910 | T. M. Owen | Chief Accountant | Treasury | — | — |

### Deterministic checks: `owen_t-m_e1886` vs `Owen, T. M___Natal___1905`

- [PASS] surname_gate: bio 'OWEN' vs stint 'Owen, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1905-1910
- [PASS] position_sim: best 72 vs bar 60: 'ch. acctnt' ~ 'Chief Accountant'
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

