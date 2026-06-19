"""Knowledge-graph extraction FROM the Colonial Office List biographies.

Goal: the best-possible grounded person-career graph built from the services-
section biographies of the new (Infinity-2) OCR, independent of the staff-list
linking work (deferred). Pipeline:

  discover (volume.reader/bios) -> cluster persons across editions (persons)
  -> normalize + tag (normalize) -> LLM structure pass (extract, via volume.llm)
  -> validate (validate) -> ground places to Wikidata (ground) -> resolve the
  historical colony via the empire-evolution-wpcs KG (colony) -> emit JSONL
  node/edge tables (emit).

Every fact carries (edition_year, page, block, bbox) provenance back to the raw
OCR. Places are GROUNDED to Wikidata QIDs, never guessed; colony is left null
when no period-valid polity resolves (uneven coverage is acceptable).
"""
