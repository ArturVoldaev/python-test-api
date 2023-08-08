import requests
from faker import Faker
from dotenv import load_dotenv
import os
import generate_body_for_user


class TestClass:
    fake = Faker()
    load_dotenv()

    def generate_data(self):
        data = generate_body_for_user.UserBody(
            self.fake.unique.random_int(),
            self.fake.first_name(),
            self.fake.first_name(),
            self.fake.last_name(),
            self.fake.ascii_email(),
            self.fake.password(length=12),
            self.fake.basic_phone_number(),
            self.fake.unique.random_int()).generate_data()
        return data

    def user_post_req(self, data):
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_USER")}'
        post_requests = requests.post(url, json=data)
        return post_requests

    def user_get_req(self):
        post_data = self.generate_data()
        self.user_post_req(post_data)
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_USER")}/{post_data.get("username")}'
        get_requests = requests.get(url)
        return get_requests

    def user_put_req(self, data):
        post_data = self.generate_data()
        self.user_post_req(post_data)
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_USER")}/{post_data.get("username")}'
        put_requests = requests.put(url, json=data)
        return put_requests

    def user_delete_req(self, data):
        post_data = data
        self.user_post_req(post_data)
        url = f'{os.getenv("DOMAIN")}/{os.getenv("END_POINT_USER")}/{post_data.get("username")}'
        delete_requests = requests.delete(url)
        return delete_requests

    def test_create_user(self):
        data = self.generate_data()
        assert self.user_post_req(data).status_code == requests.codes.ok

    def test_get_user(self):
        assert self.user_get_req().status_code == requests.codes.ok

    def test_put_user(self):
        data = self.generate_data()
        assert self.user_put_req(data).status_code == requests.codes.ok
        assert self.user_put_req(data).json().get('message') == data.get('id')
        assert self.user_put_req(data).json().get('code') == requests.codes.ok

    def test_delete_user(self):
        data = self.generate_data()
        assert self.user_delete_req(data).status_code == requests.codes.ok
        assert self.user_delete_req(data).json().get('code') == requests.codes.ok
        assert self.user_delete_req(data).json().get('message') == data.get('username')
