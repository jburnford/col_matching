<!-- {"case_id": "case_prior_william-h_b1878", "bio_ids": ["prior_william-h_b1878"], "stint_ids": ["Prior, H___Sarawak___1910"]} -->
# Dossier case_prior_william-h_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `prior_william-h_b1878`

- Printed name: **PRIOR, WILLIAM H.**
- Birth year: 1878 (attested in editions [1924])
- Appears in editions: [1924]

### Verbatim printed entry text (OCR)

**Version `col1924-L57334.v` — printed in editions [1924]:**

> PRIOR, HON. WILLIAM H., B.A., LL.B.—B. 1878; ed. pub. and high schls., Ont., Osgoode Hall Law Schol., Toronto Univ. (B.A., LL.B.); barrister; el. to Ont. legis., g.o., 1914; re.e.l., 1919 and 1923; prov. treasurer in Ferguson admntr., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1914 | el. to Ont. legis., g.o. | Ontario | [1924] |
| 1 | 1919–1923 | re.e.l. | — | [1924] |
| 2 | 1923–1923 | prov. treasurer in Ferguson admntr. | — | [1924] |

## Candidate stint `Prior, H___Sarawak___1910`

- Staff-list name: **Prior, H** | colony: **Sarawak** | listed 1910–1913 | editions [1910, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | H. Prior | Assistant Superintendent of Police | Civil Establishment | — | — |
| 1912 | H. Prior | Assistant Superintendent of Police | Civil Establishment | — | — |
| 1913 | H. Prior | Assistant Superintendent of Police | Civil Establishment | — | — |

### Deterministic checks: `prior_william-h_b1878` vs `Prior, H___Sarawak___1910`

- [PASS] surname_gate: bio 'PRIOR' vs stint 'Prior, H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1910, birth 1878 (age 32)
- [FAIL] colony: no placed event resolves to 'Sarawak'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1913
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

