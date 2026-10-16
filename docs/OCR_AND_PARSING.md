# OCR models and parsing provenance

This document describes the routes represented in this repository and the
provenance needed for a historical-place contribution to WHG. OCR transcribes
the printed page; parsing turns that transcription into structured fields;
grounding proposes which geographic entity a name refers to. Errors and model
versions must be recorded separately for each stage.

## OCR: Infinity-2, Chandra 2, and the earlier olmOCR corpus

**OCR model attribution is unconfirmed.** The earlier
[public methods page](about.html) named **Chandra 2** and described execution
on the **Nibi cluster, Digital Research Alliance of Canada**. The layout reader
instead names **Infinity-2** in a comment. Chandra 2 and Infinity/Infinity-2
remain candidate attributions until original run evidence resolves the model
for each batch. The local checkout contains
downstream OCR artifacts and readers, not a complete Chandra 2 inference setup
or a per-volume model-run registry. An exact checkpoint revision, runtime,
decoding settings, image preprocessing, and job identity cannot be recovered
from the model name alone.

Infinity-2 is also named by `volume_link.py`, the volume/KG package descriptions,
and the [within-volume pilot](VOLUME_PILOT.md). These provide consistent
implementation-level attribution for the layout-aware route, but not immutable
checkpoint or per-batch execution evidence.

There are also older **olmOCR** references and a legacy markdown reader.
Do not relabel that older corpus as Chandra 2 output. In addition,
`col_match/volume/reader.py` contains an “Infinity-2” comment for the layout-aware
tree, while the earlier public methods description named Chandra 2. This is an unresolved
provenance discrepancy, not evidence that those names denote the same model.
Preserve the original artifact and recover its OCR job manifest before assigning
a checkpoint to an individual edition. The inspected Colonial Office 1913
`result.json` is a top-level page list, without top-level model/run metadata.

| OCR artifact route | Reader and segmentation | Source locator |
| --- | --- | --- |
| Layout-aware Colonial Office, Dominions Office, and Commonwealth Relations Office OCR: `raw_ocr/json/<volume>.pdf/result.json` | [`volume/reader.py`](../col_match/volume/reader.py), [`volume/bios.py`](../col_match/volume/bios.py) | Edition, document family, zero-based PDF page index, zero-based block index, bounding box |
| India Office HTML, markdown, and `<edition>_metadata.json`, normally under `iol_ocr_1860-1940/` | [`volume/iol_reader.py`](../col_match/volume/iol_reader.py), [`volume/iol_bios.py`](../col_match/volume/iol_bios.py) | Edition and HTML/text position; page estimated from page-token mass, without block bounding boxes |
| Earlier full-volume `olmocr_results.md` | [`services/corpus.py`](../col_match/services/corpus.py), [`services/segment.py`](../col_match/services/segment.py) | Volume and markdown line range |

The India Office reader establishes an artifact format, not its OCR model.
Confirm its run metadata before assigning Chandra 2 or any other checkpoint.
The raw India Office tree is ignored by Git and absent in this checkout;
published structured graph files are present. A directory name such as
`iol_ocr_1860-1940` is not a definitive statement of available publication years.

The layout reader preserves the OCR's block reading order rather than sorting
bounding boxes. Its page index is **not necessarily the printed page number**.
India Office discovery collapses alternative OCR copies of the same physical
edition but retains January/July editions as distinct sources. Its segmentation
prefers HTML paragraph/headword structure, with a markdown fallback.

## Parsing routes

### Deterministic extraction

The layout-aware biography extractor finds the services section and biography
headwords, joins continuation blocks, and preserves their source locators. The
older markdown segmenter uses the density of surname/headword-shaped lines.
The India Office extractor uses HTML headings, paragraphs, and bold headwords;
cross-reference aliases are handled separately from biographies.

[`services/rules_parse.py`](../col_match/services/rules_parse.py) extracts dated
clauses, places, and other biography fields. It handles abbreviated date ranges,
ditto forms, and repeated-location context. It can mark a place as inherited
from an earlier clause. Such a field is a parser inference, not another printed
occurrence of that name. Entries the rules cannot fully account for can be
routed to a language-model tier.

### Language-model parsing

These are **separate configured paths**, not proof that every release record
passed through every model:

| Stage | Model configuration visible in code | Implementation |
| --- | --- | --- |
| Earlier services fallback | Gemini aliases `models/gemini-flash-latest`, then `models/gemini-pro-latest` for escalation | [`services/llm_parse.py`](../col_match/services/llm_parse.py); batch responses pass validation, persistent failures are retained for review |
| Within-volume biography/roster fallback | `COL_VOLUME_LLM_MODEL`, default `qwen3.6`; OpenAI-compatible endpoint; temperature 0, default maximum 4,096 tokens | [`volume/llm.py`](../col_match/volume/llm.py); optional model calls, not required by the deterministic reader |
| Full deduplicated biography structuring | Default served alias `qwen3.6-35b-a3b`; temperature 0; thinking disabled unless requested | [`kg_structure_corpus.py`](../kg_structure_corpus.py); normalized source text, `KG_BIO_SYSTEM` plus `KEYS_SUFFIX`, resumable outputs |
| Nibi delta structuring, including an India Office repair run | Served alias `qwen3-30b-a3b`; the IOL SLURM job selects a local `qwen3-30b-a3b-fp8` model directory | [`qwen_struct_worker.py`](../nibi/qwen_struct_worker.py), [`qwen_iol_struct.slurm`](../nibi/qwen_iol_struct.slurm); worklist carries the system prompt, temperature 0, thinking disabled |

The repository also contains specialized civil-list, roster, education, and
other parsers. They are distinct extraction tasks; do not describe all of them
as one biography parser. See [the volume pilot](VOLUME_PILOT.md) and
[the KG validation loop](KG_LLM_LOOP.md).

A served alias, directory name, or `*-latest` alias is not an immutable model
revision. Preserve the resolved checkpoint and quantization from the actual
job. Temperature zero does not guarantee identical output across runtime,
hardware, model, or prompt revisions. Script defaults document reproducible
configuration choices, not the complete execution history of existing data.

### Validation, grounding, and graph emission

[`services/validate.py`](../col_match/services/validate.py) checks parsed entries
against canonical source text, including event-span alignment.
[`kg/validate.py`](../col_match/kg/validate.py) checks source-supported dates,
place tokens, ordering, and other fields; it records dropped/flagged values.
Its place check is intentionally OCR-tolerant and can accept one long matching
token. Passing that check does **not** prove geographic identity or that a
place and date belong to the same source clause.

Abbreviation normalization, context resolution, Wikidata grounding, subsequent
reviewed corrections, and graph emission follow parsing. Preserve these as
separate transformations. Merging biographies across editions does not establish
that every merged place occurs in every edition. A grounded label is not
necessarily the name printed in the historical source.

## Place-only WHG lineage

```text
Source scan/PDF
  → OCR artifact + OCR run identity
  → source-specific text/block/paragraph
  → parsed place/date candidate + parser run identity
  → geographic candidate + grounding evidence
  → dated place attestation + source locator
  → WHG export and validation
```

[`build_whg_gazetteer.py`](../build_whg_gazetteer.py) currently reads the
source-specific Colonial Office biography files and both published place/event
corpora. It separates lexical name retrieval from explicit place-and-year
source candidates. It excludes inherited places from direct evidence, keeps
publication and historical years distinct, and does not reuse atlas capital
coordinates as territory geometry. Its SHA-256 input manifest identifies the
files used, but **does not reconstruct missing upstream OCR/model provenance**.

For WHG, retain the source title/edition, scan or PDF URI, printed name, separate
historical/publication years, exact locator, and derivation chain. People are
not contribution entities. A locator may point into a biographical source
without exporting the person or their career. See
[WHG preparation](WHG_GAZETTEER.md) for evidence tiers and current limitations.

## Model/run metadata to preserve

Use [`ocr_run_manifest.example.json`](../config/ocr_run_manifest.example.json)
as a capture template for each OCR run and its downstream parser runs. It is
an **unfilled example**, not a manifest for existing artifacts. Record:

- Scan/PDF identity, edition, source URI, file hash, and actual page coverage.
- OCR model/checkpoint revision, processor/tokenizer revision, runtime versions,
  preprocessing, decoding options, hardware, and scheduler job/log references.
- Parser entry point and code commit; rules version or resolved model revision;
  full prompt hash and generation settings; normalization and validation version.
- Input/output hashes, error/retry counts, and the source-locator convention.

Unknown fields should remain explicitly unknown. Recover old job logs and
manifests where available; avoid backfilling current model defaults as historical
run facts. Keep transcription accuracy, parsing accuracy, and geographic
resolution accuracy as separate evaluation results, with sample and method.
