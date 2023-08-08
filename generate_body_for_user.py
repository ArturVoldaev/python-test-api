class UserBody:
    def __init__(self, random_user_id,
                 random_user_name,
                 random_user_first_name,
                 random_user_last_name,
                 random_user_email,
                 random_user_password,
                 random_user_phone,
                 random_user_status):
        self.random_user_id = random_user_id
        self.random_user_name = random_user_name
        self.random_user_first_name = random_user_first_name
        self.random_user_password = random_user_password
        self.random_user_last_name = random_user_last_name
        self.random_user_email = random_user_email

        self.random_user_phone = random_user_phone
        self.random_user_status = random_user_status

    def generate_data(self):
        data = {
          "id": f"{self.random_user_id}",
          "username": f"{self.random_user_name}",
          "firstName": f"{self.random_user_first_name}",
          "lastName": f"{self.random_user_last_name}",
          "email": f"{self.random_user_email}",
          "password": f"{self.random_user_password}",
          "phone": f"{self.random_user_phone}",
          "userStatus": f"{self.random_user_status}",
        }

        return data