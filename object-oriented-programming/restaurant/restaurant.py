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
