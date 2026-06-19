<!-- {"case_id": "case_buckeridge_f-h_b1899", "bio_ids": ["buckeridge_f-h_b1899"], "stint_ids": ["Buckeridge, F. H___Mauritius___1950"]} -->
# Dossier case_buckeridge_f-h_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `buckeridge_f-h_b1899`

- Printed name: **BUCKERIDGE, F. H**
- Birth year: 1899 (attested in editions [1953, 1954, 1955])
- Honours: M.B.E
- Appears in editions: [1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1953-L16729.v` — printed in editions [1953, 1954, 1955]:**

> BUCKERIDGE, F. H., M.B.E.—b. 1899; ed. private schs.; mil. serv., 1915-19; G.P.O., London, 1921; Nig., 1925-28; G.P.O., London, 1928-38; Tang., 1938-47; Pal., 1947-48; C.O., 1949; P.M.G., Maur., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | G.P.O., London | — | [1953, 1954, 1955] |
| 1 | 1925–1928 | G.P.O., London | Nigeria | [1953, 1954, 1955] |
| 2 | 1928–1938 | G.P.O., London | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955] |
| 3 | 1938–1947 | G.P.O., London | Tanganyika | [1953, 1954, 1955] |
| 4 | 1947–1948 | G.P.O., London | Palestine | [1953, 1954, 1955] |
| 5 | 1949 | G.P.O., London | Colonial Office | [1953, 1954, 1955] |
| 6 | 1949 | P.M.G. | Mauritius | [1953, 1954, 1955] |

## Candidate stint `Buckeridge, F. H___Mauritius___1950`

- Staff-list name: **Buckeridge, F. H** | colony: **Mauritius** | listed 1950–1954 | editions [1950, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | F. H. Buckeridge | Postmaster-General | Posts and Telegraphs | — | — |
| 1952 | F. H. Buckeridge | Postmaster-General | Civil Establishment | — | — |
| 1953 | F. H. Buckeridge | Postmaster-General | Civil Establishment | — | — |
| 1954 | F. H. Buckeridge | Postmaster-General | Civil Establishment | — | — |

### Deterministic checks: `buckeridge_f-h_b1899` vs `Buckeridge, F. H___Mauritius___1950`

- [PASS] surname_gate: bio 'BUCKERIDGE' vs stint 'Buckeridge, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1950, birth 1899 (age 51)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1954
- [FAIL] position_sim: best 30 vs bar 60: 'P.M.G.' ~ 'Postmaster-General'
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

