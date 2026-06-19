<!-- {"case_id": "case_dobbin_james-hamilton_b1896", "bio_ids": ["dobbin_james-hamilton_b1896"], "stint_ids": ["Dobbin, J. H___Gold Coast___1934"]} -->
# Dossier case_dobbin_james-hamilton_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dobbin_james-hamilton_b1896`

- Printed name: **DOBBIN, James Hamilton**
- Birth year: 1896 (attested in editions [1948, 1949, 1950, 1951])
- Honours: D.P.H, L.R.C.P
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32256.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DOBBIN, James Hamilton, L.R.C.P., L.R.C.S. (Edin.), L.R.F.P.S. (Glas.), D.T.M. & H. (Liv.), D.P.H.—b. 1896; L.S.H.T.M. cert. (distinct.); on mil. serv., 1914–19 and 1939–40, capt.; med. offr., G.C., 1928; M.O.H., 1928; asst. D.M.S., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | med. offr. | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1946 | asst. D.M.S | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Dobbin, J. H___Gold Coast___1934`

- Staff-list name: **Dobbin, J. H** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | J. H. Dobbin | Medical Officers of Health | Health Branch | — | — |
| 1936 | J. H. Dobbin | Medical Officers of Health | Health Branch | — | — |

### Deterministic checks: `dobbin_james-hamilton_b1896` vs `Dobbin, J. H___Gold Coast___1934`

- [PASS] surname_gate: bio 'DOBBIN' vs stint 'Dobbin, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1934, birth 1896 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 47 vs bar 60: 'med. offr.' ~ 'Medical Officers of Health'
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

