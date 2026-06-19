<!-- {"case_id": "case_daunt_achilles_b1894", "bio_ids": ["daunt_achilles_b1894"], "stint_ids": ["Daunt, A___Trinidad and Tobago___1922"]} -->
# Dossier case_daunt_achilles_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['daunt_achilles_b1894'] carry a single initial only — the namesake trap applies.

## Biography `daunt_achilles_b1894`

- Printed name: **DAUNT, Achilles**
- Birth year: 1894 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32111.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DAUNT, Achilles, M.A. (Oxon.)—b. 1894; ed. Marlborough Coll. and Trinity Coll., Oxford; on mil. serv. 1914–19, capt.; master, Queen's Royal Coll., Trin., 1920; senr. master, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | master, Queen's Royal Coll. | Trinidad | [1948, 1949, 1950, 1951] |
| 1 | 1938 | senr. master | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Daunt, A___Trinidad and Tobago___1922`

- Staff-list name: **Daunt, A** | colony: **Trinidad and Tobago** | listed 1922–1940 | editions [1922, 1923, 1925, 1927, 1928, 1929, 1931, 1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. Daunt | 6th Assistant Master | Queen's Royal College | — | — |
| 1923 | A. Daunt | 4th | Queen's Royal College | — | — |
| 1925 | A. Daunt | Asst. Master | Queen's Royal College | — | — |
| 1927 | A. Daunt | 4th | Queen's Royal College | — | — |
| 1928 | A. Daunt | Asst. Masters | Queen's Royal College | — | — |
| 1929 | A. Daunt | Assistant Master | Queen's Royal College | — | — |
| 1931 | A. Daunt | Asst. Masters | Queen's Royal College | — | — |
| 1933 | A. Daunt | Asst. Master | Queen's Royal College | — | — |
| 1934 | A. Daunt | Asst. Masters | Queen's Royal College | — | — |
| 1937 | A. Daunt | Assistant Master | Queen's Royal College | — | — |
| 1939 | A. Daunt | 2nd Master | Queen's Royal College | — | — |
| 1940 | A. Daunt | Senior Master | Queen's Royal College | — | — |

### Deterministic checks: `daunt_achilles_b1894` vs `Daunt, A___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'DAUNT' vs stint 'Daunt, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1922, birth 1894 (age 28)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1940
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

