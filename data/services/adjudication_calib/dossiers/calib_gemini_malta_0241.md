<!-- {"case_id": "calib_gemini_malta_0241", "bio_ids": ["amato-gauci_f-e_b1917"], "stint_ids": ["Amato-Gauci, F. E___Malta___1953"]} -->
# Dossier calib_gemini_malta_0241

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `amato-gauci_f-e_b1917`

- Printed name: **AMATO-GAUCI, F. E**
- Birth year: 1917 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1955-L19480.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> AMATO-GAUCI, F. E., M.B.E. (mil.) (1945)—b. 1917; ed. St. John Academy and Royal Univ. of Malta; mil. serv., 1939–45, maj.; civ. serv. (admin.), Malta, 1936; prin. offr., 1948; dir. of labr., 1949; dir., labr. and soc. welf., 1955; dir., emig., labr. and soc. welf., 1956; under sec., 1959; (also ex off., registr., trade unions, and chmn., labr. bd., youth advsy. comtee., port workers' joint coun., port workers' bd.).

**Version `col1963-L16865.v` — printed in editions [1963, 1964]:**

> AMATO-GAUCI, F. E., M.B.E. (mil.) (1945)—b. 1917; ed. St. John Academy and Royal Univ. of Malta; mil. serv., 1939-45, maj.; civ. serv. (admin.), Malta, 1936; prin. offr., 1948; dir. of labr., 1949; dir., labr. and soc. welf., 1955; dir., emig., labr. and soc. welf., 1956; under sec., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | civ. serv. (admin.) | Malta | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | prin. offr | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1949 | dir. of labr | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1955 | dir., labr. and soc. welf | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1956 | dir., emig., labr. and soc. welf | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1959 | under sec | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Amato-Gauci, F. E___Malta___1953`

- Staff-list name: **Amato-Gauci, F. E** | colony: **Malta** | listed 1953–1959 | editions [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | F. E. Amato-Gauci | Director of Labour | The Maltese Government | — | — |
| 1954 | F. E. Amato-Gauci | Director of Labour | The Maltese Government | — | — |
| 1955 | F. E. Amato-Gauci | Director of Labour | THE MALTESE GOVERNMENT | — | — |
| 1956 | F. E. Amato-Gauci | Director of Labour | The Maltese Government | — | — |
| 1957 | F. E. Amato-Gauci | Director of Emigration, Labour and Social Welfare | The Maltese Government | — | — |
| 1958 | F. E. Amato-Gauci | Director of Emigration, Labour and Social Welfare | The Maltese Government | — | — |
| 1959 | F. E. Amato-Gauci | Director of Emigration, Labour and Social Welfare | The Maltese Government | M.B.E. | — |

### Deterministic checks: `amato-gauci_f-e_b1917` vs `Amato-Gauci, F. E___Malta___1953`

- [PASS] surname_gate: bio 'AMATO-GAUCI' vs stint 'Amato-Gauci, F. E' (exact)
- [PASS] initials: bio ['F', 'E'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1953, birth 1917 (age 36)
- [PASS] colony: 6 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1953-1959
- [PASS] position_sim: best 94 vs bar 60: 'dir. of labr' ~ 'Director of Labour'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1955, 1956, 1957, 1958] pos~74 (bar: >=2)
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

