<!-- {"case_id": "case_hopkins_terence-francis-gethin_b1902", "bio_ids": ["hopkins_terence-francis-gethin_b1902"], "stint_ids": ["Hopkins, T. F. G___Gambia___1936"]} -->
# Dossier case_hopkins_terence-francis-gethin_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hopkins, T. F. G___Gambia___1936` is also gate-compatible with biography(ies) outside this case: ['hopkins_francis-gethin_e1894'] (already linked elsewhere or filtered).

## Biography `hopkins_terence-francis-gethin_b1902`

- Printed name: **HOPKINS, Terence Francis Gethin**
- Birth year: 1902 (attested in editions [1957, 1958, 1959])
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L24192.v` — printed in editions [1957, 1958, 1959]:**

> HOPKINS, T. F. G.—b. 1902; ed. Epsom Coll. and R.M.C., Sandhurst; comsmd. Gloucs. regt., 1922; secon. G.C. regt., R.W.A.F.F., 1926–29; admin. cadet, Nig., 1930; secon. Gam., 1935–39; senr. D.O., 1949; resdt., N. Nig., 1955–58.

**Version `col1948-L33448.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOPKINS, Terence Francis Gethin.—b. 1902; ed. Epsom Coll. and R.M.C., Sandhurst; on mil. serv. from 1922; G.C. Regt., 1926; cadet, Nig., 1930; admin. offr., cl. III; cl. II, 1949; seconded to Gam., 1935-40.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | comsmd. Gloucs. regt | — | [1957, 1958, 1959] |
| 1 | 1926–1929 | secon. G.C. regt., R.W.A.F.F | Gold Coast | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 2 | 1930 | admin. cadet | Nigeria | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 3 | 1935–1939 | secon. Gam | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 4 | 1949 | senr. D.O | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 5 | 1955–1958 | resdt. | Northern Nigeria | [1957, 1958, 1959] |

## Candidate stint `Hopkins, T. F. G___Gambia___1936`

- Staff-list name: **Hopkins, T. F. G** | colony: **Gambia** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | T. F. G. Hopkins | Commissioners and Assistant Commissioners | Provincial Administration | — | — |
| 1937 | T. F. G. Hopkins | Commissioner | Provincial Administration | — | — |
| 1939 | T. F. G. Hopkins | Commissioners and Assistant Commissioners | Provincial Administration | — | — |

### Deterministic checks: `hopkins_terence-francis-gethin_b1902` vs `Hopkins, T. F. G___Gambia___1936`

- [PASS] surname_gate: bio 'HOPKINS' vs stint 'Hopkins, T. F. G' (exact)
- [PASS] initials: bio ['T', 'F', 'G'] ~ stint ['T', 'F', 'G']
- [PASS] age_gate: stint starts 1936, birth 1902 (age 34)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

