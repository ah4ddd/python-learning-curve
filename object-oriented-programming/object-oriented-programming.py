class Restaurant:
    total_restaurant = 0

    def __init__(self,name,cuisines):
        self.name = name
        self.cuisines = cuisines
        self.number_served = 0
        self.served_in_a_day = 0
        Restaurant.total_restaurant += 1

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisines.title()} cuisine.")

    def open_restaurant(self):
        print(f"{self.name.title()} is open 7 days a week, from 10 AM to 9 PM.")

    def take_reservation(self, name, people):
        print(f"✅ Reservation for {people} people under {name.title()} at {self.name.title()}")

    def rate_restaurant(self, rating):
        print(f"⭐ {self.name.title()} rated {rating}/5 stars!")

    def customer_served(self,served):
        self.number_served += served
        print(f"{self.name.title()} has served {self.number_served} customers")

    def increment_customer_served(self,served,day):
        self.served_in_a_day += served
        print(f"{self.name.title()} has served {self.served_in_a_day} customers on a {day.title()}")

restaurant = Restaurant("Quarto","Italian")
restaurant_2 = Restaurant("Dragon Palace","Chinese")
restaurant_3 = Restaurant("Ramen Bar","Japanese")

print(f"Total {Restaurant.total_restaurant} choices  : {restaurant.name} | {restaurant.cuisines} | {restaurant_2.name} {restaurant_2.cuisines} | {restaurant_3.name} {restaurant_3.cuisines}")

print(f"{restaurant.name} serves pretty good {restaurant.cuisines} food.\n")

restaurant.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

restaurant.take_reservation("Ahad",2)
restaurant_3.rate_restaurant(4.9)
restaurant.customer_served(32)
restaurant_2.increment_customer_served(55,"friday")
restaurant.open_restaurant()

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

user = User("Ahad","Umayyad")
user2 = User("Siya", "Lily")
user3 = User("Xi", "wei")

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
