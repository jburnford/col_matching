<!-- {"case_id": "case_leverseedge_leslie-frank_e1926", "bio_ids": ["leverseedge_leslie-frank_e1926"], "stint_ids": ["Leversedge, L. F___Northern Rhodesia___1952"]} -->
# Dossier case_leverseedge_leslie-frank_e1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Leversedge, L. F___Northern Rhodesia___1952` is also gate-compatible with biography(ies) outside this case: ['leversedge_l-f_b1904'] (already linked elsewhere or filtered).

## Biography `leverseedge_leslie-frank_e1926`

- Printed name: **LEVERSEEDGE, Leslie Frank**
- Birth year: not printed
- Appears in editions: [1949, 1950, 1954]

### Verbatim printed entry text (OCR)

**Version `col1949-L33646.v` — printed in editions [1949, 1950, 1954]:**

> LEVERSEEDGE, Leslie Frank.—ed. St. Paul’s Sch., Darjeeling, India, St. Peter’s Sch., York and St. John’s Coll., Camb., M.A. (Cantab.); barrister-at-law (Inner Temple); cadet, N. Rhod., 1926; dist. offr., 1928; prov. comsnr., 1947; senr., 1949; mem. N. Rhod. police comsn. of enquiry, 1946-47.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | cadet | Northern Rhodesia | [1949, 1950, 1954] |
| 1 | 1928 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1949, 1950, 1954] |
| 2 | 1946–1947 | mem. N. Rhod. police comsn. of enquiry | Northern Rhodesia *(inherited from previous clause)* | [1949, 1950, 1954] |
| 3 | 1947 | prov. comsnr | Northern Rhodesia *(inherited from previous clause)* | [1949, 1950, 1954] |
| 4 | 1949 | senr | Northern Rhodesia *(inherited from previous clause)* | [1949, 1950, 1954] |

## Candidate stint `Leversedge, L. F___Northern Rhodesia___1952`

- Staff-list name: **Leversedge, L. F** | colony: **Northern Rhodesia** | listed 1952–1958 | editions [1952, 1953, 1954, 1955, 1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | L. F. Leversedge | Development Secretary | Civil Establishment | — | — |
| 1953 | L. F. Leversedge | Development Secretary | Civil Establishment | — | — |
| 1954 | L. F. Leversedge | Development Secretary | Civil Establishment | — | — |
| 1955 | L. F. Leversedge | Development Secretary | Civil Establishment | — | — |
| 1956 | L. F. Leversedge | Development Secretary | Civil Establishment | C.M.G. | — |
| 1957 | L. F. Leversedge | Economic Secretary | Civil Establishment | C.M.G. | — |
| 1958 | L. F. Leversedge | Economic Secretary | Executive Council | C.M.G. | — |
| 1958 | L. F. Leversedge | Economic Secretary | Civil Establishment | C.M.G. | — |

### Deterministic checks: `leverseedge_leslie-frank_e1926` vs `Leversedge, L. F___Northern Rhodesia___1952`

- [PASS] surname_gate: bio 'LEVERSEEDGE' vs stint 'Leversedge, L. F' (fuzzy:1)
- [PASS] initials: bio ['L', 'F'] ~ stint ['L', 'F']
- [PASS] age_gate: stint starts 1952; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1958
- [FAIL] position_sim: best 27 vs bar 60: 'senr' ~ 'Economic Secretary'
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

