<!-- {"case_id": "case_peake_harold-gordon_b1890", "bio_ids": ["peake_harold-gordon_b1890"], "stint_ids": ["Peake, H. G___Zanzibar___1934"]} -->
# Dossier case_peake_harold-gordon_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peake_harold-gordon_b1890`

- Printed name: **PEAKE, Harold Gordon**
- Birth year: 1890 (attested in editions [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940])
- Honours: A.C.G.I
- Appears in editions: [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L67271.v` — printed in editions [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940]:**

> PEAKE, Harold Gordon, B.Sc. (hons.), Lond., A.C.G.I., A.M. Inst. C.E.—B. 1890; ed. Eltham Coll. and Imp. Coll. of Science and Tech., London; adm. engrg. staff, Rosyth dockyard, 1912; ast. engrg., P.W.D., F.M.S., 1914; mil. wks. service, India, garrison engrg., Peshawar, 1919; engrg., P.W.D., Nigeria, 1924; senr. exec. engrg., 1928; D.P.W., Zanzibar, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | adm. engrg. staff, Rosyth dockyard | — | [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |
| 1 | 1914 | ast. engrg., P.W.D. | Federated Malay States | [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |
| 2 | 1919 | mil. wks. service, India, garrison engrg., Peshawar | Federated Malay States *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |
| 3 | 1924 | engrg., P.W.D. | Nigeria | [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |
| 4 | 1928 | senr. exec. engrg | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |
| 5 | 1932 | D.P.W. | Zanzibar | [1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |

## Candidate stint `Peake, H. G___Zanzibar___1934`

- Staff-list name: **Peake, H. G** | colony: **Zanzibar** | listed 1934–1940 | editions [1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | H. G. Peake | Director | Electricity and Wireless Branch | — | — |
| 1934 | H. G. Peake | Director of Public Works | Public Works Department | — | — |
| 1936 | H. G. Peake | Director | Public Works, Electricity and Wireless, and Surveys | — | — |
| 1937 | H. G. Peake | Director | Public Works, Electricity and Wireless | — | — |
| 1940 | H. G. Peake | Director | Public Works, Electricity and Wireless | — | — |

### Deterministic checks: `peake_harold-gordon_b1890` vs `Peake, H. G___Zanzibar___1934`

- [PASS] surname_gate: bio 'PEAKE' vs stint 'Peake, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1934, birth 1890 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1940
- [FAIL] position_sim: best 22 vs bar 60: 'D.P.W.' ~ 'Director of Public Works'
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

