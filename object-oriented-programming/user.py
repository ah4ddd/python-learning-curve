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

class Privileges:
    def __init__(self):
        self.privileges = [
            "Can Post",
            "Can ban users",
            "Can delete post",
            "Can Manage messages",
            "Can managage users",
            "Can access admin panel"
            ]
    def show_privileges(self):
        print(f"{"-"*5}Admin Priviledges{"-"*5}\n")
        for admin in self.privileges:
            print(f"{admin}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

user = User("Ahad","Umayyad")
user2 = User("Siya", "Lily")
user3 = User("Xi", "wei")
admin = Admin("Super", "Admin")

user.greet_user()
user2.greet_user()
user3.greet_user()

user.describe_user()
user2.describe_user()
user3.describe_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()

user.increment_login_attempts()

admin.privileges.show_privileges()
admin.describe_user()
