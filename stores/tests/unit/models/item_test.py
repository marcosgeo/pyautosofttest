from unittest import TestCase

from stores.models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel("New Item", 19.99)

        self.assertEqual(item.name, "New Item", "Name must be the same")

        self.assertEqual(item.price, 19.99, "Price should be the same")

    def test_item_json(self):
        item = ItemModel("New Item", 19.99)
        expected = {
            "name": "New Item",
            "price": 19.99
        }

        self.assertEqual(item.json(), expected, "The JSON export the the item is incorrect")