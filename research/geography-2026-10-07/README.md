# Historical geography repairs, 7 October 2026

The Wodehouse example exposed errors in the graph, the atlas's missing-place fallback, and its choice of capital. This repair checks both the Colonial Office and India Office corpora: **305,164 career events**. It also repairs the known Brewster defeat error and checks explicit defeat events elsewhere.

## Verified corrections

| Finding | Repair |
|---|---|
| Wodehouse's 1858 Venezuela mission was displayed in South Africa | Keep the explicit Venezuela place. Repair the ungrounded India Office version and its incorrect role label too. |
| Wodehouse's 1861 high commissionership used the Union of South Africa | Use the Cape appointment and Cape Town administrative seat. |
| His 1851 Honduras posting used Belmopan, or inherited British Guiana | Both records use British Honduras and the Belize City seat. |
| 1,120 events used the Union before 1910: 1,062 CO and 58 IO | Remove the invalid jurisdiction. 801 already have another grounded place and retain it; Wodehouse is resolved to the Cape. The remaining 318 broad references stay unresolved, with the source place string visible. |
| 1,462 dated events already grounded to British Honduras predate Belmopan; the repaired IO event adds one | Use Belize City before 1970. |
| 15,470 India events before 1911 used the later Delhi coordinate | Use Calcutta before 1911 and Delhi after 1911. The year-only 1911 transition is a regional point. Pre-1858 map labels say Company period rather than British Raj. |
| Capital selection ignored dates and selected the first of several P36 values | Use dated capital statements. Multiple eligible capitals get a labelled regional point, as do capitals that did not yet exist. Administrative seats remain approximate map references, not claims of exact workplaces. |
| 3,955 records had an explicit grounded place but no colony | Use the explicit place rather than borrowing a different career posting. Missing locations remain in the register; they break routes. |
| Brewster's defeat became a 1912–1916 office held | Preserve an electoral-defeat event, remove its held-role edge and invented end date. |
| Eleven other events explicitly describe electoral defeat | Apply the same event-type correction. Do not classify military victories or resignations by a loose `defeat` substring. |

Equal roles recorded years apart are no longer merged into an assumed continuous tenure. Officials without a mapped posting remain searchable. Dated plotting nodes retain the underlying entity identifier separately from the map key.

## Evidence

- The saved Colonial Office and India Office biographies and graph records supply Wodehouse's mission, Honduras appointment, and Cape service. The workshop preserves the [1867 entry](https://jimclifford.ca/imperial-careers-workshop/steps/01-atlas.html) and [Brewster source](https://github.com/jburnford/imperial-careers-workshop/blob/main/outputs/ground/brewster.json).
- [Wodehouse's letter from Government House, Cape Town, 18 December 1863](https://history.state.gov/historicaldocuments/frus1864p1/d108), US State Department, corroborates his Cape administrative location.
- [Belmopan City Council history](https://belmopancitycouncil.org/welcome/our-history/) describes the move from Belize City and completion of Belmopan's first phase in 1970. This overrides Wikidata's inconsistent 1971 capital qualifier.
- [Hansard, 12 December 1911](https://api.parliament.uk/historic-hansard/commons/1911/dec/12/removal-from-calcutta-to-delhi) records the announcement transferring the seat from Calcutta to Delhi. Year-only data cannot resolve the transition within 1911.
- [South African government yearbook, History](https://www.gcis.gov.za/sites/default/files/docs/resourcecentre/yearbook/2010/History.pdf) dates Union to 31 May 1910. Year-only records retain 1910 as a boundary year.
- `wikidata.json` is the 7 October `wbgetentities` evidence cache: 2,504 identifiers, English labels, coordinates, inception/dissolution and capital statements including qualifiers and references. Normal builds use this snapshot offline.

## Audit limits and review queue

`baseline-counts.json` and `baseline-corrections.json` preserve the pre-repair screen and reviewed row changes. `current-counts.json` and `current-corrections.json` describe the rebuilt graph. Counts refer to event rows, not unique people. The two copies of a corrected event in spine and facts are not counted twice.

The broad inception/dissolution screen leaves **21,723 candidates**, listed in `current-temporal-review.tsv`. These are **not 21,723 verified errors**. Names can persist across changes of legal status; Wikidata dates can be incomplete or wrong, and some old place identifiers are being used as geographic proxies. For example, the United Provinces item has an implausibly narrow date interval, while Singapore's Crown Colony identifier starts long after earlier Singapore postings. These require comparison with the source and period-specific entities; this release does not claim to have adjudicated them all. No automatic mass replacement is made from an inception date alone.

`defeat-source-review.json` contains 192 distinct candidate clauses in the available CO biographies, including resignations, military actions, references to another person's defeat, and OCR variants. It is a source-review queue, not a list of 192 misclassified appointments. The eleven explicitly classified defeats and Brewster were repaired; the wider source screen has not been fully adjudicated. The raw IOL biography directory was not available in this checkout; its complete structured event corpus was checked.

Historical video exports remain snapshots of their original builds. The interactive atlas and the public JSON are rebuilt here. The workshop identifies its opening video as an earlier overview and its error screenshots as before views.

## Reproduction and checks

```sh
python3 build_static_atlas.py
python3 audit_historical_geography.py
python3 -m unittest discover -s tests -p 'test_historical_geography.py' -v
python3 -m unittest discover -s tests -p 'test_atlas_artifacts.py' -v
```

`kg_apply_historical_fixups.py` runs in both the standard graph re-emit and the atlas build. It is idempotent, retains raw source strings, and updates spine, facts and role edges together. The build uses the same place projection for routes and career panels. The tests cover all published stints and arc endpoints, dated seats, both Wodehouse records, Brewster, missing locations, and tour references. Browser checks cover both Wodehouse panels, Brewster, an entirely unplaced career, tours, and mobile layout.

To refresh external evidence explicitly: `python3 refresh_atlas_geography.py`. Review changes to the cached claims before publishing a new build.
