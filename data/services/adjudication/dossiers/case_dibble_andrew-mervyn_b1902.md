<!-- {"case_id": "case_dibble_andrew-mervyn_b1902", "bio_ids": ["dibble_andrew-mervyn_b1902"], "stint_ids": ["Dibble, A. M___Northern Rhodesia___1937"]} -->
# Dossier case_dibble_andrew-mervyn_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dibble_andrew-mervyn_b1902`

- Printed name: **DIBBLE, Andrew Mervyn**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951])
- Honours: A.M.I.C.E, M.B.E
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32228.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DIBBLE, Andrew Mervyn, M.B.E., B.Sc., A.M.I.C.E., Assoc.M.N.Z.Soc.E.—b. 1902; ed. Auckland Univ. Coll., N.Z.; apptd. Fiji, 1929; trans. to Tonga, 1934; ch. engrn., African housing dept., N. Rhod., 1936; D.P.W., Aden, 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | apptd. Fiji | — | [1948, 1949, 1950, 1951] |
| 1 | 1934 | trans. to Tonga | — | [1948, 1949, 1950, 1951] |
| 2 | 1936 | ch. engrn., African housing dept. | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 3 | 1950 | D.P.W. | Aden | [1948, 1949, 1950, 1951] |

## Candidate stint `Dibble, A. M___Northern Rhodesia___1937`

- Staff-list name: **Dibble, A. M** | colony: **Northern Rhodesia** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | A. M. Dibble | Assistant Engineer | Public Works Department | — | — |
| 1939 | A. M. Dibble | Assistant Engineer | Public Works Department | — | — |
| 1940 | A. M. Dibble | Assistant Engineer | Public Works Department | — | — |

### Deterministic checks: `dibble_andrew-mervyn_b1902` vs `Dibble, A. M___Northern Rhodesia___1937`

- [PASS] surname_gate: bio 'DIBBLE' vs stint 'Dibble, A. M' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1937, birth 1902 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 47 vs bar 60: 'ch. engrn., African housing dept.' ~ 'Assistant Engineer'
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

