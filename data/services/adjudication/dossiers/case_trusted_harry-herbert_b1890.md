<!-- {"case_id": "case_trusted_harry-herbert_b1890", "bio_ids": ["trusted_harry-herbert_b1890"], "stint_ids": ["Trusted, Harry H___Leeward Islands___1927", "Trusted, Harry___Palestine___1932"]} -->
# Dossier case_trusted_harry-herbert_b1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Trusted, Harry H___Leeward Islands___1927` is also gate-compatible with biography(ies) outside this case: ['trusted_harry-herbert_b1888'] (already linked elsewhere or filtered).
- NOTE: stint `Trusted, Harry___Palestine___1932` is also gate-compatible with biography(ies) outside this case: ['trusted_harry-herbert_b1888'] (already linked elsewhere or filtered).

## Biography `trusted_harry-herbert_b1890`

- Printed name: **TRUSTED, HARRY HERBERT**
- Birth year: 1890 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L65396.v` — printed in editions [1937]:**

> TRUSTED, HARRY HERBERT.—B., 1890; ed. Ellesmere Coll. and Tri. Hall; to bar, Inner Temple, 1913; (Duke of Cornwall's L.I. and staff, 1914-19; puisne judge, Leeward gen., 1927; commnr. to revise laws, Leeward Is., 1928; R.C., Leeward atty.-gen., Cyprus, Dec., 1929; advisory staff, C.O., Aug., Palestine, 1932; ch. just., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | to bar, Inner Temple | — | [1937] |
| 1 | 1914–1919 | (Duke of Cornwall's L.I. and staff | — | [1937] |
| 2 | 1927 | puisne judge, Leeward gen | — | [1937] |
| 3 | 1928 | commnr. to revise laws, Leeward Is | — | [1937] |
| 4 | 1929 | R.C., Leeward atty.-gen. | Cyprus | [1937] |
| 5 | 1932 | advisory staff, C.O., Aug. | Palestine | [1937] |
| 6 | 1936 | ch. just | Palestine *(inherited from previous clause)* | [1937] |

## Candidate stint `Trusted, Harry H___Leeward Islands___1927`

- Staff-list name: **Trusted, Harry H** | colony: **Leeward Islands** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | H. H. Trusted | 2nd Puisne Judge | Judicial Establishment | — | — |
| 1927 | Harry H. Trusted | 2nd Puisne Judge | Judicial and Legal | — | — |
| 1928 | H. H. Trusted | Attorney-General | Judicial Establishment | — | — |
| 1928 | H. H. Trusted | Attorney-General | Legislative Council (Local) | — | — |
| 1928 | H. H. Trusted | Chairman | Public Library | — | — |
| 1928 | H. H. Trusted | Attorney-General | Official Members | — | — |
| 1929 | H. H. Trusted | Attorney-General | Judicial Establishment | — | — |
| 1930 | H. H. Trusted | Attorney-General | Judicial Establishment | — | — |
| 1930 | H. H. Trusted | Attorney-General | Legislative Council (Local) | — | — |

### Deterministic checks: `trusted_harry-herbert_b1890` vs `Trusted, Harry H___Leeward Islands___1927`

- [PASS] surname_gate: bio 'TRUSTED' vs stint 'Trusted, Harry H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1927, birth 1890 (age 37)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Trusted, Harry___Palestine___1932`

- Staff-list name: **Trusted, Harry** | colony: **Palestine** | listed 1932–1940 | editions [1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | H. H. Trusted | Attorney General | Legal Department | — | — |
| 1940 | Sir Harry Trusted | Chief Justice | Supreme Court | — | — |

### Deterministic checks: `trusted_harry-herbert_b1890` vs `Trusted, Harry___Palestine___1932`

- [PASS] surname_gate: bio 'TRUSTED' vs stint 'Trusted, Harry' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1932, birth 1890 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1932-1940
- [PASS] position_sim: best 70 vs bar 60: 'ch. just' ~ 'Chief Justice'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

