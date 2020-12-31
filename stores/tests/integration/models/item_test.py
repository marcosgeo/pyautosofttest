from stores.models.item import ItemModel
from stores.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel("New Item", 19.99)

            self.assertIsNone(ItemModel.find_by_name("New Item"),
                              f"Found an item with name {item.name}, but expected not to.")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name("New Item"),
                                 f"Not found an item with name '{item.name}', but this is expected!")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name("New Item"),
                              f"Failed to delete an item with name '{item.name}'.")
