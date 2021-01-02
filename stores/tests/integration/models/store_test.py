from stores.tests.integration.integration_base_test import BaseTest

from stores.models.store import StoreModel
from stores.models.item import ItemModel


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel("New Store")

        self.assertListEqual(store.items.all(), [],
                             "The store's itmes length was not 0 even though no items were added.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel("New Store")
            self.assertIsNone(StoreModel.find_by_name("New Store"))
            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name("New Store"))
            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name("New Store"))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("New Store")
            item = ItemModel("New Item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, "New Item")

    def test_store_json(self):
        store = StoreModel("New Store")
        expected = {
            "name": "New Store",
            "items": []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel("New Store")
            item = ItemModel("New Item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                "name": "New Store",
                "items": [{"name": "New Item", "price": 19.99}]
            }

            self.assertDictEqual(store.json(), expected)
