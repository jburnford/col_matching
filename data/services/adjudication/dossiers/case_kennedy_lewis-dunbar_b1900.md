<!-- {"case_id": "case_kennedy_lewis-dunbar_b1900", "bio_ids": ["kennedy_lewis-dunbar_b1900"], "stint_ids": ["Kennedy, L. D___Sarawak___1940"]} -->
# Dossier case_kennedy_lewis-dunbar_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 63 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kennedy_lewis-dunbar_b1900`

- Printed name: **KENNEDY, Lewis Dunbar**
- Birth year: 1900 (attested in editions [1949, 1950, 1951, 1953, 1954, 1955])
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1949-L33406.v` — printed in editions [1949, 1950, 1951, 1953, 1954, 1955]:**

> KENNEDY, Lewis Dunbar.—b. 1900; ed. High Sch., Wick, and Sutherland Tech. Sch., Golspie; on mil. serv., 1917-19; asst. supt., customs, Sarawak, 1926; supt., 1926; comsnr., trade and customs, 1939; civ. intern., 1941-45.

**Version `col1948-L33791.v` — printed in editions [1948]:**

> KENNEDY, Lewis Dunbar.—b. 1900; ed. Sutherland Tech. Sch., Golspie, High Sch., Wick; on mil. serv. 1917-19; supt. of customs, Sarawak, 1926; comsnr. of trade and customs, superscale "B," 1939; superscale "A," 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. supt., customs | Sarawak | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1939 | comsnr., trade and customs | Sarawak *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1941–1945 | civ. intern | Sarawak *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954, 1955] |
| 3 | 1946 | superscale "A," | Sarawak *(inherited from previous clause)* | [1948] |

## Candidate stint `Kennedy, L. D___Sarawak___1940`

- Staff-list name: **Kennedy, L. D** | colony: **Sarawak** | listed 1940–1954 | editions [1940, 1948, 1949, 1950, 1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | L. D. Kennedy | Commissioner of Trade and Customs | Civil Establishment | — | — |
| 1948 | L. D. Kennedy | Supreme Council Member | Supreme Council | — | — |
| 1949 | L. D. Kennedy | Commissioner of Trade and Customs | Trade and Customs | — | — |
| 1950 | L. D. Kennedy | Commissioner of Trade and Customs | TRADE AND CUSTOMS | — | — |
| 1951 | L. D. Kennedy | Commissioner of Trade and Customs | Trade and Customs | — | — |
| 1952 | L. D. Kennedy | Commissioner of Trade and Customs | Civil Establishment | — | — |
| 1953 | L. D. Kennedy | Commissioner of Trade and Customs | Civil Establishment | — | — |
| 1954 | L. D. Kennedy | Commissioner of Trade and Customs | Civil Establishment | — | — |

### Deterministic checks: `kennedy_lewis-dunbar_b1900` vs `Kennedy, L. D___Sarawak___1940`

- [PASS] surname_gate: bio 'KENNEDY' vs stint 'Kennedy, L. D' (exact)
- [PASS] initials: bio ['L', 'D'] ~ stint ['L', 'D']
- [PASS] age_gate: stint starts 1940, birth 1900 (age 40)
- [PASS] colony: 4 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1940-1954
- [PASS] position_sim: best 84 vs bar 60: 'comsnr., trade and customs' ~ 'Commissioner of Trade and Customs'
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

