<!-- {"case_id": "case_morris_r-h_b1915", "bio_ids": ["morris_r-h_b1915"], "stint_ids": ["Morris, R. H___Sarawak___1949"]} -->
# Dossier case_morris_r-h_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 113 official(s) with this surname in the graph's staff lists; 39 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morris_r-h_b1915`

- Printed name: **MORRIS, R. H**
- Birth year: 1915 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1963)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L25436.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> MORRIS, R. H., O.B.E. (1963).—b. 1915; ed. Maitland High Sch., N.S.W., and Sydney Univ.; mil. serv., 1940–46, capt.; admin. cadet, Sarawak, 1946; asst. D.O., 1947; D.O., 1950; prin. asst. sec., 1952; seconded, asst. resdt., Brunei, 1954–58; dist. offr., Sarawak, 1958–64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. cadet | Sarawak | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1947 | asst. D.O | Sarawak *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1950 | asst. D.O | Dominions Office | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1952 | prin. asst. sec | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1954–1958 | seconded, asst. resdt. | Brunei | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 5 | 1958–1964 | dist. offr. | Sarawak | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Morris, R. H___Sarawak___1949`

- Staff-list name: **Morris, R. H** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. H. Morris | District Officer / Assistant District Officer / Cadet | Administrative Service | — | — |
| 1950 | R. H. Morris | District Officers, Assistant District Officers and Cadets | Administrative Service | — | — |
| 1951 | R. H. Morris | District Officers, Assistant District Officers and Cadets | Administrative Service | — | — |

### Deterministic checks: `morris_r-h_b1915` vs `Morris, R. H___Sarawak___1949`

- [PASS] surname_gate: bio 'MORRIS' vs stint 'Morris, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 3 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 36 vs bar 60: 'asst. D.O' ~ 'District Officer / Assistant District Officer / Cadet'
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

