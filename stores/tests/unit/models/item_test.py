from stores.tests.unit.unit_base_test import UnitBaseTest

from stores.models.item import ItemModel


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel("New Item", 19.99, 1)

        self.assertEqual(item.name, "New Item", "Name must be the same")
        self.assertEqual(item.price, 19.99, "Price should be the same")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel("New Item", 19.99, 1)
        expected = {
            "name": "New Item",
            "price": 19.99
        }

        self.assertEqual(item.json(), expected, "The JSON export the the item is incorrect")