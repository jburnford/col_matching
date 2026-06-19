<!-- {"case_id": "case_tacey_neville-stanley_b1904", "bio_ids": ["tacey_neville-stanley_b1904"], "stint_ids": ["Lacey, N___Northern Rhodesia___1925"]} -->
# Dossier case_tacey_neville-stanley_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tacey_neville-stanley_b1904`

- Printed name: **TACEY, Neville Stanley**
- Birth year: 1904 (attested in editions [1950, 1951])
- Honours: E.D. (Territorial)
- Appears in editions: [1949, 1950, 1951, 1956]

### Verbatim printed entry text (OCR)

**Version `col1950-L39992.v` — printed in editions [1950, 1951]:**

> TACEY, Neville Stanley, E.D. (Territorial), barrister-at-law (Middle Temple).—b. 1904; ed. Hurstpierpoint Coll., Sussex; R.A. (T.A.) 1925-36, capt.; R.A. (T.A.R.O.), 1936; K.A.R.R.O., 1938; on mil. serv., 1939, 1940-46, capt., R.A. (T.A.R.O.), 1946; res. mag., T.T., 1938.

**Version `col1949-L36064.v` — printed in editions [1949]:**

> TACEY, Neville Stanley, E.D. (Territorial), Barrister-at-Law (Middle Temple).—b. 1904 ; ed. Hurstpierpoint Coll., Sussex ; on mil. serv. 1939, 1940-46 ; capt., R.A. (T.A.R.O.), 1946 ; res. mag., T.T., 1938.

**Version `col1956-L24465.v` — printed in editions [1956]:**

> TACEY, N. S., T.D.—b. 1904; ed. Hurstpierpoint Coll., Sussex; barrister-at-law, Middle Temple; mil. serv., 1939-46, capt.; res. mag., Tang., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925–1936 | capt. | — | [1950, 1951] |
| 1 | 1936–1936 | R.A. (T.A.R.O.) | — | [1950, 1951] |
| 2 | 1938–1938 | K.A.R.R.O. | — | [1950, 1951] |
| 3 | 1938–1938 | res. mag. | Tanganyika Territory | [1949, 1950, 1951, 1956] |
| 4 | 1939–1946 | on mil. serv. | — | [1950, 1951] |
| 5 | 1946–1946 | capt., R.A. (T.A.R.O.) | — | [1949, 1950, 1951] |

## Candidate stint `Lacey, N___Northern Rhodesia___1925`

- Staff-list name: **Lacey, N** | colony: **Northern Rhodesia** | listed 1925–1933 | editions [1925, 1927, 1928, 1929, 1930, 1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | N. Lacey | Collectors | Customs | — | — |
| 1927 | N. Lacey | Collectors | Customs | — | — |
| 1928 | N. Lacey | Collector | Customs | — | — |
| 1929 | N. Lacey | Collectors | Customs | — | — |
| 1930 | N. Lacey | Collector | Customs | — | — |
| 1931 | N. Lacey | Collectors | Customs | — | — |
| 1933 | N. Lacey | Senior Collector of Customs | Customs | — | — |

### Deterministic checks: `tacey_neville-stanley_b1904` vs `Lacey, N___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'TACEY' vs stint 'Lacey, N' (fuzzy:1)
- [PASS] initials: bio ['N', 'S'] ~ stint ['N']
- [PASS] age_gate: stint starts 1925, birth 1904 (age 21)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1933
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

