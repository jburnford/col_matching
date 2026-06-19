<!-- {"case_id": "case_ram_labhaya-milhotra_b1900", "bio_ids": ["ram_labhaya-milhotra_b1900"], "stint_ids": ["Ram, L. M___British Honduras___1936"]} -->
# Dossier case_ram_labhaya-milhotra_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ram_labhaya-milhotra_b1900`

- Printed name: **RAM, Labhaya Milhotra**
- Birth year: 1900 (attested in editions [1956])
- Honours: B.S, D.P.H, M.B, M.R.C.P
- Appears in editions: [1948, 1949, 1950, 1951, 1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L23665.v` — printed in editions [1956]:**

> RAM, L. M.—b. 1900; ed. King Edward Medical Coll., Lahore and Punjab and London Univs.; mil. serv., 1942-46, lt.-col.; M.O., Bajwara hosp., India, 1925; asst. M.O., soc. hygiene, F.M.S., 1927; M.O., B. Hond., 1935; Fed. of Mal., 1948; S.M.O., soc. hygiene, S'pore, 1949; ch. health offr., 1954; identified malaria carrier mosquitoes, B. Hond., 1941; W.H.O. fellow, 1953; app. W.H.O. panel of experts on treponematosis and venereal infections, 1955.

**Version `col1951-L41831.v` — printed in editions [1951]:**

> RAM, Labhaya Milhotra, M.B., B.S. (Punjab), M.R.C.P.(Edin.), D.P.H.(Lond.)—b. 1900; ed. K.E. Punjab Univ., Edin. Univ. and Lond. Univ.; asst. surg. V.D. spec., Mal., 1927; med. offr., B. Hond., 1935; Indian Army, 1942-46; Mal., 1948; ag. S.M.O. soc. hyg., S'pore, 1949.

**Version `col1948-L35402.v` — printed in editions [1948, 1949, 1950]:**

> RAM, Labhaya Milhotra, M.B., B.S., M.R.C.P., D.P.H.—b. 1900; ed. K.E. Med., Coll., Lahore and London Univ.; on mil. serv. 1942–46, lt.-col.; med. dept., Malaya, 1927; med. offr., Br. Hond., 1935; Mal., 1947; author of Observations on the Anophele of British Honduras and A Cure of Eclampsia.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | M.O., Bajwara hosp., India | — | [1956] |
| 1 | 1927 | asst. M.O., soc. hygiene | Federated Malay States | [1956] |
| 2 | 1927 | asst. surg. V.D. spec. | Malaya | [1948, 1949, 1950, 1951] |
| 3 | 1935 | M.O. | British Honduras | [1951, 1956] |
| 4 | 1935 | med. offr., Br. Hond | Malaya *(inherited from previous clause)* | [1948, 1949, 1950] |
| 5 | 1941 | identified malaria carrier mosquitoes | British Honduras | [1956] |
| 6 | 1942–1946 | Indian Army | British Honduras *(inherited from previous clause)* | [1951] |
| 7 | 1947 | med. offr., Br. Hond | Malaya | [1948, 1949, 1950] |
| 8 | 1948 | Fed. of Mal | British Honduras *(inherited from previous clause)* | [1956] |
| 9 | 1948 | Indian Army | Malaya | [1951] |
| 10 | 1949 | S.M.O., soc. hygiene, S'pore | British Honduras *(inherited from previous clause)* | [1951, 1956] |
| 11 | 1953 | W.H.O. fellow | British Honduras *(inherited from previous clause)* | [1956] |
| 12 | 1954 | ch. health offr | British Honduras *(inherited from previous clause)* | [1956] |
| 13 | 1955 | app. W.H.O. panel of experts on treponematosis and venereal infections | British Honduras *(inherited from previous clause)* | [1956] |

## Candidate stint `Ram, L. M___British Honduras___1936`

- Staff-list name: **Ram, L. M** | colony: **British Honduras** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | L. M. Ram | Medical Officer | Medical | — | — |
| 1937 | L. M. Ram | Medical Officers | Medical | — | — |
| 1939 | L. M. Ram | Medical Officer | Medical | — | — |
| 1940 | L. M. Ram | Medical Officer | Medical | — | — |

### Deterministic checks: `ram_labhaya-milhotra_b1900` vs `Ram, L. M___British Honduras___1936`

- [PASS] surname_gate: bio 'RAM' vs stint 'Ram, L. M' (exact)
- [PASS] initials: bio ['L', 'M'] ~ stint ['L', 'M']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [PASS] colony: 8 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 38 vs bar 60: 'identified malaria carrier mosquitoes' ~ 'Medical Officers'
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

