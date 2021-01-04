from stores.models.user import UserModel
from stores.tests.integration.integration_base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel("User Name", "user password")

            self.assertIsNone(UserModel.find_by_username("User Name"))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username("User Name"))
            self.assertIsNotNone(UserModel.find_by_id(1))
