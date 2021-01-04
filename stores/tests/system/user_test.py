import json
from stores.models.user import UserModel
from stores.tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post("/register", data={"username": "new.user", "password": "xyz123"})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username("new.user"))
                self.assertDictEqual({"message": "User created successfully."},
                                     json.loads(response.data))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={"username": "new.user", "password": "xyz.123"})
                auth_resp = client.post("/auth",
                                        data=json.dumps({"username": "new.user", "password": "xyz.123"}),
                                        headers={"Content-Type": "application/json"})
                self.assertIn("access_token", json.loads(auth_resp.data).keys())

    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={"username": "user.name", "password": "123.xyz"})
                response = client.post("/register", data={"username": "user.name", "password": "123.xyz"})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({"message": "A user with that username already exists"},
                                     json.loads(response.data))
