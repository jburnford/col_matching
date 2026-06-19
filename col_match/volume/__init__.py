"""Within-volume bio↔roster linking on the new (Infinity-2) Colonial Office
List OCR.

A self-contained pilot, deliberately isolated from the old cross-edition
``col_match.services`` pipeline. One edition's ``result.json`` (page → blocks
``{bbox, category, text}``) is read once (reader), split into bbox-grounded
services-section biographies (bios) and by-colony staff-list records (roster),
then linked within that single volume (match). Everything carries a provenance
key ``(edition_year, page, block_index, bbox)`` back to the raw OCR.
"""
