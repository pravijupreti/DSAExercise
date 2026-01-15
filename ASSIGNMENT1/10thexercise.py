class User():
    def __init__(self,first_name,last_name,user_Name,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.user_Name = user_Name
        self.email = email
        self.location = location
    
    def describe_user(self):
        print(f"Name: {self.first_name + " " + self.last_name}\nUsername: {self.user_Name}\nEmail: {self.email}\nLocation: {self.location}")
    def greet_user(self):
        print(f"Welcome back {self.user_Name}!")

Matti= User('Matti', 'Paajanen', 'mpaajanen', 'm.paajanen@gmail.com', 'Helsinki')
Matti.describe_user()

Maila= User('Maila', 'Halonen', 'm_halonen', 'm.halonen@mtv.fi', 'Vaasa')
Maila.greet_user()