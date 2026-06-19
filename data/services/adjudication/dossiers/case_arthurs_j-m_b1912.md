<!-- {"case_id": "case_arthurs_j-m_b1912", "bio_ids": ["arthurs_j-m_b1912"], "stint_ids": ["Arthur, John___Straits Settlements___1933"]} -->
# Dossier case_arthurs_j-m_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Arthur, John___Straits Settlements___1933` is also gate-compatible with biography(ies) outside this case: ['arthur_james-startin-wills_b1881'] (already linked elsewhere or filtered).

## Biography `arthurs_j-m_b1912`

- Printed name: **ARTHURS, J. M**
- Birth year: 1912 (attested in editions [1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1959-L20275.v` — printed in editions [1959, 1960, 1961, 1962, 1963]:**

> ARTHURS, J. M.—b. 1912; ed. Christian Bros. Sch., Omagh, and Dublin Univ.; agric. instr., Nig., 1948; Uga., 1956; prin., Arapai farm inst., 1957-62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | agric. instr. | Nigeria | [1959, 1960, 1961, 1962, 1963] |
| 1 | 1956 | agric. instr. | Uganda | [1959, 1960, 1961, 1962, 1963] |
| 2 | 1957–1962 | prin., Arapai farm inst | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Arthur, John___Straits Settlements___1933`

- Staff-list name: **Arthur, John** | colony: **Straits Settlements** | listed 1933–1936 | editions [1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. S. W. Arthur | Secretary of Postal Affairs | MALAYAN CIVIL SERVICE (CADET SERVICE) | — | — |
| 1933 | J. S. W. Arthur | Secretary for Postal Affairs, S.S. and F.M.S. | Post Office | — | — |
| 1936 | J. S. W. Arthur | Director General of Posts and Tels., Malaya | Class I, Grade A | — | — |

### Deterministic checks: `arthurs_j-m_b1912` vs `Arthur, John___Straits Settlements___1933`

- [PASS] surname_gate: bio 'ARTHURS' vs stint 'Arthur, John' (fuzzy:1)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J']
- [PASS] age_gate: stint starts 1933, birth 1912 (age 21)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1936
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

