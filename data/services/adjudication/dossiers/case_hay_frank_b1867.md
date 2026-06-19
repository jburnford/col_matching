<!-- {"case_id": "case_hay_frank_b1867", "bio_ids": ["hay_frank_b1867"], "stint_ids": ["Hay, F___New Zealand___1912"]} -->
# Dossier case_hay_frank_b1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hay_frank_b1867'] carry a single initial only — the namesake trap applies.

## Biography `hay_frank_b1867`

- Printed name: **HAY, FRANK**
- Birth year: 1867 (attested in editions [1923, 1924, 1925])
- Honours: M.B
- Appears in editions: [1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1923-L55104.v` — printed in editions [1923, 1924, 1925]:**

> HAY, FRANK, M.B., C.M. (Aberdeen).—B. 1867; ed. privately; dep. insprn.-gen., mental hosps., N.Z., 1904; insprn.-gen., 1907; mem., prisons bd. and nat. prov. fund bd.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | dep. insprn.-gen., mental hosps. | New Zealand | [1923, 1924, 1925] |
| 1 | 1907 | insprn.-gen | New Zealand *(inherited from previous clause)* | [1923, 1924, 1925] |

## Candidate stint `Hay, F___New Zealand___1912`

- Staff-list name: **Hay, F** | colony: **New Zealand** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. Hay | Inspector of Prisons | DEPARTMENT OF JUSTICE AND PATENT OFFICE | — | — |
| 1912 | F. Hay | Inspector-General | Mental Hospitals | — | — |
| 1913 | F. Hay | Inspector of Prisons | Department of Justice and Patent Office | — | — |
| 1913 | F. Hay | Inspector-General | MENTAL HOSPITALS | — | — |
| 1914 | F. Hay | Inspector-General | Mental Hospitals. | — | — |
| 1915 | F. Hay | Inspector-General | Mental Hospitals | — | — |
| 1917 | F. Hay | Inspector-General | Mental Hospitals | — | — |
| 1918 | F. Hay | Inspector-General | Mental Hospitals | — | — |
| 1920 | F. Hay | Inspector-General | Mental Hospitals | — | — |
| 1922 | F. Hay | Inspector-General | Mental Hospitals | — | — |

### Deterministic checks: `hay_frank_b1867` vs `Hay, F___New Zealand___1912`

- [PASS] surname_gate: bio 'HAY' vs stint 'Hay, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1912, birth 1867 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1922
- [PASS] position_sim: best 64 vs bar 60: 'insprn.-gen' ~ 'Inspector-General'
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

