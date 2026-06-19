<!-- {"case_id": "case_dundas_james_b1907", "bio_ids": ["dundas_james_b1907"], "stint_ids": ["Dundas, J___Nigeria___1934"]} -->
# Dossier case_dundas_james_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dundas_james_b1907'] carry a single initial only — the namesake trap applies.

## Biography `dundas_james_b1907`

- Printed name: **DUNDAS, James**
- Birth year: 1907 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L31747.v` — printed in editions [1949, 1950, 1951]:**

> DUNDAS, James, B.Sc. (for.).—b. 1907; ed. George Watson's Coll. and Edin., and Oxford Univs.; asst. consvtr., forests, Nig., 1929; mem., Anglo-French for. comsnn., 1936-7 and part author of report; author of numerous papers on forestry matters.

**Version `col1948-L32343.v` — printed in editions [1948]:**

> DUNDAS, James, B.Sc. (for.).—b. 1907; ed. George Watson's Coll., Edinburgh, and Oxford Univs.; asst. consvtr. of forests, Nig., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929–1929 | asst. consvtr., forests | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1936–1937 | mem., Anglo-French for. comsnn. | — | [1949, 1950, 1951] |

## Candidate stint `Dundas, J___Nigeria___1934`

- Staff-list name: **Dundas, J** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | J. Dundas | Conservators and Assistant Conservators | Forestry | — | — |
| 1939 | J. Dundas | Senior Assistant Conservators and Assistant Conservators of Forests | Forestry | — | — |

### Deterministic checks: `dundas_james_b1907` vs `Dundas, J___Nigeria___1934`

- [PASS] surname_gate: bio 'DUNDAS' vs stint 'Dundas, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1934, birth 1907 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

