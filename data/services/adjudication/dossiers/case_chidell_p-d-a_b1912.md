<!-- {"case_id": "case_chidell_p-d-a_b1912", "bio_ids": ["chidell_p-d-a_b1912"], "stint_ids": ["Chidell, P. D. A___Hong Kong___1949"]} -->
# Dossier case_chidell_p-d-a_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chidell_p-d-a_b1912`

- Printed name: **CHIDELL, P. D. A**
- Birth year: 1912 (attested in editions [1959, 1960])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1959-L21663.v` — printed in editions [1959, 1960]:**

> CHIDELL, P. D. A.—b. 1912; ed. Stowe; examiner, war tax dept., H.K., 1940; p.o.w., 1941-45; asst. comsrr., Inl. rev., 1947-59; arbit. nom. by govt. in dispute with H.K. Tel. Co., Ltd., 1949.

**Version `col1953-L16870.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958]:**

> CHIDELL, P. D. A.—b. 1912; ed. Stowe; examiner, war tax dept., H.K., 1940; p.o.w., 1941–45; asst. comsnr., inl. rev., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | examiner, war tax dept. | Hong Kong | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1941–1945 | p.o.w | Hong Kong *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1947–1959 | asst. comsrr., Inl. rev | Hong Kong *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1949 | arbit. nom. by govt. in dispute with H.K. Tel. Co., Ltd | Hong Kong *(inherited from previous clause)* | [1959, 1960] |

## Candidate stint `Chidell, P. D. A___Hong Kong___1949`

- Staff-list name: **Chidell, P. D. A** | colony: **Hong Kong** | listed 1949–1956 | editions [1949, 1950, 1951, 1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. D. A. Chidell | Assistant Commissioners of Inland Revenue | Inland Revenue | — | — |
| 1950 | P. D. A. Chidell | Assistant Commissioners of Inland Revenue | INLAND REVENUE | — | — |
| 1951 | P. D. A. Chidell | Assistant Commissioners of Inland Revenue | INLAND REVENUE | — | — |
| 1953 | P. D. A. Chidell | Assistant Commissioner of Inland Revenue | Civil Establishment | — | — |
| 1954 | P. D. A. Chidell | Assistant Commissioners of Inland Revenue | Civil Establishment | — | — |
| 1955 | P. D. A. Chidell | Assistant Commissioner of Inland Revenue | Civil Establishment | — | — |
| 1956 | P. D. A. Chidell | Assistant Commissioner of Inland Revenue | Civil Establishment | — | — |

### Deterministic checks: `chidell_p-d-a_b1912` vs `Chidell, P. D. A___Hong Kong___1949`

- [PASS] surname_gate: bio 'CHIDELL' vs stint 'Chidell, P. D. A' (exact)
- [PASS] initials: bio ['P', 'D', 'A'] ~ stint ['P', 'D', 'A']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1956
- [PASS] position_sim: best 61 vs bar 60: 'asst. comsrr., Inl. rev' ~ 'Assistant Commissioner of Inland Revenue'
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

