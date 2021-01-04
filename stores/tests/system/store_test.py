import json

from stores.models.item import ItemModel
from stores.models.store import StoreModel
from stores.tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post("/store/novissima")

                self.assertEqual(resp.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name("novissima"))
                self.assertDictEqual({"name": "novissima", "items": []},
                                     json.loads(resp.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post("/store/store1")
                resp = client.post("/store/store1")

                self.assertEqual(resp.status_code, 404)

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("NewStore").save_to_db()
                resp = client.delete("/store/NewStore")

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"message": "Store deleted"},
                                     json.loads(resp.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("ExistingStore").save_to_db()
                resp = client.get("/store/ExistingStore")

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"name": "ExistingStore", "items": []},
                                     json.loads(resp.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get("/store/ExistingStore")

                self.assertEqual(resp.status_code, 404)
                self.assertDictEqual({"message": "Store not found"},
                                     json.loads(resp.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("ExistingStore").save_to_db()
                ItemModel("NewItem", 19.99, 1).save_to_db()

                resp = client.get("/store/ExistingStore")
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"name": "ExistingStore", "items": [{"name": "NewItem", "price": 19.99}]},
                                     json.loads(resp.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("StoreOne").save_to_db()
                StoreModel("StoreTwo").save_to_db()

                resp = client.get("/stores")
                self.assertDictEqual({"stores": [{"name": "StoreOne", "items": []},
                                     {"name": "StoreTwo", "items": []}]},
                                     json.loads(resp.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Store_A").save_to_db()
                StoreModel("Store_B").save_to_db()
                ItemModel("Item_1A", 19.99, 1).save_to_db()
                ItemModel("Item_2A", 9.99, 1).save_to_db()
                ItemModel("Item_1B", 35.89, 2).save_to_db()

                resp = client.get("/stores")
                self.assertDictEqual(
                    {"stores": [
                        {"name": "Store_A", "items": [
                            {"name": "Item_1A", "price": 19.99},
                            {"name": "Item_2A", "price": 9.99}
                        ]},
                        {"name": "Store_B", "items": [
                            {"name": "Item_1B", "price": 35.89}
                        ]}
                    ]},
                    json.loads(resp.data)
                )
