<!-- {"case_id": "case_bickerstaff_william-stanley_b1909", "bio_ids": ["bickerstaff_william-stanley_b1909"], "stint_ids": ["Bickerstaff, W. S___Gold Coast___1949"]} -->
# Dossier case_bickerstaff_william-stanley_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bickerstaff_william-stanley_b1909`

- Printed name: **BICKERSTAFF, William Stanley**
- Birth year: 1909 (attested in editions [1948, 1949, 1950, 1951, 1954, 1955])
- Honours: A.M.I.C.E
- Appears in editions: [1948, 1949, 1950, 1951, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L31183.v` — printed in editions [1948, 1949, 1950, 1951, 1954, 1955]:**

> BICKERSTAFF, William Stanley, M.Eng. (Liv.), A.M.I.C.E.—b. 1909; ed. Cowley Sec. Sch., St. Helens, Lancs. and Liverpool Univ., 1st cl. hons. civ. engnr., degree of B.Eng.; exec. engnr., P.W.D., Nig., 1936; prin., gov. tech. sch., G.C., 1948; asst. dir., educ. (tech.), 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | exec. engnr., P.W.D. | Nigeria | [1948, 1949, 1950, 1951, 1954, 1955] |
| 1 | 1948 | prin., gov. tech. sch. | Gold Coast | [1948, 1949, 1950, 1951, 1954, 1955] |

## Candidate stint `Bickerstaff, W. S___Gold Coast___1949`

- Staff-list name: **Bickerstaff, W. S** | colony: **Gold Coast** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. S. Bickerstaff | Assistant Director of Education | Education | — | — |
| 1950 | W. S. Bickerstaff | Assistant Directors of Education | Education | — | — |

### Deterministic checks: `bickerstaff_william-stanley_b1909` vs `Bickerstaff, W. S___Gold Coast___1949`

- [PASS] surname_gate: bio 'BICKERSTAFF' vs stint 'Bickerstaff, W. S' (exact)
- [PASS] initials: bio ['W', 'S'] ~ stint ['W', 'S']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 29 vs bar 60: 'prin., gov. tech. sch.' ~ 'Assistant Director of Education'
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

