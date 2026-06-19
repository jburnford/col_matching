<!-- {"case_id": "case_dannatt_robert-malcolm_b1891", "bio_ids": ["dannatt_robert-malcolm_b1891"], "stint_ids": ["Dannatt, R. M___Straits Settlements___1931"]} -->
# Dossier case_dannatt_robert-malcolm_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dannatt_robert-malcolm_b1891`

- Printed name: **DANNATT, Robert Malcolm**
- Birth year: 1891 (attested in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: M.B
- Appears in editions: [1932, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L59509.v` — printed in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940]:**

> DANNATT, Robert Malcolm, M.B., B.S. (Lond.), F.R.C.S. (Eng.), L.R.C.P. (Lond.), F.R.C.S. (Edin.).—B. 1891; med. offr., F.M.S., Oct., 1925; surgn., F.M.S., Mar., 1926; do., Selangor, Nov., 1933; ag. senr. surg., S'pore, Aug., 1935; res. surg., col. hosp., Grenada, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | med. offr. | Federated Malay States | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1926 | surgn. | Federated Malay States | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1933 | do., Selangor | Federated Malay States *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1935 | ag. senr. surg., S'pore | Federated Malay States *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1937 | res. surg., col. hosp. | Grenada | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Dannatt, R. M___Straits Settlements___1931`

- Staff-list name: **Dannatt, R. M** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1932, 1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. M. Dannatt | Surgeon | Medical | — | — |
| 1932 | R. M. Dannatt | Surgeon | Medical | — | — |
| 1933 | R. M. Dannatt | Surgeon | Medical | — | — |
| 1936 | R. M. Dannatt | Senior Surgeon | Medical | — | — |

### Deterministic checks: `dannatt_robert-malcolm_b1891` vs `Dannatt, R. M___Straits Settlements___1931`

- [PASS] surname_gate: bio 'DANNATT' vs stint 'Dannatt, R. M' (exact)
- [PASS] initials: bio ['R', 'M'] ~ stint ['R', 'M']
- [PASS] age_gate: stint starts 1931, birth 1891 (age 40)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1936
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

