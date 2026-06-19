<!-- {"case_id": "case_kemsley_s-h_b1905", "bio_ids": ["kemsley_s-h_b1905"], "stint_ids": ["Kemsley, S. H___Bermuda___1950"]} -->
# Dossier case_kemsley_s-h_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kemsley_s-h_b1905`

- Printed name: **KEMSLEY, S. H**
- Birth year: 1905 (attested in editions [1961, 1962, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L24010.v` — printed in editions [1961, 1962, 1964, 1965, 1966]:**

> KEMSLEY, S. H.—b. 1905; ed. Military Sch., Prospect, Bermuda, and Saltus Gram. Sch., Bermuda; mil. serv., 1942-46, capt.; survr. & dftsmn., P.W.D., Berm., 1937; exec. offr., transport cont. bd., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | survr. & dftsmn., P.W.D. | Bermuda | [1961, 1962, 1964, 1965, 1966] |
| 1 | 1946 | exec. offr., transport cont. bd | Bermuda *(inherited from previous clause)* | [1961, 1962, 1964, 1965, 1966] |

## Candidate stint `Kemsley, S. H___Bermuda___1950`

- Staff-list name: **Kemsley, S. H** | colony: **Bermuda** | listed 1950–1966 | editions [1950, 1951, 1952, 1953, 1954, 1955, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | S. H. Kemsley | Executive Officer | TRANSPORT CONTROL BOARD | — | — |
| 1951 | S. H. Kemsley | Executive Officer | TRANSPORT CONTROL BOARD | — | — |
| 1952 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1953 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1954 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1955 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1957 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1958 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1959 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1960 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1961 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1962 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1963 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1965 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |
| 1966 | S. H. Kemsley | Executive Officer, Transport Control Board | Civil Establishment | — | — |

### Deterministic checks: `kemsley_s-h_b1905` vs `Kemsley, S. H___Bermuda___1950`

- [PASS] surname_gate: bio 'KEMSLEY' vs stint 'Kemsley, S. H' (exact)
- [PASS] initials: bio ['S', 'H'] ~ stint ['S', 'H']
- [PASS] age_gate: stint starts 1950, birth 1905 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Bermuda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1966
- [PASS] position_sim: best 79 vs bar 60: 'exec. offr., transport cont. bd' ~ 'Executive Officer, Transport Control Board'
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

