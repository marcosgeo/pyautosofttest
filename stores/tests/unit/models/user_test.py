from stores.models.user import UserModel
from stores.tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel("New User", "user password")

        self.assertEqual(user.username, "New User")
        self.assertEqual(user.password, "user password")
