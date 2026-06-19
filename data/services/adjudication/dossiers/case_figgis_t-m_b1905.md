<!-- {"case_id": "case_figgis_t-m_b1905", "bio_ids": ["figgis_t-m_b1905"], "stint_ids": ["Figgis, T. M___Nyasaland___1949"]} -->
# Dossier case_figgis_t-m_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `figgis_t-m_b1905`

- Printed name: **FIGGIS, T. M**
- Birth year: 1905 (attested in editions [1957, 1958, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L22996.v` — printed in editions [1957, 1958, 1960, 1961, 1962, 1963]:**

> FIGGIS, T. M.—b. 1905; ed. Shrewsbury Sch. and Queen’s Univ., Belfast; barrister-at-law, Lincoln’s Inn; Japanese govt. educ. service, 1930–33; legal practice, 1934–36; law lecturer, 1936–39; Egyptian govt. service, 1940–45; resdt. mag., Nyasa., 1946; senr. resdt., mag. 1957–62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1933 | Japanese govt. educ. service | — | [1957, 1958, 1960, 1961, 1962, 1963] |
| 1 | 1934–1936 | legal practice | — | [1957, 1958, 1960, 1961, 1962, 1963] |
| 2 | 1936–1939 | law lecturer | — | [1957, 1958, 1960, 1961, 1962, 1963] |
| 3 | 1940–1945 | Egyptian govt. service | — | [1957, 1958, 1960, 1961, 1962, 1963] |
| 4 | 1946 | resdt. mag. | Nyasaland | [1957, 1958, 1960, 1961, 1962, 1963] |
| 5 | 1957–1962 | senr. resdt., mag | Nyasaland *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963] |

## Candidate stint `Figgis, T. M___Nyasaland___1949`

- Staff-list name: **Figgis, T. M** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. M. Figgis | Crown Counsel | LEGAL | — | — |
| 1950 | T. M. Figgis | Crown Counsel | LEGAL | — | — |
| 1951 | T. M. Figgis | Crown Counsel | LEGAL | — | — |

### Deterministic checks: `figgis_t-m_b1905` vs `Figgis, T. M___Nyasaland___1949`

- [PASS] surname_gate: bio 'FIGGIS' vs stint 'Figgis, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 18 vs bar 60: 'resdt. mag.' ~ 'Crown Counsel'
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

