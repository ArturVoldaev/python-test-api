import requests
import unittest
from faker import Faker
from dotenv import load_dotenv
import os
import generate_body_for_store

class TestStoreApi(unittest.TestCase):

    fake = Faker()
    load_dotenv()

    def generate_data(self):
        data = generate_body_for_store.StoreBody(self.fake.random_int(min=1, max=9),
                                                 self.fake.unique.random_int(),
                                                 self.fake.unique.random_int(),
                                                 self.fake.pybool(),
                                                 "2023-08-06T13:01:17.336+0000").generate_data()
        return data
    def test_post_is_status_code_200(self):
        data = self.generate_data()
        self.assertEqual(self.store_post_req(data).status_code, requests.codes.ok)

    def test_get_is_order_created(self):
        data = self.generate_data()
        self.store_post_req(data)
        string_id = int(data.get("id"))
        self.assertEqual(self.store_get_req(data).status_code, requests.codes.ok)
        self.assertEqual(self.store_get_req(data).json().get("id"), string_id)


    def test_delete_order(self):
        data = self.generate_data()
        self.assertEqual(self.store_delete_req(data).status_code, requests.codes.ok)

    def store_post_req(self, data):
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_STORE")}/'
        store_post_request_add_a_new_order = requests.post(url, json=data)
        return store_post_request_add_a_new_order

    def store_get_req(self, data):
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_STORE")}/{data.get("id")}'
        store_get_request = requests.get(url)
        return store_get_request

    def store_delete_req(self, data):
        self.store_post_req(data)
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_STORE")}/{data.get("id")}'
        store_delete_req = requests.delete(url)
        return store_delete_req


if __name__ == '__main__':
    unittest.main()

