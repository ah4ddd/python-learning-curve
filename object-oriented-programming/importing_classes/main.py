from car import Car as Cat
import vehicle as vcat
from electric_car import ElectricCar as Ecat

my_car = Cat("Honda", "Civic", 2020)
my_bike = vcat.Motorcycle("Harley", "Sportster", 2019)
my_truck = vcat.Truck("Ford", "F-150", 2021)
my_tesla = Ecat("Tesla", "Model 3", 2023)

print(my_car.get_descriptive_name())
my_car.read_odometer(50)
my_car.drive(50)

print(my_car.get_descriptive_name())
print(my_bike.get_descriptive_name())
print(my_truck.get_descriptive_name())

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.charge()
