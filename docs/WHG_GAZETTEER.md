# Place-only WHG preparation

Run from the repository root:

```sh
python build_whg_gazetteer.py
python -m unittest discover -s tests -p test_whg_gazetteer.py -v
```

The default output directory is `out/whg/` (ignored by Git). This is an offline
preparation pipeline; it does not contact WHG or publish anything. Inputs and
outputs have SHA-256 fingerprints. An unchanged rerun reuses intact artifacts;
changed inputs or damaged outputs trigger a rebuild. Use `--force` to rebuild.

## Scope and evidence

The contribution is places and years. There are no person records, personal
identifiers, role fields, appointments, or career networks in its outputs.
Internal source file/line and event-index locators allow an auditor to retrieve
the original passage. They refer to historical biographical sources, but those
biographies are not copied into the export.

For the upstream models and transformations, see
[OCR and parsing provenance](OCR_AND_PARSING.md), including the reported
Chandra 2 OCR, legacy olmOCR route, deterministic parsing, and Qwen/Gemini
model configurations. The WHG build's file hashes do not substitute for missing
OCR checkpoint and parser-run metadata.

Existing grounded place tables provide **candidate identities**, not a validated
gazetteer. Identical Wikidata IDs are provisionally grouped across both corpora;
incorrect conflations must be corrected upstream before a release. IDs use
`imperial-places:Q…`; preserve an ID crosswalk if identities are later split.

The pipeline keeps three evidence levels separate:

1. **Merged event candidates:** existing explicit `place_qid` and discrete start
   years. No fallback to `colony_qid`, which can be inferred or inconsistent.
2. **Name occurrences:** a token-based multi-pattern matcher scans source text
   once using the place-name vocabulary. These are retrieval candidates only:
   Victoria or Washington may refer to a person, not a location. Source character
   offsets recover the exact original string. No historical year is inferred.
3. **Explicit place/year source candidates:** a source-specific parsed event must
   have a non-inherited place, a full historical year no later than the edition,
   and a passage corroborated in raw text containing both. Normalization ignores
   case/punctuation, preserves word boundaries, and does not expand abbreviations.
   The printed place must map to one candidate QID in that corpus. This supports
   the extraction; it does not independently establish geographic identity.

Only the third level supplies the initial WHG preview. Publication years and
historical years remain separate. Earliest/latest mentions never become an
asserted place lifespan, and gaps are not filled. Missing raw India Office
biographies are reported rather than replaced with merged edition lists.

Place types are proposals derived from existing labels. Multiple competing
classes remain unresolved. Geometry is deliberately absent: atlas capital and
regional plotting points are not automatically valid gazetteer geometries.

## Outputs

| File | Purpose |
| --- | --- |
| `places.jsonl` | One candidate per QID, discrete years, variants, status rules, source examples, and issues |
| `evidence.jsonl` | Streaming source ledger with separate evidence tiers, dates, and locators |
| `review.tsv` | One row per candidate identity, with counts, issue codes, and a priority score |
| `review-groups.json` | Issue-based queues ordered by affected evidence/event counts |
| `unresolved-names.json` | Unmapped or ambiguous explicit names grouped across repeated passages |
| `whg-preview.tsv` | LP-TSV-shaped preview of directly corroborated names with proposed types |
| `whg-ready.tsv` | The subset with explicit identity approval and type decisions |
| `report.json` | Coverage, exclusion counts, and limitations |
| `manifest.json` | Reproducibility fingerprints |

The simple TSV uses a real source publication year for its selected title. The
ledger preserves all source and historical years. Variants use `@und` because
the language of a name is not inferred merely from the language of the book.
Names containing TSV structural characters or obvious stray quote/bracket
delimiters are held back from the table but retained verbatim in the evidence.
Clean variants for the same place remain eligible. Rich per-name dates,
source citations, and imperial relationships need a subsequent Linked Places
JSON mapping; these sidecars must not be discarded when preparing that release.
Neither preview nor ready output is claimed to have passed WHG's online validator.

## Imperial relationship rules

`config/whg_rules.json` holds explicit entity-and-period rules with citations.
Allowed statuses are `british_empire`, `outside_british_empire`,
`mixed_or_contested`, and `unknown`. Unmatched years remain unknown. Conflicting
rules produce mixed/contested status. Rule application to merged candidate years
is explicitly separate from application to corroborated historical years.

The seed rule classifies Washington, DC (`Q61`) as outside the British Empire
for 1801–1966, based on its US federal-capital status documented by the
[National Archives](https://www.archives.gov/research/district-of-columbia).
These are deliberately bounded operational dates, not a founding/dissolution
claim. The rule does not resolve the identity of every printed “Washington.”
No status is inherited from a present-day country or a graph colony label.
Metropolitan Britain, dominions, mandates, protectorates, and disputed periods
need a documented classification policy before expanding the rule table.

## Approval and reducing review at scale

`place_decisions` starts empty. An identity decision can be recorded as:

```json
{
  "Q61": {
    "approved": true,
    "evidence": "URI or local audit record of an independent identity check",
    "fclass": "P",
    "title": "Washington"
  }
}
```

This is an example, not a pre-approved decision. A chosen title must occur in
direct source evidence. Approval alone cannot manufacture missing source data.
Imperial status may remain unknown without blocking a useful place record.

The first pass intentionally does **not** auto-approve the existing Wikidata
grounding. A scalable next stage should:

1. Retrieve authority candidates once per identity/name/context group, caching
   request, response, service version, and source lineage. WHG/Wikidata agreement
   is not independent corroboration if both derive from the same data.
2. Resolve retrieved passages using geographic context and entity type, including
   person-name versus place-name ambiguity. A language model may propose the
   interpretation, but must return source offsets and candidate IDs; unsupported
   names, dates, or citations fail deterministic checks.
3. Calibrate automatic acceptance on a stratified historical-geography sample;
   separately measure identity, date-linkage, and source precision. Keep a held-out
   set and audit a random sample of automatically accepted cases.
4. Save accepted decisions and scoped reusable rules. Rerun only affected groups
   in a later incremental implementation. The current cache works per complete
   build, not per claim or remote API request.
5. Review high-impact ambiguous groups and a random accepted sample near release,
   rather than inspecting every mention. Existing temporal flags are candidates,
   not verified errors; the pipeline groups the saved screen by place identity.

The present implementation supplies extraction, retrieval, provenance, grouping,
and export safeguards. Authority reconciliation, calibrated automatic acceptance,
complete imperial-status coverage, source recovery for India Office records,
and the rich Linked Places export remain additional stages.

## Tail diagnostics and image-review handoff

```sh
python build_whg_gazetteer.py
python build_whg_tail_review.py
python -m unittest discover -s tests -p 'test_whg*.py' -v
```

The tail step defaults to **one to five structured event references per QID**;
change this with `--max-event-references`. Event counts include repeated and
merged graph records and are not independent witnesses. The step retains every
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

### Current environment limits

The checked workspace has Colonial Office OCR JSON and source biographies but
no source PDFs/page images, no raw India Office HTML/markdown tree, and no
upstream OCR execution manifests. Visual transcription, full India Office
source verification, and attribution of OCR batches to Chandra 2 versus
Infinity/Infinity-2 remain blocked by those missing artifacts. Existing local
authority caches supply screening questions; calibrated independent authority
reconciliation and rich Linked Places export are still additional stages.

The committed [16 October preparation snapshot](../research/whg-preparation-2026-10-16/README.md)
contains aggregate results, an excerpt-free tail queue, and reproduction hashes.
