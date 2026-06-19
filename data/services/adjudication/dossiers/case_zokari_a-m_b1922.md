<!-- {"case_id": "case_zokari_a-m_b1922", "bio_ids": ["zokari_a-m_b1922"], "stint_ids": ["Zokari, A. M___Aden___1962"]} -->
# Dossier case_zokari_a-m_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `zokari_a-m_b1922`

- Printed name: **ZOKARI, A. M.**
- Birth year: 1922 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L19169.v` — printed in editions [1966]:**

> ZOKARI, A. M.—b. 1922; clk., Aden, 1946; asst. political offr., 1948; admin. asst., p.r.o., 1956; broadcastg. offr., 1958; pub. rel. offr., 1961. PARLIAMENTARY AND NON-PARLIAMENTARY PAPERS OF COLONIAL INTEREST PUBLISHED DURING 1965 Arranged in three parts: (a) periodicals, (b) by subject, (c) by territories.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946–1946 | clk. | Aden | [1966] |
| 1 | 1948–1948 | asst. political offr. | — | [1966] |
| 2 | 1956–1956 | admin. asst., p.r.o. | — | [1966] |
| 3 | 1958–1958 | broadcastg. offr. | — | [1966] |
| 4 | 1961–1961 | pub. rel. offr. | — | [1966] |

## Candidate stint `Zokari, A. M___Aden___1962`

- Staff-list name: **Zokari, A. M** | colony: **Aden** | listed 1962–1966 | editions [1962, 1963, 1964, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | A. M. Zokari | Public Relations Officer | Civil Establishment | — | — |
| 1963 | A. M. Zokari | Public Relations Officer | Civil Establishment | — | — |
| 1964 | A. M. Zokari | Public Relations Officer | Civil Establishment | — | — |
| 1966 | A. M. Zokari | Public Relations Officer | Civil Establishment | — | — |

### Deterministic checks: `zokari_a-m_b1922` vs `Zokari, A. M___Aden___1962`

- [PASS] surname_gate: bio 'ZOKARI' vs stint 'Zokari, A. M' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1962, birth 1922 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Aden'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1966
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

