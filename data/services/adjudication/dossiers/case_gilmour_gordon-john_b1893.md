<!-- {"case_id": "case_gilmour_gordon-john_b1893", "bio_ids": ["gilmour_gordon-john_b1893"], "stint_ids": ["Gilmour, G. J___Straits Settlements___1932"]} -->
# Dossier case_gilmour_gordon-john_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gilmour_gordon-john_b1893`

- Printed name: **GILMOUR, GORDON JOHN**
- Birth year: 1893 (attested in editions [1936, 1937, 1940])
- Appears in editions: [1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L61003.v` — printed in editions [1936, 1937, 1940]:**

> GILMOUR, GORDON JOHN.—B. 1893; ed. Fremantle schol. (W.A.); supvr. govt. monops., S.S., Feb., 1911; war serv., Jan., 1915-Mar., 1919; supvr., tob. dep., govt. monops., S.S., July, 1919; supvr., grade I, Jan., 1924; contr., Feb., 1930; asst. supt., S'pore, Nov., 1931; do., Penang, June, 1933; in addn., dep. supt., rubber control, Penang Is., June, 1934; dep. comsrr., preventive br., S'pore, dep. supt., rubber control in adln., Oct., 1935; dep. comsrr., Negri Semb., Apr., 1938; title changed to asst. comptlr., cust., Oct., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | supvr. govt. monops. | Straits Settlements | [1936, 1937, 1940] |
| 1 | 1919 | supvr., tob. dep., govt. monops. | Straits Settlements | [1936, 1937, 1940] |
| 2 | 1924 | supvr., grade I | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 3 | 1930 | contr | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 4 | 1931 | asst. supt., S'pore | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 5 | 1933 | do., Penang | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 6 | 1934 | in addn., dep. supt., rubber control, Penang Is | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 7 | 1935 | dep. comsrr., preventive br., S'pore, dep. supt., rubber control in adln | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 8 | 1938 | dep. comsrr., Negri Semb | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |

## Candidate stint `Gilmour, G. J___Straits Settlements___1932`

- Staff-list name: **Gilmour, G. J** | colony: **Straits Settlements** | listed 1932–1936 | editions [1932, 1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | G. J. Gilmour | Controller | Government Monopolies Department | — | — |
| 1933 | G. J. Gilmour | Controllers | Government Monopolies Department | — | — |
| 1936 | G. J. Gilmour | Deputy Commissioner of Excise | Department of Excise | — | — |

### Deterministic checks: `gilmour_gordon-john_b1893` vs `Gilmour, G. J___Straits Settlements___1932`

- [PASS] surname_gate: bio 'GILMOUR' vs stint 'Gilmour, G. J' (exact)
- [PASS] initials: bio ['G', 'J'] ~ stint ['G', 'J']
- [PASS] age_gate: stint starts 1932, birth 1893 (age 39)
- [PASS] colony: 9 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1932-1936
- [PASS] position_sim: best 67 vs bar 60: 'contr' ~ 'Controller'
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

