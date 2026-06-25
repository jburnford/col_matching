# LadybugDB (Cypher) graph database

`kg_load_ladybug.py` builds the v3 knowledge graph into an embedded **LadybugDB**
database (a community fork of KuzuDB — embedded, columnar, Cypher) at
`data/kg/ladybug_db`.

```bash
python3 -m pip install --break-system-packages ladybug pandas pyarrow   # ladybug == LadybugDB
python3 kg_load_ladybug.py            # rebuilds data/kg/ladybug_db from the graph_stage3 jsonl
```

The DB (~70 MB) is a **regenerable build artifact** — it is gitignored, not
committed. Rebuild it from the committed jsonl any time.

## Graph model (reified career events)

Career events are reified as their own nodes so person / role / org / place are
all independently traversable:

```
(Person)-[:HAS_EVENT]->(CareerEvent)-[:EVENT_ROLE]->(Role)
                        (CareerEvent)-[:EVENT_ORG]->(Organisation)
                        (CareerEvent)-[:EVENT_PLACE]->(Place)
                        (CareerEvent)-[:EVENT_COLONY]->(Place)
(Person)-[:RECEIVED]->(Honour)            // person-level
(Person)-[:HOLDS_QUAL]->(Qualification)
(Person)-[:EDUCATED_AT]->(Institution)
```

CareerEvent carries `year_start, year_end, is_acting, position_raw`. Every grounded
node (Role/Organisation/Institution/Honour/Qualification) keys on its `id` =
Wikidata QID or `colkg:` internal id; Place keys on `qid`.

### Loaded counts
| Nodes | | Rels | |
|---|---|---|---|
| Person | 30,095 | HAS_EVENT | 189,918 |
| CareerEvent | 189,918 | EVENT_ROLE | 171,000 |
| Role | 32,330 | EVENT_ORG | 3,956 |
| Place | 1,571 | EVENT_PLACE | 138,766 |
| Organisation | 779 | EVENT_COLONY | 104,663 |
| Institution | 3,802 | RECEIVED | 14,420 |
| Honour | 1,507 | HOLDS_QUAL | 1,356 |
| Qualification | 95 | EDUCATED_AT | 14,505 |

## Querying

```python
import ladybug
conn = ladybug.Connection(ladybug.Database("data/kg/ladybug_db"))
df = conn.execute("MATCH (p:Person) RETURN count(p)").get_as_df()
```

Example Cypher:

```cypher
-- complete career statements (role + place + dated)
MATCH (e:CareerEvent)-[:EVENT_ROLE]->(r:Role), (e)-[:EVENT_PLACE]->(pl:Place)
WHERE e.year_start IS NOT NULL
RETURN count(e);                                  -- 121,160

-- KCMG recipients who held a governor role, by year
MATCH (p:Person)-[:RECEIVED]->(:Honour {id:'Q12177415'}),
      (p)-[:HAS_EVENT]->(e:CareerEvent)-[:EVENT_ROLE]->(r:Role)
WHERE r.label CONTAINS 'governor'
RETURN p.surname, r.label, e.year_start ORDER BY e.year_start;

-- where alumni of an institution served (institution -> place)
MATCH (p:Person)-[:EDUCATED_AT]->(i:Institution {label:'University of Oxford'}),
      (p)-[:HAS_EVENT]->(e:CareerEvent)-[:EVENT_PLACE]->(pl:Place)
RETURN pl.label, count(*) AS n ORDER BY n DESC LIMIT 10;

-- people who served at a specific employer organisation
MATCH (p:Person)-[:HAS_EVENT]->(e:CareerEvent)-[:EVENT_ORG]->(o:Organisation)
RETURN o.label, count(DISTINCT p) AS n ORDER BY n DESC LIMIT 10;
```

Notes:
- Place serves both `EVENT_PLACE` and `EVENT_COLONY` (both are place QIDs).
- `EVENT_ROLE` carries a `modifiers` string (e.g. "acting", "assistant"); the
  acting flag is also on the CareerEvent (`is_acting`).
- Rels are filtered to existing endpoints at load time (no dangling references).
