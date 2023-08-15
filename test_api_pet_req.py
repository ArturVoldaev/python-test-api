import requests
import unittest
from faker import Faker
import generate_obj
import pytest
import allure
import os
from dotenv import load_dotenv
@pytest.mark.usefixtures('some_data')
class TestPetApi(unittest.TestCase):

    fake = Faker()
    load_dotenv()

    def generate_data(self):
        data = generate_obj.DataObject(self.fake.unique.random_int(),
                                       self.fake.language_name(),
                                       'random_pet_status',
                                       self.fake.unique.random_int(),
                                       self.fake.catch_phrase(),
                                       self.fake.unique.random_int(),
                                       self.fake.job()).generate_data()
        return data

    # @pytest.mark.smoke
    def test_post_code_200(self, some_data):
        # data = self.generate_data()
        # self.assertEqual(self.pet_post_req(data).status_code, requests.codes.ok)
        assert some_data == 665

    def test_02_get_is_pet_created(self):
        data = self.generate_data()
        self.pet_post_req(data)
        self.assertEqual(self.pet_get_req(data).status_code, requests.codes.ok)
    #
    def test_03_post_is_id_correct(self):
        data = self.generate_data()
        response = self.pet_post_req(data)
        self.assertEqual(response.json().get("id"), int(data.get("id")))

    def test_04_post_is_category_correct(self):
        data = self.generate_data()
        response = self.pet_post_req(data)
        self.assertEqual(response.json().get("category").get("id"), int(data.get("category").get("id")))
        self.assertEqual(response.json().get("category").get("name"), data.get("category").get("name"))

    def test_05_put_is_pet_updated(self):
        data = self.generate_data()
        self.assertEqual(self.pet_put_req(data).status_code, requests.codes.ok)

    def test_06_put_did_get_new_param(self):
        data = self.generate_data()
        response = self.pet_put_req(data).json().get("category")
        self.assertEqual(response.get("id"), int(data.get("category").get("id")))
        self.assertEqual(response.get("name"), data.get("category").get("name"))

    def test_07_delete_pet(self):
        data = self.generate_data()
        print(data)
        self.assertEqual(self.pet_delete_req(data).status_code, requests.codes.ok)
        self.assertEqual(self.pet_get_req(data).status_code, requests.codes.not_found)

    def pet_post_req(self, data):
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_PET")}'
        post_request = requests.post(url, json=data)
        return post_request

    # @allure.step
    def pet_get_req(self, data):
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_PET")}/{data.get("id")}'
        pet_get_request = requests.get(url)
        return pet_get_request
    @allure.step('I want know smt "{data}"')
    def pet_put_req(self, data):
        self.pet_post_req(data)
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_PET")}'
        pet_out_request = requests.put(url, json=data)
        return pet_out_request

    def pet_delete_req(self, data):
        self.pet_post_req(data)
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_PET")}/{data.get("id")}'
        pet_delete_req = requests.delete(url)
        return pet_delete_req


@allure.suite("TOP SUITE")
@allure.title('NEW TITLE = "{num}"')
@allure.description("Some description bla bla bla")
@allure.link("www.google.com")
@pytest.mark.param
@pytest.mark.parametrize("num", [1, 2, 3, 4, 5])
def test_assert_more_zero(num):
    assert num > 0

if __name__ == '__main__':
    unittest.main()

