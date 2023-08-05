import requests
import unittest
import time
from faker import Faker


class TestApi(unittest.TestCase):

    fake = Faker()

    random_pet_id = fake.unique.random_int()
    random_pet_name = fake.language_name()
    random_pet_status = "available"

    random_tags_id = fake.unique.random_int()
    random_tags_name = fake.catch_phrase()

    random_category_id = fake.unique.random_int()
    random_category_name = fake.job()

    data = {
        "id": f"{random_pet_id}",
        "category": {
            "id": f"{random_category_id}",
            "name": f"{random_category_name}"
        },
        "name": f"{random_pet_name}",
        "photoUrls": ["string"],
        "tags": [{"id": f"{random_tags_id}", "name": f"{random_tags_name}"}],
        "status": f"{random_pet_status}"
    }

    print("Data type")
    print(type(data))







    def test_post_is_id_correct(self):
        response = self.pet_post_req(self.data)
        self.assertEqual(response.json().get("id"), self.random_pet_id)

    #
    # def test_post_is_category_correct(self):
    #     response = self.pet_post_req(self.data).json().get("category")
    #     self.assertEqual(response.get("id"), self.random_category_id)
    #     self.assertEqual(response.get("name"), self.random_category_name)



    def pet_post_req(self, data):
        pet_post_request_add_a_new_pet = requests.post('https://petstore.swagger.io/v2/pet', json=data)
        print(self.data)
        return pet_post_request_add_a_new_pet

    def test_post_is_status_code_200(self):
        self.assertEqual(self.pet_post_req(self.data).status_code, 200)

    def test_get_is_pet_created(self):
        self.assertEqual(self.pet_get_req().status_code, 200)

    def pet_get_req(self):
        time.sleep(5)
        url = f'https://petstore.swagger.io/v2/pet/{self.random_pet_id}'
        pet_get_request = requests.get(url)
        print("my url " + url)
        print(f"my id in json id {self.random_pet_id}")
        print("Type of id")
        print(type(self.random_pet_id))
        print("Type of url")
        print(type(url))
        return pet_get_request

    # def pet_put_req(self, data):
    #     pet_out_request = requests.put('https://petstore.swagger.io/v2/pet/', json=data)
    #     return pet_out_request


if __name__ == '__main__':
    unittest.main()

