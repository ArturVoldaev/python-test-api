import requests
import unittest
from faker import Faker
import generate_obj


class TestApi(unittest.TestCase):

    fake = Faker()

    data_1 = generate_obj.DataObject(fake.unique.random_int(), fake.language_name(), 'random_pet_status', fake.unique.random_int(), fake.catch_phrase(), fake.unique.random_int(), fake.job())
    data_2 = generate_obj.DataObject(fake.unique.random_int(), fake.language_name(), 'random_pet_status', fake.unique.random_int(), fake.catch_phrase(), fake.unique.random_int(), fake.job())

    def test_01_post_is_status_code_200(self):
        self.assertEqual(self.pet_post_req(self.data_1.generate_data()).status_code, 200)

    def test_02_get_is_pet_created(self):
        self.assertEqual(self.pet_get_req().status_code, 200)

    def test_03_post_is_id_correct(self):
        response = self.pet_post_req(self.data_1.generate_data())
        self.assertEqual(response.json().get("id"), self.data_1.random_pet_id)

    def test_04_post_is_category_correct(self):
        response = self.pet_post_req(self.data_1.generate_data()).json().get("category")
        self.assertEqual(response.get("id"), self.data_1.random_category_id)
        self.assertEqual(response.get("name"), self.data_1.random_category_name)

    def test_05_put_is_pet_updated(self):
        self.assertEqual(self.pet_put_req(self.data_2.generate_data()).status_code, 200)

    def test_06_put_did_get_new_param(self):
        response = self.pet_put_req(self.data_2.generate_data()).json().get("category")
        self.assertEqual(response.get("id"), self.data_2.random_category_id)
        self.assertEqual(response.get("name"), self.data_2.random_category_name)

    def test_07_delete_pet(self):
        self.assertEqual(self.pet_delete_req().status_code, 200)

    def test_08_get_deleted_obj(self):
        self.assertEqual(self.pet_get_after_deleted().status_code, 404)

    def pet_post_req(self, data):
        pet_post_request_add_a_new_pet = requests.post('https://petstore.swagger.io/v2/pet', json=data)
        return pet_post_request_add_a_new_pet

    def pet_get_req(self):
        url = f'https://petstore.swagger.io/v2/pet/{self.data_1.random_pet_id}'
        pet_get_request = requests.get(url)
        return pet_get_request

    def pet_put_req(self, data):
        pet_out_request = requests.put('https://petstore.swagger.io/v2/pet/', json=data)
        return pet_out_request

    def pet_delete_req(self):
        url = f'https://petstore.swagger.io/v2/pet/{self.data_2.random_pet_id}'
        pet_delete_req = requests.delete(url)
        return pet_delete_req

    def pet_get_after_deleted(self):
        url = f'https://petstore.swagger.io/v2/pet/{self.data_2.random_pet_id}'
        pet_get_request = requests.get(url)
        return pet_get_request


if __name__ == '__main__':
    unittest.main()

