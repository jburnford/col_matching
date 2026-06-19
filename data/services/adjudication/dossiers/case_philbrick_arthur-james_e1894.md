<!-- {"case_id": "case_philbrick_arthur-james_e1894", "bio_ids": ["philbrick_arthur-james_e1894"], "stint_ids": ["Philbrick, A. J___Gold Coast___1905"]} -->
# Dossier case_philbrick_arthur-james_e1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Philbrick, A. J___Gold Coast___1905` is also gate-compatible with biography(ies) outside this case: ['philbrick_arthur-james_e1889'] (already linked elsewhere or filtered).

## Biography `philbrick_arthur-james_e1894`

- Printed name: **PHILBRICK, ARTHUR JAMES**
- Birth year: not printed
- Appears in editions: [1914]

### Verbatim printed entry text (OCR)

**Version `col1914-L49159.v` — printed in editions [1914]:**

> PHILBRICK, ARTHUR JAMES.—Ed. Weymouth Coll. and Queen's Coll., Oxford; local auditor, Niger Coast Prot., 27th Oct., 1894; astt. auditor, E. Africa Prot., 9th Dec., 1896; local auditor, Uganda, 29th Apr., 1897; served in Uganda mutiny (medal and clasp); local auditor, E. Africa and Uganda rly., 26th Dec., 1901; auditor, Hong Kong, 1st Nov., 1904; J.P., 1905; hon. auditor, Hong Kong Univ., 2nd May, 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | local auditor, Niger Coast Prot | — | [1914] |
| 1 | 1896 | astt. auditor, E. Africa Prot | — | [1914] |
| 2 | 1897 | local auditor | Uganda | [1914] |
| 3 | 1901 | local auditor, E. Africa and Uganda rly | Uganda *(inherited from previous clause)* | [1914] |
| 4 | 1904 | auditor | Hong Kong | [1914] |
| 5 | 1905 | J.P | Hong Kong *(inherited from previous clause)* | [1914] |
| 6 | 1911 | hon. auditor, Hong Kong Univ | Hong Kong | [1914] |

## Candidate stint `Philbrick, A. J___Gold Coast___1905`

- Staff-list name: **Philbrick, A. J** | colony: **Gold Coast** | listed 1905–1923 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. J. Philbrick | Provincial Commissioner | Judicial Department | — | — |
| 1906 | A. J. Philbrick | Provincial Commissioner | Judicial Department | — | — |
| 1907 | A. J. Philbrick | Provincial Commissioner | Judicial Department | — | — |
| 1908 | A. J. Philbrick | Provincial Commissioner | Judicial Department | — | — |
| 1909 | A. J. Philbrick | Provincial Commissioners | Judicial Department | — | — |
| 1910 | A. J. Philbrick | Provincial Commissioner | Judicial Department | — | — |
| 1912 | A. J. Philbrick | Provincial Commissioner | ASHANTI | — | — |
| 1913 | A. J. Philbrick | Provincial Commissioner | ASHANTI | — | — |
| 1914 | A. J. Philbrick | Provincial Commissioner | ASHANTI | — | — |
| 1915 | A. J. Philbrick | Provincial Commissioner | ASHANTI | — | — |
| 1917 | A. J. Philbrick | Provincial Commissioner | Administrative and Political Department | — | — |
| 1918 | A. J. Philbrick | Provincial Commissioner | Administrative and Political Department | — | — |
| 1919 | A. J. Philbrick | Provincial Commissioner | Administrative and Political Department | — | — |
| 1922 | A. J. Philbrick | Chief Commissioner, Northern Territories | Administrative and Political Department | — | — |
| 1923 | A. J. Philbrick | Chief Commissioner, Northern Territories | Administrative and Political Department | — | — |

### Deterministic checks: `philbrick_arthur-james_e1894` vs `Philbrick, A. J___Gold Coast___1905`

- [PASS] surname_gate: bio 'PHILBRICK' vs stint 'Philbrick, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1923
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

