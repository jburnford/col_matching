<!-- {"case_id": "case_dalley_john-douglas_b1900", "bio_ids": ["dalley_john-douglas_b1900"], "stint_ids": ["Dalley, J. D___Straits Settlements___1936"]} -->
# Dossier case_dalley_john-douglas_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dalley_john-douglas_b1900`

- Printed name: **DALLEY, JOHN DOUGLAS**
- Birth year: 1900 (attested in editions [1936, 1940])
- Appears in editions: [1936, 1937, 1940, 1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1936-L60094.v` — printed in editions [1936, 1940]:**

> DALLEY, JOHN DOUGLAS.—B. 1900; pol. probr., F.M.S., Nov., 1920, probry. a.c.p., Jan., 1922; on depm. to Kedah; a.c.p., Nov., 1923; lst a.c.p., Selangor, Dec., 1924; c.p.o., Johore S., Apr., 1926; a.c.p., K. Kangar, June, 1931; a.c.p., S'pore, Sept., 1932; comdt., pol. depot, Nov., 1933; dep. comsrr., pol., F.M.S., Aug., 1934; comsrr., pol., Trengganu, Oct., 1936; title changed to supt., July, 1938.

**Version `col1937-L60150.v` — printed in editions [1937]:**

> DALLEY, JOHN DOUGLAS.—B. 1900; POL. PROBR., F.M.S., NOV., 1920; PROBRY, A.C.P., JAN., 1922; ON DEPN. TO KEDAH; A.C.P., NOV., 1923; LAT. A.C.P., SELANGOR, DEC., 1924; C.P.O., JOHORE S., APR., 1926; A.C.P., K. KANGAR, JUNE, 1931; A.S.P., S'PORE, SEPT., 1932; COMDT., POL. DEPOT, NOV., 1933; DEP. COMSR., POL., F.M.S., AUG., 1934.

**Version `col1948-L32096.v` — printed in editions [1948, 1949]:**

> DALLEY, John Douglas.—b. 1900; police prob., F.M.S., 1920; supt. of police, 1938; dir. of Mal. security serv. (pan-Malayan), 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | pol. probr. | Federated Malay States | [1936, 1937, 1940, 1948, 1949] |
| 1 | 1922 | probry. a.c.p. | — | [1936, 1937, 1940] |
| 2 | 1923 | a.c.p. | — | [1936, 1937, 1940] |
| 3 | 1924 | lst a.c.p. | Selangor | [1936, 1940] |
| 4 | 1924 | LAT. A.C.P., SELANGOR, DEC | — | [1937] |
| 5 | 1926 | c.p.o. | Johore | [1936, 1937, 1940] |
| 6 | 1931 | a.c.p. | — | [1936, 1937, 1940] |
| 7 | 1932 | a.c.p. | Singapore | [1936, 1940] |
| 8 | 1932 | A.S.P., S'PORE, SEPT | — | [1937] |
| 9 | 1933 | comdt., pol. depot | — | [1936, 1937, 1940] |
| 10 | 1934 | dep. comsrr., pol. | Federated Malay States | [1936, 1940] |
| 11 | 1934 | DEP. COMSR., POL., F.M.S., AUG | — | [1937] |
| 12 | 1936 | comsrr., pol. | Trengganu | [1936, 1940] |
| 13 | 1938 | supt. | Federated Malay States *(inherited from previous clause)* | [1936, 1940, 1948, 1949] |
| 14 | 1946 | dir. of Mal. security serv. (pan-Malayan) | Federated Malay States *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Dalley, J. D___Straits Settlements___1936`

- Staff-list name: **Dalley, J. D** | colony: **Straits Settlements** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. D. Dalley | Superintendent (Commandant Depot) | Police | — | — |
| 1939 | J. D. Dalley | Superintendent | Police | — | — |

### Deterministic checks: `dalley_john-douglas_b1900` vs `Dalley, J. D___Straits Settlements___1936`

- [PASS] surname_gate: bio 'DALLEY' vs stint 'Dalley, J. D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

