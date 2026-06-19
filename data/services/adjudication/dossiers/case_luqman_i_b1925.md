<!-- {"case_id": "case_luqman_i_b1925", "bio_ids": ["luqman_i_b1925"], "stint_ids": ["Luqman, I___Aden___1964"]} -->
# Dossier case_luqman_i_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['luqman_i_b1925'] carry a single initial only — the namesake trap applies.

## Biography `luqman_i_b1925`

- Printed name: **LUQMAN, I**
- Birth year: 1925 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L22218.v` — printed in editions [1963, 1964, 1965, 1966]:**

> LUQMAN, I.—b. 1925; ed. Sec. Sch., Aden; American Univ., Cairo, and Lond. Univ.; asst. hd. mstr., int. sch., Aden, 1952; dist. mstr., 1956; educ. offr., 1958; vice-prin., tech. inst., 1959; senr. educ. offr., 1960; admin. offr., cl. II, 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | asst. hd. mstr., int. sch. | Aden | [1963, 1964, 1965, 1966] |
| 1 | 1956 | dist. mstr | Aden *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1959 | vice-prin., tech. inst | Aden *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 3 | 1960 | senr. educ. offr | Aden *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 4 | 1963 | admin. offr., cl. II | Aden *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Luqman, I___Aden___1964`

- Staff-list name: **Luqman, I** | colony: **Aden** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | I. Luqman | Administrative Officers (Superscale) | CIVIL ESTABLISHMENT | — | — |
| 1965 | I. Luqman | Administrative Officers (Superscale) | Civil Establishment | — | — |
| 1966 | I. Luqman | Deputy Chairman, Public Service Commission | Joint Organisations | — | — |
| 1966 | I. Luqman | Deputy Ministerial Secretary | Civil Establishment | — | — |

### Deterministic checks: `luqman_i_b1925` vs `Luqman, I___Aden___1964`

- [PASS] surname_gate: bio 'LUQMAN' vs stint 'Luqman, I' (exact)
- [PASS] initials: bio ['I'] ~ stint ['I']
- [PASS] age_gate: stint starts 1964, birth 1925 (age 39)
- [PASS] colony: 5 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1964-1966
- [FAIL] position_sim: best 48 vs bar 60: 'admin. offr., cl. II' ~ 'Administrative Officers (Superscale)'
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

