# Grounding institutions (education first, then employers/orgs) — resumable loop

Goal: ground the **count≥2 head** (~1,757 institutions, ~88% of education mentions)
to Wikidata QIDs via MCP vector search; everyone sharing an ungrounded
institution still links via a minted **internal id** `colkg:<Slug>`.

## State
- Worklist: `data/kg/education_worklist.jsonl` (4,983 distinct, 27,238 mentions;
  rebuild: `python3 kg_education_worklist.py`).
- Cache: `data/kg/institutions_grounding.jsonl` (keyed by `institution` surface).
- count==1 tail (3,211) already minted internal ids (`internal-tail --max-count 1`).
- Wikidata-grounded so far: 15 (Univ London/Edinburgh/Cambridge/Glasgow/Oxford/
  Aberdeen-pending, Trinity Dublin/Cambridge, 4 Inns of Court, King's London,
  New College/Brasenose/Balliol Oxford) — already 4,408 mentions.

## Batch = 250 institutions per session
One batch grounds the next **250** count-desc institutions (≈50 assistant
messages × 5 MCP calls — the rate limit). At ~1,757 head institutions, that's
~7 batches. After each batch: `stats`, then `record` is already persisted to the
on-disk cache (survives /clear); optionally `git add -f` the cache for backup.
Resume prompt: **"Ground the next 250 institutions — follow docs/GROUND_INSTITUTIONS.md"**.

## Four dispositions per surface (decide BEFORE spending an MCP call)
- **mcp** — a real Wikidata entity exists for THIS surface → QID, `source:"mcp"`.
- **reuse (abbrev_variant)** — surface is an abbreviation/spelling variant of an
  ALREADY-grounded QID ("Imp. College"→Q189022, "Chelt. College"→Q467269,
  "Geo. Watson's"→Q3760670, "R. School of Mines"→Q1508631, "...Camb./Oxon" parented
  forms) → reuse that QID, ZERO MCP cost, `source:"reuse"`.
- **internal** — ONE real institution lacking a findable Wikidata entity (local
  colonial/grammar school: Grey College Bloemfontein, Wolmer's, Cornwall College Jca;
  or an org like Ceylon Police) → `colkg:<Slug>`.
- **ambiguous** — BARE unparented multi-referent surface (see Disambiguation notes) →
  `kg_ground_institutions.py ambiguous -`, NOT internal-minted.

## Loop (≤5 MCP calls per assistant message — rate limit)
0. **Reuse pre-pass (no MCP):** dump `pending --n 60`, eyeball for abbreviation/variant
   forms of QIDs already in the cache and `record` them with `source:"reuse"`. Also
   triage bare-vs-parented: parented/place-cued → ground; bare multi-referent →
   `ambiguous`. This clears a big share of each batch before any MCP call.
1. `python3 kg_ground_institutions.py pending --n 15` → top uncached, count-desc.
2. MCP `search_items` each (bare name first; the endpoint is INTERMITTENT —
   descriptive queries often return empty, retry bare; whole batches sometimes
   need a retry pass). Pick the QID whose description is the educational
   institution (university/college/school/Inn), NOT a building/boat-club/painting.
3. Write rows to a tmp jsonl and `record`:
   `{"institution":<surface>,"type":..,"id":"Q..","label":..,"instance_of":[..],"country_qid":..,"source":"mcp","match_type":"mcp_verified"}`
4. If no real Wikidata entity exists → `internal` (single referent) or `ambiguous`
   (bare multi-referent). `echo "Ceylon Police" | python3 kg_ground_institutions.py internal -`
5. Repeat. `stats` for coverage. Every ~10 batches, eyeball the cache for
   wrong-type grabs (building/journal/boat-club QIDs).

## Disambiguation notes
- **Bare, unparented college/school surfaces are MULTI-REFERENT — do NOT internal-mint
  them** (a single `colkg:` node would false-merge distinct institutions, same harm as a
  wrong QID). Mark them ambiguous instead:
  `printf "St. John's College\nKing's College\n" | python3 kg_ground_institutions.py ambiguous -`
  → `id:null, source:"ambiguous"`, EXCLUDED from emit, queued for a future per-mention
  context-disambiguation pass (resolve each mention by its surrounding location cue).
  Verified multi-referent in-corpus (scan education strings for location cues):
  St. John's College (Cambridge/Jo'burg/Belize/Hurstpierpoint/York/Winnipeg…),
  King's College (London/Cambridge — rarely Toronto, those default to "University of
  Toronto"), Queen's College, King's School, Trinity College (Dublin 268/Camb 221/Oxf 89),
  Christ's College (Camb 118 but NZ 13), Victoria College (Stellenbosch 55/Jersey 26),
  St. Mary's College (Trin 64 but Dublin/Toronto/Camb), St. Andrew's College
  (Grahamstown 20/Dublin 19), St. Joseph's College (HK/Mauritius/Dublin),
  King Edward's School (B'ham but unqualified), King Edward VI School, Royal School,
  London School, Wales School, Tech. College, C.M.S. School.
  Heuristic: people DO write the parented/main-university form when they mean a specific
  one ("St. John's College, Cambridge", "University of Toronto") — so a BARE surface that
  survives is genuinely the ambiguous residue. Ground only the parented surfaces.

### Per-mention disambiguation pass — parsing rules (TODO, for the ambiguous residue)
- **Distributed "Univs." rule (Jim, 2026-06-23):** a trailing PLURAL "Univs." (or
  "Univs", "universities") distributes back over the preceding comma-separated tokens.
  `"St. Andrews, Camb., and Edin. Univs."` = the *Universities* of St Andrews (Scotland
  Q216273) + Cambridge + Edinburgh — NOT a college, even though no "university" word is
  adjacent to "St. Andrews". Must parse the list tail before bucketing a token as
  school-vs-university.
- **"university" vs "college" word disambiguates the saint-name**, but only after the
  distributed-Univs expansion: "St Andrews university"→Scotland; "St Andrew's College"→
  SA(Grahamstown ~43)/Dublin(~22), never Scotland; "St Andrew's School"→Rothesay(Scot)/
  Bloemfontein(SA)/Oyo(Nigeria)/Eastbourne/Alexandria/Singapore (highly multi).
- **Location cue resolves the rest:** Grahamstown→SA, Dublin/Booterstown→IRL, Jo'burg/
  Witwatersrand→ZA, Belize→BZ, Hurstpierpoint→Sussex, etc. ~67/75 of bare "St Andrew's
  College" resolve by cue. Parented forms ("..., Dublin") ground directly now.
- **The univ marker is NOT always present** (measured on 133 "St. Andrews" mentions:
  70% adjacent "univ", 5% distributed "Univs.", 3% degree-marker, 23% naked — and most
  "naked" carry a location/college cue instead). So the per-mention resolver chains
  signals in PRIORITY ORDER: (1) adjacent "univ/university", (2) distributed "Univs."
  across the comma-list, (3) degree marker `M.A./B.Sc./M.D./D.D./LL.B (St Andrews)`,
  (4) location cue (`college, Grahamstown`). Only a handful have zero signal → true
  residue. This 4-ladder logic is why bare surfaces are flagged, not force-grounded:
  one surface node can't climb the ladders, a per-mention pass can.
- "Royal College" = real colonial schools "Royal College, Mauritius / Colombo" —
  ground per location or mint `colkg:Royal_College_Mauritius` etc.
- Inns of Court, universities, Oxbridge colleges, Sandhurst/Woolwich, famous
  public schools all HAVE QIDs — ground them; the long tail of local grammar
  schools mostly won't (internal ids).

## Then
- `python3 kg_ground_institutions.py emit` → `graph_stage3/institutions.jsonl`
  (nodes) + `education_edges.jsonl` (person→institution).
- NEXT entity class after education = **employer/org institutions** (the 3,488
  ungrounded `org` event places: railways, police, departments) — same harness,
  same internal-id scheme (Ceylon Police → `colkg:Ceylon_Police`).
