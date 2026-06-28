#!/usr/bin/env bash
# Re-emit a corpus's KG after a merge-map change (school-blocked dedup).
# Usage: bash reemit_dedup.sh <co|iol>
# Chain: apply merge map -> emit spine -> overlay emits (roles/org/honours/
# career_facts) -> remap MCP-grounded layers (education_edges, grounding) ->
# re-emit spine (re-attach remapped grounding) -> dedup node variants.
#
# CAVEAT: kg_remap_edge_layers.py mutates education_edges + person_grounding.final
# IN PLACE. That is idempotent for a FIXED merge map, but if you CHANGE the map and
# re-run, first restore those two files from a pre-dedup backup (else a prior run's
# remap is baked in). See data/_backup_*/.
set -euo pipefail
corpus="${1:?usage: reemit_dedup.sh <co|iol>}"

if [ "$corpus" = co ]; then
  export COL_KG_OUT=data/kg
  SPINE=data/kg/llm_struct_corpus.stage3.jsonl
  python3 kg_dedup_stage3_apply.py \
    --corpus data/kg/llm_struct_corpus.reviewed.jsonl \
    --map data/kg/dedup_stage3_merge_map.school.jsonl --out "$SPINE"
elif [ "$corpus" = iol ]; then
  export COL_KG_OUT=data/iol
  SPINE=data/iol/llm_struct_corpus.stage3.deduped.jsonl
  COL_PROV=data/iol/persons.deduped.jsonl python3 kg_dedup_stage3_apply.py \
    --corpus data/iol/llm_struct_corpus.valid.jsonl \
    --map data/iol/dedup_stage3_merge_map.school.jsonl --out "$SPINE"
else
  echo "unknown corpus: $corpus"; exit 1
fi

echo "── emit spine ($COL_KG_OUT)"
python3 kg_emit_stage3.py --corpus "$SPINE"
echo "── overlay emits"
python3 kg_emit_roles.py        >/dev/null
python3 kg_emit_org.py          >/dev/null
python3 kg_emit_honours.py      >/dev/null
python3 kg_emit_career_facts.py >/dev/null
echo "── remap MCP-grounded layers (education_edges, grounding)"
python3 kg_remap_edge_layers.py
echo "── re-emit spine (re-attach remapped grounding)"
python3 kg_emit_stage3.py --corpus "$SPINE" >/dev/null
echo "── dedup node variants"
python3 kg_dedup_nodes.py       >/dev/null
echo "── orphan check"
python3 - <<'PY'
import json, os
GD = os.environ["COL_KG_OUT"] + "/graph_stage3"
pers = {json.loads(l)["person_id"] for l in open(GD + "/persons.jsonl")}
for f in ("role_edges", "employment_edges", "honour_edges", "qualification_edges",
          "career_facts", "education_edges", "person_grounding.final"):
    p = f"{GD}/{f}.jsonl"
    if os.path.exists(p):
        ids = {json.loads(l)["person_id"] for l in open(p)}
        print(f"   {f}: orphans {len(ids - pers)}")
g = sum(1 for l in open(GD + "/persons.jsonl") if json.loads(l).get("wikidata_qid"))
print(f"   persons {len(pers)}  grounded {g}")
PY
