"""Services-section pipeline: parse the printed "Record of Services"
biographical sections from the raw olmOCR Colonial Office List corpus into
per-official biographies with per-edition provenance.

See docs/approach.md (Phase 1) and the approved plan. Outputs are files under
data/services/ — this subpackage never writes to the production graph.
"""
