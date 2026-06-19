<!-- {"case_id": "case_manning_t-h_b1904", "bio_ids": ["manning_t-h_b1904"], "stint_ids": ["Manning, T. H___Western Pacific___1951"]} -->
# Dossier case_manning_t-h_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `manning_t-h_b1904`

- Printed name: **MANNING, T. H**
- Birth year: 1904 (attested in editions [1959, 1960, 1961, 1962])
- Honours: I.S.O (1959)
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L25804.v` — printed in editions [1959, 1960, 1961, 1962]:**

> MANNING, T. H., I.S.O. (1959).—b. 1904; ed. Torquay Gram. Sch.; apptd. Fiji, 1937; G.E.I.C., 1938; Fiji, 1941; prot. postmaster, B.S.I.P., 1949; compt., posts and telecoms., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | apptd. Fiji | — | [1959, 1960, 1961, 1962] |
| 1 | 1937 | compt., posts and telecoms | Fiji *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 2 | 1938 | G.E.I.C | — | [1959, 1960, 1961, 1962] |
| 3 | 1941 | G.E.I.C | Fiji | [1959, 1960, 1961, 1962] |
| 4 | 1949 | prot. postmaster, B.S.I.P | Fiji *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |

## Candidate stint `Manning, T. H___Western Pacific___1951`

- Staff-list name: **Manning, T. H** | colony: **Western Pacific** | listed 1951–1962 | editions [1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | T. H. Manning | Postmaster, Grade I | POSTAL | — | — |
| 1952 | T. H. Manning | Postmaster, Grade I | Civil Establishment | — | — |
| 1953 | T. H. Manning | Postmaster | Civil Establishment | — | — |
| 1954 | T. H. Manning | Postmaster | Civil Establishment | — | — |
| 1955 | T. H. Manning | Protectorate Postmaster | Civil Establishment | — | — |
| 1956 | T. H. Manning | Protectorate Postmaster | Civil Establishment | — | — |
| 1957 | T. H. Manning | Protectorate Postmaster | Civil Establishment | — | — |
| 1958 | T. H. Manning | Protectorate Postmaster | Civil Establishment | — | — |
| 1959 | T. H. Manning | Comptroller of Posts and Telecommunications | Civil Establishment | — | — |
| 1960 | T. H. Manning | Comptroller of Posts and Telecommunications | Civil Establishment | — | — |
| 1961 | T. H. Manning | Comptroller of Posts and Telecommunications | Civil Establishment | — | — |
| 1962 | T. H. Manning | Comptroller of Posts and Telecommunications | Civil Establishment | — | — |

### Deterministic checks: `manning_t-h_b1904` vs `Manning, T. H___Western Pacific___1951`

- [PASS] surname_gate: bio 'MANNING' vs stint 'Manning, T. H' (exact)
- [PASS] initials: bio ['T', 'H'] ~ stint ['T', 'H']
- [PASS] age_gate: stint starts 1951, birth 1904 (age 47)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1962
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

