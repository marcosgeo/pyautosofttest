from stores.models.item import ItemModel
from stores.models.store import StoreModel
from stores.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel("New Store").save_to_db()
            item = ItemModel("New Item", 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name("New Item"),
                              f"Found an item with name {item.name}, but expected not to.")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name("New Item"),
                                 f"Not found an item with name '{item.name}', but this is expected!")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name("New Item"),
                              f"Failed to delete an item with name '{item.name}'.")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("New Store")
            item = ItemModel("New Item", 45.66, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, "New Store")
