<!-- {"case_id": "case_thomson_n-a_b1897", "bio_ids": ["thomson_n-a_b1897"], "stint_ids": ["Thomson, N. A___Northern Rhodesia___1951"]} -->
# Dossier case_thomson_n-a_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 111 official(s) with this surname in the graph's staff lists; 35 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `thomson_n-a_b1897`

- Printed name: **THOMSON, N. A**
- Birth year: 1897 (attested in editions [1951, 1953, 1954, 1955, 1957, 1958, 1960])
- Honours: C.B.E (1958)
- Appears in editions: [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1951-L43165.v` — printed in editions [1951, 1953, 1954, 1955, 1957, 1958, 1960]:**

> THOMSON, N. A., C.B.E. (1958).—b. 1897; ed. Grey Inst., Pt. Elizabeth; mil. serv., 1940-45, capt.; apptd. pub. serv., 1913; div. contrlr., posts, Union of S.A.; dep. P.M.G., N. Rhod., 1946; P.M.G., 1949; secon. fedl. govt., 1954; ret. 1959.

**Version `col1956-L24565.v` — printed in editions [1956, 1959]:**

> THOMPSON, N. A., C.B.E. (1958).—b. 1897; ed. Grey Inst., Pt. Elizabeth; mil. serv., 1940-45, capt.; apptd. pub. serv., 1913; div. contrlr. posts, Union of S.A.; dep. P.M.G., N. Rhod., 1946; P.M.G., 1949; secon. fedl. govt., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | apptd. pub. serv | — | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1946 | dep. P.M.G. | Northern Rhodesia | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1949 | P.M.G | Northern Rhodesia *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1954 | secon. fedl. govt | Northern Rhodesia *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 4 | 1959 | ret | Northern Rhodesia *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1957, 1958, 1960] |

## Candidate stint `Thomson, N. A___Northern Rhodesia___1951`

- Staff-list name: **Thomson, N. A** | colony: **Northern Rhodesia** | listed 1951–1958 | editions [1951, 1953, 1954, 1955, 1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | N. A. Thomson | Postmaster-General | Posts and Telegraphs | — | — |
| 1953 | N. A. Thomson | Postmaster-General | Civil Establishment | — | — |
| 1954 | N. A. Thomson | Postmaster-General | Civil Establishment | — | — |
| 1955 | N. A. Thomson | Postmaster-General | Civil Establishment | — | — |
| 1956 | N. A. Thomson | Postmaster-General | Civil Establishment | — | — |
| 1957 | N. A. Thomson | Postmaster-General | Civil Establishment | — | — |
| 1958 | N. A. Thomson | Postmaster-General | Civil Establishment | C.B.E. | — |

### Deterministic checks: `thomson_n-a_b1897` vs `Thomson, N. A___Northern Rhodesia___1951`

- [PASS] surname_gate: bio 'THOMSON' vs stint 'Thomson, N. A' (exact)
- [PASS] initials: bio ['N', 'A'] ~ stint ['N', 'A']
- [PASS] age_gate: stint starts 1951, birth 1897 (age 54)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1951-1958
- [FAIL] position_sim: best 31 vs bar 60: 'secon. fedl. govt' ~ 'Postmaster-General'
- [PASS] honour: shared: C.B.E
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

