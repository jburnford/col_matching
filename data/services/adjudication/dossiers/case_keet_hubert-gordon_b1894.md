<!-- {"case_id": "case_keet_hubert-gordon_b1894", "bio_ids": ["keet_hubert-gordon_b1894"], "stint_ids": ["Keet, H. G___Straits Settlements___1932"]} -->
# Dossier case_keet_hubert-gordon_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `keet_hubert-gordon_b1894`

- Printed name: **KEET, Hubert Gordon**
- Birth year: 1894 (attested in editions [1937, 1939, 1940])
- Honours: D.S.O, M.C
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L62297.v` — printed in editions [1937, 1939, 1940]:**

> KEET, Major Hubert Gordon, D.S.O., M.C., (Reg. Army, R. of O.)—B. 1894; supt. excise, S.S., 1909; served Great War, France and Belgium, 1914-18, (twice ment. in desps.); asst. contr., govt. monops., S.S., June 1923; ag. asst. supt., do., 1930; contr., govt., monopo., June, 1931; senr. contr., May, 1933; contr., govt. monopo., Malacca, May, 1934; dep. contr., rubber, June, 1934; J.P., Malacca, Oct., 1934; supt., excise, S'pore, Mar., 1936; supt., cust. and excise, Taiping, Perak, Dec., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | supt. excise | Straits Settlements | [1937, 1939, 1940] |
| 1 | 1914–1918 | served Great War, France and Belgium | Straits Settlements *(inherited from previous clause)* | [1937, 1939, 1940] |
| 2 | 1923 | asst. contr., govt. monops. | Straits Settlements | [1937, 1939, 1940] |
| 3 | 1930 | ag. asst. supt. | Dominions Office | [1937, 1939, 1940] |
| 4 | 1931 | contr., govt., monopo | Dominions Office *(inherited from previous clause)* | [1937, 1939, 1940] |
| 5 | 1933 | senr. contr | Dominions Office *(inherited from previous clause)* | [1937, 1939, 1940] |
| 6 | 1934 | contr., govt. monopo., Malacca | Dominions Office *(inherited from previous clause)* | [1937, 1939, 1940] |
| 7 | 1936 | supt., excise, S'pore | Dominions Office *(inherited from previous clause)* | [1937, 1939, 1940] |

## Candidate stint `Keet, H. G___Straits Settlements___1932`

- Staff-list name: **Keet, H. G** | colony: **Straits Settlements** | listed 1932–1936 | editions [1932, 1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | H. G. Keet | Assistant Controller | Government Monopolies Department | D.S.O. | — |
| 1933 | H. G. Keet | Controllers | Government Monopolies Department | D.S.O. | — |
| 1936 | H. G. Keet | Superintendent of Excise | Department of Excise | D.S.O. | — |

### Deterministic checks: `keet_hubert-gordon_b1894` vs `Keet, H. G___Straits Settlements___1932`

- [PASS] surname_gate: bio 'KEET' vs stint 'Keet, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1932, birth 1894 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: D.S.O
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

