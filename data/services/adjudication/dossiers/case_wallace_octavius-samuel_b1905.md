<!-- {"case_id": "case_wallace_octavius-samuel_b1905", "bio_ids": ["wallace_octavius-samuel_b1905"], "stint_ids": ["Wallace, O. S___Northern Rhodesia___1936"]} -->
# Dossier case_wallace_octavius-samuel_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wallace_octavius-samuel_b1905`

- Printed name: **WALLACE, Octavius Samuel**
- Birth year: 1905 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L28130.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> WALLACE, O. S.—b. 1905; ed. St. Andrew's Coll., St. Stephen's Green Sch. and Trinity Coll., Dublin, and Gonville and Caius Coll., Camb.; barrister-at-law, Middle Temple; cadet, N. Rhod., 1930; D.O., 1932; secon., C.O., 1944-49; senr. D.O., 1953-60.

**Version `col1948-L36640.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WALLACE, Octavius Samuel.—b. 1905; ed. St. Andrew's Coll., St. Stephen's Green Sch., Trinity Coll., Dublin, B.A., Gonville and Caius Coll., Cambridge Univ., B.A. (Cantab.), 1929), Middle Temple; cadet, N. Rhod., 1930; dist. offr., 1932; seconded to C.O., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1932 | cadet | Dominions Office | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1932 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1944–1949 | secon. | Colonial Office | [1957, 1958, 1959, 1960, 1961] |
| 4 | 1944 | seconded to C.O | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 5 | 1953–1960 | senr. D.O | Colonial Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Wallace, O. S___Northern Rhodesia___1936`

- Staff-list name: **Wallace, O. S** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | O. S. Wallace | District Officers | District Administration | — | — |
| 1939 | O. S. Wallace | District Officer | District Administration | — | — |
| 1940 | O. S. Wallace | District Officer | District Administration | — | — |

### Deterministic checks: `wallace_octavius-samuel_b1905` vs `Wallace, O. S___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'WALLACE' vs stint 'Wallace, O. S' (exact)
- [PASS] initials: bio ['O', 'S'] ~ stint ['O', 'S']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 72 vs bar 60: 'dist. offr' ~ 'District Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

