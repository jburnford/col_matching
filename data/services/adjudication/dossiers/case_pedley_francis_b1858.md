<!-- {"case_id": "case_pedley_francis_b1858", "bio_ids": ["pedley_francis_b1858"], "stint_ids": ["Pedley, Francis___Canada___1905"]} -->
# Dossier case_pedley_francis_b1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pedley_francis_b1858'] carry a single initial only — the namesake trap applies.

## Biography `pedley_francis_b1858`

- Printed name: **PEDLEY, FRANCIS**
- Birth year: 1858 (attested in editions [1910, 1911, 1912, 1913])
- Honours: B.A
- Appears in editions: [1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1910-L48020.v` — printed in editions [1910, 1911, 1912, 1913]:**

> PEDLEY, FRANCIS, B.A., Barrister-at-Law.—B. 1858; sup. of immigrtn., Canada, 1897; dep. supt.-gen. of Indian aff airs, 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | sup. of immigrtn. | Canada | [1910, 1911, 1912, 1913] |
| 1 | 1902 | dep. supt.-gen. of Indian aff airs | Canada *(inherited from previous clause)* | [1910, 1911, 1912, 1913] |

## Candidate stint `Pedley, Francis___Canada___1905`

- Staff-list name: **Pedley, Francis** | colony: **Canada** | listed 1905–1913 | editions [1905, 1906, 1907, 1908, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Francis Pedley | Deputy Superintendent-General | Department of Indian Affairs | — | — |
| 1906 | Francis Pedley | Deputy Superintendent-General | Department of Indian Affairs | — | — |
| 1907 | Francis Pedley | Deputy Superintendent-General | Department of Indian Affairs | — | — |
| 1908 | Francis Pedley | Deputy Superintendent-General | DEPARTMENT OF INDIAN AFFAIRS | — | — |
| 1912 | Francis Pedley | Deputy Superintendent-General | Department of Indian Affairs | — | — |
| 1913 | Francis Pedley | Deputy Superintendent-General | Department of Indian Affairs | — | — |

### Deterministic checks: `pedley_francis_b1858` vs `Pedley, Francis___Canada___1905`

- [PASS] surname_gate: bio 'PEDLEY' vs stint 'Pedley, Francis' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1905, birth 1858 (age 47)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1913
- [FAIL] position_sim: best 41 vs bar 60: 'dep. supt.-gen. of Indian aff airs' ~ 'Deputy Superintendent-General'
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

