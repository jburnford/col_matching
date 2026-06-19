<!-- {"case_id": "case_mahabir_jules_b1891", "bio_ids": ["mahabir_jules_b1891"], "stint_ids": ["Mahabir, J___Trinidad and Tobago___1937"]} -->
# Dossier case_mahabir_jules_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mahabir_jules_b1891'] carry a single initial only — the namesake trap applies.

## Biography `mahabir_jules_b1891`

- Printed name: **MAHABIR, JULES**
- Birth year: 1891 (attested in editions [1935, 1936, 1937, 1940])
- Appears in editions: [1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L60642.v` — printed in editions [1935, 1936, 1937, 1940]:**

> MAHABIR, JULES.—B. 1891; called to bar, Gray's Inn, July, 1916; mag., St. Patrick, Trinidad, Mar., 1934; do., Caroni, Nov., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | called to bar, Gray's Inn | — | [1935, 1936, 1937, 1940] |
| 1 | 1934 | mag., St. Patrick | Trinidad | [1935, 1936, 1937, 1940] |
| 2 | 1938 | do., Caroni | Trinidad *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |

## Candidate stint `Mahabir, J___Trinidad and Tobago___1937`

- Staff-list name: **Mahabir, J** | colony: **Trinidad and Tobago** | listed 1937–1949 | editions [1937, 1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | J. Mahabir | County St. Patrick | Magistrates | — | — |
| 1939 | J. Mahabir | County St. Patrick | Magistrates | — | — |
| 1940 | J. Mahabir | Magistrate | Magistracy | — | — |
| 1949 | J. Mahabir | Magistrates | Judicial | — | — |

### Deterministic checks: `mahabir_jules_b1891` vs `Mahabir, J___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'MAHABIR' vs stint 'Mahabir, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1937, birth 1891 (age 46)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1949
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

