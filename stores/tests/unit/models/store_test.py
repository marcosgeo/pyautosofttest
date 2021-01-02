from stores.models.store import StoreModel
from stores.tests.unit.unit_base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel("New Store")

        self.assertEqual(store.name, "New Store", "The name of the store should be the same.")