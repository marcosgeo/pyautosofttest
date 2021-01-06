import json
from stores.tests.base_test import BaseTest
from stores.models.user import UserModel
from stores.models.item import ItemModel
from stores.models.store import StoreModel


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel("new.user", "pw.1234").save_to_db()
                auth_request = client.post("/auth",
                                           data=json.dumps({"username": "new.user", "password": "pw.1234"}),
                                           headers={"Content-Type": "application/json"})
                auth_token = json.loads(auth_request.data)["access_token"]
                self.access_token = f"JWT {auth_token}"

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get("/item/test")
                self.assertEqual(resp.status_code, 401)

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                header = {"Authentication": self.access_token}

                resp = client.get("/item/test", headers=header)
                self.assertEqual(resp.status_code, 401)

    def test_get_existing_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("New Store").save_to_db()
                ItemModel("New Item", 9.99, 1).save_to_db()
                resp = client.get("/item/New Item", headers={"Authorization": self.access_token})
                self.assertEqual(resp.status_code, 200)
 
    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("NewStore").save_to_db()
                ItemModel("NewItem", 9.99, 1).save_to_db()

                resp = client.delete("/item/NewItem", headers={"Authorization": self.access_token})
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"message": "Item deleted"}, json.loads(resp.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("NewStore").save_to_db()

                resp = client.post("/item/NewItem", data={"price": 9.99, "store_id": 1},
                                   headers={"Authorization": self.access_token})

                self.assertEqual(resp.status_code, 201)
                self.assertDictEqual({"name": "NewItem", "price": 9.99},
                                     json.loads(resp.data))

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("NewStore").save_to_db()
                ItemModel("NewItem", 9.99, 1).save_to_db()

                resp = client.post("/item/NewItem", data={"price": 9.99, "store_id": 1},
                                   headers={"Authorization": self.access_token})

                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({"message": "An item with name 'NewItem' already exists."},
                                     json.loads(resp.data))

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("NewStore").save_to_db()

                resp = client.put("/item/NewItem", data={"price": 9.99, "store_id": 1},
                                  headers={"Authorization": self.access_token})

                self.assertEqual(resp.status_code, 200)
                self.assertEqual(ItemModel.find_by_name("NewItem").price, 9.99)
                self.assertDictEqual({"name": "NewItem", "price": 9.99},
                                     json.loads(resp.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("NewStore").save_to_db()
                ItemModel("ExistingItem", 9.99, 1).save_to_db()

                self.assertEqual(ItemModel.find_by_name("ExistingItem").price, 9.99)

                resp = client.put("/item/ExistingItem", data={"price": 13.97, "store_id": 1},
                                  headers={"Authorization": self.access_token})

                self.assertEqual(resp.status_code, 200)
                self.assertEqual(ItemModel.find_by_name("ExistingItem").price, 13.97)
                self.assertDictEqual({"name": "ExistingItem", "price":13.97},
                                     json.loads(resp.data))


    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("NewStore").save_to_db()
                ItemModel("NewItem", 8.99, 1).save_to_db()

                resp = client.get("/items")

                self.assertDictEqual({"items": [{"name": "NewItem", "price": 8.99}]},
                                     json.loads(resp.data))

