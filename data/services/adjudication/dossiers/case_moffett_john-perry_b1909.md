<!-- {"case_id": "case_moffett_john-perry_b1909", "bio_ids": ["moffett_john-perry_b1909"], "stint_ids": ["Moffett, J. P___Tanganyika___1954"]} -->
# Dossier case_moffett_john-perry_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `moffett_john-perry_b1909`

- Printed name: **MOFFETT, John Perry**
- Birth year: 1909 (attested in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960])
- Honours: B.A, C.M.G (1959)
- Appears in editions: [1949, 1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1954-L21607.v` — printed in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960]:**

> MOFFETT, J. P., C.M.G. (1959).—b. 1909; ed. Cork Gram. Sch. and Dublin Univ.; cadet, Tang., 1932; A.D.O., 1934; spec. duty evac. Africans from sleep sickness areas, 1936-37; D.O., 1944; native cts. advr., 1948; prin. asst. sec., 1952; comsnr., soc. devel., 1953-59; ed. Tanganyika; A review of its resources and their development.

**Version `col1949-L34372.v` — printed in editions [1949, 1951]:**

> MOFFETT, John Perry, B.A., LL.B. (T.C.D.).—b. 1909; ed. Cork Grammar Sch., Dublin Univ.; cadet, T.T., 1932; asst. dist. offr., 1934; special duty, evac. of natives from sleep. sick. areas, 1936; dist. offr.; native courts advr., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | cadet | Tanganyika | [1949, 1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1934 | A.D.O | Tanganyika *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1934 | asst. dist. offr | — | [1949, 1951] |
| 3 | 1936–1937 | spec. duty evac. Africans from sleep sickness areas | Tanganyika *(inherited from previous clause)* | [1949, 1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 4 | 1944 | spec. duty evac. Africans from sleep sickness areas | Dominions Office | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 5 | 1948 | native cts. advr | Dominions Office *(inherited from previous clause)* | [1949, 1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 6 | 1952 | prin. asst. sec | Dominions Office *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 7 | 1953–1959 | comsnr., soc. devel | Dominions Office *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Moffett, J. P___Tanganyika___1954`

- Staff-list name: **Moffett, J. P** | colony: **Tanganyika** | listed 1954–1958 | editions [1954, 1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | J. P. Moffett | Commissioner for Social Development | Civil Establishment | — | — |
| 1956 | J. P. Moffett | Commissioner for Social Development | Civil Establishment | — | — |
| 1957 | J. P. Moffett | Commissioner for Social Development | Civil Establishment | — | — |
| 1958 | J. P. Moffett | Commissioner for Social Development | Civil Establishment | — | — |

### Deterministic checks: `moffett_john-perry_b1909` vs `Moffett, J. P___Tanganyika___1954`

- [PASS] surname_gate: bio 'MOFFETT' vs stint 'Moffett, J. P' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1954, birth 1909 (age 45)
- [PASS] colony: 3 placed event(s) resolve to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1958
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

