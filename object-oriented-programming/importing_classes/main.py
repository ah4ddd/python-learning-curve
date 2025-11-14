from car import Car
from vehicle import Motorcycle, Truck

my_car = Car("Honda", "Civic", 2020)
my_bike = Motorcycle("Harley", "Sportster", 2019)
my_truck = Truck("Ford", "F-150", 2021)

print(my_car.get_descriptive_name())
my_car.read_odometer(50)
my_car.drive(50)


print(my_car.get_descriptive_name())
print(my_bike.get_descriptive_name())
print(my_truck.get_descriptive_name())
