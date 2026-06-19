<!-- {"case_id": "case_mcswan_david-morrison_b1895", "bio_ids": ["mcswan_david-morrison_b1895"], "stint_ids": ["McSwan, D. M___Straits Settlements___1931"]} -->
# Dossier case_mcswan_david-morrison_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcswan_david-morrison_b1895`

- Printed name: **McSWAN, DAVID MORRISON**
- Birth year: 1895 (attested in editions [1939, 1940])
- Honours: M.B, M.C
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68874.v` — printed in editions [1939, 1940]:**

> McSWAN, DAVID MORRISON, M.C., M.B., Ch.B., Certif. L.S.T.M.—B. 1895; ed. Kent Rd. High Schl. and Glas. Univ.; med. offr., F.M.S., July, 1925; do., T.T.S., Hosp., S'pore., June, 1931; do., Gen. Hosp., J. Bahru, June, 1932; med. offr. superscale grade B, Sept., 1936; ag. ch. med. offr., S'pore., Feb., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | med. offr. | Federated Malay States | [1939, 1940] |
| 1 | 1931 | do., T.T.S., Hosp., S'pore | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1932 | do., Gen. Hosp., J. Bahru | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1936 | med. offr. superscale grade B | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1937 | ag. ch. med. offr., S'pore | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `McSwan, D. M___Straits Settlements___1931`

- Staff-list name: **McSwan, D. M** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1932, 1933, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | D. M. McSwan | Medical Officer | Medical | — | — |
| 1932 | D. M. McSwan | Medical Officer | Medical | — | — |
| 1933 | D. M. McSwan | Medical Officer | Medical | — | — |
| 1934 | D. M. McSwan | Medical and Health Officer | Singapore | — | — |
| 1939 | D. M. McSwan | Supercase Medical Officer, Grade B. | Medical | — | — |

### Deterministic checks: `mcswan_david-morrison_b1895` vs `McSwan, D. M___Straits Settlements___1931`

- [PASS] surname_gate: bio 'McSWAN' vs stint 'McSwan, D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1931, birth 1895 (age 36)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1939
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

