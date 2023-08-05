from faker import Faker


class DataObject:

    def __init__(self, random_pet_id, random_pet_name, random_pet_status, random_tags_id, random_tags_name,
                 random_category_id, random_category_name):
        self.random_pet_id = random_pet_id
        self.random_pet_name = random_pet_name
        self.random_pet_status = "avalable"
        self.random_pet_status = random_pet_status
        self.random_tags_id = random_tags_id
        self.random_tags_name = random_tags_name
        self.random_category_id = random_category_id
        self.random_category_name = random_category_name

    def generate_data(self):
        data = {
            "id": f"{self.random_pet_id}",
            "category": {
                "id": f"{self.random_category_id}",
                "name": f"{self.random_category_name}"
            },
            "name": f"{self.random_pet_name}",
            "photoUrls": ["string"],
            "tags": [{"id": f"{self.random_tags_id}", "name": f"{self.random_tags_name}"}],
            "status": f"{self.random_pet_status}"
        }

        return data