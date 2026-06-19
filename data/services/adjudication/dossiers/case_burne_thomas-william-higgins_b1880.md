<!-- {"case_id": "case_burne_thomas-william-higgins_b1880", "bio_ids": ["burne_thomas-william-higgins_b1880"], "stint_ids": ["Burne, T. W. H___Straits Settlements___1915", "Burne, T. W. H___Straits Settlements___1920"]} -->
# Dossier case_burne_thomas-william-higgins_b1880

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burne_thomas-william-higgins_b1880`

- Printed name: **BURNE, THOMAS WILLIAM HIGGINS**
- Birth year: 1880 (attested in editions [1928, 1929, 1930, 1931, 1932])
- Appears in editions: [1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1928-L64606.v` — printed in editions [1928, 1929, 1930, 1931, 1932]:**

> BURNE, THOMAS WILLIAM HIGGINS.—B. 1880; ed. Malvern Coll. and St. Bartholomew's Hosp. (Univ. of London), M.B., B.S. (Lond.); medl. offr., S.S. Apr., 1914; ag. surg., gen. hosp., Singapore, Nov., 1915; ch. surg., F.M.S., Feb., 1925; senr. surg., Aug., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | medl. offr. | Straits Settlements | [1928, 1929, 1930, 1931, 1932] |
| 1 | 1915 | ag. surg., gen. hosp. | Singapore | [1928, 1929, 1930, 1931, 1932] |
| 2 | 1925 | ch. surg. | Federated Malay States | [1928, 1929, 1930, 1931, 1932] |
| 3 | 1928 | senr. surg | Federated Malay States *(inherited from previous clause)* | [1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Burne, T. W. H___Straits Settlements___1915`

- Staff-list name: **Burne, T. W. H** | colony: **Straits Settlements** | listed 1915–1917 | editions [1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | T. W. Burne | House Surgeons and Assistant Health Officers | Medical | — | — |
| 1917 | T. W. Burne | Medical Officers and Health Officers | Medical | — | — |

### Deterministic checks: `burne_thomas-william-higgins_b1880` vs `Burne, T. W. H___Straits Settlements___1915`

- [PASS] surname_gate: bio 'BURNE' vs stint 'Burne, T. W. H' (exact)
- [PASS] initials: bio ['T', 'W', 'H'] ~ stint ['T', 'W', 'H']
- [PASS] age_gate: stint starts 1915, birth 1880 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1917
- [FAIL] position_sim: best 50 vs bar 60: 'medl. offr.' ~ 'Medical Officers and Health Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Burne, T. W. H___Straits Settlements___1920`

- Staff-list name: **Burne, T. W. H** | colony: **Straits Settlements** | listed 1920–1933 | editions [1920, 1921, 1922, 1923, 1925, 1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | T. W. H. Burne | Medical Officers and Health Officers, Class IV. | Medical | — | — |
| 1921 | T. W. H. Burne | Medical Officers and Health Officers | Medical | — | — |
| 1922 | T. W. H. Burne | Officer seconded to Unfederated States | Medical | — | — |
| 1923 | T. W. H. Burne | Officer seconded to Unfederated States | Medical | — | — |
| 1925 | T. W. H. Burne | Medical Officer (seconded to Unfederated Malay States) | LABUAN | — | — |
| 1931 | T. W. H. Burne | Senior Surgeon | Medical | — | — |
| 1932 | T. W. H. Burne | Senior Surgeon | Medical | — | — |
| 1933 | T. W. H. Burne | Senior Surgeon | Medical | — | — |

### Deterministic checks: `burne_thomas-william-higgins_b1880` vs `Burne, T. W. H___Straits Settlements___1920`

- [PASS] surname_gate: bio 'BURNE' vs stint 'Burne, T. W. H' (exact)
- [PASS] initials: bio ['T', 'W', 'H'] ~ stint ['T', 'W', 'H']
- [PASS] age_gate: stint starts 1920, birth 1880 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1933
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

