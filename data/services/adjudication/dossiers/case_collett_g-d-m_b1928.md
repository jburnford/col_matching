<!-- {"case_id": "case_collett_g-d-m_b1928", "bio_ids": ["collett_g-d-m_b1928"], "stint_ids": ["Collett, G. D. M___Bahamas___1964"]} -->
# Dossier case_collett_g-d-m_b1928

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `collett_g-d-m_b1928`

- Printed name: **COLLETT, G. D. M**
- Birth year: 1928 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L14368.v` — printed in editions [1965, 1966]:**

> COLLETT, G. D. M.—b. 1928; ed. Cheltenham and Trinity Coll., Oxford; barrister-at-law, Middle Temple; mil. serv., 1948–50, R.A.F., flying offrr.; cr. coun., Nyas., 1953–60; solr. gen., Bah., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953–1960 | cr. coun., Nyas | — | [1965, 1966] |
| 1 | 1963 | solr. gen. | Bahamas | [1965, 1966] |

## Candidate stint `Collett, G. D. M___Bahamas___1964`

- Staff-list name: **Collett, G. D. M** | colony: **Bahamas** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | G. D. M. Collett | Solicitor-General | Civil Establishment | — | — |
| 1965 | G. D. M. Collett | Solicitor-General | Civil Establishment | — | — |
| 1966 | G. D. M. Collett | Solicitor-General | Law Officers | — | — |

### Deterministic checks: `collett_g-d-m_b1928` vs `Collett, G. D. M___Bahamas___1964`

- [PASS] surname_gate: bio 'COLLETT' vs stint 'Collett, G. D. M' (exact)
- [PASS] initials: bio ['G', 'D', 'M'] ~ stint ['G', 'D', 'M']
- [PASS] age_gate: stint starts 1964, birth 1928 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1964-1966
- [FAIL] position_sim: best 33 vs bar 60: 'solr. gen.' ~ 'Solicitor-General'
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

