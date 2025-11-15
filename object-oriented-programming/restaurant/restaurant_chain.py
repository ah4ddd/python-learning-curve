from restaurant import Restaurant
from ice_cream_stand import IceCreamStand

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
