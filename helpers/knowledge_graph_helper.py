from helpers.wikidata_helper import find_wikidata_id
from helpers.wikidata_helper import query_entity_links
from helpers.wikidata_helper import read_linked_entities

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(names):
    results_list = []
    for idx, name in enumerate(names):
        # first get the wikipedia entity_id for each name
        entity_id = find_wikidata_id(name)
        if entity_id == "entityNotFound":
            continue

        # next we query wikipedia to get entity links
        json_links = query_entity_links(entity_id)

        # the following function extracts entities from the links
        related_links = read_linked_entities(json_links)

        # now we can construct an connection in our graph between two entities
        for related_entity, related_name in related_links:
            result = dict(
                name=name,
                original_entity=entity_id,
                linked_entities=related_entity,
                name_linked_entities=related_name,
            )
            results_list.append(result)

    results_list = pd.DataFrame(results_list)
    graph = nx.from_pandas_edgelist(results_list, 'original_entity', 'linked_entities')
    target_names = results_list[["linked_entities", "name_linked_entities"]].drop_duplicates().rename(
        columns={"linked_entities": "labels", "name_linked_entities": "name"})
    source_names = results_list[["original_entity", "name"]].drop_duplicates().rename(
        columns={"original_entity": "labels"})
    names = pd.concat([target_names, source_names])
    names = names.set_index("labels")
    names = names.to_dict()["name"]
    plt.figure(figsize=(20, 20))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, node_size=60, font_size=9, width=0.2)
    nx.draw_networkx_labels(graph, pos, names, font_size=12)
    plt.show()