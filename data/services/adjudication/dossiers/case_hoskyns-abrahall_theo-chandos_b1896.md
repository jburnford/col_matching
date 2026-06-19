<!-- {"case_id": "case_hoskyns-abrahall_theo-chandos_b1896", "bio_ids": ["hoskyns-abrahall_theo-chandos_b1896"], "stint_ids": ["Hoskyns-Abraball, T___Nigeria___1934"]} -->
# Dossier case_hoskyns-abrahall_theo-chandos_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hoskyns-abrahall_theo-chandos_b1896`

- Printed name: **HOSKYNS-ABRAHALL, Theo Chandos**
- Birth year: 1896 (attested in editions [1948, 1949, 1950, 1951])
- Honours: C.M.G (1942), Kt. Bach (1950)
- Appears in editions: [1939, 1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33456.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOSKYNS-ABRAHALL, Sir Theo Chandos, Kt. Bach. (1950), C.M.G. (1942).—b. 1896; ed. Epsom Coll., on mil. serv., 1915-20, capt.; admin. offr., Nig., 1921; senr. dist. offr., 1936; cl. I, 1937; dep. ch. sec., 1939; ch. comsnr., W. Prov., 1946; submitted recommendations for planning and development greater Lagos, 1946.

**Version `col1939-L67824.v` — printed in editions [1939, 1940]:**

> HOSKYNS-ABRAHALL, THEO.—B. 1896; ed. Epsom Coll.; served with H.M. Forces, France, Salonika, Egypt and Palestine; admstr. offr., Nigeria, 1921; senr. dist. offr., 1936; admstr. offr., cls. I, 1937; dep. ch. sec., 1939.

**Version `col1939-L67678.v` — printed in editions [1939]:**

> HOISKYNS-ABRAHALL, THEO.—B. 1896; ed. Epsom Coll.; served with H.M. Forces, France, Salonika, Egypt and Palestine; admstr. offr., Nigeria, 1921; senr. dist. offr., 1936; admstr. offr., cls. I, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | admin. offr. | Nigeria | [1939, 1940, 1948, 1949, 1950, 1951] |
| 1 | 1936 | senr. dist. offr | Nigeria *(inherited from previous clause)* | [1939, 1940, 1948, 1949, 1950, 1951] |
| 2 | 1937 | cl. I | Nigeria *(inherited from previous clause)* | [1939, 1940, 1948, 1949, 1950, 1951] |
| 3 | 1939 | dep. ch. sec | Nigeria *(inherited from previous clause)* | [1939, 1940, 1948, 1949, 1950, 1951] |
| 4 | 1946 | ch. comsnr., W. Prov | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hoskyns-Abraball, T___Nigeria___1934`

- Staff-list name: **Hoskyns-Abraball, T** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | T. Hoskyns-Abraball | — | Administrative Service | — | — |
| 1939 | T. Hoskyns-Abraball | Principal Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `hoskyns-abrahall_theo-chandos_b1896` vs `Hoskyns-Abraball, T___Nigeria___1934`

- [PASS] surname_gate: bio 'HOSKYNS-ABRAHALL' vs stint 'Hoskyns-Abraball, T' (fuzzy:1)
- [PASS] initials: bio ['T', 'C'] ~ stint ['T']
- [PASS] age_gate: stint starts 1934, birth 1896 (age 38)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 42 vs bar 60: 'senr. dist. offr' ~ 'Principal Assistant Secretary'
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

