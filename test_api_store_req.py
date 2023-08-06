import requests
import unittest
from faker import Faker
import generate_body_for_store


class TestStoreApi(unittest.TestCase):

    fake = Faker()

    data_1 = generate_body_for_store.StoreBody(fake.random_digit_not_null(), fake.unique.random_int(), fake.unique.random_int(), fake.pybool(), fake.iso8601())

    def test_01_post_is_status_code_200(self):
        self.assertEqual(self.store_post_req(self.data_1.generate_data()).status_code, 200)

    def test_02_get_is_order_created(self):
        self.assertEqual(self.store_get_req().status_code, 200)

    def test_03_delete_order(self):
        self.assertEqual(self.store_delete_req().status_code, 200)

    def test_04_get_deleted_order(self):
        self.assertEqual(self.store_get_req().status_code, 404)

    def store_post_req(self, data):
        store_post_request_add_a_new_order = requests.post('https://petstore.swagger.io/v2/store/order', json=data)
        return store_post_request_add_a_new_order

    def store_get_req(self):
        url = f'https://petstore.swagger.io/v2/store/order/{self.data_1.random_pet_id}'
        store_get_request = requests.get(url)
        return store_get_request

    def store_delete_req(self):
        url = f'https://petstore.swagger.io/v2/store/order/{self.data_1.random_pet_id}'
        store_delete_req = requests.delete(url)
        return store_delete_req


if __name__ == '__main__':
    unittest.main()

