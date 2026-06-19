<!-- {"case_id": "case_alabaster_chaloner-grenville_b1880", "bio_ids": ["alabaster_chaloner-grenville_b1880"], "stint_ids": ["Alabaster, C. G___Hong Kong___1930"]} -->
# Dossier case_alabaster_chaloner-grenville_b1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Alabaster, C. G___Hong Kong___1930` is also gate-compatible with biography(ies) outside this case: ['alabaster_chaloner-grinnell_b1880'] (already linked elsewhere or filtered).

## Biography `alabaster_chaloner-grenville_b1880`

- Printed name: **ALABASTER, Chaloner Grenville**
- Birth year: 1880 (attested in editions [1948, 1950, 1951])
- Honours: K.C. (1922), Kt. Bach. (1942), O.B.E. (1918)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L30748.v` — printed in editions [1948, 1950, 1951]:**

> ALABASTER, Sir Chaloner Grenville, Kt. Bach. (1942), O.B.E. (1918), K.C. (1922).—b. 1880; ed. Tonbridge; barrister-at-law (Inner Temple, 1904); ag. atty.-gen., H. Kong, 1911, 1912, 1928, 1930; confirmed in appt., 1931; ag. ch. just., 1937; attached leg. advisory staff C.O., Aug. to Sept., 1934; interned 1942-45; edtr., Laws of Hong Kong, 1844-1912.

**Version `col1949-L29991.v` — printed in editions [1949]:**

> ALABASTER, Sir Chaloner Grenville, Kt. Bach (1942), O.B.E. (1918), K.C. (1922)—b. 1880; ed. Tonbridge; barrister-at-law (Inner Temple, 1904); atty. gen., H.K. ALCOCK; Rowland Newman.—b. 1912; ed. Highwood Prep. Sch., Mill Hill, Highbury Sch., King Ed. VII Nautical Sch., and Met. Police Coll., Hendon; met. police, 1935; col. service, 1938; senr. asst. supt., police, Nig., 1947; seconded to S.L. as asst. supt. 1943–44; compiled police instruc. book (S.L.).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904–1904 | barrister-at-law | — | [1948, 1949, 1950, 1951] |
| 1 | 1911–1930 | ag. atty.-gen. | Hong Kong | [1948, 1950, 1951] |
| 2 | 1912 | Rowland Newman.—b | — | [1949] |
| 3 | 1931–1931 | confirmed in appt. | — | [1948, 1950, 1951] |
| 4 | 1934–1934 | attached leg. advisory staff | Colonial Office | [1948, 1950, 1951] |
| 5 | 1935 | met. police | — | [1949] |
| 6 | 1937–1937 | ag. ch. just. | — | [1948, 1950, 1951] |
| 7 | 1938 | col. service | — | [1949] |
| 8 | 1942–1945 | interned | — | [1948, 1950, 1951] |
| 9 | 1943–1944 | seconded to S.L. as asst. supt | Nigeria *(inherited from previous clause)* | [1949] |
| 10 | 1947 | senr. asst. supt., police | Nigeria | [1949] |

## Candidate stint `Alabaster, C. G___Hong Kong___1930`

- Staff-list name: **Alabaster, C. G** | colony: **Hong Kong** | listed 1930–1939 | editions [1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | C. G. Alabaster | Assistant to Attorney-General | Law Officers | — | — |
| 1931 | C. G. Alabaster | Attorney-General | Law Officers | — | — |
| 1932 | C. G. Alabaster | Attorney-General | Law Officers | — | — |
| 1933 | C. G. Alabaster | Attorney-General | Law Officers | — | — |
| 1934 | C. G. Alabaster | Attorney-General | Law Officers | — | — |
| 1936 | C. G. Alabaster | Attorney-General | Law Officers | — | — |
| 1937 | C. G. Alabaster | Attorney-General | Law Officers | — | — |
| 1939 | C. G. Alabaster | Attorney-General | Law Officers | — | — |

### Deterministic checks: `alabaster_chaloner-grenville_b1880` vs `Alabaster, C. G___Hong Kong___1930`

- [PASS] surname_gate: bio 'ALABASTER' vs stint 'Alabaster, C. G' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1930, birth 1880 (age 50)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1939
- [FAIL] position_sim: best 56 vs bar 60: 'ag. atty.-gen.' ~ 'Attorney-General'
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

