<!-- {"case_id": "case_heynes_william-henry_b1903", "bio_ids": ["heynes_william-henry_b1903"], "stint_ids": ["Heynes, W. H___Gold Coast___1934"]} -->
# Dossier case_heynes_william-henry_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heynes_william-henry_b1903`

- Printed name: **HEYNES, William Henry**
- Birth year: 1903 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L33312.v` — printed in editions [1948, 1949, 1950]:**

> HEYNES, William Henry.—b. 1903; lab. asst., vet. dept., Nig., 1927; trans. to G.C., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | lab. asst., vet. dept. | Nigeria | [1948, 1949, 1950] |
| 1 | 1932 | trans. to G.C | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Heynes, W. H___Gold Coast___1934`

- Staff-list name: **Heynes, W. H** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | W. H. Heynes | Laboratory Assistant | Animal Health Department | — | — |
| 1936 | W. H. Heynes | Laboratory Assistant | Animal Health Department | — | — |

### Deterministic checks: `heynes_william-henry_b1903` vs `Heynes, W. H___Gold Coast___1934`

- [PASS] surname_gate: bio 'HEYNES' vs stint 'Heynes, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1934, birth 1903 (age 31)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1936
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

