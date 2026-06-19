<!-- {"case_id": "case_van-lare_w-b_b1904", "bio_ids": ["van-lare_w-b_b1904"], "stint_ids": ["Van Lare, W. B___Gold Coast___1949"]} -->
# Dossier case_van-lare_w-b_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `van-lare_w-b_b1904`

- Printed name: **VAN LARE, W. B**
- Birth year: 1904 (attested in editions [1955, 1956])
- Appears in editions: [1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1955-L23129.v` — printed in editions [1955, 1956]:**

> VAN LARE, W. B.—b. 1904; ed. Mfantsipim Sch. and Univ. Coll., Lond.; barrister-at-law, Lincoln's Inn; dist. mag., G.C., 1943; puisne judge, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | dist. mag. | Gold Coast | [1955, 1956] |
| 1 | 1952 | puisne judge | Gold Coast *(inherited from previous clause)* | [1955, 1956] |

## Candidate stint `Van Lare, W. B___Gold Coast___1949`

- Staff-list name: **Van Lare, W. B** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. B. Van Lare | District Magistrate | Judicial | — | — |
| 1950 | W. B. Van Lare | District Magistrates | Judicial | — | — |
| 1951 | W. B. Van Lare | District Magistrate | Judicial | — | — |

### Deterministic checks: `van-lare_w-b_b1904` vs `Van Lare, W. B___Gold Coast___1949`

- [PASS] surname_gate: bio 'VAN LARE' vs stint 'Van Lare, W. B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'dist. mag.' ~ 'District Magistrate'
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

