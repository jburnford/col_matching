<!-- {"case_id": "case_waugh_harold-brook_b1903", "bio_ids": ["waugh_harold-brook_b1903"], "stint_ids": ["Waugh, H. B___Northern Rhodesia___1936"]} -->
# Dossier case_waugh_harold-brook_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `waugh_harold-brook_b1903`

- Printed name: **WAUGH, Harold Brook**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36722.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WAUGH, Harold Brook.—b. 1903 ; ed. Campbell Coll., Belfast, Royal Belfast Acad. Inst. and Emmanuel Coll., Camb., B.A. (Cantab.) ; cadet, N. Rhod., 1929 ; dist. offr., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1931 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Waugh, H. B___Northern Rhodesia___1936`

- Staff-list name: **Waugh, H. B** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | H. B. Waugh | District Officers | District Administration | — | — |
| 1939 | H. B. Waugh | District Officer | District Administration | — | — |
| 1940 | H. B. Waugh | District Officer | District Administration | — | — |

### Deterministic checks: `waugh_harold-brook_b1903` vs `Waugh, H. B___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'WAUGH' vs stint 'Waugh, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1936, birth 1903 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 72 vs bar 60: 'dist. offr' ~ 'District Officer'
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

