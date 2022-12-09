from unittest import TestCase
from helpers.wikidata_helper import find_wikidata_id
from helpers.wikidata_helper import query_entity_links
from helpers.wikidata_helper import read_linked_entities



class Test(TestCase):
    def test_find_wikidata_id(self):
        name = "Godfather"
        entity_id = find_wikidata_id(name)
        self.assertNotEqual(entity_id, "entityNotFound")

    def test_find_wikidata_id_wrong(self):
        name = "fhmslqdfhsmlfjb"
        entity_id = find_wikidata_id(name)
        self.assertEqual(entity_id, "entityNotFound")

    def test_query_entity_links(self):
        name = "Godfather"
        entity_id = find_wikidata_id(name)
        json_links = query_entity_links(entity_id)
        self.assertIsNotNone(json_links)

    def test_read_link_entities(self):
        name = "Godfather"
        entity_id = find_wikidata_id(name)
        json_links = query_entity_links(entity_id)
        related_links = read_linked_entities(json_links)
        self.assertIsNotNone(related_links)
