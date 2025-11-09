class Restaurant:
    def __init__(self,name,cuisines):
        self.name = name
        self.cuisines = cuisines

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisines} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open 7 days a week, from 10 AM to 9 PM.")

restaurant = Restaurant("Quarto","Italian")
restaurant_2 = Restaurant("Dragon Palace","Chinese")
restaurant_3 = Restaurant("Ramen Bar","Japanese")

print(f"{restaurant.name} serves pretty good {restaurant.cuisines} food.\n")

restaurant.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

restaurant.open_restaurant()

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}")

    def describe_user(self):
        print(f"The full name of user is {self.first_name.title()} {self.last_name.title()}")
        print(f"The first name of user is {self.first_name.title()}")
        print(f"The last name of user is {self.last_name.title()}")

user = User("Ahad","Umayyad")
user2 = User("Siya", "Lily")
user3 = User("Xi", "wei")


user.greet_user()
user2.greet_user()
user3.greet_user()

user.describe_user()
user2.describe_user()
user3.describe_user()
