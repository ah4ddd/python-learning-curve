class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}")

    def describe_user(self):
        print(f"The full name of user is {self.first_name.title()} {self.last_name.title()}")
        print(f"The first name of user is {self.first_name.title()}")
        print(f"The last name of user is {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Current {self.first_name} login attempts : {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts reset for {self.first_name} to {self.login_attempts}")



