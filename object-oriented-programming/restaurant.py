class Restaurant:
    total_restaurant = 0

    def __init__(self,name,cuisines):
        self.name = name
        self.cuisines = cuisines
        self.number_served = 0
        self.served_in_a_day = 0
        Restaurant.total_restaurant += 1

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisines.title()}.")

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

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisines):
        super().__init__(name, cuisines)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint', 'cookie dough']

    def display_flavors(self):
        print(f"{self.name.title()} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

restaurant = Restaurant("Quarto","Italian")
restaurant_2 = Restaurant("Dragon Palace","Chinese")
restaurant_3 = Restaurant("Ramen Bar","Japanese")
icecream_stand = IceCreamStand("Sweet Treats","Desserts")

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
icecream_stand.display_flavors()
icecream_stand.describe_restaurant()

