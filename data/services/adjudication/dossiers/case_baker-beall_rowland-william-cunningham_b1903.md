<!-- {"case_id": "case_baker-beall_rowland-william-cunningham_b1903", "bio_ids": ["baker-beall_rowland-william-cunningham_b1903"], "stint_ids": ["Baker-Beall, R. W. C___Kenya___1937"]} -->
# Dossier case_baker-beall_rowland-william-cunningham_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `baker-beall_rowland-william-cunningham_b1903`

- Printed name: **BAKER-BEALL, Rowland William Cunningham**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Honours: M.B.E
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L30947.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> BAKER-BEALL, Rowland William Cunningham, M.B.E.—b. 1903; ed. Sherborne Sch., Dorset and Worcester Coll., Oxford, B.A. (Oxon.); admin. offr., Ken., 1927; fin. sec., Zanz., 1942; dep. fin. sec., Nig., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | admin. offr. | Kenya | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1942 | fin. sec. | Zanzibar | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1947 | dep. fin. sec. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Baker-Beall, R. W. C___Kenya___1937`

- Staff-list name: **Baker-Beall, R. W. C** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | R. W. C. Baker-Beall | Clerk to Legislative Council | Secretariat | — | — |
| 1939 | R. W. C. Baker-Beall | Clerk to Legislative Council | Secretariat | — | — |
| 1940 | R. W. C. Baker-Beall | District Officers | Provincial Administration | — | — |

### Deterministic checks: `baker-beall_rowland-william-cunningham_b1903` vs `Baker-Beall, R. W. C___Kenya___1937`

- [PASS] surname_gate: bio 'BAKER-BEALL' vs stint 'Baker-Beall, R. W. C' (exact)
- [PASS] initials: bio ['R', 'W', 'C'] ~ stint ['R', 'W', 'C']
- [PASS] age_gate: stint starts 1937, birth 1903 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 52 vs bar 60: 'admin. offr.' ~ 'District Officers'
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

