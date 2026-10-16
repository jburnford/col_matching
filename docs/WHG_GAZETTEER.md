# WHG gazetteer: every place in the biographies

Run from the repository root:

```sh
python3 whg_fetch_wikidata.py          # once; incremental. Caches data/whg/wikidata_places.json
python3 build_whg_gazetteer.py         # → out/whg/ (ignored)
python3 build_whg_tail_review.py       # optional rare-place review packets → out/whg-tail/
python3 -m unittest discover -s tests -p 'test_whg*.py' -v
```

The build is offline. It writes a [World Historical Gazetteer](https://whgazetteer.org)
contribution covering **every location named in the career biographies** of the
Colonial Office and India Office Lists, in both upload formats:

| File | Purpose |
| --- | --- |
| `whg-places.tsv` | LP-TSV 0.5: one row per place with title, source, years, feature class, AAT type, Wikidata match, printed variants, parent, point, description |
| `whg-places.lpf.json` | Linked Places Format 1.3: same places with per-name citations (up to five editions) and timespans |
| `places.jsonl` | Full per-place record: evidence tiers, identity methods, printed toponyms, years by tier, authority dates, review issues |
| `evidence.jsonl` | One line per place mention: printed name, historical year, identity method, evidence tier, source locator (biography file/line/offsets) and every edition that printed it |
| `review.tsv` | Per-place review queue with issue codes |
| `excluded-mentions.tsv` | Every place string *not* exported, with a reason (office, campaign, generic word, unexpanded abbreviation, descriptive phrase, non-place entity) |
| `report.json` / `manifest.json` | Counts and SHA-256 fingerprints of inputs and outputs |

No people, roles, or careers appear in the TSV, LPF, or `places.jsonl`.
Evidence locators point into the biography files for audit.

## Where the places come from

The spine is the published career graphs (`data/{kg,iol}/graph_stage3/career_events.jsonl`).
Every event that names a place is resolved to exactly one outcome, in order:

1. **Graph grounding** — the event's reviewed `place_qid` (context-resolved
   homonyms such as Victoria or Perth stay as the graph resolved them).
2. **Period rules** — `config/whg_place_identities.json` maps names whose entity
   changed with time (Transvaal, Natal, Cape, South Africa, Sind, Assam, Central
   Provinces, Iraq) to the period-correct entity by event year. These are the
   mentions an earlier review nulled as "jurisdiction outside period".
3. **Surface rules** — curated aliases and OCR repairs (`Kong` → Hong Kong).
4. **Graph surface vote** — the QID the graph assigns the same printed name in
   the same corpus, when one QID has ≥80% of the votes.
5. **Grounding tables** — `data/{kg,iol}/places_grounding.jsonl`, same corpus first.
6. **Composites** — `Natal and Hong Kong`, `S.S. and F.M.S.` are split and each
   part resolved; `S. African museum, Capetown` keeps Capetown.
7. **Exclusions** — offices and departments, campaigns, generic words (`Union`,
   `various stations`), unexpanded initialisms (`N.S.`, `C.A.`), lower-case
   descriptive phrases, and graph QIDs whose Wikidata classes are organisations
   (India Office). Each is listed in `excluded-mentions.tsv`.
8. **Name-only places** — everything else becomes a place without an authority
   match (`Pusa`, `Dandagamuwa`, `Krobo`). WHG reconciliation can propose a match.

Local places (`ip-local-…`) are used where no period-correct Wikidata item
exists (Assam before the 1905 partition).

### Name-only homonyms

A name-only record takes its context from the person's nearest posting with a
colony. Contexts are grouped at country level (Wikidata P17, ignoring the UK
umbrella), so Raj provinces fold together but Crown colonies stay separate:
`St. Thomas` in Jamaica and in Barbados become two records. The context becomes
`parent_name`/`parent_id` (LPF relation `gvp:broaderPartitive`, certainty
`less-certain`), flagged `parent_inferred_from_career_context`.

## Evidence tiers

Each mention is searched in **every edition** of the person's printed biography
(the `attestations` of the structured corpus), not only the edition the model read:

- `same_clause` — the printed name and the full event year occur in one clause.
- `printed` — the name is printed but the year is not in the same clause
  (e.g. a place carried forward from an earlier clause, or an abbreviated year).
- `structured_only` — the name was not found as printed (model normalisation,
  OCR damage, or a merged-away biography).

Years in the export come from the strongest tier that has any years. Variants
and citations come only from names actually found in the text. Normalisation
ignores case and punctuation and does not expand abbreviations.

## Export decisions

- **Title**: the most-attested printed toponym (strongest tier first);
  `title_source` and `attestation_year` are the first edition that printed it
  (e.g. `Colonial Office List (1913)`, `India Office List (July 1885)`). If no
  printed form survives, the Wikidata label is used with `title_source=Wikidata`.
- **start/end**: earliest and latest dated career references to the place —
  an attestation span, not the place's lifespan. Years outside the Wikidata
  entity's inception/dissolution (±1) are kept out of the span and flagged
  `years_outside_authority_entity_dates`.
- **fclasses / aat_types / types**: from the Wikidata P31 classes; AAT IDs come
  from P1014 on the class or its nearest superclass (≤3 hops). WHG reports that
  feature classes are not yet searchable and AAT types are preferred, so both
  are given. Name-only places get a feature class from their name
  (`district` → A, `river` → H, `valley` → T, `prison` → S, else P) and are flagged.
- **Geometry**: the Wikidata P625 point (`geo_source=Wikidata`), or a curated
  point for local places. Atlas plotting seats are never used.
- **Variants**: other printed forms, cleaned of OCR edge furniture (`. Cyprus`,
  `Kedah &`), tagged `@en` (English-language usage in an English publication).
- **IDs**: `ip-Q…`, `ip-local-…`, `ip-name-…`; LPF `@id` prefixes
  `https://jimclifford.ca/col_matching/whg/places/`. Keep a crosswalk if a
  Wikidata identity is later split.

## Imperial relationship rules

`config/whg_rules.json` holds explicit entity-and-period status rules with
citations (`british_empire`, `outside_british_empire`, `mixed_or_contested`,
`unknown`). They are recorded per year in `places.jsonl`, not exported to WHG.
No status is inherited from a modern country or a graph colony label.

## Known limits

- Graph identities are the project's reviewed grounding, not independent
  verification; homonym and period errors fixed upstream flow through on rebuild.
- Name-only places have no geometry until reconciled.
- Abbreviations held as `unexpanded_abbreviation` (`N.S.`, `T.W.I.`) need a
  context-aware expansion pass before they can join the gazetteer.
- Nothing has been uploaded to WHG or run through its validator.

## Tail diagnostics and image-review handoff

```sh
python build_whg_gazetteer.py
python build_whg_tail_review.py
python -m unittest discover -s tests -p 'test_whg*.py' -v
```

The tail step defaults to **one to five place mentions per gazetteer record**
(Wikidata, local or name-only); change this with `--max-event-references`.
Mention counts include repeated and merged graph records and are not
independent witnesses. The step retains every
tail candidate, whether or not a source is retrievable. It does not modify the
gazetteer, approve an identity, or exclude a rare place.

`out/whg-tail/` contains:

| File | Purpose |
| --- | --- |
| `tail-review.tsv` | Ranked candidate-level review queue; no biographical excerpts |
| `tail-details.jsonl` | Internal source examples, date questions, and frequency diagnostics |
| `image-review-packets.jsonl` | Internal handoff with OCR excerpts, exact source hashes, page/block targets, and reviewer instructions |
| `summary.json` / `manifest.json` | Coverage, known limits, parameters, and input/output hashes |

Signals include ambiguous aliases, historical-name/OCR differences, short names,
city-versus-district mismatches, education contexts, and dates outside candidate
authority-entity bounds. These are questions, not verified errors. Historical
name differences can be correct; education can supply genuine geographic
evidence; authority dates can be wrong. No penalty is assigned simply for being
outside the British Empire or far from other places.

The pipeline deduplicates normalized source-clause signatures, so a statement
repeated across many editions is visible as repetition. Distinct signatures
are **not** a count of independent historical witnesses. Publication years,
candidate historical-year endpoints, and unverified years co-occurring in an
excerpt are stored separately. No interval is filled between endpoints.
Candidate event years not found in any retrieved name-bearing clause get an
additional support-gap flag. This can reveal location inheritance into later
clauses; it can also reflect incomplete retrieval or abbreviated dates. The
pipeline does not declare those years false or replace them automatically.

Source examples come from actual per-edition biography text and are verified
against the prior build's hashes. Each image packet checks the saved block
locator against original OCR text and bounding boxes. Entire-excerpt matches
are preferred; name-only matches remain weaker targets. Broad block lists are
condensed with original provenance counts and hashes retained. Neither form of
alignment proves that the OCR transcription is visually correct.

**Internal review files can quote personal names in brief source excerpts.**
They are separate from the public place-only contribution and remain under
ignored `out/`. Only aggregate summaries and the excerpt-free candidate queue
are included in the committed research snapshot.

### Supplying images later

Copy [`whg_image_sources.example.json`](../config/whg_image_sources.example.json)
to a local configuration and map exact OCR volume directory names to a PDF path
or page-image paths. Page keys are zero-based PDF indices, not printed page
numbers. Then run:

```sh
python build_whg_tail_review.py --image-sources /path/to/local-image-sources.json
```

This discovers configured files and prepares targets; it does not render,
crop, or visually inspect them. Do not treat OCR bounding-box units as image
pixels without verifying the coordinate space and image dimensions.

For subsequent human or model review, use
[`whg_image_review.schema.json`](../config/whg_image_review.schema.json). Record
the actual image hash, page, reviewer/model version, literal transcription,
legibility, and a separate geographic interpretation. A response must correspond
to the packet and image actually inspected. An unreadable image or ambiguous
entity should produce abstention. Schema conformance alone is not evidence that
an image was read, and reviews do not automatically change public data.

### Source images

Page images are not in this checkout. The Colonial Office OCR (`raw_ocr/json/`,
mirrored at `~/plato/colonial_office_lists/`) is of Google Books scans. Chandra 2
job scripts (`datalab-to/chandra-ocr-2`) are in `~/plato/chandra/`, but no
per-edition run log is kept with the OCR output.
India Office raw OCR is under the ignored `iol_ocr_1860-1940/` and its parsed
biographies under the ignored `data/iol/bios/`; a clone without them builds the
Colonial Office half of the evidence only.
