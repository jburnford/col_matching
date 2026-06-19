<!-- {"case_id": "case_hockley_naivashene-phyllis_b1910", "bio_ids": ["hockley_naivashene-phyllis_b1910"], "stint_ids": ["Hockley, N. P___Kenya___1937"]} -->
# Dossier case_hockley_naivashene-phyllis_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hockley_naivashene-phyllis_b1910`

- Printed name: **HOCKLEY, Naivashene Phyllis**
- Birth year: 1910 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32928.v` — printed in editions [1949, 1950, 1951]:**

> HOCKLEY, Naivashene Phyllis.—b. 1910; ed. Loreto Convent, Nairobi, Camden House Coll., Lond. (high. Froebel teach. cert.); asst. mistress, Jeanes Sch., Ken., 1934; prin., educ. dept., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | asst. mistress, Jeanes Sch. | Kenya | [1949, 1950, 1951] |
| 1 | 1948 | prin., educ. dept | Kenya *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Hockley, N. P___Kenya___1937`

- Staff-list name: **Hockley, N. P** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | N. P. Hockley | Education Officer—African Education | Education | — | — |
| 1939 | Miss N. P. Hockley | Education Officer, African Education | Education | — | — |
| 1940 | Miss N. P. Hockley | Education Officers—African Education | Education | — | — |

### Deterministic checks: `hockley_naivashene-phyllis_b1910` vs `Hockley, N. P___Kenya___1937`

- [PASS] surname_gate: bio 'HOCKLEY' vs stint 'Hockley, N. P' (exact)
- [PASS] initials: bio ['N', 'P'] ~ stint ['N', 'P']
- [PASS] age_gate: stint starts 1937, birth 1910 (age 27)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 33 vs bar 60: 'asst. mistress, Jeanes Sch.' ~ 'Education Officer, African Education'
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

