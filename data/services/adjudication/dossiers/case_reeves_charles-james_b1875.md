<!-- {"case_id": "case_reeves_charles-james_b1875", "bio_ids": ["reeves_charles-james_b1875"], "stint_ids": ["Reeves, Conrad___Western Australia___1896", "Reeves, Conrad___Windward Islands___1890"]} -->
# Dossier case_reeves_charles-james_b1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Reeves, Conrad___Western Australia___1896` is also gate-compatible with biography(ies) outside this case: ['reeves_william-conrad_e1863'] (already linked elsewhere or filtered).
- NOTE: stint `Reeves, Conrad___Windward Islands___1890` is also gate-compatible with biography(ies) outside this case: ['reeves_william-conrad_e1863'] (already linked elsewhere or filtered).

## Biography `reeves_charles-james_b1875`

- Printed name: **REEVES, CHARLES JAMES**
- Birth year: 1875 (attested in editions [1935, 1936, 1937])
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `dol1935-L61689.v` — printed in editions [1935, 1936, 1937]:**

> REEVES, CHARLES JAMES.—B. 1875; entd. office consulting engrns. to W. African govt. rlys., 1895; apptd. to Crown Agents office, 1911; asst. head, appts. dept., 1919; dep. head, do., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | entd. office consulting engrns. to W. African govt. rlys | — | [1935, 1936, 1937] |
| 1 | 1911 | apptd. to Crown Agents office | — | [1935, 1936, 1937] |
| 2 | 1919 | asst. head, appts. dept | — | [1935, 1936, 1937] |
| 3 | 1933 | dep. head | Dominions Office | [1935, 1936, 1937] |

## Candidate stint `Reeves, Conrad___Western Australia___1896`

- Staff-list name: **Reeves, Conrad** | colony: **Western Australia** | listed 1896–1898 | editions [1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | Sir Conrad Reeves | Chief Justice | Court of Appeal | — | — |
| 1897 | Sir Conrad Reeves | Justice | Court of Appeal | — | — |
| 1898 | Sir Conrad Reeves | Chief Justice | Court of Appeal | — | — |

### Deterministic checks: `reeves_charles-james_b1875` vs `Reeves, Conrad___Western Australia___1896`

- [PASS] surname_gate: bio 'REEVES' vs stint 'Reeves, Conrad' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C']
- [PASS] age_gate: stint starts 1896, birth 1875 (age 21)
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Reeves, Conrad___Windward Islands___1890`

- Staff-list name: **Reeves, Conrad** | colony: **Windward Islands** | listed 1890–1900 | editions [1890, 1894, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | Sir Conrad Reeves | Chief Justice | Court of Appeal | — | — |
| 1894 | Sir Conrad Reeves | Chief Justice | — | — | — |
| 1899 | Sir Conrad Reeves | Chief Justice | Court of Appeal | — | — |
| 1900 | Sir Conrad Reeves | Chief Justice | Court of Appeal | — | — |

### Deterministic checks: `reeves_charles-james_b1875` vs `Reeves, Conrad___Windward Islands___1890`

- [PASS] surname_gate: bio 'REEVES' vs stint 'Reeves, Conrad' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C']
- [PASS] age_gate: stint starts 1890, birth 1875 (age 15)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1900
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

