<!-- {"case_id": "case_couppiss_theocharis-achillea_b1904", "bio_ids": ["couppiss_theocharis-achillea_b1904"], "stint_ids": ["Couppis, Th. A___Cyprus___1936"]} -->
# Dossier case_couppiss_theocharis-achillea_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `couppiss_theocharis-achillea_b1904`

- Printed name: **COUPPISS, Theocharis Achillea**
- Birth year: 1904 (attested in editions [1948])
- Appears in editions: [1948, 1950, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1948-L31941.v` — printed in editions [1948]:**

> COUPPISS, Theocharis Achillea.—b. 1904; ed. Greek Gymnasium, English Sch., Cyprus, and Univ. of Oxford, B.A. (Oxon); mounted forest guard, Cyp., 1925; forester, 1930; senr. forest ranger, 1932; asst. consvtr., 1934; author of Trees and Their Place in Village Land Use Development, and other papers on land and forestry in Cyprus.

**Version `col1950-L34621.v` — printed in editions [1950]:**

> COUPPIS, Theocharis Achillea.—b. 1904; ed. Greek Gymnasium, English Sch., Cyprus, Oxford Univ., B.A. (Oxon); mounted forest guard, Cyp., 1925; forester, 1930; senr. forest ranger, 1932; asst. constr., 1934; author of Trees and Their Place in Village Land Use Development, and other papers on land and forestry in Cyprus.

**Version `col1958-L21653.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> COUPPIS, T. A.—b. 1904; ed. Cyprus Morhou Gymnasium, English Sch., Nicosia, and Forestry Sch., Oxford Univ.; mil. serv., 1941; apptd. Cyprus, 1924; asst. consvr., forests, 1934; ret., 1950; forest offr., Zanz., 1951; author of sundry pp. on forestry.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | apptd. Cyprus | — | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1925 | mounted forest guard | Cyprus | [1948, 1950] |
| 2 | 1930 | forester | Cyprus *(inherited from previous clause)* | [1948, 1950] |
| 3 | 1932 | senr. forest ranger | Cyprus *(inherited from previous clause)* | [1948, 1950] |
| 4 | 1934 | asst. consvtr | Cyprus *(inherited from previous clause)* | [1948, 1950] |
| 5 | 1934 | asst. consvr., forests | — | [1958, 1959, 1960, 1961, 1962, 1963] |
| 6 | 1950 | ret | — | [1958, 1959, 1960, 1961, 1962, 1963] |
| 7 | 1951 | forest offr. | Zanzibar | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Couppis, Th. A___Cyprus___1936`

- Staff-list name: **Couppis, Th. A** | colony: **Cyprus** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | Th. A. Couppis | Assistant Conservator of Forests, Second Grade | Forest Department | — | — |
| 1939 | Th. A. Couppis | Assistant Conservator of Forests, 2nd Grade | Forest Department | — | — |

### Deterministic checks: `couppiss_theocharis-achillea_b1904` vs `Couppis, Th. A___Cyprus___1936`

- [PASS] surname_gate: bio 'COUPPISS' vs stint 'Couppis, Th. A' (fuzzy:1)
- [PASS] initials: bio ['T', 'A'] ~ stint ['T', 'A']
- [PASS] age_gate: stint starts 1936, birth 1904 (age 32)
- [PASS] colony: 4 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1939
- [FAIL] position_sim: best 44 vs bar 60: 'asst. consvtr' ~ 'Assistant Conservator of Forests, 2nd Grade'
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

