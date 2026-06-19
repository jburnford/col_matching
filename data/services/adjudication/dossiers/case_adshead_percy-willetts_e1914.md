<!-- {"case_id": "case_adshead_percy-willetts_e1914", "bio_ids": ["adshead_percy-willetts_e1914"], "stint_ids": ["Adshead, P. W___Uganda___1928"]} -->
# Dossier case_adshead_percy-willetts_e1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Adshead, P. W___Uganda___1928` is also gate-compatible with biography(ies) outside this case: ['adshead_percy-williams_b1892'] (already linked elsewhere or filtered).

## Biography `adshead_percy-willetts_e1914`

- Printed name: **ADSHEAD, Percy Willetts**
- Birth year: not printed
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L30728.v` — printed in editions [1948, 1949]:**

> ADSHEAD, Percy Willetts, A.C.A.—b.—ed. Tettenham Coll.; on mil. serv. 1914-19, capt., and 1941-46, col.; ch. acctnt., P.W.D., Uga., 1926; senr. asst. treas., Pal., 1937; acctnt.-gen., 1941; inspr.-gen. of fin. and acctnts., 1943; contrlr. of fin., 1944; acctnt.-gen., Nig., 1946; mem. of business profits comttee., Uga., 1928, Morris Carter cotton coms., 1929, and of Cams. dev. corp., 1946; ext. M.L.C., Nig., Oct. and Dec., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | capt. | — | [1948, 1949] |
| 1 | 1926–1926 | ch. acctnt., P.W.D. | Uganda | [1948, 1949] |
| 2 | 1928–1928 | mem. of business profits comttee. | Uganda | [1948, 1949] |
| 3 | 1929–1929 | Morris Carter cotton coms. | — | [1948, 1949] |
| 4 | 1937–1937 | senr. asst. treas. | Palestine | [1948, 1949] |
| 5 | 1941–1946 | col. | — | [1948, 1949] |
| 6 | 1941–1941 | acctnt.-gen. | — | [1948, 1949] |
| 7 | 1943–1943 | inspr.-gen. of fin. and acctnts. | — | [1948, 1949] |
| 8 | 1944–1944 | contrlr. of fin. | — | [1948, 1949] |
| 9 | 1946–1946 | acctnt.-gen. | Nigeria | [1948, 1949] |
| 10 | 1946–1946 | and of Cams. dev. corp. | Cameroons | [1948, 1949] |

## Candidate stint `Adshead, P. W___Uganda___1928`

- Staff-list name: **Adshead, P. W** | colony: **Uganda** | listed 1928–1933 | editions [1928, 1929, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | P. W. Adshead | Chief Accountant | Public Works | — | — |
| 1929 | P. W. Adshead | Chief Accountant | Public Works | — | — |
| 1933 | P. W. Adshead | Chief Accountant | Public Works Department | — | — |

### Deterministic checks: `adshead_percy-willetts_e1914` vs `Adshead, P. W___Uganda___1928`

- [PASS] surname_gate: bio 'ADSHEAD' vs stint 'Adshead, P. W' (exact)
- [PASS] initials: bio ['P', 'W'] ~ stint ['P', 'W']
- [PASS] age_gate: stint starts 1928; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1928-1933
- [FAIL] position_sim: best 30 vs bar 60: 'mem. of business profits comttee.' ~ 'Chief Accountant'
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

