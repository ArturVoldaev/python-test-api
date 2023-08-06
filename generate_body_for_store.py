class StoreBody:
    def __init__(self, random_pet_id,
                 random_id,
                 random_quantity,
                 random_complete,
                 random_data_stamp):
        self.random_pet_id = random_pet_id
        self.random_id = random_id
        self.random_quantity = random_quantity
        self.random_status = "placed"
        self.random_complete = random_complete
        self.random_data_stamp = random_data_stamp

    def generate_data(self):
        data = {
          "id": f"{self.random_pet_id}",
          "petId": f"{self.random_id}",
          "quantity": f"{self.random_quantity}",
          "shipDate": f"{self.random_data_stamp}",
          "status": f"{self.random_status}",
          "complete": f"{self.random_complete}"
        }

        return data