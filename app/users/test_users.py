import unittest
import requests
from app.settings import API_URL
from app.settings import TEST_API_TOKEN


class UsersTest(unittest.TestCase):
    # USERS_API_URL = "{}/users".format(API_URL)

    def test_get_all_users(self):
        # Make request to the users api endpoint
        r = requests.get(
            "{}/users".format(API_URL), 
            headers={'Authorization': TEST_API_TOKEN}
        )
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()