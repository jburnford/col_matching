<!-- {"case_id": "case_law_chung-hung_b1913", "bio_ids": ["law_chung-hung_b1913"], "stint_ids": ["Law, C. E___Zanzibar___1936"]} -->
# Dossier case_law_chung-hung_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['law_chung-hung_b1913'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Law, C. E___Zanzibar___1936` is also gate-compatible with biography(ies) outside this case: ['law_charles-ewan_b1884'] (already linked elsewhere or filtered).

## Biography `law_chung-hung_b1913`

- Printed name: **LAW, Chung-hung**
- Birth year: 1913 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L18978.v` — printed in editions [1964, 1965, 1966]:**

> LAW, Chung-hung.—b. 1913; ed. King's Coll., Univ. H.K.; master, H.K., 1939; educ. offr., 1952; senr. educ. offr., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | master | Hong Kong | [1964, 1965, 1966] |
| 1 | 1962 | senr. educ. offr | Hong Kong *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Law, C. E___Zanzibar___1936`

- Staff-list name: **Law, C. E** | colony: **Zanzibar** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | C. E. Law | Chief Justice | Judicial Department | — | — |
| 1937 | C. E. Law | Chief Justice | Judicial Department | — | — |

### Deterministic checks: `law_chung-hung_b1913` vs `Law, C. E___Zanzibar___1936`

- [PASS] surname_gate: bio 'LAW' vs stint 'Law, C. E' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1936, birth 1913 (age 23)
- [FAIL] colony: no placed event resolves to 'Zanzibar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1937
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

